# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StandardPlatformApiConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'api_type': 'str',
        'url': 'str'
    }

    attribute_map = {
        'api_type': 'api_type',
        'url': 'url'
    }

    def __init__(self, api_type=None, url=None):
        r"""StandardPlatformApiConfig

        The model defined in huaweicloud sdk

        :param api_type: API类型。 * PRODUCT_QUERY: 查询商品 * LIVE_EVENT_CALLBACK: 直播事件回调
        :type api_type: str
        :param url: URL。仅支持HTTPS形式URL
        :type url: str
        """
        
        

        self._api_type = None
        self._url = None
        self.discriminator = None

        self.api_type = api_type
        self.url = url

    @property
    def api_type(self):
        r"""Gets the api_type of this StandardPlatformApiConfig.

        API类型。 * PRODUCT_QUERY: 查询商品 * LIVE_EVENT_CALLBACK: 直播事件回调

        :return: The api_type of this StandardPlatformApiConfig.
        :rtype: str
        """
        return self._api_type

    @api_type.setter
    def api_type(self, api_type):
        r"""Sets the api_type of this StandardPlatformApiConfig.

        API类型。 * PRODUCT_QUERY: 查询商品 * LIVE_EVENT_CALLBACK: 直播事件回调

        :param api_type: The api_type of this StandardPlatformApiConfig.
        :type api_type: str
        """
        self._api_type = api_type

    @property
    def url(self):
        r"""Gets the url of this StandardPlatformApiConfig.

        URL。仅支持HTTPS形式URL

        :return: The url of this StandardPlatformApiConfig.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this StandardPlatformApiConfig.

        URL。仅支持HTTPS形式URL

        :param url: The url of this StandardPlatformApiConfig.
        :type url: str
        """
        self._url = url

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
        if not isinstance(other, StandardPlatformApiConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
