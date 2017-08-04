class MediaModel:
    def __init__(self, attributes):
        """

        :param attributes:
        """
        default_properties = {
            "name": "",
            "service": "",
            "source": "",
            "type": "",
            "created": "",
            "thumbnailURL": "",
            "mediaURL": "",
            "credit": "",
        }

        for k, v in attributes.items():
            if k in default_properties.keys():
                default_properties[k] = v

        self.properties = default_properties
