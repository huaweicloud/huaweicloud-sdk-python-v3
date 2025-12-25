# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OcaIp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'value': 'str',
        'version': 'str',
        'network': 'OcaIpNetwork',
        'remark': 'str',
        'name': 'str',
        'relative_value': 'str',
        'server_room': 'str',
        'server_rack': 'str',
        'data_center': 'OcaIpDataCenter',
        'mac_addr': 'str',
        'important': 'str',
        'extend_properties': 'OcaIpExtendProperties'
    }

    attribute_map = {
        'value': 'value',
        'version': 'version',
        'network': 'network',
        'remark': 'remark',
        'name': 'name',
        'relative_value': 'relative_value',
        'server_room': 'server_room',
        'server_rack': 'server_rack',
        'data_center': 'data_center',
        'mac_addr': 'mac_addr',
        'important': 'important',
        'extend_properties': 'extend_properties'
    }

    def __init__(self, value=None, version=None, network=None, remark=None, name=None, relative_value=None, server_room=None, server_rack=None, data_center=None, mac_addr=None, important=None, extend_properties=None):
        r"""OcaIp

        The model defined in huaweicloud sdk

        :param value: 资产值
        :type value: str
        :param version: 资产类型：  ipv4、ipv6
        :type version: str
        :param network: 
        :type network: :class:`huaweicloudsdksecmaster.v1.OcaIpNetwork`
        :param remark: 资产备注
        :type remark: str
        :param name: 资产名称，默认为资产值
        :type name: str
        :param relative_value: 相对值，如资产为ipv4，则为对应的ipv6
        :type relative_value: str
        :param server_room: 机房
        :type server_room: str
        :param server_rack: 机柜
        :type server_rack: str
        :param data_center: 
        :type data_center: :class:`huaweicloudsdksecmaster.v1.OcaIpDataCenter`
        :param mac_addr: mac地址
        :type mac_addr: str
        :param important: 重要等级0 ：不重要 1：重要
        :type important: str
        :param extend_properties: 
        :type extend_properties: :class:`huaweicloudsdksecmaster.v1.OcaIpExtendProperties`
        """
        
        

        self._value = None
        self._version = None
        self._network = None
        self._remark = None
        self._name = None
        self._relative_value = None
        self._server_room = None
        self._server_rack = None
        self._data_center = None
        self._mac_addr = None
        self._important = None
        self._extend_properties = None
        self.discriminator = None

        self.value = value
        self.version = version
        self.network = network
        if remark is not None:
            self.remark = remark
        if name is not None:
            self.name = name
        if relative_value is not None:
            self.relative_value = relative_value
        self.server_room = server_room
        self.server_rack = server_rack
        self.data_center = data_center
        if mac_addr is not None:
            self.mac_addr = mac_addr
        if important is not None:
            self.important = important
        if extend_properties is not None:
            self.extend_properties = extend_properties

    @property
    def value(self):
        r"""Gets the value of this OcaIp.

        资产值

        :return: The value of this OcaIp.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this OcaIp.

        资产值

        :param value: The value of this OcaIp.
        :type value: str
        """
        self._value = value

    @property
    def version(self):
        r"""Gets the version of this OcaIp.

        资产类型：  ipv4、ipv6

        :return: The version of this OcaIp.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this OcaIp.

        资产类型：  ipv4、ipv6

        :param version: The version of this OcaIp.
        :type version: str
        """
        self._version = version

    @property
    def network(self):
        r"""Gets the network of this OcaIp.

        :return: The network of this OcaIp.
        :rtype: :class:`huaweicloudsdksecmaster.v1.OcaIpNetwork`
        """
        return self._network

    @network.setter
    def network(self, network):
        r"""Sets the network of this OcaIp.

        :param network: The network of this OcaIp.
        :type network: :class:`huaweicloudsdksecmaster.v1.OcaIpNetwork`
        """
        self._network = network

    @property
    def remark(self):
        r"""Gets the remark of this OcaIp.

        资产备注

        :return: The remark of this OcaIp.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        r"""Sets the remark of this OcaIp.

        资产备注

        :param remark: The remark of this OcaIp.
        :type remark: str
        """
        self._remark = remark

    @property
    def name(self):
        r"""Gets the name of this OcaIp.

        资产名称，默认为资产值

        :return: The name of this OcaIp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this OcaIp.

        资产名称，默认为资产值

        :param name: The name of this OcaIp.
        :type name: str
        """
        self._name = name

    @property
    def relative_value(self):
        r"""Gets the relative_value of this OcaIp.

        相对值，如资产为ipv4，则为对应的ipv6

        :return: The relative_value of this OcaIp.
        :rtype: str
        """
        return self._relative_value

    @relative_value.setter
    def relative_value(self, relative_value):
        r"""Sets the relative_value of this OcaIp.

        相对值，如资产为ipv4，则为对应的ipv6

        :param relative_value: The relative_value of this OcaIp.
        :type relative_value: str
        """
        self._relative_value = relative_value

    @property
    def server_room(self):
        r"""Gets the server_room of this OcaIp.

        机房

        :return: The server_room of this OcaIp.
        :rtype: str
        """
        return self._server_room

    @server_room.setter
    def server_room(self, server_room):
        r"""Sets the server_room of this OcaIp.

        机房

        :param server_room: The server_room of this OcaIp.
        :type server_room: str
        """
        self._server_room = server_room

    @property
    def server_rack(self):
        r"""Gets the server_rack of this OcaIp.

        机柜

        :return: The server_rack of this OcaIp.
        :rtype: str
        """
        return self._server_rack

    @server_rack.setter
    def server_rack(self, server_rack):
        r"""Sets the server_rack of this OcaIp.

        机柜

        :param server_rack: The server_rack of this OcaIp.
        :type server_rack: str
        """
        self._server_rack = server_rack

    @property
    def data_center(self):
        r"""Gets the data_center of this OcaIp.

        :return: The data_center of this OcaIp.
        :rtype: :class:`huaweicloudsdksecmaster.v1.OcaIpDataCenter`
        """
        return self._data_center

    @data_center.setter
    def data_center(self, data_center):
        r"""Sets the data_center of this OcaIp.

        :param data_center: The data_center of this OcaIp.
        :type data_center: :class:`huaweicloudsdksecmaster.v1.OcaIpDataCenter`
        """
        self._data_center = data_center

    @property
    def mac_addr(self):
        r"""Gets the mac_addr of this OcaIp.

        mac地址

        :return: The mac_addr of this OcaIp.
        :rtype: str
        """
        return self._mac_addr

    @mac_addr.setter
    def mac_addr(self, mac_addr):
        r"""Sets the mac_addr of this OcaIp.

        mac地址

        :param mac_addr: The mac_addr of this OcaIp.
        :type mac_addr: str
        """
        self._mac_addr = mac_addr

    @property
    def important(self):
        r"""Gets the important of this OcaIp.

        重要等级0 ：不重要 1：重要

        :return: The important of this OcaIp.
        :rtype: str
        """
        return self._important

    @important.setter
    def important(self, important):
        r"""Sets the important of this OcaIp.

        重要等级0 ：不重要 1：重要

        :param important: The important of this OcaIp.
        :type important: str
        """
        self._important = important

    @property
    def extend_properties(self):
        r"""Gets the extend_properties of this OcaIp.

        :return: The extend_properties of this OcaIp.
        :rtype: :class:`huaweicloudsdksecmaster.v1.OcaIpExtendProperties`
        """
        return self._extend_properties

    @extend_properties.setter
    def extend_properties(self, extend_properties):
        r"""Sets the extend_properties of this OcaIp.

        :param extend_properties: The extend_properties of this OcaIp.
        :type extend_properties: :class:`huaweicloudsdksecmaster.v1.OcaIpExtendProperties`
        """
        self._extend_properties = extend_properties

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
        if not isinstance(other, OcaIp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
