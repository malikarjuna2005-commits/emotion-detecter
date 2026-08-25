# Final Project: Emotion Detector (oaqjp-final-project-emb-ai)

An AI-based web application that detects emotions from text using the Watson NLP service.

## Repository

Public repository: https://github.com/malikarjuna2005-commits/oaqjp-final-project-emb-ai


## Features

- Detects anger, disgust, fear, joy, and sadness.
- Identifies the dominant emotion.
- Provides a Flask web interface and HTTP endpoint.
- Handles blank input, HTTP 400 responses, and Watson network failures.

## Project Structure

```text
EmotionDetection/
	__init__.py
	emotion_detection.py
server.py
test_emotion_detection.py
requirements.txt
```

## Setup

Create and activate a virtual environment, then install the dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Run the Application

Start the Flask server:

```bash
python server.py
```

Open http://127.0.0.1:5000/ and enter a statement. The analysis endpoint is:

```text
http://127.0.0.1:5000/emotionDetector?textToAnalyze=I%20am%20happy
```

For blank or invalid input, the application returns:

```text
Invalid text! Please try again!
```

## Test and Code Quality

Run the unit tests:

```bash
python -m unittest -v
```

Run static analysis:

```bash
pylint server.py EmotionDetection/emotion_detection.py EmotionDetection/__init__.py test_emotion_detection.py
```

The current test suite contains six passing tests, and the project reaches a pylint score of 10.00/10.

## Assignment Evidence

- `6b_deployment_test.png`: Flask deployment interface.
- `7c_error_handling_interface.png`: Blank-input error response.
