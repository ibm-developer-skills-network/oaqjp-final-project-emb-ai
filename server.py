"""Flask web application for emotion detection."""

from flask import Flask, request, render_template_string
from emotion_detection import emotion_detector


app = Flask(__name__)

PAGE = """
<!doctype html>
<html lang="en">
<head><meta charset="utf-8"><title>Emotion Detection</title></head>
<body>
  <h1>Emotion Detection</h1>
  <form action="/emotionDetector" method="get">
    <label for="textToAnalyze">Enter text to analyze:</label>
    <input id="textToAnalyze" name="textToAnalyze" type="text" required>
    <button type="submit">Analyze</button>
  </form>
  <div id="result">{{ result }}</div>
</body>
</html>
"""


@app.get("/")
def home():
    """Render the application's home page."""
    return render_template_string(PAGE, result="")


@app.get("/emotionDetector")
def detect_emotion():
    """Analyze submitted text, returning a helpful message for blank input."""
    text_to_analyze = request.args.get("textToAnalyze", "").strip()
    if not text_to_analyze:
        return (
            "Invalid input! Please provide some text to analyze.",
            400,
        )

    try:
        result = emotion_detector(text_to_analyze)
    except (RuntimeError, ValueError, KeyError) as error:
        app.logger.exception("Emotion detection failed")
        return (f"Emotion detection service error: {error}", 502)

    if result["dominant_emotion"] is None:
        return (
            "Invalid input! Please provide valid text to analyze.",
            400,
        )

    summary = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. The dominant emotion is "
        f"{result['dominant_emotion']}."
    )
    return summary, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
