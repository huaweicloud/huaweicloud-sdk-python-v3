# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CountItem:

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
        'num': 'int'
    }

    attribute_map = {
        'key': 'key',
        'num': 'num'
    }

    def __init__(self, key=None, num=None):
        """CountItem

        The model defined in huaweicloud sdk

        :param key: 类型，包括请求总量（ACCESS）、Bot攻击防护（CRAWLER）、攻击总量（TOTAL_ATTACK）、Web基础防护（WEB_ATTACK）、精准防护（PRECISE）以及CC攻击防护（CC）
        :type key: str
        :param num: 数量
        :type num: int
        """
        
        

        self._key = None
        self._num = None
        self.discriminator = None

        if key is not None:
            self.key = key
        if num is not None:
            self.num = num

    @property
    def key(self):
        """Gets the key of this CountItem.

        类型，包括请求总量（ACCESS）、Bot攻击防护（CRAWLER）、攻击总量（TOTAL_ATTACK）、Web基础防护（WEB_ATTACK）、精准防护（PRECISE）以及CC攻击防护（CC）

        :return: The key of this CountItem.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this CountItem.

        类型，包括请求总量（ACCESS）、Bot攻击防护（CRAWLER）、攻击总量（TOTAL_ATTACK）、Web基础防护（WEB_ATTACK）、精准防护（PRECISE）以及CC攻击防护（CC）

        :param key: The key of this CountItem.
        :type key: str
        """
        self._key = key

    @property
    def num(self):
        """Gets the num of this CountItem.

        数量

        :return: The num of this CountItem.
        :rtype: int
        """
        return self._num

    @num.setter
    def num(self, num):
        """Sets the num of this CountItem.

        数量

        :param num: The num of this CountItem.
        :type num: int
        """
        self._num = num

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
        if not isinstance(other, CountItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
