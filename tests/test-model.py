import unittest

from services.model import MediaModel


class ModelTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_constructor(self):
        attrs = {
            "name": "foo"
        }

        media = MediaModel(attrs)

        self.assertEqual(media.properties['name'], "foo")
        self.assertEqual(media.properties['service'], "")
        self.assertRaises(KeyError, lambda: media.properties['foobar'])


if __name__ == "__main__":
    unittest.main()
