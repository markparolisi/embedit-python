from imgurpython import ImgurClient

from .model import MediaModel


class ImgurService:
    def getMedia(searchQuery):
        mediaModels = []

        attrs = {
            "name": "foo"
        }

        media = MediaModel(attrs)

        mediaModels.append(media)

        return mediaModels
