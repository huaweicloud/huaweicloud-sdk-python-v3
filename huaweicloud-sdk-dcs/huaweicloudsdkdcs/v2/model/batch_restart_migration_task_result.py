# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchRestartMigrationTaskResult:

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
        'task_id': 'str',
        'error_msg': 'str',
        'error_code': 'str'
    }

    attribute_map = {
        'result': 'result',
        'task_id': 'task_id',
        'error_msg': 'error_msg',
        'error_code': 'error_code'
    }

    def __init__(self, result=None, task_id=None, error_msg=None, error_code=None):
        r"""BatchRestartMigrationTaskResult

        The model defined in huaweicloud sdk

        :param result: 下发重启迁移任务操作结果。
        :type result: str
        :param task_id: 数据迁移任务ID。
        :type task_id: str
        :param error_msg: 错误信息
        :type error_msg: str
        :param error_code: 错误码
        :type error_code: str
        """
        
        

        self._result = None
        self._task_id = None
        self._error_msg = None
        self._error_code = None
        self.discriminator = None

        if result is not None:
            self.result = result
        if task_id is not None:
            self.task_id = task_id
        if error_msg is not None:
            self.error_msg = error_msg
        if error_code is not None:
            self.error_code = error_code

    @property
    def result(self):
        r"""Gets the result of this BatchRestartMigrationTaskResult.

        下发重启迁移任务操作结果。

        :return: The result of this BatchRestartMigrationTaskResult.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this BatchRestartMigrationTaskResult.

        下发重启迁移任务操作结果。

        :param result: The result of this BatchRestartMigrationTaskResult.
        :type result: str
        """
        self._result = result

    @property
    def task_id(self):
        r"""Gets the task_id of this BatchRestartMigrationTaskResult.

        数据迁移任务ID。

        :return: The task_id of this BatchRestartMigrationTaskResult.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this BatchRestartMigrationTaskResult.

        数据迁移任务ID。

        :param task_id: The task_id of this BatchRestartMigrationTaskResult.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def error_msg(self):
        r"""Gets the error_msg of this BatchRestartMigrationTaskResult.

        错误信息

        :return: The error_msg of this BatchRestartMigrationTaskResult.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        r"""Sets the error_msg of this BatchRestartMigrationTaskResult.

        错误信息

        :param error_msg: The error_msg of this BatchRestartMigrationTaskResult.
        :type error_msg: str
        """
        self._error_msg = error_msg

    @property
    def error_code(self):
        r"""Gets the error_code of this BatchRestartMigrationTaskResult.

        错误码

        :return: The error_code of this BatchRestartMigrationTaskResult.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this BatchRestartMigrationTaskResult.

        错误码

        :param error_code: The error_code of this BatchRestartMigrationTaskResult.
        :type error_code: str
        """
        self._error_code = error_code

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
        if not isinstance(other, BatchRestartMigrationTaskResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
