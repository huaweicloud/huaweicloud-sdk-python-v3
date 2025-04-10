# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ObjectArrayPatterns:

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
        'type': 'str',
        'max_length': 'int',
        'max_value': 'float',
        'min_value': 'float',
        'nullable': 'bool',
        'hint': 'str'
    }

    attribute_map = {
        'key': 'key',
        'type': 'type',
        'max_length': 'max_length',
        'max_value': 'max_value',
        'min_value': 'min_value',
        'nullable': 'nullable',
        'hint': 'hint'
    }

    def __init__(self, key=None, type=None, max_length=None, max_value=None, min_value=None, nullable=None, hint=None):
        r"""ObjectArrayPatterns

        The model defined in huaweicloud sdk

        :param key: 键
        :type key: str
        :param type: 对象类型
        :type type: str
        :param max_length: 最大长度
        :type max_length: int
        :param max_value: 最大值
        :type max_value: float
        :param min_value: 最小值
        :type min_value: float
        :param nullable: 是否可以为空值
        :type nullable: bool
        :param hint: 提示信息
        :type hint: str
        """
        
        

        self._key = None
        self._type = None
        self._max_length = None
        self._max_value = None
        self._min_value = None
        self._nullable = None
        self._hint = None
        self.discriminator = None

        if key is not None:
            self.key = key
        if type is not None:
            self.type = type
        if max_length is not None:
            self.max_length = max_length
        if max_value is not None:
            self.max_value = max_value
        if min_value is not None:
            self.min_value = min_value
        if nullable is not None:
            self.nullable = nullable
        if hint is not None:
            self.hint = hint

    @property
    def key(self):
        r"""Gets the key of this ObjectArrayPatterns.

        键

        :return: The key of this ObjectArrayPatterns.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        r"""Sets the key of this ObjectArrayPatterns.

        键

        :param key: The key of this ObjectArrayPatterns.
        :type key: str
        """
        self._key = key

    @property
    def type(self):
        r"""Gets the type of this ObjectArrayPatterns.

        对象类型

        :return: The type of this ObjectArrayPatterns.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ObjectArrayPatterns.

        对象类型

        :param type: The type of this ObjectArrayPatterns.
        :type type: str
        """
        self._type = type

    @property
    def max_length(self):
        r"""Gets the max_length of this ObjectArrayPatterns.

        最大长度

        :return: The max_length of this ObjectArrayPatterns.
        :rtype: int
        """
        return self._max_length

    @max_length.setter
    def max_length(self, max_length):
        r"""Sets the max_length of this ObjectArrayPatterns.

        最大长度

        :param max_length: The max_length of this ObjectArrayPatterns.
        :type max_length: int
        """
        self._max_length = max_length

    @property
    def max_value(self):
        r"""Gets the max_value of this ObjectArrayPatterns.

        最大值

        :return: The max_value of this ObjectArrayPatterns.
        :rtype: float
        """
        return self._max_value

    @max_value.setter
    def max_value(self, max_value):
        r"""Sets the max_value of this ObjectArrayPatterns.

        最大值

        :param max_value: The max_value of this ObjectArrayPatterns.
        :type max_value: float
        """
        self._max_value = max_value

    @property
    def min_value(self):
        r"""Gets the min_value of this ObjectArrayPatterns.

        最小值

        :return: The min_value of this ObjectArrayPatterns.
        :rtype: float
        """
        return self._min_value

    @min_value.setter
    def min_value(self, min_value):
        r"""Sets the min_value of this ObjectArrayPatterns.

        最小值

        :param min_value: The min_value of this ObjectArrayPatterns.
        :type min_value: float
        """
        self._min_value = min_value

    @property
    def nullable(self):
        r"""Gets the nullable of this ObjectArrayPatterns.

        是否可以为空值

        :return: The nullable of this ObjectArrayPatterns.
        :rtype: bool
        """
        return self._nullable

    @nullable.setter
    def nullable(self, nullable):
        r"""Sets the nullable of this ObjectArrayPatterns.

        是否可以为空值

        :param nullable: The nullable of this ObjectArrayPatterns.
        :type nullable: bool
        """
        self._nullable = nullable

    @property
    def hint(self):
        r"""Gets the hint of this ObjectArrayPatterns.

        提示信息

        :return: The hint of this ObjectArrayPatterns.
        :rtype: str
        """
        return self._hint

    @hint.setter
    def hint(self, hint):
        r"""Sets the hint of this ObjectArrayPatterns.

        提示信息

        :param hint: The hint of this ObjectArrayPatterns.
        :type hint: str
        """
        self._hint = hint

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
        if not isinstance(other, ObjectArrayPatterns):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
