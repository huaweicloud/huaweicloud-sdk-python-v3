# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowOpsDatasetResponse(SdkResponse):

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
        'latest_version_id': 'str',
        'item_count': 'int',
        'change_uncommitted': 'bool',
        'schemas': 'list[OpsSchemaInfo]',
        'versions': 'list[OpsVersionInfo]',
        'base_info': 'OpsBaseInfo'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'latest_version': 'latest_version',
        'latest_version_id': 'latest_version_id',
        'item_count': 'item_count',
        'change_uncommitted': 'change_uncommitted',
        'schemas': 'schemas',
        'versions': 'versions',
        'base_info': 'base_info'
    }

    def __init__(self, id=None, name=None, description=None, latest_version=None, latest_version_id=None, item_count=None, change_uncommitted=None, schemas=None, versions=None, base_info=None):
        r"""ShowOpsDatasetResponse

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 评测集的全局唯一标识符。 **取值范围：** 符合通用唯一识别码(UUID)标准的字符串。 
        :type id: str
        :param name: **参数解释：** 评测集的显示名称。 **取值范围：** 中英文、数字及常见特殊字符。 
        :type name: str
        :param description: **参数解释：** 对该评测集用途或内容的详细文字说明。 **取值范围：** 任意字符串。 
        :type description: str
        :param latest_version: **参数解释：** 该评测集当前已发布的最新版本号。 **取值范围：** 自定义的版本名称字符串。 
        :type latest_version: str
        :param latest_version_id: **参数解释：** 最新发布版本对应的唯一标识符ID。 **取值范围：** 符合通用唯一识别码(UUID)标准的字符串。 
        :type latest_version_id: str
        :param item_count: **参数解释：** 评测集中包含的总记录条数（含未提交的草稿数据）。 **取值范围：** 0到2147483647。 
        :type item_count: int
        :param change_uncommitted: **参数解释：** 标识当前草稿态相对于最新发布版本是否有尚未提交的变更。 **取值范围：** - true：有未提交变更 - false：无变更 
        :type change_uncommitted: bool
        :param schemas: **参数解释：** 定义评测集内部数据结构的字段定义列表。 **取值范围：** 符合OpsSchemaInfo定义的对象列表。 
        :type schemas: list[:class:`huaweicloudsdkagentarts.v1.OpsSchemaInfo`]
        :param versions: **参数解释：** 评测集的历史发布版本详情列表。 **取值范围：** 符合OpsVersionInfo定义的对象列表。 
        :type versions: list[:class:`huaweicloudsdkagentarts.v1.OpsVersionInfo`]
        :param base_info: 
        :type base_info: :class:`huaweicloudsdkagentarts.v1.OpsBaseInfo`
        """
        
        super().__init__()

        self._id = None
        self._name = None
        self._description = None
        self._latest_version = None
        self._latest_version_id = None
        self._item_count = None
        self._change_uncommitted = None
        self._schemas = None
        self._versions = None
        self._base_info = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if latest_version is not None:
            self.latest_version = latest_version
        if latest_version_id is not None:
            self.latest_version_id = latest_version_id
        if item_count is not None:
            self.item_count = item_count
        if change_uncommitted is not None:
            self.change_uncommitted = change_uncommitted
        if schemas is not None:
            self.schemas = schemas
        if versions is not None:
            self.versions = versions
        if base_info is not None:
            self.base_info = base_info

    @property
    def id(self):
        r"""Gets the id of this ShowOpsDatasetResponse.

        **参数解释：** 评测集的全局唯一标识符。 **取值范围：** 符合通用唯一识别码(UUID)标准的字符串。 

        :return: The id of this ShowOpsDatasetResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowOpsDatasetResponse.

        **参数解释：** 评测集的全局唯一标识符。 **取值范围：** 符合通用唯一识别码(UUID)标准的字符串。 

        :param id: The id of this ShowOpsDatasetResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ShowOpsDatasetResponse.

        **参数解释：** 评测集的显示名称。 **取值范围：** 中英文、数字及常见特殊字符。 

        :return: The name of this ShowOpsDatasetResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowOpsDatasetResponse.

        **参数解释：** 评测集的显示名称。 **取值范围：** 中英文、数字及常见特殊字符。 

        :param name: The name of this ShowOpsDatasetResponse.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this ShowOpsDatasetResponse.

        **参数解释：** 对该评测集用途或内容的详细文字说明。 **取值范围：** 任意字符串。 

        :return: The description of this ShowOpsDatasetResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowOpsDatasetResponse.

        **参数解释：** 对该评测集用途或内容的详细文字说明。 **取值范围：** 任意字符串。 

        :param description: The description of this ShowOpsDatasetResponse.
        :type description: str
        """
        self._description = description

    @property
    def latest_version(self):
        r"""Gets the latest_version of this ShowOpsDatasetResponse.

        **参数解释：** 该评测集当前已发布的最新版本号。 **取值范围：** 自定义的版本名称字符串。 

        :return: The latest_version of this ShowOpsDatasetResponse.
        :rtype: str
        """
        return self._latest_version

    @latest_version.setter
    def latest_version(self, latest_version):
        r"""Sets the latest_version of this ShowOpsDatasetResponse.

        **参数解释：** 该评测集当前已发布的最新版本号。 **取值范围：** 自定义的版本名称字符串。 

        :param latest_version: The latest_version of this ShowOpsDatasetResponse.
        :type latest_version: str
        """
        self._latest_version = latest_version

    @property
    def latest_version_id(self):
        r"""Gets the latest_version_id of this ShowOpsDatasetResponse.

        **参数解释：** 最新发布版本对应的唯一标识符ID。 **取值范围：** 符合通用唯一识别码(UUID)标准的字符串。 

        :return: The latest_version_id of this ShowOpsDatasetResponse.
        :rtype: str
        """
        return self._latest_version_id

    @latest_version_id.setter
    def latest_version_id(self, latest_version_id):
        r"""Sets the latest_version_id of this ShowOpsDatasetResponse.

        **参数解释：** 最新发布版本对应的唯一标识符ID。 **取值范围：** 符合通用唯一识别码(UUID)标准的字符串。 

        :param latest_version_id: The latest_version_id of this ShowOpsDatasetResponse.
        :type latest_version_id: str
        """
        self._latest_version_id = latest_version_id

    @property
    def item_count(self):
        r"""Gets the item_count of this ShowOpsDatasetResponse.

        **参数解释：** 评测集中包含的总记录条数（含未提交的草稿数据）。 **取值范围：** 0到2147483647。 

        :return: The item_count of this ShowOpsDatasetResponse.
        :rtype: int
        """
        return self._item_count

    @item_count.setter
    def item_count(self, item_count):
        r"""Sets the item_count of this ShowOpsDatasetResponse.

        **参数解释：** 评测集中包含的总记录条数（含未提交的草稿数据）。 **取值范围：** 0到2147483647。 

        :param item_count: The item_count of this ShowOpsDatasetResponse.
        :type item_count: int
        """
        self._item_count = item_count

    @property
    def change_uncommitted(self):
        r"""Gets the change_uncommitted of this ShowOpsDatasetResponse.

        **参数解释：** 标识当前草稿态相对于最新发布版本是否有尚未提交的变更。 **取值范围：** - true：有未提交变更 - false：无变更 

        :return: The change_uncommitted of this ShowOpsDatasetResponse.
        :rtype: bool
        """
        return self._change_uncommitted

    @change_uncommitted.setter
    def change_uncommitted(self, change_uncommitted):
        r"""Sets the change_uncommitted of this ShowOpsDatasetResponse.

        **参数解释：** 标识当前草稿态相对于最新发布版本是否有尚未提交的变更。 **取值范围：** - true：有未提交变更 - false：无变更 

        :param change_uncommitted: The change_uncommitted of this ShowOpsDatasetResponse.
        :type change_uncommitted: bool
        """
        self._change_uncommitted = change_uncommitted

    @property
    def schemas(self):
        r"""Gets the schemas of this ShowOpsDatasetResponse.

        **参数解释：** 定义评测集内部数据结构的字段定义列表。 **取值范围：** 符合OpsSchemaInfo定义的对象列表。 

        :return: The schemas of this ShowOpsDatasetResponse.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.OpsSchemaInfo`]
        """
        return self._schemas

    @schemas.setter
    def schemas(self, schemas):
        r"""Sets the schemas of this ShowOpsDatasetResponse.

        **参数解释：** 定义评测集内部数据结构的字段定义列表。 **取值范围：** 符合OpsSchemaInfo定义的对象列表。 

        :param schemas: The schemas of this ShowOpsDatasetResponse.
        :type schemas: list[:class:`huaweicloudsdkagentarts.v1.OpsSchemaInfo`]
        """
        self._schemas = schemas

    @property
    def versions(self):
        r"""Gets the versions of this ShowOpsDatasetResponse.

        **参数解释：** 评测集的历史发布版本详情列表。 **取值范围：** 符合OpsVersionInfo定义的对象列表。 

        :return: The versions of this ShowOpsDatasetResponse.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.OpsVersionInfo`]
        """
        return self._versions

    @versions.setter
    def versions(self, versions):
        r"""Sets the versions of this ShowOpsDatasetResponse.

        **参数解释：** 评测集的历史发布版本详情列表。 **取值范围：** 符合OpsVersionInfo定义的对象列表。 

        :param versions: The versions of this ShowOpsDatasetResponse.
        :type versions: list[:class:`huaweicloudsdkagentarts.v1.OpsVersionInfo`]
        """
        self._versions = versions

    @property
    def base_info(self):
        r"""Gets the base_info of this ShowOpsDatasetResponse.

        :return: The base_info of this ShowOpsDatasetResponse.
        :rtype: :class:`huaweicloudsdkagentarts.v1.OpsBaseInfo`
        """
        return self._base_info

    @base_info.setter
    def base_info(self, base_info):
        r"""Sets the base_info of this ShowOpsDatasetResponse.

        :param base_info: The base_info of this ShowOpsDatasetResponse.
        :type base_info: :class:`huaweicloudsdkagentarts.v1.OpsBaseInfo`
        """
        self._base_info = base_info

    def to_dict(self):
        import warnings
        warnings.warn("ShowOpsDatasetResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowOpsDatasetResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
