"""Unit tests for the emotion detector."""

import unittest
from unittest.mock import Mock, patch

from emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Verify response parsing and error handling."""

    @patch("emotion_detection.requests.post")
    def test_dominant_joy(self, mock_post):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "emotionPredictions": [{
                "emotion": {
                    "anger": 0.01,
                    "disgust": 0.02,
                    "fear": 0.03,
                    "joy": 0.90,
                    "sadness": 0.04,
                }
            }]
        }
        mock_post.return_value = mock_response

        with patch("emotion_detection.WATSON_NLP_URL", "https://example.test"):
            result = emotion_detector("I am very happy")

        self.assertEqual(result["dominant_emotion"], "joy")
        self.assertEqual(result["joy"], 0.90)

    @patch("emotion_detection.requests.post")
    def test_http_400_returns_empty_result(self, mock_post):
        mock_response = Mock()
        mock_response.status_code = 400
        mock_post.return_value = mock_response

        with patch("emotion_detection.WATSON_NLP_URL", "https://example.test"):
            result = emotion_detector("invalid request text")

        self.assertIsNone(result["dominant_emotion"])
        self.assertIsNone(result["anger"])

    def test_blank_text_returns_empty_result(self):
        result = emotion_detector("   ")
        self.assertIsNone(result["dominant_emotion"])


if __name__ == "__main__":
    unittest.main()
