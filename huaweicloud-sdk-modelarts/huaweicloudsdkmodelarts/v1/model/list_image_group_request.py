# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListImageGroupRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'name_fuzzy_match': 'bool',
        'namespace': 'str',
        'type': 'str',
        'workspace_id': 'str',
        'limit': 'int',
        'offset': 'int',
        'swr_instance_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'name_fuzzy_match': 'name_fuzzy_match',
        'namespace': 'namespace',
        'type': 'type',
        'workspace_id': 'workspace_id',
        'limit': 'limit',
        'offset': 'offset',
        'swr_instance_id': 'swr_instance_id'
    }

    def __init__(self, name=None, name_fuzzy_match=None, namespace=None, type=None, workspace_id=None, limit=None, offset=None, swr_instance_id=None):
        r"""ListImageGroupRequest

        The model defined in huaweicloud sdk

        :param name: **参数解释**：镜像名称。 **约束限制**：不涉及。 **取值范围**：长度限制为512个字符，支持小写字母、数字、中划线、下划线和点。 **默认取值**：不涉及。
        :type name: str
        :param name_fuzzy_match: **参数解释**：镜像名称是否模糊匹配查询。 **约束限制**：不涉及。 **取值范围**：布尔类型： - true：支持模糊匹配查询。 - false：不支持模糊匹配查询。  **默认取值**：true。
        :type name_fuzzy_match: bool
        :param namespace: **参数解释**：镜像所属组织，可以在SWR控制台“组织管理”创建和查看。 **约束限制**：不涉及。 **取值范围**：长度限制为64个字符，支持大小写字母、数字、中划线、下划线和点号，且必须是小写字母开头。 **默认取值**：不涉及。
        :type namespace: str
        :param type: **参数解释**：镜像类型。 **约束限制**：不涉及。 **取值范围**：枚举类型，取值如下： - BUILD_IN：系统内置镜像。 - DEDICATED：用户保存的镜像。  **默认取值**：不涉及。
        :type type: str
        :param workspace_id: **参数解释**：工作空间ID。[获取方法请参见[查询工作空间列表](ListWorkspace.xml)。](tag:hc)未创建工作空间时默认值为“0”，存在创建并使用的工作空间，以实际取值为准。 **约束限制**：不涉及。 **取值范围**：0或32位仅包含字符0-9或小写字母a-z的字符串。 **默认取值**：0。
        :type workspace_id: str
        :param limit: **参数解释**：每一页显示的镜像实例数量。 **约束限制**：不涉及。 **取值范围**：正整数。 **默认取值**：200。
        :type limit: int
        :param offset: **参数解释**：分页记录的起始位置偏移量。 **约束限制**：不涉及。 **取值范围**：非负整数。 **默认取值**：0。
        :type offset: int
        :param swr_instance_id: **参数解释**：企业版SWR仓库ID。 **参数约束**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type swr_instance_id: str
        """
        
        

        self._name = None
        self._name_fuzzy_match = None
        self._namespace = None
        self._type = None
        self._workspace_id = None
        self._limit = None
        self._offset = None
        self._swr_instance_id = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if name_fuzzy_match is not None:
            self.name_fuzzy_match = name_fuzzy_match
        if namespace is not None:
            self.namespace = namespace
        if type is not None:
            self.type = type
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if swr_instance_id is not None:
            self.swr_instance_id = swr_instance_id

    @property
    def name(self):
        r"""Gets the name of this ListImageGroupRequest.

        **参数解释**：镜像名称。 **约束限制**：不涉及。 **取值范围**：长度限制为512个字符，支持小写字母、数字、中划线、下划线和点。 **默认取值**：不涉及。

        :return: The name of this ListImageGroupRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListImageGroupRequest.

        **参数解释**：镜像名称。 **约束限制**：不涉及。 **取值范围**：长度限制为512个字符，支持小写字母、数字、中划线、下划线和点。 **默认取值**：不涉及。

        :param name: The name of this ListImageGroupRequest.
        :type name: str
        """
        self._name = name

    @property
    def name_fuzzy_match(self):
        r"""Gets the name_fuzzy_match of this ListImageGroupRequest.

        **参数解释**：镜像名称是否模糊匹配查询。 **约束限制**：不涉及。 **取值范围**：布尔类型： - true：支持模糊匹配查询。 - false：不支持模糊匹配查询。  **默认取值**：true。

        :return: The name_fuzzy_match of this ListImageGroupRequest.
        :rtype: bool
        """
        return self._name_fuzzy_match

    @name_fuzzy_match.setter
    def name_fuzzy_match(self, name_fuzzy_match):
        r"""Sets the name_fuzzy_match of this ListImageGroupRequest.

        **参数解释**：镜像名称是否模糊匹配查询。 **约束限制**：不涉及。 **取值范围**：布尔类型： - true：支持模糊匹配查询。 - false：不支持模糊匹配查询。  **默认取值**：true。

        :param name_fuzzy_match: The name_fuzzy_match of this ListImageGroupRequest.
        :type name_fuzzy_match: bool
        """
        self._name_fuzzy_match = name_fuzzy_match

    @property
    def namespace(self):
        r"""Gets the namespace of this ListImageGroupRequest.

        **参数解释**：镜像所属组织，可以在SWR控制台“组织管理”创建和查看。 **约束限制**：不涉及。 **取值范围**：长度限制为64个字符，支持大小写字母、数字、中划线、下划线和点号，且必须是小写字母开头。 **默认取值**：不涉及。

        :return: The namespace of this ListImageGroupRequest.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this ListImageGroupRequest.

        **参数解释**：镜像所属组织，可以在SWR控制台“组织管理”创建和查看。 **约束限制**：不涉及。 **取值范围**：长度限制为64个字符，支持大小写字母、数字、中划线、下划线和点号，且必须是小写字母开头。 **默认取值**：不涉及。

        :param namespace: The namespace of this ListImageGroupRequest.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def type(self):
        r"""Gets the type of this ListImageGroupRequest.

        **参数解释**：镜像类型。 **约束限制**：不涉及。 **取值范围**：枚举类型，取值如下： - BUILD_IN：系统内置镜像。 - DEDICATED：用户保存的镜像。  **默认取值**：不涉及。

        :return: The type of this ListImageGroupRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListImageGroupRequest.

        **参数解释**：镜像类型。 **约束限制**：不涉及。 **取值范围**：枚举类型，取值如下： - BUILD_IN：系统内置镜像。 - DEDICATED：用户保存的镜像。  **默认取值**：不涉及。

        :param type: The type of this ListImageGroupRequest.
        :type type: str
        """
        self._type = type

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ListImageGroupRequest.

        **参数解释**：工作空间ID。[获取方法请参见[查询工作空间列表](ListWorkspace.xml)。](tag:hc)未创建工作空间时默认值为“0”，存在创建并使用的工作空间，以实际取值为准。 **约束限制**：不涉及。 **取值范围**：0或32位仅包含字符0-9或小写字母a-z的字符串。 **默认取值**：0。

        :return: The workspace_id of this ListImageGroupRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ListImageGroupRequest.

        **参数解释**：工作空间ID。[获取方法请参见[查询工作空间列表](ListWorkspace.xml)。](tag:hc)未创建工作空间时默认值为“0”，存在创建并使用的工作空间，以实际取值为准。 **约束限制**：不涉及。 **取值范围**：0或32位仅包含字符0-9或小写字母a-z的字符串。 **默认取值**：0。

        :param workspace_id: The workspace_id of this ListImageGroupRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def limit(self):
        r"""Gets the limit of this ListImageGroupRequest.

        **参数解释**：每一页显示的镜像实例数量。 **约束限制**：不涉及。 **取值范围**：正整数。 **默认取值**：200。

        :return: The limit of this ListImageGroupRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListImageGroupRequest.

        **参数解释**：每一页显示的镜像实例数量。 **约束限制**：不涉及。 **取值范围**：正整数。 **默认取值**：200。

        :param limit: The limit of this ListImageGroupRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListImageGroupRequest.

        **参数解释**：分页记录的起始位置偏移量。 **约束限制**：不涉及。 **取值范围**：非负整数。 **默认取值**：0。

        :return: The offset of this ListImageGroupRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListImageGroupRequest.

        **参数解释**：分页记录的起始位置偏移量。 **约束限制**：不涉及。 **取值范围**：非负整数。 **默认取值**：0。

        :param offset: The offset of this ListImageGroupRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def swr_instance_id(self):
        r"""Gets the swr_instance_id of this ListImageGroupRequest.

        **参数解释**：企业版SWR仓库ID。 **参数约束**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The swr_instance_id of this ListImageGroupRequest.
        :rtype: str
        """
        return self._swr_instance_id

    @swr_instance_id.setter
    def swr_instance_id(self, swr_instance_id):
        r"""Sets the swr_instance_id of this ListImageGroupRequest.

        **参数解释**：企业版SWR仓库ID。 **参数约束**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param swr_instance_id: The swr_instance_id of this ListImageGroupRequest.
        :type swr_instance_id: str
        """
        self._swr_instance_id = swr_instance_id

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
        if not isinstance(other, ListImageGroupRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
