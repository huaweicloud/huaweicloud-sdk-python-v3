# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StopMigrationTaskResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'result': 'str',
        'task_id': 'str'
    }

    attribute_map = {
        'result': 'result',
        'task_id': 'task_id'
    }

    def __init__(self, result=None, task_id=None):
        """StopMigrationTaskResult

        The model defined in huaweicloud sdk

        :param result: 下发停止迁移任务操作结果。
        :type result: str
        :param task_id: 数据迁移任务ID。
        :type task_id: str
        """
        
        

        self._result = None
        self._task_id = None
        self.discriminator = None

        if result is not None:
            self.result = result
        if task_id is not None:
            self.task_id = task_id

    @property
    def result(self):
        """Gets the result of this StopMigrationTaskResult.

        下发停止迁移任务操作结果。

        :return: The result of this StopMigrationTaskResult.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this StopMigrationTaskResult.

        下发停止迁移任务操作结果。

        :param result: The result of this StopMigrationTaskResult.
        :type result: str
        """
        self._result = result

    @property
    def task_id(self):
        """Gets the task_id of this StopMigrationTaskResult.

        数据迁移任务ID。

        :return: The task_id of this StopMigrationTaskResult.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this StopMigrationTaskResult.

        数据迁移任务ID。

        :param task_id: The task_id of this StopMigrationTaskResult.
        :type task_id: str
        """
        self._task_id = task_id

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
        if not isinstance(other, StopMigrationTaskResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
