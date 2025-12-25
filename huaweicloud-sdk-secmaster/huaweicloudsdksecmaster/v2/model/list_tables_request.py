# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTablesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'workspace_id': 'str',
        'category': 'str',
        'table_id': 'str',
        'table_alias': 'str',
        'table_name': 'str',
        'offset': 'int',
        'limit': 'int',
        'sort_key': 'str',
        'sort_dir': 'str',
        'exists': 'bool'
    }

    attribute_map = {
        'project_id': 'project_id',
        'workspace_id': 'workspace_id',
        'category': 'category',
        'table_id': 'table_id',
        'table_alias': 'table_alias',
        'table_name': 'table_name',
        'offset': 'offset',
        'limit': 'limit',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir',
        'exists': 'exists'
    }

    def __init__(self, project_id=None, workspace_id=None, category=None, table_id=None, table_alias=None, table_name=None, offset=None, limit=None, sort_key=None, sort_dir=None, exists=None):
        r"""ListTablesRequest

        The model defined in huaweicloud sdk

        :param project_id: **参数解释：** 项目ID，用于明确项目归属，配置后可通过该ID查询项目下资产，可以通过调用API获取，也可以从控制台获取。[获取项目ID](secmaster_03_0014.xml) **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type project_id: str
        :param workspace_id: 工作空间ID
        :type workspace_id: str
        :param category: **参数解释**: 目录类型 - STREAMING 实时流 - INDEX 索引 - APPLICATION 应用 - TENANT_BUCKET 租户桶 - LAKE 数据湖  **约束限制** 不涉及 **取值范围**: - STREAMING - INDEX - APPLICATION - TENANT_BUCKET - LAKE  **默认值** 不涉及                        
        :type category: str
        :param table_id: 表id
        :type table_id: str
        :param table_alias: 表别名
        :type table_alias: str
        :param table_name: 表名称
        :type table_name: str
        :param offset: **参数解释：** 偏移量 **取值范围：** 0-1000000 **默认取值：** 0
        :type offset: int
        :param limit: **参数解释：** 查询数据限制 **取值范围：** 0-1000 **默认取值：** 不涉及
        :type limit: int
        :param sort_key: 按照属性排序。
        :type sort_key: str
        :param sort_dir: 排序顺序，支持 &#x60;ASC&#x60; 或 &#x60;DESC&#x60;。
        :type sort_dir: str
        :param exists: 是否存在
        :type exists: bool
        """
        
        

        self._project_id = None
        self._workspace_id = None
        self._category = None
        self._table_id = None
        self._table_alias = None
        self._table_name = None
        self._offset = None
        self._limit = None
        self._sort_key = None
        self._sort_dir = None
        self._exists = None
        self.discriminator = None

        self.project_id = project_id
        self.workspace_id = workspace_id
        if category is not None:
            self.category = category
        if table_id is not None:
            self.table_id = table_id
        if table_alias is not None:
            self.table_alias = table_alias
        if table_name is not None:
            self.table_name = table_name
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_dir is not None:
            self.sort_dir = sort_dir
        if exists is not None:
            self.exists = exists

    @property
    def project_id(self):
        r"""Gets the project_id of this ListTablesRequest.

        **参数解释：** 项目ID，用于明确项目归属，配置后可通过该ID查询项目下资产，可以通过调用API获取，也可以从控制台获取。[获取项目ID](secmaster_03_0014.xml) **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The project_id of this ListTablesRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ListTablesRequest.

        **参数解释：** 项目ID，用于明确项目归属，配置后可通过该ID查询项目下资产，可以通过调用API获取，也可以从控制台获取。[获取项目ID](secmaster_03_0014.xml) **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param project_id: The project_id of this ListTablesRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ListTablesRequest.

        工作空间ID

        :return: The workspace_id of this ListTablesRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ListTablesRequest.

        工作空间ID

        :param workspace_id: The workspace_id of this ListTablesRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def category(self):
        r"""Gets the category of this ListTablesRequest.

        **参数解释**: 目录类型 - STREAMING 实时流 - INDEX 索引 - APPLICATION 应用 - TENANT_BUCKET 租户桶 - LAKE 数据湖  **约束限制** 不涉及 **取值范围**: - STREAMING - INDEX - APPLICATION - TENANT_BUCKET - LAKE  **默认值** 不涉及                        

        :return: The category of this ListTablesRequest.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this ListTablesRequest.

        **参数解释**: 目录类型 - STREAMING 实时流 - INDEX 索引 - APPLICATION 应用 - TENANT_BUCKET 租户桶 - LAKE 数据湖  **约束限制** 不涉及 **取值范围**: - STREAMING - INDEX - APPLICATION - TENANT_BUCKET - LAKE  **默认值** 不涉及                        

        :param category: The category of this ListTablesRequest.
        :type category: str
        """
        self._category = category

    @property
    def table_id(self):
        r"""Gets the table_id of this ListTablesRequest.

        表id

        :return: The table_id of this ListTablesRequest.
        :rtype: str
        """
        return self._table_id

    @table_id.setter
    def table_id(self, table_id):
        r"""Sets the table_id of this ListTablesRequest.

        表id

        :param table_id: The table_id of this ListTablesRequest.
        :type table_id: str
        """
        self._table_id = table_id

    @property
    def table_alias(self):
        r"""Gets the table_alias of this ListTablesRequest.

        表别名

        :return: The table_alias of this ListTablesRequest.
        :rtype: str
        """
        return self._table_alias

    @table_alias.setter
    def table_alias(self, table_alias):
        r"""Sets the table_alias of this ListTablesRequest.

        表别名

        :param table_alias: The table_alias of this ListTablesRequest.
        :type table_alias: str
        """
        self._table_alias = table_alias

    @property
    def table_name(self):
        r"""Gets the table_name of this ListTablesRequest.

        表名称

        :return: The table_name of this ListTablesRequest.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        r"""Sets the table_name of this ListTablesRequest.

        表名称

        :param table_name: The table_name of this ListTablesRequest.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def offset(self):
        r"""Gets the offset of this ListTablesRequest.

        **参数解释：** 偏移量 **取值范围：** 0-1000000 **默认取值：** 0

        :return: The offset of this ListTablesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListTablesRequest.

        **参数解释：** 偏移量 **取值范围：** 0-1000000 **默认取值：** 0

        :param offset: The offset of this ListTablesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListTablesRequest.

        **参数解释：** 查询数据限制 **取值范围：** 0-1000 **默认取值：** 不涉及

        :return: The limit of this ListTablesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListTablesRequest.

        **参数解释：** 查询数据限制 **取值范围：** 0-1000 **默认取值：** 不涉及

        :param limit: The limit of this ListTablesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def sort_key(self):
        r"""Gets the sort_key of this ListTablesRequest.

        按照属性排序。

        :return: The sort_key of this ListTablesRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this ListTablesRequest.

        按照属性排序。

        :param sort_key: The sort_key of this ListTablesRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ListTablesRequest.

        排序顺序，支持 `ASC` 或 `DESC`。

        :return: The sort_dir of this ListTablesRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ListTablesRequest.

        排序顺序，支持 `ASC` 或 `DESC`。

        :param sort_dir: The sort_dir of this ListTablesRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

    @property
    def exists(self):
        r"""Gets the exists of this ListTablesRequest.

        是否存在

        :return: The exists of this ListTablesRequest.
        :rtype: bool
        """
        return self._exists

    @exists.setter
    def exists(self, exists):
        r"""Sets the exists of this ListTablesRequest.

        是否存在

        :param exists: The exists of this ListTablesRequest.
        :type exists: bool
        """
        self._exists = exists

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
        if not isinstance(other, ListTablesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
