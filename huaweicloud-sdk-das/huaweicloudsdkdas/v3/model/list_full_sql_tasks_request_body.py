# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFullSqlTasksRequestBody:

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
        'node_id': 'str',
        'range_left': 'int',
        'range_right': 'int',
        'create_at_left': 'int',
        'create_at_right': 'int',
        'user': 'str',
        'keyword': 'str',
        'db_name': 'str',
        'operation': 'str',
        'thread_id': 'str',
        'trx_id': 'str',
        'status': 'str',
        'sql_template_id': 'str',
        'sort_field': 'str',
        'asc': 'bool',
        'page_size': 'int',
        'cur_page': 'int'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'node_id': 'node_id',
        'range_left': 'range_left',
        'range_right': 'range_right',
        'create_at_left': 'create_at_left',
        'create_at_right': 'create_at_right',
        'user': 'user',
        'keyword': 'keyword',
        'db_name': 'db_name',
        'operation': 'operation',
        'thread_id': 'thread_id',
        'trx_id': 'trx_id',
        'status': 'status',
        'sql_template_id': 'sql_template_id',
        'sort_field': 'sort_field',
        'asc': 'asc',
        'page_size': 'page_size',
        'cur_page': 'cur_page'
    }

    def __init__(self, instance_id=None, node_id=None, range_left=None, range_right=None, create_at_left=None, create_at_right=None, user=None, keyword=None, db_name=None, operation=None, thread_id=None, trx_id=None, status=None, sql_template_id=None, sort_field=None, asc=None, page_size=None, cur_page=None):
        r"""ListFullSqlTasksRequestBody

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param node_id: 节点ID
        :type node_id: str
        :param range_left: 起止时间的查询左区间
        :type range_left: int
        :param range_right: 起止时间的查询右区间
        :type range_right: int
        :param create_at_left: 创建时间的查询左区间
        :type create_at_left: int
        :param create_at_right: 创建时间的查询右区间
        :type create_at_right: int
        :param user: 用户名
        :type user: str
        :param keyword: 关键字
        :type keyword: str
        :param db_name: 数据库
        :type db_name: str
        :param operation: 操作
        :type operation: str
        :param thread_id: 线程ID
        :type thread_id: str
        :param trx_id: 事务ID
        :type trx_id: str
        :param status: 执行状态（0：成功，1：失败）
        :type status: str
        :param sql_template_id: SQL模板ID
        :type sql_template_id: str
        :param sort_field: 排序字段（create_at, range_start_at, range_end_at）
        :type sort_field: str
        :param asc: 排序规则（true：升序，false：降序）
        :type asc: bool
        :param page_size: 每页记录数
        :type page_size: int
        :param cur_page: 当前页码
        :type cur_page: int
        """
        
        

        self._instance_id = None
        self._node_id = None
        self._range_left = None
        self._range_right = None
        self._create_at_left = None
        self._create_at_right = None
        self._user = None
        self._keyword = None
        self._db_name = None
        self._operation = None
        self._thread_id = None
        self._trx_id = None
        self._status = None
        self._sql_template_id = None
        self._sort_field = None
        self._asc = None
        self._page_size = None
        self._cur_page = None
        self.discriminator = None

        self.instance_id = instance_id
        if node_id is not None:
            self.node_id = node_id
        if range_left is not None:
            self.range_left = range_left
        if range_right is not None:
            self.range_right = range_right
        if create_at_left is not None:
            self.create_at_left = create_at_left
        if create_at_right is not None:
            self.create_at_right = create_at_right
        if user is not None:
            self.user = user
        if keyword is not None:
            self.keyword = keyword
        if db_name is not None:
            self.db_name = db_name
        if operation is not None:
            self.operation = operation
        if thread_id is not None:
            self.thread_id = thread_id
        if trx_id is not None:
            self.trx_id = trx_id
        if status is not None:
            self.status = status
        if sql_template_id is not None:
            self.sql_template_id = sql_template_id
        if sort_field is not None:
            self.sort_field = sort_field
        if asc is not None:
            self.asc = asc
        if page_size is not None:
            self.page_size = page_size
        if cur_page is not None:
            self.cur_page = cur_page

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListFullSqlTasksRequestBody.

        实例ID

        :return: The instance_id of this ListFullSqlTasksRequestBody.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListFullSqlTasksRequestBody.

        实例ID

        :param instance_id: The instance_id of this ListFullSqlTasksRequestBody.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def node_id(self):
        r"""Gets the node_id of this ListFullSqlTasksRequestBody.

        节点ID

        :return: The node_id of this ListFullSqlTasksRequestBody.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this ListFullSqlTasksRequestBody.

        节点ID

        :param node_id: The node_id of this ListFullSqlTasksRequestBody.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def range_left(self):
        r"""Gets the range_left of this ListFullSqlTasksRequestBody.

        起止时间的查询左区间

        :return: The range_left of this ListFullSqlTasksRequestBody.
        :rtype: int
        """
        return self._range_left

    @range_left.setter
    def range_left(self, range_left):
        r"""Sets the range_left of this ListFullSqlTasksRequestBody.

        起止时间的查询左区间

        :param range_left: The range_left of this ListFullSqlTasksRequestBody.
        :type range_left: int
        """
        self._range_left = range_left

    @property
    def range_right(self):
        r"""Gets the range_right of this ListFullSqlTasksRequestBody.

        起止时间的查询右区间

        :return: The range_right of this ListFullSqlTasksRequestBody.
        :rtype: int
        """
        return self._range_right

    @range_right.setter
    def range_right(self, range_right):
        r"""Sets the range_right of this ListFullSqlTasksRequestBody.

        起止时间的查询右区间

        :param range_right: The range_right of this ListFullSqlTasksRequestBody.
        :type range_right: int
        """
        self._range_right = range_right

    @property
    def create_at_left(self):
        r"""Gets the create_at_left of this ListFullSqlTasksRequestBody.

        创建时间的查询左区间

        :return: The create_at_left of this ListFullSqlTasksRequestBody.
        :rtype: int
        """
        return self._create_at_left

    @create_at_left.setter
    def create_at_left(self, create_at_left):
        r"""Sets the create_at_left of this ListFullSqlTasksRequestBody.

        创建时间的查询左区间

        :param create_at_left: The create_at_left of this ListFullSqlTasksRequestBody.
        :type create_at_left: int
        """
        self._create_at_left = create_at_left

    @property
    def create_at_right(self):
        r"""Gets the create_at_right of this ListFullSqlTasksRequestBody.

        创建时间的查询右区间

        :return: The create_at_right of this ListFullSqlTasksRequestBody.
        :rtype: int
        """
        return self._create_at_right

    @create_at_right.setter
    def create_at_right(self, create_at_right):
        r"""Sets the create_at_right of this ListFullSqlTasksRequestBody.

        创建时间的查询右区间

        :param create_at_right: The create_at_right of this ListFullSqlTasksRequestBody.
        :type create_at_right: int
        """
        self._create_at_right = create_at_right

    @property
    def user(self):
        r"""Gets the user of this ListFullSqlTasksRequestBody.

        用户名

        :return: The user of this ListFullSqlTasksRequestBody.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        r"""Sets the user of this ListFullSqlTasksRequestBody.

        用户名

        :param user: The user of this ListFullSqlTasksRequestBody.
        :type user: str
        """
        self._user = user

    @property
    def keyword(self):
        r"""Gets the keyword of this ListFullSqlTasksRequestBody.

        关键字

        :return: The keyword of this ListFullSqlTasksRequestBody.
        :rtype: str
        """
        return self._keyword

    @keyword.setter
    def keyword(self, keyword):
        r"""Sets the keyword of this ListFullSqlTasksRequestBody.

        关键字

        :param keyword: The keyword of this ListFullSqlTasksRequestBody.
        :type keyword: str
        """
        self._keyword = keyword

    @property
    def db_name(self):
        r"""Gets the db_name of this ListFullSqlTasksRequestBody.

        数据库

        :return: The db_name of this ListFullSqlTasksRequestBody.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        r"""Sets the db_name of this ListFullSqlTasksRequestBody.

        数据库

        :param db_name: The db_name of this ListFullSqlTasksRequestBody.
        :type db_name: str
        """
        self._db_name = db_name

    @property
    def operation(self):
        r"""Gets the operation of this ListFullSqlTasksRequestBody.

        操作

        :return: The operation of this ListFullSqlTasksRequestBody.
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        r"""Sets the operation of this ListFullSqlTasksRequestBody.

        操作

        :param operation: The operation of this ListFullSqlTasksRequestBody.
        :type operation: str
        """
        self._operation = operation

    @property
    def thread_id(self):
        r"""Gets the thread_id of this ListFullSqlTasksRequestBody.

        线程ID

        :return: The thread_id of this ListFullSqlTasksRequestBody.
        :rtype: str
        """
        return self._thread_id

    @thread_id.setter
    def thread_id(self, thread_id):
        r"""Sets the thread_id of this ListFullSqlTasksRequestBody.

        线程ID

        :param thread_id: The thread_id of this ListFullSqlTasksRequestBody.
        :type thread_id: str
        """
        self._thread_id = thread_id

    @property
    def trx_id(self):
        r"""Gets the trx_id of this ListFullSqlTasksRequestBody.

        事务ID

        :return: The trx_id of this ListFullSqlTasksRequestBody.
        :rtype: str
        """
        return self._trx_id

    @trx_id.setter
    def trx_id(self, trx_id):
        r"""Sets the trx_id of this ListFullSqlTasksRequestBody.

        事务ID

        :param trx_id: The trx_id of this ListFullSqlTasksRequestBody.
        :type trx_id: str
        """
        self._trx_id = trx_id

    @property
    def status(self):
        r"""Gets the status of this ListFullSqlTasksRequestBody.

        执行状态（0：成功，1：失败）

        :return: The status of this ListFullSqlTasksRequestBody.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListFullSqlTasksRequestBody.

        执行状态（0：成功，1：失败）

        :param status: The status of this ListFullSqlTasksRequestBody.
        :type status: str
        """
        self._status = status

    @property
    def sql_template_id(self):
        r"""Gets the sql_template_id of this ListFullSqlTasksRequestBody.

        SQL模板ID

        :return: The sql_template_id of this ListFullSqlTasksRequestBody.
        :rtype: str
        """
        return self._sql_template_id

    @sql_template_id.setter
    def sql_template_id(self, sql_template_id):
        r"""Sets the sql_template_id of this ListFullSqlTasksRequestBody.

        SQL模板ID

        :param sql_template_id: The sql_template_id of this ListFullSqlTasksRequestBody.
        :type sql_template_id: str
        """
        self._sql_template_id = sql_template_id

    @property
    def sort_field(self):
        r"""Gets the sort_field of this ListFullSqlTasksRequestBody.

        排序字段（create_at, range_start_at, range_end_at）

        :return: The sort_field of this ListFullSqlTasksRequestBody.
        :rtype: str
        """
        return self._sort_field

    @sort_field.setter
    def sort_field(self, sort_field):
        r"""Sets the sort_field of this ListFullSqlTasksRequestBody.

        排序字段（create_at, range_start_at, range_end_at）

        :param sort_field: The sort_field of this ListFullSqlTasksRequestBody.
        :type sort_field: str
        """
        self._sort_field = sort_field

    @property
    def asc(self):
        r"""Gets the asc of this ListFullSqlTasksRequestBody.

        排序规则（true：升序，false：降序）

        :return: The asc of this ListFullSqlTasksRequestBody.
        :rtype: bool
        """
        return self._asc

    @asc.setter
    def asc(self, asc):
        r"""Sets the asc of this ListFullSqlTasksRequestBody.

        排序规则（true：升序，false：降序）

        :param asc: The asc of this ListFullSqlTasksRequestBody.
        :type asc: bool
        """
        self._asc = asc

    @property
    def page_size(self):
        r"""Gets the page_size of this ListFullSqlTasksRequestBody.

        每页记录数

        :return: The page_size of this ListFullSqlTasksRequestBody.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        r"""Sets the page_size of this ListFullSqlTasksRequestBody.

        每页记录数

        :param page_size: The page_size of this ListFullSqlTasksRequestBody.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def cur_page(self):
        r"""Gets the cur_page of this ListFullSqlTasksRequestBody.

        当前页码

        :return: The cur_page of this ListFullSqlTasksRequestBody.
        :rtype: int
        """
        return self._cur_page

    @cur_page.setter
    def cur_page(self, cur_page):
        r"""Sets the cur_page of this ListFullSqlTasksRequestBody.

        当前页码

        :param cur_page: The cur_page of this ListFullSqlTasksRequestBody.
        :type cur_page: int
        """
        self._cur_page = cur_page

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
        if not isinstance(other, ListFullSqlTasksRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
