# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListV2WorkspacesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enterprise_project_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'name': 'str',
        'id': 'str',
        'tags': 'list[str]'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'offset': 'offset',
        'limit': 'limit',
        'name': 'name',
        'id': 'id',
        'tags': 'tags'
    }

    def __init__(self, enterprise_project_id=None, offset=None, limit=None, name=None, id=None, tags=None):
        r"""ListV2WorkspacesRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**：企业项目ID，获取方法，请参见[获取企业项目ID](aidatalake_02_0042.xml)。 **约束限制**：不涉及。 **取值范围**：长度为1~36的英文字符、数字、中划线和下划线的组合。 **默认取值**：all_granted_eps。 
        :type enterprise_project_id: str
        :param offset: **参数解释**：偏移量，表示从此偏移量开始查询。 **约束限制**：不涉及。 **取值范围**：0~1000000000。 **默认取值**：0。
        :type offset: int
        :param limit: **参数解释**：指定每一页返回的最大条目数。 **约束限制**：不涉及。 **取值范围**：1~100。 **默认取值**：10。
        :type limit: int
        :param name: **参数解释**：工作空间名称。 **约束限制**：不涉及。 **取值范围**：长度为4~32的英文字母、数字、下划线和中划线的组合。 **默认取值**：不涉及。 
        :type name: str
        :param id: **参数解释**：工作空间ID，可通过[获取工作空间ID](aidatalake_02_0044.xml)获取。 **约束限制**：不涉及。 **取值范围**：长度为1~36的英文字符、数字和中划线的组合。 **默认取值**：不涉及。 
        :type id: str
        :param tags: **参数解释**：标签过滤条件，支持多个标签。格式为 key#value1,value2，用英文逗号分隔多个值。 **约束限制**：最多10个标签。 
        :type tags: list[str]
        """
        
        

        self._enterprise_project_id = None
        self._offset = None
        self._limit = None
        self._name = None
        self._id = None
        self._tags = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if tags is not None:
            self.tags = tags

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListV2WorkspacesRequest.

        **参数解释**：企业项目ID，获取方法，请参见[获取企业项目ID](aidatalake_02_0042.xml)。 **约束限制**：不涉及。 **取值范围**：长度为1~36的英文字符、数字、中划线和下划线的组合。 **默认取值**：all_granted_eps。 

        :return: The enterprise_project_id of this ListV2WorkspacesRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListV2WorkspacesRequest.

        **参数解释**：企业项目ID，获取方法，请参见[获取企业项目ID](aidatalake_02_0042.xml)。 **约束限制**：不涉及。 **取值范围**：长度为1~36的英文字符、数字、中划线和下划线的组合。 **默认取值**：all_granted_eps。 

        :param enterprise_project_id: The enterprise_project_id of this ListV2WorkspacesRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def offset(self):
        r"""Gets the offset of this ListV2WorkspacesRequest.

        **参数解释**：偏移量，表示从此偏移量开始查询。 **约束限制**：不涉及。 **取值范围**：0~1000000000。 **默认取值**：0。

        :return: The offset of this ListV2WorkspacesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListV2WorkspacesRequest.

        **参数解释**：偏移量，表示从此偏移量开始查询。 **约束限制**：不涉及。 **取值范围**：0~1000000000。 **默认取值**：0。

        :param offset: The offset of this ListV2WorkspacesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListV2WorkspacesRequest.

        **参数解释**：指定每一页返回的最大条目数。 **约束限制**：不涉及。 **取值范围**：1~100。 **默认取值**：10。

        :return: The limit of this ListV2WorkspacesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListV2WorkspacesRequest.

        **参数解释**：指定每一页返回的最大条目数。 **约束限制**：不涉及。 **取值范围**：1~100。 **默认取值**：10。

        :param limit: The limit of this ListV2WorkspacesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def name(self):
        r"""Gets the name of this ListV2WorkspacesRequest.

        **参数解释**：工作空间名称。 **约束限制**：不涉及。 **取值范围**：长度为4~32的英文字母、数字、下划线和中划线的组合。 **默认取值**：不涉及。 

        :return: The name of this ListV2WorkspacesRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListV2WorkspacesRequest.

        **参数解释**：工作空间名称。 **约束限制**：不涉及。 **取值范围**：长度为4~32的英文字母、数字、下划线和中划线的组合。 **默认取值**：不涉及。 

        :param name: The name of this ListV2WorkspacesRequest.
        :type name: str
        """
        self._name = name

    @property
    def id(self):
        r"""Gets the id of this ListV2WorkspacesRequest.

        **参数解释**：工作空间ID，可通过[获取工作空间ID](aidatalake_02_0044.xml)获取。 **约束限制**：不涉及。 **取值范围**：长度为1~36的英文字符、数字和中划线的组合。 **默认取值**：不涉及。 

        :return: The id of this ListV2WorkspacesRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListV2WorkspacesRequest.

        **参数解释**：工作空间ID，可通过[获取工作空间ID](aidatalake_02_0044.xml)获取。 **约束限制**：不涉及。 **取值范围**：长度为1~36的英文字符、数字和中划线的组合。 **默认取值**：不涉及。 

        :param id: The id of this ListV2WorkspacesRequest.
        :type id: str
        """
        self._id = id

    @property
    def tags(self):
        r"""Gets the tags of this ListV2WorkspacesRequest.

        **参数解释**：标签过滤条件，支持多个标签。格式为 key#value1,value2，用英文逗号分隔多个值。 **约束限制**：最多10个标签。 

        :return: The tags of this ListV2WorkspacesRequest.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ListV2WorkspacesRequest.

        **参数解释**：标签过滤条件，支持多个标签。格式为 key#value1,value2，用英文逗号分隔多个值。 **约束限制**：最多10个标签。 

        :param tags: The tags of this ListV2WorkspacesRequest.
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
        if not isinstance(other, ListV2WorkspacesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
