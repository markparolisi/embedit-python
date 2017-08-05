import unittest

from services.giphy import GiphyService


class GiphyTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_getMedia(self):
        media = GiphyService.getMedia("pizza")

        self.assertGreater(len(media), 0)
        self.assertEqual(media[0].properties['service'], "Giphy")


if __name__ == "__main__":
    unittest.main()
