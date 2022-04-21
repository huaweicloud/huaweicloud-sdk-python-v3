# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskSuccessRate:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'task_id': 'str',
        'task_name': 'str',
        'success_rate': 'str',
        'record_count': 'int',
        'success_record_count': 'int'
    }

    attribute_map = {
        'task_id': 'task_id',
        'task_name': 'task_name',
        'success_rate': 'success_rate',
        'record_count': 'record_count',
        'success_record_count': 'success_record_count'
    }

    def __init__(self, task_id=None, task_name=None, success_rate=None, record_count=None, success_record_count=None):
        """TaskSuccessRate

        The model defined in huaweicloud sdk

        :param task_id: 任务id
        :type task_id: str
        :param task_name: 任务名称
        :type task_name: str
        :param success_rate: 成功率
        :type success_rate: str
        :param record_count: 执行记录数
        :type record_count: int
        :param success_record_count: 成功的执行记录数
        :type success_record_count: int
        """
        
        

        self._task_id = None
        self._task_name = None
        self._success_rate = None
        self._record_count = None
        self._success_record_count = None
        self.discriminator = None

        if task_id is not None:
            self.task_id = task_id
        if task_name is not None:
            self.task_name = task_name
        if success_rate is not None:
            self.success_rate = success_rate
        if record_count is not None:
            self.record_count = record_count
        if success_record_count is not None:
            self.success_record_count = success_record_count

    @property
    def task_id(self):
        """Gets the task_id of this TaskSuccessRate.

        任务id

        :return: The task_id of this TaskSuccessRate.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this TaskSuccessRate.

        任务id

        :param task_id: The task_id of this TaskSuccessRate.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def task_name(self):
        """Gets the task_name of this TaskSuccessRate.

        任务名称

        :return: The task_name of this TaskSuccessRate.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        """Sets the task_name of this TaskSuccessRate.

        任务名称

        :param task_name: The task_name of this TaskSuccessRate.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def success_rate(self):
        """Gets the success_rate of this TaskSuccessRate.

        成功率

        :return: The success_rate of this TaskSuccessRate.
        :rtype: str
        """
        return self._success_rate

    @success_rate.setter
    def success_rate(self, success_rate):
        """Sets the success_rate of this TaskSuccessRate.

        成功率

        :param success_rate: The success_rate of this TaskSuccessRate.
        :type success_rate: str
        """
        self._success_rate = success_rate

    @property
    def record_count(self):
        """Gets the record_count of this TaskSuccessRate.

        执行记录数

        :return: The record_count of this TaskSuccessRate.
        :rtype: int
        """
        return self._record_count

    @record_count.setter
    def record_count(self, record_count):
        """Sets the record_count of this TaskSuccessRate.

        执行记录数

        :param record_count: The record_count of this TaskSuccessRate.
        :type record_count: int
        """
        self._record_count = record_count

    @property
    def success_record_count(self):
        """Gets the success_record_count of this TaskSuccessRate.

        成功的执行记录数

        :return: The success_record_count of this TaskSuccessRate.
        :rtype: int
        """
        return self._success_record_count

    @success_record_count.setter
    def success_record_count(self, success_record_count):
        """Sets the success_record_count of this TaskSuccessRate.

        成功的执行记录数

        :param success_record_count: The success_record_count of this TaskSuccessRate.
        :type success_record_count: int
        """
        self._success_record_count = success_record_count

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
        if not isinstance(other, TaskSuccessRate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
