# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PreUpgradeProbeDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'port': 'int',
        'path': 'str',
        'interval': 'int',
        'protocol': 'str',
        'timeout_config': 'UpgradeProbeTimeoutConfigDTO'
    }

    attribute_map = {
        'port': 'port',
        'path': 'path',
        'interval': 'interval',
        'protocol': 'protocol',
        'timeout_config': 'timeout_config'
    }

    def __init__(self, port=None, path=None, interval=None, protocol=None, timeout_config=None):
        r"""PreUpgradeProbeDTO

        The model defined in huaweicloud sdk

        :param port: 端口
        :type port: int
        :param path: 请求路径
        :type path: str
        :param interval: 轮询间隔
        :type interval: int
        :param protocol: 协议类型
        :type protocol: str
        :param timeout_config: 
        :type timeout_config: :class:`huaweicloudsdkiotedge.v2.UpgradeProbeTimeoutConfigDTO`
        """
        
        

        self._port = None
        self._path = None
        self._interval = None
        self._protocol = None
        self._timeout_config = None
        self.discriminator = None

        if port is not None:
            self.port = port
        if path is not None:
            self.path = path
        if interval is not None:
            self.interval = interval
        if protocol is not None:
            self.protocol = protocol
        if timeout_config is not None:
            self.timeout_config = timeout_config

    @property
    def port(self):
        r"""Gets the port of this PreUpgradeProbeDTO.

        端口

        :return: The port of this PreUpgradeProbeDTO.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this PreUpgradeProbeDTO.

        端口

        :param port: The port of this PreUpgradeProbeDTO.
        :type port: int
        """
        self._port = port

    @property
    def path(self):
        r"""Gets the path of this PreUpgradeProbeDTO.

        请求路径

        :return: The path of this PreUpgradeProbeDTO.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this PreUpgradeProbeDTO.

        请求路径

        :param path: The path of this PreUpgradeProbeDTO.
        :type path: str
        """
        self._path = path

    @property
    def interval(self):
        r"""Gets the interval of this PreUpgradeProbeDTO.

        轮询间隔

        :return: The interval of this PreUpgradeProbeDTO.
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        r"""Sets the interval of this PreUpgradeProbeDTO.

        轮询间隔

        :param interval: The interval of this PreUpgradeProbeDTO.
        :type interval: int
        """
        self._interval = interval

    @property
    def protocol(self):
        r"""Gets the protocol of this PreUpgradeProbeDTO.

        协议类型

        :return: The protocol of this PreUpgradeProbeDTO.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        r"""Sets the protocol of this PreUpgradeProbeDTO.

        协议类型

        :param protocol: The protocol of this PreUpgradeProbeDTO.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def timeout_config(self):
        r"""Gets the timeout_config of this PreUpgradeProbeDTO.

        :return: The timeout_config of this PreUpgradeProbeDTO.
        :rtype: :class:`huaweicloudsdkiotedge.v2.UpgradeProbeTimeoutConfigDTO`
        """
        return self._timeout_config

    @timeout_config.setter
    def timeout_config(self, timeout_config):
        r"""Sets the timeout_config of this PreUpgradeProbeDTO.

        :param timeout_config: The timeout_config of this PreUpgradeProbeDTO.
        :type timeout_config: :class:`huaweicloudsdkiotedge.v2.UpgradeProbeTimeoutConfigDTO`
        """
        self._timeout_config = timeout_config

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
        if not isinstance(other, PreUpgradeProbeDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
