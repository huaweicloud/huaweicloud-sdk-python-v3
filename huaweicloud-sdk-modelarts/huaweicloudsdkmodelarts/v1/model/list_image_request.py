# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListImageRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'name': 'str',
        'name_fuzzy_match': 'bool',
        'namespace': 'str',
        'offset': 'int',
        'service_type': 'str',
        'sort_dir': 'str',
        'sort_key': 'str',
        'type': 'str',
        'workspace_id': 'str',
        'show_name': 'str',
        'show_tag': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'name': 'name',
        'name_fuzzy_match': 'name_fuzzy_match',
        'namespace': 'namespace',
        'offset': 'offset',
        'service_type': 'service_type',
        'sort_dir': 'sort_dir',
        'sort_key': 'sort_key',
        'type': 'type',
        'workspace_id': 'workspace_id',
        'show_name': 'show_name',
        'show_tag': 'show_tag'
    }

    def __init__(self, limit=None, name=None, name_fuzzy_match=None, namespace=None, offset=None, service_type=None, sort_dir=None, sort_key=None, type=None, workspace_id=None, show_name=None, show_tag=None):
        r"""ListImageRequest

        The model defined in huaweicloud sdk

        :param limit: **参数解释**：每一页显示的镜像实例数量。 **约束限制**：不涉及。 **取值范围**：正整数。 **默认取值**：200。
        :type limit: int
        :param name: **参数解释**：镜像名称。 **约束限制**：不涉及。 **取值范围**：长度限制为512个字符，支持小写字母、数字、中划线、下划线和点。 **默认取值**：不涉及。
        :type name: str
        :param name_fuzzy_match: **参数解释**：镜像名称是否模糊匹配查询。 **约束限制**：不涉及。 **取值范围**：布尔类型： - true：支持模糊匹配查询。 - false：不支持模糊匹配查询。  **默认取值**：true。
        :type name_fuzzy_match: bool
        :param namespace: **参数解释**：镜像所属组织，可以在SWR控制台“组织管理”创建和查看。 **约束限制**：不涉及。 **取值范围**：长度限制为64个字符，支持大小写字母、数字、中划线、下划线和点号，且必须是小写字母开头。 **默认取值**：不涉及。
        :type namespace: str
        :param offset: **参数解释**：分页记录的起始位置偏移量。 **约束限制**：不涉及。 **取值范围**：非负整数。 **默认取值**：0。
        :type offset: int
        :param service_type: **参数解释**：镜像支持服务类型。 **约束限制**：不涉及。 **取值范围**：枚举类型，取值如下： - COMMON：通用镜像。 - INFERENCE: 建议仅在推理部署场景使用。 - TRAIN: 建议仅在训练任务场景使用。 - DEV: 建议仅在开发调测场景使用。 - UNKNOWN: 未明确设置的镜像支持的服务类型。  **默认取值**：UNKNOWN。
        :type service_type: str
        :param sort_dir: **参数解释**：实例排序方式。 **约束限制**：不涉及。 **取值范围**：枚举类型，取值如下： - ASC：升序 - DESC：降序  **默认取值**：DESC。
        :type sort_dir: str
        :param sort_key: **参数解释**：排序的字段，多个字段使用(“,”)逗号分隔。 **约束限制**：不涉及。 **取值范围**：长度限制为128个字符，支持大小写字母、数字、中划线、下划线和逗号。 **默认取值**：不涉及。
        :type sort_key: str
        :param type: **参数解释**：镜像类型。 **约束限制**：不涉及。 **取值范围**：枚举类型，取值如下： - BUILD_IN：系统内置镜像。 - DEDICATED：用户保存的镜像。  **默认取值**：BUILD_IN。
        :type type: str
        :param workspace_id: **参数解释**：工作空间ID。未创建工作空间时默认值为“0”，存在创建并使用的工作空间，以实际取值为准。 **约束限制**：不涉及。 **取值范围**：0或32位仅包含字符0-9或小写字母a-z的字符串。 **默认取值**：0。
        :type workspace_id: str
        :param show_name: **参数解释**：镜像展示name。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type show_name: str
        :param show_tag: **参数解释**：镜像展示Tag。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type show_tag: str
        """
        
        

        self._limit = None
        self._name = None
        self._name_fuzzy_match = None
        self._namespace = None
        self._offset = None
        self._service_type = None
        self._sort_dir = None
        self._sort_key = None
        self._type = None
        self._workspace_id = None
        self._show_name = None
        self._show_tag = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if name is not None:
            self.name = name
        if name_fuzzy_match is not None:
            self.name_fuzzy_match = name_fuzzy_match
        if namespace is not None:
            self.namespace = namespace
        if offset is not None:
            self.offset = offset
        if service_type is not None:
            self.service_type = service_type
        if sort_dir is not None:
            self.sort_dir = sort_dir
        if sort_key is not None:
            self.sort_key = sort_key
        if type is not None:
            self.type = type
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if show_name is not None:
            self.show_name = show_name
        if show_tag is not None:
            self.show_tag = show_tag

    @property
    def limit(self):
        r"""Gets the limit of this ListImageRequest.

        **参数解释**：每一页显示的镜像实例数量。 **约束限制**：不涉及。 **取值范围**：正整数。 **默认取值**：200。

        :return: The limit of this ListImageRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListImageRequest.

        **参数解释**：每一页显示的镜像实例数量。 **约束限制**：不涉及。 **取值范围**：正整数。 **默认取值**：200。

        :param limit: The limit of this ListImageRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def name(self):
        r"""Gets the name of this ListImageRequest.

        **参数解释**：镜像名称。 **约束限制**：不涉及。 **取值范围**：长度限制为512个字符，支持小写字母、数字、中划线、下划线和点。 **默认取值**：不涉及。

        :return: The name of this ListImageRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListImageRequest.

        **参数解释**：镜像名称。 **约束限制**：不涉及。 **取值范围**：长度限制为512个字符，支持小写字母、数字、中划线、下划线和点。 **默认取值**：不涉及。

        :param name: The name of this ListImageRequest.
        :type name: str
        """
        self._name = name

    @property
    def name_fuzzy_match(self):
        r"""Gets the name_fuzzy_match of this ListImageRequest.

        **参数解释**：镜像名称是否模糊匹配查询。 **约束限制**：不涉及。 **取值范围**：布尔类型： - true：支持模糊匹配查询。 - false：不支持模糊匹配查询。  **默认取值**：true。

        :return: The name_fuzzy_match of this ListImageRequest.
        :rtype: bool
        """
        return self._name_fuzzy_match

    @name_fuzzy_match.setter
    def name_fuzzy_match(self, name_fuzzy_match):
        r"""Sets the name_fuzzy_match of this ListImageRequest.

        **参数解释**：镜像名称是否模糊匹配查询。 **约束限制**：不涉及。 **取值范围**：布尔类型： - true：支持模糊匹配查询。 - false：不支持模糊匹配查询。  **默认取值**：true。

        :param name_fuzzy_match: The name_fuzzy_match of this ListImageRequest.
        :type name_fuzzy_match: bool
        """
        self._name_fuzzy_match = name_fuzzy_match

    @property
    def namespace(self):
        r"""Gets the namespace of this ListImageRequest.

        **参数解释**：镜像所属组织，可以在SWR控制台“组织管理”创建和查看。 **约束限制**：不涉及。 **取值范围**：长度限制为64个字符，支持大小写字母、数字、中划线、下划线和点号，且必须是小写字母开头。 **默认取值**：不涉及。

        :return: The namespace of this ListImageRequest.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this ListImageRequest.

        **参数解释**：镜像所属组织，可以在SWR控制台“组织管理”创建和查看。 **约束限制**：不涉及。 **取值范围**：长度限制为64个字符，支持大小写字母、数字、中划线、下划线和点号，且必须是小写字母开头。 **默认取值**：不涉及。

        :param namespace: The namespace of this ListImageRequest.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def offset(self):
        r"""Gets the offset of this ListImageRequest.

        **参数解释**：分页记录的起始位置偏移量。 **约束限制**：不涉及。 **取值范围**：非负整数。 **默认取值**：0。

        :return: The offset of this ListImageRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListImageRequest.

        **参数解释**：分页记录的起始位置偏移量。 **约束限制**：不涉及。 **取值范围**：非负整数。 **默认取值**：0。

        :param offset: The offset of this ListImageRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def service_type(self):
        r"""Gets the service_type of this ListImageRequest.

        **参数解释**：镜像支持服务类型。 **约束限制**：不涉及。 **取值范围**：枚举类型，取值如下： - COMMON：通用镜像。 - INFERENCE: 建议仅在推理部署场景使用。 - TRAIN: 建议仅在训练任务场景使用。 - DEV: 建议仅在开发调测场景使用。 - UNKNOWN: 未明确设置的镜像支持的服务类型。  **默认取值**：UNKNOWN。

        :return: The service_type of this ListImageRequest.
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        r"""Sets the service_type of this ListImageRequest.

        **参数解释**：镜像支持服务类型。 **约束限制**：不涉及。 **取值范围**：枚举类型，取值如下： - COMMON：通用镜像。 - INFERENCE: 建议仅在推理部署场景使用。 - TRAIN: 建议仅在训练任务场景使用。 - DEV: 建议仅在开发调测场景使用。 - UNKNOWN: 未明确设置的镜像支持的服务类型。  **默认取值**：UNKNOWN。

        :param service_type: The service_type of this ListImageRequest.
        :type service_type: str
        """
        self._service_type = service_type

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ListImageRequest.

        **参数解释**：实例排序方式。 **约束限制**：不涉及。 **取值范围**：枚举类型，取值如下： - ASC：升序 - DESC：降序  **默认取值**：DESC。

        :return: The sort_dir of this ListImageRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ListImageRequest.

        **参数解释**：实例排序方式。 **约束限制**：不涉及。 **取值范围**：枚举类型，取值如下： - ASC：升序 - DESC：降序  **默认取值**：DESC。

        :param sort_dir: The sort_dir of this ListImageRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

    @property
    def sort_key(self):
        r"""Gets the sort_key of this ListImageRequest.

        **参数解释**：排序的字段，多个字段使用(“,”)逗号分隔。 **约束限制**：不涉及。 **取值范围**：长度限制为128个字符，支持大小写字母、数字、中划线、下划线和逗号。 **默认取值**：不涉及。

        :return: The sort_key of this ListImageRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this ListImageRequest.

        **参数解释**：排序的字段，多个字段使用(“,”)逗号分隔。 **约束限制**：不涉及。 **取值范围**：长度限制为128个字符，支持大小写字母、数字、中划线、下划线和逗号。 **默认取值**：不涉及。

        :param sort_key: The sort_key of this ListImageRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def type(self):
        r"""Gets the type of this ListImageRequest.

        **参数解释**：镜像类型。 **约束限制**：不涉及。 **取值范围**：枚举类型，取值如下： - BUILD_IN：系统内置镜像。 - DEDICATED：用户保存的镜像。  **默认取值**：BUILD_IN。

        :return: The type of this ListImageRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListImageRequest.

        **参数解释**：镜像类型。 **约束限制**：不涉及。 **取值范围**：枚举类型，取值如下： - BUILD_IN：系统内置镜像。 - DEDICATED：用户保存的镜像。  **默认取值**：BUILD_IN。

        :param type: The type of this ListImageRequest.
        :type type: str
        """
        self._type = type

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ListImageRequest.

        **参数解释**：工作空间ID。未创建工作空间时默认值为“0”，存在创建并使用的工作空间，以实际取值为准。 **约束限制**：不涉及。 **取值范围**：0或32位仅包含字符0-9或小写字母a-z的字符串。 **默认取值**：0。

        :return: The workspace_id of this ListImageRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ListImageRequest.

        **参数解释**：工作空间ID。未创建工作空间时默认值为“0”，存在创建并使用的工作空间，以实际取值为准。 **约束限制**：不涉及。 **取值范围**：0或32位仅包含字符0-9或小写字母a-z的字符串。 **默认取值**：0。

        :param workspace_id: The workspace_id of this ListImageRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def show_name(self):
        r"""Gets the show_name of this ListImageRequest.

        **参数解释**：镜像展示name。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The show_name of this ListImageRequest.
        :rtype: str
        """
        return self._show_name

    @show_name.setter
    def show_name(self, show_name):
        r"""Sets the show_name of this ListImageRequest.

        **参数解释**：镜像展示name。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param show_name: The show_name of this ListImageRequest.
        :type show_name: str
        """
        self._show_name = show_name

    @property
    def show_tag(self):
        r"""Gets the show_tag of this ListImageRequest.

        **参数解释**：镜像展示Tag。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The show_tag of this ListImageRequest.
        :rtype: str
        """
        return self._show_tag

    @show_tag.setter
    def show_tag(self, show_tag):
        r"""Sets the show_tag of this ListImageRequest.

        **参数解释**：镜像展示Tag。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param show_tag: The show_tag of this ListImageRequest.
        :type show_tag: str
        """
        self._show_tag = show_tag

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
        if not isinstance(other, ListImageRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
