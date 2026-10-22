# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListV2ComputesRequest:

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
        'offset': 'int',
        'limit': 'int',
        'name': 'str',
        'compute_id': 'str',
        'tags': 'list[str]'
    }

    attribute_map = {
        'workspace_id': 'workspace_id',
        'offset': 'offset',
        'limit': 'limit',
        'name': 'name',
        'compute_id': 'compute_id',
        'tags': 'tags'
    }

    def __init__(self, workspace_id=None, offset=None, limit=None, name=None, compute_id=None, tags=None):
        r"""ListV2ComputesRequest

        The model defined in huaweicloud sdk

        :param workspace_id: **参数解释**：**参数解释**：工作空间ID，可通过[获取工作空间ID](aidatalake_02_0044.xml)获取。 **约束限制**：不涉及。  **取值范围**：长度为32-36个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。
        :type workspace_id: str
        :param offset: **参数解释**：偏移量，表示从此偏移量开始查询。 **约束限制**：不涉及。 **取值范围**：0~1000000000。 **默认取值**：0。
        :type offset: int
        :param limit: **参数解释**：分页大小。 **约束限制**：不涉及。 **取值范围**：1~1000。 **默认取值**：100。 
        :type limit: int
        :param name: **参数解释**：计算资源名称，模糊查询。 **约束限制**：不涉及。 **取值范围**：支持小写字母、数字、中划线，必须字母开头、字母或数字结尾，长度为1~63个字符。 **默认取值**：不涉及。 
        :type name: str
        :param compute_id: **参数解释**：计算资源ID。可通过[查询计算资源列表]获取计算资源ID(ListV2Computes.xml)。 **约束限制**：不涉及。 **取值范围**：长度为1~36的英文字符、数字和中划线的组合。 **默认取值**：不涉及。 
        :type compute_id: str
        :param tags: **参数解释**：标签过滤条件，支持多个标签。格式为 key#value1,value2，用英文逗号分隔多个值。 **约束限制**：最多10个标签。 
        :type tags: list[str]
        """
        
        

        self._workspace_id = None
        self._offset = None
        self._limit = None
        self._name = None
        self._compute_id = None
        self._tags = None
        self.discriminator = None

        self.workspace_id = workspace_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if name is not None:
            self.name = name
        if compute_id is not None:
            self.compute_id = compute_id
        if tags is not None:
            self.tags = tags

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ListV2ComputesRequest.

        **参数解释**：**参数解释**：工作空间ID，可通过[获取工作空间ID](aidatalake_02_0044.xml)获取。 **约束限制**：不涉及。  **取值范围**：长度为32-36个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。

        :return: The workspace_id of this ListV2ComputesRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ListV2ComputesRequest.

        **参数解释**：**参数解释**：工作空间ID，可通过[获取工作空间ID](aidatalake_02_0044.xml)获取。 **约束限制**：不涉及。  **取值范围**：长度为32-36个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。

        :param workspace_id: The workspace_id of this ListV2ComputesRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def offset(self):
        r"""Gets the offset of this ListV2ComputesRequest.

        **参数解释**：偏移量，表示从此偏移量开始查询。 **约束限制**：不涉及。 **取值范围**：0~1000000000。 **默认取值**：0。

        :return: The offset of this ListV2ComputesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListV2ComputesRequest.

        **参数解释**：偏移量，表示从此偏移量开始查询。 **约束限制**：不涉及。 **取值范围**：0~1000000000。 **默认取值**：0。

        :param offset: The offset of this ListV2ComputesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListV2ComputesRequest.

        **参数解释**：分页大小。 **约束限制**：不涉及。 **取值范围**：1~1000。 **默认取值**：100。 

        :return: The limit of this ListV2ComputesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListV2ComputesRequest.

        **参数解释**：分页大小。 **约束限制**：不涉及。 **取值范围**：1~1000。 **默认取值**：100。 

        :param limit: The limit of this ListV2ComputesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def name(self):
        r"""Gets the name of this ListV2ComputesRequest.

        **参数解释**：计算资源名称，模糊查询。 **约束限制**：不涉及。 **取值范围**：支持小写字母、数字、中划线，必须字母开头、字母或数字结尾，长度为1~63个字符。 **默认取值**：不涉及。 

        :return: The name of this ListV2ComputesRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListV2ComputesRequest.

        **参数解释**：计算资源名称，模糊查询。 **约束限制**：不涉及。 **取值范围**：支持小写字母、数字、中划线，必须字母开头、字母或数字结尾，长度为1~63个字符。 **默认取值**：不涉及。 

        :param name: The name of this ListV2ComputesRequest.
        :type name: str
        """
        self._name = name

    @property
    def compute_id(self):
        r"""Gets the compute_id of this ListV2ComputesRequest.

        **参数解释**：计算资源ID。可通过[查询计算资源列表]获取计算资源ID(ListV2Computes.xml)。 **约束限制**：不涉及。 **取值范围**：长度为1~36的英文字符、数字和中划线的组合。 **默认取值**：不涉及。 

        :return: The compute_id of this ListV2ComputesRequest.
        :rtype: str
        """
        return self._compute_id

    @compute_id.setter
    def compute_id(self, compute_id):
        r"""Sets the compute_id of this ListV2ComputesRequest.

        **参数解释**：计算资源ID。可通过[查询计算资源列表]获取计算资源ID(ListV2Computes.xml)。 **约束限制**：不涉及。 **取值范围**：长度为1~36的英文字符、数字和中划线的组合。 **默认取值**：不涉及。 

        :param compute_id: The compute_id of this ListV2ComputesRequest.
        :type compute_id: str
        """
        self._compute_id = compute_id

    @property
    def tags(self):
        r"""Gets the tags of this ListV2ComputesRequest.

        **参数解释**：标签过滤条件，支持多个标签。格式为 key#value1,value2，用英文逗号分隔多个值。 **约束限制**：最多10个标签。 

        :return: The tags of this ListV2ComputesRequest.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ListV2ComputesRequest.

        **参数解释**：标签过滤条件，支持多个标签。格式为 key#value1,value2，用英文逗号分隔多个值。 **约束限制**：最多10个标签。 

        :param tags: The tags of this ListV2ComputesRequest.
        :type tags: list[str]
        """
        self._tags = tags

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
        if not isinstance(other, ListV2ComputesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
