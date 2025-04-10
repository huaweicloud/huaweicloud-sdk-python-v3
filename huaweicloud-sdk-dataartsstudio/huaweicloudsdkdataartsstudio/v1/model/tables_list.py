# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TablesList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'table_name': 'str',
        'table_id': 'str',
        'table_name_cn': 'str',
        'columns': 'str',
        'dw_id': 'str',
        'dw_name': 'str',
        'dw_type': 'str',
        'database_name': 'str',
        'schema_name': 'str',
        'life_cycle': 'int',
        'description': 'str',
        'user_id': 'str',
        'user_name': 'str',
        'project_id': 'str',
        'create_time': 'str',
        'table_size': 'int',
        'total_count': 'int',
        'is_valid': 'int',
        'extra_setting': 'str',
        'partitioned': 'bool'
    }

    attribute_map = {
        'table_name': 'table_name',
        'table_id': 'table_id',
        'table_name_cn': 'table_name_cn',
        'columns': 'columns',
        'dw_id': 'dw_id',
        'dw_name': 'dw_name',
        'dw_type': 'dw_type',
        'database_name': 'database_name',
        'schema_name': 'schema_name',
        'life_cycle': 'life_cycle',
        'description': 'description',
        'user_id': 'user_id',
        'user_name': 'user_name',
        'project_id': 'project_id',
        'create_time': 'create_time',
        'table_size': 'table_size',
        'total_count': 'total_count',
        'is_valid': 'is_valid',
        'extra_setting': 'extra_setting',
        'partitioned': 'partitioned'
    }

    def __init__(self, table_name=None, table_id=None, table_name_cn=None, columns=None, dw_id=None, dw_name=None, dw_type=None, database_name=None, schema_name=None, life_cycle=None, description=None, user_id=None, user_name=None, project_id=None, create_time=None, table_size=None, total_count=None, is_valid=None, extra_setting=None, partitioned=None):
        r"""TablesList

        The model defined in huaweicloud sdk

        :param table_name: 表名称
        :type table_name: str
        :param table_id: 表id
        :type table_id: str
        :param table_name_cn: 表的中文名称
        :type table_name_cn: str
        :param columns: 表中字段
        :type columns: str
        :param dw_id: 数据连接id
        :type dw_id: str
        :param dw_name: 数据连接名称
        :type dw_name: str
        :param dw_type: 数据连接类型
        :type dw_type: str
        :param database_name: 数据库名称
        :type database_name: str
        :param schema_name: schema名称
        :type schema_name: str
        :param life_cycle: 表的生命周期
        :type life_cycle: int
        :param description: 表的描述
        :type description: str
        :param user_id: 用户id
        :type user_id: str
        :param user_name: 用户名称
        :type user_name: str
        :param project_id: 数据连接id
        :type project_id: str
        :param create_time: 表的创建时间
        :type create_time: str
        :param table_size: 表的大小
        :type table_size: int
        :param total_count: 当前查询条件下表的总记录数
        :type total_count: int
        :param is_valid: 表是否合规
        :type is_valid: int
        :param extra_setting: 表的额外设置
        :type extra_setting: str
        :param partitioned: 是否进行数据分区
        :type partitioned: bool
        """
        
        

        self._table_name = None
        self._table_id = None
        self._table_name_cn = None
        self._columns = None
        self._dw_id = None
        self._dw_name = None
        self._dw_type = None
        self._database_name = None
        self._schema_name = None
        self._life_cycle = None
        self._description = None
        self._user_id = None
        self._user_name = None
        self._project_id = None
        self._create_time = None
        self._table_size = None
        self._total_count = None
        self._is_valid = None
        self._extra_setting = None
        self._partitioned = None
        self.discriminator = None

        if table_name is not None:
            self.table_name = table_name
        if table_id is not None:
            self.table_id = table_id
        if table_name_cn is not None:
            self.table_name_cn = table_name_cn
        if columns is not None:
            self.columns = columns
        if dw_id is not None:
            self.dw_id = dw_id
        if dw_name is not None:
            self.dw_name = dw_name
        if dw_type is not None:
            self.dw_type = dw_type
        if database_name is not None:
            self.database_name = database_name
        if schema_name is not None:
            self.schema_name = schema_name
        if life_cycle is not None:
            self.life_cycle = life_cycle
        if description is not None:
            self.description = description
        if user_id is not None:
            self.user_id = user_id
        if user_name is not None:
            self.user_name = user_name
        if project_id is not None:
            self.project_id = project_id
        if create_time is not None:
            self.create_time = create_time
        if table_size is not None:
            self.table_size = table_size
        if total_count is not None:
            self.total_count = total_count
        if is_valid is not None:
            self.is_valid = is_valid
        if extra_setting is not None:
            self.extra_setting = extra_setting
        if partitioned is not None:
            self.partitioned = partitioned

    @property
    def table_name(self):
        r"""Gets the table_name of this TablesList.

        表名称

        :return: The table_name of this TablesList.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        r"""Sets the table_name of this TablesList.

        表名称

        :param table_name: The table_name of this TablesList.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def table_id(self):
        r"""Gets the table_id of this TablesList.

        表id

        :return: The table_id of this TablesList.
        :rtype: str
        """
        return self._table_id

    @table_id.setter
    def table_id(self, table_id):
        r"""Sets the table_id of this TablesList.

        表id

        :param table_id: The table_id of this TablesList.
        :type table_id: str
        """
        self._table_id = table_id

    @property
    def table_name_cn(self):
        r"""Gets the table_name_cn of this TablesList.

        表的中文名称

        :return: The table_name_cn of this TablesList.
        :rtype: str
        """
        return self._table_name_cn

    @table_name_cn.setter
    def table_name_cn(self, table_name_cn):
        r"""Sets the table_name_cn of this TablesList.

        表的中文名称

        :param table_name_cn: The table_name_cn of this TablesList.
        :type table_name_cn: str
        """
        self._table_name_cn = table_name_cn

    @property
    def columns(self):
        r"""Gets the columns of this TablesList.

        表中字段

        :return: The columns of this TablesList.
        :rtype: str
        """
        return self._columns

    @columns.setter
    def columns(self, columns):
        r"""Sets the columns of this TablesList.

        表中字段

        :param columns: The columns of this TablesList.
        :type columns: str
        """
        self._columns = columns

    @property
    def dw_id(self):
        r"""Gets the dw_id of this TablesList.

        数据连接id

        :return: The dw_id of this TablesList.
        :rtype: str
        """
        return self._dw_id

    @dw_id.setter
    def dw_id(self, dw_id):
        r"""Sets the dw_id of this TablesList.

        数据连接id

        :param dw_id: The dw_id of this TablesList.
        :type dw_id: str
        """
        self._dw_id = dw_id

    @property
    def dw_name(self):
        r"""Gets the dw_name of this TablesList.

        数据连接名称

        :return: The dw_name of this TablesList.
        :rtype: str
        """
        return self._dw_name

    @dw_name.setter
    def dw_name(self, dw_name):
        r"""Sets the dw_name of this TablesList.

        数据连接名称

        :param dw_name: The dw_name of this TablesList.
        :type dw_name: str
        """
        self._dw_name = dw_name

    @property
    def dw_type(self):
        r"""Gets the dw_type of this TablesList.

        数据连接类型

        :return: The dw_type of this TablesList.
        :rtype: str
        """
        return self._dw_type

    @dw_type.setter
    def dw_type(self, dw_type):
        r"""Sets the dw_type of this TablesList.

        数据连接类型

        :param dw_type: The dw_type of this TablesList.
        :type dw_type: str
        """
        self._dw_type = dw_type

    @property
    def database_name(self):
        r"""Gets the database_name of this TablesList.

        数据库名称

        :return: The database_name of this TablesList.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        r"""Sets the database_name of this TablesList.

        数据库名称

        :param database_name: The database_name of this TablesList.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def schema_name(self):
        r"""Gets the schema_name of this TablesList.

        schema名称

        :return: The schema_name of this TablesList.
        :rtype: str
        """
        return self._schema_name

    @schema_name.setter
    def schema_name(self, schema_name):
        r"""Sets the schema_name of this TablesList.

        schema名称

        :param schema_name: The schema_name of this TablesList.
        :type schema_name: str
        """
        self._schema_name = schema_name

    @property
    def life_cycle(self):
        r"""Gets the life_cycle of this TablesList.

        表的生命周期

        :return: The life_cycle of this TablesList.
        :rtype: int
        """
        return self._life_cycle

    @life_cycle.setter
    def life_cycle(self, life_cycle):
        r"""Sets the life_cycle of this TablesList.

        表的生命周期

        :param life_cycle: The life_cycle of this TablesList.
        :type life_cycle: int
        """
        self._life_cycle = life_cycle

    @property
    def description(self):
        r"""Gets the description of this TablesList.

        表的描述

        :return: The description of this TablesList.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this TablesList.

        表的描述

        :param description: The description of this TablesList.
        :type description: str
        """
        self._description = description

    @property
    def user_id(self):
        r"""Gets the user_id of this TablesList.

        用户id

        :return: The user_id of this TablesList.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this TablesList.

        用户id

        :param user_id: The user_id of this TablesList.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def user_name(self):
        r"""Gets the user_name of this TablesList.

        用户名称

        :return: The user_name of this TablesList.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this TablesList.

        用户名称

        :param user_name: The user_name of this TablesList.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def project_id(self):
        r"""Gets the project_id of this TablesList.

        数据连接id

        :return: The project_id of this TablesList.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this TablesList.

        数据连接id

        :param project_id: The project_id of this TablesList.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def create_time(self):
        r"""Gets the create_time of this TablesList.

        表的创建时间

        :return: The create_time of this TablesList.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this TablesList.

        表的创建时间

        :param create_time: The create_time of this TablesList.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def table_size(self):
        r"""Gets the table_size of this TablesList.

        表的大小

        :return: The table_size of this TablesList.
        :rtype: int
        """
        return self._table_size

    @table_size.setter
    def table_size(self, table_size):
        r"""Sets the table_size of this TablesList.

        表的大小

        :param table_size: The table_size of this TablesList.
        :type table_size: int
        """
        self._table_size = table_size

    @property
    def total_count(self):
        r"""Gets the total_count of this TablesList.

        当前查询条件下表的总记录数

        :return: The total_count of this TablesList.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this TablesList.

        当前查询条件下表的总记录数

        :param total_count: The total_count of this TablesList.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def is_valid(self):
        r"""Gets the is_valid of this TablesList.

        表是否合规

        :return: The is_valid of this TablesList.
        :rtype: int
        """
        return self._is_valid

    @is_valid.setter
    def is_valid(self, is_valid):
        r"""Sets the is_valid of this TablesList.

        表是否合规

        :param is_valid: The is_valid of this TablesList.
        :type is_valid: int
        """
        self._is_valid = is_valid

    @property
    def extra_setting(self):
        r"""Gets the extra_setting of this TablesList.

        表的额外设置

        :return: The extra_setting of this TablesList.
        :rtype: str
        """
        return self._extra_setting

    @extra_setting.setter
    def extra_setting(self, extra_setting):
        r"""Sets the extra_setting of this TablesList.

        表的额外设置

        :param extra_setting: The extra_setting of this TablesList.
        :type extra_setting: str
        """
        self._extra_setting = extra_setting

    @property
    def partitioned(self):
        r"""Gets the partitioned of this TablesList.

        是否进行数据分区

        :return: The partitioned of this TablesList.
        :rtype: bool
        """
        return self._partitioned

    @partitioned.setter
    def partitioned(self, partitioned):
        r"""Sets the partitioned of this TablesList.

        是否进行数据分区

        :param partitioned: The partitioned of this TablesList.
        :type partitioned: bool
        """
        self._partitioned = partitioned

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
        if not isinstance(other, TablesList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
