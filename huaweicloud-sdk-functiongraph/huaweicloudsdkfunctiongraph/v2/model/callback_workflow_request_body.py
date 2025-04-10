# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CallbackWorkflowRequestBody:

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
        'error': 'str',
        'output': 'object'
    }

    attribute_map = {
        'result': 'result',
        'error': 'error',
        'output': 'output'
    }

    def __init__(self, result=None, error=None, output=None):
        r"""CallbackWorkflowRequestBody

        The model defined in huaweicloud sdk

        :param result: 执行结果
        :type result: str
        :param error: 错误信息
        :type error: str
        :param output: 工作流的执行结果，JSON格式，仅在status为success时有值
        :type output: object
        """
        
        

        self._result = None
        self._error = None
        self._output = None
        self.discriminator = None

        self.result = result
        if error is not None:
            self.error = error
        self.output = output

    @property
    def result(self):
        r"""Gets the result of this CallbackWorkflowRequestBody.

        执行结果

        :return: The result of this CallbackWorkflowRequestBody.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this CallbackWorkflowRequestBody.

        执行结果

        :param result: The result of this CallbackWorkflowRequestBody.
        :type result: str
        """
        self._result = result

    @property
    def error(self):
        r"""Gets the error of this CallbackWorkflowRequestBody.

        错误信息

        :return: The error of this CallbackWorkflowRequestBody.
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        r"""Sets the error of this CallbackWorkflowRequestBody.

        错误信息

        :param error: The error of this CallbackWorkflowRequestBody.
        :type error: str
        """
        self._error = error

    @property
    def output(self):
        r"""Gets the output of this CallbackWorkflowRequestBody.

        工作流的执行结果，JSON格式，仅在status为success时有值

        :return: The output of this CallbackWorkflowRequestBody.
        :rtype: object
        """
        return self._output

    @output.setter
    def output(self, output):
        r"""Sets the output of this CallbackWorkflowRequestBody.

        工作流的执行结果，JSON格式，仅在status为success时有值

        :param output: The output of this CallbackWorkflowRequestBody.
        :type output: object
        """
        self._output = output

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
        if not isinstance(other, CallbackWorkflowRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
