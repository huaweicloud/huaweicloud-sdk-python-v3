# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ErrorMessage:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'error_code': 'str',
        'error_msg': 'str',
        'solution_msg': 'str'
    }

    attribute_map = {
        'error_code': 'error_code',
        'error_msg': 'error_msg',
        'solution_msg': 'solution_msg'
    }

    def __init__(self, error_code=None, error_msg=None, solution_msg=None):
        r"""ErrorMessage

        The model defined in huaweicloud sdk

        :param error_code: **参数解释**：错误码。 **取值范围**：长度为8~36个字符。
        :type error_code: str
        :param error_msg: **参数解释**：错误描述。 **取值范围**：长度为2~4096个字符。
        :type error_msg: str
        :param solution_msg: **参数解释**：解决方案描述。 **取值范围**：长度为2~4096个字符。
        :type solution_msg: str
        """
        
        

        self._error_code = None
        self._error_msg = None
        self._solution_msg = None
        self.discriminator = None

        self.error_code = error_code
        self.error_msg = error_msg
        if solution_msg is not None:
            self.solution_msg = solution_msg

    @property
    def error_code(self):
        r"""Gets the error_code of this ErrorMessage.

        **参数解释**：错误码。 **取值范围**：长度为8~36个字符。

        :return: The error_code of this ErrorMessage.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this ErrorMessage.

        **参数解释**：错误码。 **取值范围**：长度为8~36个字符。

        :param error_code: The error_code of this ErrorMessage.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_msg(self):
        r"""Gets the error_msg of this ErrorMessage.

        **参数解释**：错误描述。 **取值范围**：长度为2~4096个字符。

        :return: The error_msg of this ErrorMessage.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        r"""Sets the error_msg of this ErrorMessage.

        **参数解释**：错误描述。 **取值范围**：长度为2~4096个字符。

        :param error_msg: The error_msg of this ErrorMessage.
        :type error_msg: str
        """
        self._error_msg = error_msg

    @property
    def solution_msg(self):
        r"""Gets the solution_msg of this ErrorMessage.

        **参数解释**：解决方案描述。 **取值范围**：长度为2~4096个字符。

        :return: The solution_msg of this ErrorMessage.
        :rtype: str
        """
        return self._solution_msg

    @solution_msg.setter
    def solution_msg(self, solution_msg):
        r"""Sets the solution_msg of this ErrorMessage.

        **参数解释**：解决方案描述。 **取值范围**：长度为2~4096个字符。

        :param solution_msg: The solution_msg of this ErrorMessage.
        :type solution_msg: str
        """
        self._solution_msg = solution_msg

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
        if not isinstance(other, ErrorMessage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
