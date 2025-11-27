# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Taint:

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
        'value': 'str',
        'effect': 'str',
        'timeadded': 'datetime'
    }

    attribute_map = {
        'key': 'key',
        'value': 'value',
        'effect': 'effect',
        'timeadded': 'timeadded'
    }

    def __init__(self, key=None, value=None, effect=None, timeadded=None):
        r"""Taint

        The model defined in huaweicloud sdk

        :param key: 键
        :type key: str
        :param value: 值
        :type value: str
        :param effect: effect信息
        :type effect: str
        :param timeadded: 时间戳信息
        :type timeadded: datetime
        """
        
        

        self._key = None
        self._value = None
        self._effect = None
        self._timeadded = None
        self.discriminator = None

        if key is not None:
            self.key = key
        if value is not None:
            self.value = value
        if effect is not None:
            self.effect = effect
        if timeadded is not None:
            self.timeadded = timeadded

    @property
    def key(self):
        r"""Gets the key of this Taint.

        键

        :return: The key of this Taint.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        r"""Sets the key of this Taint.

        键

        :param key: The key of this Taint.
        :type key: str
        """
        self._key = key

    @property
    def value(self):
        r"""Gets the value of this Taint.

        值

        :return: The value of this Taint.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this Taint.

        值

        :param value: The value of this Taint.
        :type value: str
        """
        self._value = value

    @property
    def effect(self):
        r"""Gets the effect of this Taint.

        effect信息

        :return: The effect of this Taint.
        :rtype: str
        """
        return self._effect

    @effect.setter
    def effect(self, effect):
        r"""Sets the effect of this Taint.

        effect信息

        :param effect: The effect of this Taint.
        :type effect: str
        """
        self._effect = effect

    @property
    def timeadded(self):
        r"""Gets the timeadded of this Taint.

        时间戳信息

        :return: The timeadded of this Taint.
        :rtype: datetime
        """
        return self._timeadded

    @timeadded.setter
    def timeadded(self, timeadded):
        r"""Sets the timeadded of this Taint.

        时间戳信息

        :param timeadded: The timeadded of this Taint.
        :type timeadded: datetime
        """
        self._timeadded = timeadded

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Taint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
