import json
from src import utils


class TestApplication:

    @staticmethod
    def get_api_key():
        with open("credentials.json") as f:
            custom_vision_key = json.load(f)["api_key"]

        return custom_vision_key

    def test_model_prediction(self):

        # Select test image
        test_image = utils.take_trash_picture()

        # Compute prediction
        custom_vision_key = self.get_api_key()
        prediction = utils.classify_waste(test_image, custom_vision_key)

        # Test result
        assert len(prediction) == 1
        assert type(prediction) == str
        assert prediction in ["glass", "plastic", "metal", "trash"]
