# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CustomParameter:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_private': 'bool',
        'key': 'str',
        'value': 'str'
    }

    attribute_map = {
        'is_private': 'isPrivate',
        'key': 'key',
        'value': 'value'
    }

    def __init__(self, is_private=None, key=None, value=None):
        r"""CustomParameter

        The model defined in huaweicloud sdk

        :param is_private: **参数解释：** 是否是私密参数。 **取值范围：** - true：私密参数。 - false：非私密参数。
        :type is_private: bool
        :param key: **参数解释：** 自定义参数的key。 **取值范围：** 长度为[1~128]个字符。
        :type key: str
        :param value: **参数解释：** 自定义参数的Value。 **取值范围：** 长度为[1~8192]个字符。
        :type value: str
        """
        
        

        self._is_private = None
        self._key = None
        self._value = None
        self.discriminator = None

        if is_private is not None:
            self.is_private = is_private
        if key is not None:
            self.key = key
        if value is not None:
            self.value = value

    @property
    def is_private(self):
        r"""Gets the is_private of this CustomParameter.

        **参数解释：** 是否是私密参数。 **取值范围：** - true：私密参数。 - false：非私密参数。

        :return: The is_private of this CustomParameter.
        :rtype: bool
        """
        return self._is_private

    @is_private.setter
    def is_private(self, is_private):
        r"""Sets the is_private of this CustomParameter.

        **参数解释：** 是否是私密参数。 **取值范围：** - true：私密参数。 - false：非私密参数。

        :param is_private: The is_private of this CustomParameter.
        :type is_private: bool
        """
        self._is_private = is_private

    @property
    def key(self):
        r"""Gets the key of this CustomParameter.

        **参数解释：** 自定义参数的key。 **取值范围：** 长度为[1~128]个字符。

        :return: The key of this CustomParameter.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        r"""Sets the key of this CustomParameter.

        **参数解释：** 自定义参数的key。 **取值范围：** 长度为[1~128]个字符。

        :param key: The key of this CustomParameter.
        :type key: str
        """
        self._key = key

    @property
    def value(self):
        r"""Gets the value of this CustomParameter.

        **参数解释：** 自定义参数的Value。 **取值范围：** 长度为[1~8192]个字符。

        :return: The value of this CustomParameter.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this CustomParameter.

        **参数解释：** 自定义参数的Value。 **取值范围：** 长度为[1~8192]个字符。

        :param value: The value of this CustomParameter.
        :type value: str
        """
        self._value = value

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
        if not isinstance(other, CustomParameter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
