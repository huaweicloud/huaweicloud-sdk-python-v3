# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListMonitorLogRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'task_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'begin_time': 'int',
        'end_time': 'int'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'task_id': 'task_id',
        'offset': 'offset',
        'limit': 'limit',
        'begin_time': 'begin_time',
        'end_time': 'end_time'
    }

    def __init__(self, instance_id=None, task_id=None, offset=None, limit=None, begin_time=None, end_time=None):
        """ListMonitorLogRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param task_id: 任务ID
        :type task_id: str
        :param offset: 偏移量，表示从此偏移量开始查询， offset大于等于1
        :type offset: int
        :param limit: 每页显示条目数量，最大数量999，超过999后只返回999
        :type limit: int
        :param begin_time: 日志查询的起始时间，格式timestamp(ms)，使用UTC时区
        :type begin_time: int
        :param end_time: 日志查询的结束时间，格式timestamp(ms)，使用UTC时区
        :type end_time: int
        """
        
        

        self._instance_id = None
        self._task_id = None
        self._offset = None
        self._limit = None
        self._begin_time = None
        self._end_time = None
        self.discriminator = None

        self.instance_id = instance_id
        self.task_id = task_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def instance_id(self):
        """Gets the instance_id of this ListMonitorLogRequest.

        实例ID

        :return: The instance_id of this ListMonitorLogRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListMonitorLogRequest.

        实例ID

        :param instance_id: The instance_id of this ListMonitorLogRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def task_id(self):
        """Gets the task_id of this ListMonitorLogRequest.

        任务ID

        :return: The task_id of this ListMonitorLogRequest.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this ListMonitorLogRequest.

        任务ID

        :param task_id: The task_id of this ListMonitorLogRequest.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def offset(self):
        """Gets the offset of this ListMonitorLogRequest.

        偏移量，表示从此偏移量开始查询， offset大于等于1

        :return: The offset of this ListMonitorLogRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListMonitorLogRequest.

        偏移量，表示从此偏移量开始查询， offset大于等于1

        :param offset: The offset of this ListMonitorLogRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListMonitorLogRequest.

        每页显示条目数量，最大数量999，超过999后只返回999

        :return: The limit of this ListMonitorLogRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListMonitorLogRequest.

        每页显示条目数量，最大数量999，超过999后只返回999

        :param limit: The limit of this ListMonitorLogRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def begin_time(self):
        """Gets the begin_time of this ListMonitorLogRequest.

        日志查询的起始时间，格式timestamp(ms)，使用UTC时区

        :return: The begin_time of this ListMonitorLogRequest.
        :rtype: int
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        """Sets the begin_time of this ListMonitorLogRequest.

        日志查询的起始时间，格式timestamp(ms)，使用UTC时区

        :param begin_time: The begin_time of this ListMonitorLogRequest.
        :type begin_time: int
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        """Gets the end_time of this ListMonitorLogRequest.

        日志查询的结束时间，格式timestamp(ms)，使用UTC时区

        :return: The end_time of this ListMonitorLogRequest.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ListMonitorLogRequest.

        日志查询的结束时间，格式timestamp(ms)，使用UTC时区

        :param end_time: The end_time of this ListMonitorLogRequest.
        :type end_time: int
        """
        self._end_time = end_time

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
        if not isinstance(other, ListMonitorLogRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
