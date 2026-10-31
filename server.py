"""Flask web server for the emotion detection application.

This module provides a web interface for analyzing the emotions expressed
in user-provided text. It exposes the root page and the `/emotionDetector`
endpoint, which uses the EmotionDetection package to return emotion scores
and the dominant emotion.
"""


from flask import Flask, render_template, request
from EmotionDetection import emotion_detector


app = Flask(__name__)


@app.route("/")
def render_index_page():
    """Render the application's main web page.

    Returns:
        str: The rendered contents of the index HTML template.
    """

    return render_template("index.html")


@app.route("/emotionDetector")
def detector():
    """Analyze the text submitted by the user and return emotion results.

    The function retrieves text from the ``textToAnalyze`` query parameter,
    uses ``emotion_detector`` to calculate the emotion scores, and returns
    the scores and dominant emotion as formatted text. If the submitted text
    is invalid or empty, an error message is returned.

    Returns:
        str: A formatted emotion-analysis result or an invalid-input message.
    """

    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)
    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"
    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
