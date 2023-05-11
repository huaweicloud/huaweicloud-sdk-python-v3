# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAnonymousAuthRandomResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'site_url': 'str',
        'random': 'str'
    }

    attribute_map = {
        'site_url': 'siteUrl',
        'random': 'random'
    }

    def __init__(self, site_url=None, random=None):
        """CreateAnonymousAuthRandomResponse

        The model defined in huaweicloud sdk

        :param site_url: 下一跳URL。
        :type site_url: str
        :param random: 鉴权随机数。
        :type random: str
        """
        
        super(CreateAnonymousAuthRandomResponse, self).__init__()

        self._site_url = None
        self._random = None
        self.discriminator = None

        if site_url is not None:
            self.site_url = site_url
        if random is not None:
            self.random = random

    @property
    def site_url(self):
        """Gets the site_url of this CreateAnonymousAuthRandomResponse.

        下一跳URL。

        :return: The site_url of this CreateAnonymousAuthRandomResponse.
        :rtype: str
        """
        return self._site_url

    @site_url.setter
    def site_url(self, site_url):
        """Sets the site_url of this CreateAnonymousAuthRandomResponse.

        下一跳URL。

        :param site_url: The site_url of this CreateAnonymousAuthRandomResponse.
        :type site_url: str
        """
        self._site_url = site_url

    @property
    def random(self):
        """Gets the random of this CreateAnonymousAuthRandomResponse.

        鉴权随机数。

        :return: The random of this CreateAnonymousAuthRandomResponse.
        :rtype: str
        """
        return self._random

    @random.setter
    def random(self, random):
        """Sets the random of this CreateAnonymousAuthRandomResponse.

        鉴权随机数。

        :param random: The random of this CreateAnonymousAuthRandomResponse.
        :type random: str
        """
        self._random = random

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateAnonymousAuthRandomResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
