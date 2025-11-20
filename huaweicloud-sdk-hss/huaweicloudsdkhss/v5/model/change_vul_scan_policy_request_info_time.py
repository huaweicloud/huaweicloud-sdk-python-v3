# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChangeVulScanPolicyRequestInfoTime:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'day_part': 'list[int]',
        'hour_part': 'int',
        'minute_part': 'int',
        'next_scan_time': 'int',
        'timezone_offset': 'int'
    }

    attribute_map = {
        'day_part': 'day_part',
        'hour_part': 'hour_part',
        'minute_part': 'minute_part',
        'next_scan_time': 'next_scan_time',
        'timezone_offset': 'timezone_offset'
    }

    def __init__(self, day_part=None, hour_part=None, minute_part=None, next_scan_time=None, timezone_offset=None):
        r"""ChangeVulScanPolicyRequestInfoTime

        The model defined in huaweicloud sdk

        :param day_part: **参数解释**: 扫描日期或者星期列表 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值31 **默认取值**: 不涉及 
        :type day_part: list[int]
        :param hour_part: **参数解释**: 扫描时间的小时部分 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值11 **默认取值**: 不涉及 
        :type hour_part: int
        :param minute_part: **参数解释**: 扫描时间的分钟部分 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值59 **默认取值**: 不涉及 
        :type minute_part: int
        :param next_scan_time: **参数解释**: 下一次扫描时间 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2^63-1 **默认取值**: 不涉及 
        :type next_scan_time: int
        :param timezone_offset: **参数解释**: 距离标准时区的差值，如东八区（GMT+8）为-480 **约束限制**: 不涉及 **取值范围**: 最小值-840，最大值720 **默认取值**: 不涉及 
        :type timezone_offset: int
        """
        
        

        self._day_part = None
        self._hour_part = None
        self._minute_part = None
        self._next_scan_time = None
        self._timezone_offset = None
        self.discriminator = None

        if day_part is not None:
            self.day_part = day_part
        if hour_part is not None:
            self.hour_part = hour_part
        if minute_part is not None:
            self.minute_part = minute_part
        if next_scan_time is not None:
            self.next_scan_time = next_scan_time
        if timezone_offset is not None:
            self.timezone_offset = timezone_offset

    @property
    def day_part(self):
        r"""Gets the day_part of this ChangeVulScanPolicyRequestInfoTime.

        **参数解释**: 扫描日期或者星期列表 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值31 **默认取值**: 不涉及 

        :return: The day_part of this ChangeVulScanPolicyRequestInfoTime.
        :rtype: list[int]
        """
        return self._day_part

    @day_part.setter
    def day_part(self, day_part):
        r"""Sets the day_part of this ChangeVulScanPolicyRequestInfoTime.

        **参数解释**: 扫描日期或者星期列表 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值31 **默认取值**: 不涉及 

        :param day_part: The day_part of this ChangeVulScanPolicyRequestInfoTime.
        :type day_part: list[int]
        """
        self._day_part = day_part

    @property
    def hour_part(self):
        r"""Gets the hour_part of this ChangeVulScanPolicyRequestInfoTime.

        **参数解释**: 扫描时间的小时部分 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值11 **默认取值**: 不涉及 

        :return: The hour_part of this ChangeVulScanPolicyRequestInfoTime.
        :rtype: int
        """
        return self._hour_part

    @hour_part.setter
    def hour_part(self, hour_part):
        r"""Sets the hour_part of this ChangeVulScanPolicyRequestInfoTime.

        **参数解释**: 扫描时间的小时部分 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值11 **默认取值**: 不涉及 

        :param hour_part: The hour_part of this ChangeVulScanPolicyRequestInfoTime.
        :type hour_part: int
        """
        self._hour_part = hour_part

    @property
    def minute_part(self):
        r"""Gets the minute_part of this ChangeVulScanPolicyRequestInfoTime.

        **参数解释**: 扫描时间的分钟部分 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值59 **默认取值**: 不涉及 

        :return: The minute_part of this ChangeVulScanPolicyRequestInfoTime.
        :rtype: int
        """
        return self._minute_part

    @minute_part.setter
    def minute_part(self, minute_part):
        r"""Sets the minute_part of this ChangeVulScanPolicyRequestInfoTime.

        **参数解释**: 扫描时间的分钟部分 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值59 **默认取值**: 不涉及 

        :param minute_part: The minute_part of this ChangeVulScanPolicyRequestInfoTime.
        :type minute_part: int
        """
        self._minute_part = minute_part

    @property
    def next_scan_time(self):
        r"""Gets the next_scan_time of this ChangeVulScanPolicyRequestInfoTime.

        **参数解释**: 下一次扫描时间 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2^63-1 **默认取值**: 不涉及 

        :return: The next_scan_time of this ChangeVulScanPolicyRequestInfoTime.
        :rtype: int
        """
        return self._next_scan_time

    @next_scan_time.setter
    def next_scan_time(self, next_scan_time):
        r"""Sets the next_scan_time of this ChangeVulScanPolicyRequestInfoTime.

        **参数解释**: 下一次扫描时间 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2^63-1 **默认取值**: 不涉及 

        :param next_scan_time: The next_scan_time of this ChangeVulScanPolicyRequestInfoTime.
        :type next_scan_time: int
        """
        self._next_scan_time = next_scan_time

    @property
    def timezone_offset(self):
        r"""Gets the timezone_offset of this ChangeVulScanPolicyRequestInfoTime.

        **参数解释**: 距离标准时区的差值，如东八区（GMT+8）为-480 **约束限制**: 不涉及 **取值范围**: 最小值-840，最大值720 **默认取值**: 不涉及 

        :return: The timezone_offset of this ChangeVulScanPolicyRequestInfoTime.
        :rtype: int
        """
        return self._timezone_offset

    @timezone_offset.setter
    def timezone_offset(self, timezone_offset):
        r"""Sets the timezone_offset of this ChangeVulScanPolicyRequestInfoTime.

        **参数解释**: 距离标准时区的差值，如东八区（GMT+8）为-480 **约束限制**: 不涉及 **取值范围**: 最小值-840，最大值720 **默认取值**: 不涉及 

        :param timezone_offset: The timezone_offset of this ChangeVulScanPolicyRequestInfoTime.
        :type timezone_offset: int
        """
        self._timezone_offset = timezone_offset

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
        if not isinstance(other, ChangeVulScanPolicyRequestInfoTime):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
