# JS.Doodu

## Version 1.0.1

JS.Doodu is a sophisticated web application designed to capture detailed browser and system information from the client and send it to a Node.js server for storage and analysis. This tool is perfect for web developers, data analysts, cybersecurity enthusiasts, and ethical hackers looking to gain deep insights into client-side environments.

## Features

- **IP Address Detection**: Automatically fetches and logs the client's IP address.
- **Browser Information**: Collects comprehensive browser details such as name, version, language, and more.
- **System Information**: Gathers data about the client's operating system, platform, and hardware.
- **Network Information**: Logs network-related information like connection type and downlink speed.
- **Geolocation**: Captures the client's geographic location (latitude and longitude).
- **Device Capabilities**: Detects available device features such as battery status, media devices, and sensors.
- **Performance Metrics**: Logs navigation timing and other performance-related metrics.
- **BeEF-XSS Integration**: Utilizes BeEF-XSS for advanced browser exploitation framework features, accessible via `http://127.0.0.1:3000/hook.js`.

## Installation

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/alyaparan/jsdoodu.git
    cd jsdoodu
    ```

2. **Navigate to the Server Directory**:
    ```sh
    cd server
    ```

3. **Install Server Dependencies**:
    ```sh
    npm install
    ```

4. **Start the Node.js Server**:
    ```sh
    node server.js
    ```

5. **Open Another Terminal and Navigate to the Website Directory**:
    ```sh
    cd ../website
    ```

6. **Start the HTTP Server for the Website**:
    ```sh
    python3 -m http.server 80
    ```

7. **Access the Application**:
   Open a web browser and navigate to `http://localhost`. This will load the `index.html` page and start capturing client-side data.

## File Structure

The project directory structure is as follows:

    jsdoodu/
        ├── server/
        │   ├── node_modules/
        │   ├── package-lock.json
        │   ├── package.json
        │   └── server.js
        ├── website/
        │   ├── client.js
        │   ├── favicon.ico
        │   ├── index.html
        │   ├── script.js
        │   └── styles.css
        ├── jsdoodu.py
        ├── README.md
        ├── .gitignore
        ├── LICENSE
        └── CODE_OF_CONDUCT.md

### Directories and Files

- **`server/`**: Contains the Node.js server files.
  - `node_modules/`: Directory for Node.js dependencies.
  - `package-lock.json`, `package.json`: Node.js package management files.
  - `server.js`: Main server script.

- **`website/`**: Contains the client-side files for the web application.
  - `client.js`: Client-side JavaScript file.
  - `favicon.ico`: Favicon for the website.
  - `index.html`: Main HTML file for the application.
  - `script.js`: Additional JavaScript functionality for the website.
  - `styles.css`: CSS styles for the website.

- **`jsdoodu.py`**: Python script for automating server and website startup.

### Usage

1. **Server Automatically Setup and Startup**:
   - Navigate to `server/` directory and install dependencies:
     ```sh
     cd jsdoodu

     ```
     ```sh
     python3 jsdoodu.py
     ```

3. **Accessing the Application**:
   - Open a web browser and visit `http://localhost`. This will load `index.html` and initiate data capture from the client's browser.

4. **BeEF-XSS Integration**:
   - The application integrates BeEF-XSS capabilities via `http://127.0.0.1:3000/hook.js`. Ensure your BeEF-XSS server is running on this endpoint for advanced browser exploitation features.

## Contributing

- **Code of Conduct**: Please adhere to our [Code of Conduct](CODE_OF_CONDUCT.md) when contributing.
- **Contributing Guidelines**: Read the [Contributing Guidelines](CONTRIBUTING.md) before submitting pull requests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or concerns, you can contact the project creator at:
- Website: [alikparanyan.com](http://www.alikparanyan.com)
- Email: [mail@alikparanyan.com](mailto:mail@alikparanyan.com)
- Personal Gmail: [alikparanyan@gmail.com](mailto:alikparanyan@gmail.com)
