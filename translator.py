"""English → Kannada translator.

This file provides both a small CLI fallback and a Flask web application.
The web app uses `googletrans` for translation (when available) and `gTTS`
to produce Kannada audio that the browser can play.

Run web server:
  python translator.py

Run CLI mode (original behaviour):
  python translator.py --cli "Hello"
"""

from typing import Optional
import re
import io
import urllib.parse
from pathlib import Path

try:
    from googletrans import Translator
    _GT_AVAILABLE = True
    _GT = Translator()
except Exception:
    _GT_AVAILABLE = False
    _GT = None

FALLBACK_DICT = {
    'hello': 'ಹೆಲೋ',
    'hi': 'ಹೈ',
    'world': 'ಪ್ರಪಂಚ',
    'how': 'ಹೇಗೆ',
    'are': 'ಇರಿ',
    'you': 'ನೀವು',
    'i': 'ನಾನು',
    'am': 'ಆಗಿದ್ದೇನೆ',
    'good': 'ಒಳ್ಳೆಯ',
    'morning': 'ಶುಭೋದಯ',
    'night': 'ರಾತ್ರಿ',
    'thanks': 'ಧನ್ಯವಾದಗಳು',
    'thank': 'ಧನ್ಯವಾದಗಳು'
}

def _preserve_punct(original: str, translated: str) -> str:
    m = re.match(r"^(\W*)(.*?)(\W*)$", original)
    if not m:
        return translated
    pre, core, post = m.group(1), m.group(2), m.group(3)
    return pre + translated + post


def translate_text(text: str) -> str:
    """Translate English `text` to Kannada.

    Uses `googletrans` when available; falls back to a word-by-word dictionary.
    """
    if not text:
        return ''
    if _GT_AVAILABLE and _GT is not None:
        try:
            res = _GT.translate(text, dest='kn')
            return res.text
        except Exception:
            pass

    words = re.split(r"(\s+)", text)
    out = []
    for token in words:
        if token.strip() == '':
            out.append(token)
            continue
        core = token
        core_stripped = re.sub(r"^\W+|\W+$", "", core)
        key = core_stripped.lower()
        translated = FALLBACK_DICT.get(key)
        if translated:
            translated = _preserve_punct(core, translated)
            out.append(translated)
        else:
            out.append(_preserve_punct(core, f"[{core_stripped}]"))
    return ''.join(out)


# --- Web app -------------------------------------------------
from flask import Flask, render_template, request, send_file, url_for
from gtts import gTTS

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    src_text = ''
    translation = ''
    if request.method == 'POST':
        src_text = request.form.get('text', '').strip()
        if src_text:
            translation = translate_text(src_text)
    return render_template('index.html', src_text=src_text, translation=translation)


@app.route('/tts')
def tts():
    """Return Kannada TTS audio for the provided `text` query parameter."""
    text = request.args.get('text', '')
    lang = request.args.get('lang', 'kn')
    if not text:
        return ('', 204)
    tts = gTTS(text=text, lang=lang)
    mp3_fp = io.BytesIO()
    tts.write_to_fp(mp3_fp)
    mp3_fp.seek(0)
    return send_file(mp3_fp, mimetype='audio/mpeg', as_attachment=False, download_name='speech.mp3')


def run_cli_mode(argv: Optional[list] = None) -> None:
    import argparse
    parser = argparse.ArgumentParser(description='English to Kannada translator (CLI)')
    parser.add_argument('text', nargs='*', help='Text to translate (if omitted, reads stdin)')
    parser.add_argument('-f', '--file', help='Path to text file to translate')
    args = parser.parse_args(argv)

    if args.file:
        p = Path(args.file)
        if p.exists():
            print(translate_text(p.read_text(encoding='utf-8')))
        else:
            print(f'File not found: {args.file}')
    elif args.text:
        input_text = ' '.join(args.text)
        print(translate_text(input_text))
    else:
        try:
            s = input('Enter text to translate: ').strip()
        except EOFError:
            s = ''
        if s:
            print(translate_text(s))


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('--cli', action='store_true', help='Run in CLI mode instead of starting the web server')
    parser.add_argument('--host', default='127.0.0.1', help='Host for web server')
    parser.add_argument('--port', default=5000, type=int, help='Port for web server')
    args, remaining = parser.parse_known_args()
    if args.cli:
        run_cli_mode(remaining)
    else:
        app.run(host=args.host, port=args.port, debug=True)
