"""
This module contains all ther server APIS
"""

from flask import Flask, request, render_template

from EmotionDetector.emotion_detector import emotion_detector

app = Flask(
    "Emotion Detector", template_folder="../templates", static_folder="../static"
)


@app.route("/emotionDetector")
def find_emotion_scores():
    """
    Checks the emotion scores of the given text
    """
    text_to_analyze = request.args.get("textToAnalyze")
    r = emotion_detector(text_to_analyze)
    if r["dominant_emotion"] is None:
        return "Invalid text! Please try again!."

    return (
        f"For the given statement, the system response is "
        f"'anger': {r['anger']}, "
        f"'disgust': {r['disgust']}, "
        f"'fear': {r['fear']}, "
        f"'joy': {r['joy']} and "
        f"'sadness': {r['sadness']}. "
        f"The dominant emotion is {r['dominant_emotion']}."
    ).join("")


@app.route("/")
def render_index_page():
    """
    Renders index.html file
    """
    return render_template("index.html")


app.run(port=5000)
