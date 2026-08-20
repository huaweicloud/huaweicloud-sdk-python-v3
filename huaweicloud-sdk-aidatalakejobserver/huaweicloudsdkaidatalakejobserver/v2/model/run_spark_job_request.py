# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RunSparkJobRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []
    sensitive_list.append('x_client_token')

    openapi_types = {
        'workspace_id': 'str',
        'x_client_token': 'str',
        'body': 'RunSparkJobRequestBody'
    }

    attribute_map = {
        'workspace_id': 'workspace_id',
        'x_client_token': 'X-Client-Token',
        'body': 'body'
    }

    def __init__(self, workspace_id=None, x_client_token=None, body=None):
        r"""RunSparkJobRequest

        The model defined in huaweicloud sdk

        :param workspace_id: **参数解释**：工作空间的ID。 **约束限制**：不涉及。 **取值范围**：长度为1~36个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。
        :type workspace_id: str
        :param x_client_token: **参数解释**：服务事务ID，用于链路追踪和防止重复提交。 **约束限制**：不涉及。 **取值范围**：采用UUID格式，长度为36个字符。 **默认取值**：不涉及。 
        :type x_client_token: str
        :param body: Body of the RunSparkJobRequest
        :type body: :class:`huaweicloudsdkaidatalakejobserver.v2.RunSparkJobRequestBody`
        """
        
        

        self._workspace_id = None
        self._x_client_token = None
        self._body = None
        self.discriminator = None

        self.workspace_id = workspace_id
        if x_client_token is not None:
            self.x_client_token = x_client_token
        if body is not None:
            self.body = body

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this RunSparkJobRequest.

        **参数解释**：工作空间的ID。 **约束限制**：不涉及。 **取值范围**：长度为1~36个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。

        :return: The workspace_id of this RunSparkJobRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this RunSparkJobRequest.

        **参数解释**：工作空间的ID。 **约束限制**：不涉及。 **取值范围**：长度为1~36个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。

        :param workspace_id: The workspace_id of this RunSparkJobRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def x_client_token(self):
        r"""Gets the x_client_token of this RunSparkJobRequest.

        **参数解释**：服务事务ID，用于链路追踪和防止重复提交。 **约束限制**：不涉及。 **取值范围**：采用UUID格式，长度为36个字符。 **默认取值**：不涉及。 

        :return: The x_client_token of this RunSparkJobRequest.
        :rtype: str
        """
        return self._x_client_token

    @x_client_token.setter
    def x_client_token(self, x_client_token):
        r"""Sets the x_client_token of this RunSparkJobRequest.

        **参数解释**：服务事务ID，用于链路追踪和防止重复提交。 **约束限制**：不涉及。 **取值范围**：采用UUID格式，长度为36个字符。 **默认取值**：不涉及。 

        :param x_client_token: The x_client_token of this RunSparkJobRequest.
        :type x_client_token: str
        """
        self._x_client_token = x_client_token

    @property
    def body(self):
        r"""Gets the body of this RunSparkJobRequest.

        :return: The body of this RunSparkJobRequest.
        :rtype: :class:`huaweicloudsdkaidatalakejobserver.v2.RunSparkJobRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this RunSparkJobRequest.

        :param body: The body of this RunSparkJobRequest.
        :type body: :class:`huaweicloudsdkaidatalakejobserver.v2.RunSparkJobRequestBody`
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
        if not isinstance(other, RunSparkJobRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
