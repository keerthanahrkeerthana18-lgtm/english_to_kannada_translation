"""
Entry point for Flask application deployment.
This is the main application file that Render/hosting platforms will run.
"""

import os
import logging
from translator import app

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

if __name__ == '__main__':
    # Get host and port from environment variables
    # Render sets PORT automatically, defaults to 5000 for local development
    host = os.environ.get('HOST', '0.0.0.0')
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    
    logger.info(f'🚀 Starting English to Kannada Translator')
    logger.info(f'   Server: http://{host}:{port}')
    logger.info(f'   Debug Mode: {debug}')
    
    # Run Flask app
    app.run(host=host, port=port, debug=debug)
