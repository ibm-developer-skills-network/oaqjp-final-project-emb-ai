"""Detect emotions in English text using the Watson NLP service."""

import os
import requests


WATSON_NLP_URL = os.getenv("WATSON_NLP_URL", "").strip()
MODEL_ID = os.getenv(
    "WATSON_NLP_MODEL_ID",
    "emotion_aggregated-workflow_lang_en_stock",
)
TIMEOUT_SECONDS = 30


def emotion_detector(text):
    """Return emotion scores and the dominant emotion for *text*.

    The service endpoint must be supplied through WATSON_NLP_URL.
    On an HTTP 400 response, return the standard empty-result structure.
    """
    if not isinstance(text, str) or not text.strip():
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }

    if not WATSON_NLP_URL:
        raise RuntimeError(
            "Set the WATSON_NLP_URL environment variable to your Watson NLP endpoint."
        )

    payload = {"raw_document": {"text": text}}
    headers = {"grpc-metadata-mm-model-id": MODEL_ID}

    response = requests.post(
        WATSON_NLP_URL,
        json=payload,
        headers=headers,
        timeout=TIMEOUT_SECONDS,
    )

    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }

    response.raise_for_status()
    result = response.json()
    emotions = result["emotionPredictions"][0]["emotion"]

    scores = {
        "anger": emotions["anger"],
        "disgust": emotions["disgust"],
        "fear": emotions["fear"],
        "joy": emotions["joy"],
        "sadness": emotions["sadness"],
    }
    scores["dominant_emotion"] = max(scores, key=scores.get)
    return scores
