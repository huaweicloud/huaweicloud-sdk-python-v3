# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HookCreate:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'secret': 'str',
        'url': 'str'
    }

    attribute_map = {
        'secret': 'secret',
        'url': 'url'
    }

    def __init__(self, secret=None, url=None):
        """HookCreate

        The model defined in huaweicloud sdk

        :param secret: 无法猜测的随机字符串，用于验证接收到的payloads。
        :type secret: str
        :param url: hook触发时的回调URL。
        :type url: str
        """
        
        

        self._secret = None
        self._url = None
        self.discriminator = None

        self.secret = secret
        self.url = url

    @property
    def secret(self):
        """Gets the secret of this HookCreate.

        无法猜测的随机字符串，用于验证接收到的payloads。

        :return: The secret of this HookCreate.
        :rtype: str
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        """Sets the secret of this HookCreate.

        无法猜测的随机字符串，用于验证接收到的payloads。

        :param secret: The secret of this HookCreate.
        :type secret: str
        """
        self._secret = secret

    @property
    def url(self):
        """Gets the url of this HookCreate.

        hook触发时的回调URL。

        :return: The url of this HookCreate.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this HookCreate.

        hook触发时的回调URL。

        :param url: The url of this HookCreate.
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
        if not isinstance(other, HookCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
