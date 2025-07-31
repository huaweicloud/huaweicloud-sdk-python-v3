# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class KubernetesServicePortInfo:

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
        'service_id': 'str',
        'name': 'str',
        'protocol': 'str',
        'port': 'int',
        'target_port': 'str',
        'node_port': 'int'
    }

    attribute_map = {
        'id': 'id',
        'service_id': 'service_id',
        'name': 'name',
        'protocol': 'protocol',
        'port': 'port',
        'target_port': 'target_port',
        'node_port': 'node_port'
    }

    def __init__(self, id=None, service_id=None, name=None, protocol=None, port=None, target_port=None, node_port=None):
        r"""KubernetesServicePortInfo

        The model defined in huaweicloud sdk

        :param id: ID
        :type id: str
        :param service_id: 关联服务 ID
        :type service_id: str
        :param name: 端口名
        :type name: str
        :param protocol: 服务协议
        :type protocol: str
        :param port: 端口号
        :type port: int
        :param target_port: 后端容器端口
        :type target_port: str
        :param node_port: 节点端口
        :type node_port: int
        """
        
        

        self._id = None
        self._service_id = None
        self._name = None
        self._protocol = None
        self._port = None
        self._target_port = None
        self._node_port = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if service_id is not None:
            self.service_id = service_id
        if name is not None:
            self.name = name
        if protocol is not None:
            self.protocol = protocol
        if port is not None:
            self.port = port
        if target_port is not None:
            self.target_port = target_port
        if node_port is not None:
            self.node_port = node_port

    @property
    def id(self):
        r"""Gets the id of this KubernetesServicePortInfo.

        ID

        :return: The id of this KubernetesServicePortInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this KubernetesServicePortInfo.

        ID

        :param id: The id of this KubernetesServicePortInfo.
        :type id: str
        """
        self._id = id

    @property
    def service_id(self):
        r"""Gets the service_id of this KubernetesServicePortInfo.

        关联服务 ID

        :return: The service_id of this KubernetesServicePortInfo.
        :rtype: str
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        r"""Sets the service_id of this KubernetesServicePortInfo.

        关联服务 ID

        :param service_id: The service_id of this KubernetesServicePortInfo.
        :type service_id: str
        """
        self._service_id = service_id

    @property
    def name(self):
        r"""Gets the name of this KubernetesServicePortInfo.

        端口名

        :return: The name of this KubernetesServicePortInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this KubernetesServicePortInfo.

        端口名

        :param name: The name of this KubernetesServicePortInfo.
        :type name: str
        """
        self._name = name

    @property
    def protocol(self):
        r"""Gets the protocol of this KubernetesServicePortInfo.

        服务协议

        :return: The protocol of this KubernetesServicePortInfo.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        r"""Sets the protocol of this KubernetesServicePortInfo.

        服务协议

        :param protocol: The protocol of this KubernetesServicePortInfo.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def port(self):
        r"""Gets the port of this KubernetesServicePortInfo.

        端口号

        :return: The port of this KubernetesServicePortInfo.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this KubernetesServicePortInfo.

        端口号

        :param port: The port of this KubernetesServicePortInfo.
        :type port: int
        """
        self._port = port

    @property
    def target_port(self):
        r"""Gets the target_port of this KubernetesServicePortInfo.

        后端容器端口

        :return: The target_port of this KubernetesServicePortInfo.
        :rtype: str
        """
        return self._target_port

    @target_port.setter
    def target_port(self, target_port):
        r"""Sets the target_port of this KubernetesServicePortInfo.

        后端容器端口

        :param target_port: The target_port of this KubernetesServicePortInfo.
        :type target_port: str
        """
        self._target_port = target_port

    @property
    def node_port(self):
        r"""Gets the node_port of this KubernetesServicePortInfo.

        节点端口

        :return: The node_port of this KubernetesServicePortInfo.
        :rtype: int
        """
        return self._node_port

    @node_port.setter
    def node_port(self, node_port):
        r"""Sets the node_port of this KubernetesServicePortInfo.

        节点端口

        :param node_port: The node_port of this KubernetesServicePortInfo.
        :type node_port: int
        """
        self._node_port = node_port

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
        if not isinstance(other, KubernetesServicePortInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
