# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DomainItem:

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
        'web_tag': 'str'
    }

    attribute_map = {
        'key': 'key',
        'num': 'num',
        'web_tag': 'web_tag'
    }

    def __init__(self, key=None, num=None, web_tag=None):
        """DomainItem

        The model defined in huaweicloud sdk

        :param key: 域名
        :type key: str
        :param num: 数量
        :type num: int
        :param web_tag: 网站名称，对应WAF控制台域名详情中的网站名称
        :type web_tag: str
        """
        
        

        self._key = None
        self._num = None
        self._web_tag = None
        self.discriminator = None

        if key is not None:
            self.key = key
        if num is not None:
            self.num = num
        if web_tag is not None:
            self.web_tag = web_tag

    @property
    def key(self):
        """Gets the key of this DomainItem.

        域名

        :return: The key of this DomainItem.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this DomainItem.

        域名

        :param key: The key of this DomainItem.
        :type key: str
        """
        self._key = key

    @property
    def num(self):
        """Gets the num of this DomainItem.

        数量

        :return: The num of this DomainItem.
        :rtype: int
        """
        return self._num

    @num.setter
    def num(self, num):
        """Sets the num of this DomainItem.

        数量

        :param num: The num of this DomainItem.
        :type num: int
        """
        self._num = num

    @property
    def web_tag(self):
        """Gets the web_tag of this DomainItem.

        网站名称，对应WAF控制台域名详情中的网站名称

        :return: The web_tag of this DomainItem.
        :rtype: str
        """
        return self._web_tag

    @web_tag.setter
    def web_tag(self, web_tag):
        """Sets the web_tag of this DomainItem.

        网站名称，对应WAF控制台域名详情中的网站名称

        :param web_tag: The web_tag of this DomainItem.
        :type web_tag: str
        """
        self._web_tag = web_tag

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
        if not isinstance(other, DomainItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
