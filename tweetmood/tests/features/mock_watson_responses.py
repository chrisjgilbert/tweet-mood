class MockWatsonResponses:

    def mock_successful_response(self):
        return {'usage': {'text_units': 1, 'text_characters': 8531, 'features': 2}, 'language': 'en', 'keywords': [{'text': 'video Brexit Crisis', 'relevance': 0.808171, 'emotion': {'sadness': 0.123281, 'joy': 0.2856, 'fear': 0.00047, 'disgust': 0.363526, 'anger': 0.466701}, 'count': 1}, {'text': 'deal Brexit warnings', 'relevance': 0.736128, 'emotion': {'sadness': 0.123281, 'joy': 0.2856, 'fear': 0.00047, 'disgust': 0.363526, 'anger': 0.466701}, 'count': 1}], 'emotion': {'targets': [{'text': 'brexit', 'emotion': {'sadness': 0.594142, 'joy': 0.536118, 'fear': 0.132222, 'disgust': 0.25296, 'anger': 0.50368}}], 'document': {'emotion': {'sadness': 0.123281, 'joy': 0.2856, 'fear': 0.00047, 'disgust': 0.363526, 'anger': 0.466701}}}}

    def mock_warnings_response(self):
        return {'warnings': {'text_units': 1, 'text_characters': 8531, 'features': 2}, 'language': 'en', 'keywords': [{'text': 'video Brexit Crisis', 'relevance': 0.808171, 'emotion': {'sadness': 0.123281, 'joy': 0.2856, 'fear': 0.00047, 'disgust': 0.363526, 'anger': 0.466701}, 'count': 1}, {'text': 'deal Brexit warnings', 'relevance': 0.736128, 'emotion': {'sadness': 0.123281, 'joy': 0.2856, 'fear': 0.00047, 'disgust': 0.363526, 'anger': 0.466701}, 'count': 1}], 'emotion': {'targets': [{'text': 'brexit', 'emotion': {'sadness': 0.594142, 'joy': 0.536118, 'fear': 0.132222, 'disgust': 0.25296, 'anger': 0.50368}}], 'document': {'emotion': {'sadness': 0.123281, 'joy': 0.2856, 'fear': 0.00047, 'disgust': 0.363526, 'anger': 0.466701}}}}
