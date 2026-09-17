# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowOpsDatasetVersionResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'created_by': 'OpsEvaluationUserInfo',
        'id': 'str',
        'reference_count': 'int',
        'version': 'str',
        'can_delete': 'bool',
        'version_num': 'int',
        'description': 'str',
        'item_count': 'int',
        'schema_snapshot': 'list[OpsSchemaInfo]',
        'created_at': 'datetime'
    }

    attribute_map = {
        'created_by': 'created_by',
        'id': 'id',
        'reference_count': 'reference_count',
        'version': 'version',
        'can_delete': 'can_delete',
        'version_num': 'version_num',
        'description': 'description',
        'item_count': 'item_count',
        'schema_snapshot': 'schema_snapshot',
        'created_at': 'created_at'
    }

    def __init__(self, created_by=None, id=None, reference_count=None, version=None, can_delete=None, version_num=None, description=None, item_count=None, schema_snapshot=None, created_at=None):
        r"""ShowOpsDatasetVersionResponse

        The model defined in huaweicloud sdk

        :param created_by: 
        :type created_by: :class:`huaweicloudsdkagentarts.v1.OpsEvaluationUserInfo`
        :param id: **参数解释：** 版本的内部唯一标识符。 **取值范围：** 符合通用唯一识别码(UUID)标准的字符串。
        :type id: str
        :param reference_count: **参数解释：** 该版本被评估任务引用的次数。 **约束限制：** 不涉及。 **取值范围：** 0~2147483647。
        :type reference_count: int
        :param version: **参数解释：** 发布的版本显示名称。 **取值范围：** 自定义字符串。
        :type version: str
        :param can_delete: **参数解释：** 该版本是否允许被删除。存在被评估任务引用的版本不可删除。 **约束限制：** 不涉及。 **取值范围：** - true：可删除 - false：不可删除
        :type can_delete: bool
        :param version_num: **参数解释：** 系统生成的递增版本序号。 **取值范围：** 0到2147483647。
        :type version_num: int
        :param description: **参数解释：** 该版本的详细备注说明。 **取值范围：** 任意字符串。
        :type description: str
        :param item_count: **参数解释：** 该版本快照中包含的数据条目总数。 **取值范围：** 0到2147483647。
        :type item_count: int
        :param schema_snapshot: **参数解释：** 发布该版本时的数据结构定义快照。 **取值范围：** OpsSchemaInfo 对象列表。
        :type schema_snapshot: list[:class:`huaweicloudsdkagentarts.v1.OpsSchemaInfo`]
        :param created_at: **参数解释：** 版本的正式发布时间。 **取值范围：** UTC 时间字符串。
        :type created_at: datetime
        """
        
        super().__init__()

        self._created_by = None
        self._id = None
        self._reference_count = None
        self._version = None
        self._can_delete = None
        self._version_num = None
        self._description = None
        self._item_count = None
        self._schema_snapshot = None
        self._created_at = None
        self.discriminator = None

        if created_by is not None:
            self.created_by = created_by
        if id is not None:
            self.id = id
        if reference_count is not None:
            self.reference_count = reference_count
        if version is not None:
            self.version = version
        if can_delete is not None:
            self.can_delete = can_delete
        if version_num is not None:
            self.version_num = version_num
        if description is not None:
            self.description = description
        if item_count is not None:
            self.item_count = item_count
        if schema_snapshot is not None:
            self.schema_snapshot = schema_snapshot
        if created_at is not None:
            self.created_at = created_at

    @property
    def created_by(self):
        r"""Gets the created_by of this ShowOpsDatasetVersionResponse.

        :return: The created_by of this ShowOpsDatasetVersionResponse.
        :rtype: :class:`huaweicloudsdkagentarts.v1.OpsEvaluationUserInfo`
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        r"""Sets the created_by of this ShowOpsDatasetVersionResponse.

        :param created_by: The created_by of this ShowOpsDatasetVersionResponse.
        :type created_by: :class:`huaweicloudsdkagentarts.v1.OpsEvaluationUserInfo`
        """
        self._created_by = created_by

    @property
    def id(self):
        r"""Gets the id of this ShowOpsDatasetVersionResponse.

        **参数解释：** 版本的内部唯一标识符。 **取值范围：** 符合通用唯一识别码(UUID)标准的字符串。

        :return: The id of this ShowOpsDatasetVersionResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowOpsDatasetVersionResponse.

        **参数解释：** 版本的内部唯一标识符。 **取值范围：** 符合通用唯一识别码(UUID)标准的字符串。

        :param id: The id of this ShowOpsDatasetVersionResponse.
        :type id: str
        """
        self._id = id

    @property
    def reference_count(self):
        r"""Gets the reference_count of this ShowOpsDatasetVersionResponse.

        **参数解释：** 该版本被评估任务引用的次数。 **约束限制：** 不涉及。 **取值范围：** 0~2147483647。

        :return: The reference_count of this ShowOpsDatasetVersionResponse.
        :rtype: int
        """
        return self._reference_count

    @reference_count.setter
    def reference_count(self, reference_count):
        r"""Sets the reference_count of this ShowOpsDatasetVersionResponse.

        **参数解释：** 该版本被评估任务引用的次数。 **约束限制：** 不涉及。 **取值范围：** 0~2147483647。

        :param reference_count: The reference_count of this ShowOpsDatasetVersionResponse.
        :type reference_count: int
        """
        self._reference_count = reference_count

    @property
    def version(self):
        r"""Gets the version of this ShowOpsDatasetVersionResponse.

        **参数解释：** 发布的版本显示名称。 **取值范围：** 自定义字符串。

        :return: The version of this ShowOpsDatasetVersionResponse.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ShowOpsDatasetVersionResponse.

        **参数解释：** 发布的版本显示名称。 **取值范围：** 自定义字符串。

        :param version: The version of this ShowOpsDatasetVersionResponse.
        :type version: str
        """
        self._version = version

    @property
    def can_delete(self):
        r"""Gets the can_delete of this ShowOpsDatasetVersionResponse.

        **参数解释：** 该版本是否允许被删除。存在被评估任务引用的版本不可删除。 **约束限制：** 不涉及。 **取值范围：** - true：可删除 - false：不可删除

        :return: The can_delete of this ShowOpsDatasetVersionResponse.
        :rtype: bool
        """
        return self._can_delete

    @can_delete.setter
    def can_delete(self, can_delete):
        r"""Sets the can_delete of this ShowOpsDatasetVersionResponse.

        **参数解释：** 该版本是否允许被删除。存在被评估任务引用的版本不可删除。 **约束限制：** 不涉及。 **取值范围：** - true：可删除 - false：不可删除

        :param can_delete: The can_delete of this ShowOpsDatasetVersionResponse.
        :type can_delete: bool
        """
        self._can_delete = can_delete

    @property
    def version_num(self):
        r"""Gets the version_num of this ShowOpsDatasetVersionResponse.

        **参数解释：** 系统生成的递增版本序号。 **取值范围：** 0到2147483647。

        :return: The version_num of this ShowOpsDatasetVersionResponse.
        :rtype: int
        """
        return self._version_num

    @version_num.setter
    def version_num(self, version_num):
        r"""Sets the version_num of this ShowOpsDatasetVersionResponse.

        **参数解释：** 系统生成的递增版本序号。 **取值范围：** 0到2147483647。

        :param version_num: The version_num of this ShowOpsDatasetVersionResponse.
        :type version_num: int
        """
        self._version_num = version_num

    @property
    def description(self):
        r"""Gets the description of this ShowOpsDatasetVersionResponse.

        **参数解释：** 该版本的详细备注说明。 **取值范围：** 任意字符串。

        :return: The description of this ShowOpsDatasetVersionResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowOpsDatasetVersionResponse.

        **参数解释：** 该版本的详细备注说明。 **取值范围：** 任意字符串。

        :param description: The description of this ShowOpsDatasetVersionResponse.
        :type description: str
        """
        self._description = description

    @property
    def item_count(self):
        r"""Gets the item_count of this ShowOpsDatasetVersionResponse.

        **参数解释：** 该版本快照中包含的数据条目总数。 **取值范围：** 0到2147483647。

        :return: The item_count of this ShowOpsDatasetVersionResponse.
        :rtype: int
        """
        return self._item_count

    @item_count.setter
    def item_count(self, item_count):
        r"""Sets the item_count of this ShowOpsDatasetVersionResponse.

        **参数解释：** 该版本快照中包含的数据条目总数。 **取值范围：** 0到2147483647。

        :param item_count: The item_count of this ShowOpsDatasetVersionResponse.
        :type item_count: int
        """
        self._item_count = item_count

    @property
    def schema_snapshot(self):
        r"""Gets the schema_snapshot of this ShowOpsDatasetVersionResponse.

        **参数解释：** 发布该版本时的数据结构定义快照。 **取值范围：** OpsSchemaInfo 对象列表。

        :return: The schema_snapshot of this ShowOpsDatasetVersionResponse.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.OpsSchemaInfo`]
        """
        return self._schema_snapshot

    @schema_snapshot.setter
    def schema_snapshot(self, schema_snapshot):
        r"""Sets the schema_snapshot of this ShowOpsDatasetVersionResponse.

        **参数解释：** 发布该版本时的数据结构定义快照。 **取值范围：** OpsSchemaInfo 对象列表。

        :param schema_snapshot: The schema_snapshot of this ShowOpsDatasetVersionResponse.
        :type schema_snapshot: list[:class:`huaweicloudsdkagentarts.v1.OpsSchemaInfo`]
        """
        self._schema_snapshot = schema_snapshot

    @property
    def created_at(self):
        r"""Gets the created_at of this ShowOpsDatasetVersionResponse.

        **参数解释：** 版本的正式发布时间。 **取值范围：** UTC 时间字符串。

        :return: The created_at of this ShowOpsDatasetVersionResponse.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this ShowOpsDatasetVersionResponse.

        **参数解释：** 版本的正式发布时间。 **取值范围：** UTC 时间字符串。

        :param created_at: The created_at of this ShowOpsDatasetVersionResponse.
        :type created_at: datetime
        """
        self._created_at = created_at

    def to_dict(self):
        import warnings
        warnings.warn("ShowOpsDatasetVersionResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ShowOpsDatasetVersionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
