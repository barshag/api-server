import connexion
import six

from swagger_server.models.hashtag_list import HashtagList  # noqa: E501
from swagger_server import util


def get_pet_by_id(seed_hashtag):  # noqa: E501
    """Get hashtags from seed hashtag

    Returns List of hashtags that are # noqa: E501

    :param seed_hashtag: The initial seed
    :type seed_hashtag: str

    :rtype: HashtagList
    """
    return 'do some magic!'
