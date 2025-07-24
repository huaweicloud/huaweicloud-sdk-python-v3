# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AlarmDailyTrend:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alarm_date': 'datetime',
        'alarm_devices': 'list[AlarmDeviceInfo]',
        'alarm_levels': 'list[AlarmLevelInfo]'
    }

    attribute_map = {
        'alarm_date': 'alarm_date',
        'alarm_devices': 'alarm_devices',
        'alarm_levels': 'alarm_levels'
    }

    def __init__(self, alarm_date=None, alarm_devices=None, alarm_levels=None):
        r"""AlarmDailyTrend

        The model defined in huaweicloud sdk

        :param alarm_date: 告警时间
        :type alarm_date: datetime
        :param alarm_devices: 告警设备信息，包括设备类型及告警数量
        :type alarm_devices: list[:class:`huaweicloudsdkclouddc.v1.AlarmDeviceInfo`]
        :param alarm_levels: 告警级别
        :type alarm_levels: list[:class:`huaweicloudsdkclouddc.v1.AlarmLevelInfo`]
        """
        
        

        self._alarm_date = None
        self._alarm_devices = None
        self._alarm_levels = None
        self.discriminator = None

        if alarm_date is not None:
            self.alarm_date = alarm_date
        if alarm_devices is not None:
            self.alarm_devices = alarm_devices
        if alarm_levels is not None:
            self.alarm_levels = alarm_levels

    @property
    def alarm_date(self):
        r"""Gets the alarm_date of this AlarmDailyTrend.

        告警时间

        :return: The alarm_date of this AlarmDailyTrend.
        :rtype: datetime
        """
        return self._alarm_date

    @alarm_date.setter
    def alarm_date(self, alarm_date):
        r"""Sets the alarm_date of this AlarmDailyTrend.

        告警时间

        :param alarm_date: The alarm_date of this AlarmDailyTrend.
        :type alarm_date: datetime
        """
        self._alarm_date = alarm_date

    @property
    def alarm_devices(self):
        r"""Gets the alarm_devices of this AlarmDailyTrend.

        告警设备信息，包括设备类型及告警数量

        :return: The alarm_devices of this AlarmDailyTrend.
        :rtype: list[:class:`huaweicloudsdkclouddc.v1.AlarmDeviceInfo`]
        """
        return self._alarm_devices

    @alarm_devices.setter
    def alarm_devices(self, alarm_devices):
        r"""Sets the alarm_devices of this AlarmDailyTrend.

        告警设备信息，包括设备类型及告警数量

        :param alarm_devices: The alarm_devices of this AlarmDailyTrend.
        :type alarm_devices: list[:class:`huaweicloudsdkclouddc.v1.AlarmDeviceInfo`]
        """
        self._alarm_devices = alarm_devices

    @property
    def alarm_levels(self):
        r"""Gets the alarm_levels of this AlarmDailyTrend.

        告警级别

        :return: The alarm_levels of this AlarmDailyTrend.
        :rtype: list[:class:`huaweicloudsdkclouddc.v1.AlarmLevelInfo`]
        """
        return self._alarm_levels

    @alarm_levels.setter
    def alarm_levels(self, alarm_levels):
        r"""Sets the alarm_levels of this AlarmDailyTrend.

        告警级别

        :param alarm_levels: The alarm_levels of this AlarmDailyTrend.
        :type alarm_levels: list[:class:`huaweicloudsdkclouddc.v1.AlarmLevelInfo`]
        """
        self._alarm_levels = alarm_levels

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
        if not isinstance(other, AlarmDailyTrend):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
