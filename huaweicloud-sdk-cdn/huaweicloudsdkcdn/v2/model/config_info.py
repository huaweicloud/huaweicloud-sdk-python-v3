# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConfigInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'url': 'TopUrl',
        'ua': 'TopUa'
    }

    attribute_map = {
        'url': 'url',
        'ua': 'ua'
    }

    def __init__(self, url=None, ua=None):
        r"""ConfigInfo

        The model defined in huaweicloud sdk

        :param url: 
        :type url: :class:`huaweicloudsdkcdn.v2.TopUrl`
        :param ua: 
        :type ua: :class:`huaweicloudsdkcdn.v2.TopUa`
        """
        
        

        self._url = None
        self._ua = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if ua is not None:
            self.ua = ua

    @property
    def url(self):
        r"""Gets the url of this ConfigInfo.

        :return: The url of this ConfigInfo.
        :rtype: :class:`huaweicloudsdkcdn.v2.TopUrl`
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this ConfigInfo.

        :param url: The url of this ConfigInfo.
        :type url: :class:`huaweicloudsdkcdn.v2.TopUrl`
        """
        self._url = url

    @property
    def ua(self):
        r"""Gets the ua of this ConfigInfo.

        :return: The ua of this ConfigInfo.
        :rtype: :class:`huaweicloudsdkcdn.v2.TopUa`
        """
        return self._ua

    @ua.setter
    def ua(self, ua):
        r"""Sets the ua of this ConfigInfo.

        :param ua: The ua of this ConfigInfo.
        :type ua: :class:`huaweicloudsdkcdn.v2.TopUa`
        """
        self._ua = ua

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
        if not isinstance(other, ConfigInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
