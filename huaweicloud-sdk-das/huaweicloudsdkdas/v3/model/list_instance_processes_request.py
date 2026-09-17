# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstanceProcessesRequest:

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
        'user': 'str',
        'host': 'str',
        'db': 'str',
        'state': 'str',
        'command': 'str',
        'keywords': 'str',
        'cur_page': 'int',
        'per_page': 'int',
        'order_by': 'str',
        'order': 'str',
        'node_id': 'str',
        'network_type': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'engine_type': 'engine_type',
        'user': 'user',
        'host': 'host',
        'db': 'db',
        'state': 'state',
        'command': 'command',
        'keywords': 'keywords',
        'cur_page': 'cur_page',
        'per_page': 'per_page',
        'order_by': 'order_by',
        'order': 'order',
        'node_id': 'node_id',
        'network_type': 'network_type'
    }

    def __init__(self, instance_id=None, engine_type=None, user=None, host=None, db=None, state=None, command=None, keywords=None, cur_page=None, per_page=None, order_by=None, order=None, node_id=None, network_type=None):
        r"""ListInstanceProcessesRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param engine_type: 数据库引擎类型
        :type engine_type: str
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
        :param cur_page: 页码
        :type cur_page: int
        :param per_page: 每页记录数
        :type per_page: int
        :param order_by: 排序字段
        :type order_by: str
        :param order: 排序方式（asc/desc）
        :type order: str
        :param node_id: 节点ID
        :type node_id: str
        :param network_type: 数据库来源类型
        :type network_type: str
        """
        
        

        self._instance_id = None
        self._engine_type = None
        self._user = None
        self._host = None
        self._db = None
        self._state = None
        self._command = None
        self._keywords = None
        self._cur_page = None
        self._per_page = None
        self._order_by = None
        self._order = None
        self._node_id = None
        self._network_type = None
        self.discriminator = None

        self.instance_id = instance_id
        if engine_type is not None:
            self.engine_type = engine_type
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
        if network_type is not None:
            self.network_type = network_type

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListInstanceProcessesRequest.

        实例ID

        :return: The instance_id of this ListInstanceProcessesRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListInstanceProcessesRequest.

        实例ID

        :param instance_id: The instance_id of this ListInstanceProcessesRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def engine_type(self):
        r"""Gets the engine_type of this ListInstanceProcessesRequest.

        数据库引擎类型

        :return: The engine_type of this ListInstanceProcessesRequest.
        :rtype: str
        """
        return self._engine_type

    @engine_type.setter
    def engine_type(self, engine_type):
        r"""Sets the engine_type of this ListInstanceProcessesRequest.

        数据库引擎类型

        :param engine_type: The engine_type of this ListInstanceProcessesRequest.
        :type engine_type: str
        """
        self._engine_type = engine_type

    @property
    def user(self):
        r"""Gets the user of this ListInstanceProcessesRequest.

        用户名

        :return: The user of this ListInstanceProcessesRequest.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        r"""Sets the user of this ListInstanceProcessesRequest.

        用户名

        :param user: The user of this ListInstanceProcessesRequest.
        :type user: str
        """
        self._user = user

    @property
    def host(self):
        r"""Gets the host of this ListInstanceProcessesRequest.

        访问来源IP

        :return: The host of this ListInstanceProcessesRequest.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        r"""Sets the host of this ListInstanceProcessesRequest.

        访问来源IP

        :param host: The host of this ListInstanceProcessesRequest.
        :type host: str
        """
        self._host = host

    @property
    def db(self):
        r"""Gets the db of this ListInstanceProcessesRequest.

        数据库

        :return: The db of this ListInstanceProcessesRequest.
        :rtype: str
        """
        return self._db

    @db.setter
    def db(self, db):
        r"""Sets the db of this ListInstanceProcessesRequest.

        数据库

        :param db: The db of this ListInstanceProcessesRequest.
        :type db: str
        """
        self._db = db

    @property
    def state(self):
        r"""Gets the state of this ListInstanceProcessesRequest.

        状态

        :return: The state of this ListInstanceProcessesRequest.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this ListInstanceProcessesRequest.

        状态

        :param state: The state of this ListInstanceProcessesRequest.
        :type state: str
        """
        self._state = state

    @property
    def command(self):
        r"""Gets the command of this ListInstanceProcessesRequest.

        命令

        :return: The command of this ListInstanceProcessesRequest.
        :rtype: str
        """
        return self._command

    @command.setter
    def command(self, command):
        r"""Sets the command of this ListInstanceProcessesRequest.

        命令

        :param command: The command of this ListInstanceProcessesRequest.
        :type command: str
        """
        self._command = command

    @property
    def keywords(self):
        r"""Gets the keywords of this ListInstanceProcessesRequest.

        模糊搜索条件

        :return: The keywords of this ListInstanceProcessesRequest.
        :rtype: str
        """
        return self._keywords

    @keywords.setter
    def keywords(self, keywords):
        r"""Sets the keywords of this ListInstanceProcessesRequest.

        模糊搜索条件

        :param keywords: The keywords of this ListInstanceProcessesRequest.
        :type keywords: str
        """
        self._keywords = keywords

    @property
    def cur_page(self):
        r"""Gets the cur_page of this ListInstanceProcessesRequest.

        页码

        :return: The cur_page of this ListInstanceProcessesRequest.
        :rtype: int
        """
        return self._cur_page

    @cur_page.setter
    def cur_page(self, cur_page):
        r"""Sets the cur_page of this ListInstanceProcessesRequest.

        页码

        :param cur_page: The cur_page of this ListInstanceProcessesRequest.
        :type cur_page: int
        """
        self._cur_page = cur_page

    @property
    def per_page(self):
        r"""Gets the per_page of this ListInstanceProcessesRequest.

        每页记录数

        :return: The per_page of this ListInstanceProcessesRequest.
        :rtype: int
        """
        return self._per_page

    @per_page.setter
    def per_page(self, per_page):
        r"""Sets the per_page of this ListInstanceProcessesRequest.

        每页记录数

        :param per_page: The per_page of this ListInstanceProcessesRequest.
        :type per_page: int
        """
        self._per_page = per_page

    @property
    def order_by(self):
        r"""Gets the order_by of this ListInstanceProcessesRequest.

        排序字段

        :return: The order_by of this ListInstanceProcessesRequest.
        :rtype: str
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        r"""Sets the order_by of this ListInstanceProcessesRequest.

        排序字段

        :param order_by: The order_by of this ListInstanceProcessesRequest.
        :type order_by: str
        """
        self._order_by = order_by

    @property
    def order(self):
        r"""Gets the order of this ListInstanceProcessesRequest.

        排序方式（asc/desc）

        :return: The order of this ListInstanceProcessesRequest.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        r"""Sets the order of this ListInstanceProcessesRequest.

        排序方式（asc/desc）

        :param order: The order of this ListInstanceProcessesRequest.
        :type order: str
        """
        self._order = order

    @property
    def node_id(self):
        r"""Gets the node_id of this ListInstanceProcessesRequest.

        节点ID

        :return: The node_id of this ListInstanceProcessesRequest.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this ListInstanceProcessesRequest.

        节点ID

        :param node_id: The node_id of this ListInstanceProcessesRequest.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def network_type(self):
        r"""Gets the network_type of this ListInstanceProcessesRequest.

        数据库来源类型

        :return: The network_type of this ListInstanceProcessesRequest.
        :rtype: str
        """
        return self._network_type

    @network_type.setter
    def network_type(self, network_type):
        r"""Sets the network_type of this ListInstanceProcessesRequest.

        数据库来源类型

        :param network_type: The network_type of this ListInstanceProcessesRequest.
        :type network_type: str
        """
        self._network_type = network_type

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
        if not isinstance(other, ListInstanceProcessesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
