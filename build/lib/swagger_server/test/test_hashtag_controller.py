# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.hashtag_list import HashtagList  # noqa: E501
from swagger_server.test import BaseTestCase


class TestHashtagController(BaseTestCase):
    """HashtagController integration test stubs"""

    def test_get_pet_by_id(self):
        """Test case for get_pet_by_id

        Get hashtags from seed hashtag
        """
        response = self.client.open(
            '//Hashtags/{seedHashtag}'.format(seed_hashtag='seed_hashtag_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
