# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListBackgroundTasksRequest:

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
        'start': 'int',
        'limit': 'int',
        'begin_time': 'str',
        'end_time': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'start': 'start',
        'limit': 'limit',
        'begin_time': 'begin_time',
        'end_time': 'end_time'
    }

    def __init__(self, instance_id=None, start=None, limit=None, begin_time=None, end_time=None):
        """ListBackgroundTasksRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID。
        :type instance_id: str
        :param start: 开启查询的任务编号。
        :type start: int
        :param limit: 查询的任务个数。
        :type limit: int
        :param begin_time: 查询任务的最小时间，格式为YYYYMMDDHHmmss。
        :type begin_time: str
        :param end_time: 查询任务的最大时间，格式为YYYYMMDDHHmmss。
        :type end_time: str
        """
        
        

        self._instance_id = None
        self._start = None
        self._limit = None
        self._begin_time = None
        self._end_time = None
        self.discriminator = None

        self.instance_id = instance_id
        if start is not None:
            self.start = start
        if limit is not None:
            self.limit = limit
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def instance_id(self):
        """Gets the instance_id of this ListBackgroundTasksRequest.

        实例ID。

        :return: The instance_id of this ListBackgroundTasksRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListBackgroundTasksRequest.

        实例ID。

        :param instance_id: The instance_id of this ListBackgroundTasksRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def start(self):
        """Gets the start of this ListBackgroundTasksRequest.

        开启查询的任务编号。

        :return: The start of this ListBackgroundTasksRequest.
        :rtype: int
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this ListBackgroundTasksRequest.

        开启查询的任务编号。

        :param start: The start of this ListBackgroundTasksRequest.
        :type start: int
        """
        self._start = start

    @property
    def limit(self):
        """Gets the limit of this ListBackgroundTasksRequest.

        查询的任务个数。

        :return: The limit of this ListBackgroundTasksRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListBackgroundTasksRequest.

        查询的任务个数。

        :param limit: The limit of this ListBackgroundTasksRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def begin_time(self):
        """Gets the begin_time of this ListBackgroundTasksRequest.

        查询任务的最小时间，格式为YYYYMMDDHHmmss。

        :return: The begin_time of this ListBackgroundTasksRequest.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        """Sets the begin_time of this ListBackgroundTasksRequest.

        查询任务的最小时间，格式为YYYYMMDDHHmmss。

        :param begin_time: The begin_time of this ListBackgroundTasksRequest.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        """Gets the end_time of this ListBackgroundTasksRequest.

        查询任务的最大时间，格式为YYYYMMDDHHmmss。

        :return: The end_time of this ListBackgroundTasksRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ListBackgroundTasksRequest.

        查询任务的最大时间，格式为YYYYMMDDHHmmss。

        :param end_time: The end_time of this ListBackgroundTasksRequest.
        :type end_time: str
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
        if not isinstance(other, ListBackgroundTasksRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
