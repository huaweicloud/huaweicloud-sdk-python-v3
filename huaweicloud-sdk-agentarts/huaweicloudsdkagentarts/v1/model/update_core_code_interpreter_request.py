# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateCoreCodeInterpreterRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'code_interpreter_id': 'str',
        'body': 'UpdateCoreCodeInterpreterRequestBody'
    }

    attribute_map = {
        'code_interpreter_id': 'code_interpreter_id',
        'body': 'body'
    }

    def __init__(self, code_interpreter_id=None, body=None):
        r"""UpdateCoreCodeInterpreterRequest

        The model defined in huaweicloud sdk

        :param code_interpreter_id: **参数解释：** 代码解释器ID，可通过[查询代码解释器列表](https://support.huaweicloud.com/api-agentarts/ListCoreCodeInterpreters.html)接口获取。 **约束限制：** 不涉及。 **取值范围：** 符合UUID正则^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$的36位字符串。 **默认取值：** 不涉及。
        :type code_interpreter_id: str
        :param body: Body of the UpdateCoreCodeInterpreterRequest
        :type body: :class:`huaweicloudsdkagentarts.v1.UpdateCoreCodeInterpreterRequestBody`
        """
        
        

        self._code_interpreter_id = None
        self._body = None
        self.discriminator = None

        self.code_interpreter_id = code_interpreter_id
        if body is not None:
            self.body = body

    @property
    def code_interpreter_id(self):
        r"""Gets the code_interpreter_id of this UpdateCoreCodeInterpreterRequest.

        **参数解释：** 代码解释器ID，可通过[查询代码解释器列表](https://support.huaweicloud.com/api-agentarts/ListCoreCodeInterpreters.html)接口获取。 **约束限制：** 不涉及。 **取值范围：** 符合UUID正则^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$的36位字符串。 **默认取值：** 不涉及。

        :return: The code_interpreter_id of this UpdateCoreCodeInterpreterRequest.
        :rtype: str
        """
        return self._code_interpreter_id

    @code_interpreter_id.setter
    def code_interpreter_id(self, code_interpreter_id):
        r"""Sets the code_interpreter_id of this UpdateCoreCodeInterpreterRequest.

        **参数解释：** 代码解释器ID，可通过[查询代码解释器列表](https://support.huaweicloud.com/api-agentarts/ListCoreCodeInterpreters.html)接口获取。 **约束限制：** 不涉及。 **取值范围：** 符合UUID正则^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$的36位字符串。 **默认取值：** 不涉及。

        :param code_interpreter_id: The code_interpreter_id of this UpdateCoreCodeInterpreterRequest.
        :type code_interpreter_id: str
        """
        self._code_interpreter_id = code_interpreter_id

    @property
    def body(self):
        r"""Gets the body of this UpdateCoreCodeInterpreterRequest.

        :return: The body of this UpdateCoreCodeInterpreterRequest.
        :rtype: :class:`huaweicloudsdkagentarts.v1.UpdateCoreCodeInterpreterRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateCoreCodeInterpreterRequest.

        :param body: The body of this UpdateCoreCodeInterpreterRequest.
        :type body: :class:`huaweicloudsdkagentarts.v1.UpdateCoreCodeInterpreterRequestBody`
        """
        self._body = body

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
        if not isinstance(other, UpdateCoreCodeInterpreterRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
