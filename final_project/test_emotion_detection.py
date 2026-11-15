"""
This module tests the emotion_detector function to pass the static values
"""

import unittest

from EmotionDetector.emotion_detector import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """
    Unit test class of the emotion_detector module
    """

    def test_emotion_detector(self):
        """
        Test the output of the emotion_detector function
        """
        test1 = emotion_detector("I am glad this happened")["dominant_emotion"]
        self.assertEqual(test1, "joy")
        test2 = emotion_detector("I am really mad about this")["dominant_emotion"]
        self.assertEqual(test2, "anger")
        test3 = emotion_detector("I feel disgusted just hearing about this")[
            "dominant_emotion"
        ]
        self.assertEqual(test3, "disgust")
        test4 = emotion_detector("I am so sad about this")["dominant_emotion"]
        self.assertEqual(test4, "sadness")
        test5 = emotion_detector("I am really afraid that this will happen")[
            "dominant_emotion"
        ]
        self.assertEqual(test5, "fear")


unittest.main()
