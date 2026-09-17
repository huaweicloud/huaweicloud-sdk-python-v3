# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DasConnInfo:

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
        'instance_id': 'str',
        'instance_name': 'str',
        'network_type': 'str',
        'engine_type': 'str',
        'datastore_version': 'str',
        'user_name': 'str',
        'database_name': 'str',
        'is_save_password': 'bool',
        'ip_address': 'str',
        'port': 'int',
        'remarks': 'str',
        'instance_type': 'str',
        'create_at': 'int',
        'status': 'str',
        'sql_record_flag': 'bool',
        'conn_share_type': 'str',
        'shared_count': 'int',
        'service_type': 'str',
        'shared_user_name': 'str',
        'shared_user_id': 'str',
        'expired_time': 'int'
    }

    attribute_map = {
        'connection_id': 'connection_id',
        'instance_id': 'instance_id',
        'instance_name': 'instance_name',
        'network_type': 'network_type',
        'engine_type': 'engine_type',
        'datastore_version': 'datastore_version',
        'user_name': 'user_name',
        'database_name': 'database_name',
        'is_save_password': 'is_save_password',
        'ip_address': 'ip_address',
        'port': 'port',
        'remarks': 'remarks',
        'instance_type': 'instance_type',
        'create_at': 'create_at',
        'status': 'status',
        'sql_record_flag': 'sql_record_flag',
        'conn_share_type': 'conn_share_type',
        'shared_count': 'shared_count',
        'service_type': 'service_type',
        'shared_user_name': 'shared_user_name',
        'shared_user_id': 'shared_user_id',
        'expired_time': 'expired_time'
    }

    def __init__(self, connection_id=None, instance_id=None, instance_name=None, network_type=None, engine_type=None, datastore_version=None, user_name=None, database_name=None, is_save_password=None, ip_address=None, port=None, remarks=None, instance_type=None, create_at=None, status=None, sql_record_flag=None, conn_share_type=None, shared_count=None, service_type=None, shared_user_name=None, shared_user_id=None, expired_time=None):
        r"""DasConnInfo

        The model defined in huaweicloud sdk

        :param connection_id: 连接ID
        :type connection_id: str
        :param instance_id: 实例ID
        :type instance_id: str
        :param instance_name: 实例名称
        :type instance_name: str
        :param network_type: 数据库来源类型
        :type network_type: str
        :param engine_type: 数据库引擎类型
        :type engine_type: str
        :param datastore_version: 数据库版本
        :type datastore_version: str
        :param user_name: 用户名
        :type user_name: str
        :param database_name: 数据库名称
        :type database_name: str
        :param is_save_password: 是否保存密码
        :type is_save_password: bool
        :param ip_address: IP地址
        :type ip_address: str
        :param port: 端口号
        :type port: int
        :param remarks: 备注
        :type remarks: str
        :param instance_type: 实例类型
        :type instance_type: str
        :param create_at: 连接的创建时间
        :type create_at: int
        :param status: 状态
        :type status: str
        :param sql_record_flag: sql记录开关
        :type sql_record_flag: bool
        :param conn_share_type: 连接类型
        :type conn_share_type: str
        :param shared_count: 共享用户数
        :type shared_count: int
        :param service_type: 服务类型
        :type service_type: str
        :param shared_user_name: 共享人名称
        :type shared_user_name: str
        :param shared_user_id: 共享人ID
        :type shared_user_id: str
        :param expired_time: 共享过期时间
        :type expired_time: int
        """
        
        

        self._connection_id = None
        self._instance_id = None
        self._instance_name = None
        self._network_type = None
        self._engine_type = None
        self._datastore_version = None
        self._user_name = None
        self._database_name = None
        self._is_save_password = None
        self._ip_address = None
        self._port = None
        self._remarks = None
        self._instance_type = None
        self._create_at = None
        self._status = None
        self._sql_record_flag = None
        self._conn_share_type = None
        self._shared_count = None
        self._service_type = None
        self._shared_user_name = None
        self._shared_user_id = None
        self._expired_time = None
        self.discriminator = None

        if connection_id is not None:
            self.connection_id = connection_id
        if instance_id is not None:
            self.instance_id = instance_id
        if instance_name is not None:
            self.instance_name = instance_name
        if network_type is not None:
            self.network_type = network_type
        if engine_type is not None:
            self.engine_type = engine_type
        if datastore_version is not None:
            self.datastore_version = datastore_version
        if user_name is not None:
            self.user_name = user_name
        if database_name is not None:
            self.database_name = database_name
        if is_save_password is not None:
            self.is_save_password = is_save_password
        if ip_address is not None:
            self.ip_address = ip_address
        if port is not None:
            self.port = port
        if remarks is not None:
            self.remarks = remarks
        if instance_type is not None:
            self.instance_type = instance_type
        if create_at is not None:
            self.create_at = create_at
        if status is not None:
            self.status = status
        if sql_record_flag is not None:
            self.sql_record_flag = sql_record_flag
        if conn_share_type is not None:
            self.conn_share_type = conn_share_type
        if shared_count is not None:
            self.shared_count = shared_count
        if service_type is not None:
            self.service_type = service_type
        if shared_user_name is not None:
            self.shared_user_name = shared_user_name
        if shared_user_id is not None:
            self.shared_user_id = shared_user_id
        if expired_time is not None:
            self.expired_time = expired_time

    @property
    def connection_id(self):
        r"""Gets the connection_id of this DasConnInfo.

        连接ID

        :return: The connection_id of this DasConnInfo.
        :rtype: str
        """
        return self._connection_id

    @connection_id.setter
    def connection_id(self, connection_id):
        r"""Sets the connection_id of this DasConnInfo.

        连接ID

        :param connection_id: The connection_id of this DasConnInfo.
        :type connection_id: str
        """
        self._connection_id = connection_id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this DasConnInfo.

        实例ID

        :return: The instance_id of this DasConnInfo.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this DasConnInfo.

        实例ID

        :param instance_id: The instance_id of this DasConnInfo.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def instance_name(self):
        r"""Gets the instance_name of this DasConnInfo.

        实例名称

        :return: The instance_name of this DasConnInfo.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        r"""Sets the instance_name of this DasConnInfo.

        实例名称

        :param instance_name: The instance_name of this DasConnInfo.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def network_type(self):
        r"""Gets the network_type of this DasConnInfo.

        数据库来源类型

        :return: The network_type of this DasConnInfo.
        :rtype: str
        """
        return self._network_type

    @network_type.setter
    def network_type(self, network_type):
        r"""Sets the network_type of this DasConnInfo.

        数据库来源类型

        :param network_type: The network_type of this DasConnInfo.
        :type network_type: str
        """
        self._network_type = network_type

    @property
    def engine_type(self):
        r"""Gets the engine_type of this DasConnInfo.

        数据库引擎类型

        :return: The engine_type of this DasConnInfo.
        :rtype: str
        """
        return self._engine_type

    @engine_type.setter
    def engine_type(self, engine_type):
        r"""Sets the engine_type of this DasConnInfo.

        数据库引擎类型

        :param engine_type: The engine_type of this DasConnInfo.
        :type engine_type: str
        """
        self._engine_type = engine_type

    @property
    def datastore_version(self):
        r"""Gets the datastore_version of this DasConnInfo.

        数据库版本

        :return: The datastore_version of this DasConnInfo.
        :rtype: str
        """
        return self._datastore_version

    @datastore_version.setter
    def datastore_version(self, datastore_version):
        r"""Sets the datastore_version of this DasConnInfo.

        数据库版本

        :param datastore_version: The datastore_version of this DasConnInfo.
        :type datastore_version: str
        """
        self._datastore_version = datastore_version

    @property
    def user_name(self):
        r"""Gets the user_name of this DasConnInfo.

        用户名

        :return: The user_name of this DasConnInfo.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this DasConnInfo.

        用户名

        :param user_name: The user_name of this DasConnInfo.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def database_name(self):
        r"""Gets the database_name of this DasConnInfo.

        数据库名称

        :return: The database_name of this DasConnInfo.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        r"""Sets the database_name of this DasConnInfo.

        数据库名称

        :param database_name: The database_name of this DasConnInfo.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def is_save_password(self):
        r"""Gets the is_save_password of this DasConnInfo.

        是否保存密码

        :return: The is_save_password of this DasConnInfo.
        :rtype: bool
        """
        return self._is_save_password

    @is_save_password.setter
    def is_save_password(self, is_save_password):
        r"""Sets the is_save_password of this DasConnInfo.

        是否保存密码

        :param is_save_password: The is_save_password of this DasConnInfo.
        :type is_save_password: bool
        """
        self._is_save_password = is_save_password

    @property
    def ip_address(self):
        r"""Gets the ip_address of this DasConnInfo.

        IP地址

        :return: The ip_address of this DasConnInfo.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        r"""Sets the ip_address of this DasConnInfo.

        IP地址

        :param ip_address: The ip_address of this DasConnInfo.
        :type ip_address: str
        """
        self._ip_address = ip_address

    @property
    def port(self):
        r"""Gets the port of this DasConnInfo.

        端口号

        :return: The port of this DasConnInfo.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this DasConnInfo.

        端口号

        :param port: The port of this DasConnInfo.
        :type port: int
        """
        self._port = port

    @property
    def remarks(self):
        r"""Gets the remarks of this DasConnInfo.

        备注

        :return: The remarks of this DasConnInfo.
        :rtype: str
        """
        return self._remarks

    @remarks.setter
    def remarks(self, remarks):
        r"""Sets the remarks of this DasConnInfo.

        备注

        :param remarks: The remarks of this DasConnInfo.
        :type remarks: str
        """
        self._remarks = remarks

    @property
    def instance_type(self):
        r"""Gets the instance_type of this DasConnInfo.

        实例类型

        :return: The instance_type of this DasConnInfo.
        :rtype: str
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        r"""Sets the instance_type of this DasConnInfo.

        实例类型

        :param instance_type: The instance_type of this DasConnInfo.
        :type instance_type: str
        """
        self._instance_type = instance_type

    @property
    def create_at(self):
        r"""Gets the create_at of this DasConnInfo.

        连接的创建时间

        :return: The create_at of this DasConnInfo.
        :rtype: int
        """
        return self._create_at

    @create_at.setter
    def create_at(self, create_at):
        r"""Sets the create_at of this DasConnInfo.

        连接的创建时间

        :param create_at: The create_at of this DasConnInfo.
        :type create_at: int
        """
        self._create_at = create_at

    @property
    def status(self):
        r"""Gets the status of this DasConnInfo.

        状态

        :return: The status of this DasConnInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this DasConnInfo.

        状态

        :param status: The status of this DasConnInfo.
        :type status: str
        """
        self._status = status

    @property
    def sql_record_flag(self):
        r"""Gets the sql_record_flag of this DasConnInfo.

        sql记录开关

        :return: The sql_record_flag of this DasConnInfo.
        :rtype: bool
        """
        return self._sql_record_flag

    @sql_record_flag.setter
    def sql_record_flag(self, sql_record_flag):
        r"""Sets the sql_record_flag of this DasConnInfo.

        sql记录开关

        :param sql_record_flag: The sql_record_flag of this DasConnInfo.
        :type sql_record_flag: bool
        """
        self._sql_record_flag = sql_record_flag

    @property
    def conn_share_type(self):
        r"""Gets the conn_share_type of this DasConnInfo.

        连接类型

        :return: The conn_share_type of this DasConnInfo.
        :rtype: str
        """
        return self._conn_share_type

    @conn_share_type.setter
    def conn_share_type(self, conn_share_type):
        r"""Sets the conn_share_type of this DasConnInfo.

        连接类型

        :param conn_share_type: The conn_share_type of this DasConnInfo.
        :type conn_share_type: str
        """
        self._conn_share_type = conn_share_type

    @property
    def shared_count(self):
        r"""Gets the shared_count of this DasConnInfo.

        共享用户数

        :return: The shared_count of this DasConnInfo.
        :rtype: int
        """
        return self._shared_count

    @shared_count.setter
    def shared_count(self, shared_count):
        r"""Sets the shared_count of this DasConnInfo.

        共享用户数

        :param shared_count: The shared_count of this DasConnInfo.
        :type shared_count: int
        """
        self._shared_count = shared_count

    @property
    def service_type(self):
        r"""Gets the service_type of this DasConnInfo.

        服务类型

        :return: The service_type of this DasConnInfo.
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        r"""Sets the service_type of this DasConnInfo.

        服务类型

        :param service_type: The service_type of this DasConnInfo.
        :type service_type: str
        """
        self._service_type = service_type

    @property
    def shared_user_name(self):
        r"""Gets the shared_user_name of this DasConnInfo.

        共享人名称

        :return: The shared_user_name of this DasConnInfo.
        :rtype: str
        """
        return self._shared_user_name

    @shared_user_name.setter
    def shared_user_name(self, shared_user_name):
        r"""Sets the shared_user_name of this DasConnInfo.

        共享人名称

        :param shared_user_name: The shared_user_name of this DasConnInfo.
        :type shared_user_name: str
        """
        self._shared_user_name = shared_user_name

    @property
    def shared_user_id(self):
        r"""Gets the shared_user_id of this DasConnInfo.

        共享人ID

        :return: The shared_user_id of this DasConnInfo.
        :rtype: str
        """
        return self._shared_user_id

    @shared_user_id.setter
    def shared_user_id(self, shared_user_id):
        r"""Sets the shared_user_id of this DasConnInfo.

        共享人ID

        :param shared_user_id: The shared_user_id of this DasConnInfo.
        :type shared_user_id: str
        """
        self._shared_user_id = shared_user_id

    @property
    def expired_time(self):
        r"""Gets the expired_time of this DasConnInfo.

        共享过期时间

        :return: The expired_time of this DasConnInfo.
        :rtype: int
        """
        return self._expired_time

    @expired_time.setter
    def expired_time(self, expired_time):
        r"""Sets the expired_time of this DasConnInfo.

        共享过期时间

        :param expired_time: The expired_time of this DasConnInfo.
        :type expired_time: int
        """
        self._expired_time = expired_time

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
        if not isinstance(other, DasConnInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
