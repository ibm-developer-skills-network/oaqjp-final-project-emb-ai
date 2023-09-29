''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask framework package
from flask import Flask, render_template, request

# Import the sentiment_analyzer function from the package created
from EmotionDetection.emotion_detection import emotion_detector

# Initiate the flask app
app = Flask('Emotion Detector')

@app.route("/emotionDetector")
def sent_detector():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using emotion_detector()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    '''
    text_to_analyze = request.args.get('textToAnalyze')

    # Check if the input is blank or contains only whitespace
    if not text_to_analyze or text_to_analyze.strip() == "":
        return 'Blank input! Please provide text to analyze.'
    
    response = emotion_detector(text_to_analyze)
    label = response['label']
    score = response['score']
    if label is None:
        return 'Invalid input! Try again.'
    return f"The given text has been identified as {label} with a score of {score}."

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 5000)