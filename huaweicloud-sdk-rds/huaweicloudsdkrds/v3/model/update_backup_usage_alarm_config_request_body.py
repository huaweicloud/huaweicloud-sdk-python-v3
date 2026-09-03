# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateBackupUsageAlarmConfigRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alarm_enabled': 'str',
        'threshold_percent': 'int',
        'increment_percent': 'int'
    }

    attribute_map = {
        'alarm_enabled': 'alarm_enabled',
        'threshold_percent': 'threshold_percent',
        'increment_percent': 'increment_percent'
    }

    def __init__(self, alarm_enabled=None, threshold_percent=None, increment_percent=None):
        r"""UpdateBackupUsageAlarmConfigRequestBody

        The model defined in huaweicloud sdk

        :param alarm_enabled: **参数解释**：  告警开关。  **约束限制**：  不涉及。  **取值范围**：  - ON - OFF  **默认取值**：  不涉及。
        :type alarm_enabled: str
        :param threshold_percent: **参数解释**：  阈值百分比，占免费备份空间大小的百分比。  **约束限制**：  不涉及。  **取值范围**：  1-100。  **默认取值**：  90
        :type threshold_percent: int
        :param increment_percent: **参数解释**：  增量百分比，占免费备份空间大小的百分比。  **约束限制**：  不涉及。  **取值范围**：  1-100。  **默认取值**：  10
        :type increment_percent: int
        """
        
        

        self._alarm_enabled = None
        self._threshold_percent = None
        self._increment_percent = None
        self.discriminator = None

        self.alarm_enabled = alarm_enabled
        if threshold_percent is not None:
            self.threshold_percent = threshold_percent
        if increment_percent is not None:
            self.increment_percent = increment_percent

    @property
    def alarm_enabled(self):
        r"""Gets the alarm_enabled of this UpdateBackupUsageAlarmConfigRequestBody.

        **参数解释**：  告警开关。  **约束限制**：  不涉及。  **取值范围**：  - ON - OFF  **默认取值**：  不涉及。

        :return: The alarm_enabled of this UpdateBackupUsageAlarmConfigRequestBody.
        :rtype: str
        """
        return self._alarm_enabled

    @alarm_enabled.setter
    def alarm_enabled(self, alarm_enabled):
        r"""Sets the alarm_enabled of this UpdateBackupUsageAlarmConfigRequestBody.

        **参数解释**：  告警开关。  **约束限制**：  不涉及。  **取值范围**：  - ON - OFF  **默认取值**：  不涉及。

        :param alarm_enabled: The alarm_enabled of this UpdateBackupUsageAlarmConfigRequestBody.
        :type alarm_enabled: str
        """
        self._alarm_enabled = alarm_enabled

    @property
    def threshold_percent(self):
        r"""Gets the threshold_percent of this UpdateBackupUsageAlarmConfigRequestBody.

        **参数解释**：  阈值百分比，占免费备份空间大小的百分比。  **约束限制**：  不涉及。  **取值范围**：  1-100。  **默认取值**：  90

        :return: The threshold_percent of this UpdateBackupUsageAlarmConfigRequestBody.
        :rtype: int
        """
        return self._threshold_percent

    @threshold_percent.setter
    def threshold_percent(self, threshold_percent):
        r"""Sets the threshold_percent of this UpdateBackupUsageAlarmConfigRequestBody.

        **参数解释**：  阈值百分比，占免费备份空间大小的百分比。  **约束限制**：  不涉及。  **取值范围**：  1-100。  **默认取值**：  90

        :param threshold_percent: The threshold_percent of this UpdateBackupUsageAlarmConfigRequestBody.
        :type threshold_percent: int
        """
        self._threshold_percent = threshold_percent

    @property
    def increment_percent(self):
        r"""Gets the increment_percent of this UpdateBackupUsageAlarmConfigRequestBody.

        **参数解释**：  增量百分比，占免费备份空间大小的百分比。  **约束限制**：  不涉及。  **取值范围**：  1-100。  **默认取值**：  10

        :return: The increment_percent of this UpdateBackupUsageAlarmConfigRequestBody.
        :rtype: int
        """
        return self._increment_percent

    @increment_percent.setter
    def increment_percent(self, increment_percent):
        r"""Sets the increment_percent of this UpdateBackupUsageAlarmConfigRequestBody.

        **参数解释**：  增量百分比，占免费备份空间大小的百分比。  **约束限制**：  不涉及。  **取值范围**：  1-100。  **默认取值**：  10

        :param increment_percent: The increment_percent of this UpdateBackupUsageAlarmConfigRequestBody.
        :type increment_percent: int
        """
        self._increment_percent = increment_percent

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
        if not isinstance(other, UpdateBackupUsageAlarmConfigRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
