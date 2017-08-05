from flask import Flask
from flask import request
from flask import jsonify
from services.imgur import ImgurService
from services.giphy import GiphyService

app = Flask(__name__)


@app.route("/")
def index():
    """
    Placeholder endpoint
    """
    return "Please access the service at /media"


@app.route("/media")
def media():
    """
    Primary endpoint for the service

    :return:
    """
    query = request.args.get('q')
    services = request.args.get('services')

    # Require a search term
    if query is None or len(query) is 0:
        error = {
            "message": "Missing query parameter"
        }
        return jsonify(error), 400

    # Require a list of service(s)
    if services is None or len(services) is 0:
        error = {
            "message": "Missing services parameter"
        }
        return jsonify(error), 400

    services_list = services.lower().split(",")

    # Declare a return value container
    media_models = []

    if "imgur" in services_list:
        imgur_media = ImgurService.getMedia(query)
        media_models = media_models + imgur_media

    if "giphy" in services_list:
        giphy_media = GiphyService.getMedia(query)
        media_models = media_models + giphy_media

        media_models = [m.properties for m in media_models]

    return jsonify(media_models)


if __name__ == "__main__":
    app.run(port=8080)
