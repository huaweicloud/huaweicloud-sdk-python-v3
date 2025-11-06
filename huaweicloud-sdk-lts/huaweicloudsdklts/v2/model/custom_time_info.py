# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CustomTimeInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enable': 'bool',
        'key': 'str',
        'value': 'str',
        'time_format': 'str'
    }

    attribute_map = {
        'enable': 'enable',
        'key': 'key',
        'value': 'value',
        'time_format': 'time_format'
    }

    def __init__(self, enable=None, key=None, value=None, time_format=None):
        r"""CustomTimeInfo

        The model defined in huaweicloud sdk

        :param enable: **参数解释：** 是否开启自定义时间字段。 **取值范围：** - true - fasle
        :type enable: bool
        :param key: **参数解释：** 从demoField中选取的作为日志系统时间的字段名称。 **取值范围：** 不涉及。
        :type key: str
        :param value: **参数解释：** 从demoField中选取的作为日志系统时间的字段内容示例。 **取值范围：** 不涉及。
        :type value: str
        :param time_format: **参数解释：** 用于解析字段为时间类型的时间格式参数。 **取值范围：** 不涉及。   
        :type time_format: str
        """
        
        

        self._enable = None
        self._key = None
        self._value = None
        self._time_format = None
        self.discriminator = None

        if enable is not None:
            self.enable = enable
        if key is not None:
            self.key = key
        if value is not None:
            self.value = value
        if time_format is not None:
            self.time_format = time_format

    @property
    def enable(self):
        r"""Gets the enable of this CustomTimeInfo.

        **参数解释：** 是否开启自定义时间字段。 **取值范围：** - true - fasle

        :return: The enable of this CustomTimeInfo.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        r"""Sets the enable of this CustomTimeInfo.

        **参数解释：** 是否开启自定义时间字段。 **取值范围：** - true - fasle

        :param enable: The enable of this CustomTimeInfo.
        :type enable: bool
        """
        self._enable = enable

    @property
    def key(self):
        r"""Gets the key of this CustomTimeInfo.

        **参数解释：** 从demoField中选取的作为日志系统时间的字段名称。 **取值范围：** 不涉及。

        :return: The key of this CustomTimeInfo.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        r"""Sets the key of this CustomTimeInfo.

        **参数解释：** 从demoField中选取的作为日志系统时间的字段名称。 **取值范围：** 不涉及。

        :param key: The key of this CustomTimeInfo.
        :type key: str
        """
        self._key = key

    @property
    def value(self):
        r"""Gets the value of this CustomTimeInfo.

        **参数解释：** 从demoField中选取的作为日志系统时间的字段内容示例。 **取值范围：** 不涉及。

        :return: The value of this CustomTimeInfo.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this CustomTimeInfo.

        **参数解释：** 从demoField中选取的作为日志系统时间的字段内容示例。 **取值范围：** 不涉及。

        :param value: The value of this CustomTimeInfo.
        :type value: str
        """
        self._value = value

    @property
    def time_format(self):
        r"""Gets the time_format of this CustomTimeInfo.

        **参数解释：** 用于解析字段为时间类型的时间格式参数。 **取值范围：** 不涉及。   

        :return: The time_format of this CustomTimeInfo.
        :rtype: str
        """
        return self._time_format

    @time_format.setter
    def time_format(self, time_format):
        r"""Sets the time_format of this CustomTimeInfo.

        **参数解释：** 用于解析字段为时间类型的时间格式参数。 **取值范围：** 不涉及。   

        :param time_format: The time_format of this CustomTimeInfo.
        :type time_format: str
        """
        self._time_format = time_format

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
        if not isinstance(other, CustomTimeInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
