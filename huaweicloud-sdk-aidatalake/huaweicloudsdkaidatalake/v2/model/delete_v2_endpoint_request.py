# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteV2EndpointRequest:

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
        'endpoint_id': 'str',
        'force': 'bool'
    }

    attribute_map = {
        'workspace_id': 'workspace_id',
        'endpoint_id': 'endpoint_id',
        'force': 'force'
    }

    def __init__(self, workspace_id=None, endpoint_id=None, force=None):
        r"""DeleteV2EndpointRequest

        The model defined in huaweicloud sdk

        :param workspace_id: **参数解释**：**参数解释**：工作空间ID，可通过[获取工作空间ID](aidatalake_02_0044.xml)获取。 **约束限制**：不涉及。  **取值范围**：长度为32-36个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。
        :type workspace_id: str
        :param endpoint_id: **参数解释**：端点ID，可通过[查询端点列表](ListV2Endpoints.xml)获取端点ID。 **约束限制**：不涉及。  **取值范围**：长度为32-36个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。
        :type endpoint_id: str
        :param force: **参数解释**：强制删除。 **约束限制**：当配置为true时，不管任何情况强制删除。 **取值范围**：   - true：强制删除。   - false：非强制删除。 **默认取值**：false。
        :type force: bool
        """
        
        

        self._workspace_id = None
        self._endpoint_id = None
        self._force = None
        self.discriminator = None

        self.workspace_id = workspace_id
        self.endpoint_id = endpoint_id
        if force is not None:
            self.force = force

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this DeleteV2EndpointRequest.

        **参数解释**：**参数解释**：工作空间ID，可通过[获取工作空间ID](aidatalake_02_0044.xml)获取。 **约束限制**：不涉及。  **取值范围**：长度为32-36个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。

        :return: The workspace_id of this DeleteV2EndpointRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this DeleteV2EndpointRequest.

        **参数解释**：**参数解释**：工作空间ID，可通过[获取工作空间ID](aidatalake_02_0044.xml)获取。 **约束限制**：不涉及。  **取值范围**：长度为32-36个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。

        :param workspace_id: The workspace_id of this DeleteV2EndpointRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def endpoint_id(self):
        r"""Gets the endpoint_id of this DeleteV2EndpointRequest.

        **参数解释**：端点ID，可通过[查询端点列表](ListV2Endpoints.xml)获取端点ID。 **约束限制**：不涉及。  **取值范围**：长度为32-36个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。

        :return: The endpoint_id of this DeleteV2EndpointRequest.
        :rtype: str
        """
        return self._endpoint_id

    @endpoint_id.setter
    def endpoint_id(self, endpoint_id):
        r"""Sets the endpoint_id of this DeleteV2EndpointRequest.

        **参数解释**：端点ID，可通过[查询端点列表](ListV2Endpoints.xml)获取端点ID。 **约束限制**：不涉及。  **取值范围**：长度为32-36个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。

        :param endpoint_id: The endpoint_id of this DeleteV2EndpointRequest.
        :type endpoint_id: str
        """
        self._endpoint_id = endpoint_id

    @property
    def force(self):
        r"""Gets the force of this DeleteV2EndpointRequest.

        **参数解释**：强制删除。 **约束限制**：当配置为true时，不管任何情况强制删除。 **取值范围**：   - true：强制删除。   - false：非强制删除。 **默认取值**：false。

        :return: The force of this DeleteV2EndpointRequest.
        :rtype: bool
        """
        return self._force

    @force.setter
    def force(self, force):
        r"""Sets the force of this DeleteV2EndpointRequest.

        **参数解释**：强制删除。 **约束限制**：当配置为true时，不管任何情况强制删除。 **取值范围**：   - true：强制删除。   - false：非强制删除。 **默认取值**：false。

        :param force: The force of this DeleteV2EndpointRequest.
        :type force: bool
        """
        self._force = force

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
        if not isinstance(other, DeleteV2EndpointRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
