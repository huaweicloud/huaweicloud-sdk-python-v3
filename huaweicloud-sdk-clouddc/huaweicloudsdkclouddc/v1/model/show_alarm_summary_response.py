# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAlarmSummaryResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alarm_levels': 'list[AlarmLevelInfo]',
        'alarm_devices': 'list[AlarmDeviceInfo]',
        'alarm_hosts': 'list[AlarmHost]',
        'alarm_groups': 'list[AlarmGroup]'
    }

    attribute_map = {
        'alarm_levels': 'alarm_levels',
        'alarm_devices': 'alarm_devices',
        'alarm_hosts': 'alarm_hosts',
        'alarm_groups': 'alarm_groups'
    }

    def __init__(self, alarm_levels=None, alarm_devices=None, alarm_hosts=None, alarm_groups=None):
        r"""ShowAlarmSummaryResponse

        The model defined in huaweicloud sdk

        :param alarm_levels: 告警级别
        :type alarm_levels: list[:class:`huaweicloudsdkclouddc.v1.AlarmLevelInfo`]
        :param alarm_devices: 告警设备信息，包括设备类型及告警数量
        :type alarm_devices: list[:class:`huaweicloudsdkclouddc.v1.AlarmDeviceInfo`]
        :param alarm_hosts: 故障服务器Top10
        :type alarm_hosts: list[:class:`huaweicloudsdkclouddc.v1.AlarmHost`]
        :param alarm_groups: 告警分组
        :type alarm_groups: list[:class:`huaweicloudsdkclouddc.v1.AlarmGroup`]
        """
        
        super(ShowAlarmSummaryResponse, self).__init__()

        self._alarm_levels = None
        self._alarm_devices = None
        self._alarm_hosts = None
        self._alarm_groups = None
        self.discriminator = None

        if alarm_levels is not None:
            self.alarm_levels = alarm_levels
        if alarm_devices is not None:
            self.alarm_devices = alarm_devices
        if alarm_hosts is not None:
            self.alarm_hosts = alarm_hosts
        if alarm_groups is not None:
            self.alarm_groups = alarm_groups

    @property
    def alarm_levels(self):
        r"""Gets the alarm_levels of this ShowAlarmSummaryResponse.

        告警级别

        :return: The alarm_levels of this ShowAlarmSummaryResponse.
        :rtype: list[:class:`huaweicloudsdkclouddc.v1.AlarmLevelInfo`]
        """
        return self._alarm_levels

    @alarm_levels.setter
    def alarm_levels(self, alarm_levels):
        r"""Sets the alarm_levels of this ShowAlarmSummaryResponse.

        告警级别

        :param alarm_levels: The alarm_levels of this ShowAlarmSummaryResponse.
        :type alarm_levels: list[:class:`huaweicloudsdkclouddc.v1.AlarmLevelInfo`]
        """
        self._alarm_levels = alarm_levels

    @property
    def alarm_devices(self):
        r"""Gets the alarm_devices of this ShowAlarmSummaryResponse.

        告警设备信息，包括设备类型及告警数量

        :return: The alarm_devices of this ShowAlarmSummaryResponse.
        :rtype: list[:class:`huaweicloudsdkclouddc.v1.AlarmDeviceInfo`]
        """
        return self._alarm_devices

    @alarm_devices.setter
    def alarm_devices(self, alarm_devices):
        r"""Sets the alarm_devices of this ShowAlarmSummaryResponse.

        告警设备信息，包括设备类型及告警数量

        :param alarm_devices: The alarm_devices of this ShowAlarmSummaryResponse.
        :type alarm_devices: list[:class:`huaweicloudsdkclouddc.v1.AlarmDeviceInfo`]
        """
        self._alarm_devices = alarm_devices

    @property
    def alarm_hosts(self):
        r"""Gets the alarm_hosts of this ShowAlarmSummaryResponse.

        故障服务器Top10

        :return: The alarm_hosts of this ShowAlarmSummaryResponse.
        :rtype: list[:class:`huaweicloudsdkclouddc.v1.AlarmHost`]
        """
        return self._alarm_hosts

    @alarm_hosts.setter
    def alarm_hosts(self, alarm_hosts):
        r"""Sets the alarm_hosts of this ShowAlarmSummaryResponse.

        故障服务器Top10

        :param alarm_hosts: The alarm_hosts of this ShowAlarmSummaryResponse.
        :type alarm_hosts: list[:class:`huaweicloudsdkclouddc.v1.AlarmHost`]
        """
        self._alarm_hosts = alarm_hosts

    @property
    def alarm_groups(self):
        r"""Gets the alarm_groups of this ShowAlarmSummaryResponse.

        告警分组

        :return: The alarm_groups of this ShowAlarmSummaryResponse.
        :rtype: list[:class:`huaweicloudsdkclouddc.v1.AlarmGroup`]
        """
        return self._alarm_groups

    @alarm_groups.setter
    def alarm_groups(self, alarm_groups):
        r"""Sets the alarm_groups of this ShowAlarmSummaryResponse.

        告警分组

        :param alarm_groups: The alarm_groups of this ShowAlarmSummaryResponse.
        :type alarm_groups: list[:class:`huaweicloudsdkclouddc.v1.AlarmGroup`]
        """
        self._alarm_groups = alarm_groups

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
        if not isinstance(other, ShowAlarmSummaryResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
