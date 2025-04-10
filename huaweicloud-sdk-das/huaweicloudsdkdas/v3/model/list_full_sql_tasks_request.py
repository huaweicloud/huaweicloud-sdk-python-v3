# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFullSqlTasksRequest:

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
        'page': 'int',
        'limit': 'int',
        'x_language': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
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
        'page': 'page',
        'limit': 'limit',
        'x_language': 'X-Language'
    }

    def __init__(self, instance_id=None, range_left=None, range_right=None, create_at_left=None, create_at_right=None, user=None, keyword=None, db_name=None, operation=None, thread_id=None, trx_id=None, status=None, sql_template_id=None, sort_field=None, asc=None, page=None, limit=None, x_language=None):
        r"""ListFullSqlTasksRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID。
        :type instance_id: str
        :param range_left: 最小任务起止时间（Unix timestamp），单位：毫秒。
        :type range_left: int
        :param range_right: 最大任务起止时间（Unix timestamp），单位：毫秒。
        :type range_right: int
        :param create_at_left: 最小任务创建时间（Unix timestamp），单位：毫秒。
        :type create_at_left: int
        :param create_at_right: 最大任务创建时间（Unix timestamp），单位：毫秒。
        :type create_at_right: int
        :param user: 用户名。
        :type user: str
        :param keyword: 关键字。
        :type keyword: str
        :param db_name: 数据库名。
        :type db_name: str
        :param operation: 操作类型。
        :type operation: str
        :param thread_id: 线程ID。
        :type thread_id: str
        :param trx_id: 事务ID。
        :type trx_id: str
        :param status: 执行状态（0:成功，1:失败）。
        :type status: str
        :param sql_template_id: SQL模板ID。
        :type sql_template_id: str
        :param sort_field: 排序字段（create_at:任务创建时间, range_start_at,range_end_at:任务起止时间）。
        :type sort_field: str
        :param asc: 排序顺序（true:正序, false:逆序）。
        :type asc: bool
        :param page: 页码。
        :type page: int
        :param limit: 每页记录数。最大为100。
        :type limit: int
        :param x_language: 请求语言类型。
        :type x_language: str
        """
        
        

        self._instance_id = None
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
        self._page = None
        self._limit = None
        self._x_language = None
        self.discriminator = None

        self.instance_id = instance_id
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
        if page is not None:
            self.page = page
        if limit is not None:
            self.limit = limit
        if x_language is not None:
            self.x_language = x_language

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListFullSqlTasksRequest.

        实例ID。

        :return: The instance_id of this ListFullSqlTasksRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListFullSqlTasksRequest.

        实例ID。

        :param instance_id: The instance_id of this ListFullSqlTasksRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def range_left(self):
        r"""Gets the range_left of this ListFullSqlTasksRequest.

        最小任务起止时间（Unix timestamp），单位：毫秒。

        :return: The range_left of this ListFullSqlTasksRequest.
        :rtype: int
        """
        return self._range_left

    @range_left.setter
    def range_left(self, range_left):
        r"""Sets the range_left of this ListFullSqlTasksRequest.

        最小任务起止时间（Unix timestamp），单位：毫秒。

        :param range_left: The range_left of this ListFullSqlTasksRequest.
        :type range_left: int
        """
        self._range_left = range_left

    @property
    def range_right(self):
        r"""Gets the range_right of this ListFullSqlTasksRequest.

        最大任务起止时间（Unix timestamp），单位：毫秒。

        :return: The range_right of this ListFullSqlTasksRequest.
        :rtype: int
        """
        return self._range_right

    @range_right.setter
    def range_right(self, range_right):
        r"""Sets the range_right of this ListFullSqlTasksRequest.

        最大任务起止时间（Unix timestamp），单位：毫秒。

        :param range_right: The range_right of this ListFullSqlTasksRequest.
        :type range_right: int
        """
        self._range_right = range_right

    @property
    def create_at_left(self):
        r"""Gets the create_at_left of this ListFullSqlTasksRequest.

        最小任务创建时间（Unix timestamp），单位：毫秒。

        :return: The create_at_left of this ListFullSqlTasksRequest.
        :rtype: int
        """
        return self._create_at_left

    @create_at_left.setter
    def create_at_left(self, create_at_left):
        r"""Sets the create_at_left of this ListFullSqlTasksRequest.

        最小任务创建时间（Unix timestamp），单位：毫秒。

        :param create_at_left: The create_at_left of this ListFullSqlTasksRequest.
        :type create_at_left: int
        """
        self._create_at_left = create_at_left

    @property
    def create_at_right(self):
        r"""Gets the create_at_right of this ListFullSqlTasksRequest.

        最大任务创建时间（Unix timestamp），单位：毫秒。

        :return: The create_at_right of this ListFullSqlTasksRequest.
        :rtype: int
        """
        return self._create_at_right

    @create_at_right.setter
    def create_at_right(self, create_at_right):
        r"""Sets the create_at_right of this ListFullSqlTasksRequest.

        最大任务创建时间（Unix timestamp），单位：毫秒。

        :param create_at_right: The create_at_right of this ListFullSqlTasksRequest.
        :type create_at_right: int
        """
        self._create_at_right = create_at_right

    @property
    def user(self):
        r"""Gets the user of this ListFullSqlTasksRequest.

        用户名。

        :return: The user of this ListFullSqlTasksRequest.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        r"""Sets the user of this ListFullSqlTasksRequest.

        用户名。

        :param user: The user of this ListFullSqlTasksRequest.
        :type user: str
        """
        self._user = user

    @property
    def keyword(self):
        r"""Gets the keyword of this ListFullSqlTasksRequest.

        关键字。

        :return: The keyword of this ListFullSqlTasksRequest.
        :rtype: str
        """
        return self._keyword

    @keyword.setter
    def keyword(self, keyword):
        r"""Sets the keyword of this ListFullSqlTasksRequest.

        关键字。

        :param keyword: The keyword of this ListFullSqlTasksRequest.
        :type keyword: str
        """
        self._keyword = keyword

    @property
    def db_name(self):
        r"""Gets the db_name of this ListFullSqlTasksRequest.

        数据库名。

        :return: The db_name of this ListFullSqlTasksRequest.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        r"""Sets the db_name of this ListFullSqlTasksRequest.

        数据库名。

        :param db_name: The db_name of this ListFullSqlTasksRequest.
        :type db_name: str
        """
        self._db_name = db_name

    @property
    def operation(self):
        r"""Gets the operation of this ListFullSqlTasksRequest.

        操作类型。

        :return: The operation of this ListFullSqlTasksRequest.
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        r"""Sets the operation of this ListFullSqlTasksRequest.

        操作类型。

        :param operation: The operation of this ListFullSqlTasksRequest.
        :type operation: str
        """
        self._operation = operation

    @property
    def thread_id(self):
        r"""Gets the thread_id of this ListFullSqlTasksRequest.

        线程ID。

        :return: The thread_id of this ListFullSqlTasksRequest.
        :rtype: str
        """
        return self._thread_id

    @thread_id.setter
    def thread_id(self, thread_id):
        r"""Sets the thread_id of this ListFullSqlTasksRequest.

        线程ID。

        :param thread_id: The thread_id of this ListFullSqlTasksRequest.
        :type thread_id: str
        """
        self._thread_id = thread_id

    @property
    def trx_id(self):
        r"""Gets the trx_id of this ListFullSqlTasksRequest.

        事务ID。

        :return: The trx_id of this ListFullSqlTasksRequest.
        :rtype: str
        """
        return self._trx_id

    @trx_id.setter
    def trx_id(self, trx_id):
        r"""Sets the trx_id of this ListFullSqlTasksRequest.

        事务ID。

        :param trx_id: The trx_id of this ListFullSqlTasksRequest.
        :type trx_id: str
        """
        self._trx_id = trx_id

    @property
    def status(self):
        r"""Gets the status of this ListFullSqlTasksRequest.

        执行状态（0:成功，1:失败）。

        :return: The status of this ListFullSqlTasksRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListFullSqlTasksRequest.

        执行状态（0:成功，1:失败）。

        :param status: The status of this ListFullSqlTasksRequest.
        :type status: str
        """
        self._status = status

    @property
    def sql_template_id(self):
        r"""Gets the sql_template_id of this ListFullSqlTasksRequest.

        SQL模板ID。

        :return: The sql_template_id of this ListFullSqlTasksRequest.
        :rtype: str
        """
        return self._sql_template_id

    @sql_template_id.setter
    def sql_template_id(self, sql_template_id):
        r"""Sets the sql_template_id of this ListFullSqlTasksRequest.

        SQL模板ID。

        :param sql_template_id: The sql_template_id of this ListFullSqlTasksRequest.
        :type sql_template_id: str
        """
        self._sql_template_id = sql_template_id

    @property
    def sort_field(self):
        r"""Gets the sort_field of this ListFullSqlTasksRequest.

        排序字段（create_at:任务创建时间, range_start_at,range_end_at:任务起止时间）。

        :return: The sort_field of this ListFullSqlTasksRequest.
        :rtype: str
        """
        return self._sort_field

    @sort_field.setter
    def sort_field(self, sort_field):
        r"""Sets the sort_field of this ListFullSqlTasksRequest.

        排序字段（create_at:任务创建时间, range_start_at,range_end_at:任务起止时间）。

        :param sort_field: The sort_field of this ListFullSqlTasksRequest.
        :type sort_field: str
        """
        self._sort_field = sort_field

    @property
    def asc(self):
        r"""Gets the asc of this ListFullSqlTasksRequest.

        排序顺序（true:正序, false:逆序）。

        :return: The asc of this ListFullSqlTasksRequest.
        :rtype: bool
        """
        return self._asc

    @asc.setter
    def asc(self, asc):
        r"""Sets the asc of this ListFullSqlTasksRequest.

        排序顺序（true:正序, false:逆序）。

        :param asc: The asc of this ListFullSqlTasksRequest.
        :type asc: bool
        """
        self._asc = asc

    @property
    def page(self):
        r"""Gets the page of this ListFullSqlTasksRequest.

        页码。

        :return: The page of this ListFullSqlTasksRequest.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        r"""Sets the page of this ListFullSqlTasksRequest.

        页码。

        :param page: The page of this ListFullSqlTasksRequest.
        :type page: int
        """
        self._page = page

    @property
    def limit(self):
        r"""Gets the limit of this ListFullSqlTasksRequest.

        每页记录数。最大为100。

        :return: The limit of this ListFullSqlTasksRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListFullSqlTasksRequest.

        每页记录数。最大为100。

        :param limit: The limit of this ListFullSqlTasksRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def x_language(self):
        r"""Gets the x_language of this ListFullSqlTasksRequest.

        请求语言类型。

        :return: The x_language of this ListFullSqlTasksRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ListFullSqlTasksRequest.

        请求语言类型。

        :param x_language: The x_language of this ListFullSqlTasksRequest.
        :type x_language: str
        """
        self._x_language = x_language

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
        if not isinstance(other, ListFullSqlTasksRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
