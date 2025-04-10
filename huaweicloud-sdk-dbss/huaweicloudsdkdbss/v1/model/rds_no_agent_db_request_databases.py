# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RdsNoAgentDbRequestDatabases:

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
        'version': 'str',
        'type': 'str',
        'enterprise_id': 'str',
        'enterprise_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'db_name': 'db_name',
        'status': 'status',
        'port': 'port',
        'ip': 'ip',
        'instance_name': 'instance_name',
        'version': 'version',
        'type': 'type',
        'enterprise_id': 'enterprise_id',
        'enterprise_name': 'enterprise_name'
    }

    def __init__(self, id=None, db_name=None, status=None, port=None, ip=None, instance_name=None, version=None, type=None, enterprise_id=None, enterprise_name=None):
        r"""RdsNoAgentDbRequestDatabases

        The model defined in huaweicloud sdk

        :param id: 数据库ID
        :type id: str
        :param db_name: 数据库名称
        :type db_name: str
        :param status: 数据库状态
        :type status: str
        :param port: 数据库端口
        :type port: str
        :param ip: 数据库IP
        :type ip: str
        :param instance_name: 数据库实例名称
        :type instance_name: str
        :param version: 数据库版本
        :type version: str
        :param type: 数据库类型
        :type type: str
        :param enterprise_id: 企业项目ID
        :type enterprise_id: str
        :param enterprise_name: 企业项目名称
        :type enterprise_name: str
        """
        
        

        self._id = None
        self._db_name = None
        self._status = None
        self._port = None
        self._ip = None
        self._instance_name = None
        self._version = None
        self._type = None
        self._enterprise_id = None
        self._enterprise_name = None
        self.discriminator = None

        self.id = id
        self.db_name = db_name
        self.status = status
        self.port = port
        self.ip = ip
        self.instance_name = instance_name
        self.version = version
        self.type = type
        self.enterprise_id = enterprise_id
        if enterprise_name is not None:
            self.enterprise_name = enterprise_name

    @property
    def id(self):
        r"""Gets the id of this RdsNoAgentDbRequestDatabases.

        数据库ID

        :return: The id of this RdsNoAgentDbRequestDatabases.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this RdsNoAgentDbRequestDatabases.

        数据库ID

        :param id: The id of this RdsNoAgentDbRequestDatabases.
        :type id: str
        """
        self._id = id

    @property
    def db_name(self):
        r"""Gets the db_name of this RdsNoAgentDbRequestDatabases.

        数据库名称

        :return: The db_name of this RdsNoAgentDbRequestDatabases.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        r"""Sets the db_name of this RdsNoAgentDbRequestDatabases.

        数据库名称

        :param db_name: The db_name of this RdsNoAgentDbRequestDatabases.
        :type db_name: str
        """
        self._db_name = db_name

    @property
    def status(self):
        r"""Gets the status of this RdsNoAgentDbRequestDatabases.

        数据库状态

        :return: The status of this RdsNoAgentDbRequestDatabases.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this RdsNoAgentDbRequestDatabases.

        数据库状态

        :param status: The status of this RdsNoAgentDbRequestDatabases.
        :type status: str
        """
        self._status = status

    @property
    def port(self):
        r"""Gets the port of this RdsNoAgentDbRequestDatabases.

        数据库端口

        :return: The port of this RdsNoAgentDbRequestDatabases.
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this RdsNoAgentDbRequestDatabases.

        数据库端口

        :param port: The port of this RdsNoAgentDbRequestDatabases.
        :type port: str
        """
        self._port = port

    @property
    def ip(self):
        r"""Gets the ip of this RdsNoAgentDbRequestDatabases.

        数据库IP

        :return: The ip of this RdsNoAgentDbRequestDatabases.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        r"""Sets the ip of this RdsNoAgentDbRequestDatabases.

        数据库IP

        :param ip: The ip of this RdsNoAgentDbRequestDatabases.
        :type ip: str
        """
        self._ip = ip

    @property
    def instance_name(self):
        r"""Gets the instance_name of this RdsNoAgentDbRequestDatabases.

        数据库实例名称

        :return: The instance_name of this RdsNoAgentDbRequestDatabases.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        r"""Sets the instance_name of this RdsNoAgentDbRequestDatabases.

        数据库实例名称

        :param instance_name: The instance_name of this RdsNoAgentDbRequestDatabases.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def version(self):
        r"""Gets the version of this RdsNoAgentDbRequestDatabases.

        数据库版本

        :return: The version of this RdsNoAgentDbRequestDatabases.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this RdsNoAgentDbRequestDatabases.

        数据库版本

        :param version: The version of this RdsNoAgentDbRequestDatabases.
        :type version: str
        """
        self._version = version

    @property
    def type(self):
        r"""Gets the type of this RdsNoAgentDbRequestDatabases.

        数据库类型

        :return: The type of this RdsNoAgentDbRequestDatabases.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this RdsNoAgentDbRequestDatabases.

        数据库类型

        :param type: The type of this RdsNoAgentDbRequestDatabases.
        :type type: str
        """
        self._type = type

    @property
    def enterprise_id(self):
        r"""Gets the enterprise_id of this RdsNoAgentDbRequestDatabases.

        企业项目ID

        :return: The enterprise_id of this RdsNoAgentDbRequestDatabases.
        :rtype: str
        """
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, enterprise_id):
        r"""Sets the enterprise_id of this RdsNoAgentDbRequestDatabases.

        企业项目ID

        :param enterprise_id: The enterprise_id of this RdsNoAgentDbRequestDatabases.
        :type enterprise_id: str
        """
        self._enterprise_id = enterprise_id

    @property
    def enterprise_name(self):
        r"""Gets the enterprise_name of this RdsNoAgentDbRequestDatabases.

        企业项目名称

        :return: The enterprise_name of this RdsNoAgentDbRequestDatabases.
        :rtype: str
        """
        return self._enterprise_name

    @enterprise_name.setter
    def enterprise_name(self, enterprise_name):
        r"""Sets the enterprise_name of this RdsNoAgentDbRequestDatabases.

        企业项目名称

        :param enterprise_name: The enterprise_name of this RdsNoAgentDbRequestDatabases.
        :type enterprise_name: str
        """
        self._enterprise_name = enterprise_name

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
        if not isinstance(other, RdsNoAgentDbRequestDatabases):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
