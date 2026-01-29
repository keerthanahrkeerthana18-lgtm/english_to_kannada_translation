# English to Kannada Translator 🌐

A full-stack web application that translates English text to Kannada with audio playback support. Built with Flask, Google Translate API, and Google Text-to-Speech.

## Features

✨ **Real-time Translation** — Translates English text to Kannada using Google Translate API  
🔊 **Audio Playback** — Listen to Kannada pronunciation with built-in audio player  
📱 **Responsive Design** — Works seamlessly on desktop, tablet, and mobile devices  
⚡ **Fallback Dictionary** — Graceful fallback for offline translation  
🎨 **Modern UI** — Clean and intuitive interface with gradient design  

## Project Structure

```
english_to_kannada_translation/
├── translator.py           # Main Flask app & translation logic
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── static/
│   └── style.css          # CSS styling
└── templates/
    └── index.html         # HTML template
```

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Setup

1. Clone or download the project:
```bash
cd english_to_kannada_translation
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Web App (Default)

Run the Flask web server:
```bash
python translator.py
```

Then open your browser and navigate to:
```
http://127.0.0.1:5000
```

### CLI Mode

Use the command-line interface:
```bash
# Single text translation
python translator.py --cli "Hello, how are you?"

# Translate from file
python translator.py --cli --file input.txt

# Interactive mode (if no text provided)
python translator.py --cli
```

### Custom Server Settings

```bash
# Run on different host/port
python translator.py --host 0.0.0.0 --port 8080
```

## Dependencies

- **Flask** — Web framework for the application
- **googletrans** — Google Translate API wrapper
- **gTTS** — Google Text-to-Speech engine

See `requirements.txt` for specific versions.

## How It Works

1. **User Input** → User enters English text in the web UI
2. **Translation** → Text is translated using Google Translate API (with fallback dictionary)
3. **Display** → Translated Kannada text is displayed
4. **Audio** → gTTS generates Kannada speech audio on-demand

## Fallback Dictionary

When Google Translate is unavailable, the app uses a built-in dictionary with common English-Kannada word mappings. Unknown words are marked with brackets `[word]`.

Example fallback translations:
- hello → ಹೆಲೋ
- world → ಪ್ರಪಂಚ
- thank you → ಧನ್ಯವಾದಗಳು

## Browser Support

- Chrome/Edge 90+
- Firefox 88+
- Safari 14+
- Mobile browsers (iOS Safari, Chrome Mobile)

## Troubleshooting

**Translation not working?**
- Check your internet connection (required for Google Translate)
- The app will fall back to the dictionary if the API fails

**Audio not playing?**
- Ensure JavaScript is enabled
- Check browser audio permissions
- Try a different browser

**Port already in use?**
```bash
python translator.py --port 5001
```

## License

This project is open source and available for personal and educational use.

## Future Enhancements

- [ ] Reverse translation (Kannada → English)
- [ ] Multiple language support
- [ ] Translation history
- [ ] Offline mode with local models
- [ ] API endpoint for programmatic access
