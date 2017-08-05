from datetime import datetime
from imgurpython import ImgurClient
import re
import json_config

from .model import MediaModel


class ImgurService:
    @staticmethod
    def getMedia(search_query):
        """

        :param search_query: String to search service for
        :return:
        """
        media_models = []

        cfg = json_config.connect("credentials.json")
        client_id = cfg["imgur"]["clientID"]
        client_secret = cfg["imgur"]["clientSecret"]
        client = ImgurClient(client_id, client_secret)
        items = client.gallery_search(search_query, sort="viral")

        for item in items:

            if item.is_album is True:
                continue

            created = datetime.fromtimestamp(item.datetime).isoformat()
            thumbnail_url = re.sub(r"(\.[a-z]{3,4})$", "m\\1", item.link)

            attrs = {
                "name": item.title,
                "service": 'Imgur',
                "mediaURL": item.link,
                "source": item.link,
                "type": 'image',
                "created": created,
                "thumbnailURL": thumbnail_url,
                "credit": 'http://imgur.com/user/' + item.account_url,
            }

            media = MediaModel(attrs)
            media_models.append(media)

        return media_models
