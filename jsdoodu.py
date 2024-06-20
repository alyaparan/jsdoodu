import subprocess
import os
import http.server
import socketserver
import threading
import signal
import sys
import logging
import json
import time
import urllib.request

# Get the current script directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Function to load configuration from JSON file
def load_config():
    try:
        with open(os.path.join(script_dir, 'config.json')) as config_file:
            config = json.load(config_file)
        return config
    except FileNotFoundError:
        logger.error("Config file not found. Exiting.")
        sys.exit(1)
    except json.JSONDecodeError as e:
        logger.error(f"Error parsing config file: {e}. Exiting.")
        sys.exit(1)

# Function to run npm install in the server directory
def npm_install_server_directory():
    max_retries = 3
    retries = 0
    while retries < max_retries:
        try:
            os.chdir(os.path.join(script_dir, 'server'))
            subprocess.run(['npm', 'install'], check=True)
            break  # Installation successful, exit loop
        except subprocess.CalledProcessError as e:
            logger.error(f"npm install failed with error: {e}")
            retries += 1
            if retries < max_retries:
                logger.info(f"Retrying npm install (Attempt {retries}/{max_retries})...")
                time.sleep(5)  # Wait 5 seconds before retrying
            else:
                logger.error("Maximum retries exceeded. Exiting.")
                sys.exit(1)
        except Exception as e:
            logger.error(f"An unexpected error occurred during npm install: {e}")
            sys.exit(1)

# Function to start Node.js server
def start_node_server():
    try:
        logger.info("Starting Node.js server...")
        subprocess.run(['node', 'server.js'], cwd=os.path.join(script_dir, 'server'), check=True)
    except subprocess.CalledProcessError as e:
        logger.error(f"Node.js server failed to start: {e}")
        sys.exit(1)
    except Exception as e:
        logger.error(f"An unexpected error occurred during Node.js server start: {e}")
        sys.exit(1)

# Function to check Node.js server health
def check_node_server_health():
    try:
        response = urllib.request.urlopen('http://localhost:3000/health')  # Adjust URL as per your server configuration
        if response.getcode() == 200:
            logger.info("Node.js server is healthy.")
        else:
            logger.warning("Node.js server returned non-200 status.")
    except Exception as e:
        logger.error(f"Failed to check Node.js server health: {e}")

# Function to start HTTP server for the website
def start_http_server(http_port):
    try:
        os.chdir(os.path.join(script_dir, 'website'))  # Change directory to where your website files are located
        Handler = http.server.SimpleHTTPRequestHandler
        with socketserver.TCPServer(("", http_port), Handler) as httpd:
            logger.info(f"Serving website at port {http_port}...")
            httpd.serve_forever()
    except OSError as e:
        logger.error(f"OS error occurred: {e}")
    except Exception as e:
        logger.error(f"Unexpected error occurred in HTTP server: {e}")
    finally:
        if 'httpd' in locals():
            httpd.server_close()
            logger.info("HTTP server stopped.")

# Signal handler for graceful shutdown
def signal_handler(sig, frame):
    logger.info(f"Received signal {sig}. Exiting...")

    # Shutdown HTTP server
    if 'httpd' in locals():
        httpd.shutdown()
        httpd.server_close()

    sys.exit(0)

if __name__ == "__main__":
    # Load configuration
    config = load_config()

    # Set up signal handler for graceful shutdown
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    # Run npm install in the server directory
    npm_install_server_directory()

    # Start Node.js server in a separate thread
    node_thread = threading.Thread(target=start_node_server)
    node_thread.start()

    # Start HTTP server for the website
    http_port = config.get('http_port', 80)
    start_http_server(http_port)

    # Periodically check Node.js server health
    health_check_interval = config.get('health_check_interval', 60)
    while True:
        check_node_server_health()
        time.sleep(health_check_interval)

    # Wait for the Node.js server thread to complete (which it won't unless interrupted)
    node_thread.join()

    logger.info("Exiting program.")
