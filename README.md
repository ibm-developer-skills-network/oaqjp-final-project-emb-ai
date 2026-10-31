# Emotion Detection Web Application

A lightweight web application built with **Flask** and **Python** that evaluates text input to identify emotional sentiment. The application connects to an external IBM Watson NLP service via REST API to score emotions (anger, disgust, fear, joy, sadness) and determine the dominant emotion in real time.

---

## Features

- **Emotion Analysis:** Analyzes input statements and returns confidence scores across 5 emotional states (anger, disgust, fear, joy, sadness) alongside the dominant emotion.
- **Modular Architecture:** Core prediction and parsing logic is packaged into a reusable internal module (`EmotionDetection`).
- **Robust Error Handling:** Detects blank or invalid user payloads and gracefully handles HTTP 400 responses across the API client and Flask server.
- **Automated Testing:** Covered with unit test cases using Python's standard `unittest` framework to verify classification logic.
- **Code Quality:** Adheres to PEP 8 standards with static code analysis verified via `pylint`.

---

## Project Structure

```text
├── EmotionDetection/
│   ├── __init__.py                # Package initialization and module export
│   └── emotion_detection.py       # API call logic, JSON parsing, and dominant emotion detection
├── static/
│   └── mywebscript.js             # Client-side JavaScript handling async requests
├── templates/
│   └── index.html                 # Frontend user interface
├── server.py                      # Flask routing, request handling, and error response logic
├── test_emotion_detection.py      # Automated unit tests
└── README.md                      # Project documentation
```

---

## Installation & Setup

### 1. Prerequisites
- Python 3.8+ installed on your system.
- `pip` package manager.

### 2. Clone the Repository
```bash
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>
```

### 3. Install Dependencies
Install the required packages (`flask` and `requests`):
```bash
pip install flask requests
```

*(Optional) Install development dependencies for testing and linting:*
```bash
pip install pylint
```

---

## Running the Application

1. Start the Flask server:
   ```bash
   python3 server.py
   ```
2. Open your web browser and navigate to:
   ```text
   http://127.0.0.1:5000/
   ```
3. Enter any statement into the text input area and click **Run Sentiment Analysis**.

---

## Running Unit Tests

Run the test suite using Python's built-in `unittest` runner:
```bash
python3 test_emotion_detection.py
```

To run static code analysis with `pylint`:
```bash
pylint server.py EmotionDetection/emotion_detection.py
```

---

## API Behavior

### `GET /emotionDetector`
Processes user text passed via query parameter.

- **Query Parameter:** `textToAnalyze` (string)
- **Valid Request Example:**
  ```text
  GET /emotionDetector?textToAnalyze=I am so happy I passed the exam!
  ```
  **Response:**
  ```text
  For the given statement, the system response is 'anger': 0.005, 'disgust': 0.002, 'fear': 0.004, 'joy': 0.954 and 'sadness': 0.012. The dominant emotion is joy.
  ```
- **Invalid / Empty Request:**
  ```text
  GET /emotionDetector?textToAnalyze=
  ```
  **Response:**
  ```text
  Invalid text! Please try again!
  ```
