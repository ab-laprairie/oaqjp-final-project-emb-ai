# Import the requests library to handle HTTP requests
import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Handle blank or None input
    if not text_to_analyse or text_to_analyse.strip() == "":
        return {key: None for key in ['anger', 'disgust', 'fear', 'joy', 'sadness', 'dominant_emotion']}

    myobj = {"raw_document": {"text": text_to_analyse}}

    try:
        # Make the POST request to the API
        response = requests.post(url, json=myobj, headers=header)

        # Check the status code of the response
        if response.status_code == 400:
            return {key: None for key in ['anger', 'disgust', 'fear', 'joy', 'sadness', 'dominant_emotion']}

        # Parse the API response
        formatted_response = response.json()

        # Extract the emotion scores
        emotion_scores = formatted_response['emotionPredictions'][0]['emotion']

        # Find the dominant emotion
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)

        # Format the output
        return {**emotion_scores, 'dominant_emotion': dominant_emotion}

    except (requests.exceptions.RequestException, KeyError, IndexError, ValueError) as e:
        # Handle request errors or response parsing issues
        print(f"Error occurred: {e}")
        return {key: None for key in ['anger', 'disgust', 'fear', 'joy', 'sadness', 'dominant_emotion']}
