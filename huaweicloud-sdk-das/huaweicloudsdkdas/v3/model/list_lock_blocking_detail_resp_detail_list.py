# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListLockBlockingDetailRespDetailList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'unique_id': 'str',
        'spid': 'int',
        'blocked_by_spid': 'int',
        'collect_time': 'int',
        'start_time': 'int',
        'elapsed_time': 'int',
        'cpu': 'int',
        'wait_time': 'int',
        'wait_type': 'str',
        'sql': 'str',
        'query_hash': 'str',
        'db_name': 'str',
        'host_name': 'str',
        'client_app_name': 'str',
        'login_id': 'str',
        'cmd': 'str',
        'physical_io': 'int'
    }

    attribute_map = {
        'id': 'id',
        'unique_id': 'unique_id',
        'spid': 'spid',
        'blocked_by_spid': 'blocked_by_spid',
        'collect_time': 'collect_time',
        'start_time': 'start_time',
        'elapsed_time': 'elapsed_time',
        'cpu': 'cpu',
        'wait_time': 'wait_time',
        'wait_type': 'wait_type',
        'sql': 'sql',
        'query_hash': 'query_hash',
        'db_name': 'db_name',
        'host_name': 'host_name',
        'client_app_name': 'client_app_name',
        'login_id': 'login_id',
        'cmd': 'cmd',
        'physical_io': 'physical_io'
    }

    def __init__(self, id=None, unique_id=None, spid=None, blocked_by_spid=None, collect_time=None, start_time=None, elapsed_time=None, cpu=None, wait_time=None, wait_type=None, sql=None, query_hash=None, db_name=None, host_name=None, client_app_name=None, login_id=None, cmd=None, physical_io=None):
        r"""ListLockBlockingDetailRespDetailList

        The model defined in huaweicloud sdk

        :param id: 唯一ID
        :type id: str
        :param unique_id: 批次ID
        :type unique_id: str
        :param spid: 会话ID
        :type spid: int
        :param blocked_by_spid: 阻塞会话ID
        :type blocked_by_spid: int
        :param collect_time: 采集时间
        :type collect_time: int
        :param start_time: SQL开始时间
        :type start_time: int
        :param elapsed_time: 执行耗时（ms）
        :type elapsed_time: int
        :param cpu: CPU时间（ms）
        :type cpu: int
        :param wait_time: 阻塞时长（ms）
        :type wait_time: int
        :param wait_type: 等待类型
        :type wait_type: str
        :param sql: SQL
        :type sql: str
        :param query_hash: Query Hash
        :type query_hash: str
        :param db_name: 数据库名
        :type db_name: str
        :param host_name: 客户端HostName
        :type host_name: str
        :param client_app_name: 客户端名称
        :type client_app_name: str
        :param login_id: 当前用户
        :type login_id: str
        :param cmd: SQL命令类型
        :type cmd: str
        :param physical_io: SQL消耗的I/O
        :type physical_io: int
        """
        
        

        self._id = None
        self._unique_id = None
        self._spid = None
        self._blocked_by_spid = None
        self._collect_time = None
        self._start_time = None
        self._elapsed_time = None
        self._cpu = None
        self._wait_time = None
        self._wait_type = None
        self._sql = None
        self._query_hash = None
        self._db_name = None
        self._host_name = None
        self._client_app_name = None
        self._login_id = None
        self._cmd = None
        self._physical_io = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if unique_id is not None:
            self.unique_id = unique_id
        if spid is not None:
            self.spid = spid
        if blocked_by_spid is not None:
            self.blocked_by_spid = blocked_by_spid
        if collect_time is not None:
            self.collect_time = collect_time
        if start_time is not None:
            self.start_time = start_time
        if elapsed_time is not None:
            self.elapsed_time = elapsed_time
        if cpu is not None:
            self.cpu = cpu
        if wait_time is not None:
            self.wait_time = wait_time
        if wait_type is not None:
            self.wait_type = wait_type
        if sql is not None:
            self.sql = sql
        if query_hash is not None:
            self.query_hash = query_hash
        if db_name is not None:
            self.db_name = db_name
        if host_name is not None:
            self.host_name = host_name
        if client_app_name is not None:
            self.client_app_name = client_app_name
        if login_id is not None:
            self.login_id = login_id
        if cmd is not None:
            self.cmd = cmd
        if physical_io is not None:
            self.physical_io = physical_io

    @property
    def id(self):
        r"""Gets the id of this ListLockBlockingDetailRespDetailList.

        唯一ID

        :return: The id of this ListLockBlockingDetailRespDetailList.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListLockBlockingDetailRespDetailList.

        唯一ID

        :param id: The id of this ListLockBlockingDetailRespDetailList.
        :type id: str
        """
        self._id = id

    @property
    def unique_id(self):
        r"""Gets the unique_id of this ListLockBlockingDetailRespDetailList.

        批次ID

        :return: The unique_id of this ListLockBlockingDetailRespDetailList.
        :rtype: str
        """
        return self._unique_id

    @unique_id.setter
    def unique_id(self, unique_id):
        r"""Sets the unique_id of this ListLockBlockingDetailRespDetailList.

        批次ID

        :param unique_id: The unique_id of this ListLockBlockingDetailRespDetailList.
        :type unique_id: str
        """
        self._unique_id = unique_id

    @property
    def spid(self):
        r"""Gets the spid of this ListLockBlockingDetailRespDetailList.

        会话ID

        :return: The spid of this ListLockBlockingDetailRespDetailList.
        :rtype: int
        """
        return self._spid

    @spid.setter
    def spid(self, spid):
        r"""Sets the spid of this ListLockBlockingDetailRespDetailList.

        会话ID

        :param spid: The spid of this ListLockBlockingDetailRespDetailList.
        :type spid: int
        """
        self._spid = spid

    @property
    def blocked_by_spid(self):
        r"""Gets the blocked_by_spid of this ListLockBlockingDetailRespDetailList.

        阻塞会话ID

        :return: The blocked_by_spid of this ListLockBlockingDetailRespDetailList.
        :rtype: int
        """
        return self._blocked_by_spid

    @blocked_by_spid.setter
    def blocked_by_spid(self, blocked_by_spid):
        r"""Sets the blocked_by_spid of this ListLockBlockingDetailRespDetailList.

        阻塞会话ID

        :param blocked_by_spid: The blocked_by_spid of this ListLockBlockingDetailRespDetailList.
        :type blocked_by_spid: int
        """
        self._blocked_by_spid = blocked_by_spid

    @property
    def collect_time(self):
        r"""Gets the collect_time of this ListLockBlockingDetailRespDetailList.

        采集时间

        :return: The collect_time of this ListLockBlockingDetailRespDetailList.
        :rtype: int
        """
        return self._collect_time

    @collect_time.setter
    def collect_time(self, collect_time):
        r"""Sets the collect_time of this ListLockBlockingDetailRespDetailList.

        采集时间

        :param collect_time: The collect_time of this ListLockBlockingDetailRespDetailList.
        :type collect_time: int
        """
        self._collect_time = collect_time

    @property
    def start_time(self):
        r"""Gets the start_time of this ListLockBlockingDetailRespDetailList.

        SQL开始时间

        :return: The start_time of this ListLockBlockingDetailRespDetailList.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListLockBlockingDetailRespDetailList.

        SQL开始时间

        :param start_time: The start_time of this ListLockBlockingDetailRespDetailList.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def elapsed_time(self):
        r"""Gets the elapsed_time of this ListLockBlockingDetailRespDetailList.

        执行耗时（ms）

        :return: The elapsed_time of this ListLockBlockingDetailRespDetailList.
        :rtype: int
        """
        return self._elapsed_time

    @elapsed_time.setter
    def elapsed_time(self, elapsed_time):
        r"""Sets the elapsed_time of this ListLockBlockingDetailRespDetailList.

        执行耗时（ms）

        :param elapsed_time: The elapsed_time of this ListLockBlockingDetailRespDetailList.
        :type elapsed_time: int
        """
        self._elapsed_time = elapsed_time

    @property
    def cpu(self):
        r"""Gets the cpu of this ListLockBlockingDetailRespDetailList.

        CPU时间（ms）

        :return: The cpu of this ListLockBlockingDetailRespDetailList.
        :rtype: int
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        r"""Sets the cpu of this ListLockBlockingDetailRespDetailList.

        CPU时间（ms）

        :param cpu: The cpu of this ListLockBlockingDetailRespDetailList.
        :type cpu: int
        """
        self._cpu = cpu

    @property
    def wait_time(self):
        r"""Gets the wait_time of this ListLockBlockingDetailRespDetailList.

        阻塞时长（ms）

        :return: The wait_time of this ListLockBlockingDetailRespDetailList.
        :rtype: int
        """
        return self._wait_time

    @wait_time.setter
    def wait_time(self, wait_time):
        r"""Sets the wait_time of this ListLockBlockingDetailRespDetailList.

        阻塞时长（ms）

        :param wait_time: The wait_time of this ListLockBlockingDetailRespDetailList.
        :type wait_time: int
        """
        self._wait_time = wait_time

    @property
    def wait_type(self):
        r"""Gets the wait_type of this ListLockBlockingDetailRespDetailList.

        等待类型

        :return: The wait_type of this ListLockBlockingDetailRespDetailList.
        :rtype: str
        """
        return self._wait_type

    @wait_type.setter
    def wait_type(self, wait_type):
        r"""Sets the wait_type of this ListLockBlockingDetailRespDetailList.

        等待类型

        :param wait_type: The wait_type of this ListLockBlockingDetailRespDetailList.
        :type wait_type: str
        """
        self._wait_type = wait_type

    @property
    def sql(self):
        r"""Gets the sql of this ListLockBlockingDetailRespDetailList.

        SQL

        :return: The sql of this ListLockBlockingDetailRespDetailList.
        :rtype: str
        """
        return self._sql

    @sql.setter
    def sql(self, sql):
        r"""Sets the sql of this ListLockBlockingDetailRespDetailList.

        SQL

        :param sql: The sql of this ListLockBlockingDetailRespDetailList.
        :type sql: str
        """
        self._sql = sql

    @property
    def query_hash(self):
        r"""Gets the query_hash of this ListLockBlockingDetailRespDetailList.

        Query Hash

        :return: The query_hash of this ListLockBlockingDetailRespDetailList.
        :rtype: str
        """
        return self._query_hash

    @query_hash.setter
    def query_hash(self, query_hash):
        r"""Sets the query_hash of this ListLockBlockingDetailRespDetailList.

        Query Hash

        :param query_hash: The query_hash of this ListLockBlockingDetailRespDetailList.
        :type query_hash: str
        """
        self._query_hash = query_hash

    @property
    def db_name(self):
        r"""Gets the db_name of this ListLockBlockingDetailRespDetailList.

        数据库名

        :return: The db_name of this ListLockBlockingDetailRespDetailList.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        r"""Sets the db_name of this ListLockBlockingDetailRespDetailList.

        数据库名

        :param db_name: The db_name of this ListLockBlockingDetailRespDetailList.
        :type db_name: str
        """
        self._db_name = db_name

    @property
    def host_name(self):
        r"""Gets the host_name of this ListLockBlockingDetailRespDetailList.

        客户端HostName

        :return: The host_name of this ListLockBlockingDetailRespDetailList.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this ListLockBlockingDetailRespDetailList.

        客户端HostName

        :param host_name: The host_name of this ListLockBlockingDetailRespDetailList.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def client_app_name(self):
        r"""Gets the client_app_name of this ListLockBlockingDetailRespDetailList.

        客户端名称

        :return: The client_app_name of this ListLockBlockingDetailRespDetailList.
        :rtype: str
        """
        return self._client_app_name

    @client_app_name.setter
    def client_app_name(self, client_app_name):
        r"""Sets the client_app_name of this ListLockBlockingDetailRespDetailList.

        客户端名称

        :param client_app_name: The client_app_name of this ListLockBlockingDetailRespDetailList.
        :type client_app_name: str
        """
        self._client_app_name = client_app_name

    @property
    def login_id(self):
        r"""Gets the login_id of this ListLockBlockingDetailRespDetailList.

        当前用户

        :return: The login_id of this ListLockBlockingDetailRespDetailList.
        :rtype: str
        """
        return self._login_id

    @login_id.setter
    def login_id(self, login_id):
        r"""Sets the login_id of this ListLockBlockingDetailRespDetailList.

        当前用户

        :param login_id: The login_id of this ListLockBlockingDetailRespDetailList.
        :type login_id: str
        """
        self._login_id = login_id

    @property
    def cmd(self):
        r"""Gets the cmd of this ListLockBlockingDetailRespDetailList.

        SQL命令类型

        :return: The cmd of this ListLockBlockingDetailRespDetailList.
        :rtype: str
        """
        return self._cmd

    @cmd.setter
    def cmd(self, cmd):
        r"""Sets the cmd of this ListLockBlockingDetailRespDetailList.

        SQL命令类型

        :param cmd: The cmd of this ListLockBlockingDetailRespDetailList.
        :type cmd: str
        """
        self._cmd = cmd

    @property
    def physical_io(self):
        r"""Gets the physical_io of this ListLockBlockingDetailRespDetailList.

        SQL消耗的I/O

        :return: The physical_io of this ListLockBlockingDetailRespDetailList.
        :rtype: int
        """
        return self._physical_io

    @physical_io.setter
    def physical_io(self, physical_io):
        r"""Sets the physical_io of this ListLockBlockingDetailRespDetailList.

        SQL消耗的I/O

        :param physical_io: The physical_io of this ListLockBlockingDetailRespDetailList.
        :type physical_io: int
        """
        self._physical_io = physical_io

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
        if not isinstance(other, ListLockBlockingDetailRespDetailList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
