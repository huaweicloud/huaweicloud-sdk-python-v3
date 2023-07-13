# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CollectSessionStatsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'qabot_id': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'interval': 'str',
        'time_zone': 'str'
    }

    attribute_map = {
        'qabot_id': 'qabot_id',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'interval': 'interval',
        'time_zone': 'time_zone'
    }

    def __init__(self, qabot_id=None, start_time=None, end_time=None, interval=None, time_zone=None):
        """CollectSessionStatsRequest

        The model defined in huaweicloud sdk

        :param qabot_id: qabot编号，UUID格式。
        :type qabot_id: str
        :param start_time: 查询的起始时间，long，UTC时间，默认值为0。
        :type start_time: str
        :param end_time: 查询的结束时间，long，UTC时间，默认值为当前时间的毫秒数。
        :type end_time: str
        :param interval: 统计周期目前支持month,week,day。
        :type interval: str
        :param time_zone: 请求所在时区，例如：中国东八区为\&quot;+08:00\&quot;；美国西五区为\&quot;-05:00\&quot;；默认为\&quot;UTC\&quot;。
        :type time_zone: str
        """
        
        

        self._qabot_id = None
        self._start_time = None
        self._end_time = None
        self._interval = None
        self._time_zone = None
        self.discriminator = None

        self.qabot_id = qabot_id
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if interval is not None:
            self.interval = interval
        if time_zone is not None:
            self.time_zone = time_zone

    @property
    def qabot_id(self):
        """Gets the qabot_id of this CollectSessionStatsRequest.

        qabot编号，UUID格式。

        :return: The qabot_id of this CollectSessionStatsRequest.
        :rtype: str
        """
        return self._qabot_id

    @qabot_id.setter
    def qabot_id(self, qabot_id):
        """Sets the qabot_id of this CollectSessionStatsRequest.

        qabot编号，UUID格式。

        :param qabot_id: The qabot_id of this CollectSessionStatsRequest.
        :type qabot_id: str
        """
        self._qabot_id = qabot_id

    @property
    def start_time(self):
        """Gets the start_time of this CollectSessionStatsRequest.

        查询的起始时间，long，UTC时间，默认值为0。

        :return: The start_time of this CollectSessionStatsRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this CollectSessionStatsRequest.

        查询的起始时间，long，UTC时间，默认值为0。

        :param start_time: The start_time of this CollectSessionStatsRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this CollectSessionStatsRequest.

        查询的结束时间，long，UTC时间，默认值为当前时间的毫秒数。

        :return: The end_time of this CollectSessionStatsRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this CollectSessionStatsRequest.

        查询的结束时间，long，UTC时间，默认值为当前时间的毫秒数。

        :param end_time: The end_time of this CollectSessionStatsRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def interval(self):
        """Gets the interval of this CollectSessionStatsRequest.

        统计周期目前支持month,week,day。

        :return: The interval of this CollectSessionStatsRequest.
        :rtype: str
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this CollectSessionStatsRequest.

        统计周期目前支持month,week,day。

        :param interval: The interval of this CollectSessionStatsRequest.
        :type interval: str
        """
        self._interval = interval

    @property
    def time_zone(self):
        """Gets the time_zone of this CollectSessionStatsRequest.

        请求所在时区，例如：中国东八区为\"+08:00\"；美国西五区为\"-05:00\"；默认为\"UTC\"。

        :return: The time_zone of this CollectSessionStatsRequest.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this CollectSessionStatsRequest.

        请求所在时区，例如：中国东八区为\"+08:00\"；美国西五区为\"-05:00\"；默认为\"UTC\"。

        :param time_zone: The time_zone of this CollectSessionStatsRequest.
        :type time_zone: str
        """
        self._time_zone = time_zone

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
        if not isinstance(other, CollectSessionStatsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
