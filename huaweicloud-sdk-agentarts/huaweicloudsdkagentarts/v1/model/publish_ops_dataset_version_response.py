# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PublishOpsDatasetVersionResponse(SdkResponse):

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
        'version': 'str',
        'version_num': 'int',
        'description': 'str',
        'item_count': 'int',
        'schema_snapshot': 'list[OpsSchemaInfo]',
        'created_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'version': 'version',
        'version_num': 'version_num',
        'description': 'description',
        'item_count': 'item_count',
        'schema_snapshot': 'schema_snapshot',
        'created_at': 'created_at'
    }

    def __init__(self, id=None, version=None, version_num=None, description=None, item_count=None, schema_snapshot=None, created_at=None):
        r"""PublishOpsDatasetVersionResponse

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 版本的内部唯一标识符。 **取值范围：** 符合通用唯一识别码(UUID)标准的字符串。
        :type id: str
        :param version: **参数解释：** 发布的版本显示名称。 **取值范围：** 自定义字符串。
        :type version: str
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

        self._id = None
        self._version = None
        self._version_num = None
        self._description = None
        self._item_count = None
        self._schema_snapshot = None
        self._created_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if version is not None:
            self.version = version
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
    def id(self):
        r"""Gets the id of this PublishOpsDatasetVersionResponse.

        **参数解释：** 版本的内部唯一标识符。 **取值范围：** 符合通用唯一识别码(UUID)标准的字符串。

        :return: The id of this PublishOpsDatasetVersionResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this PublishOpsDatasetVersionResponse.

        **参数解释：** 版本的内部唯一标识符。 **取值范围：** 符合通用唯一识别码(UUID)标准的字符串。

        :param id: The id of this PublishOpsDatasetVersionResponse.
        :type id: str
        """
        self._id = id

    @property
    def version(self):
        r"""Gets the version of this PublishOpsDatasetVersionResponse.

        **参数解释：** 发布的版本显示名称。 **取值范围：** 自定义字符串。

        :return: The version of this PublishOpsDatasetVersionResponse.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this PublishOpsDatasetVersionResponse.

        **参数解释：** 发布的版本显示名称。 **取值范围：** 自定义字符串。

        :param version: The version of this PublishOpsDatasetVersionResponse.
        :type version: str
        """
        self._version = version

    @property
    def version_num(self):
        r"""Gets the version_num of this PublishOpsDatasetVersionResponse.

        **参数解释：** 系统生成的递增版本序号。 **取值范围：** 0到2147483647。

        :return: The version_num of this PublishOpsDatasetVersionResponse.
        :rtype: int
        """
        return self._version_num

    @version_num.setter
    def version_num(self, version_num):
        r"""Sets the version_num of this PublishOpsDatasetVersionResponse.

        **参数解释：** 系统生成的递增版本序号。 **取值范围：** 0到2147483647。

        :param version_num: The version_num of this PublishOpsDatasetVersionResponse.
        :type version_num: int
        """
        self._version_num = version_num

    @property
    def description(self):
        r"""Gets the description of this PublishOpsDatasetVersionResponse.

        **参数解释：** 该版本的详细备注说明。 **取值范围：** 任意字符串。

        :return: The description of this PublishOpsDatasetVersionResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this PublishOpsDatasetVersionResponse.

        **参数解释：** 该版本的详细备注说明。 **取值范围：** 任意字符串。

        :param description: The description of this PublishOpsDatasetVersionResponse.
        :type description: str
        """
        self._description = description

    @property
    def item_count(self):
        r"""Gets the item_count of this PublishOpsDatasetVersionResponse.

        **参数解释：** 该版本快照中包含的数据条目总数。 **取值范围：** 0到2147483647。

        :return: The item_count of this PublishOpsDatasetVersionResponse.
        :rtype: int
        """
        return self._item_count

    @item_count.setter
    def item_count(self, item_count):
        r"""Sets the item_count of this PublishOpsDatasetVersionResponse.

        **参数解释：** 该版本快照中包含的数据条目总数。 **取值范围：** 0到2147483647。

        :param item_count: The item_count of this PublishOpsDatasetVersionResponse.
        :type item_count: int
        """
        self._item_count = item_count

    @property
    def schema_snapshot(self):
        r"""Gets the schema_snapshot of this PublishOpsDatasetVersionResponse.

        **参数解释：** 发布该版本时的数据结构定义快照。 **取值范围：** OpsSchemaInfo 对象列表。

        :return: The schema_snapshot of this PublishOpsDatasetVersionResponse.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.OpsSchemaInfo`]
        """
        return self._schema_snapshot

    @schema_snapshot.setter
    def schema_snapshot(self, schema_snapshot):
        r"""Sets the schema_snapshot of this PublishOpsDatasetVersionResponse.

        **参数解释：** 发布该版本时的数据结构定义快照。 **取值范围：** OpsSchemaInfo 对象列表。

        :param schema_snapshot: The schema_snapshot of this PublishOpsDatasetVersionResponse.
        :type schema_snapshot: list[:class:`huaweicloudsdkagentarts.v1.OpsSchemaInfo`]
        """
        self._schema_snapshot = schema_snapshot

    @property
    def created_at(self):
        r"""Gets the created_at of this PublishOpsDatasetVersionResponse.

        **参数解释：** 版本的正式发布时间。 **取值范围：** UTC 时间字符串。

        :return: The created_at of this PublishOpsDatasetVersionResponse.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this PublishOpsDatasetVersionResponse.

        **参数解释：** 版本的正式发布时间。 **取值范围：** UTC 时间字符串。

        :param created_at: The created_at of this PublishOpsDatasetVersionResponse.
        :type created_at: datetime
        """
        self._created_at = created_at

    def to_dict(self):
        import warnings
        warnings.warn("PublishOpsDatasetVersionResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, PublishOpsDatasetVersionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
