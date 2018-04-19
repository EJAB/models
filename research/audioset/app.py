import os

from routes import app

if __name__ == '__main__':
    app.debug = True
    host = os.environ.get('IP', '0.0.0.0')
    port = int(os.environ.get('PORT', 8080))
    """creates a web server, not robust, just for testing and developing, adhoc = https instead of http"""
    app.run(host=host, port=port, ssl_context='adhoc')