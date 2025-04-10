# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CommonStatItem:

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
        'value': 'int'
    }

    attribute_map = {
        'key': 'key',
        'value': 'value'
    }

    def __init__(self, key=None, value=None):
        r"""CommonStatItem

        The model defined in huaweicloud sdk

        :param key: 对应请求参数group_by的子类别。例如在Http攻击分布统计接口中，group_by为action时，key可为：log、block、captcha、js_challenge；在Http攻击Top接口中，group_by为url时，key可为请求的URL，例：/abc。
        :type key: str
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
        r"""Gets the key of this CommonStatItem.

        对应请求参数group_by的子类别。例如在Http攻击分布统计接口中，group_by为action时，key可为：log、block、captcha、js_challenge；在Http攻击Top接口中，group_by为url时，key可为请求的URL，例：/abc。

        :return: The key of this CommonStatItem.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        r"""Sets the key of this CommonStatItem.

        对应请求参数group_by的子类别。例如在Http攻击分布统计接口中，group_by为action时，key可为：log、block、captcha、js_challenge；在Http攻击Top接口中，group_by为url时，key可为请求的URL，例：/abc。

        :param key: The key of this CommonStatItem.
        :type key: str
        """
        self._key = key

    @property
    def value(self):
        r"""Gets the value of this CommonStatItem.

        攻击请求数

        :return: The value of this CommonStatItem.
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this CommonStatItem.

        攻击请求数

        :param value: The value of this CommonStatItem.
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
        if not isinstance(other, CommonStatItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
