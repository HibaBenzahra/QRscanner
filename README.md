# QR Code Scanner

## Overview
This project is a real-time QR code scanner built using Python with OpenCV, PyZbar, and Tkinter. It utilizes a webcam to scan QR codes and checks them against a predefined list for authorization. The application also plays a sound when a QR code is detected.

## Features
- **Real-time QR Code Detection**: Uses a webcam to scan QR codes.
- **Authorization Check**: Verifies scanned QR codes against a stored list (`codes.txt`).
- **Audio Feedback**: Plays a sound when a QR code is detected.
- **GUI Interface**: Built with Tkinter for an easy-to-use experience.
- **Start/Stop Controls**: Enables and disables scanning via buttons.

## Installation
### Prerequisites
Ensure you have Python installed along with the required dependencies:

### Installation Steps
1. Clone this repository or download the script.
2. Install dependencies using pip:
   ```sh
   pip install opencv-python numpy pyzbar pillow pygame
   ```
3. Run the script:
   ```sh
   python qr_scanner.py
   ```

## Usage
- Click **Start Scan** to activate the webcam and start scanning QR codes.
- If a QR code is detected:
  - It checks if it's authorized (present in `codes.txt`).
  - Displays "Authorized" (green) or "None Authorized" (red).
  - Draws a bounding polygon around the QR code.
  - Plays a sound if a new QR code is detected.
- Click **Stop Scan** to pause scanning.
- Click **Exit** to close the application.

## Technologies Used
- **Python**: Programming language
- **OpenCV**: Computer vision library for real-time QR code scanning
- **PyZbar**: Library for decoding QR codes
- **Tkinter**: GUI framework for user interaction
- **Pygame**: For playing sound alerts

## Contributing
If you'd like to improve this project, feel free to fork the repository and submit a pull request with your enhancements.

## License
This project is open-source and available under the MIT License.

