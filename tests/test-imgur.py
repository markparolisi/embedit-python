import unittest

from services.imgur import ImgurService


class ImgurTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_getMedia(self):
        media = ImgurService.getMedia("pizza")

        self.assertGreater(len(media), 0)
        self.assertEqual(media[0].properties['service'], "Imgur")


if __name__ == "__main__":
    unittest.main()
