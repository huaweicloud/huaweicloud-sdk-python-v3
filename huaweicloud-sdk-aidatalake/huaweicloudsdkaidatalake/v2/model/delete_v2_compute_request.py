# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteV2ComputeRequest:

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
        'compute_id': 'str'
    }

    attribute_map = {
        'workspace_id': 'workspace_id',
        'compute_id': 'compute_id'
    }

    def __init__(self, workspace_id=None, compute_id=None):
        r"""DeleteV2ComputeRequest

        The model defined in huaweicloud sdk

        :param workspace_id: **参数解释**：**参数解释**：工作空间ID，可通过[获取工作空间ID](aidatalake_02_0044.xml)获取。 **约束限制**：不涉及。  **取值范围**：长度为32-36个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。
        :type workspace_id: str
        :param compute_id: **参数解释**：计算资源ID。可通过[查询计算资源列表]获取计算资源ID(ListV2Computes.xml)。 **约束限制**：不涉及。 **取值范围**：长度为1-36个英文字母、数字和中划线的组合。 **默认取值**：不涉及。 
        :type compute_id: str
        """
        
        

        self._workspace_id = None
        self._compute_id = None
        self.discriminator = None

        self.workspace_id = workspace_id
        self.compute_id = compute_id

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this DeleteV2ComputeRequest.

        **参数解释**：**参数解释**：工作空间ID，可通过[获取工作空间ID](aidatalake_02_0044.xml)获取。 **约束限制**：不涉及。  **取值范围**：长度为32-36个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。

        :return: The workspace_id of this DeleteV2ComputeRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this DeleteV2ComputeRequest.

        **参数解释**：**参数解释**：工作空间ID，可通过[获取工作空间ID](aidatalake_02_0044.xml)获取。 **约束限制**：不涉及。  **取值范围**：长度为32-36个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。

        :param workspace_id: The workspace_id of this DeleteV2ComputeRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def compute_id(self):
        r"""Gets the compute_id of this DeleteV2ComputeRequest.

        **参数解释**：计算资源ID。可通过[查询计算资源列表]获取计算资源ID(ListV2Computes.xml)。 **约束限制**：不涉及。 **取值范围**：长度为1-36个英文字母、数字和中划线的组合。 **默认取值**：不涉及。 

        :return: The compute_id of this DeleteV2ComputeRequest.
        :rtype: str
        """
        return self._compute_id

    @compute_id.setter
    def compute_id(self, compute_id):
        r"""Sets the compute_id of this DeleteV2ComputeRequest.

        **参数解释**：计算资源ID。可通过[查询计算资源列表]获取计算资源ID(ListV2Computes.xml)。 **约束限制**：不涉及。 **取值范围**：长度为1-36个英文字母、数字和中划线的组合。 **默认取值**：不涉及。 

        :param compute_id: The compute_id of this DeleteV2ComputeRequest.
        :type compute_id: str
        """
        self._compute_id = compute_id

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
        if not isinstance(other, DeleteV2ComputeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
