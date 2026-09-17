# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModifyConnectionRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'username': 'str',
        'password': 'str',
        'is_save_password': 'bool',
        'node_ids': 'list[str]',
        'remarks': 'str',
        'port': 'int',
        'database_name': 'str',
        'sql_record_flag': 'bool'
    }

    attribute_map = {
        'username': 'username',
        'password': 'password',
        'is_save_password': 'is_save_password',
        'node_ids': 'node_ids',
        'remarks': 'remarks',
        'port': 'port',
        'database_name': 'database_name',
        'sql_record_flag': 'sql_record_flag'
    }

    def __init__(self, username=None, password=None, is_save_password=None, node_ids=None, remarks=None, port=None, database_name=None, sql_record_flag=None):
        r"""ModifyConnectionRequestBody

        The model defined in huaweicloud sdk

        :param username: 用户名
        :type username: str
        :param password: 密码
        :type password: str
        :param is_save_password: 是否保存密码
        :type is_save_password: bool
        :param node_ids: 节点ID列表
        :type node_ids: list[str]
        :param remarks: 备注
        :type remarks: str
        :param port: 端口
        :type port: int
        :param database_name: 数据库名称
        :type database_name: str
        :param sql_record_flag: SQL记录开关
        :type sql_record_flag: bool
        """
        
        

        self._username = None
        self._password = None
        self._is_save_password = None
        self._node_ids = None
        self._remarks = None
        self._port = None
        self._database_name = None
        self._sql_record_flag = None
        self.discriminator = None

        self.username = username
        self.password = password
        self.is_save_password = is_save_password
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
    def username(self):
        r"""Gets the username of this ModifyConnectionRequestBody.

        用户名

        :return: The username of this ModifyConnectionRequestBody.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        r"""Sets the username of this ModifyConnectionRequestBody.

        用户名

        :param username: The username of this ModifyConnectionRequestBody.
        :type username: str
        """
        self._username = username

    @property
    def password(self):
        r"""Gets the password of this ModifyConnectionRequestBody.

        密码

        :return: The password of this ModifyConnectionRequestBody.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        r"""Sets the password of this ModifyConnectionRequestBody.

        密码

        :param password: The password of this ModifyConnectionRequestBody.
        :type password: str
        """
        self._password = password

    @property
    def is_save_password(self):
        r"""Gets the is_save_password of this ModifyConnectionRequestBody.

        是否保存密码

        :return: The is_save_password of this ModifyConnectionRequestBody.
        :rtype: bool
        """
        return self._is_save_password

    @is_save_password.setter
    def is_save_password(self, is_save_password):
        r"""Sets the is_save_password of this ModifyConnectionRequestBody.

        是否保存密码

        :param is_save_password: The is_save_password of this ModifyConnectionRequestBody.
        :type is_save_password: bool
        """
        self._is_save_password = is_save_password

    @property
    def node_ids(self):
        r"""Gets the node_ids of this ModifyConnectionRequestBody.

        节点ID列表

        :return: The node_ids of this ModifyConnectionRequestBody.
        :rtype: list[str]
        """
        return self._node_ids

    @node_ids.setter
    def node_ids(self, node_ids):
        r"""Sets the node_ids of this ModifyConnectionRequestBody.

        节点ID列表

        :param node_ids: The node_ids of this ModifyConnectionRequestBody.
        :type node_ids: list[str]
        """
        self._node_ids = node_ids

    @property
    def remarks(self):
        r"""Gets the remarks of this ModifyConnectionRequestBody.

        备注

        :return: The remarks of this ModifyConnectionRequestBody.
        :rtype: str
        """
        return self._remarks

    @remarks.setter
    def remarks(self, remarks):
        r"""Sets the remarks of this ModifyConnectionRequestBody.

        备注

        :param remarks: The remarks of this ModifyConnectionRequestBody.
        :type remarks: str
        """
        self._remarks = remarks

    @property
    def port(self):
        r"""Gets the port of this ModifyConnectionRequestBody.

        端口

        :return: The port of this ModifyConnectionRequestBody.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this ModifyConnectionRequestBody.

        端口

        :param port: The port of this ModifyConnectionRequestBody.
        :type port: int
        """
        self._port = port

    @property
    def database_name(self):
        r"""Gets the database_name of this ModifyConnectionRequestBody.

        数据库名称

        :return: The database_name of this ModifyConnectionRequestBody.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        r"""Sets the database_name of this ModifyConnectionRequestBody.

        数据库名称

        :param database_name: The database_name of this ModifyConnectionRequestBody.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def sql_record_flag(self):
        r"""Gets the sql_record_flag of this ModifyConnectionRequestBody.

        SQL记录开关

        :return: The sql_record_flag of this ModifyConnectionRequestBody.
        :rtype: bool
        """
        return self._sql_record_flag

    @sql_record_flag.setter
    def sql_record_flag(self, sql_record_flag):
        r"""Sets the sql_record_flag of this ModifyConnectionRequestBody.

        SQL记录开关

        :param sql_record_flag: The sql_record_flag of this ModifyConnectionRequestBody.
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
        if not isinstance(other, ModifyConnectionRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
