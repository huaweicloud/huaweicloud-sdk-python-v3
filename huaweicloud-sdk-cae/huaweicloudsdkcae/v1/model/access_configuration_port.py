# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AccessConfigurationPort:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'target_port': 'str',
        'port': 'str',
        'protocol': 'str',
        'default_certificate': 'str',
        'certificate': 'str',
        'policy': 'str',
        'path': 'list[AccessConfigurationHttpPath]'
    }

    attribute_map = {
        'target_port': 'target_port',
        'port': 'port',
        'protocol': 'protocol',
        'default_certificate': 'default_certificate',
        'certificate': 'certificate',
        'policy': 'policy',
        'path': 'path'
    }

    def __init__(self, target_port=None, port=None, protocol=None, default_certificate=None, certificate=None, policy=None, path=None):
        """AccessConfigurationPort

        The model defined in huaweicloud sdk

        :param target_port: 监听端口。
        :type target_port: str
        :param port: 访问端口。
        :type port: str
        :param protocol: 协议。
        :type protocol: str
        :param default_certificate: 默认证书，访问方式配置为转发策略且协议为HTTPS时配置，未配置域名证书对时使用默认证书。
        :type default_certificate: str
        :param certificate: 证书。
        :type certificate: str
        :param policy: 安全策略。
        :type policy: str
        :param path: 
        :type path: list[:class:`huaweicloudsdkcae.v1.AccessConfigurationHttpPath`]
        """
        
        

        self._target_port = None
        self._port = None
        self._protocol = None
        self._default_certificate = None
        self._certificate = None
        self._policy = None
        self._path = None
        self.discriminator = None

        if target_port is not None:
            self.target_port = target_port
        if port is not None:
            self.port = port
        if protocol is not None:
            self.protocol = protocol
        if default_certificate is not None:
            self.default_certificate = default_certificate
        if certificate is not None:
            self.certificate = certificate
        if policy is not None:
            self.policy = policy
        if path is not None:
            self.path = path

    @property
    def target_port(self):
        """Gets the target_port of this AccessConfigurationPort.

        监听端口。

        :return: The target_port of this AccessConfigurationPort.
        :rtype: str
        """
        return self._target_port

    @target_port.setter
    def target_port(self, target_port):
        """Sets the target_port of this AccessConfigurationPort.

        监听端口。

        :param target_port: The target_port of this AccessConfigurationPort.
        :type target_port: str
        """
        self._target_port = target_port

    @property
    def port(self):
        """Gets the port of this AccessConfigurationPort.

        访问端口。

        :return: The port of this AccessConfigurationPort.
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this AccessConfigurationPort.

        访问端口。

        :param port: The port of this AccessConfigurationPort.
        :type port: str
        """
        self._port = port

    @property
    def protocol(self):
        """Gets the protocol of this AccessConfigurationPort.

        协议。

        :return: The protocol of this AccessConfigurationPort.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this AccessConfigurationPort.

        协议。

        :param protocol: The protocol of this AccessConfigurationPort.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def default_certificate(self):
        """Gets the default_certificate of this AccessConfigurationPort.

        默认证书，访问方式配置为转发策略且协议为HTTPS时配置，未配置域名证书对时使用默认证书。

        :return: The default_certificate of this AccessConfigurationPort.
        :rtype: str
        """
        return self._default_certificate

    @default_certificate.setter
    def default_certificate(self, default_certificate):
        """Sets the default_certificate of this AccessConfigurationPort.

        默认证书，访问方式配置为转发策略且协议为HTTPS时配置，未配置域名证书对时使用默认证书。

        :param default_certificate: The default_certificate of this AccessConfigurationPort.
        :type default_certificate: str
        """
        self._default_certificate = default_certificate

    @property
    def certificate(self):
        """Gets the certificate of this AccessConfigurationPort.

        证书。

        :return: The certificate of this AccessConfigurationPort.
        :rtype: str
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate):
        """Sets the certificate of this AccessConfigurationPort.

        证书。

        :param certificate: The certificate of this AccessConfigurationPort.
        :type certificate: str
        """
        self._certificate = certificate

    @property
    def policy(self):
        """Gets the policy of this AccessConfigurationPort.

        安全策略。

        :return: The policy of this AccessConfigurationPort.
        :rtype: str
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """Sets the policy of this AccessConfigurationPort.

        安全策略。

        :param policy: The policy of this AccessConfigurationPort.
        :type policy: str
        """
        self._policy = policy

    @property
    def path(self):
        """Gets the path of this AccessConfigurationPort.

        :return: The path of this AccessConfigurationPort.
        :rtype: list[:class:`huaweicloudsdkcae.v1.AccessConfigurationHttpPath`]
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this AccessConfigurationPort.

        :param path: The path of this AccessConfigurationPort.
        :type path: list[:class:`huaweicloudsdkcae.v1.AccessConfigurationHttpPath`]
        """
        self._path = path

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
        if not isinstance(other, AccessConfigurationPort):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
