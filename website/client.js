document.addEventListener('DOMContentLoaded', () => {
    const data = {}; // Object to hold all captured data

    const addData = (feature, details) => {
        // Store captured data in the object
        data[feature] = details;
    };

    // Function to fetch client IP address
    const fetchClientIP = () => {
        return fetch('https://ipinfo.io/json')
            .then(response => {
                if (!response.ok) {
                    throw new Error('Failed to fetch IP address');
                }
                return response.json();
            })
            .then(data => data.ip)
            .catch(error => {
                console.error('Error fetching IP address:', error);
                return 'Not Available';
            });
    };

    const gatherData = async () => {
        try {
            const ip = await fetchClientIP();
            addData('IP Address', ip);

            // Capture various browser and system information
            addData('Browser CodeName', navigator.appCodeName);
            addData('Browser Name', navigator.appName);
            addData('Browser Version', navigator.appVersion);
            addData('Cookies Enabled', navigator.cookieEnabled);
            addData('Browser Language', navigator.language);
            addData('Browser Online', navigator.onLine);
            addData('Platform', navigator.platform);
            addData('User-agent header', navigator.userAgent);
            addData('Screen Width', screen.width);
            addData('Screen Height', screen.height);
            addData('Viewport Width', window.innerWidth);
            addData('Viewport Height', window.innerHeight);
            addData('Timezone', Intl.DateTimeFormat().resolvedOptions().timeZone);
            addData('Local Storage Available', typeof Storage !== 'undefined');
            addData('Session Storage Available', typeof sessionStorage !== 'undefined');
            addData('Online Status', navigator.onLine);

            if (navigator.getBattery) {
                try {
                    const battery = await navigator.getBattery();
                    addData('Battery Level', `${battery.level * 100}%`);
                    addData('Battery Charging', battery.charging);
                } catch (error) {
                    console.error('Battery information error:', error);
                    addData('Battery Level', 'Not Available');
                    addData('Battery Charging', 'Not Available');
                }
            } else {
                addData('Battery Level', 'Not Available');
                addData('Battery Charging', 'Not Available');
            }

            if (navigator.connection) {
                addData('Network Type', navigator.connection.effectiveType);
                addData('Network Downlink', navigator.connection.downlink);
                addData('Network RTT', navigator.connection.rtt);
            } else {
                addData('Network Type', 'Not Available');
            }

            if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(
                    position => {
                        addData('Geolocation', `Latitude: ${position.coords.latitude}, Longitude: ${position.coords.longitude}`);
                    },
                    error => {
                        console.error('Geolocation error:', error);
                        addData('Geolocation', 'Not Available');
                    }
                );
            } else {
                addData('Geolocation', 'Not Available');
            }

            if (screen.orientation) {
                addData('Screen Orientation', screen.orientation.type);
            } else {
                addData('Screen Orientation', 'Not Available');
            }

            addData('Cookies Enabled', navigator.cookieEnabled);
            addData('Do Not Track', navigator.doNotTrack);
            addData('Java Enabled', navigator.javaEnabled());

            if (navigator.mediaDevices && navigator.mediaDevices.enumerateDevices) {
                try {
                    const devices = await navigator.mediaDevices.enumerateDevices();
                    devices.forEach(device => {
                        addData('Media Device', `${device.kind}: ${device.label}`);
                    });
                } catch (error) {
                    console.error('Media devices error:', error);
                    addData('Media Devices', 'Not Available');
                }
            } else {
                addData('Media Devices', 'Not Available');
            }

            addData('File System Access', 'showOpenFilePicker' in window || 'showSaveFilePicker' in window);
            addData('USB Devices', 'usb' in navigator);
            addData('Keyboard Layout', 'keyboard' in navigator);

            if (navigator.mediaDevices && navigator.mediaDevices.enumerateDevices) {
                try {
                    const devices = await navigator.mediaDevices.enumerateDevices();
                    devices.forEach(device => {
                        addData('WebRTC Device', `${device.kind}: ${device.label}`);
                    });
                } catch (error) {
                    console.error('WebRTC devices error:', error);
                    addData('WebRTC Device Enumeration', 'Not Available');
                }
            } else {
                addData('WebRTC Device Enumeration', 'Not Available');
            }

            addData('Speech Recognition', 'webkitSpeechRecognition' in window || 'SpeechRecognition' in window);
            addData('Bluetooth', 'bluetooth' in navigator);
            addData('NFC', 'nfc' in navigator);
            addData('Payment Request API', 'PaymentRequest' in window);
            addData('WebAuthn', 'PublicKeyCredential' in window);
            addData('Gamepads', 'getGamepads' in navigator);
            addData('WebAssembly', 'WebAssembly' in window);
            addData('WebSocket', 'WebSocket' in window);
            addData('Ambient Light Sensor', 'AmbientLightSensor' in window);
            addData('Speech Synthesis', 'speechSynthesis' in window);
            addData('WebVR', 'getVRDisplays' in navigator);
            addData('WebXR', 'xr' in navigator);
            addData('Clipboard API', 'clipboard' in navigator);

            const performanceMetrics = performance.getEntriesByType('navigation');
            addData('Navigation Timing', JSON.stringify(performanceMetrics));

            addData('Device Motion', 'DeviceMotionEvent' in window);
            addData('Device Orientation', 'DeviceOrientationEvent' in window);
            addData('Browser Vendor', navigator.vendor);

            addData('Storage Quota', 'storage' in navigator && 'estimate' in navigator.storage);
            addData('IndexedDB Support', 'indexedDB' in window);
            addData('Service Workers Support', 'serviceWorker' in navigator);
            addData('Push Notifications Support', 'PushManager' in window);
            addData('Device Memory', navigator.deviceMemory || 'Not Available');
            addData('Hardware Concurrency', navigator.hardwareConcurrency);
            addData('Touch Points', navigator.maxTouchPoints || 'Not Available');
            addData('Pointer Events', 'onpointerdown' in window);
            addData('Subresource Integrity Support', 'integrity' in HTMLScriptElement.prototype);
            addData('Content Security Policy (CSP) Support', 'securitypolicyviolation' in document);
            addData('HTTP/2 Support', 'connection' in navigator && navigator.connection.nextHopProtocol === 'h2');
            addData('Fetch API Support', 'fetch' in window);
            addData('Resource Timing API Support', 'performance' in window && 'getEntriesByType' in performance);
            addData('Network Information API Support', 'connection' in navigator);
            addData('Beacon API Support', 'sendBeacon' in navigator);
            addData('Vibration API Support', 'vibrate' in navigator);
            addData('Digital Goods API', 'getDigitalGoods' in navigator);
            addData('Virtual Keyboard API', 'virtualKeyboard' in navigator);
            addData('Idle Detection API', 'IdleDetector' in window);
            addData('Interaction Media Features', 'matchMedia' in window && 'media' in matchMedia('(any-pointer: fine)'));
            addData('Web Share API', 'share' in navigator);
            addData('Permissions API', 'permissions' in navigator);

            // Add timestamp to the data object
            data.Timestamp = new Date().toISOString(); // Adds current timestamp in ISO 8601 format

            // Convert data object to JSON string
            const jsonData = JSON.stringify(data, null, 2); // Pretty-print JSON

            // AJAX request to send JSON data to Node.js server
            const xhr = new XMLHttpRequest();
            xhr.open('POST', 'http://localhost:3001/upload', true);
            xhr.setRequestHeader('Content-Type', 'application/json');
            xhr.onreadystatechange = () => {
                if (xhr.readyState === XMLHttpRequest.DONE) {
                    if (xhr.status === 200) {
                        console.log('Data sent successfully.');
                    } else {
                        console.error('Failed to send data. Status:', xhr.status);
                    }
                }
            };
            xhr.send(jsonData);
        } catch (error) {
            console.error('Error capturing data:', error);
        }
    };

    gatherData();
});
