# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TasksSuccessRateQuery:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'start_date': 'str',
        'end_date': 'str',
        'task_ids': 'list[str]'
    }

    attribute_map = {
        'start_date': 'start_date',
        'end_date': 'end_date',
        'task_ids': 'task_ids'
    }

    def __init__(self, start_date=None, end_date=None, task_ids=None):
        """TasksSuccessRateQuery

        The model defined in huaweicloud sdk

        :param start_date: 部署应用开始时间范围的左边界（包含），格式yyyy-MM-dd
        :type start_date: str
        :param end_date: 部署应用开始时间范围的右边界（包含），格式yyyy-MM-dd 。最大时间范围为1年。
        :type end_date: str
        :param task_ids: 任务id列表
        :type task_ids: list[str]
        """
        
        

        self._start_date = None
        self._end_date = None
        self._task_ids = None
        self.discriminator = None

        self.start_date = start_date
        self.end_date = end_date
        self.task_ids = task_ids

    @property
    def start_date(self):
        """Gets the start_date of this TasksSuccessRateQuery.

        部署应用开始时间范围的左边界（包含），格式yyyy-MM-dd

        :return: The start_date of this TasksSuccessRateQuery.
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this TasksSuccessRateQuery.

        部署应用开始时间范围的左边界（包含），格式yyyy-MM-dd

        :param start_date: The start_date of this TasksSuccessRateQuery.
        :type start_date: str
        """
        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this TasksSuccessRateQuery.

        部署应用开始时间范围的右边界（包含），格式yyyy-MM-dd 。最大时间范围为1年。

        :return: The end_date of this TasksSuccessRateQuery.
        :rtype: str
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this TasksSuccessRateQuery.

        部署应用开始时间范围的右边界（包含），格式yyyy-MM-dd 。最大时间范围为1年。

        :param end_date: The end_date of this TasksSuccessRateQuery.
        :type end_date: str
        """
        self._end_date = end_date

    @property
    def task_ids(self):
        """Gets the task_ids of this TasksSuccessRateQuery.

        任务id列表

        :return: The task_ids of this TasksSuccessRateQuery.
        :rtype: list[str]
        """
        return self._task_ids

    @task_ids.setter
    def task_ids(self, task_ids):
        """Sets the task_ids of this TasksSuccessRateQuery.

        任务id列表

        :param task_ids: The task_ids of this TasksSuccessRateQuery.
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
        if not isinstance(other, TasksSuccessRateQuery):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
