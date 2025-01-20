# Emotion Detection System

This project is a Flask-based web application that analyzes text input to detect emotions like anger, joy, sadness, disgust, and fear. The application uses IBM Watson's Emotion Detection API to perform sentiment analysis and returns the dominant emotion along with the confidence scores for each emotion.

---

## Table of Contents

1. [Features](#features)  
2. [Technologies Used](#technologies-used)  
3. [Setup Instructions](#setup-instructions)  
4. [Usage](#usage)  
5. [Error Handling](#error-handling)  
6. [Project Structure](#project-structure)  
7. [License](#license)  

---

## Features

- Accepts user input through a web interface.
- Uses the IBM Watson API to analyze emotions in text.
- Returns detailed emotion scores for anger, disgust, fear, joy, and sadness.
- Highlights the dominant emotion with the highest confidence score.
- Handles errors for invalid or empty inputs gracefully.

---

## Technologies Used

- **Python 3.10**
- **Flask**: For building the web application.
- **HTML & JavaScript**: For the front-end user interface.
- **IBM Watson API**: For emotion detection.
- **Requests**: To send HTTP requests to the API.

---

## Setup Instructions

### Prerequisites
1. Python 3.10 or higher installed on your system.
2. Internet connection to access the IBM Watson API.
3. `pip` for installing Python packages.

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/emotion_detection_system.git
   cd emotion_detection_system
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Start the Flask application:
   ```bash
   python server.py
   ```

4. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

---

## Usage

1. Enter a text statement in the input field on the home page.
2. Click the "Analyze" button.
3. View the system's response, including:
   - Emotion scores for all categories.
   - The dominant emotion and its confidence score.

---

## Error Handling

- **Invalid Text**: If the user submits a blank or invalid input, the application will display:
  ```
  Invalid text! Please try again!
  ```

- **API Errors**: If there’s an issue with the API (e.g., no response or incorrect formatting), the system will log the error and notify the user.

---

## Project Structure

```plaintext
Emotion_Detection_System/
├── templates/
│   └── index.html              # Front-end interface
├── static/
│   └── mywebscript.js          # Client-side JavaScript
├── emotion_detection/
│   └── emotion_detection.py    # Emotion detection logic
├── server.py                   # Main Flask application
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

