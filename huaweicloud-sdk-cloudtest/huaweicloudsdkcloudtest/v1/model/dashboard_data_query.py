# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DashboardDataQuery:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'end_time': 'int',
        'page_num': 'int',
        'page_size': 'int',
        'start_time': 'int',
        'task_ids': 'list[str]'
    }

    attribute_map = {
        'end_time': 'end_time',
        'page_num': 'page_num',
        'page_size': 'page_size',
        'start_time': 'start_time',
        'task_ids': 'task_ids'
    }

    def __init__(self, end_time=None, page_num=None, page_size=None, start_time=None, task_ids=None):
        """DashboardDataQuery

        The model defined in huaweicloud sdk

        :param end_time: 查询结束时间
        :type end_time: int
        :param page_num: 分页参数，页码
        :type page_num: int
        :param page_size: 分页参数，每页大小
        :type page_size: int
        :param start_time: 查询开始时间
        :type start_time: int
        :param task_ids: 任务Id列表
        :type task_ids: list[str]
        """
        
        

        self._end_time = None
        self._page_num = None
        self._page_size = None
        self._start_time = None
        self._task_ids = None
        self.discriminator = None

        if end_time is not None:
            self.end_time = end_time
        if page_num is not None:
            self.page_num = page_num
        if page_size is not None:
            self.page_size = page_size
        if start_time is not None:
            self.start_time = start_time
        if task_ids is not None:
            self.task_ids = task_ids

    @property
    def end_time(self):
        """Gets the end_time of this DashboardDataQuery.

        查询结束时间

        :return: The end_time of this DashboardDataQuery.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this DashboardDataQuery.

        查询结束时间

        :param end_time: The end_time of this DashboardDataQuery.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def page_num(self):
        """Gets the page_num of this DashboardDataQuery.

        分页参数，页码

        :return: The page_num of this DashboardDataQuery.
        :rtype: int
        """
        return self._page_num

    @page_num.setter
    def page_num(self, page_num):
        """Sets the page_num of this DashboardDataQuery.

        分页参数，页码

        :param page_num: The page_num of this DashboardDataQuery.
        :type page_num: int
        """
        self._page_num = page_num

    @property
    def page_size(self):
        """Gets the page_size of this DashboardDataQuery.

        分页参数，每页大小

        :return: The page_size of this DashboardDataQuery.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this DashboardDataQuery.

        分页参数，每页大小

        :param page_size: The page_size of this DashboardDataQuery.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def start_time(self):
        """Gets the start_time of this DashboardDataQuery.

        查询开始时间

        :return: The start_time of this DashboardDataQuery.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this DashboardDataQuery.

        查询开始时间

        :param start_time: The start_time of this DashboardDataQuery.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def task_ids(self):
        """Gets the task_ids of this DashboardDataQuery.

        任务Id列表

        :return: The task_ids of this DashboardDataQuery.
        :rtype: list[str]
        """
        return self._task_ids

    @task_ids.setter
    def task_ids(self, task_ids):
        """Sets the task_ids of this DashboardDataQuery.

        任务Id列表

        :param task_ids: The task_ids of this DashboardDataQuery.
        :type task_ids: list[str]
        """
        self._task_ids = task_ids

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
        if not isinstance(other, DashboardDataQuery):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
