from src import utils


class TestApplication:

    def test_model_prediction(self):

        # Select test image
        test_image = utils.take_trash_picture()
        # Get API key
        custom_vision_key = utils.get_custom_vision_api_key("credentials.json")
        # Compute prediction
        prediction = utils.classify_waste(test_image, custom_vision_key)
        # Test result
        assert type(prediction) == str
        assert prediction in ["glass", "plastic", "metal", "trash"]
