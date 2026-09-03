# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateDbsConnectionRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'engine_type': 'str',
        'instance_id': 'str',
        'network_type': 'str',
        'username': 'str',
        'is_save_password': 'bool',
        'password': 'str',
        'node_ids': 'list[str]',
        'remarks': 'str',
        'port': 'int',
        'database_name': 'str',
        'sql_record_flag': 'bool'
    }

    attribute_map = {
        'engine_type': 'engine_type',
        'instance_id': 'instance_id',
        'network_type': 'network_type',
        'username': 'username',
        'is_save_password': 'is_save_password',
        'password': 'password',
        'node_ids': 'node_ids',
        'remarks': 'remarks',
        'port': 'port',
        'database_name': 'database_name',
        'sql_record_flag': 'sql_record_flag'
    }

    def __init__(self, engine_type=None, instance_id=None, network_type=None, username=None, is_save_password=None, password=None, node_ids=None, remarks=None, port=None, database_name=None, sql_record_flag=None):
        r"""CreateDbsConnectionRequestBody

        The model defined in huaweicloud sdk

        :param engine_type: 数据库引擎类型，取值范围：mysql, sqlserver, postgresql, taurus, gaussdbv5, mongodb, ddm
        :type engine_type: str
        :param instance_id: 实例ID，实例的唯一标识
        :type instance_id: str
        :param network_type: 数据库来源类型，取值范围：rds, gaussdb, dds, ddm
        :type network_type: str
        :param username: 用户名
        :type username: str
        :param is_save_password: 是否保存密码
        :type is_save_password: bool
        :param password: 密码
        :type password: str
        :param node_ids: 节点ID列表，实例节点的唯一标识
        :type node_ids: list[str]
        :param remarks: 备注
        :type remarks: str
        :param port: 端口，取值范围：[1,65536]
        :type port: int
        :param database_name: 数据库名字
        :type database_name: str
        :param sql_record_flag: SQL记录开关
        :type sql_record_flag: bool
        """
        
        

        self._engine_type = None
        self._instance_id = None
        self._network_type = None
        self._username = None
        self._is_save_password = None
        self._password = None
        self._node_ids = None
        self._remarks = None
        self._port = None
        self._database_name = None
        self._sql_record_flag = None
        self.discriminator = None

        self.engine_type = engine_type
        self.instance_id = instance_id
        self.network_type = network_type
        self.username = username
        self.is_save_password = is_save_password
        self.password = password
        if node_ids is not None:
            self.node_ids = node_ids
        if remarks is not None:
            self.remarks = remarks
        if port is not None:
            self.port = port
        if database_name is not None:
            self.database_name = database_name
        if sql_record_flag is not None:
            self.sql_record_flag = sql_record_flag

    @property
    def engine_type(self):
        r"""Gets the engine_type of this CreateDbsConnectionRequestBody.

        数据库引擎类型，取值范围：mysql, sqlserver, postgresql, taurus, gaussdbv5, mongodb, ddm

        :return: The engine_type of this CreateDbsConnectionRequestBody.
        :rtype: str
        """
        return self._engine_type

    @engine_type.setter
    def engine_type(self, engine_type):
        r"""Sets the engine_type of this CreateDbsConnectionRequestBody.

        数据库引擎类型，取值范围：mysql, sqlserver, postgresql, taurus, gaussdbv5, mongodb, ddm

        :param engine_type: The engine_type of this CreateDbsConnectionRequestBody.
        :type engine_type: str
        """
        self._engine_type = engine_type

    @property
    def instance_id(self):
        r"""Gets the instance_id of this CreateDbsConnectionRequestBody.

        实例ID，实例的唯一标识

        :return: The instance_id of this CreateDbsConnectionRequestBody.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this CreateDbsConnectionRequestBody.

        实例ID，实例的唯一标识

        :param instance_id: The instance_id of this CreateDbsConnectionRequestBody.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def network_type(self):
        r"""Gets the network_type of this CreateDbsConnectionRequestBody.

        数据库来源类型，取值范围：rds, gaussdb, dds, ddm

        :return: The network_type of this CreateDbsConnectionRequestBody.
        :rtype: str
        """
        return self._network_type

    @network_type.setter
    def network_type(self, network_type):
        r"""Sets the network_type of this CreateDbsConnectionRequestBody.

        数据库来源类型，取值范围：rds, gaussdb, dds, ddm

        :param network_type: The network_type of this CreateDbsConnectionRequestBody.
        :type network_type: str
        """
        self._network_type = network_type

    @property
    def username(self):
        r"""Gets the username of this CreateDbsConnectionRequestBody.

        用户名

        :return: The username of this CreateDbsConnectionRequestBody.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        r"""Sets the username of this CreateDbsConnectionRequestBody.

        用户名

        :param username: The username of this CreateDbsConnectionRequestBody.
        :type username: str
        """
        self._username = username

    @property
    def is_save_password(self):
        r"""Gets the is_save_password of this CreateDbsConnectionRequestBody.

        是否保存密码

        :return: The is_save_password of this CreateDbsConnectionRequestBody.
        :rtype: bool
        """
        return self._is_save_password

    @is_save_password.setter
    def is_save_password(self, is_save_password):
        r"""Sets the is_save_password of this CreateDbsConnectionRequestBody.

        是否保存密码

        :param is_save_password: The is_save_password of this CreateDbsConnectionRequestBody.
        :type is_save_password: bool
        """
        self._is_save_password = is_save_password

    @property
    def password(self):
        r"""Gets the password of this CreateDbsConnectionRequestBody.

        密码

        :return: The password of this CreateDbsConnectionRequestBody.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        r"""Sets the password of this CreateDbsConnectionRequestBody.

        密码

        :param password: The password of this CreateDbsConnectionRequestBody.
        :type password: str
        """
        self._password = password

    @property
    def node_ids(self):
        r"""Gets the node_ids of this CreateDbsConnectionRequestBody.

        节点ID列表，实例节点的唯一标识

        :return: The node_ids of this CreateDbsConnectionRequestBody.
        :rtype: list[str]
        """
        return self._node_ids

    @node_ids.setter
    def node_ids(self, node_ids):
        r"""Sets the node_ids of this CreateDbsConnectionRequestBody.

        节点ID列表，实例节点的唯一标识

        :param node_ids: The node_ids of this CreateDbsConnectionRequestBody.
        :type node_ids: list[str]
        """
        self._node_ids = node_ids

    @property
    def remarks(self):
        r"""Gets the remarks of this CreateDbsConnectionRequestBody.

        备注

        :return: The remarks of this CreateDbsConnectionRequestBody.
        :rtype: str
        """
        return self._remarks

    @remarks.setter
    def remarks(self, remarks):
        r"""Sets the remarks of this CreateDbsConnectionRequestBody.

        备注

        :param remarks: The remarks of this CreateDbsConnectionRequestBody.
        :type remarks: str
        """
        self._remarks = remarks

    @property
    def port(self):
        r"""Gets the port of this CreateDbsConnectionRequestBody.

        端口，取值范围：[1,65536]

        :return: The port of this CreateDbsConnectionRequestBody.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this CreateDbsConnectionRequestBody.

        端口，取值范围：[1,65536]

        :param port: The port of this CreateDbsConnectionRequestBody.
        :type port: int
        """
        self._port = port

    @property
    def database_name(self):
        r"""Gets the database_name of this CreateDbsConnectionRequestBody.

        数据库名字

        :return: The database_name of this CreateDbsConnectionRequestBody.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        r"""Sets the database_name of this CreateDbsConnectionRequestBody.

        数据库名字

        :param database_name: The database_name of this CreateDbsConnectionRequestBody.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def sql_record_flag(self):
        r"""Gets the sql_record_flag of this CreateDbsConnectionRequestBody.

        SQL记录开关

        :return: The sql_record_flag of this CreateDbsConnectionRequestBody.
        :rtype: bool
        """
        return self._sql_record_flag

    @sql_record_flag.setter
    def sql_record_flag(self, sql_record_flag):
        r"""Sets the sql_record_flag of this CreateDbsConnectionRequestBody.

        SQL记录开关

        :param sql_record_flag: The sql_record_flag of this CreateDbsConnectionRequestBody.
        :type sql_record_flag: bool
        """
        self._sql_record_flag = sql_record_flag

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
        if not isinstance(other, CreateDbsConnectionRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
