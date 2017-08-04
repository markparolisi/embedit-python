from datetime import datetime
from imgurpython import ImgurClient
import re
import json_config

from .model import MediaModel


class ImgurService:
    def getMedia(searchQuery):
        mediaModels = []

        cfg = json_config.connect("credentials.json")
        imgurClientID = cfg["imgur"]["clientID"]
        imgurClientSecret = cfg["imgur"]["clientSecret"]
        client = ImgurClient(imgurClientID, imgurClientSecret)
        items = client.gallery_search(searchQuery, sort="viral")

        for item in items:
            print(item)

            if item.is_album is True:
                continue

            created = datetime.fromtimestamp(item.datetime).isoformat()
            thumbnailURL = re.sub(r"(\.[a-z]{3,4})$", "m\\1", item.link)

            attrs = {
                "name": item.title,
                "service": 'Imgur',
                "mediaURL": item.link,
                "source": item.link,
                "type": 'image',
                "created": created,
                "thumbnailURL": thumbnailURL,
                "credit": 'http://imgur.com/user/' + item.account_url,
            }

            media = MediaModel(attrs)
            mediaModels.append(media)

        return mediaModels
