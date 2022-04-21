# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskStatisticDetails:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'running_tasks_count': 'int',
        'abnormal_tasks_count': 'int',
        'terminated_tasks_count': 'int',
        'completed_tasks_count': 'int'
    }

    attribute_map = {
        'running_tasks_count': 'running_tasks_count',
        'abnormal_tasks_count': 'abnormal_tasks_count',
        'terminated_tasks_count': 'terminated_tasks_count',
        'completed_tasks_count': 'completed_tasks_count'
    }

    def __init__(self, running_tasks_count=None, abnormal_tasks_count=None, terminated_tasks_count=None, completed_tasks_count=None):
        """TaskStatisticDetails

        The model defined in huaweicloud sdk

        :param running_tasks_count: 运行任务数量
        :type running_tasks_count: int
        :param abnormal_tasks_count: 异常任务数量
        :type abnormal_tasks_count: int
        :param terminated_tasks_count: 终止任务数量
        :type terminated_tasks_count: int
        :param completed_tasks_count: 成功任务数量
        :type completed_tasks_count: int
        """
        
        

        self._running_tasks_count = None
        self._abnormal_tasks_count = None
        self._terminated_tasks_count = None
        self._completed_tasks_count = None
        self.discriminator = None

        if running_tasks_count is not None:
            self.running_tasks_count = running_tasks_count
        if abnormal_tasks_count is not None:
            self.abnormal_tasks_count = abnormal_tasks_count
        if terminated_tasks_count is not None:
            self.terminated_tasks_count = terminated_tasks_count
        if completed_tasks_count is not None:
            self.completed_tasks_count = completed_tasks_count

    @property
    def running_tasks_count(self):
        """Gets the running_tasks_count of this TaskStatisticDetails.

        运行任务数量

        :return: The running_tasks_count of this TaskStatisticDetails.
        :rtype: int
        """
        return self._running_tasks_count

    @running_tasks_count.setter
    def running_tasks_count(self, running_tasks_count):
        """Sets the running_tasks_count of this TaskStatisticDetails.

        运行任务数量

        :param running_tasks_count: The running_tasks_count of this TaskStatisticDetails.
        :type running_tasks_count: int
        """
        self._running_tasks_count = running_tasks_count

    @property
    def abnormal_tasks_count(self):
        """Gets the abnormal_tasks_count of this TaskStatisticDetails.

        异常任务数量

        :return: The abnormal_tasks_count of this TaskStatisticDetails.
        :rtype: int
        """
        return self._abnormal_tasks_count

    @abnormal_tasks_count.setter
    def abnormal_tasks_count(self, abnormal_tasks_count):
        """Sets the abnormal_tasks_count of this TaskStatisticDetails.

        异常任务数量

        :param abnormal_tasks_count: The abnormal_tasks_count of this TaskStatisticDetails.
        :type abnormal_tasks_count: int
        """
        self._abnormal_tasks_count = abnormal_tasks_count

    @property
    def terminated_tasks_count(self):
        """Gets the terminated_tasks_count of this TaskStatisticDetails.

        终止任务数量

        :return: The terminated_tasks_count of this TaskStatisticDetails.
        :rtype: int
        """
        return self._terminated_tasks_count

    @terminated_tasks_count.setter
    def terminated_tasks_count(self, terminated_tasks_count):
        """Sets the terminated_tasks_count of this TaskStatisticDetails.

        终止任务数量

        :param terminated_tasks_count: The terminated_tasks_count of this TaskStatisticDetails.
        :type terminated_tasks_count: int
        """
        self._terminated_tasks_count = terminated_tasks_count

    @property
    def completed_tasks_count(self):
        """Gets the completed_tasks_count of this TaskStatisticDetails.

        成功任务数量

        :return: The completed_tasks_count of this TaskStatisticDetails.
        :rtype: int
        """
        return self._completed_tasks_count

    @completed_tasks_count.setter
    def completed_tasks_count(self, completed_tasks_count):
        """Sets the completed_tasks_count of this TaskStatisticDetails.

        成功任务数量

        :param completed_tasks_count: The completed_tasks_count of this TaskStatisticDetails.
        :type completed_tasks_count: int
        """
        self._completed_tasks_count = completed_tasks_count

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
        if not isinstance(other, TaskStatisticDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
