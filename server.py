"""
server.py

A Flask application to provide dominant emotion using emotion_detector function.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Initiate the Flask app
app = Flask("EmotionDetector")

@app.route("/emotionDetector")
def sent_detector():
    """
    Detects the emotion of the provided text.
    Retrieves the text to detect emotion from the request arguments,
    calls the emotion_detector function, and returns the detection results.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get("textToAnalyze", "").strip()

    # Check if text_to_analyze is None or empty
    if not text_to_analyze:
        return "Invalid text! Please try again!"

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Extract the dominant emotion and scores from the response
    dominant_emotion = response.get("dominant_emotion")
    # Check if the dominant emotion is None
    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    # Extract the emotion scores
    anger = response.get("anger", 0)
    disgust = response.get("disgust", 0)
    fear = response.get("fear", 0)
    joy = response.get("joy", 0)
    sadness = response.get("sadness", 0)

    # Format the response as per the requirements
    formatted_response = (
        f"For the given statement, the system response is 'anger': {anger}, "
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )

    return formatted_response


@app.route("/")
def render_index_page():
    """Renders the index.html template."""
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5004)
