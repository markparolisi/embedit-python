import giphypop
from .model import MediaModel
import json_config


class GiphyService:
    @staticmethod
    def getMedia(search_query):
        """

        :param search_query: String to search service for
        :return:
        """
        media_models = []
        cfg = json_config.connect("credentials.json")
        giphy_api_key = cfg["giphy"]["apiKey"]
        client = giphypop.Giphy(api_key=giphy_api_key)
        items = client.search(search_query)

        for item in items:
            # created = datetime.fromtimestamp(item.import_datetime).isoformat()
            created = ""

            attrs = {
                "name": item.id,
                "service": 'Giphy',
                "mediaURL": item.media_url,
                "source": item.url,
                "type": 'gif',
                "created": created,
                "thumbnailURL": item.fixed_width.downsampled.url,
                "credit": item.url,
            }

            media = MediaModel(attrs)
            media_models.append(media)

        return media_models
