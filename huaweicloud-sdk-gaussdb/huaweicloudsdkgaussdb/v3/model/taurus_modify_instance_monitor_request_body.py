# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaurusModifyInstanceMonitorRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'monitor_switch': 'bool',
        'period': 'int'
    }

    attribute_map = {
        'monitor_switch': 'monitor_switch',
        'period': 'period'
    }

    def __init__(self, monitor_switch=None, period=None):
        """TaurusModifyInstanceMonitorRequestBody

        The model defined in huaweicloud sdk

        :param monitor_switch: 实例秒级监控开关。  - true：开启 - false：关闭
        :type monitor_switch: bool
        :param period: 采集周期，仅在monitor_switch为true时生效。默认为5s。monitor_switch为false时，不传该参数。取值：  - 1：采集周期为1s。 - 5：采集周期为5s。
        :type period: int
        """
        
        

        self._monitor_switch = None
        self._period = None
        self.discriminator = None

        self.monitor_switch = monitor_switch
        if period is not None:
            self.period = period

    @property
    def monitor_switch(self):
        """Gets the monitor_switch of this TaurusModifyInstanceMonitorRequestBody.

        实例秒级监控开关。  - true：开启 - false：关闭

        :return: The monitor_switch of this TaurusModifyInstanceMonitorRequestBody.
        :rtype: bool
        """
        return self._monitor_switch

    @monitor_switch.setter
    def monitor_switch(self, monitor_switch):
        """Sets the monitor_switch of this TaurusModifyInstanceMonitorRequestBody.

        实例秒级监控开关。  - true：开启 - false：关闭

        :param monitor_switch: The monitor_switch of this TaurusModifyInstanceMonitorRequestBody.
        :type monitor_switch: bool
        """
        self._monitor_switch = monitor_switch

    @property
    def period(self):
        """Gets the period of this TaurusModifyInstanceMonitorRequestBody.

        采集周期，仅在monitor_switch为true时生效。默认为5s。monitor_switch为false时，不传该参数。取值：  - 1：采集周期为1s。 - 5：采集周期为5s。

        :return: The period of this TaurusModifyInstanceMonitorRequestBody.
        :rtype: int
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this TaurusModifyInstanceMonitorRequestBody.

        采集周期，仅在monitor_switch为true时生效。默认为5s。monitor_switch为false时，不传该参数。取值：  - 1：采集周期为1s。 - 5：采集周期为5s。

        :param period: The period of this TaurusModifyInstanceMonitorRequestBody.
        :type period: int
        """
        self._period = period

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
        if not isinstance(other, TaurusModifyInstanceMonitorRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
