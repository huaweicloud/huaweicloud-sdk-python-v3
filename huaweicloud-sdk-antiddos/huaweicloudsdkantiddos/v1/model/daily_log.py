# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DailyLog:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'start_time': 'int',
        'end_time': 'int',
        'status': 'int',
        'trigger_bps': 'int',
        'trigger_pps': 'int',
        'trigger_http_pps': 'int'
    }

    attribute_map = {
        'start_time': 'start_time',
        'end_time': 'end_time',
        'status': 'status',
        'trigger_bps': 'trigger_bps',
        'trigger_pps': 'trigger_pps',
        'trigger_http_pps': 'trigger_http_pps'
    }

    def __init__(self, start_time=None, end_time=None, status=None, trigger_bps=None, trigger_pps=None, trigger_http_pps=None):
        """DailyLog

        The model defined in huaweicloud sdk

        :param start_time: 开始时间
        :type start_time: int
        :param end_time: 结束时间
        :type end_time: int
        :param status: 防护状态，可选范围： - 1：表示清洗 - 2：表示黑洞
        :type status: int
        :param trigger_bps: 触发时流量
        :type trigger_bps: int
        :param trigger_pps: 触发时报文速率
        :type trigger_pps: int
        :param trigger_http_pps: 触发时HTTP请求速率
        :type trigger_http_pps: int
        """
        
        

        self._start_time = None
        self._end_time = None
        self._status = None
        self._trigger_bps = None
        self._trigger_pps = None
        self._trigger_http_pps = None
        self.discriminator = None

        self.start_time = start_time
        self.end_time = end_time
        self.status = status
        self.trigger_bps = trigger_bps
        self.trigger_pps = trigger_pps
        self.trigger_http_pps = trigger_http_pps

    @property
    def start_time(self):
        """Gets the start_time of this DailyLog.

        开始时间

        :return: The start_time of this DailyLog.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this DailyLog.

        开始时间

        :param start_time: The start_time of this DailyLog.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this DailyLog.

        结束时间

        :return: The end_time of this DailyLog.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this DailyLog.

        结束时间

        :param end_time: The end_time of this DailyLog.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def status(self):
        """Gets the status of this DailyLog.

        防护状态，可选范围： - 1：表示清洗 - 2：表示黑洞

        :return: The status of this DailyLog.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DailyLog.

        防护状态，可选范围： - 1：表示清洗 - 2：表示黑洞

        :param status: The status of this DailyLog.
        :type status: int
        """
        self._status = status

    @property
    def trigger_bps(self):
        """Gets the trigger_bps of this DailyLog.

        触发时流量

        :return: The trigger_bps of this DailyLog.
        :rtype: int
        """
        return self._trigger_bps

    @trigger_bps.setter
    def trigger_bps(self, trigger_bps):
        """Sets the trigger_bps of this DailyLog.

        触发时流量

        :param trigger_bps: The trigger_bps of this DailyLog.
        :type trigger_bps: int
        """
        self._trigger_bps = trigger_bps

    @property
    def trigger_pps(self):
        """Gets the trigger_pps of this DailyLog.

        触发时报文速率

        :return: The trigger_pps of this DailyLog.
        :rtype: int
        """
        return self._trigger_pps

    @trigger_pps.setter
    def trigger_pps(self, trigger_pps):
        """Sets the trigger_pps of this DailyLog.

        触发时报文速率

        :param trigger_pps: The trigger_pps of this DailyLog.
        :type trigger_pps: int
        """
        self._trigger_pps = trigger_pps

    @property
    def trigger_http_pps(self):
        """Gets the trigger_http_pps of this DailyLog.

        触发时HTTP请求速率

        :return: The trigger_http_pps of this DailyLog.
        :rtype: int
        """
        return self._trigger_http_pps

    @trigger_http_pps.setter
    def trigger_http_pps(self, trigger_http_pps):
        """Sets the trigger_http_pps of this DailyLog.

        触发时HTTP请求速率

        :param trigger_http_pps: The trigger_http_pps of this DailyLog.
        :type trigger_http_pps: int
        """
        self._trigger_http_pps = trigger_http_pps

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
        if not isinstance(other, DailyLog):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
