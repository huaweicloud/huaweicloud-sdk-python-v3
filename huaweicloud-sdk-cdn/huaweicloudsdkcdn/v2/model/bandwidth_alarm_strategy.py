# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BandwidthAlarmStrategy:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'value': 'int'
    }

    attribute_map = {
        'status': 'status',
        'value': 'value'
    }

    def __init__(self, status=None, value=None):
        r"""BandwidthAlarmStrategy

        The model defined in huaweicloud sdk

        :param status: **参数解释：** 带宽告警开关 **约束限制：** 不涉及 **取值范围：** - on: 开启 - off: 关闭  **默认取值：** off: 关闭
        :type status: str
        :param value: **参数解释：** 带宽告警阈值，单位：bit/s **约束限制：** - status为on时必填  **取值范围：** 1000000-10000000000000 **默认取值：** 不涉及
        :type value: int
        """
        
        

        self._status = None
        self._value = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if value is not None:
            self.value = value

    @property
    def status(self):
        r"""Gets the status of this BandwidthAlarmStrategy.

        **参数解释：** 带宽告警开关 **约束限制：** 不涉及 **取值范围：** - on: 开启 - off: 关闭  **默认取值：** off: 关闭

        :return: The status of this BandwidthAlarmStrategy.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this BandwidthAlarmStrategy.

        **参数解释：** 带宽告警开关 **约束限制：** 不涉及 **取值范围：** - on: 开启 - off: 关闭  **默认取值：** off: 关闭

        :param status: The status of this BandwidthAlarmStrategy.
        :type status: str
        """
        self._status = status

    @property
    def value(self):
        r"""Gets the value of this BandwidthAlarmStrategy.

        **参数解释：** 带宽告警阈值，单位：bit/s **约束限制：** - status为on时必填  **取值范围：** 1000000-10000000000000 **默认取值：** 不涉及

        :return: The value of this BandwidthAlarmStrategy.
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this BandwidthAlarmStrategy.

        **参数解释：** 带宽告警阈值，单位：bit/s **约束限制：** - status为on时必填  **取值范围：** 1000000-10000000000000 **默认取值：** 不涉及

        :param value: The value of this BandwidthAlarmStrategy.
        :type value: int
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
        if not isinstance(other, BandwidthAlarmStrategy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
