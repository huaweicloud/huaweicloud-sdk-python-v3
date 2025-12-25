# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OcaIpService:

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
        'protocol': 'str',
        'name': 'str',
        'version': 'str',
        'vendor': 'OcaIpVendor'
    }

    attribute_map = {
        'port': 'port',
        'protocol': 'protocol',
        'name': 'name',
        'version': 'version',
        'vendor': 'vendor'
    }

    def __init__(self, port=None, protocol=None, name=None, version=None, vendor=None):
        r"""OcaIpService

        The model defined in huaweicloud sdk

        :param port: 应用对应端口
        :type port: int
        :param protocol: 协议
        :type protocol: str
        :param name: 应用名称
        :type name: str
        :param version: 应用版本
        :type version: str
        :param vendor: 
        :type vendor: :class:`huaweicloudsdksecmaster.v1.OcaIpVendor`
        """
        
        

        self._port = None
        self._protocol = None
        self._name = None
        self._version = None
        self._vendor = None
        self.discriminator = None

        if port is not None:
            self.port = port
        if protocol is not None:
            self.protocol = protocol
        if name is not None:
            self.name = name
        if version is not None:
            self.version = version
        if vendor is not None:
            self.vendor = vendor

    @property
    def port(self):
        r"""Gets the port of this OcaIpService.

        应用对应端口

        :return: The port of this OcaIpService.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this OcaIpService.

        应用对应端口

        :param port: The port of this OcaIpService.
        :type port: int
        """
        self._port = port

    @property
    def protocol(self):
        r"""Gets the protocol of this OcaIpService.

        协议

        :return: The protocol of this OcaIpService.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        r"""Sets the protocol of this OcaIpService.

        协议

        :param protocol: The protocol of this OcaIpService.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def name(self):
        r"""Gets the name of this OcaIpService.

        应用名称

        :return: The name of this OcaIpService.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this OcaIpService.

        应用名称

        :param name: The name of this OcaIpService.
        :type name: str
        """
        self._name = name

    @property
    def version(self):
        r"""Gets the version of this OcaIpService.

        应用版本

        :return: The version of this OcaIpService.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this OcaIpService.

        应用版本

        :param version: The version of this OcaIpService.
        :type version: str
        """
        self._version = version

    @property
    def vendor(self):
        r"""Gets the vendor of this OcaIpService.

        :return: The vendor of this OcaIpService.
        :rtype: :class:`huaweicloudsdksecmaster.v1.OcaIpVendor`
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        r"""Sets the vendor of this OcaIpService.

        :param vendor: The vendor of this OcaIpService.
        :type vendor: :class:`huaweicloudsdksecmaster.v1.OcaIpVendor`
        """
        self._vendor = vendor

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
        if not isinstance(other, OcaIpService):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
