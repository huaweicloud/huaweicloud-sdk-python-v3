# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UrlItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'key': 'str',
        'num': 'int',
        'host': 'str'
    }

    attribute_map = {
        'key': 'key',
        'num': 'num',
        'host': 'host'
    }

    def __init__(self, key=None, num=None, host=None):
        """UrlItem

        The model defined in huaweicloud sdk

        :param key: url路径
        :type key: str
        :param num: 数量
        :type num: int
        :param host: 域名
        :type host: str
        """
        
        

        self._key = None
        self._num = None
        self._host = None
        self.discriminator = None

        if key is not None:
            self.key = key
        if num is not None:
            self.num = num
        if host is not None:
            self.host = host

    @property
    def key(self):
        """Gets the key of this UrlItem.

        url路径

        :return: The key of this UrlItem.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this UrlItem.

        url路径

        :param key: The key of this UrlItem.
        :type key: str
        """
        self._key = key

    @property
    def num(self):
        """Gets the num of this UrlItem.

        数量

        :return: The num of this UrlItem.
        :rtype: int
        """
        return self._num

    @num.setter
    def num(self, num):
        """Sets the num of this UrlItem.

        数量

        :param num: The num of this UrlItem.
        :type num: int
        """
        self._num = num

    @property
    def host(self):
        """Gets the host of this UrlItem.

        域名

        :return: The host of this UrlItem.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this UrlItem.

        域名

        :param host: The host of this UrlItem.
        :type host: str
        """
        self._host = host

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
        if not isinstance(other, UrlItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
