import subprocess
import os
import http.server
import socketserver
import threading
import signal
import sys
import logging

# Get the current script directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger(__name__)

# Function to run npm install in the server directory
def npm_install_server_directory():
    try:
        os.chdir(os.path.join(script_dir, 'server'))  # Change directory to where your server package.json is located
        subprocess.run(['npm', 'install'], check=True)
    except subprocess.CalledProcessError as e:
        logger.error(f"npm install failed with error: {e}")
        sys.exit(1)
    except Exception as e:
        logger.error(f"An error occurred during npm install: {e}")
        sys.exit(1)

# Function to start Node.js server
def start_node_server():
    try:
        logger.info("Starting Node.js server...")
        subprocess.run(['node', 'server.js'], cwd=os.path.join(script_dir, 'server'), check=True)
    except subprocess.CalledProcessError as e:
        logger.error(f"Node.js server failed to start: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        logger.info("Node.js server stopped.")
        sys.exit(0)

# Function to start HTTP server for the website
def start_http_server():
    try:
        os.chdir(os.path.join(script_dir, 'website'))  # Change directory to where your website files are located
        Handler = http.server.SimpleHTTPRequestHandler
        with socketserver.TCPServer(("", 80), Handler) as httpd:
            logger.info("Serving website at port 80...")
            httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        httpd.server_close()
        logger.info("HTTP server stopped.")

# Signal handler for graceful shutdown
def signal_handler(sig, frame):
    logger.info(f"Received signal {sig}. Exiting...")
    sys.exit(0)

if __name__ == "__main__":
    # Set up signal handler for graceful shutdown
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    # Run npm install in the server directory
    npm_install_server_directory()

    # Start Node.js server in a separate thread
    node_thread = threading.Thread(target=start_node_server)
    node_thread.start()

    # Start HTTP server for the website
    start_http_server()

    # Wait for the Node.js server thread to complete (which it won't unless interrupted)
    node_thread.join()

    logger.info("Exiting program.")
