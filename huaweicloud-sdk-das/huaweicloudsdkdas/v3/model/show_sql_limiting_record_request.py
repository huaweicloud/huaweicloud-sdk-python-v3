# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSqlLimitingRecordRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'engine_type': 'str',
        'node_id': 'str',
        'sql_type': 'str',
        'db_name': 'str',
        'query_id': 'str',
        'cur_page': 'str',
        'per_page': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'engine_type': 'engine_type',
        'node_id': 'node_id',
        'sql_type': 'sql_type',
        'db_name': 'db_name',
        'query_id': 'query_id',
        'cur_page': 'cur_page',
        'per_page': 'per_page'
    }

    def __init__(self, instance_id=None, engine_type=None, node_id=None, sql_type=None, db_name=None, query_id=None, cur_page=None, per_page=None):
        r"""ShowSqlLimitingRecordRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param engine_type: 数据库引擎类型
        :type engine_type: str
        :param node_id: 节点ID
        :type node_id: str
        :param sql_type: SQL类型
        :type sql_type: str
        :param db_name: 数据库名称
        :type db_name: str
        :param query_id: 查询ID
        :type query_id: str
        :param cur_page: 页码
        :type cur_page: str
        :param per_page: 每页记录数
        :type per_page: str
        """
        
        

        self._instance_id = None
        self._engine_type = None
        self._node_id = None
        self._sql_type = None
        self._db_name = None
        self._query_id = None
        self._cur_page = None
        self._per_page = None
        self.discriminator = None

        self.instance_id = instance_id
        self.engine_type = engine_type
        if node_id is not None:
            self.node_id = node_id
        if sql_type is not None:
            self.sql_type = sql_type
        if db_name is not None:
            self.db_name = db_name
        if query_id is not None:
            self.query_id = query_id
        if cur_page is not None:
            self.cur_page = cur_page
        if per_page is not None:
            self.per_page = per_page

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ShowSqlLimitingRecordRequest.

        实例ID

        :return: The instance_id of this ShowSqlLimitingRecordRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ShowSqlLimitingRecordRequest.

        实例ID

        :param instance_id: The instance_id of this ShowSqlLimitingRecordRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def engine_type(self):
        r"""Gets the engine_type of this ShowSqlLimitingRecordRequest.

        数据库引擎类型

        :return: The engine_type of this ShowSqlLimitingRecordRequest.
        :rtype: str
        """
        return self._engine_type

    @engine_type.setter
    def engine_type(self, engine_type):
        r"""Sets the engine_type of this ShowSqlLimitingRecordRequest.

        数据库引擎类型

        :param engine_type: The engine_type of this ShowSqlLimitingRecordRequest.
        :type engine_type: str
        """
        self._engine_type = engine_type

    @property
    def node_id(self):
        r"""Gets the node_id of this ShowSqlLimitingRecordRequest.

        节点ID

        :return: The node_id of this ShowSqlLimitingRecordRequest.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this ShowSqlLimitingRecordRequest.

        节点ID

        :param node_id: The node_id of this ShowSqlLimitingRecordRequest.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def sql_type(self):
        r"""Gets the sql_type of this ShowSqlLimitingRecordRequest.

        SQL类型

        :return: The sql_type of this ShowSqlLimitingRecordRequest.
        :rtype: str
        """
        return self._sql_type

    @sql_type.setter
    def sql_type(self, sql_type):
        r"""Sets the sql_type of this ShowSqlLimitingRecordRequest.

        SQL类型

        :param sql_type: The sql_type of this ShowSqlLimitingRecordRequest.
        :type sql_type: str
        """
        self._sql_type = sql_type

    @property
    def db_name(self):
        r"""Gets the db_name of this ShowSqlLimitingRecordRequest.

        数据库名称

        :return: The db_name of this ShowSqlLimitingRecordRequest.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        r"""Sets the db_name of this ShowSqlLimitingRecordRequest.

        数据库名称

        :param db_name: The db_name of this ShowSqlLimitingRecordRequest.
        :type db_name: str
        """
        self._db_name = db_name

    @property
    def query_id(self):
        r"""Gets the query_id of this ShowSqlLimitingRecordRequest.

        查询ID

        :return: The query_id of this ShowSqlLimitingRecordRequest.
        :rtype: str
        """
        return self._query_id

    @query_id.setter
    def query_id(self, query_id):
        r"""Sets the query_id of this ShowSqlLimitingRecordRequest.

        查询ID

        :param query_id: The query_id of this ShowSqlLimitingRecordRequest.
        :type query_id: str
        """
        self._query_id = query_id

    @property
    def cur_page(self):
        r"""Gets the cur_page of this ShowSqlLimitingRecordRequest.

        页码

        :return: The cur_page of this ShowSqlLimitingRecordRequest.
        :rtype: str
        """
        return self._cur_page

    @cur_page.setter
    def cur_page(self, cur_page):
        r"""Sets the cur_page of this ShowSqlLimitingRecordRequest.

        页码

        :param cur_page: The cur_page of this ShowSqlLimitingRecordRequest.
        :type cur_page: str
        """
        self._cur_page = cur_page

    @property
    def per_page(self):
        r"""Gets the per_page of this ShowSqlLimitingRecordRequest.

        每页记录数

        :return: The per_page of this ShowSqlLimitingRecordRequest.
        :rtype: str
        """
        return self._per_page

    @per_page.setter
    def per_page(self, per_page):
        r"""Sets the per_page of this ShowSqlLimitingRecordRequest.

        每页记录数

        :param per_page: The per_page of this ShowSqlLimitingRecordRequest.
        :type per_page: str
        """
        self._per_page = per_page

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
        if not isinstance(other, ShowSqlLimitingRecordRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
