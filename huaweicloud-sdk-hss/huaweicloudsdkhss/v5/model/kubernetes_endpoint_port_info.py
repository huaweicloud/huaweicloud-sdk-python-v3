# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class KubernetesEndpointPortInfo:

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
        'endpoint_id': 'str',
        'name': 'str',
        'protocol': 'str',
        'port': 'int',
        'app_protocol': 'str'
    }

    attribute_map = {
        'id': 'id',
        'endpoint_id': 'endpoint_id',
        'name': 'name',
        'protocol': 'protocol',
        'port': 'port',
        'app_protocol': 'app_protocol'
    }

    def __init__(self, id=None, endpoint_id=None, name=None, protocol=None, port=None, app_protocol=None):
        r"""KubernetesEndpointPortInfo

        The model defined in huaweicloud sdk

        :param id: ID
        :type id: str
        :param endpoint_id: 关联端点ID
        :type endpoint_id: str
        :param name: 端口名
        :type name: str
        :param protocol: 服务协议
        :type protocol: str
        :param port: 端口号
        :type port: int
        :param app_protocol: 应用协议
        :type app_protocol: str
        """
        
        

        self._id = None
        self._endpoint_id = None
        self._name = None
        self._protocol = None
        self._port = None
        self._app_protocol = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if endpoint_id is not None:
            self.endpoint_id = endpoint_id
        if name is not None:
            self.name = name
        if protocol is not None:
            self.protocol = protocol
        if port is not None:
            self.port = port
        if app_protocol is not None:
            self.app_protocol = app_protocol

    @property
    def id(self):
        r"""Gets the id of this KubernetesEndpointPortInfo.

        ID

        :return: The id of this KubernetesEndpointPortInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this KubernetesEndpointPortInfo.

        ID

        :param id: The id of this KubernetesEndpointPortInfo.
        :type id: str
        """
        self._id = id

    @property
    def endpoint_id(self):
        r"""Gets the endpoint_id of this KubernetesEndpointPortInfo.

        关联端点ID

        :return: The endpoint_id of this KubernetesEndpointPortInfo.
        :rtype: str
        """
        return self._endpoint_id

    @endpoint_id.setter
    def endpoint_id(self, endpoint_id):
        r"""Sets the endpoint_id of this KubernetesEndpointPortInfo.

        关联端点ID

        :param endpoint_id: The endpoint_id of this KubernetesEndpointPortInfo.
        :type endpoint_id: str
        """
        self._endpoint_id = endpoint_id

    @property
    def name(self):
        r"""Gets the name of this KubernetesEndpointPortInfo.

        端口名

        :return: The name of this KubernetesEndpointPortInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this KubernetesEndpointPortInfo.

        端口名

        :param name: The name of this KubernetesEndpointPortInfo.
        :type name: str
        """
        self._name = name

    @property
    def protocol(self):
        r"""Gets the protocol of this KubernetesEndpointPortInfo.

        服务协议

        :return: The protocol of this KubernetesEndpointPortInfo.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        r"""Sets the protocol of this KubernetesEndpointPortInfo.

        服务协议

        :param protocol: The protocol of this KubernetesEndpointPortInfo.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def port(self):
        r"""Gets the port of this KubernetesEndpointPortInfo.

        端口号

        :return: The port of this KubernetesEndpointPortInfo.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this KubernetesEndpointPortInfo.

        端口号

        :param port: The port of this KubernetesEndpointPortInfo.
        :type port: int
        """
        self._port = port

    @property
    def app_protocol(self):
        r"""Gets the app_protocol of this KubernetesEndpointPortInfo.

        应用协议

        :return: The app_protocol of this KubernetesEndpointPortInfo.
        :rtype: str
        """
        return self._app_protocol

    @app_protocol.setter
    def app_protocol(self, app_protocol):
        r"""Sets the app_protocol of this KubernetesEndpointPortInfo.

        应用协议

        :param app_protocol: The app_protocol of this KubernetesEndpointPortInfo.
        :type app_protocol: str
        """
        self._app_protocol = app_protocol

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
        if not isinstance(other, KubernetesEndpointPortInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
