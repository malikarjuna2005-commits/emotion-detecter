"""Unit tests for the emotion detector."""

import json
import unittest
from unittest.mock import Mock, patch

from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetection(unittest.TestCase):
    """Test cases for emotion detection."""

    def mock_response(self, dominant_emotion):
        """Build a Watson-shaped response for an expected emotion."""
        emotions = {
            "anger": 0.01,
            "disgust": 0.01,
            "fear": 0.01,
            "joy": 0.01,
            "sadness": 0.01
        }
        emotions[dominant_emotion] = 0.95
        response = Mock()
        response.status_code = 200
        response.text = json.dumps(
            {"emotionPredictions": [{"emotion": emotions}]}
        )
        return response

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_joy(self, mock_post):
        """Verify that joyful text is classified as joy."""
        mock_post.return_value = self.mock_response("joy")
        result = emotion_detector("I am glad this happened")
        self.assertEqual(
            result["dominant_emotion"],
            "joy"
        )

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_anger(self, mock_post):
        """Verify that angry text is classified as anger."""
        mock_post.return_value = self.mock_response("anger")
        result = emotion_detector("I am really mad about this")
        self.assertEqual(
            result["dominant_emotion"],
            "anger"
        )

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_disgust(self, mock_post):
        """Verify that disgusting text is classified as disgust."""
        mock_post.return_value = self.mock_response("disgust")
        result = emotion_detector(
            "I feel disgusted just hearing about this"
        )
        self.assertEqual(
            result["dominant_emotion"],
            "disgust"
        )

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_sadness(self, mock_post):
        """Verify that sad text is classified as sadness."""
        mock_post.return_value = self.mock_response("sadness")
        result = emotion_detector("I am so sad about this")
        self.assertEqual(
            result["dominant_emotion"],
            "sadness"
        )

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_fear(self, mock_post):
        """Verify that fearful text is classified as fear."""
        mock_post.return_value = self.mock_response("fear")
        result = emotion_detector(
            "I am really afraid that this will happen"
        )
        self.assertEqual(
            result["dominant_emotion"],
            "fear"
        )

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_invalid_input(self, mock_post):
        """Verify that Watson HTTP 400 responses return empty results."""
        mock_post.return_value = Mock(status_code=400)
        result = emotion_detector("")
        self.assertIsNone(result["dominant_emotion"])


if __name__ == "__main__":
    unittest.main()
