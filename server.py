"""
Server for the Emotion Detector application.
"""

from flask import Flask, request

from EmotionDetection.emotion_detection import emotion_detector


app = Flask(__name__)


@app.route("/emotionDetector")
def sent_detector():
    """Detect the emotion of submitted text."""

    text_to_analyse = request.args.get(
        "textToAnalyze"
    )

    if not text_to_analyse or not text_to_analyse.strip():
        return "Invalid text! Please try again!"

    response = emotion_detector(text_to_analyse)

    if response["dominant_emotion"] is None:
        return (
            "Invalid text! Please try again!"
        )

    return (
        "For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is "
        f"{response['dominant_emotion']}."
    )


@app.route("/")
def render_index_page():
    """Render the Emotion Detector home page."""

    return (
        "<h1>Emotion Detector</h1>"
        "<form action='/emotionDetector'>"
        "<input type='text' "
        "name='textToAnalyze'>"
        "<input type='submit' "
        "value='Analyze'>"
        "</form>"
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )
