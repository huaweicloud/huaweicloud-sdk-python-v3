# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Match:

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
        'operate': 'str',
        'value': 'list[str]'
    }

    attribute_map = {
        'key': 'key',
        'operate': 'operate',
        'value': 'value'
    }

    def __init__(self, key=None, operate=None, value=None):
        r"""Match

        The model defined in huaweicloud sdk

        :param key: 指定按照Metadata中的key进行匹配
        :type key: str
        :param operate: 指定匹配的方式：EXIST:存在，REGEX:正则，EQUALS:等于
        :type operate: str
        :param value: 要匹配的key对应的value，当operate为存在时，此值为空
        :type value: list[str]
        """
        
        

        self._key = None
        self._operate = None
        self._value = None
        self.discriminator = None

        self.key = key
        self.operate = operate
        if value is not None:
            self.value = value

    @property
    def key(self):
        r"""Gets the key of this Match.

        指定按照Metadata中的key进行匹配

        :return: The key of this Match.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        r"""Sets the key of this Match.

        指定按照Metadata中的key进行匹配

        :param key: The key of this Match.
        :type key: str
        """
        self._key = key

    @property
    def operate(self):
        r"""Gets the operate of this Match.

        指定匹配的方式：EXIST:存在，REGEX:正则，EQUALS:等于

        :return: The operate of this Match.
        :rtype: str
        """
        return self._operate

    @operate.setter
    def operate(self, operate):
        r"""Sets the operate of this Match.

        指定匹配的方式：EXIST:存在，REGEX:正则，EQUALS:等于

        :param operate: The operate of this Match.
        :type operate: str
        """
        self._operate = operate

    @property
    def value(self):
        r"""Gets the value of this Match.

        要匹配的key对应的value，当operate为存在时，此值为空

        :return: The value of this Match.
        :rtype: list[str]
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this Match.

        要匹配的key对应的value，当operate为存在时，此值为空

        :param value: The value of this Match.
        :type value: list[str]
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
        if not isinstance(other, Match):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
