# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApiListConnectionsInfoRespDasConnInfoList:

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
        'create_at': 'int',
        'status': 'str',
        'conn_share_type': 'str',
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
        'create_at': 'create_at',
        'status': 'status',
        'conn_share_type': 'conn_share_type',
        'shared_user_name': 'shared_user_name',
        'shared_user_id': 'shared_user_id',
        'expired_time': 'expired_time'
    }

    def __init__(self, connection_id=None, instance_id=None, instance_name=None, network_type=None, engine_type=None, datastore_version=None, user_name=None, database_name=None, is_save_password=None, ip_address=None, port=None, remarks=None, create_at=None, status=None, conn_share_type=None, shared_user_name=None, shared_user_id=None, expired_time=None):
        r"""ApiListConnectionsInfoRespDasConnInfoList

        The model defined in huaweicloud sdk

        :param connection_id: 连接Id
        :type connection_id: str
        :param instance_id: 实例Id
        :type instance_id: str
        :param instance_name: 实例名称
        :type instance_name: str
        :param network_type: 数据库来源
        :type network_type: str
        :param engine_type: 数据库引擎
        :type engine_type: str
        :param datastore_version: 数据存储版本
        :type datastore_version: str
        :param user_name: 用户名
        :type user_name: str
        :param database_name: 数据库名称
        :type database_name: str
        :param is_save_password: 是否保存密码
        :type is_save_password: bool
        :param ip_address: ip地址
        :type ip_address: str
        :param port: 端口号
        :type port: int
        :param remarks: 备注
        :type remarks: str
        :param create_at: 连接的创建时间
        :type create_at: int
        :param status: 状态，NORMAL-正常，INSTANCE_DELETE-实例删除
        :type status: str
        :param conn_share_type: 连接类型，NORMAL-正常连接，SHARE-共享连接
        :type conn_share_type: str
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
        self._create_at = None
        self._status = None
        self._conn_share_type = None
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
        if create_at is not None:
            self.create_at = create_at
        if status is not None:
            self.status = status
        if conn_share_type is not None:
            self.conn_share_type = conn_share_type
        if shared_user_name is not None:
            self.shared_user_name = shared_user_name
        if shared_user_id is not None:
            self.shared_user_id = shared_user_id
        if expired_time is not None:
            self.expired_time = expired_time

    @property
    def connection_id(self):
        r"""Gets the connection_id of this ApiListConnectionsInfoRespDasConnInfoList.

        连接Id

        :return: The connection_id of this ApiListConnectionsInfoRespDasConnInfoList.
        :rtype: str
        """
        return self._connection_id

    @connection_id.setter
    def connection_id(self, connection_id):
        r"""Sets the connection_id of this ApiListConnectionsInfoRespDasConnInfoList.

        连接Id

        :param connection_id: The connection_id of this ApiListConnectionsInfoRespDasConnInfoList.
        :type connection_id: str
        """
        self._connection_id = connection_id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ApiListConnectionsInfoRespDasConnInfoList.

        实例Id

        :return: The instance_id of this ApiListConnectionsInfoRespDasConnInfoList.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ApiListConnectionsInfoRespDasConnInfoList.

        实例Id

        :param instance_id: The instance_id of this ApiListConnectionsInfoRespDasConnInfoList.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def instance_name(self):
        r"""Gets the instance_name of this ApiListConnectionsInfoRespDasConnInfoList.

        实例名称

        :return: The instance_name of this ApiListConnectionsInfoRespDasConnInfoList.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        r"""Sets the instance_name of this ApiListConnectionsInfoRespDasConnInfoList.

        实例名称

        :param instance_name: The instance_name of this ApiListConnectionsInfoRespDasConnInfoList.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def network_type(self):
        r"""Gets the network_type of this ApiListConnectionsInfoRespDasConnInfoList.

        数据库来源

        :return: The network_type of this ApiListConnectionsInfoRespDasConnInfoList.
        :rtype: str
        """
        return self._network_type

    @network_type.setter
    def network_type(self, network_type):
        r"""Sets the network_type of this ApiListConnectionsInfoRespDasConnInfoList.

        数据库来源

        :param network_type: The network_type of this ApiListConnectionsInfoRespDasConnInfoList.
        :type network_type: str
        """
        self._network_type = network_type

    @property
    def engine_type(self):
        r"""Gets the engine_type of this ApiListConnectionsInfoRespDasConnInfoList.

        数据库引擎

        :return: The engine_type of this ApiListConnectionsInfoRespDasConnInfoList.
        :rtype: str
        """
        return self._engine_type

    @engine_type.setter
    def engine_type(self, engine_type):
        r"""Sets the engine_type of this ApiListConnectionsInfoRespDasConnInfoList.

        数据库引擎

        :param engine_type: The engine_type of this ApiListConnectionsInfoRespDasConnInfoList.
        :type engine_type: str
        """
        self._engine_type = engine_type

    @property
    def datastore_version(self):
        r"""Gets the datastore_version of this ApiListConnectionsInfoRespDasConnInfoList.

        数据存储版本

        :return: The datastore_version of this ApiListConnectionsInfoRespDasConnInfoList.
        :rtype: str
        """
        return self._datastore_version

    @datastore_version.setter
    def datastore_version(self, datastore_version):
        r"""Sets the datastore_version of this ApiListConnectionsInfoRespDasConnInfoList.

        数据存储版本

        :param datastore_version: The datastore_version of this ApiListConnectionsInfoRespDasConnInfoList.
        :type datastore_version: str
        """
        self._datastore_version = datastore_version

    @property
    def user_name(self):
        r"""Gets the user_name of this ApiListConnectionsInfoRespDasConnInfoList.

        用户名

        :return: The user_name of this ApiListConnectionsInfoRespDasConnInfoList.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this ApiListConnectionsInfoRespDasConnInfoList.

        用户名

        :param user_name: The user_name of this ApiListConnectionsInfoRespDasConnInfoList.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def database_name(self):
        r"""Gets the database_name of this ApiListConnectionsInfoRespDasConnInfoList.

        数据库名称

        :return: The database_name of this ApiListConnectionsInfoRespDasConnInfoList.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        r"""Sets the database_name of this ApiListConnectionsInfoRespDasConnInfoList.

        数据库名称

        :param database_name: The database_name of this ApiListConnectionsInfoRespDasConnInfoList.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def is_save_password(self):
        r"""Gets the is_save_password of this ApiListConnectionsInfoRespDasConnInfoList.

        是否保存密码

        :return: The is_save_password of this ApiListConnectionsInfoRespDasConnInfoList.
        :rtype: bool
        """
        return self._is_save_password

    @is_save_password.setter
    def is_save_password(self, is_save_password):
        r"""Sets the is_save_password of this ApiListConnectionsInfoRespDasConnInfoList.

        是否保存密码

        :param is_save_password: The is_save_password of this ApiListConnectionsInfoRespDasConnInfoList.
        :type is_save_password: bool
        """
        self._is_save_password = is_save_password

    @property
    def ip_address(self):
        r"""Gets the ip_address of this ApiListConnectionsInfoRespDasConnInfoList.

        ip地址

        :return: The ip_address of this ApiListConnectionsInfoRespDasConnInfoList.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        r"""Sets the ip_address of this ApiListConnectionsInfoRespDasConnInfoList.

        ip地址

        :param ip_address: The ip_address of this ApiListConnectionsInfoRespDasConnInfoList.
        :type ip_address: str
        """
        self._ip_address = ip_address

    @property
    def port(self):
        r"""Gets the port of this ApiListConnectionsInfoRespDasConnInfoList.

        端口号

        :return: The port of this ApiListConnectionsInfoRespDasConnInfoList.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this ApiListConnectionsInfoRespDasConnInfoList.

        端口号

        :param port: The port of this ApiListConnectionsInfoRespDasConnInfoList.
        :type port: int
        """
        self._port = port

    @property
    def remarks(self):
        r"""Gets the remarks of this ApiListConnectionsInfoRespDasConnInfoList.

        备注

        :return: The remarks of this ApiListConnectionsInfoRespDasConnInfoList.
        :rtype: str
        """
        return self._remarks

    @remarks.setter
    def remarks(self, remarks):
        r"""Sets the remarks of this ApiListConnectionsInfoRespDasConnInfoList.

        备注

        :param remarks: The remarks of this ApiListConnectionsInfoRespDasConnInfoList.
        :type remarks: str
        """
        self._remarks = remarks

    @property
    def create_at(self):
        r"""Gets the create_at of this ApiListConnectionsInfoRespDasConnInfoList.

        连接的创建时间

        :return: The create_at of this ApiListConnectionsInfoRespDasConnInfoList.
        :rtype: int
        """
        return self._create_at

    @create_at.setter
    def create_at(self, create_at):
        r"""Sets the create_at of this ApiListConnectionsInfoRespDasConnInfoList.

        连接的创建时间

        :param create_at: The create_at of this ApiListConnectionsInfoRespDasConnInfoList.
        :type create_at: int
        """
        self._create_at = create_at

    @property
    def status(self):
        r"""Gets the status of this ApiListConnectionsInfoRespDasConnInfoList.

        状态，NORMAL-正常，INSTANCE_DELETE-实例删除

        :return: The status of this ApiListConnectionsInfoRespDasConnInfoList.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ApiListConnectionsInfoRespDasConnInfoList.

        状态，NORMAL-正常，INSTANCE_DELETE-实例删除

        :param status: The status of this ApiListConnectionsInfoRespDasConnInfoList.
        :type status: str
        """
        self._status = status

    @property
    def conn_share_type(self):
        r"""Gets the conn_share_type of this ApiListConnectionsInfoRespDasConnInfoList.

        连接类型，NORMAL-正常连接，SHARE-共享连接

        :return: The conn_share_type of this ApiListConnectionsInfoRespDasConnInfoList.
        :rtype: str
        """
        return self._conn_share_type

    @conn_share_type.setter
    def conn_share_type(self, conn_share_type):
        r"""Sets the conn_share_type of this ApiListConnectionsInfoRespDasConnInfoList.

        连接类型，NORMAL-正常连接，SHARE-共享连接

        :param conn_share_type: The conn_share_type of this ApiListConnectionsInfoRespDasConnInfoList.
        :type conn_share_type: str
        """
        self._conn_share_type = conn_share_type

    @property
    def shared_user_name(self):
        r"""Gets the shared_user_name of this ApiListConnectionsInfoRespDasConnInfoList.

        共享人名称

        :return: The shared_user_name of this ApiListConnectionsInfoRespDasConnInfoList.
        :rtype: str
        """
        return self._shared_user_name

    @shared_user_name.setter
    def shared_user_name(self, shared_user_name):
        r"""Sets the shared_user_name of this ApiListConnectionsInfoRespDasConnInfoList.

        共享人名称

        :param shared_user_name: The shared_user_name of this ApiListConnectionsInfoRespDasConnInfoList.
        :type shared_user_name: str
        """
        self._shared_user_name = shared_user_name

    @property
    def shared_user_id(self):
        r"""Gets the shared_user_id of this ApiListConnectionsInfoRespDasConnInfoList.

        共享人ID

        :return: The shared_user_id of this ApiListConnectionsInfoRespDasConnInfoList.
        :rtype: str
        """
        return self._shared_user_id

    @shared_user_id.setter
    def shared_user_id(self, shared_user_id):
        r"""Sets the shared_user_id of this ApiListConnectionsInfoRespDasConnInfoList.

        共享人ID

        :param shared_user_id: The shared_user_id of this ApiListConnectionsInfoRespDasConnInfoList.
        :type shared_user_id: str
        """
        self._shared_user_id = shared_user_id

    @property
    def expired_time(self):
        r"""Gets the expired_time of this ApiListConnectionsInfoRespDasConnInfoList.

        共享过期时间

        :return: The expired_time of this ApiListConnectionsInfoRespDasConnInfoList.
        :rtype: int
        """
        return self._expired_time

    @expired_time.setter
    def expired_time(self, expired_time):
        r"""Sets the expired_time of this ApiListConnectionsInfoRespDasConnInfoList.

        共享过期时间

        :param expired_time: The expired_time of this ApiListConnectionsInfoRespDasConnInfoList.
        :type expired_time: int
        """
        self._expired_time = expired_time

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
        if not isinstance(other, ApiListConnectionsInfoRespDasConnInfoList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
