# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HwcEcsAddress:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'version': 'str',
        'addr': 'str',
        'type': 'str',
        'mac_addr': 'str',
        'port_id': 'str',
        'vpc_id': 'str'
    }

    attribute_map = {
        'version': 'version',
        'addr': 'addr',
        'type': 'type',
        'mac_addr': 'mac_addr',
        'port_id': 'port_id',
        'vpc_id': 'vpc_id'
    }

    def __init__(self, version=None, addr=None, type=None, mac_addr=None, port_id=None, vpc_id=None):
        r"""HwcEcsAddress

        The model defined in huaweicloud sdk

        :param version: IP地址版本。 “4”：代表IPv4。 “6”：代表IPv6。
        :type version: str
        :param addr: IP地址。
        :type addr: str
        :param type: IP地址类型。 fixed：代表私有IP地址。 floating：代表浮动IP地址
        :type type: str
        :param mac_addr: MAC地址。
        :type mac_addr: str
        :param port_id: IP地址对应的端口ID。
        :type port_id: str
        :param vpc_id: 所属虚拟私有云的ID。
        :type vpc_id: str
        """
        
        

        self._version = None
        self._addr = None
        self._type = None
        self._mac_addr = None
        self._port_id = None
        self._vpc_id = None
        self.discriminator = None

        self.version = version
        self.addr = addr
        self.type = type
        self.mac_addr = mac_addr
        self.port_id = port_id
        self.vpc_id = vpc_id

    @property
    def version(self):
        r"""Gets the version of this HwcEcsAddress.

        IP地址版本。 “4”：代表IPv4。 “6”：代表IPv6。

        :return: The version of this HwcEcsAddress.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this HwcEcsAddress.

        IP地址版本。 “4”：代表IPv4。 “6”：代表IPv6。

        :param version: The version of this HwcEcsAddress.
        :type version: str
        """
        self._version = version

    @property
    def addr(self):
        r"""Gets the addr of this HwcEcsAddress.

        IP地址。

        :return: The addr of this HwcEcsAddress.
        :rtype: str
        """
        return self._addr

    @addr.setter
    def addr(self, addr):
        r"""Sets the addr of this HwcEcsAddress.

        IP地址。

        :param addr: The addr of this HwcEcsAddress.
        :type addr: str
        """
        self._addr = addr

    @property
    def type(self):
        r"""Gets the type of this HwcEcsAddress.

        IP地址类型。 fixed：代表私有IP地址。 floating：代表浮动IP地址

        :return: The type of this HwcEcsAddress.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this HwcEcsAddress.

        IP地址类型。 fixed：代表私有IP地址。 floating：代表浮动IP地址

        :param type: The type of this HwcEcsAddress.
        :type type: str
        """
        self._type = type

    @property
    def mac_addr(self):
        r"""Gets the mac_addr of this HwcEcsAddress.

        MAC地址。

        :return: The mac_addr of this HwcEcsAddress.
        :rtype: str
        """
        return self._mac_addr

    @mac_addr.setter
    def mac_addr(self, mac_addr):
        r"""Sets the mac_addr of this HwcEcsAddress.

        MAC地址。

        :param mac_addr: The mac_addr of this HwcEcsAddress.
        :type mac_addr: str
        """
        self._mac_addr = mac_addr

    @property
    def port_id(self):
        r"""Gets the port_id of this HwcEcsAddress.

        IP地址对应的端口ID。

        :return: The port_id of this HwcEcsAddress.
        :rtype: str
        """
        return self._port_id

    @port_id.setter
    def port_id(self, port_id):
        r"""Sets the port_id of this HwcEcsAddress.

        IP地址对应的端口ID。

        :param port_id: The port_id of this HwcEcsAddress.
        :type port_id: str
        """
        self._port_id = port_id

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this HwcEcsAddress.

        所属虚拟私有云的ID。

        :return: The vpc_id of this HwcEcsAddress.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this HwcEcsAddress.

        所属虚拟私有云的ID。

        :param vpc_id: The vpc_id of this HwcEcsAddress.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

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
        if not isinstance(other, HwcEcsAddress):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
