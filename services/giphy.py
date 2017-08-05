import giphypop
from datetime import datetime
from .model import MediaModel


class GiphyService:
    def getMedia(searchQuery):
        mediaModels = []

        client = giphypop.Giphy()
        items = client.search(searchQuery)

        for item in items:

            #created = datetime.fromtimestamp(item.import_datetime).isoformat()
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
            mediaModels.append(media)

        return mediaModels
