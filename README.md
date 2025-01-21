
# File Sharing via Local HTTP Server

This Python script allows you to easily share files from your local system using a simple HTTP server. It also generates a QR code for quick access, making file sharing convenient and efficient.

---

## Features
- Shares files from a specified directory over the local network.
- Generates a QR code for easy access to the file server URL.
- Opens the file server URL automatically in the default browser.
- Works on Windows, Linux, and macOS.

---

## How It Works
1. The script starts a local HTTP server on a specified port.
2. Files from a given directory are made accessible via a browser.
3. A QR code is generated and displayed, allowing quick access to the server using a mobile device.

---

## Prerequisites
- Python 3.x installed on your system.
- Required Python libraries:
  - `http.server` (built-in)
  - `socketserver` (built-in)
  - `socket` (built-in)
  - `os` (built-in)
  - `webbrowser` (built-in)
  - `pyqrcode`
  - `subprocess` (built-in)

Install the `pyqrcode` library if not already installed:
```bash
pip install pyqrcode
```

---

## Usage
1. Clone the repository or download the script.
2. Edit the script to specify the directory you want to share:
   ```python
   DIRECTORY = "E:\final year\"
   ```
   Replace `"E:\final year\"` with the path to your desired directory.

3. Run the script:
   ```bash
   python main.py
   ```

4. The script will:
   - Start the server on `http://<your-ip>:3000/`.
   - Display the QR code for quick access.
   - Automatically open the URL in your default browser.

---

## Example Output
- **Server Information**:
  ```
  Server started on port 3000
  Server IP: 192.168.1.100
  Access files at: http://192.168.1.100:3000/
  QRCode generated
  ```

- **QR Code**:
  The QR code opens the file server URL when scanned with a mobile device.

---

## Stopping the Server
- To stop the server, press `Ctrl+C` in the terminal.

---

## Notes
- Ensure the specified directory exists. The script will create it if it doesn’t.
- This script is intended for use within a trusted local network. Do not use it over untrusted or public networks.

---

