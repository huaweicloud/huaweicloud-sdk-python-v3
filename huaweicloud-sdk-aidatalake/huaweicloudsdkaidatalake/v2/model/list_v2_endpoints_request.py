# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListV2EndpointsRequest:

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
        'engine_types': 'list[EngineType]',
        'compute_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'name': 'str',
        'storage_id': 'str',
        'tags': 'list[str]'
    }

    attribute_map = {
        'workspace_id': 'workspace_id',
        'engine_types': 'engine_types',
        'compute_id': 'compute_id',
        'offset': 'offset',
        'limit': 'limit',
        'name': 'name',
        'storage_id': 'storage_id',
        'tags': 'tags'
    }

    def __init__(self, workspace_id=None, engine_types=None, compute_id=None, offset=None, limit=None, name=None, storage_id=None, tags=None):
        r"""ListV2EndpointsRequest

        The model defined in huaweicloud sdk

        :param workspace_id: **参数解释**：**参数解释**：工作空间ID，可通过[获取工作空间ID](aidatalake_02_0044.xml)获取。 **约束限制**：不涉及。  **取值范围**：长度为32-36个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。
        :type workspace_id: str
        :param engine_types: **参数解释**：端点引擎类型列表。取值包括：   - AuraJob：AuraJob引擎。   - SparkSql：SparkSql引擎。   - SparkJob：SparkJob引擎。   - FlinkJob：FlinkJob引擎。   - AuraJobV2：AuraJobV2引擎。   - RayCluster：RayCluster引擎。   - RayJob：RayJob引擎。   - RayService：RayService引擎。 **约束限制**：不涉及。 
        :type engine_types: list[:class:`huaweicloudsdkaidatalake.v2.EngineType`]
        :param compute_id: **参数解释**：计算资源ID。可通过[查询计算资源列表]获取计算资源ID(ListV2Computes.xml)。 **约束限制**：不涉及。 **取值范围**：长度为1~36的英文字符、数字和中划线的组合。 **默认取值**：不涉及。 
        :type compute_id: str
        :param offset: **参数解释**：偏移量，表示从此偏移量开始查询。 **约束限制**：不涉及。 **取值范围**：0~1000000000。 **默认取值**：0。
        :type offset: int
        :param limit: **参数解释**：指定每一页返回的最大条目数。 **约束限制**：不涉及。 **取值范围**：1~100。 **默认取值**：10。
        :type limit: int
        :param name: **参数解释**：端点名称，精确查询。 **约束限制**：不涉及。 **取值范围**：长度为1~63个字符，遵循RFC 1035规范，支持小写字母、数字、中划线，必须字母开头、字母或数字结尾。 **默认取值**：不涉及。 
        :type name: str
        :param storage_id: **参数解释**：存储资源ID，可通过[查询存储资源列表](ListV2Storages.xml)获取存储资源ID。 **约束限制**：不涉及。 **取值范围**：长度为1~64的英文字符、数字和中划线的组合。 **默认取值**：不涉及。 
        :type storage_id: str
        :param tags: **参数解释**：标签过滤条件，支持多个标签。格式为 key#value1,value2，用英文逗号分隔多个值。 **约束限制**：最多10个标签。 
        :type tags: list[str]
        """
        
        

        self._workspace_id = None
        self._engine_types = None
        self._compute_id = None
        self._offset = None
        self._limit = None
        self._name = None
        self._storage_id = None
        self._tags = None
        self.discriminator = None

        self.workspace_id = workspace_id
        if engine_types is not None:
            self.engine_types = engine_types
        if compute_id is not None:
            self.compute_id = compute_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if name is not None:
            self.name = name
        if storage_id is not None:
            self.storage_id = storage_id
        if tags is not None:
            self.tags = tags

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ListV2EndpointsRequest.

        **参数解释**：**参数解释**：工作空间ID，可通过[获取工作空间ID](aidatalake_02_0044.xml)获取。 **约束限制**：不涉及。  **取值范围**：长度为32-36个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。

        :return: The workspace_id of this ListV2EndpointsRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ListV2EndpointsRequest.

        **参数解释**：**参数解释**：工作空间ID，可通过[获取工作空间ID](aidatalake_02_0044.xml)获取。 **约束限制**：不涉及。  **取值范围**：长度为32-36个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。

        :param workspace_id: The workspace_id of this ListV2EndpointsRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def engine_types(self):
        r"""Gets the engine_types of this ListV2EndpointsRequest.

        **参数解释**：端点引擎类型列表。取值包括：   - AuraJob：AuraJob引擎。   - SparkSql：SparkSql引擎。   - SparkJob：SparkJob引擎。   - FlinkJob：FlinkJob引擎。   - AuraJobV2：AuraJobV2引擎。   - RayCluster：RayCluster引擎。   - RayJob：RayJob引擎。   - RayService：RayService引擎。 **约束限制**：不涉及。 

        :return: The engine_types of this ListV2EndpointsRequest.
        :rtype: list[:class:`huaweicloudsdkaidatalake.v2.EngineType`]
        """
        return self._engine_types

    @engine_types.setter
    def engine_types(self, engine_types):
        r"""Sets the engine_types of this ListV2EndpointsRequest.

        **参数解释**：端点引擎类型列表。取值包括：   - AuraJob：AuraJob引擎。   - SparkSql：SparkSql引擎。   - SparkJob：SparkJob引擎。   - FlinkJob：FlinkJob引擎。   - AuraJobV2：AuraJobV2引擎。   - RayCluster：RayCluster引擎。   - RayJob：RayJob引擎。   - RayService：RayService引擎。 **约束限制**：不涉及。 

        :param engine_types: The engine_types of this ListV2EndpointsRequest.
        :type engine_types: list[:class:`huaweicloudsdkaidatalake.v2.EngineType`]
        """
        self._engine_types = engine_types

    @property
    def compute_id(self):
        r"""Gets the compute_id of this ListV2EndpointsRequest.

        **参数解释**：计算资源ID。可通过[查询计算资源列表]获取计算资源ID(ListV2Computes.xml)。 **约束限制**：不涉及。 **取值范围**：长度为1~36的英文字符、数字和中划线的组合。 **默认取值**：不涉及。 

        :return: The compute_id of this ListV2EndpointsRequest.
        :rtype: str
        """
        return self._compute_id

    @compute_id.setter
    def compute_id(self, compute_id):
        r"""Sets the compute_id of this ListV2EndpointsRequest.

        **参数解释**：计算资源ID。可通过[查询计算资源列表]获取计算资源ID(ListV2Computes.xml)。 **约束限制**：不涉及。 **取值范围**：长度为1~36的英文字符、数字和中划线的组合。 **默认取值**：不涉及。 

        :param compute_id: The compute_id of this ListV2EndpointsRequest.
        :type compute_id: str
        """
        self._compute_id = compute_id

    @property
    def offset(self):
        r"""Gets the offset of this ListV2EndpointsRequest.

        **参数解释**：偏移量，表示从此偏移量开始查询。 **约束限制**：不涉及。 **取值范围**：0~1000000000。 **默认取值**：0。

        :return: The offset of this ListV2EndpointsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListV2EndpointsRequest.

        **参数解释**：偏移量，表示从此偏移量开始查询。 **约束限制**：不涉及。 **取值范围**：0~1000000000。 **默认取值**：0。

        :param offset: The offset of this ListV2EndpointsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListV2EndpointsRequest.

        **参数解释**：指定每一页返回的最大条目数。 **约束限制**：不涉及。 **取值范围**：1~100。 **默认取值**：10。

        :return: The limit of this ListV2EndpointsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListV2EndpointsRequest.

        **参数解释**：指定每一页返回的最大条目数。 **约束限制**：不涉及。 **取值范围**：1~100。 **默认取值**：10。

        :param limit: The limit of this ListV2EndpointsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def name(self):
        r"""Gets the name of this ListV2EndpointsRequest.

        **参数解释**：端点名称，精确查询。 **约束限制**：不涉及。 **取值范围**：长度为1~63个字符，遵循RFC 1035规范，支持小写字母、数字、中划线，必须字母开头、字母或数字结尾。 **默认取值**：不涉及。 

        :return: The name of this ListV2EndpointsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListV2EndpointsRequest.

        **参数解释**：端点名称，精确查询。 **约束限制**：不涉及。 **取值范围**：长度为1~63个字符，遵循RFC 1035规范，支持小写字母、数字、中划线，必须字母开头、字母或数字结尾。 **默认取值**：不涉及。 

        :param name: The name of this ListV2EndpointsRequest.
        :type name: str
        """
        self._name = name

    @property
    def storage_id(self):
        r"""Gets the storage_id of this ListV2EndpointsRequest.

        **参数解释**：存储资源ID，可通过[查询存储资源列表](ListV2Storages.xml)获取存储资源ID。 **约束限制**：不涉及。 **取值范围**：长度为1~64的英文字符、数字和中划线的组合。 **默认取值**：不涉及。 

        :return: The storage_id of this ListV2EndpointsRequest.
        :rtype: str
        """
        return self._storage_id

    @storage_id.setter
    def storage_id(self, storage_id):
        r"""Sets the storage_id of this ListV2EndpointsRequest.

        **参数解释**：存储资源ID，可通过[查询存储资源列表](ListV2Storages.xml)获取存储资源ID。 **约束限制**：不涉及。 **取值范围**：长度为1~64的英文字符、数字和中划线的组合。 **默认取值**：不涉及。 

        :param storage_id: The storage_id of this ListV2EndpointsRequest.
        :type storage_id: str
        """
        self._storage_id = storage_id

    @property
    def tags(self):
        r"""Gets the tags of this ListV2EndpointsRequest.

        **参数解释**：标签过滤条件，支持多个标签。格式为 key#value1,value2，用英文逗号分隔多个值。 **约束限制**：最多10个标签。 

        :return: The tags of this ListV2EndpointsRequest.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ListV2EndpointsRequest.

        **参数解释**：标签过滤条件，支持多个标签。格式为 key#value1,value2，用英文逗号分隔多个值。 **约束限制**：最多10个标签。 

        :param tags: The tags of this ListV2EndpointsRequest.
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
        if not isinstance(other, ListV2EndpointsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
