# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RdsDbListResponseDatabases:

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
        'db_name': 'str',
        'status': 'str',
        'port': 'str',
        'ip': 'str',
        'instance_name': 'str',
        'type': 'str',
        'version': 'str',
        'is_supported': 'bool',
        'enterprise_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'db_name': 'db_name',
        'status': 'status',
        'port': 'port',
        'ip': 'ip',
        'instance_name': 'instance_name',
        'type': 'type',
        'version': 'version',
        'is_supported': 'is_supported',
        'enterprise_id': 'enterprise_id'
    }

    def __init__(self, id=None, db_name=None, status=None, port=None, ip=None, instance_name=None, type=None, version=None, is_supported=None, enterprise_id=None):
        r"""RdsDbListResponseDatabases

        The model defined in huaweicloud sdk

        :param id: ID
        :type id: str
        :param db_name: 数据库名称
        :type db_name: str
        :param status: 实例状态。 - BUILD：表示实例正在创建。 - ACTIVE：表示实例正常。 - FAILED：表示实例异常。 - FROZEN：表示实例冻结。 - MODIFYING：表示实例正在扩容。 - REBOOTING：表示实例正在重启。 - RESTORING：表示实例正在恢复。 - MODIFYING INSTANCE TYPE：表示实例正在转主备。 - SWITCHOVER：表示实例正在主备切换。 - MIGRATING：表示实例正在迁移。 - BACKING UP：表示实例正在进行备份。 - MODIFYING DATABASE PORT：表示实例正在修改数据库端口。 - STORAGE FULL：表示实例磁盘空间满。
        :type status: str
        :param port: 数据库端口
        :type port: str
        :param ip: 数据库IP
        :type ip: str
        :param instance_name: rds实例名称
        :type instance_name: str
        :param type: 数据库类型 - MYSQL - ORACLE - POSTGRESQL - SQLSERVER - DAMENG - TAURUS - DWS - KINGBASE - MARIADB - GAUSSDBOPENGAUSS
        :type type: str
        :param version: 版本
        :type version: str
        :param is_supported: 是否支持免agent审计
        :type is_supported: bool
        :param enterprise_id: 企业项目ID
        :type enterprise_id: str
        """
        
        

        self._id = None
        self._db_name = None
        self._status = None
        self._port = None
        self._ip = None
        self._instance_name = None
        self._type = None
        self._version = None
        self._is_supported = None
        self._enterprise_id = None
        self.discriminator = None

        self.id = id
        self.db_name = db_name
        self.status = status
        self.port = port
        self.ip = ip
        if instance_name is not None:
            self.instance_name = instance_name
        self.type = type
        self.version = version
        self.is_supported = is_supported
        if enterprise_id is not None:
            self.enterprise_id = enterprise_id

    @property
    def id(self):
        r"""Gets the id of this RdsDbListResponseDatabases.

        ID

        :return: The id of this RdsDbListResponseDatabases.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this RdsDbListResponseDatabases.

        ID

        :param id: The id of this RdsDbListResponseDatabases.
        :type id: str
        """
        self._id = id

    @property
    def db_name(self):
        r"""Gets the db_name of this RdsDbListResponseDatabases.

        数据库名称

        :return: The db_name of this RdsDbListResponseDatabases.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        r"""Sets the db_name of this RdsDbListResponseDatabases.

        数据库名称

        :param db_name: The db_name of this RdsDbListResponseDatabases.
        :type db_name: str
        """
        self._db_name = db_name

    @property
    def status(self):
        r"""Gets the status of this RdsDbListResponseDatabases.

        实例状态。 - BUILD：表示实例正在创建。 - ACTIVE：表示实例正常。 - FAILED：表示实例异常。 - FROZEN：表示实例冻结。 - MODIFYING：表示实例正在扩容。 - REBOOTING：表示实例正在重启。 - RESTORING：表示实例正在恢复。 - MODIFYING INSTANCE TYPE：表示实例正在转主备。 - SWITCHOVER：表示实例正在主备切换。 - MIGRATING：表示实例正在迁移。 - BACKING UP：表示实例正在进行备份。 - MODIFYING DATABASE PORT：表示实例正在修改数据库端口。 - STORAGE FULL：表示实例磁盘空间满。

        :return: The status of this RdsDbListResponseDatabases.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this RdsDbListResponseDatabases.

        实例状态。 - BUILD：表示实例正在创建。 - ACTIVE：表示实例正常。 - FAILED：表示实例异常。 - FROZEN：表示实例冻结。 - MODIFYING：表示实例正在扩容。 - REBOOTING：表示实例正在重启。 - RESTORING：表示实例正在恢复。 - MODIFYING INSTANCE TYPE：表示实例正在转主备。 - SWITCHOVER：表示实例正在主备切换。 - MIGRATING：表示实例正在迁移。 - BACKING UP：表示实例正在进行备份。 - MODIFYING DATABASE PORT：表示实例正在修改数据库端口。 - STORAGE FULL：表示实例磁盘空间满。

        :param status: The status of this RdsDbListResponseDatabases.
        :type status: str
        """
        self._status = status

    @property
    def port(self):
        r"""Gets the port of this RdsDbListResponseDatabases.

        数据库端口

        :return: The port of this RdsDbListResponseDatabases.
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this RdsDbListResponseDatabases.

        数据库端口

        :param port: The port of this RdsDbListResponseDatabases.
        :type port: str
        """
        self._port = port

    @property
    def ip(self):
        r"""Gets the ip of this RdsDbListResponseDatabases.

        数据库IP

        :return: The ip of this RdsDbListResponseDatabases.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        r"""Sets the ip of this RdsDbListResponseDatabases.

        数据库IP

        :param ip: The ip of this RdsDbListResponseDatabases.
        :type ip: str
        """
        self._ip = ip

    @property
    def instance_name(self):
        r"""Gets the instance_name of this RdsDbListResponseDatabases.

        rds实例名称

        :return: The instance_name of this RdsDbListResponseDatabases.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        r"""Sets the instance_name of this RdsDbListResponseDatabases.

        rds实例名称

        :param instance_name: The instance_name of this RdsDbListResponseDatabases.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def type(self):
        r"""Gets the type of this RdsDbListResponseDatabases.

        数据库类型 - MYSQL - ORACLE - POSTGRESQL - SQLSERVER - DAMENG - TAURUS - DWS - KINGBASE - MARIADB - GAUSSDBOPENGAUSS

        :return: The type of this RdsDbListResponseDatabases.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this RdsDbListResponseDatabases.

        数据库类型 - MYSQL - ORACLE - POSTGRESQL - SQLSERVER - DAMENG - TAURUS - DWS - KINGBASE - MARIADB - GAUSSDBOPENGAUSS

        :param type: The type of this RdsDbListResponseDatabases.
        :type type: str
        """
        self._type = type

    @property
    def version(self):
        r"""Gets the version of this RdsDbListResponseDatabases.

        版本

        :return: The version of this RdsDbListResponseDatabases.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this RdsDbListResponseDatabases.

        版本

        :param version: The version of this RdsDbListResponseDatabases.
        :type version: str
        """
        self._version = version

    @property
    def is_supported(self):
        r"""Gets the is_supported of this RdsDbListResponseDatabases.

        是否支持免agent审计

        :return: The is_supported of this RdsDbListResponseDatabases.
        :rtype: bool
        """
        return self._is_supported

    @is_supported.setter
    def is_supported(self, is_supported):
        r"""Sets the is_supported of this RdsDbListResponseDatabases.

        是否支持免agent审计

        :param is_supported: The is_supported of this RdsDbListResponseDatabases.
        :type is_supported: bool
        """
        self._is_supported = is_supported

    @property
    def enterprise_id(self):
        r"""Gets the enterprise_id of this RdsDbListResponseDatabases.

        企业项目ID

        :return: The enterprise_id of this RdsDbListResponseDatabases.
        :rtype: str
        """
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, enterprise_id):
        r"""Sets the enterprise_id of this RdsDbListResponseDatabases.

        企业项目ID

        :param enterprise_id: The enterprise_id of this RdsDbListResponseDatabases.
        :type enterprise_id: str
        """
        self._enterprise_id = enterprise_id

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
        if not isinstance(other, RdsDbListResponseDatabases):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
