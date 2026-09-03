# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeadLockDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dead_lock_id': 'str',
        'last_tran_started': 'str',
        'spid': 'str',
        'is_victim': 'bool',
        'log_used': 'int',
        'lock_mode': 'str',
        'wait_resource_desc': 'str',
        'object_owned': 'str',
        'object_requested': 'str',
        'wait_resource': 'str',
        'host_name': 'str',
        'login_name': 'str',
        'status': 'str',
        'client_app': 'str',
        'sql': 'str',
        'db_id': 'str',
        'db_name': 'str',
        'sub_detail_list': 'list[DeadLockSubDetail]'
    }

    attribute_map = {
        'dead_lock_id': 'dead_lock_id',
        'last_tran_started': 'last_tran_started',
        'spid': 'spid',
        'is_victim': 'is_victim',
        'log_used': 'log_used',
        'lock_mode': 'lock_mode',
        'wait_resource_desc': 'wait_resource_desc',
        'object_owned': 'object_owned',
        'object_requested': 'object_requested',
        'wait_resource': 'wait_resource',
        'host_name': 'host_name',
        'login_name': 'login_name',
        'status': 'status',
        'client_app': 'client_app',
        'sql': 'sql',
        'db_id': 'db_id',
        'db_name': 'db_name',
        'sub_detail_list': 'sub_detail_list'
    }

    def __init__(self, dead_lock_id=None, last_tran_started=None, spid=None, is_victim=None, log_used=None, lock_mode=None, wait_resource_desc=None, object_owned=None, object_requested=None, wait_resource=None, host_name=None, login_name=None, status=None, client_app=None, sql=None, db_id=None, db_name=None, sub_detail_list=None):
        r"""DeadLockDetail

        The model defined in huaweicloud sdk

        :param dead_lock_id: 死锁ID
        :type dead_lock_id: str
        :param last_tran_started: 事务开启时间
        :type last_tran_started: str
        :param spid: 服务进程ID
        :type spid: str
        :param is_victim: 该会话是否已被终止
        :type is_victim: bool
        :param log_used: 任务使用的日志空间
        :type log_used: int
        :param lock_mode: 锁模式（S,X,U）
        :type lock_mode: str
        :param wait_resource_desc: 等待中的资源详情
        :type wait_resource_desc: str
        :param object_owned: 被锁住的对象
        :type object_owned: str
        :param object_requested: 请求加锁的对象
        :type object_requested: str
        :param wait_resource: 等待资源名称
        :type wait_resource: str
        :param host_name: 主机名称
        :type host_name: str
        :param login_name: 状态
        :type login_name: str
        :param status: 等待中的资源详情
        :type status: str
        :param client_app: 客户端
        :type client_app: str
        :param sql: SQL
        :type sql: str
        :param db_id: 数据库ID
        :type db_id: str
        :param db_name: 数据库名称
        :type db_name: str
        :param sub_detail_list: 死锁子明细列表
        :type sub_detail_list: list[:class:`huaweicloudsdkdas.v3.DeadLockSubDetail`]
        """
        
        

        self._dead_lock_id = None
        self._last_tran_started = None
        self._spid = None
        self._is_victim = None
        self._log_used = None
        self._lock_mode = None
        self._wait_resource_desc = None
        self._object_owned = None
        self._object_requested = None
        self._wait_resource = None
        self._host_name = None
        self._login_name = None
        self._status = None
        self._client_app = None
        self._sql = None
        self._db_id = None
        self._db_name = None
        self._sub_detail_list = None
        self.discriminator = None

        if dead_lock_id is not None:
            self.dead_lock_id = dead_lock_id
        if last_tran_started is not None:
            self.last_tran_started = last_tran_started
        if spid is not None:
            self.spid = spid
        if is_victim is not None:
            self.is_victim = is_victim
        if log_used is not None:
            self.log_used = log_used
        if lock_mode is not None:
            self.lock_mode = lock_mode
        if wait_resource_desc is not None:
            self.wait_resource_desc = wait_resource_desc
        if object_owned is not None:
            self.object_owned = object_owned
        if object_requested is not None:
            self.object_requested = object_requested
        if wait_resource is not None:
            self.wait_resource = wait_resource
        if host_name is not None:
            self.host_name = host_name
        if login_name is not None:
            self.login_name = login_name
        if status is not None:
            self.status = status
        if client_app is not None:
            self.client_app = client_app
        if sql is not None:
            self.sql = sql
        if db_id is not None:
            self.db_id = db_id
        if db_name is not None:
            self.db_name = db_name
        if sub_detail_list is not None:
            self.sub_detail_list = sub_detail_list

    @property
    def dead_lock_id(self):
        r"""Gets the dead_lock_id of this DeadLockDetail.

        死锁ID

        :return: The dead_lock_id of this DeadLockDetail.
        :rtype: str
        """
        return self._dead_lock_id

    @dead_lock_id.setter
    def dead_lock_id(self, dead_lock_id):
        r"""Sets the dead_lock_id of this DeadLockDetail.

        死锁ID

        :param dead_lock_id: The dead_lock_id of this DeadLockDetail.
        :type dead_lock_id: str
        """
        self._dead_lock_id = dead_lock_id

    @property
    def last_tran_started(self):
        r"""Gets the last_tran_started of this DeadLockDetail.

        事务开启时间

        :return: The last_tran_started of this DeadLockDetail.
        :rtype: str
        """
        return self._last_tran_started

    @last_tran_started.setter
    def last_tran_started(self, last_tran_started):
        r"""Sets the last_tran_started of this DeadLockDetail.

        事务开启时间

        :param last_tran_started: The last_tran_started of this DeadLockDetail.
        :type last_tran_started: str
        """
        self._last_tran_started = last_tran_started

    @property
    def spid(self):
        r"""Gets the spid of this DeadLockDetail.

        服务进程ID

        :return: The spid of this DeadLockDetail.
        :rtype: str
        """
        return self._spid

    @spid.setter
    def spid(self, spid):
        r"""Sets the spid of this DeadLockDetail.

        服务进程ID

        :param spid: The spid of this DeadLockDetail.
        :type spid: str
        """
        self._spid = spid

    @property
    def is_victim(self):
        r"""Gets the is_victim of this DeadLockDetail.

        该会话是否已被终止

        :return: The is_victim of this DeadLockDetail.
        :rtype: bool
        """
        return self._is_victim

    @is_victim.setter
    def is_victim(self, is_victim):
        r"""Sets the is_victim of this DeadLockDetail.

        该会话是否已被终止

        :param is_victim: The is_victim of this DeadLockDetail.
        :type is_victim: bool
        """
        self._is_victim = is_victim

    @property
    def log_used(self):
        r"""Gets the log_used of this DeadLockDetail.

        任务使用的日志空间

        :return: The log_used of this DeadLockDetail.
        :rtype: int
        """
        return self._log_used

    @log_used.setter
    def log_used(self, log_used):
        r"""Sets the log_used of this DeadLockDetail.

        任务使用的日志空间

        :param log_used: The log_used of this DeadLockDetail.
        :type log_used: int
        """
        self._log_used = log_used

    @property
    def lock_mode(self):
        r"""Gets the lock_mode of this DeadLockDetail.

        锁模式（S,X,U）

        :return: The lock_mode of this DeadLockDetail.
        :rtype: str
        """
        return self._lock_mode

    @lock_mode.setter
    def lock_mode(self, lock_mode):
        r"""Sets the lock_mode of this DeadLockDetail.

        锁模式（S,X,U）

        :param lock_mode: The lock_mode of this DeadLockDetail.
        :type lock_mode: str
        """
        self._lock_mode = lock_mode

    @property
    def wait_resource_desc(self):
        r"""Gets the wait_resource_desc of this DeadLockDetail.

        等待中的资源详情

        :return: The wait_resource_desc of this DeadLockDetail.
        :rtype: str
        """
        return self._wait_resource_desc

    @wait_resource_desc.setter
    def wait_resource_desc(self, wait_resource_desc):
        r"""Sets the wait_resource_desc of this DeadLockDetail.

        等待中的资源详情

        :param wait_resource_desc: The wait_resource_desc of this DeadLockDetail.
        :type wait_resource_desc: str
        """
        self._wait_resource_desc = wait_resource_desc

    @property
    def object_owned(self):
        r"""Gets the object_owned of this DeadLockDetail.

        被锁住的对象

        :return: The object_owned of this DeadLockDetail.
        :rtype: str
        """
        return self._object_owned

    @object_owned.setter
    def object_owned(self, object_owned):
        r"""Sets the object_owned of this DeadLockDetail.

        被锁住的对象

        :param object_owned: The object_owned of this DeadLockDetail.
        :type object_owned: str
        """
        self._object_owned = object_owned

    @property
    def object_requested(self):
        r"""Gets the object_requested of this DeadLockDetail.

        请求加锁的对象

        :return: The object_requested of this DeadLockDetail.
        :rtype: str
        """
        return self._object_requested

    @object_requested.setter
    def object_requested(self, object_requested):
        r"""Sets the object_requested of this DeadLockDetail.

        请求加锁的对象

        :param object_requested: The object_requested of this DeadLockDetail.
        :type object_requested: str
        """
        self._object_requested = object_requested

    @property
    def wait_resource(self):
        r"""Gets the wait_resource of this DeadLockDetail.

        等待资源名称

        :return: The wait_resource of this DeadLockDetail.
        :rtype: str
        """
        return self._wait_resource

    @wait_resource.setter
    def wait_resource(self, wait_resource):
        r"""Sets the wait_resource of this DeadLockDetail.

        等待资源名称

        :param wait_resource: The wait_resource of this DeadLockDetail.
        :type wait_resource: str
        """
        self._wait_resource = wait_resource

    @property
    def host_name(self):
        r"""Gets the host_name of this DeadLockDetail.

        主机名称

        :return: The host_name of this DeadLockDetail.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this DeadLockDetail.

        主机名称

        :param host_name: The host_name of this DeadLockDetail.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def login_name(self):
        r"""Gets the login_name of this DeadLockDetail.

        状态

        :return: The login_name of this DeadLockDetail.
        :rtype: str
        """
        return self._login_name

    @login_name.setter
    def login_name(self, login_name):
        r"""Sets the login_name of this DeadLockDetail.

        状态

        :param login_name: The login_name of this DeadLockDetail.
        :type login_name: str
        """
        self._login_name = login_name

    @property
    def status(self):
        r"""Gets the status of this DeadLockDetail.

        等待中的资源详情

        :return: The status of this DeadLockDetail.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this DeadLockDetail.

        等待中的资源详情

        :param status: The status of this DeadLockDetail.
        :type status: str
        """
        self._status = status

    @property
    def client_app(self):
        r"""Gets the client_app of this DeadLockDetail.

        客户端

        :return: The client_app of this DeadLockDetail.
        :rtype: str
        """
        return self._client_app

    @client_app.setter
    def client_app(self, client_app):
        r"""Sets the client_app of this DeadLockDetail.

        客户端

        :param client_app: The client_app of this DeadLockDetail.
        :type client_app: str
        """
        self._client_app = client_app

    @property
    def sql(self):
        r"""Gets the sql of this DeadLockDetail.

        SQL

        :return: The sql of this DeadLockDetail.
        :rtype: str
        """
        return self._sql

    @sql.setter
    def sql(self, sql):
        r"""Sets the sql of this DeadLockDetail.

        SQL

        :param sql: The sql of this DeadLockDetail.
        :type sql: str
        """
        self._sql = sql

    @property
    def db_id(self):
        r"""Gets the db_id of this DeadLockDetail.

        数据库ID

        :return: The db_id of this DeadLockDetail.
        :rtype: str
        """
        return self._db_id

    @db_id.setter
    def db_id(self, db_id):
        r"""Sets the db_id of this DeadLockDetail.

        数据库ID

        :param db_id: The db_id of this DeadLockDetail.
        :type db_id: str
        """
        self._db_id = db_id

    @property
    def db_name(self):
        r"""Gets the db_name of this DeadLockDetail.

        数据库名称

        :return: The db_name of this DeadLockDetail.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        r"""Sets the db_name of this DeadLockDetail.

        数据库名称

        :param db_name: The db_name of this DeadLockDetail.
        :type db_name: str
        """
        self._db_name = db_name

    @property
    def sub_detail_list(self):
        r"""Gets the sub_detail_list of this DeadLockDetail.

        死锁子明细列表

        :return: The sub_detail_list of this DeadLockDetail.
        :rtype: list[:class:`huaweicloudsdkdas.v3.DeadLockSubDetail`]
        """
        return self._sub_detail_list

    @sub_detail_list.setter
    def sub_detail_list(self, sub_detail_list):
        r"""Sets the sub_detail_list of this DeadLockDetail.

        死锁子明细列表

        :param sub_detail_list: The sub_detail_list of this DeadLockDetail.
        :type sub_detail_list: list[:class:`huaweicloudsdkdas.v3.DeadLockSubDetail`]
        """
        self._sub_detail_list = sub_detail_list

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
        if not isinstance(other, DeadLockDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
