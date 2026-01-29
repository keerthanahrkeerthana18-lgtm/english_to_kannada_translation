"""
Index and Entry Point for English to Kannada Translator
"""

from translator import app, translate_text

# Route Index/Documentation
ROUTES = {
    '/': {
        'method': 'GET, POST',
        'description': 'Main translator interface',
        'example': 'POST /  [form data: text=...]'
    },
    '/tts': {
        'method': 'GET',
        'description': 'Text-to-Speech audio stream',
        'params': {
            'text': 'Kannada text to convert to speech',
            'lang': 'Language code (default: kn for Kannada)'
        },
        'example': 'GET /tts?text=ಹೆಲೋ'
    }
}

def print_index():
    """Print available routes and usage information."""
    print("\n" + "="*60)
    print("  English to Kannada Translator - Route Index")
    print("="*60 + "\n")
    
    for route, info in ROUTES.items():
        print(f"📍 Route: {route}")
        print(f"   Method: {info['method']}")
        print(f"   Description: {info['description']}")
        
        if 'params' in info:
            print("   Parameters:")
            for param, desc in info['params'].items():
                print(f"     - {param}: {desc}")
        
        print(f"   Example: {info['example']}\n")
    
    print("="*60)
    print("  Quick Start")
    print("="*60)
    print("\n1. Run the web app:")
    print("   python translator.py")
    print("\n2. Open in browser:")
    print("   http://127.0.0.1:5000")
    print("\n3. Or use CLI mode:")
    print("   python translator.py --cli \"Hello\"")
    print("\n" + "="*60 + "\n")

def test_translation(text: str = "Hello, how are you?"):
    """Test the translator with sample text."""
    print(f"\n📝 Testing translation: '{text}'")
    result = translate_text(text)
    print(f"✓ Result: {result}\n")
    return result

if __name__ == '__main__':
    import sys
    
    # Display index if no arguments
    if len(sys.argv) == 1:
        print_index()
    
    # Test translation with optional argument
    elif sys.argv[1] == '--test':
        test_text = sys.argv[2] if len(sys.argv) > 2 else "Hello, how are you?"
        test_translation(test_text)
    
    # Show help
    elif sys.argv[1] == '--help':
        print_index()
    
    # Start Flask app
    elif sys.argv[1] == '--run':
        host = sys.argv[3] if len(sys.argv) > 3 and sys.argv[2] == '--host' else '127.0.0.1'
        port = int(sys.argv[4]) if len(sys.argv) > 4 and sys.argv[3] == '--port' else 5000
        print(f"\n🚀 Starting Flask app on http://{host}:{port}\n")
        app.run(host=host, port=port, debug=True)
