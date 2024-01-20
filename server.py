from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def detect_emotion():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return jsonify({
            'error': 'Invalid text! Please try again.'
        })
    else:
        return jsonify({
            'anger': response['anger'],
            'disgust': response['disgust'],
            'fear': response['fear'],
            'joy': response['joy'],
            'sadness': response['sadness'],
            'statement': f". The dominant emotion is {response['dominant_emotion']}."
        })

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)