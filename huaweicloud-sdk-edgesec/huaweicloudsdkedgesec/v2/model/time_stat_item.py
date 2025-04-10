# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TimeStatItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'key': 'int',
        'value': 'int'
    }

    attribute_map = {
        'key': 'key',
        'value': 'value'
    }

    def __init__(self, key=None, value=None):
        r"""TimeStatItem

        The model defined in huaweicloud sdk

        :param key: 时间戳，按时间粒度向左对齐。例如时间粒度为5分钟级，统计[19:10,19:15)，则该时间戳为19:10时刻时间
        :type key: int
        :param value: 攻击请求数
        :type value: int
        """
        
        

        self._key = None
        self._value = None
        self.discriminator = None

        self.key = key
        self.value = value

    @property
    def key(self):
        r"""Gets the key of this TimeStatItem.

        时间戳，按时间粒度向左对齐。例如时间粒度为5分钟级，统计[19:10,19:15)，则该时间戳为19:10时刻时间

        :return: The key of this TimeStatItem.
        :rtype: int
        """
        return self._key

    @key.setter
    def key(self, key):
        r"""Sets the key of this TimeStatItem.

        时间戳，按时间粒度向左对齐。例如时间粒度为5分钟级，统计[19:10,19:15)，则该时间戳为19:10时刻时间

        :param key: The key of this TimeStatItem.
        :type key: int
        """
        self._key = key

    @property
    def value(self):
        r"""Gets the value of this TimeStatItem.

        攻击请求数

        :return: The value of this TimeStatItem.
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this TimeStatItem.

        攻击请求数

        :param value: The value of this TimeStatItem.
        :type value: int
        """
        self._value = value

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
        if not isinstance(other, TimeStatItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
