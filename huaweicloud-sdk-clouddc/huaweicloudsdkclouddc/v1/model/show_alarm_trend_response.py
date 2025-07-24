# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAlarmTrendResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'fault_hosts': 'list[FaultHostInfo]',
        'alarm_daily_new_trends': 'list[AlarmDailyTrend]'
    }

    attribute_map = {
        'fault_hosts': 'fault_hosts',
        'alarm_daily_new_trends': 'alarm_daily_new_trends'
    }

    def __init__(self, fault_hosts=None, alarm_daily_new_trends=None):
        r"""ShowAlarmTrendResponse

        The model defined in huaweicloud sdk

        :param fault_hosts: 故障服务器数趋势
        :type fault_hosts: list[:class:`huaweicloudsdkclouddc.v1.FaultHostInfo`]
        :param alarm_daily_new_trends: 告警每日新增趋势
        :type alarm_daily_new_trends: list[:class:`huaweicloudsdkclouddc.v1.AlarmDailyTrend`]
        """
        
        super(ShowAlarmTrendResponse, self).__init__()

        self._fault_hosts = None
        self._alarm_daily_new_trends = None
        self.discriminator = None

        if fault_hosts is not None:
            self.fault_hosts = fault_hosts
        if alarm_daily_new_trends is not None:
            self.alarm_daily_new_trends = alarm_daily_new_trends

    @property
    def fault_hosts(self):
        r"""Gets the fault_hosts of this ShowAlarmTrendResponse.

        故障服务器数趋势

        :return: The fault_hosts of this ShowAlarmTrendResponse.
        :rtype: list[:class:`huaweicloudsdkclouddc.v1.FaultHostInfo`]
        """
        return self._fault_hosts

    @fault_hosts.setter
    def fault_hosts(self, fault_hosts):
        r"""Sets the fault_hosts of this ShowAlarmTrendResponse.

        故障服务器数趋势

        :param fault_hosts: The fault_hosts of this ShowAlarmTrendResponse.
        :type fault_hosts: list[:class:`huaweicloudsdkclouddc.v1.FaultHostInfo`]
        """
        self._fault_hosts = fault_hosts

    @property
    def alarm_daily_new_trends(self):
        r"""Gets the alarm_daily_new_trends of this ShowAlarmTrendResponse.

        告警每日新增趋势

        :return: The alarm_daily_new_trends of this ShowAlarmTrendResponse.
        :rtype: list[:class:`huaweicloudsdkclouddc.v1.AlarmDailyTrend`]
        """
        return self._alarm_daily_new_trends

    @alarm_daily_new_trends.setter
    def alarm_daily_new_trends(self, alarm_daily_new_trends):
        r"""Sets the alarm_daily_new_trends of this ShowAlarmTrendResponse.

        告警每日新增趋势

        :param alarm_daily_new_trends: The alarm_daily_new_trends of this ShowAlarmTrendResponse.
        :type alarm_daily_new_trends: list[:class:`huaweicloudsdkclouddc.v1.AlarmDailyTrend`]
        """
        self._alarm_daily_new_trends = alarm_daily_new_trends

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
        if not isinstance(other, ShowAlarmTrendResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
