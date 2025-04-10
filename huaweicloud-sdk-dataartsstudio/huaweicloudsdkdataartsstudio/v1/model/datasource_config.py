# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DatasourceConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'connection_name': 'str',
        'connection_id': 'str',
        'database': 'str',
        'datatable': 'str',
        'table_id': 'str',
        'queue': 'str',
        'access_type': 'str',
        'access_mode': 'str',
        'pagination': 'str',
        'sql': 'str',
        'backend_paras': 'list[ApiRequestPara]',
        'response_paras': 'list[ApiResponsePara]',
        'order_paras': 'list[DatasourceOrderPara]',
        'total_size_sql': 'str'
    }

    attribute_map = {
        'type': 'type',
        'connection_name': 'connection_name',
        'connection_id': 'connection_id',
        'database': 'database',
        'datatable': 'datatable',
        'table_id': 'table_id',
        'queue': 'queue',
        'access_type': 'access_type',
        'access_mode': 'access_mode',
        'pagination': 'pagination',
        'sql': 'sql',
        'backend_paras': 'backend_paras',
        'response_paras': 'response_paras',
        'order_paras': 'order_paras',
        'total_size_sql': 'total_size_sql'
    }

    def __init__(self, type=None, connection_name=None, connection_id=None, database=None, datatable=None, table_id=None, queue=None, access_type=None, access_mode=None, pagination=None, sql=None, backend_paras=None, response_paras=None, order_paras=None, total_size_sql=None):
        r"""DatasourceConfig

        The model defined in huaweicloud sdk

        :param type: 数据源的类型
        :type type: str
        :param connection_name: 数据连接名称
        :type connection_name: str
        :param connection_id: 数据连接ID
        :type connection_id: str
        :param database: 数据库名
        :type database: str
        :param datatable: 数据表名称
        :type datatable: str
        :param table_id: 数据表ID
        :type table_id: str
        :param queue: DLI的队列名称
        :type queue: str
        :param access_type: 取数方式
        :type access_type: str
        :param access_mode: 获取数据的模式
        :type access_mode: str
        :param pagination: 
        :type pagination: str
        :param sql: 脚本模式下的sql语句
        :type sql: str
        :param backend_paras: API后端参数
        :type backend_paras: list[:class:`huaweicloudsdkdataartsstudio.v1.ApiRequestPara`]
        :param response_paras: 配置类API返回参数
        :type response_paras: list[:class:`huaweicloudsdkdataartsstudio.v1.ApiResponsePara`]
        :param order_paras: 排序参数
        :type order_paras: list[:class:`huaweicloudsdkdataartsstudio.v1.DatasourceOrderPara`]
        :param total_size_sql: 总条数计算脚本SQL。
        :type total_size_sql: str
        """
        
        

        self._type = None
        self._connection_name = None
        self._connection_id = None
        self._database = None
        self._datatable = None
        self._table_id = None
        self._queue = None
        self._access_type = None
        self._access_mode = None
        self._pagination = None
        self._sql = None
        self._backend_paras = None
        self._response_paras = None
        self._order_paras = None
        self._total_size_sql = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if connection_name is not None:
            self.connection_name = connection_name
        if connection_id is not None:
            self.connection_id = connection_id
        if database is not None:
            self.database = database
        if datatable is not None:
            self.datatable = datatable
        if table_id is not None:
            self.table_id = table_id
        if queue is not None:
            self.queue = queue
        if access_type is not None:
            self.access_type = access_type
        if access_mode is not None:
            self.access_mode = access_mode
        if pagination is not None:
            self.pagination = pagination
        if sql is not None:
            self.sql = sql
        if backend_paras is not None:
            self.backend_paras = backend_paras
        if response_paras is not None:
            self.response_paras = response_paras
        if order_paras is not None:
            self.order_paras = order_paras
        if total_size_sql is not None:
            self.total_size_sql = total_size_sql

    @property
    def type(self):
        r"""Gets the type of this DatasourceConfig.

        数据源的类型

        :return: The type of this DatasourceConfig.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this DatasourceConfig.

        数据源的类型

        :param type: The type of this DatasourceConfig.
        :type type: str
        """
        self._type = type

    @property
    def connection_name(self):
        r"""Gets the connection_name of this DatasourceConfig.

        数据连接名称

        :return: The connection_name of this DatasourceConfig.
        :rtype: str
        """
        return self._connection_name

    @connection_name.setter
    def connection_name(self, connection_name):
        r"""Sets the connection_name of this DatasourceConfig.

        数据连接名称

        :param connection_name: The connection_name of this DatasourceConfig.
        :type connection_name: str
        """
        self._connection_name = connection_name

    @property
    def connection_id(self):
        r"""Gets the connection_id of this DatasourceConfig.

        数据连接ID

        :return: The connection_id of this DatasourceConfig.
        :rtype: str
        """
        return self._connection_id

    @connection_id.setter
    def connection_id(self, connection_id):
        r"""Sets the connection_id of this DatasourceConfig.

        数据连接ID

        :param connection_id: The connection_id of this DatasourceConfig.
        :type connection_id: str
        """
        self._connection_id = connection_id

    @property
    def database(self):
        r"""Gets the database of this DatasourceConfig.

        数据库名

        :return: The database of this DatasourceConfig.
        :rtype: str
        """
        return self._database

    @database.setter
    def database(self, database):
        r"""Sets the database of this DatasourceConfig.

        数据库名

        :param database: The database of this DatasourceConfig.
        :type database: str
        """
        self._database = database

    @property
    def datatable(self):
        r"""Gets the datatable of this DatasourceConfig.

        数据表名称

        :return: The datatable of this DatasourceConfig.
        :rtype: str
        """
        return self._datatable

    @datatable.setter
    def datatable(self, datatable):
        r"""Sets the datatable of this DatasourceConfig.

        数据表名称

        :param datatable: The datatable of this DatasourceConfig.
        :type datatable: str
        """
        self._datatable = datatable

    @property
    def table_id(self):
        r"""Gets the table_id of this DatasourceConfig.

        数据表ID

        :return: The table_id of this DatasourceConfig.
        :rtype: str
        """
        return self._table_id

    @table_id.setter
    def table_id(self, table_id):
        r"""Sets the table_id of this DatasourceConfig.

        数据表ID

        :param table_id: The table_id of this DatasourceConfig.
        :type table_id: str
        """
        self._table_id = table_id

    @property
    def queue(self):
        r"""Gets the queue of this DatasourceConfig.

        DLI的队列名称

        :return: The queue of this DatasourceConfig.
        :rtype: str
        """
        return self._queue

    @queue.setter
    def queue(self, queue):
        r"""Sets the queue of this DatasourceConfig.

        DLI的队列名称

        :param queue: The queue of this DatasourceConfig.
        :type queue: str
        """
        self._queue = queue

    @property
    def access_type(self):
        r"""Gets the access_type of this DatasourceConfig.

        取数方式

        :return: The access_type of this DatasourceConfig.
        :rtype: str
        """
        return self._access_type

    @access_type.setter
    def access_type(self, access_type):
        r"""Sets the access_type of this DatasourceConfig.

        取数方式

        :param access_type: The access_type of this DatasourceConfig.
        :type access_type: str
        """
        self._access_type = access_type

    @property
    def access_mode(self):
        r"""Gets the access_mode of this DatasourceConfig.

        获取数据的模式

        :return: The access_mode of this DatasourceConfig.
        :rtype: str
        """
        return self._access_mode

    @access_mode.setter
    def access_mode(self, access_mode):
        r"""Sets the access_mode of this DatasourceConfig.

        获取数据的模式

        :param access_mode: The access_mode of this DatasourceConfig.
        :type access_mode: str
        """
        self._access_mode = access_mode

    @property
    def pagination(self):
        r"""Gets the pagination of this DatasourceConfig.

        :return: The pagination of this DatasourceConfig.
        :rtype: str
        """
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        r"""Sets the pagination of this DatasourceConfig.

        :param pagination: The pagination of this DatasourceConfig.
        :type pagination: str
        """
        self._pagination = pagination

    @property
    def sql(self):
        r"""Gets the sql of this DatasourceConfig.

        脚本模式下的sql语句

        :return: The sql of this DatasourceConfig.
        :rtype: str
        """
        return self._sql

    @sql.setter
    def sql(self, sql):
        r"""Sets the sql of this DatasourceConfig.

        脚本模式下的sql语句

        :param sql: The sql of this DatasourceConfig.
        :type sql: str
        """
        self._sql = sql

    @property
    def backend_paras(self):
        r"""Gets the backend_paras of this DatasourceConfig.

        API后端参数

        :return: The backend_paras of this DatasourceConfig.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.ApiRequestPara`]
        """
        return self._backend_paras

    @backend_paras.setter
    def backend_paras(self, backend_paras):
        r"""Sets the backend_paras of this DatasourceConfig.

        API后端参数

        :param backend_paras: The backend_paras of this DatasourceConfig.
        :type backend_paras: list[:class:`huaweicloudsdkdataartsstudio.v1.ApiRequestPara`]
        """
        self._backend_paras = backend_paras

    @property
    def response_paras(self):
        r"""Gets the response_paras of this DatasourceConfig.

        配置类API返回参数

        :return: The response_paras of this DatasourceConfig.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.ApiResponsePara`]
        """
        return self._response_paras

    @response_paras.setter
    def response_paras(self, response_paras):
        r"""Sets the response_paras of this DatasourceConfig.

        配置类API返回参数

        :param response_paras: The response_paras of this DatasourceConfig.
        :type response_paras: list[:class:`huaweicloudsdkdataartsstudio.v1.ApiResponsePara`]
        """
        self._response_paras = response_paras

    @property
    def order_paras(self):
        r"""Gets the order_paras of this DatasourceConfig.

        排序参数

        :return: The order_paras of this DatasourceConfig.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.DatasourceOrderPara`]
        """
        return self._order_paras

    @order_paras.setter
    def order_paras(self, order_paras):
        r"""Sets the order_paras of this DatasourceConfig.

        排序参数

        :param order_paras: The order_paras of this DatasourceConfig.
        :type order_paras: list[:class:`huaweicloudsdkdataartsstudio.v1.DatasourceOrderPara`]
        """
        self._order_paras = order_paras

    @property
    def total_size_sql(self):
        r"""Gets the total_size_sql of this DatasourceConfig.

        总条数计算脚本SQL。

        :return: The total_size_sql of this DatasourceConfig.
        :rtype: str
        """
        return self._total_size_sql

    @total_size_sql.setter
    def total_size_sql(self, total_size_sql):
        r"""Sets the total_size_sql of this DatasourceConfig.

        总条数计算脚本SQL。

        :param total_size_sql: The total_size_sql of this DatasourceConfig.
        :type total_size_sql: str
        """
        self._total_size_sql = total_size_sql

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
        if not isinstance(other, DatasourceConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
