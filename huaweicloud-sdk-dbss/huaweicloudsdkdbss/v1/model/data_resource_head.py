# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DataResourceHead:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alias': 'str',
        'datastore': 'DbDataStore',
        'db_ip': 'str',
        'db_name': 'str',
        'db_port': 'str',
        'db_user_list': 'list[DbUser]',
        'provider': 'str',
        'rds_id': 'str',
        'status': 'str',
        'type': 'str'
    }

    attribute_map = {
        'alias': 'alias',
        'datastore': 'datastore',
        'db_ip': 'db_ip',
        'db_name': 'db_name',
        'db_port': 'db_port',
        'db_user_list': 'db_user_list',
        'provider': 'provider',
        'rds_id': 'rds_id',
        'status': 'status',
        'type': 'type'
    }

    def __init__(self, alias=None, datastore=None, db_ip=None, db_name=None, db_port=None, db_user_list=None, provider=None, rds_id=None, status=None, type=None):
        r"""DataResourceHead

        The model defined in huaweicloud sdk

        :param alias: 数据库实例别名
        :type alias: str
        :param datastore: 
        :type datastore: :class:`huaweicloudsdkdbss.v1.DbDataStore`
        :param db_ip: 数据库IP
        :type db_ip: str
        :param db_name: 数据库名称
        :type db_name: str
        :param db_port: 数据库端口
        :type db_port: str
        :param db_user_list: 数据库用户列表
        :type db_user_list: list[:class:`huaweicloudsdkdbss.v1.DbUser`]
        :param provider: 云服务名称，云上数据库服务，如：rds
        :type provider: str
        :param rds_id: rds数据库ID
        :type rds_id: str
        :param status: 数据库状态
        :type status: str
        :param type: 数据库类型
        :type type: str
        """
        
        

        self._alias = None
        self._datastore = None
        self._db_ip = None
        self._db_name = None
        self._db_port = None
        self._db_user_list = None
        self._provider = None
        self._rds_id = None
        self._status = None
        self._type = None
        self.discriminator = None

        if alias is not None:
            self.alias = alias
        if datastore is not None:
            self.datastore = datastore
        if db_ip is not None:
            self.db_ip = db_ip
        if db_name is not None:
            self.db_name = db_name
        if db_port is not None:
            self.db_port = db_port
        if db_user_list is not None:
            self.db_user_list = db_user_list
        if provider is not None:
            self.provider = provider
        if rds_id is not None:
            self.rds_id = rds_id
        if status is not None:
            self.status = status
        if type is not None:
            self.type = type

    @property
    def alias(self):
        r"""Gets the alias of this DataResourceHead.

        数据库实例别名

        :return: The alias of this DataResourceHead.
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        r"""Sets the alias of this DataResourceHead.

        数据库实例别名

        :param alias: The alias of this DataResourceHead.
        :type alias: str
        """
        self._alias = alias

    @property
    def datastore(self):
        r"""Gets the datastore of this DataResourceHead.

        :return: The datastore of this DataResourceHead.
        :rtype: :class:`huaweicloudsdkdbss.v1.DbDataStore`
        """
        return self._datastore

    @datastore.setter
    def datastore(self, datastore):
        r"""Sets the datastore of this DataResourceHead.

        :param datastore: The datastore of this DataResourceHead.
        :type datastore: :class:`huaweicloudsdkdbss.v1.DbDataStore`
        """
        self._datastore = datastore

    @property
    def db_ip(self):
        r"""Gets the db_ip of this DataResourceHead.

        数据库IP

        :return: The db_ip of this DataResourceHead.
        :rtype: str
        """
        return self._db_ip

    @db_ip.setter
    def db_ip(self, db_ip):
        r"""Sets the db_ip of this DataResourceHead.

        数据库IP

        :param db_ip: The db_ip of this DataResourceHead.
        :type db_ip: str
        """
        self._db_ip = db_ip

    @property
    def db_name(self):
        r"""Gets the db_name of this DataResourceHead.

        数据库名称

        :return: The db_name of this DataResourceHead.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        r"""Sets the db_name of this DataResourceHead.

        数据库名称

        :param db_name: The db_name of this DataResourceHead.
        :type db_name: str
        """
        self._db_name = db_name

    @property
    def db_port(self):
        r"""Gets the db_port of this DataResourceHead.

        数据库端口

        :return: The db_port of this DataResourceHead.
        :rtype: str
        """
        return self._db_port

    @db_port.setter
    def db_port(self, db_port):
        r"""Sets the db_port of this DataResourceHead.

        数据库端口

        :param db_port: The db_port of this DataResourceHead.
        :type db_port: str
        """
        self._db_port = db_port

    @property
    def db_user_list(self):
        r"""Gets the db_user_list of this DataResourceHead.

        数据库用户列表

        :return: The db_user_list of this DataResourceHead.
        :rtype: list[:class:`huaweicloudsdkdbss.v1.DbUser`]
        """
        return self._db_user_list

    @db_user_list.setter
    def db_user_list(self, db_user_list):
        r"""Sets the db_user_list of this DataResourceHead.

        数据库用户列表

        :param db_user_list: The db_user_list of this DataResourceHead.
        :type db_user_list: list[:class:`huaweicloudsdkdbss.v1.DbUser`]
        """
        self._db_user_list = db_user_list

    @property
    def provider(self):
        r"""Gets the provider of this DataResourceHead.

        云服务名称，云上数据库服务，如：rds

        :return: The provider of this DataResourceHead.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        r"""Sets the provider of this DataResourceHead.

        云服务名称，云上数据库服务，如：rds

        :param provider: The provider of this DataResourceHead.
        :type provider: str
        """
        self._provider = provider

    @property
    def rds_id(self):
        r"""Gets the rds_id of this DataResourceHead.

        rds数据库ID

        :return: The rds_id of this DataResourceHead.
        :rtype: str
        """
        return self._rds_id

    @rds_id.setter
    def rds_id(self, rds_id):
        r"""Sets the rds_id of this DataResourceHead.

        rds数据库ID

        :param rds_id: The rds_id of this DataResourceHead.
        :type rds_id: str
        """
        self._rds_id = rds_id

    @property
    def status(self):
        r"""Gets the status of this DataResourceHead.

        数据库状态

        :return: The status of this DataResourceHead.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this DataResourceHead.

        数据库状态

        :param status: The status of this DataResourceHead.
        :type status: str
        """
        self._status = status

    @property
    def type(self):
        r"""Gets the type of this DataResourceHead.

        数据库类型

        :return: The type of this DataResourceHead.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this DataResourceHead.

        数据库类型

        :param type: The type of this DataResourceHead.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, DataResourceHead):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
