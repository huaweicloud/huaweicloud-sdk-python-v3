# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDatabaseObjectsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'connection_id': 'str',
        'db_name': 'str',
        'db_id': 'str',
        'schema_name': 'str',
        'table_name': 'str',
        'table_id': 'str',
        'start_at': 'int',
        'end_at': 'int',
        'page_num': 'int',
        'page_size': 'int',
        'order_by': 'str',
        'order': 'str',
        'extra_order_by': 'str',
        'extra_order': 'str',
        'obj_type': 'str',
        'ret_type': 'str',
        'is_sys': 'str',
        'obj_sub_type': 'str',
        'node_type': 'str',
        'node_id': 'str',
        'obj_name': 'str',
        'keywords': 'str',
        'cur_page': 'str',
        'per_page': 'str'
    }

    attribute_map = {
        'connection_id': 'connection_id',
        'db_name': 'db_name',
        'db_id': 'db_id',
        'schema_name': 'schema_name',
        'table_name': 'table_name',
        'table_id': 'table_id',
        'start_at': 'start_at',
        'end_at': 'end_at',
        'page_num': 'page_num',
        'page_size': 'page_size',
        'order_by': 'order_by',
        'order': 'order',
        'extra_order_by': 'extra_order_by',
        'extra_order': 'extra_order',
        'obj_type': 'obj_type',
        'ret_type': 'ret_type',
        'is_sys': 'is_sys',
        'obj_sub_type': 'obj_sub_type',
        'node_type': 'node_type',
        'node_id': 'node_id',
        'obj_name': 'obj_name',
        'keywords': 'keywords',
        'cur_page': 'cur_page',
        'per_page': 'per_page'
    }

    def __init__(self, connection_id=None, db_name=None, db_id=None, schema_name=None, table_name=None, table_id=None, start_at=None, end_at=None, page_num=None, page_size=None, order_by=None, order=None, extra_order_by=None, extra_order=None, obj_type=None, ret_type=None, is_sys=None, obj_sub_type=None, node_type=None, node_id=None, obj_name=None, keywords=None, cur_page=None, per_page=None):
        r"""ListDatabaseObjectsRequest

        The model defined in huaweicloud sdk

        :param connection_id: 连接ID
        :type connection_id: str
        :param db_name: 数据库名称
        :type db_name: str
        :param db_id: 数据库ID
        :type db_id: str
        :param schema_name: Schema名称
        :type schema_name: str
        :param table_name: 表名
        :type table_name: str
        :param table_id: 表ID
        :type table_id: str
        :param start_at: 开始时间(Unix timestamp),单位:毫秒
        :type start_at: int
        :param end_at: 结束时间(Unix timestamp),单位:毫秒
        :type end_at: int
        :param page_num: 页码
        :type page_num: int
        :param page_size: 每页记录数
        :type page_size: int
        :param order_by: 排序字段
        :type order_by: str
        :param order: 排序方式（asc/desc）
        :type order: str
        :param extra_order_by: 额外排序字段
        :type extra_order_by: str
        :param extra_order: 额外排序方式
        :type extra_order: str
        :param obj_type: 对象类型
        :type obj_type: str
        :param ret_type: 返回类型
        :type ret_type: str
        :param is_sys: 是否系统对象
        :type is_sys: str
        :param obj_sub_type: 对象子类型
        :type obj_sub_type: str
        :param node_type: 节点类型
        :type node_type: str
        :param node_id: 节点ID
        :type node_id: str
        :param obj_name: 
        :type obj_name: str
        :param keywords: 
        :type keywords: str
        :param cur_page: 
        :type cur_page: str
        :param per_page: 
        :type per_page: str
        """
        
        

        self._connection_id = None
        self._db_name = None
        self._db_id = None
        self._schema_name = None
        self._table_name = None
        self._table_id = None
        self._start_at = None
        self._end_at = None
        self._page_num = None
        self._page_size = None
        self._order_by = None
        self._order = None
        self._extra_order_by = None
        self._extra_order = None
        self._obj_type = None
        self._ret_type = None
        self._is_sys = None
        self._obj_sub_type = None
        self._node_type = None
        self._node_id = None
        self._obj_name = None
        self._keywords = None
        self._cur_page = None
        self._per_page = None
        self.discriminator = None

        self.connection_id = connection_id
        if db_name is not None:
            self.db_name = db_name
        if db_id is not None:
            self.db_id = db_id
        if schema_name is not None:
            self.schema_name = schema_name
        if table_name is not None:
            self.table_name = table_name
        if table_id is not None:
            self.table_id = table_id
        self.start_at = start_at
        self.end_at = end_at
        self.page_num = page_num
        self.page_size = page_size
        if order_by is not None:
            self.order_by = order_by
        if order is not None:
            self.order = order
        if extra_order_by is not None:
            self.extra_order_by = extra_order_by
        if extra_order is not None:
            self.extra_order = extra_order
        if obj_type is not None:
            self.obj_type = obj_type
        if ret_type is not None:
            self.ret_type = ret_type
        if is_sys is not None:
            self.is_sys = is_sys
        if obj_sub_type is not None:
            self.obj_sub_type = obj_sub_type
        if node_type is not None:
            self.node_type = node_type
        if node_id is not None:
            self.node_id = node_id
        if obj_name is not None:
            self.obj_name = obj_name
        if keywords is not None:
            self.keywords = keywords
        if cur_page is not None:
            self.cur_page = cur_page
        if per_page is not None:
            self.per_page = per_page

    @property
    def connection_id(self):
        r"""Gets the connection_id of this ListDatabaseObjectsRequest.

        连接ID

        :return: The connection_id of this ListDatabaseObjectsRequest.
        :rtype: str
        """
        return self._connection_id

    @connection_id.setter
    def connection_id(self, connection_id):
        r"""Sets the connection_id of this ListDatabaseObjectsRequest.

        连接ID

        :param connection_id: The connection_id of this ListDatabaseObjectsRequest.
        :type connection_id: str
        """
        self._connection_id = connection_id

    @property
    def db_name(self):
        r"""Gets the db_name of this ListDatabaseObjectsRequest.

        数据库名称

        :return: The db_name of this ListDatabaseObjectsRequest.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        r"""Sets the db_name of this ListDatabaseObjectsRequest.

        数据库名称

        :param db_name: The db_name of this ListDatabaseObjectsRequest.
        :type db_name: str
        """
        self._db_name = db_name

    @property
    def db_id(self):
        r"""Gets the db_id of this ListDatabaseObjectsRequest.

        数据库ID

        :return: The db_id of this ListDatabaseObjectsRequest.
        :rtype: str
        """
        return self._db_id

    @db_id.setter
    def db_id(self, db_id):
        r"""Sets the db_id of this ListDatabaseObjectsRequest.

        数据库ID

        :param db_id: The db_id of this ListDatabaseObjectsRequest.
        :type db_id: str
        """
        self._db_id = db_id

    @property
    def schema_name(self):
        r"""Gets the schema_name of this ListDatabaseObjectsRequest.

        Schema名称

        :return: The schema_name of this ListDatabaseObjectsRequest.
        :rtype: str
        """
        return self._schema_name

    @schema_name.setter
    def schema_name(self, schema_name):
        r"""Sets the schema_name of this ListDatabaseObjectsRequest.

        Schema名称

        :param schema_name: The schema_name of this ListDatabaseObjectsRequest.
        :type schema_name: str
        """
        self._schema_name = schema_name

    @property
    def table_name(self):
        r"""Gets the table_name of this ListDatabaseObjectsRequest.

        表名

        :return: The table_name of this ListDatabaseObjectsRequest.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        r"""Sets the table_name of this ListDatabaseObjectsRequest.

        表名

        :param table_name: The table_name of this ListDatabaseObjectsRequest.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def table_id(self):
        r"""Gets the table_id of this ListDatabaseObjectsRequest.

        表ID

        :return: The table_id of this ListDatabaseObjectsRequest.
        :rtype: str
        """
        return self._table_id

    @table_id.setter
    def table_id(self, table_id):
        r"""Sets the table_id of this ListDatabaseObjectsRequest.

        表ID

        :param table_id: The table_id of this ListDatabaseObjectsRequest.
        :type table_id: str
        """
        self._table_id = table_id

    @property
    def start_at(self):
        r"""Gets the start_at of this ListDatabaseObjectsRequest.

        开始时间(Unix timestamp),单位:毫秒

        :return: The start_at of this ListDatabaseObjectsRequest.
        :rtype: int
        """
        return self._start_at

    @start_at.setter
    def start_at(self, start_at):
        r"""Sets the start_at of this ListDatabaseObjectsRequest.

        开始时间(Unix timestamp),单位:毫秒

        :param start_at: The start_at of this ListDatabaseObjectsRequest.
        :type start_at: int
        """
        self._start_at = start_at

    @property
    def end_at(self):
        r"""Gets the end_at of this ListDatabaseObjectsRequest.

        结束时间(Unix timestamp),单位:毫秒

        :return: The end_at of this ListDatabaseObjectsRequest.
        :rtype: int
        """
        return self._end_at

    @end_at.setter
    def end_at(self, end_at):
        r"""Sets the end_at of this ListDatabaseObjectsRequest.

        结束时间(Unix timestamp),单位:毫秒

        :param end_at: The end_at of this ListDatabaseObjectsRequest.
        :type end_at: int
        """
        self._end_at = end_at

    @property
    def page_num(self):
        r"""Gets the page_num of this ListDatabaseObjectsRequest.

        页码

        :return: The page_num of this ListDatabaseObjectsRequest.
        :rtype: int
        """
        return self._page_num

    @page_num.setter
    def page_num(self, page_num):
        r"""Sets the page_num of this ListDatabaseObjectsRequest.

        页码

        :param page_num: The page_num of this ListDatabaseObjectsRequest.
        :type page_num: int
        """
        self._page_num = page_num

    @property
    def page_size(self):
        r"""Gets the page_size of this ListDatabaseObjectsRequest.

        每页记录数

        :return: The page_size of this ListDatabaseObjectsRequest.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        r"""Sets the page_size of this ListDatabaseObjectsRequest.

        每页记录数

        :param page_size: The page_size of this ListDatabaseObjectsRequest.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def order_by(self):
        r"""Gets the order_by of this ListDatabaseObjectsRequest.

        排序字段

        :return: The order_by of this ListDatabaseObjectsRequest.
        :rtype: str
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        r"""Sets the order_by of this ListDatabaseObjectsRequest.

        排序字段

        :param order_by: The order_by of this ListDatabaseObjectsRequest.
        :type order_by: str
        """
        self._order_by = order_by

    @property
    def order(self):
        r"""Gets the order of this ListDatabaseObjectsRequest.

        排序方式（asc/desc）

        :return: The order of this ListDatabaseObjectsRequest.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        r"""Sets the order of this ListDatabaseObjectsRequest.

        排序方式（asc/desc）

        :param order: The order of this ListDatabaseObjectsRequest.
        :type order: str
        """
        self._order = order

    @property
    def extra_order_by(self):
        r"""Gets the extra_order_by of this ListDatabaseObjectsRequest.

        额外排序字段

        :return: The extra_order_by of this ListDatabaseObjectsRequest.
        :rtype: str
        """
        return self._extra_order_by

    @extra_order_by.setter
    def extra_order_by(self, extra_order_by):
        r"""Sets the extra_order_by of this ListDatabaseObjectsRequest.

        额外排序字段

        :param extra_order_by: The extra_order_by of this ListDatabaseObjectsRequest.
        :type extra_order_by: str
        """
        self._extra_order_by = extra_order_by

    @property
    def extra_order(self):
        r"""Gets the extra_order of this ListDatabaseObjectsRequest.

        额外排序方式

        :return: The extra_order of this ListDatabaseObjectsRequest.
        :rtype: str
        """
        return self._extra_order

    @extra_order.setter
    def extra_order(self, extra_order):
        r"""Sets the extra_order of this ListDatabaseObjectsRequest.

        额外排序方式

        :param extra_order: The extra_order of this ListDatabaseObjectsRequest.
        :type extra_order: str
        """
        self._extra_order = extra_order

    @property
    def obj_type(self):
        r"""Gets the obj_type of this ListDatabaseObjectsRequest.

        对象类型

        :return: The obj_type of this ListDatabaseObjectsRequest.
        :rtype: str
        """
        return self._obj_type

    @obj_type.setter
    def obj_type(self, obj_type):
        r"""Sets the obj_type of this ListDatabaseObjectsRequest.

        对象类型

        :param obj_type: The obj_type of this ListDatabaseObjectsRequest.
        :type obj_type: str
        """
        self._obj_type = obj_type

    @property
    def ret_type(self):
        r"""Gets the ret_type of this ListDatabaseObjectsRequest.

        返回类型

        :return: The ret_type of this ListDatabaseObjectsRequest.
        :rtype: str
        """
        return self._ret_type

    @ret_type.setter
    def ret_type(self, ret_type):
        r"""Sets the ret_type of this ListDatabaseObjectsRequest.

        返回类型

        :param ret_type: The ret_type of this ListDatabaseObjectsRequest.
        :type ret_type: str
        """
        self._ret_type = ret_type

    @property
    def is_sys(self):
        r"""Gets the is_sys of this ListDatabaseObjectsRequest.

        是否系统对象

        :return: The is_sys of this ListDatabaseObjectsRequest.
        :rtype: str
        """
        return self._is_sys

    @is_sys.setter
    def is_sys(self, is_sys):
        r"""Sets the is_sys of this ListDatabaseObjectsRequest.

        是否系统对象

        :param is_sys: The is_sys of this ListDatabaseObjectsRequest.
        :type is_sys: str
        """
        self._is_sys = is_sys

    @property
    def obj_sub_type(self):
        r"""Gets the obj_sub_type of this ListDatabaseObjectsRequest.

        对象子类型

        :return: The obj_sub_type of this ListDatabaseObjectsRequest.
        :rtype: str
        """
        return self._obj_sub_type

    @obj_sub_type.setter
    def obj_sub_type(self, obj_sub_type):
        r"""Sets the obj_sub_type of this ListDatabaseObjectsRequest.

        对象子类型

        :param obj_sub_type: The obj_sub_type of this ListDatabaseObjectsRequest.
        :type obj_sub_type: str
        """
        self._obj_sub_type = obj_sub_type

    @property
    def node_type(self):
        r"""Gets the node_type of this ListDatabaseObjectsRequest.

        节点类型

        :return: The node_type of this ListDatabaseObjectsRequest.
        :rtype: str
        """
        return self._node_type

    @node_type.setter
    def node_type(self, node_type):
        r"""Sets the node_type of this ListDatabaseObjectsRequest.

        节点类型

        :param node_type: The node_type of this ListDatabaseObjectsRequest.
        :type node_type: str
        """
        self._node_type = node_type

    @property
    def node_id(self):
        r"""Gets the node_id of this ListDatabaseObjectsRequest.

        节点ID

        :return: The node_id of this ListDatabaseObjectsRequest.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this ListDatabaseObjectsRequest.

        节点ID

        :param node_id: The node_id of this ListDatabaseObjectsRequest.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def obj_name(self):
        r"""Gets the obj_name of this ListDatabaseObjectsRequest.

        :return: The obj_name of this ListDatabaseObjectsRequest.
        :rtype: str
        """
        return self._obj_name

    @obj_name.setter
    def obj_name(self, obj_name):
        r"""Sets the obj_name of this ListDatabaseObjectsRequest.

        :param obj_name: The obj_name of this ListDatabaseObjectsRequest.
        :type obj_name: str
        """
        self._obj_name = obj_name

    @property
    def keywords(self):
        r"""Gets the keywords of this ListDatabaseObjectsRequest.

        :return: The keywords of this ListDatabaseObjectsRequest.
        :rtype: str
        """
        return self._keywords

    @keywords.setter
    def keywords(self, keywords):
        r"""Sets the keywords of this ListDatabaseObjectsRequest.

        :param keywords: The keywords of this ListDatabaseObjectsRequest.
        :type keywords: str
        """
        self._keywords = keywords

    @property
    def cur_page(self):
        r"""Gets the cur_page of this ListDatabaseObjectsRequest.

        :return: The cur_page of this ListDatabaseObjectsRequest.
        :rtype: str
        """
        return self._cur_page

    @cur_page.setter
    def cur_page(self, cur_page):
        r"""Sets the cur_page of this ListDatabaseObjectsRequest.

        :param cur_page: The cur_page of this ListDatabaseObjectsRequest.
        :type cur_page: str
        """
        self._cur_page = cur_page

    @property
    def per_page(self):
        r"""Gets the per_page of this ListDatabaseObjectsRequest.

        :return: The per_page of this ListDatabaseObjectsRequest.
        :rtype: str
        """
        return self._per_page

    @per_page.setter
    def per_page(self, per_page):
        r"""Sets the per_page of this ListDatabaseObjectsRequest.

        :param per_page: The per_page of this ListDatabaseObjectsRequest.
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
        if not isinstance(other, ListDatabaseObjectsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
