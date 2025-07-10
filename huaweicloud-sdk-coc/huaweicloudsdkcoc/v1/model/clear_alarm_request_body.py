# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClearAlarmRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'remarks': 'str',
        'alarm_ids': 'str',
        'is_service_interrupt': 'bool',
        'start_time': 'int',
        'fault_recovery_time': 'int'
    }

    attribute_map = {
        'remarks': 'remarks',
        'alarm_ids': 'alarm_ids',
        'is_service_interrupt': 'is_service_interrupt',
        'start_time': 'start_time',
        'fault_recovery_time': 'fault_recovery_time'
    }

    def __init__(self, remarks=None, alarm_ids=None, is_service_interrupt=None, start_time=None, fault_recovery_time=None):
        r"""ClearAlarmRequestBody

        The model defined in huaweicloud sdk

        :param remarks: 清除备注
        :type remarks: str
        :param alarm_ids: 告警id拼接字符串，以”，“分隔
        :type alarm_ids: str
        :param is_service_interrupt: 业务是否中断
        :type is_service_interrupt: bool
        :param start_time: 故障发生时间
        :type start_time: int
        :param fault_recovery_time: 故障恢复时间
        :type fault_recovery_time: int
        """
        
        

        self._remarks = None
        self._alarm_ids = None
        self._is_service_interrupt = None
        self._start_time = None
        self._fault_recovery_time = None
        self.discriminator = None

        if remarks is not None:
            self.remarks = remarks
        self.alarm_ids = alarm_ids
        if is_service_interrupt is not None:
            self.is_service_interrupt = is_service_interrupt
        if start_time is not None:
            self.start_time = start_time
        if fault_recovery_time is not None:
            self.fault_recovery_time = fault_recovery_time

    @property
    def remarks(self):
        r"""Gets the remarks of this ClearAlarmRequestBody.

        清除备注

        :return: The remarks of this ClearAlarmRequestBody.
        :rtype: str
        """
        return self._remarks

    @remarks.setter
    def remarks(self, remarks):
        r"""Sets the remarks of this ClearAlarmRequestBody.

        清除备注

        :param remarks: The remarks of this ClearAlarmRequestBody.
        :type remarks: str
        """
        self._remarks = remarks

    @property
    def alarm_ids(self):
        r"""Gets the alarm_ids of this ClearAlarmRequestBody.

        告警id拼接字符串，以”，“分隔

        :return: The alarm_ids of this ClearAlarmRequestBody.
        :rtype: str
        """
        return self._alarm_ids

    @alarm_ids.setter
    def alarm_ids(self, alarm_ids):
        r"""Sets the alarm_ids of this ClearAlarmRequestBody.

        告警id拼接字符串，以”，“分隔

        :param alarm_ids: The alarm_ids of this ClearAlarmRequestBody.
        :type alarm_ids: str
        """
        self._alarm_ids = alarm_ids

    @property
    def is_service_interrupt(self):
        r"""Gets the is_service_interrupt of this ClearAlarmRequestBody.

        业务是否中断

        :return: The is_service_interrupt of this ClearAlarmRequestBody.
        :rtype: bool
        """
        return self._is_service_interrupt

    @is_service_interrupt.setter
    def is_service_interrupt(self, is_service_interrupt):
        r"""Sets the is_service_interrupt of this ClearAlarmRequestBody.

        业务是否中断

        :param is_service_interrupt: The is_service_interrupt of this ClearAlarmRequestBody.
        :type is_service_interrupt: bool
        """
        self._is_service_interrupt = is_service_interrupt

    @property
    def start_time(self):
        r"""Gets the start_time of this ClearAlarmRequestBody.

        故障发生时间

        :return: The start_time of this ClearAlarmRequestBody.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ClearAlarmRequestBody.

        故障发生时间

        :param start_time: The start_time of this ClearAlarmRequestBody.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def fault_recovery_time(self):
        r"""Gets the fault_recovery_time of this ClearAlarmRequestBody.

        故障恢复时间

        :return: The fault_recovery_time of this ClearAlarmRequestBody.
        :rtype: int
        """
        return self._fault_recovery_time

    @fault_recovery_time.setter
    def fault_recovery_time(self, fault_recovery_time):
        r"""Sets the fault_recovery_time of this ClearAlarmRequestBody.

        故障恢复时间

        :param fault_recovery_time: The fault_recovery_time of this ClearAlarmRequestBody.
        :type fault_recovery_time: int
        """
        self._fault_recovery_time = fault_recovery_time

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
        if not isinstance(other, ClearAlarmRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
