# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class HashtagList(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, photo_urls: List[str]=None):  # noqa: E501
        """HashtagList - a model defined in Swagger

        :param photo_urls: The photo_urls of this HashtagList.  # noqa: E501
        :type photo_urls: List[str]
        """
        self.swagger_types = {
            'photo_urls': List[str]
        }

        self.attribute_map = {
            'photo_urls': 'photoUrls'
        }
        self._photo_urls = photo_urls

    @classmethod
    def from_dict(cls, dikt) -> 'HashtagList':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The HashtagList of this HashtagList.  # noqa: E501
        :rtype: HashtagList
        """
        return util.deserialize_model(dikt, cls)

    @property
    def photo_urls(self) -> List[str]:
        """Gets the photo_urls of this HashtagList.


        :return: The photo_urls of this HashtagList.
        :rtype: List[str]
        """
        return self._photo_urls

    @photo_urls.setter
    def photo_urls(self, photo_urls: List[str]):
        """Sets the photo_urls of this HashtagList.


        :param photo_urls: The photo_urls of this HashtagList.
        :type photo_urls: List[str]
        """

        self._photo_urls = photo_urls
