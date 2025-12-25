# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GenericActionRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'workspace_id': 'str',
        'parameter': 'object'
    }

    attribute_map = {
        'type': 'type',
        'workspace_id': 'workspace_id',
        'parameter': 'parameter'
    }

    def __init__(self, type=None, workspace_id=None, parameter=None):
        r"""GenericActionRequestBody

        The model defined in huaweicloud sdk

        :param type: 表示具体行为的类型。命名为“t_行为名称”。例如 \&quot;t_dialog_feedback\&quot; 。
        :type type: str
        :param workspace_id: workspace ID
        :type workspace_id: str
        :param parameter: 具体行为的数据内容，其结构由&#39;action&#39;字段决定。 - 回答质量人工反馈action: t_dialog_feedback, 参考DialogFeedbackData结构
        :type parameter: object
        """
        
        

        self._type = None
        self._workspace_id = None
        self._parameter = None
        self.discriminator = None

        self.type = type
        if workspace_id is not None:
            self.workspace_id = workspace_id
        self.parameter = parameter

    @property
    def type(self):
        r"""Gets the type of this GenericActionRequestBody.

        表示具体行为的类型。命名为“t_行为名称”。例如 \"t_dialog_feedback\" 。

        :return: The type of this GenericActionRequestBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this GenericActionRequestBody.

        表示具体行为的类型。命名为“t_行为名称”。例如 \"t_dialog_feedback\" 。

        :param type: The type of this GenericActionRequestBody.
        :type type: str
        """
        self._type = type

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this GenericActionRequestBody.

        workspace ID

        :return: The workspace_id of this GenericActionRequestBody.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this GenericActionRequestBody.

        workspace ID

        :param workspace_id: The workspace_id of this GenericActionRequestBody.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def parameter(self):
        r"""Gets the parameter of this GenericActionRequestBody.

        具体行为的数据内容，其结构由'action'字段决定。 - 回答质量人工反馈action: t_dialog_feedback, 参考DialogFeedbackData结构

        :return: The parameter of this GenericActionRequestBody.
        :rtype: object
        """
        return self._parameter

    @parameter.setter
    def parameter(self, parameter):
        r"""Sets the parameter of this GenericActionRequestBody.

        具体行为的数据内容，其结构由'action'字段决定。 - 回答质量人工反馈action: t_dialog_feedback, 参考DialogFeedbackData结构

        :param parameter: The parameter of this GenericActionRequestBody.
        :type parameter: object
        """
        self._parameter = parameter

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
        if not isinstance(other, GenericActionRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
