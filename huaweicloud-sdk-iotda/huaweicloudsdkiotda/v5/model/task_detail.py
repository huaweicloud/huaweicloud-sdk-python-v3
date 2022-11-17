# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'target': 'str',
        'status': 'str',
        'output': 'str',
        'error': 'ErrorInfo'
    }

    attribute_map = {
        'target': 'target',
        'status': 'status',
        'output': 'output',
        'error': 'error'
    }

    def __init__(self, target=None, status=None, output=None, error=None):
        """TaskDetail

        The model defined in huaweicloud sdk

        :param target: 执行批量任务的目标。
        :type target: str
        :param status: 子任务的执行状态，结果范围：Processing，Success，Fail，Waitting，FailWaitRetry，Stopped。 - Waitting: 等待执行。 - Processing: 执行中。 - Success: 成功。 - Fail: 失败。 - FailWaitRetry: 失败重试。 - Stopped: 已停止。
        :type status: str
        :param output: 子任务执行的输出信息。
        :type output: str
        :param error: 
        :type error: :class:`huaweicloudsdkiotda.v5.ErrorInfo`
        """
        
        

        self._target = None
        self._status = None
        self._output = None
        self._error = None
        self.discriminator = None

        if target is not None:
            self.target = target
        if status is not None:
            self.status = status
        if output is not None:
            self.output = output
        if error is not None:
            self.error = error

    @property
    def target(self):
        """Gets the target of this TaskDetail.

        执行批量任务的目标。

        :return: The target of this TaskDetail.
        :rtype: str
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this TaskDetail.

        执行批量任务的目标。

        :param target: The target of this TaskDetail.
        :type target: str
        """
        self._target = target

    @property
    def status(self):
        """Gets the status of this TaskDetail.

        子任务的执行状态，结果范围：Processing，Success，Fail，Waitting，FailWaitRetry，Stopped。 - Waitting: 等待执行。 - Processing: 执行中。 - Success: 成功。 - Fail: 失败。 - FailWaitRetry: 失败重试。 - Stopped: 已停止。

        :return: The status of this TaskDetail.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TaskDetail.

        子任务的执行状态，结果范围：Processing，Success，Fail，Waitting，FailWaitRetry，Stopped。 - Waitting: 等待执行。 - Processing: 执行中。 - Success: 成功。 - Fail: 失败。 - FailWaitRetry: 失败重试。 - Stopped: 已停止。

        :param status: The status of this TaskDetail.
        :type status: str
        """
        self._status = status

    @property
    def output(self):
        """Gets the output of this TaskDetail.

        子任务执行的输出信息。

        :return: The output of this TaskDetail.
        :rtype: str
        """
        return self._output

    @output.setter
    def output(self, output):
        """Sets the output of this TaskDetail.

        子任务执行的输出信息。

        :param output: The output of this TaskDetail.
        :type output: str
        """
        self._output = output

    @property
    def error(self):
        """Gets the error of this TaskDetail.

        :return: The error of this TaskDetail.
        :rtype: :class:`huaweicloudsdkiotda.v5.ErrorInfo`
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this TaskDetail.

        :param error: The error of this TaskDetail.
        :type error: :class:`huaweicloudsdkiotda.v5.ErrorInfo`
        """
        self._error = error

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
        if not isinstance(other, TaskDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
