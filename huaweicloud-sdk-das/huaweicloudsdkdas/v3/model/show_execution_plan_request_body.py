# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowExecutionPlanRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'database_name': 'str',
        'schema_name': 'str',
        'sql_script': 'str',
        'node_id': 'str',
        'node_type': 'str',
        'use_default_search_path': 'bool',
        'ignore_limit': 'bool',
        'perpage': 'int',
        'curpage': 'int'
    }

    attribute_map = {
        'database_name': 'database_name',
        'schema_name': 'schema_name',
        'sql_script': 'sql_script',
        'node_id': 'node_id',
        'node_type': 'node_type',
        'use_default_search_path': 'use_default_search_path',
        'ignore_limit': 'ignore_limit',
        'perpage': 'perpage',
        'curpage': 'curpage'
    }

    def __init__(self, database_name=None, schema_name=None, sql_script=None, node_id=None, node_type=None, use_default_search_path=None, ignore_limit=None, perpage=None, curpage=None):
        r"""ShowExecutionPlanRequestBody

        The model defined in huaweicloud sdk

        :param database_name: 数据库名称
        :type database_name: str
        :param schema_name: schema名称
        :type schema_name: str
        :param sql_script: SQL脚本
        :type sql_script: str
        :param node_id: 实例节点ID，实例节点的唯一标识
        :type node_id: str
        :param node_type: 节点类型（master：主节点，slave：副节点，readreplica：只读节点）
        :type node_type: str
        :param use_default_search_path: PostgreSQL是否使用默认searchPath（仅在实例是PostgreSQL时可用）
        :type use_default_search_path: bool
        :param ignore_limit: 是否忽略限制
        :type ignore_limit: bool
        :param perpage: 每页记录数，取值范围：[0, 100]
        :type perpage: int
        :param curpage: 页码，取值范围：[0, 2^31-1]
        :type curpage: int
        """
        
        

        self._database_name = None
        self._schema_name = None
        self._sql_script = None
        self._node_id = None
        self._node_type = None
        self._use_default_search_path = None
        self._ignore_limit = None
        self._perpage = None
        self._curpage = None
        self.discriminator = None

        self.database_name = database_name
        if schema_name is not None:
            self.schema_name = schema_name
        self.sql_script = sql_script
        if node_id is not None:
            self.node_id = node_id
        if node_type is not None:
            self.node_type = node_type
        if use_default_search_path is not None:
            self.use_default_search_path = use_default_search_path
        if ignore_limit is not None:
            self.ignore_limit = ignore_limit
        self.perpage = perpage
        self.curpage = curpage

    @property
    def database_name(self):
        r"""Gets the database_name of this ShowExecutionPlanRequestBody.

        数据库名称

        :return: The database_name of this ShowExecutionPlanRequestBody.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        r"""Sets the database_name of this ShowExecutionPlanRequestBody.

        数据库名称

        :param database_name: The database_name of this ShowExecutionPlanRequestBody.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def schema_name(self):
        r"""Gets the schema_name of this ShowExecutionPlanRequestBody.

        schema名称

        :return: The schema_name of this ShowExecutionPlanRequestBody.
        :rtype: str
        """
        return self._schema_name

    @schema_name.setter
    def schema_name(self, schema_name):
        r"""Sets the schema_name of this ShowExecutionPlanRequestBody.

        schema名称

        :param schema_name: The schema_name of this ShowExecutionPlanRequestBody.
        :type schema_name: str
        """
        self._schema_name = schema_name

    @property
    def sql_script(self):
        r"""Gets the sql_script of this ShowExecutionPlanRequestBody.

        SQL脚本

        :return: The sql_script of this ShowExecutionPlanRequestBody.
        :rtype: str
        """
        return self._sql_script

    @sql_script.setter
    def sql_script(self, sql_script):
        r"""Sets the sql_script of this ShowExecutionPlanRequestBody.

        SQL脚本

        :param sql_script: The sql_script of this ShowExecutionPlanRequestBody.
        :type sql_script: str
        """
        self._sql_script = sql_script

    @property
    def node_id(self):
        r"""Gets the node_id of this ShowExecutionPlanRequestBody.

        实例节点ID，实例节点的唯一标识

        :return: The node_id of this ShowExecutionPlanRequestBody.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this ShowExecutionPlanRequestBody.

        实例节点ID，实例节点的唯一标识

        :param node_id: The node_id of this ShowExecutionPlanRequestBody.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def node_type(self):
        r"""Gets the node_type of this ShowExecutionPlanRequestBody.

        节点类型（master：主节点，slave：副节点，readreplica：只读节点）

        :return: The node_type of this ShowExecutionPlanRequestBody.
        :rtype: str
        """
        return self._node_type

    @node_type.setter
    def node_type(self, node_type):
        r"""Sets the node_type of this ShowExecutionPlanRequestBody.

        节点类型（master：主节点，slave：副节点，readreplica：只读节点）

        :param node_type: The node_type of this ShowExecutionPlanRequestBody.
        :type node_type: str
        """
        self._node_type = node_type

    @property
    def use_default_search_path(self):
        r"""Gets the use_default_search_path of this ShowExecutionPlanRequestBody.

        PostgreSQL是否使用默认searchPath（仅在实例是PostgreSQL时可用）

        :return: The use_default_search_path of this ShowExecutionPlanRequestBody.
        :rtype: bool
        """
        return self._use_default_search_path

    @use_default_search_path.setter
    def use_default_search_path(self, use_default_search_path):
        r"""Sets the use_default_search_path of this ShowExecutionPlanRequestBody.

        PostgreSQL是否使用默认searchPath（仅在实例是PostgreSQL时可用）

        :param use_default_search_path: The use_default_search_path of this ShowExecutionPlanRequestBody.
        :type use_default_search_path: bool
        """
        self._use_default_search_path = use_default_search_path

    @property
    def ignore_limit(self):
        r"""Gets the ignore_limit of this ShowExecutionPlanRequestBody.

        是否忽略限制

        :return: The ignore_limit of this ShowExecutionPlanRequestBody.
        :rtype: bool
        """
        return self._ignore_limit

    @ignore_limit.setter
    def ignore_limit(self, ignore_limit):
        r"""Sets the ignore_limit of this ShowExecutionPlanRequestBody.

        是否忽略限制

        :param ignore_limit: The ignore_limit of this ShowExecutionPlanRequestBody.
        :type ignore_limit: bool
        """
        self._ignore_limit = ignore_limit

    @property
    def perpage(self):
        r"""Gets the perpage of this ShowExecutionPlanRequestBody.

        每页记录数，取值范围：[0, 100]

        :return: The perpage of this ShowExecutionPlanRequestBody.
        :rtype: int
        """
        return self._perpage

    @perpage.setter
    def perpage(self, perpage):
        r"""Sets the perpage of this ShowExecutionPlanRequestBody.

        每页记录数，取值范围：[0, 100]

        :param perpage: The perpage of this ShowExecutionPlanRequestBody.
        :type perpage: int
        """
        self._perpage = perpage

    @property
    def curpage(self):
        r"""Gets the curpage of this ShowExecutionPlanRequestBody.

        页码，取值范围：[0, 2^31-1]

        :return: The curpage of this ShowExecutionPlanRequestBody.
        :rtype: int
        """
        return self._curpage

    @curpage.setter
    def curpage(self, curpage):
        r"""Sets the curpage of this ShowExecutionPlanRequestBody.

        页码，取值范围：[0, 2^31-1]

        :param curpage: The curpage of this ShowExecutionPlanRequestBody.
        :type curpage: int
        """
        self._curpage = curpage

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
        if not isinstance(other, ShowExecutionPlanRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
