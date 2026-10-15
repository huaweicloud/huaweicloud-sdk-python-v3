# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExecutionResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'exit_code': 'str',
        'error_msg': 'str'
    }

    attribute_map = {
        'exit_code': 'exit_code',
        'error_msg': 'error_msg'
    }

    def __init__(self, exit_code=None, error_msg=None):
        r"""ExecutionResult

        The model defined in huaweicloud sdk

        :param exit_code: **参数解释**：作业执行退出码。 **约束限制**：不涉及。 **取值范围**：长度为1~128的任意字符组合。 **默认取值**：不涉及。
        :type exit_code: str
        :param error_msg: **参数解释**：作业执行错误信息。 **约束限制**：不涉及。 **取值范围**：长度为1~1024的任意字符组合。 **默认取值**：不涉及。
        :type error_msg: str
        """
        
        

        self._exit_code = None
        self._error_msg = None
        self.discriminator = None

        if exit_code is not None:
            self.exit_code = exit_code
        if error_msg is not None:
            self.error_msg = error_msg

    @property
    def exit_code(self):
        r"""Gets the exit_code of this ExecutionResult.

        **参数解释**：作业执行退出码。 **约束限制**：不涉及。 **取值范围**：长度为1~128的任意字符组合。 **默认取值**：不涉及。

        :return: The exit_code of this ExecutionResult.
        :rtype: str
        """
        return self._exit_code

    @exit_code.setter
    def exit_code(self, exit_code):
        r"""Sets the exit_code of this ExecutionResult.

        **参数解释**：作业执行退出码。 **约束限制**：不涉及。 **取值范围**：长度为1~128的任意字符组合。 **默认取值**：不涉及。

        :param exit_code: The exit_code of this ExecutionResult.
        :type exit_code: str
        """
        self._exit_code = exit_code

    @property
    def error_msg(self):
        r"""Gets the error_msg of this ExecutionResult.

        **参数解释**：作业执行错误信息。 **约束限制**：不涉及。 **取值范围**：长度为1~1024的任意字符组合。 **默认取值**：不涉及。

        :return: The error_msg of this ExecutionResult.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        r"""Sets the error_msg of this ExecutionResult.

        **参数解释**：作业执行错误信息。 **约束限制**：不涉及。 **取值范围**：长度为1~1024的任意字符组合。 **默认取值**：不涉及。

        :param error_msg: The error_msg of this ExecutionResult.
        :type error_msg: str
        """
        self._error_msg = error_msg

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ExecutionResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
