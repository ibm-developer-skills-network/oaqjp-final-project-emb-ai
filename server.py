''' Executing this function initiates the application of emotion detection to be 
    executed over the Flask channel and deployed on localhost:5000.
'''
# Import Flask, render_template, request from the flask framework package
from flask import Flask, render_template, request

# Import the emotion_detector function from the package created
from EmotionDetection.emotion_detection import emotion_detector

# Initiate the flask app
app = Flask('Emotion Detector')

@app.route("/emotionDetector")
def emot_detector():
    ''' This code receives the text from the HTML interface and runs emotion detection 
        over it using the emotion_detector() function. The output returned shows the 
        emotions, their associated scores, and the dominant emotion for the provided 
        text.
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    
    dominant_emotion = emotion_detector(text_to_analyze)
    if dominant_emotion is None:
        return 'Invalid text! Please try again.'
    else:
        # Create a formatted string for emotion scores
        emotion_scores_str = ', '.join([f"'{emotion}': {score}" for emotion, score in dominant_emotion.items() if emotion != 'dominant_emotion'])

        # Add the dominant emotion separately
        response = f'For the given statement, the system response is {emotion_scores_str}. The dominant emotion is \'{dominant_emotion["dominant_emotion"]}\'.'

        return response

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application page over the 
        Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 5000)
