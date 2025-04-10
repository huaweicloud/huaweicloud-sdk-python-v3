# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WorkspaceVO:

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
        'is_physical': 'bool',
        'frequent': 'bool',
        'top': 'bool',
        'level': 'ModelLevel',
        'dw_type': 'str',
        'create_time': 'datetime',
        'update_time': 'datetime',
        'create_by': 'str',
        'update_by': 'str',
        'type': 'str',
        'biz_catalog_ids': 'str',
        'databases': 'list[str]',
        'table_model_prefix': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'is_physical': 'is_physical',
        'frequent': 'frequent',
        'top': 'top',
        'level': 'level',
        'dw_type': 'dw_type',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'create_by': 'create_by',
        'update_by': 'update_by',
        'type': 'type',
        'biz_catalog_ids': 'biz_catalog_ids',
        'databases': 'databases',
        'table_model_prefix': 'table_model_prefix'
    }

    def __init__(self, id=None, name=None, description=None, is_physical=None, frequent=None, top=None, level=None, dw_type=None, create_time=None, update_time=None, create_by=None, update_by=None, type=None, biz_catalog_ids=None, databases=None, table_model_prefix=None):
        r"""WorkspaceVO

        The model defined in huaweicloud sdk

        :param id: 编号，ID字符串。
        :type id: str
        :param name: 工作区名字。
        :type name: str
        :param description: 描述。
        :type description: str
        :param is_physical: 是否为物理表。
        :type is_physical: bool
        :param frequent: 是否为常用。
        :type frequent: bool
        :param top: 分层治理。
        :type top: bool
        :param level: 
        :type level: :class:`huaweicloudsdkdataartsstudio.v1.ModelLevel`
        :param dw_type: 数据连接类型，对应表所在的数仓类型，取值可以为DLI、DWS、MRS_HIVE、POSTGRESQL、MRS_SPARK、CLICKHOUSE、MYSQL、ORACLE和DORIS等。
        :type dw_type: str
        :param create_time: 创建时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。
        :type create_time: datetime
        :param update_time: 更新时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。
        :type update_time: datetime
        :param create_by: 创建人。
        :type create_by: str
        :param update_by: 更新人。
        :type update_by: str
        :param type: 工作区类型枚举。 枚举值：   - THIRD_NF: 关系建模   - DIMENSION: 维度建模 
        :type type: str
        :param biz_catalog_ids: 关联的业务分层的ID列表 {\&quot;l1Ids\&quot;:[],\&quot;l2Ids\&quot;:[],\&quot;l3Ids\&quot;:[]}。
        :type biz_catalog_ids: str
        :param databases: 数据库名称数组。
        :type databases: list[str]
        :param table_model_prefix: 模型校验前缀，长度不超过100，数字字母下划线组成，字母开头
        :type table_model_prefix: str
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._is_physical = None
        self._frequent = None
        self._top = None
        self._level = None
        self._dw_type = None
        self._create_time = None
        self._update_time = None
        self._create_by = None
        self._update_by = None
        self._type = None
        self._biz_catalog_ids = None
        self._databases = None
        self._table_model_prefix = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        if description is not None:
            self.description = description
        if is_physical is not None:
            self.is_physical = is_physical
        if frequent is not None:
            self.frequent = frequent
        if top is not None:
            self.top = top
        if level is not None:
            self.level = level
        if dw_type is not None:
            self.dw_type = dw_type
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if create_by is not None:
            self.create_by = create_by
        if update_by is not None:
            self.update_by = update_by
        self.type = type
        if biz_catalog_ids is not None:
            self.biz_catalog_ids = biz_catalog_ids
        if databases is not None:
            self.databases = databases
        if table_model_prefix is not None:
            self.table_model_prefix = table_model_prefix

    @property
    def id(self):
        r"""Gets the id of this WorkspaceVO.

        编号，ID字符串。

        :return: The id of this WorkspaceVO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this WorkspaceVO.

        编号，ID字符串。

        :param id: The id of this WorkspaceVO.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this WorkspaceVO.

        工作区名字。

        :return: The name of this WorkspaceVO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this WorkspaceVO.

        工作区名字。

        :param name: The name of this WorkspaceVO.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this WorkspaceVO.

        描述。

        :return: The description of this WorkspaceVO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this WorkspaceVO.

        描述。

        :param description: The description of this WorkspaceVO.
        :type description: str
        """
        self._description = description

    @property
    def is_physical(self):
        r"""Gets the is_physical of this WorkspaceVO.

        是否为物理表。

        :return: The is_physical of this WorkspaceVO.
        :rtype: bool
        """
        return self._is_physical

    @is_physical.setter
    def is_physical(self, is_physical):
        r"""Sets the is_physical of this WorkspaceVO.

        是否为物理表。

        :param is_physical: The is_physical of this WorkspaceVO.
        :type is_physical: bool
        """
        self._is_physical = is_physical

    @property
    def frequent(self):
        r"""Gets the frequent of this WorkspaceVO.

        是否为常用。

        :return: The frequent of this WorkspaceVO.
        :rtype: bool
        """
        return self._frequent

    @frequent.setter
    def frequent(self, frequent):
        r"""Sets the frequent of this WorkspaceVO.

        是否为常用。

        :param frequent: The frequent of this WorkspaceVO.
        :type frequent: bool
        """
        self._frequent = frequent

    @property
    def top(self):
        r"""Gets the top of this WorkspaceVO.

        分层治理。

        :return: The top of this WorkspaceVO.
        :rtype: bool
        """
        return self._top

    @top.setter
    def top(self, top):
        r"""Sets the top of this WorkspaceVO.

        分层治理。

        :param top: The top of this WorkspaceVO.
        :type top: bool
        """
        self._top = top

    @property
    def level(self):
        r"""Gets the level of this WorkspaceVO.

        :return: The level of this WorkspaceVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ModelLevel`
        """
        return self._level

    @level.setter
    def level(self, level):
        r"""Sets the level of this WorkspaceVO.

        :param level: The level of this WorkspaceVO.
        :type level: :class:`huaweicloudsdkdataartsstudio.v1.ModelLevel`
        """
        self._level = level

    @property
    def dw_type(self):
        r"""Gets the dw_type of this WorkspaceVO.

        数据连接类型，对应表所在的数仓类型，取值可以为DLI、DWS、MRS_HIVE、POSTGRESQL、MRS_SPARK、CLICKHOUSE、MYSQL、ORACLE和DORIS等。

        :return: The dw_type of this WorkspaceVO.
        :rtype: str
        """
        return self._dw_type

    @dw_type.setter
    def dw_type(self, dw_type):
        r"""Sets the dw_type of this WorkspaceVO.

        数据连接类型，对应表所在的数仓类型，取值可以为DLI、DWS、MRS_HIVE、POSTGRESQL、MRS_SPARK、CLICKHOUSE、MYSQL、ORACLE和DORIS等。

        :param dw_type: The dw_type of this WorkspaceVO.
        :type dw_type: str
        """
        self._dw_type = dw_type

    @property
    def create_time(self):
        r"""Gets the create_time of this WorkspaceVO.

        创建时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :return: The create_time of this WorkspaceVO.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this WorkspaceVO.

        创建时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :param create_time: The create_time of this WorkspaceVO.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this WorkspaceVO.

        更新时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :return: The update_time of this WorkspaceVO.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this WorkspaceVO.

        更新时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :param update_time: The update_time of this WorkspaceVO.
        :type update_time: datetime
        """
        self._update_time = update_time

    @property
    def create_by(self):
        r"""Gets the create_by of this WorkspaceVO.

        创建人。

        :return: The create_by of this WorkspaceVO.
        :rtype: str
        """
        return self._create_by

    @create_by.setter
    def create_by(self, create_by):
        r"""Sets the create_by of this WorkspaceVO.

        创建人。

        :param create_by: The create_by of this WorkspaceVO.
        :type create_by: str
        """
        self._create_by = create_by

    @property
    def update_by(self):
        r"""Gets the update_by of this WorkspaceVO.

        更新人。

        :return: The update_by of this WorkspaceVO.
        :rtype: str
        """
        return self._update_by

    @update_by.setter
    def update_by(self, update_by):
        r"""Sets the update_by of this WorkspaceVO.

        更新人。

        :param update_by: The update_by of this WorkspaceVO.
        :type update_by: str
        """
        self._update_by = update_by

    @property
    def type(self):
        r"""Gets the type of this WorkspaceVO.

        工作区类型枚举。 枚举值：   - THIRD_NF: 关系建模   - DIMENSION: 维度建模 

        :return: The type of this WorkspaceVO.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this WorkspaceVO.

        工作区类型枚举。 枚举值：   - THIRD_NF: 关系建模   - DIMENSION: 维度建模 

        :param type: The type of this WorkspaceVO.
        :type type: str
        """
        self._type = type

    @property
    def biz_catalog_ids(self):
        r"""Gets the biz_catalog_ids of this WorkspaceVO.

        关联的业务分层的ID列表 {\"l1Ids\":[],\"l2Ids\":[],\"l3Ids\":[]}。

        :return: The biz_catalog_ids of this WorkspaceVO.
        :rtype: str
        """
        return self._biz_catalog_ids

    @biz_catalog_ids.setter
    def biz_catalog_ids(self, biz_catalog_ids):
        r"""Sets the biz_catalog_ids of this WorkspaceVO.

        关联的业务分层的ID列表 {\"l1Ids\":[],\"l2Ids\":[],\"l3Ids\":[]}。

        :param biz_catalog_ids: The biz_catalog_ids of this WorkspaceVO.
        :type biz_catalog_ids: str
        """
        self._biz_catalog_ids = biz_catalog_ids

    @property
    def databases(self):
        r"""Gets the databases of this WorkspaceVO.

        数据库名称数组。

        :return: The databases of this WorkspaceVO.
        :rtype: list[str]
        """
        return self._databases

    @databases.setter
    def databases(self, databases):
        r"""Sets the databases of this WorkspaceVO.

        数据库名称数组。

        :param databases: The databases of this WorkspaceVO.
        :type databases: list[str]
        """
        self._databases = databases

    @property
    def table_model_prefix(self):
        r"""Gets the table_model_prefix of this WorkspaceVO.

        模型校验前缀，长度不超过100，数字字母下划线组成，字母开头

        :return: The table_model_prefix of this WorkspaceVO.
        :rtype: str
        """
        return self._table_model_prefix

    @table_model_prefix.setter
    def table_model_prefix(self, table_model_prefix):
        r"""Sets the table_model_prefix of this WorkspaceVO.

        模型校验前缀，长度不超过100，数字字母下划线组成，字母开头

        :param table_model_prefix: The table_model_prefix of this WorkspaceVO.
        :type table_model_prefix: str
        """
        self._table_model_prefix = table_model_prefix

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, WorkspaceVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
