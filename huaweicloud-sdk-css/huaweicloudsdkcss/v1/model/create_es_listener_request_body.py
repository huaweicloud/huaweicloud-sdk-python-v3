# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateEsListenerRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'protocol': 'str',
        'protocol_port': 'int',
        'server_cert_id': 'str',
        'ca_cert_id': 'str'
    }

    attribute_map = {
        'protocol': 'protocol',
        'protocol_port': 'protocol_port',
        'server_cert_id': 'server_cert_id',
        'ca_cert_id': 'ca_cert_id'
    }

    def __init__(self, protocol=None, protocol_port=None, server_cert_id=None, ca_cert_id=None):
        """CreateEsListenerRequestBody

        The model defined in huaweicloud sdk

        :param protocol: 协议类型，支持HTTP、HTTPS
        :type protocol: str
        :param protocol_port: 端口。
        :type protocol_port: int
        :param server_cert_id: server证书Id。如protocol为HTTPS则该字段必选。
        :type server_cert_id: str
        :param ca_cert_id: CA证书Id。如protocol为HTTPS且为双向认证时则该字段必选。
        :type ca_cert_id: str
        """
        
        

        self._protocol = None
        self._protocol_port = None
        self._server_cert_id = None
        self._ca_cert_id = None
        self.discriminator = None

        self.protocol = protocol
        self.protocol_port = protocol_port
        if server_cert_id is not None:
            self.server_cert_id = server_cert_id
        if ca_cert_id is not None:
            self.ca_cert_id = ca_cert_id

    @property
    def protocol(self):
        """Gets the protocol of this CreateEsListenerRequestBody.

        协议类型，支持HTTP、HTTPS

        :return: The protocol of this CreateEsListenerRequestBody.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this CreateEsListenerRequestBody.

        协议类型，支持HTTP、HTTPS

        :param protocol: The protocol of this CreateEsListenerRequestBody.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def protocol_port(self):
        """Gets the protocol_port of this CreateEsListenerRequestBody.

        端口。

        :return: The protocol_port of this CreateEsListenerRequestBody.
        :rtype: int
        """
        return self._protocol_port

    @protocol_port.setter
    def protocol_port(self, protocol_port):
        """Sets the protocol_port of this CreateEsListenerRequestBody.

        端口。

        :param protocol_port: The protocol_port of this CreateEsListenerRequestBody.
        :type protocol_port: int
        """
        self._protocol_port = protocol_port

    @property
    def server_cert_id(self):
        """Gets the server_cert_id of this CreateEsListenerRequestBody.

        server证书Id。如protocol为HTTPS则该字段必选。

        :return: The server_cert_id of this CreateEsListenerRequestBody.
        :rtype: str
        """
        return self._server_cert_id

    @server_cert_id.setter
    def server_cert_id(self, server_cert_id):
        """Sets the server_cert_id of this CreateEsListenerRequestBody.

        server证书Id。如protocol为HTTPS则该字段必选。

        :param server_cert_id: The server_cert_id of this CreateEsListenerRequestBody.
        :type server_cert_id: str
        """
        self._server_cert_id = server_cert_id

    @property
    def ca_cert_id(self):
        """Gets the ca_cert_id of this CreateEsListenerRequestBody.

        CA证书Id。如protocol为HTTPS且为双向认证时则该字段必选。

        :return: The ca_cert_id of this CreateEsListenerRequestBody.
        :rtype: str
        """
        return self._ca_cert_id

    @ca_cert_id.setter
    def ca_cert_id(self, ca_cert_id):
        """Sets the ca_cert_id of this CreateEsListenerRequestBody.

        CA证书Id。如protocol为HTTPS且为双向认证时则该字段必选。

        :param ca_cert_id: The ca_cert_id of this CreateEsListenerRequestBody.
        :type ca_cert_id: str
        """
        self._ca_cert_id = ca_cert_id

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
        if not isinstance(other, CreateEsListenerRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
