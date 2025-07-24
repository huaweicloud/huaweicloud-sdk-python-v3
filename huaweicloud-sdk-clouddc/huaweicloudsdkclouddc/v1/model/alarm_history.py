# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AlarmHistory:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alarm_record_id': 'str',
        'alarm_id': 'str',
        'alarm_name': 'str',
        'alarm_status': 'str',
        'alarm_level': 'int',
        'begin_time': 'int',
        'end_time': 'int',
        'last_alarm_time': 'int',
        'metric': 'Metric'
    }

    attribute_map = {
        'alarm_record_id': 'alarm_record_id',
        'alarm_id': 'alarm_id',
        'alarm_name': 'alarm_name',
        'alarm_status': 'alarm_status',
        'alarm_level': 'alarm_level',
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'last_alarm_time': 'last_alarm_time',
        'metric': 'metric'
    }

    def __init__(self, alarm_record_id=None, alarm_id=None, alarm_name=None, alarm_status=None, alarm_level=None, begin_time=None, end_time=None, last_alarm_time=None, metric=None):
        r"""AlarmHistory

        The model defined in huaweicloud sdk

        :param alarm_record_id: 告警记录ID
        :type alarm_record_id: str
        :param alarm_id: 告警ID
        :type alarm_id: str
        :param alarm_name: 告警名称
        :type alarm_name: str
        :param alarm_status: 告警状态
        :type alarm_status: str
        :param alarm_level: 告警级别
        :type alarm_level: int
        :param begin_time: 告警开始时间，Unix时间戳
        :type begin_time: int
        :param end_time: 告警结束时间，Unix时间戳
        :type end_time: int
        :param last_alarm_time: 最后一次告警时间，Unix时间戳
        :type last_alarm_time: int
        :param metric: 
        :type metric: :class:`huaweicloudsdkclouddc.v1.Metric`
        """
        
        

        self._alarm_record_id = None
        self._alarm_id = None
        self._alarm_name = None
        self._alarm_status = None
        self._alarm_level = None
        self._begin_time = None
        self._end_time = None
        self._last_alarm_time = None
        self._metric = None
        self.discriminator = None

        if alarm_record_id is not None:
            self.alarm_record_id = alarm_record_id
        if alarm_id is not None:
            self.alarm_id = alarm_id
        if alarm_name is not None:
            self.alarm_name = alarm_name
        if alarm_status is not None:
            self.alarm_status = alarm_status
        if alarm_level is not None:
            self.alarm_level = alarm_level
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time
        if last_alarm_time is not None:
            self.last_alarm_time = last_alarm_time
        if metric is not None:
            self.metric = metric

    @property
    def alarm_record_id(self):
        r"""Gets the alarm_record_id of this AlarmHistory.

        告警记录ID

        :return: The alarm_record_id of this AlarmHistory.
        :rtype: str
        """
        return self._alarm_record_id

    @alarm_record_id.setter
    def alarm_record_id(self, alarm_record_id):
        r"""Sets the alarm_record_id of this AlarmHistory.

        告警记录ID

        :param alarm_record_id: The alarm_record_id of this AlarmHistory.
        :type alarm_record_id: str
        """
        self._alarm_record_id = alarm_record_id

    @property
    def alarm_id(self):
        r"""Gets the alarm_id of this AlarmHistory.

        告警ID

        :return: The alarm_id of this AlarmHistory.
        :rtype: str
        """
        return self._alarm_id

    @alarm_id.setter
    def alarm_id(self, alarm_id):
        r"""Sets the alarm_id of this AlarmHistory.

        告警ID

        :param alarm_id: The alarm_id of this AlarmHistory.
        :type alarm_id: str
        """
        self._alarm_id = alarm_id

    @property
    def alarm_name(self):
        r"""Gets the alarm_name of this AlarmHistory.

        告警名称

        :return: The alarm_name of this AlarmHistory.
        :rtype: str
        """
        return self._alarm_name

    @alarm_name.setter
    def alarm_name(self, alarm_name):
        r"""Sets the alarm_name of this AlarmHistory.

        告警名称

        :param alarm_name: The alarm_name of this AlarmHistory.
        :type alarm_name: str
        """
        self._alarm_name = alarm_name

    @property
    def alarm_status(self):
        r"""Gets the alarm_status of this AlarmHistory.

        告警状态

        :return: The alarm_status of this AlarmHistory.
        :rtype: str
        """
        return self._alarm_status

    @alarm_status.setter
    def alarm_status(self, alarm_status):
        r"""Sets the alarm_status of this AlarmHistory.

        告警状态

        :param alarm_status: The alarm_status of this AlarmHistory.
        :type alarm_status: str
        """
        self._alarm_status = alarm_status

    @property
    def alarm_level(self):
        r"""Gets the alarm_level of this AlarmHistory.

        告警级别

        :return: The alarm_level of this AlarmHistory.
        :rtype: int
        """
        return self._alarm_level

    @alarm_level.setter
    def alarm_level(self, alarm_level):
        r"""Sets the alarm_level of this AlarmHistory.

        告警级别

        :param alarm_level: The alarm_level of this AlarmHistory.
        :type alarm_level: int
        """
        self._alarm_level = alarm_level

    @property
    def begin_time(self):
        r"""Gets the begin_time of this AlarmHistory.

        告警开始时间，Unix时间戳

        :return: The begin_time of this AlarmHistory.
        :rtype: int
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        r"""Sets the begin_time of this AlarmHistory.

        告警开始时间，Unix时间戳

        :param begin_time: The begin_time of this AlarmHistory.
        :type begin_time: int
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        r"""Gets the end_time of this AlarmHistory.

        告警结束时间，Unix时间戳

        :return: The end_time of this AlarmHistory.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this AlarmHistory.

        告警结束时间，Unix时间戳

        :param end_time: The end_time of this AlarmHistory.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def last_alarm_time(self):
        r"""Gets the last_alarm_time of this AlarmHistory.

        最后一次告警时间，Unix时间戳

        :return: The last_alarm_time of this AlarmHistory.
        :rtype: int
        """
        return self._last_alarm_time

    @last_alarm_time.setter
    def last_alarm_time(self, last_alarm_time):
        r"""Sets the last_alarm_time of this AlarmHistory.

        最后一次告警时间，Unix时间戳

        :param last_alarm_time: The last_alarm_time of this AlarmHistory.
        :type last_alarm_time: int
        """
        self._last_alarm_time = last_alarm_time

    @property
    def metric(self):
        r"""Gets the metric of this AlarmHistory.

        :return: The metric of this AlarmHistory.
        :rtype: :class:`huaweicloudsdkclouddc.v1.Metric`
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        r"""Sets the metric of this AlarmHistory.

        :param metric: The metric of this AlarmHistory.
        :type metric: :class:`huaweicloudsdkclouddc.v1.Metric`
        """
        self._metric = metric

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
        if not isinstance(other, AlarmHistory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
