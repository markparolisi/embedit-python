from flask import Flask
from flask import request
from flask import jsonify
from services.imgur import ImgurService
from services.giphy import GiphyService

app = Flask(__name__)


@app.route("/")
def index():
    return "Please access the service at /media"


@app.route("/media")
def media():
    query = request.args.get('q')
    services = request.args.get('services')

    if query is None or len(query) is 0:
        error = {
            "message": "Missing query parameter"
        }
        return jsonify(error), 400

    if services is None or len(services) is 0:
        error = {
            "message": "Missing services parameter"
        }
        return jsonify(error), 400

    servicesList = services.lower().split(",")

    media = []

    if "imgur" in servicesList:
        imgurMedia = ImgurService.getMedia(query)
        media = media + imgurMedia

    if "giphy" in servicesList:
        giphyMedia = GiphyService.getMedia(query)
        media = media + giphyMedia

    media = [m.properties for m in media]

    return jsonify(media)


if __name__ == "__main__":
    app.run(port=8080)
