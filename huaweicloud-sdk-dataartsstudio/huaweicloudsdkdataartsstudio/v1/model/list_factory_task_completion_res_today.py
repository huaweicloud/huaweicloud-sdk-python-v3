# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFactoryTaskCompletionResToday:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'record_time': 'int',
        'task_completion_num': 'int'
    }

    attribute_map = {
        'record_time': 'record_time',
        'task_completion_num': 'task_completion_num'
    }

    def __init__(self, record_time=None, task_completion_num=None):
        """ListFactoryTaskCompletionResToday

        The model defined in huaweicloud sdk

        :param record_time: 整时的时间点
        :type record_time: int
        :param task_completion_num: 到当前时间点完成的任务数量
        :type task_completion_num: int
        """
        
        

        self._record_time = None
        self._task_completion_num = None
        self.discriminator = None

        if record_time is not None:
            self.record_time = record_time
        if task_completion_num is not None:
            self.task_completion_num = task_completion_num

    @property
    def record_time(self):
        """Gets the record_time of this ListFactoryTaskCompletionResToday.

        整时的时间点

        :return: The record_time of this ListFactoryTaskCompletionResToday.
        :rtype: int
        """
        return self._record_time

    @record_time.setter
    def record_time(self, record_time):
        """Sets the record_time of this ListFactoryTaskCompletionResToday.

        整时的时间点

        :param record_time: The record_time of this ListFactoryTaskCompletionResToday.
        :type record_time: int
        """
        self._record_time = record_time

    @property
    def task_completion_num(self):
        """Gets the task_completion_num of this ListFactoryTaskCompletionResToday.

        到当前时间点完成的任务数量

        :return: The task_completion_num of this ListFactoryTaskCompletionResToday.
        :rtype: int
        """
        return self._task_completion_num

    @task_completion_num.setter
    def task_completion_num(self, task_completion_num):
        """Sets the task_completion_num of this ListFactoryTaskCompletionResToday.

        到当前时间点完成的任务数量

        :param task_completion_num: The task_completion_num of this ListFactoryTaskCompletionResToday.
        :type task_completion_num: int
        """
        self._task_completion_num = task_completion_num

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
        if not isinstance(other, ListFactoryTaskCompletionResToday):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
