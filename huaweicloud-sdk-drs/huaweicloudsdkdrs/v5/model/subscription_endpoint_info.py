# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SubscriptionEndpointInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'db_instance_id': 'str',
        'name': 'str',
        'ip': 'str',
        'port': 'int',
        'type': 'str',
        'user_name': 'str'
    }

    attribute_map = {
        'db_instance_id': 'db_instance_id',
        'name': 'name',
        'ip': 'ip',
        'port': 'port',
        'type': 'type',
        'user_name': 'user_name'
    }

    def __init__(self, db_instance_id=None, name=None, ip=None, port=None, type=None, user_name=None):
        r"""SubscriptionEndpointInfo

        The model defined in huaweicloud sdk

        :param db_instance_id: 数据库实例id
        :type db_instance_id: str
        :param name: 数据库名称
        :type name: str
        :param ip: 数据库内网ip
        :type ip: str
        :param port: 数据库端口
        :type port: int
        :param type: 数据库类型
        :type type: str
        :param user_name: 数据库用户名
        :type user_name: str
        """
        
        

        self._db_instance_id = None
        self._name = None
        self._ip = None
        self._port = None
        self._type = None
        self._user_name = None
        self.discriminator = None

        self.db_instance_id = db_instance_id
        self.name = name
        self.ip = ip
        self.port = port
        self.type = type
        self.user_name = user_name

    @property
    def db_instance_id(self):
        r"""Gets the db_instance_id of this SubscriptionEndpointInfo.

        数据库实例id

        :return: The db_instance_id of this SubscriptionEndpointInfo.
        :rtype: str
        """
        return self._db_instance_id

    @db_instance_id.setter
    def db_instance_id(self, db_instance_id):
        r"""Sets the db_instance_id of this SubscriptionEndpointInfo.

        数据库实例id

        :param db_instance_id: The db_instance_id of this SubscriptionEndpointInfo.
        :type db_instance_id: str
        """
        self._db_instance_id = db_instance_id

    @property
    def name(self):
        r"""Gets the name of this SubscriptionEndpointInfo.

        数据库名称

        :return: The name of this SubscriptionEndpointInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this SubscriptionEndpointInfo.

        数据库名称

        :param name: The name of this SubscriptionEndpointInfo.
        :type name: str
        """
        self._name = name

    @property
    def ip(self):
        r"""Gets the ip of this SubscriptionEndpointInfo.

        数据库内网ip

        :return: The ip of this SubscriptionEndpointInfo.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        r"""Sets the ip of this SubscriptionEndpointInfo.

        数据库内网ip

        :param ip: The ip of this SubscriptionEndpointInfo.
        :type ip: str
        """
        self._ip = ip

    @property
    def port(self):
        r"""Gets the port of this SubscriptionEndpointInfo.

        数据库端口

        :return: The port of this SubscriptionEndpointInfo.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this SubscriptionEndpointInfo.

        数据库端口

        :param port: The port of this SubscriptionEndpointInfo.
        :type port: int
        """
        self._port = port

    @property
    def type(self):
        r"""Gets the type of this SubscriptionEndpointInfo.

        数据库类型

        :return: The type of this SubscriptionEndpointInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this SubscriptionEndpointInfo.

        数据库类型

        :param type: The type of this SubscriptionEndpointInfo.
        :type type: str
        """
        self._type = type

    @property
    def user_name(self):
        r"""Gets the user_name of this SubscriptionEndpointInfo.

        数据库用户名

        :return: The user_name of this SubscriptionEndpointInfo.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this SubscriptionEndpointInfo.

        数据库用户名

        :param user_name: The user_name of this SubscriptionEndpointInfo.
        :type user_name: str
        """
        self._user_name = user_name

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
        if not isinstance(other, SubscriptionEndpointInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
