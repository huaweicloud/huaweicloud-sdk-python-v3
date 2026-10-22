# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListV2ComputeVersionsRequest:

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
        'compute_id': 'str',
        'operation_result': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'workspace_id': 'workspace_id',
        'compute_id': 'compute_id',
        'operation_result': 'operation_result',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, workspace_id=None, compute_id=None, operation_result=None, offset=None, limit=None):
        r"""ListV2ComputeVersionsRequest

        The model defined in huaweicloud sdk

        :param workspace_id: **参数解释**：**参数解释**：工作空间ID，可通过[获取工作空间ID](aidatalake_02_0044.xml)获取。 **约束限制**：不涉及。  **取值范围**：长度为32-36个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。
        :type workspace_id: str
        :param compute_id: **参数解释**：计算资源ID。可通过[查询计算资源列表]获取计算资源ID(ListV2Computes.xml)。 **约束限制**：不涉及。 **取值范围**：长度为1~36的英文字符、数字和中划线的组合。 **默认取值**：不涉及。 
        :type compute_id: str
        :param operation_result: **参数解释**：操作结果，不传则查询所有状态的操作记录。 **约束限制**：不涉及。 **取值范围**：   - SUCCESS：操作成功。   - EXECUTING：执行中。   - FAILED：操作失败。 **默认取值**：不涉及。 
        :type operation_result: str
        :param offset: **参数解释**：偏移量，表示从此偏移量开始查询。 **约束限制**：不涉及。 **取值范围**：0~1000000000。 **默认取值**：0。
        :type offset: int
        :param limit: **参数解释**：指定每一页返回的最大条目数。 **约束限制**：不涉及。 **取值范围**：1~100。 **默认取值**：10。
        :type limit: int
        """
        
        

        self._workspace_id = None
        self._compute_id = None
        self._operation_result = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.workspace_id = workspace_id
        if compute_id is not None:
            self.compute_id = compute_id
        if operation_result is not None:
            self.operation_result = operation_result
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ListV2ComputeVersionsRequest.

        **参数解释**：**参数解释**：工作空间ID，可通过[获取工作空间ID](aidatalake_02_0044.xml)获取。 **约束限制**：不涉及。  **取值范围**：长度为32-36个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。

        :return: The workspace_id of this ListV2ComputeVersionsRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ListV2ComputeVersionsRequest.

        **参数解释**：**参数解释**：工作空间ID，可通过[获取工作空间ID](aidatalake_02_0044.xml)获取。 **约束限制**：不涉及。  **取值范围**：长度为32-36个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。

        :param workspace_id: The workspace_id of this ListV2ComputeVersionsRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def compute_id(self):
        r"""Gets the compute_id of this ListV2ComputeVersionsRequest.

        **参数解释**：计算资源ID。可通过[查询计算资源列表]获取计算资源ID(ListV2Computes.xml)。 **约束限制**：不涉及。 **取值范围**：长度为1~36的英文字符、数字和中划线的组合。 **默认取值**：不涉及。 

        :return: The compute_id of this ListV2ComputeVersionsRequest.
        :rtype: str
        """
        return self._compute_id

    @compute_id.setter
    def compute_id(self, compute_id):
        r"""Sets the compute_id of this ListV2ComputeVersionsRequest.

        **参数解释**：计算资源ID。可通过[查询计算资源列表]获取计算资源ID(ListV2Computes.xml)。 **约束限制**：不涉及。 **取值范围**：长度为1~36的英文字符、数字和中划线的组合。 **默认取值**：不涉及。 

        :param compute_id: The compute_id of this ListV2ComputeVersionsRequest.
        :type compute_id: str
        """
        self._compute_id = compute_id

    @property
    def operation_result(self):
        r"""Gets the operation_result of this ListV2ComputeVersionsRequest.

        **参数解释**：操作结果，不传则查询所有状态的操作记录。 **约束限制**：不涉及。 **取值范围**：   - SUCCESS：操作成功。   - EXECUTING：执行中。   - FAILED：操作失败。 **默认取值**：不涉及。 

        :return: The operation_result of this ListV2ComputeVersionsRequest.
        :rtype: str
        """
        return self._operation_result

    @operation_result.setter
    def operation_result(self, operation_result):
        r"""Sets the operation_result of this ListV2ComputeVersionsRequest.

        **参数解释**：操作结果，不传则查询所有状态的操作记录。 **约束限制**：不涉及。 **取值范围**：   - SUCCESS：操作成功。   - EXECUTING：执行中。   - FAILED：操作失败。 **默认取值**：不涉及。 

        :param operation_result: The operation_result of this ListV2ComputeVersionsRequest.
        :type operation_result: str
        """
        self._operation_result = operation_result

    @property
    def offset(self):
        r"""Gets the offset of this ListV2ComputeVersionsRequest.

        **参数解释**：偏移量，表示从此偏移量开始查询。 **约束限制**：不涉及。 **取值范围**：0~1000000000。 **默认取值**：0。

        :return: The offset of this ListV2ComputeVersionsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListV2ComputeVersionsRequest.

        **参数解释**：偏移量，表示从此偏移量开始查询。 **约束限制**：不涉及。 **取值范围**：0~1000000000。 **默认取值**：0。

        :param offset: The offset of this ListV2ComputeVersionsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListV2ComputeVersionsRequest.

        **参数解释**：指定每一页返回的最大条目数。 **约束限制**：不涉及。 **取值范围**：1~100。 **默认取值**：10。

        :return: The limit of this ListV2ComputeVersionsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListV2ComputeVersionsRequest.

        **参数解释**：指定每一页返回的最大条目数。 **约束限制**：不涉及。 **取值范围**：1~100。 **默认取值**：10。

        :param limit: The limit of this ListV2ComputeVersionsRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListV2ComputeVersionsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
