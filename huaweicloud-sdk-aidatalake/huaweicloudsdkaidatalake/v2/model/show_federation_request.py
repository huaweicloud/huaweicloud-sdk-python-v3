# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowFederationRequest:

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
        'ray_federation_id': 'str'
    }

    attribute_map = {
        'workspace_id': 'workspace_id',
        'ray_federation_id': 'ray_federation_id'
    }

    def __init__(self, workspace_id=None, ray_federation_id=None):
        r"""ShowFederationRequest

        The model defined in huaweicloud sdk

        :param workspace_id: **参数解释**：工作空间的ID。 **约束限制**：不涉及。 **取值范围**：长度为1~36个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。
        :type workspace_id: str
        :param ray_federation_id: **参数解释**：Ray联邦端点ID，可通过查询Ray联邦端点列表接口获取。 **约束限制**：不涉及。 **取值范围**：长度为32~36的英文字符、数字和中划线的组合。 **默认取值**：不涉及。
        :type ray_federation_id: str
        """
        
        

        self._workspace_id = None
        self._ray_federation_id = None
        self.discriminator = None

        self.workspace_id = workspace_id
        self.ray_federation_id = ray_federation_id

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ShowFederationRequest.

        **参数解释**：工作空间的ID。 **约束限制**：不涉及。 **取值范围**：长度为1~36个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。

        :return: The workspace_id of this ShowFederationRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ShowFederationRequest.

        **参数解释**：工作空间的ID。 **约束限制**：不涉及。 **取值范围**：长度为1~36个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。

        :param workspace_id: The workspace_id of this ShowFederationRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def ray_federation_id(self):
        r"""Gets the ray_federation_id of this ShowFederationRequest.

        **参数解释**：Ray联邦端点ID，可通过查询Ray联邦端点列表接口获取。 **约束限制**：不涉及。 **取值范围**：长度为32~36的英文字符、数字和中划线的组合。 **默认取值**：不涉及。

        :return: The ray_federation_id of this ShowFederationRequest.
        :rtype: str
        """
        return self._ray_federation_id

    @ray_federation_id.setter
    def ray_federation_id(self, ray_federation_id):
        r"""Sets the ray_federation_id of this ShowFederationRequest.

        **参数解释**：Ray联邦端点ID，可通过查询Ray联邦端点列表接口获取。 **约束限制**：不涉及。 **取值范围**：长度为32~36的英文字符、数字和中划线的组合。 **默认取值**：不涉及。

        :param ray_federation_id: The ray_federation_id of this ShowFederationRequest.
        :type ray_federation_id: str
        """
        self._ray_federation_id = ray_federation_id

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
        if not isinstance(other, ShowFederationRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
