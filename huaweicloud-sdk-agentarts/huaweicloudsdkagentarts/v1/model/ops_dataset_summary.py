# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpsDatasetSummary:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'description': 'str',
        'latest_version': 'str',
        'item_count': 'int',
        'change_uncommitted': 'bool',
        'schemas': 'list[OpsSchemaInfo]',
        'base_info': 'OpsBaseInfo',
        'latest_version_id': 'str',
        'turn_type': 'str',
        'is_preset': 'bool',
        'can_delete': 'bool',
        'reference_count': 'int',
        'tags': 'list[OpsTmsTag]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'latest_version': 'latest_version',
        'item_count': 'item_count',
        'change_uncommitted': 'change_uncommitted',
        'schemas': 'schemas',
        'base_info': 'base_info',
        'latest_version_id': 'latest_version_id',
        'turn_type': 'turn_type',
        'is_preset': 'is_preset',
        'can_delete': 'can_delete',
        'reference_count': 'reference_count',
        'tags': 'tags'
    }

    def __init__(self, id=None, name=None, description=None, latest_version=None, item_count=None, change_uncommitted=None, schemas=None, base_info=None, latest_version_id=None, turn_type=None, is_preset=None, can_delete=None, reference_count=None, tags=None):
        r"""OpsDatasetSummary

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 评测集的全局唯一标识符。 **取值范围：** 符合通用唯一识别码(UUID)标准的字符串。 
        :type id: str
        :param name: **参数解释：** 评测集的显示名称。 **取值范围：** 中英文、数字及常见特殊字符。 
        :type name: str
        :param description: **参数解释：** 对该评测集用途或内容的详细文字说明。 **取值范围：** 任意字符串。 
        :type description: str
        :param latest_version: **参数解释：** 该评测集当前已发布的最新版本号。 **取值范围：** 版本号格式字符串（如v1.0.0）。 
        :type latest_version: str
        :param item_count: **参数解释：** 评测集中包含的总记录条数。 **取值范围：** 0到2147483647。 
        :type item_count: int
        :param change_uncommitted: **参数解释：** 标识当前草稿态相对于最新发布版本是否有尚未提交的变更。 **取值范围：** - true：有未提交变更 - false：无变更 
        :type change_uncommitted: bool
        :param schemas: **参数解释：** 定义评测集内部数据结构的Schema字段定义列表。 **取值范围：** 符合OpsSchemaInfo定义的对象列表。 
        :type schemas: list[:class:`huaweicloudsdkagentarts.v1.OpsSchemaInfo`]
        :param base_info: 
        :type base_info: :class:`huaweicloudsdkagentarts.v1.OpsBaseInfo`
        :param latest_version_id: **参数解释：** 该评测集当前已发布的最新版本号uuid。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 
        :type latest_version_id: str
        :param turn_type: **参数解释：** 该评测集对话轮次（turn）的类型。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 
        :type turn_type: str
        :param is_preset: **参数解释：** 该评测集是否预置。 **约束限制：** 不涉及。 **取值范围：** - true: 评测集为预置 - false: 评测集为非预置 
        :type is_preset: bool
        :param can_delete: **参数解释：** 该评测集是否能删除。 **约束限制：** 不涉及。 **取值范围：** - true: 可以删除 - false: 不可删除 
        :type can_delete: bool
        :param reference_count: **参数解释：** 评测集被引用次数。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 
        :type reference_count: int
        :param tags: **参数解释：** 评测集绑定的TMS标签列表。数组内每个元素为OpsTmsTag对象，包含标签的键值信息。 **约束限制：** 不涉及。
        :type tags: list[:class:`huaweicloudsdkagentarts.v1.OpsTmsTag`]
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._latest_version = None
        self._item_count = None
        self._change_uncommitted = None
        self._schemas = None
        self._base_info = None
        self._latest_version_id = None
        self._turn_type = None
        self._is_preset = None
        self._can_delete = None
        self._reference_count = None
        self._tags = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if latest_version is not None:
            self.latest_version = latest_version
        if item_count is not None:
            self.item_count = item_count
        if change_uncommitted is not None:
            self.change_uncommitted = change_uncommitted
        if schemas is not None:
            self.schemas = schemas
        if base_info is not None:
            self.base_info = base_info
        if latest_version_id is not None:
            self.latest_version_id = latest_version_id
        if turn_type is not None:
            self.turn_type = turn_type
        if is_preset is not None:
            self.is_preset = is_preset
        if can_delete is not None:
            self.can_delete = can_delete
        if reference_count is not None:
            self.reference_count = reference_count
        if tags is not None:
            self.tags = tags

    @property
    def id(self):
        r"""Gets the id of this OpsDatasetSummary.

        **参数解释：** 评测集的全局唯一标识符。 **取值范围：** 符合通用唯一识别码(UUID)标准的字符串。 

        :return: The id of this OpsDatasetSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this OpsDatasetSummary.

        **参数解释：** 评测集的全局唯一标识符。 **取值范围：** 符合通用唯一识别码(UUID)标准的字符串。 

        :param id: The id of this OpsDatasetSummary.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this OpsDatasetSummary.

        **参数解释：** 评测集的显示名称。 **取值范围：** 中英文、数字及常见特殊字符。 

        :return: The name of this OpsDatasetSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this OpsDatasetSummary.

        **参数解释：** 评测集的显示名称。 **取值范围：** 中英文、数字及常见特殊字符。 

        :param name: The name of this OpsDatasetSummary.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this OpsDatasetSummary.

        **参数解释：** 对该评测集用途或内容的详细文字说明。 **取值范围：** 任意字符串。 

        :return: The description of this OpsDatasetSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this OpsDatasetSummary.

        **参数解释：** 对该评测集用途或内容的详细文字说明。 **取值范围：** 任意字符串。 

        :param description: The description of this OpsDatasetSummary.
        :type description: str
        """
        self._description = description

    @property
    def latest_version(self):
        r"""Gets the latest_version of this OpsDatasetSummary.

        **参数解释：** 该评测集当前已发布的最新版本号。 **取值范围：** 版本号格式字符串（如v1.0.0）。 

        :return: The latest_version of this OpsDatasetSummary.
        :rtype: str
        """
        return self._latest_version

    @latest_version.setter
    def latest_version(self, latest_version):
        r"""Sets the latest_version of this OpsDatasetSummary.

        **参数解释：** 该评测集当前已发布的最新版本号。 **取值范围：** 版本号格式字符串（如v1.0.0）。 

        :param latest_version: The latest_version of this OpsDatasetSummary.
        :type latest_version: str
        """
        self._latest_version = latest_version

    @property
    def item_count(self):
        r"""Gets the item_count of this OpsDatasetSummary.

        **参数解释：** 评测集中包含的总记录条数。 **取值范围：** 0到2147483647。 

        :return: The item_count of this OpsDatasetSummary.
        :rtype: int
        """
        return self._item_count

    @item_count.setter
    def item_count(self, item_count):
        r"""Sets the item_count of this OpsDatasetSummary.

        **参数解释：** 评测集中包含的总记录条数。 **取值范围：** 0到2147483647。 

        :param item_count: The item_count of this OpsDatasetSummary.
        :type item_count: int
        """
        self._item_count = item_count

    @property
    def change_uncommitted(self):
        r"""Gets the change_uncommitted of this OpsDatasetSummary.

        **参数解释：** 标识当前草稿态相对于最新发布版本是否有尚未提交的变更。 **取值范围：** - true：有未提交变更 - false：无变更 

        :return: The change_uncommitted of this OpsDatasetSummary.
        :rtype: bool
        """
        return self._change_uncommitted

    @change_uncommitted.setter
    def change_uncommitted(self, change_uncommitted):
        r"""Sets the change_uncommitted of this OpsDatasetSummary.

        **参数解释：** 标识当前草稿态相对于最新发布版本是否有尚未提交的变更。 **取值范围：** - true：有未提交变更 - false：无变更 

        :param change_uncommitted: The change_uncommitted of this OpsDatasetSummary.
        :type change_uncommitted: bool
        """
        self._change_uncommitted = change_uncommitted

    @property
    def schemas(self):
        r"""Gets the schemas of this OpsDatasetSummary.

        **参数解释：** 定义评测集内部数据结构的Schema字段定义列表。 **取值范围：** 符合OpsSchemaInfo定义的对象列表。 

        :return: The schemas of this OpsDatasetSummary.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.OpsSchemaInfo`]
        """
        return self._schemas

    @schemas.setter
    def schemas(self, schemas):
        r"""Sets the schemas of this OpsDatasetSummary.

        **参数解释：** 定义评测集内部数据结构的Schema字段定义列表。 **取值范围：** 符合OpsSchemaInfo定义的对象列表。 

        :param schemas: The schemas of this OpsDatasetSummary.
        :type schemas: list[:class:`huaweicloudsdkagentarts.v1.OpsSchemaInfo`]
        """
        self._schemas = schemas

    @property
    def base_info(self):
        r"""Gets the base_info of this OpsDatasetSummary.

        :return: The base_info of this OpsDatasetSummary.
        :rtype: :class:`huaweicloudsdkagentarts.v1.OpsBaseInfo`
        """
        return self._base_info

    @base_info.setter
    def base_info(self, base_info):
        r"""Sets the base_info of this OpsDatasetSummary.

        :param base_info: The base_info of this OpsDatasetSummary.
        :type base_info: :class:`huaweicloudsdkagentarts.v1.OpsBaseInfo`
        """
        self._base_info = base_info

    @property
    def latest_version_id(self):
        r"""Gets the latest_version_id of this OpsDatasetSummary.

        **参数解释：** 该评测集当前已发布的最新版本号uuid。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 

        :return: The latest_version_id of this OpsDatasetSummary.
        :rtype: str
        """
        return self._latest_version_id

    @latest_version_id.setter
    def latest_version_id(self, latest_version_id):
        r"""Sets the latest_version_id of this OpsDatasetSummary.

        **参数解释：** 该评测集当前已发布的最新版本号uuid。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 

        :param latest_version_id: The latest_version_id of this OpsDatasetSummary.
        :type latest_version_id: str
        """
        self._latest_version_id = latest_version_id

    @property
    def turn_type(self):
        r"""Gets the turn_type of this OpsDatasetSummary.

        **参数解释：** 该评测集对话轮次（turn）的类型。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 

        :return: The turn_type of this OpsDatasetSummary.
        :rtype: str
        """
        return self._turn_type

    @turn_type.setter
    def turn_type(self, turn_type):
        r"""Sets the turn_type of this OpsDatasetSummary.

        **参数解释：** 该评测集对话轮次（turn）的类型。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 

        :param turn_type: The turn_type of this OpsDatasetSummary.
        :type turn_type: str
        """
        self._turn_type = turn_type

    @property
    def is_preset(self):
        r"""Gets the is_preset of this OpsDatasetSummary.

        **参数解释：** 该评测集是否预置。 **约束限制：** 不涉及。 **取值范围：** - true: 评测集为预置 - false: 评测集为非预置 

        :return: The is_preset of this OpsDatasetSummary.
        :rtype: bool
        """
        return self._is_preset

    @is_preset.setter
    def is_preset(self, is_preset):
        r"""Sets the is_preset of this OpsDatasetSummary.

        **参数解释：** 该评测集是否预置。 **约束限制：** 不涉及。 **取值范围：** - true: 评测集为预置 - false: 评测集为非预置 

        :param is_preset: The is_preset of this OpsDatasetSummary.
        :type is_preset: bool
        """
        self._is_preset = is_preset

    @property
    def can_delete(self):
        r"""Gets the can_delete of this OpsDatasetSummary.

        **参数解释：** 该评测集是否能删除。 **约束限制：** 不涉及。 **取值范围：** - true: 可以删除 - false: 不可删除 

        :return: The can_delete of this OpsDatasetSummary.
        :rtype: bool
        """
        return self._can_delete

    @can_delete.setter
    def can_delete(self, can_delete):
        r"""Sets the can_delete of this OpsDatasetSummary.

        **参数解释：** 该评测集是否能删除。 **约束限制：** 不涉及。 **取值范围：** - true: 可以删除 - false: 不可删除 

        :param can_delete: The can_delete of this OpsDatasetSummary.
        :type can_delete: bool
        """
        self._can_delete = can_delete

    @property
    def reference_count(self):
        r"""Gets the reference_count of this OpsDatasetSummary.

        **参数解释：** 评测集被引用次数。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 

        :return: The reference_count of this OpsDatasetSummary.
        :rtype: int
        """
        return self._reference_count

    @reference_count.setter
    def reference_count(self, reference_count):
        r"""Sets the reference_count of this OpsDatasetSummary.

        **参数解释：** 评测集被引用次数。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 

        :param reference_count: The reference_count of this OpsDatasetSummary.
        :type reference_count: int
        """
        self._reference_count = reference_count

    @property
    def tags(self):
        r"""Gets the tags of this OpsDatasetSummary.

        **参数解释：** 评测集绑定的TMS标签列表。数组内每个元素为OpsTmsTag对象，包含标签的键值信息。 **约束限制：** 不涉及。

        :return: The tags of this OpsDatasetSummary.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.OpsTmsTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this OpsDatasetSummary.

        **参数解释：** 评测集绑定的TMS标签列表。数组内每个元素为OpsTmsTag对象，包含标签的键值信息。 **约束限制：** 不涉及。

        :param tags: The tags of this OpsDatasetSummary.
        :type tags: list[:class:`huaweicloudsdkagentarts.v1.OpsTmsTag`]
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
        if not isinstance(other, OpsDatasetSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
