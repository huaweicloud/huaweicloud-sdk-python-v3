# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateDatabaseRequestDatabase:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'db_classification': 'str',
        'name': 'str',
        'type': 'str',
        'version': 'str',
        'charset': 'str',
        'ip': 'str',
        'port': 'str',
        'os': 'str',
        'instance_name': 'str'
    }

    attribute_map = {
        'db_classification': 'db_classification',
        'name': 'name',
        'type': 'type',
        'version': 'version',
        'charset': 'charset',
        'ip': 'ip',
        'port': 'port',
        'os': 'os',
        'instance_name': 'instance_name'
    }

    def __init__(self, db_classification=None, name=None, type=None, version=None, charset=None, ip=None, port=None, os=None, instance_name=None):
        r"""CreateDatabaseRequestDatabase

        The model defined in huaweicloud sdk

        :param db_classification: 数据库分类 - ECS:自建数据库
        :type db_classification: str
        :param name: 数据库名称
        :type name: str
        :param type: 数据库类型 - MYSQL - ORACLE - POSTGRESQL - SQLSERVER - DAMENG - TAURUS - DWS - KINGBASE - GAUSSDBOPENGAUSS - GREENPLUM - HIGHGO - SHENTONG - GBASE8A - GBASE8S - GBASEXDM - MONGODB - DDS
        :type type: str
        :param version: 数据库版本
        :type version: str
        :param charset: 字符集。 - GBK - UTF8
        :type charset: str
        :param ip: 数据库IP
        :type ip: str
        :param port: 数据库端口
        :type port: str
        :param os: 数据库操作系统 - LINUX64 - WINDOWS64 - UNIX
        :type os: str
        :param instance_name: 数据库实例名称
        :type instance_name: str
        """
        
        

        self._db_classification = None
        self._name = None
        self._type = None
        self._version = None
        self._charset = None
        self._ip = None
        self._port = None
        self._os = None
        self._instance_name = None
        self.discriminator = None

        self.db_classification = db_classification
        self.name = name
        self.type = type
        self.version = version
        self.charset = charset
        self.ip = ip
        self.port = port
        self.os = os
        if instance_name is not None:
            self.instance_name = instance_name

    @property
    def db_classification(self):
        r"""Gets the db_classification of this CreateDatabaseRequestDatabase.

        数据库分类 - ECS:自建数据库

        :return: The db_classification of this CreateDatabaseRequestDatabase.
        :rtype: str
        """
        return self._db_classification

    @db_classification.setter
    def db_classification(self, db_classification):
        r"""Sets the db_classification of this CreateDatabaseRequestDatabase.

        数据库分类 - ECS:自建数据库

        :param db_classification: The db_classification of this CreateDatabaseRequestDatabase.
        :type db_classification: str
        """
        self._db_classification = db_classification

    @property
    def name(self):
        r"""Gets the name of this CreateDatabaseRequestDatabase.

        数据库名称

        :return: The name of this CreateDatabaseRequestDatabase.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateDatabaseRequestDatabase.

        数据库名称

        :param name: The name of this CreateDatabaseRequestDatabase.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this CreateDatabaseRequestDatabase.

        数据库类型 - MYSQL - ORACLE - POSTGRESQL - SQLSERVER - DAMENG - TAURUS - DWS - KINGBASE - GAUSSDBOPENGAUSS - GREENPLUM - HIGHGO - SHENTONG - GBASE8A - GBASE8S - GBASEXDM - MONGODB - DDS

        :return: The type of this CreateDatabaseRequestDatabase.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CreateDatabaseRequestDatabase.

        数据库类型 - MYSQL - ORACLE - POSTGRESQL - SQLSERVER - DAMENG - TAURUS - DWS - KINGBASE - GAUSSDBOPENGAUSS - GREENPLUM - HIGHGO - SHENTONG - GBASE8A - GBASE8S - GBASEXDM - MONGODB - DDS

        :param type: The type of this CreateDatabaseRequestDatabase.
        :type type: str
        """
        self._type = type

    @property
    def version(self):
        r"""Gets the version of this CreateDatabaseRequestDatabase.

        数据库版本

        :return: The version of this CreateDatabaseRequestDatabase.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this CreateDatabaseRequestDatabase.

        数据库版本

        :param version: The version of this CreateDatabaseRequestDatabase.
        :type version: str
        """
        self._version = version

    @property
    def charset(self):
        r"""Gets the charset of this CreateDatabaseRequestDatabase.

        字符集。 - GBK - UTF8

        :return: The charset of this CreateDatabaseRequestDatabase.
        :rtype: str
        """
        return self._charset

    @charset.setter
    def charset(self, charset):
        r"""Sets the charset of this CreateDatabaseRequestDatabase.

        字符集。 - GBK - UTF8

        :param charset: The charset of this CreateDatabaseRequestDatabase.
        :type charset: str
        """
        self._charset = charset

    @property
    def ip(self):
        r"""Gets the ip of this CreateDatabaseRequestDatabase.

        数据库IP

        :return: The ip of this CreateDatabaseRequestDatabase.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        r"""Sets the ip of this CreateDatabaseRequestDatabase.

        数据库IP

        :param ip: The ip of this CreateDatabaseRequestDatabase.
        :type ip: str
        """
        self._ip = ip

    @property
    def port(self):
        r"""Gets the port of this CreateDatabaseRequestDatabase.

        数据库端口

        :return: The port of this CreateDatabaseRequestDatabase.
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this CreateDatabaseRequestDatabase.

        数据库端口

        :param port: The port of this CreateDatabaseRequestDatabase.
        :type port: str
        """
        self._port = port

    @property
    def os(self):
        r"""Gets the os of this CreateDatabaseRequestDatabase.

        数据库操作系统 - LINUX64 - WINDOWS64 - UNIX

        :return: The os of this CreateDatabaseRequestDatabase.
        :rtype: str
        """
        return self._os

    @os.setter
    def os(self, os):
        r"""Sets the os of this CreateDatabaseRequestDatabase.

        数据库操作系统 - LINUX64 - WINDOWS64 - UNIX

        :param os: The os of this CreateDatabaseRequestDatabase.
        :type os: str
        """
        self._os = os

    @property
    def instance_name(self):
        r"""Gets the instance_name of this CreateDatabaseRequestDatabase.

        数据库实例名称

        :return: The instance_name of this CreateDatabaseRequestDatabase.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        r"""Sets the instance_name of this CreateDatabaseRequestDatabase.

        数据库实例名称

        :param instance_name: The instance_name of this CreateDatabaseRequestDatabase.
        :type instance_name: str
        """
        self._instance_name = instance_name

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
        if not isinstance(other, CreateDatabaseRequestDatabase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
