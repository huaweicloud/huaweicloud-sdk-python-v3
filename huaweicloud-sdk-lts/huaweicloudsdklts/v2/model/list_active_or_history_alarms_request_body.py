# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListActiveOrHistoryAlarmsRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'step': 'int',
        'whether_custom_field': 'bool',
        'start_time': 'int',
        'end_time': 'int',
        'time_range': 'str',
        'search': 'str',
        'alarm_level_ids': 'list[str]',
        'sort': 'Sort'
    }

    attribute_map = {
        'step': 'step',
        'whether_custom_field': 'whether_custom_field',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'time_range': 'time_range',
        'search': 'search',
        'alarm_level_ids': 'alarm_level_ids',
        'sort': 'sort'
    }

    def __init__(self, step=None, whether_custom_field=None, start_time=None, end_time=None, time_range=None, search=None, alarm_level_ids=None, sort=None):
        """ListActiveOrHistoryAlarmsRequestBody

        The model defined in huaweicloud sdk

        :param step: 关键字检索条件
        :type step: int
        :param whether_custom_field: 是否自定义查询时间段
        :type whether_custom_field: bool
        :param start_time: 自定义时间段开始时间(时间戳)
        :type start_time: int
        :param end_time: 自定义时间段结束时间(时间戳)
        :type end_time: int
        :param time_range: 非自定义时间段时间范围(单位为分钟)
        :type time_range: str
        :param search: 关键字检索条件
        :type search: str
        :param alarm_level_ids: 告警级别(\&quot;Critical\&quot;,\&quot;Major\&quot;,\&quot;Minor\&quot;,\&quot;Info\&quot;)
        :type alarm_level_ids: list[str]
        :param sort: 
        :type sort: :class:`huaweicloudsdklts.v2.Sort`
        """
        
        

        self._step = None
        self._whether_custom_field = None
        self._start_time = None
        self._end_time = None
        self._time_range = None
        self._search = None
        self._alarm_level_ids = None
        self._sort = None
        self.discriminator = None

        if step is not None:
            self.step = step
        self.whether_custom_field = whether_custom_field
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if time_range is not None:
            self.time_range = time_range
        if search is not None:
            self.search = search
        if alarm_level_ids is not None:
            self.alarm_level_ids = alarm_level_ids
        if sort is not None:
            self.sort = sort

    @property
    def step(self):
        """Gets the step of this ListActiveOrHistoryAlarmsRequestBody.

        关键字检索条件

        :return: The step of this ListActiveOrHistoryAlarmsRequestBody.
        :rtype: int
        """
        return self._step

    @step.setter
    def step(self, step):
        """Sets the step of this ListActiveOrHistoryAlarmsRequestBody.

        关键字检索条件

        :param step: The step of this ListActiveOrHistoryAlarmsRequestBody.
        :type step: int
        """
        self._step = step

    @property
    def whether_custom_field(self):
        """Gets the whether_custom_field of this ListActiveOrHistoryAlarmsRequestBody.

        是否自定义查询时间段

        :return: The whether_custom_field of this ListActiveOrHistoryAlarmsRequestBody.
        :rtype: bool
        """
        return self._whether_custom_field

    @whether_custom_field.setter
    def whether_custom_field(self, whether_custom_field):
        """Sets the whether_custom_field of this ListActiveOrHistoryAlarmsRequestBody.

        是否自定义查询时间段

        :param whether_custom_field: The whether_custom_field of this ListActiveOrHistoryAlarmsRequestBody.
        :type whether_custom_field: bool
        """
        self._whether_custom_field = whether_custom_field

    @property
    def start_time(self):
        """Gets the start_time of this ListActiveOrHistoryAlarmsRequestBody.

        自定义时间段开始时间(时间戳)

        :return: The start_time of this ListActiveOrHistoryAlarmsRequestBody.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ListActiveOrHistoryAlarmsRequestBody.

        自定义时间段开始时间(时间戳)

        :param start_time: The start_time of this ListActiveOrHistoryAlarmsRequestBody.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ListActiveOrHistoryAlarmsRequestBody.

        自定义时间段结束时间(时间戳)

        :return: The end_time of this ListActiveOrHistoryAlarmsRequestBody.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ListActiveOrHistoryAlarmsRequestBody.

        自定义时间段结束时间(时间戳)

        :param end_time: The end_time of this ListActiveOrHistoryAlarmsRequestBody.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def time_range(self):
        """Gets the time_range of this ListActiveOrHistoryAlarmsRequestBody.

        非自定义时间段时间范围(单位为分钟)

        :return: The time_range of this ListActiveOrHistoryAlarmsRequestBody.
        :rtype: str
        """
        return self._time_range

    @time_range.setter
    def time_range(self, time_range):
        """Sets the time_range of this ListActiveOrHistoryAlarmsRequestBody.

        非自定义时间段时间范围(单位为分钟)

        :param time_range: The time_range of this ListActiveOrHistoryAlarmsRequestBody.
        :type time_range: str
        """
        self._time_range = time_range

    @property
    def search(self):
        """Gets the search of this ListActiveOrHistoryAlarmsRequestBody.

        关键字检索条件

        :return: The search of this ListActiveOrHistoryAlarmsRequestBody.
        :rtype: str
        """
        return self._search

    @search.setter
    def search(self, search):
        """Sets the search of this ListActiveOrHistoryAlarmsRequestBody.

        关键字检索条件

        :param search: The search of this ListActiveOrHistoryAlarmsRequestBody.
        :type search: str
        """
        self._search = search

    @property
    def alarm_level_ids(self):
        """Gets the alarm_level_ids of this ListActiveOrHistoryAlarmsRequestBody.

        告警级别(\"Critical\",\"Major\",\"Minor\",\"Info\")

        :return: The alarm_level_ids of this ListActiveOrHistoryAlarmsRequestBody.
        :rtype: list[str]
        """
        return self._alarm_level_ids

    @alarm_level_ids.setter
    def alarm_level_ids(self, alarm_level_ids):
        """Sets the alarm_level_ids of this ListActiveOrHistoryAlarmsRequestBody.

        告警级别(\"Critical\",\"Major\",\"Minor\",\"Info\")

        :param alarm_level_ids: The alarm_level_ids of this ListActiveOrHistoryAlarmsRequestBody.
        :type alarm_level_ids: list[str]
        """
        self._alarm_level_ids = alarm_level_ids

    @property
    def sort(self):
        """Gets the sort of this ListActiveOrHistoryAlarmsRequestBody.

        :return: The sort of this ListActiveOrHistoryAlarmsRequestBody.
        :rtype: :class:`huaweicloudsdklts.v2.Sort`
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        """Sets the sort of this ListActiveOrHistoryAlarmsRequestBody.

        :param sort: The sort of this ListActiveOrHistoryAlarmsRequestBody.
        :type sort: :class:`huaweicloudsdklts.v2.Sort`
        """
        self._sort = sort

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
        if not isinstance(other, ListActiveOrHistoryAlarmsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
