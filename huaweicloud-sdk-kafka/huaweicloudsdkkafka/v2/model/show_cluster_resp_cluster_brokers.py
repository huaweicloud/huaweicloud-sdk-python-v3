# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowClusterRespClusterBrokers:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'host': 'str',
        'port': 'int',
        'broker_id': 'str',
        'is_controller': 'bool',
        'version': 'str',
        'register_time': 'int',
        'is_health': 'bool'
    }

    attribute_map = {
        'host': 'host',
        'port': 'port',
        'broker_id': 'broker_id',
        'is_controller': 'is_controller',
        'version': 'version',
        'register_time': 'register_time',
        'is_health': 'is_health'
    }

    def __init__(self, host=None, port=None, broker_id=None, is_controller=None, version=None, register_time=None, is_health=None):
        """ShowClusterRespClusterBrokers

        The model defined in huaweicloud sdk

        :param host: 节点IP。
        :type host: str
        :param port: 端口号。
        :type port: int
        :param broker_id: 节点ID。
        :type broker_id: str
        :param is_controller: 是否为contoller节点。
        :type is_controller: bool
        :param version: 服务端版本。
        :type version: str
        :param register_time: broker注册时间，为unix时间戳格式。
        :type register_time: int
        :param is_health: Kafka实例节点的连通性是否正常。
        :type is_health: bool
        """
        
        

        self._host = None
        self._port = None
        self._broker_id = None
        self._is_controller = None
        self._version = None
        self._register_time = None
        self._is_health = None
        self.discriminator = None

        if host is not None:
            self.host = host
        if port is not None:
            self.port = port
        if broker_id is not None:
            self.broker_id = broker_id
        if is_controller is not None:
            self.is_controller = is_controller
        if version is not None:
            self.version = version
        if register_time is not None:
            self.register_time = register_time
        if is_health is not None:
            self.is_health = is_health

    @property
    def host(self):
        """Gets the host of this ShowClusterRespClusterBrokers.

        节点IP。

        :return: The host of this ShowClusterRespClusterBrokers.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this ShowClusterRespClusterBrokers.

        节点IP。

        :param host: The host of this ShowClusterRespClusterBrokers.
        :type host: str
        """
        self._host = host

    @property
    def port(self):
        """Gets the port of this ShowClusterRespClusterBrokers.

        端口号。

        :return: The port of this ShowClusterRespClusterBrokers.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this ShowClusterRespClusterBrokers.

        端口号。

        :param port: The port of this ShowClusterRespClusterBrokers.
        :type port: int
        """
        self._port = port

    @property
    def broker_id(self):
        """Gets the broker_id of this ShowClusterRespClusterBrokers.

        节点ID。

        :return: The broker_id of this ShowClusterRespClusterBrokers.
        :rtype: str
        """
        return self._broker_id

    @broker_id.setter
    def broker_id(self, broker_id):
        """Sets the broker_id of this ShowClusterRespClusterBrokers.

        节点ID。

        :param broker_id: The broker_id of this ShowClusterRespClusterBrokers.
        :type broker_id: str
        """
        self._broker_id = broker_id

    @property
    def is_controller(self):
        """Gets the is_controller of this ShowClusterRespClusterBrokers.

        是否为contoller节点。

        :return: The is_controller of this ShowClusterRespClusterBrokers.
        :rtype: bool
        """
        return self._is_controller

    @is_controller.setter
    def is_controller(self, is_controller):
        """Sets the is_controller of this ShowClusterRespClusterBrokers.

        是否为contoller节点。

        :param is_controller: The is_controller of this ShowClusterRespClusterBrokers.
        :type is_controller: bool
        """
        self._is_controller = is_controller

    @property
    def version(self):
        """Gets the version of this ShowClusterRespClusterBrokers.

        服务端版本。

        :return: The version of this ShowClusterRespClusterBrokers.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ShowClusterRespClusterBrokers.

        服务端版本。

        :param version: The version of this ShowClusterRespClusterBrokers.
        :type version: str
        """
        self._version = version

    @property
    def register_time(self):
        """Gets the register_time of this ShowClusterRespClusterBrokers.

        broker注册时间，为unix时间戳格式。

        :return: The register_time of this ShowClusterRespClusterBrokers.
        :rtype: int
        """
        return self._register_time

    @register_time.setter
    def register_time(self, register_time):
        """Sets the register_time of this ShowClusterRespClusterBrokers.

        broker注册时间，为unix时间戳格式。

        :param register_time: The register_time of this ShowClusterRespClusterBrokers.
        :type register_time: int
        """
        self._register_time = register_time

    @property
    def is_health(self):
        """Gets the is_health of this ShowClusterRespClusterBrokers.

        Kafka实例节点的连通性是否正常。

        :return: The is_health of this ShowClusterRespClusterBrokers.
        :rtype: bool
        """
        return self._is_health

    @is_health.setter
    def is_health(self, is_health):
        """Sets the is_health of this ShowClusterRespClusterBrokers.

        Kafka实例节点的连通性是否正常。

        :param is_health: The is_health of this ShowClusterRespClusterBrokers.
        :type is_health: bool
        """
        self._is_health = is_health

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
        if not isinstance(other, ShowClusterRespClusterBrokers):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
