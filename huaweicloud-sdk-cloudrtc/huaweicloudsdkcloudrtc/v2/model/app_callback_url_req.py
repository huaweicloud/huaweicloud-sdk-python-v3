# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AppCallbackUrlReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'url': 'str',
        'auth_key': 'str'
    }

    attribute_map = {
        'url': 'url',
        'auth_key': 'auth_key'
    }

    def __init__(self, url=None, auth_key=None):
        """AppCallbackUrlReq

        The model defined in huaweicloud sdk

        :param url: 回调通知url地址，url必须以http://或https://开头，需要支持POST调用。
        :type url: str
        :param auth_key: 回调秘钥，主要用于鉴权
        :type auth_key: str
        """
        
        

        self._url = None
        self._auth_key = None
        self.discriminator = None

        self.url = url
        if auth_key is not None:
            self.auth_key = auth_key

    @property
    def url(self):
        """Gets the url of this AppCallbackUrlReq.

        回调通知url地址，url必须以http://或https://开头，需要支持POST调用。

        :return: The url of this AppCallbackUrlReq.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this AppCallbackUrlReq.

        回调通知url地址，url必须以http://或https://开头，需要支持POST调用。

        :param url: The url of this AppCallbackUrlReq.
        :type url: str
        """
        self._url = url

    @property
    def auth_key(self):
        """Gets the auth_key of this AppCallbackUrlReq.

        回调秘钥，主要用于鉴权

        :return: The auth_key of this AppCallbackUrlReq.
        :rtype: str
        """
        return self._auth_key

    @auth_key.setter
    def auth_key(self, auth_key):
        """Sets the auth_key of this AppCallbackUrlReq.

        回调秘钥，主要用于鉴权

        :param auth_key: The auth_key of this AppCallbackUrlReq.
        :type auth_key: str
        """
        self._auth_key = auth_key

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
        if not isinstance(other, AppCallbackUrlReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
