# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPostgresProcessesRequest:

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
        'user': 'str',
        'host': 'str',
        'db': 'str',
        'state': 'str',
        'command': 'str',
        'keywords': 'str',
        'show_all': 'bool',
        'show_no_pid': 'bool',
        'time': 'str',
        'cur_page': 'str',
        'per_page': 'str',
        'order_by': 'str',
        'order': 'str',
        'node_id': 'str',
        'node_role': 'str',
        'hide_sys': 'bool'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'user': 'user',
        'host': 'host',
        'db': 'db',
        'state': 'state',
        'command': 'command',
        'keywords': 'keywords',
        'show_all': 'show_all',
        'show_no_pid': 'show_no_pid',
        'time': 'time',
        'cur_page': 'cur_page',
        'per_page': 'per_page',
        'order_by': 'order_by',
        'order': 'order',
        'node_id': 'node_id',
        'node_role': 'node_role',
        'hide_sys': 'hide_sys'
    }

    def __init__(self, instance_id=None, user=None, host=None, db=None, state=None, command=None, keywords=None, show_all=None, show_no_pid=None, time=None, cur_page=None, per_page=None, order_by=None, order=None, node_id=None, node_role=None, hide_sys=None):
        r"""ListPostgresProcessesRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param user: 用户名
        :type user: str
        :param host: 访问来源IP
        :type host: str
        :param db: 数据库
        :type db: str
        :param state: 状态
        :type state: str
        :param command: 命令
        :type command: str
        :param keywords: 模糊搜索条件
        :type keywords: str
        :param show_all: 是否显示全部
        :type show_all: bool
        :param show_no_pid: 是否显示没有后台进程的会话
        :type show_no_pid: bool
        :param time: 指定慢sql阈值
        :type time: str
        :param cur_page: 页码
        :type cur_page: str
        :param per_page: 每页记录数
        :type per_page: str
        :param order_by: 排序字段
        :type order_by: str
        :param order: 排序方式（asc/desc）
        :type order: str
        :param node_id: 节点ID
        :type node_id: str
        :param node_role: 节点类型
        :type node_role: str
        :param hide_sys: 是否过滤系统会话
        :type hide_sys: bool
        """
        
        

        self._instance_id = None
        self._user = None
        self._host = None
        self._db = None
        self._state = None
        self._command = None
        self._keywords = None
        self._show_all = None
        self._show_no_pid = None
        self._time = None
        self._cur_page = None
        self._per_page = None
        self._order_by = None
        self._order = None
        self._node_id = None
        self._node_role = None
        self._hide_sys = None
        self.discriminator = None

        self.instance_id = instance_id
        if user is not None:
            self.user = user
        if host is not None:
            self.host = host
        if db is not None:
            self.db = db
        if state is not None:
            self.state = state
        if command is not None:
            self.command = command
        if keywords is not None:
            self.keywords = keywords
        if show_all is not None:
            self.show_all = show_all
        if show_no_pid is not None:
            self.show_no_pid = show_no_pid
        if time is not None:
            self.time = time
        if cur_page is not None:
            self.cur_page = cur_page
        if per_page is not None:
            self.per_page = per_page
        if order_by is not None:
            self.order_by = order_by
        if order is not None:
            self.order = order
        if node_id is not None:
            self.node_id = node_id
        if node_role is not None:
            self.node_role = node_role
        if hide_sys is not None:
            self.hide_sys = hide_sys

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListPostgresProcessesRequest.

        实例ID

        :return: The instance_id of this ListPostgresProcessesRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListPostgresProcessesRequest.

        实例ID

        :param instance_id: The instance_id of this ListPostgresProcessesRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def user(self):
        r"""Gets the user of this ListPostgresProcessesRequest.

        用户名

        :return: The user of this ListPostgresProcessesRequest.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        r"""Sets the user of this ListPostgresProcessesRequest.

        用户名

        :param user: The user of this ListPostgresProcessesRequest.
        :type user: str
        """
        self._user = user

    @property
    def host(self):
        r"""Gets the host of this ListPostgresProcessesRequest.

        访问来源IP

        :return: The host of this ListPostgresProcessesRequest.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        r"""Sets the host of this ListPostgresProcessesRequest.

        访问来源IP

        :param host: The host of this ListPostgresProcessesRequest.
        :type host: str
        """
        self._host = host

    @property
    def db(self):
        r"""Gets the db of this ListPostgresProcessesRequest.

        数据库

        :return: The db of this ListPostgresProcessesRequest.
        :rtype: str
        """
        return self._db

    @db.setter
    def db(self, db):
        r"""Sets the db of this ListPostgresProcessesRequest.

        数据库

        :param db: The db of this ListPostgresProcessesRequest.
        :type db: str
        """
        self._db = db

    @property
    def state(self):
        r"""Gets the state of this ListPostgresProcessesRequest.

        状态

        :return: The state of this ListPostgresProcessesRequest.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this ListPostgresProcessesRequest.

        状态

        :param state: The state of this ListPostgresProcessesRequest.
        :type state: str
        """
        self._state = state

    @property
    def command(self):
        r"""Gets the command of this ListPostgresProcessesRequest.

        命令

        :return: The command of this ListPostgresProcessesRequest.
        :rtype: str
        """
        return self._command

    @command.setter
    def command(self, command):
        r"""Sets the command of this ListPostgresProcessesRequest.

        命令

        :param command: The command of this ListPostgresProcessesRequest.
        :type command: str
        """
        self._command = command

    @property
    def keywords(self):
        r"""Gets the keywords of this ListPostgresProcessesRequest.

        模糊搜索条件

        :return: The keywords of this ListPostgresProcessesRequest.
        :rtype: str
        """
        return self._keywords

    @keywords.setter
    def keywords(self, keywords):
        r"""Sets the keywords of this ListPostgresProcessesRequest.

        模糊搜索条件

        :param keywords: The keywords of this ListPostgresProcessesRequest.
        :type keywords: str
        """
        self._keywords = keywords

    @property
    def show_all(self):
        r"""Gets the show_all of this ListPostgresProcessesRequest.

        是否显示全部

        :return: The show_all of this ListPostgresProcessesRequest.
        :rtype: bool
        """
        return self._show_all

    @show_all.setter
    def show_all(self, show_all):
        r"""Sets the show_all of this ListPostgresProcessesRequest.

        是否显示全部

        :param show_all: The show_all of this ListPostgresProcessesRequest.
        :type show_all: bool
        """
        self._show_all = show_all

    @property
    def show_no_pid(self):
        r"""Gets the show_no_pid of this ListPostgresProcessesRequest.

        是否显示没有后台进程的会话

        :return: The show_no_pid of this ListPostgresProcessesRequest.
        :rtype: bool
        """
        return self._show_no_pid

    @show_no_pid.setter
    def show_no_pid(self, show_no_pid):
        r"""Sets the show_no_pid of this ListPostgresProcessesRequest.

        是否显示没有后台进程的会话

        :param show_no_pid: The show_no_pid of this ListPostgresProcessesRequest.
        :type show_no_pid: bool
        """
        self._show_no_pid = show_no_pid

    @property
    def time(self):
        r"""Gets the time of this ListPostgresProcessesRequest.

        指定慢sql阈值

        :return: The time of this ListPostgresProcessesRequest.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        r"""Sets the time of this ListPostgresProcessesRequest.

        指定慢sql阈值

        :param time: The time of this ListPostgresProcessesRequest.
        :type time: str
        """
        self._time = time

    @property
    def cur_page(self):
        r"""Gets the cur_page of this ListPostgresProcessesRequest.

        页码

        :return: The cur_page of this ListPostgresProcessesRequest.
        :rtype: str
        """
        return self._cur_page

    @cur_page.setter
    def cur_page(self, cur_page):
        r"""Sets the cur_page of this ListPostgresProcessesRequest.

        页码

        :param cur_page: The cur_page of this ListPostgresProcessesRequest.
        :type cur_page: str
        """
        self._cur_page = cur_page

    @property
    def per_page(self):
        r"""Gets the per_page of this ListPostgresProcessesRequest.

        每页记录数

        :return: The per_page of this ListPostgresProcessesRequest.
        :rtype: str
        """
        return self._per_page

    @per_page.setter
    def per_page(self, per_page):
        r"""Sets the per_page of this ListPostgresProcessesRequest.

        每页记录数

        :param per_page: The per_page of this ListPostgresProcessesRequest.
        :type per_page: str
        """
        self._per_page = per_page

    @property
    def order_by(self):
        r"""Gets the order_by of this ListPostgresProcessesRequest.

        排序字段

        :return: The order_by of this ListPostgresProcessesRequest.
        :rtype: str
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        r"""Sets the order_by of this ListPostgresProcessesRequest.

        排序字段

        :param order_by: The order_by of this ListPostgresProcessesRequest.
        :type order_by: str
        """
        self._order_by = order_by

    @property
    def order(self):
        r"""Gets the order of this ListPostgresProcessesRequest.

        排序方式（asc/desc）

        :return: The order of this ListPostgresProcessesRequest.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        r"""Sets the order of this ListPostgresProcessesRequest.

        排序方式（asc/desc）

        :param order: The order of this ListPostgresProcessesRequest.
        :type order: str
        """
        self._order = order

    @property
    def node_id(self):
        r"""Gets the node_id of this ListPostgresProcessesRequest.

        节点ID

        :return: The node_id of this ListPostgresProcessesRequest.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this ListPostgresProcessesRequest.

        节点ID

        :param node_id: The node_id of this ListPostgresProcessesRequest.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def node_role(self):
        r"""Gets the node_role of this ListPostgresProcessesRequest.

        节点类型

        :return: The node_role of this ListPostgresProcessesRequest.
        :rtype: str
        """
        return self._node_role

    @node_role.setter
    def node_role(self, node_role):
        r"""Sets the node_role of this ListPostgresProcessesRequest.

        节点类型

        :param node_role: The node_role of this ListPostgresProcessesRequest.
        :type node_role: str
        """
        self._node_role = node_role

    @property
    def hide_sys(self):
        r"""Gets the hide_sys of this ListPostgresProcessesRequest.

        是否过滤系统会话

        :return: The hide_sys of this ListPostgresProcessesRequest.
        :rtype: bool
        """
        return self._hide_sys

    @hide_sys.setter
    def hide_sys(self, hide_sys):
        r"""Sets the hide_sys of this ListPostgresProcessesRequest.

        是否过滤系统会话

        :param hide_sys: The hide_sys of this ListPostgresProcessesRequest.
        :type hide_sys: bool
        """
        self._hide_sys = hide_sys

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
        if not isinstance(other, ListPostgresProcessesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
