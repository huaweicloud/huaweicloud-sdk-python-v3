# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RestartSparkSqlClusterRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workspace_id': 'str',
        'endpoint_name': 'str',
        'body': 'RestartSparkSqlClusterRequestBody'
    }

    attribute_map = {
        'workspace_id': 'workspace_id',
        'endpoint_name': 'endpoint_name',
        'body': 'body'
    }

    def __init__(self, workspace_id=None, endpoint_name=None, body=None):
        r"""RestartSparkSqlClusterRequest

        The model defined in huaweicloud sdk

        :param workspace_id: **参数解释**：工作空间的ID。 **约束限制**：不涉及。 **取值范围**：长度为1~36个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。
        :type workspace_id: str
        :param endpoint_name: **参数解释**：端点名称，用于标识SparkSql集群的接入点。 **约束限制**：不涉及。 **取值范围**：只能由小写字母、数字及中划线组成，必须以小写字母开头，以小写字母或数字结尾，且长度为1~63个字符。 **默认取值**：不涉及。 
        :type endpoint_name: str
        :param body: Body of the RestartSparkSqlClusterRequest
        :type body: :class:`huaweicloudsdkaidatalakejobserver.v2.RestartSparkSqlClusterRequestBody`
        """
        
        

        self._workspace_id = None
        self._endpoint_name = None
        self._body = None
        self.discriminator = None

        self.workspace_id = workspace_id
        self.endpoint_name = endpoint_name
        if body is not None:
            self.body = body

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this RestartSparkSqlClusterRequest.

        **参数解释**：工作空间的ID。 **约束限制**：不涉及。 **取值范围**：长度为1~36个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。

        :return: The workspace_id of this RestartSparkSqlClusterRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this RestartSparkSqlClusterRequest.

        **参数解释**：工作空间的ID。 **约束限制**：不涉及。 **取值范围**：长度为1~36个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。

        :param workspace_id: The workspace_id of this RestartSparkSqlClusterRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def endpoint_name(self):
        r"""Gets the endpoint_name of this RestartSparkSqlClusterRequest.

        **参数解释**：端点名称，用于标识SparkSql集群的接入点。 **约束限制**：不涉及。 **取值范围**：只能由小写字母、数字及中划线组成，必须以小写字母开头，以小写字母或数字结尾，且长度为1~63个字符。 **默认取值**：不涉及。 

        :return: The endpoint_name of this RestartSparkSqlClusterRequest.
        :rtype: str
        """
        return self._endpoint_name

    @endpoint_name.setter
    def endpoint_name(self, endpoint_name):
        r"""Sets the endpoint_name of this RestartSparkSqlClusterRequest.

        **参数解释**：端点名称，用于标识SparkSql集群的接入点。 **约束限制**：不涉及。 **取值范围**：只能由小写字母、数字及中划线组成，必须以小写字母开头，以小写字母或数字结尾，且长度为1~63个字符。 **默认取值**：不涉及。 

        :param endpoint_name: The endpoint_name of this RestartSparkSqlClusterRequest.
        :type endpoint_name: str
        """
        self._endpoint_name = endpoint_name

    @property
    def body(self):
        r"""Gets the body of this RestartSparkSqlClusterRequest.

        :return: The body of this RestartSparkSqlClusterRequest.
        :rtype: :class:`huaweicloudsdkaidatalakejobserver.v2.RestartSparkSqlClusterRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this RestartSparkSqlClusterRequest.

        :param body: The body of this RestartSparkSqlClusterRequest.
        :type body: :class:`huaweicloudsdkaidatalakejobserver.v2.RestartSparkSqlClusterRequestBody`
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
        if not isinstance(other, RestartSparkSqlClusterRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
