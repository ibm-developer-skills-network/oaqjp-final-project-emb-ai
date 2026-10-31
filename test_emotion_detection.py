import unittest
from EmotionDetection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        tests = [
            ("I am glad this happened", "joy"),
            ("I am really mad about this", "anger"),
            ("I feel disgusted just hearing about this", "disgust"),
            ("I am so sad about this", "sadness"),
            ("I am really afraid that this will happen", "fear")
        ]
        for statement, dominant_emotion in tests:
            result = emotion_detector(statement)
            self.assertEqual(result["dominant_emotion"], dominant_emotion)


unittest.main()
