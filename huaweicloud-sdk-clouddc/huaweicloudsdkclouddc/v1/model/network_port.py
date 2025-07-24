# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NetworkPort:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'physical_port_number': 'int',
        'link_status': 'str',
        'associated_network_addresses': 'str',
        'active_link_technology': 'str',
        'port_type': 'str',
        'port_max_speed': 'str',
        'firmware_package_version': 'str',
        'bdf': 'str',
        'auto_neg': 'str'
    }

    attribute_map = {
        'physical_port_number': 'physical_port_number',
        'link_status': 'link_status',
        'associated_network_addresses': 'associated_network_addresses',
        'active_link_technology': 'active_link_technology',
        'port_type': 'port_type',
        'port_max_speed': 'port_max_speed',
        'firmware_package_version': 'firmware_package_version',
        'bdf': 'bdf',
        'auto_neg': 'auto_neg'
    }

    def __init__(self, physical_port_number=None, link_status=None, associated_network_addresses=None, active_link_technology=None, port_type=None, port_max_speed=None, firmware_package_version=None, bdf=None, auto_neg=None):
        r"""NetworkPort

        The model defined in huaweicloud sdk

        :param physical_port_number: 网络端口的物理端口号
        :type physical_port_number: int
        :param link_status: 网络端口的物理连接状态
        :type link_status: str
        :param associated_network_addresses: 网络端口的网络地址
        :type associated_network_addresses: str
        :param active_link_technology: 网络端口的网络协议
        :type active_link_technology: str
        :param port_type: 网络端口的网口类型
        :type port_type: str
        :param port_max_speed: 网络端口的最大速率
        :type port_max_speed: str
        :param firmware_package_version: 网络端口的固件版本
        :type firmware_package_version: str
        :param bdf: 网络端口的BDF
        :type bdf: str
        :param auto_neg: 协议
        :type auto_neg: str
        """
        
        

        self._physical_port_number = None
        self._link_status = None
        self._associated_network_addresses = None
        self._active_link_technology = None
        self._port_type = None
        self._port_max_speed = None
        self._firmware_package_version = None
        self._bdf = None
        self._auto_neg = None
        self.discriminator = None

        if physical_port_number is not None:
            self.physical_port_number = physical_port_number
        if link_status is not None:
            self.link_status = link_status
        if associated_network_addresses is not None:
            self.associated_network_addresses = associated_network_addresses
        if active_link_technology is not None:
            self.active_link_technology = active_link_technology
        if port_type is not None:
            self.port_type = port_type
        if port_max_speed is not None:
            self.port_max_speed = port_max_speed
        if firmware_package_version is not None:
            self.firmware_package_version = firmware_package_version
        if bdf is not None:
            self.bdf = bdf
        if auto_neg is not None:
            self.auto_neg = auto_neg

    @property
    def physical_port_number(self):
        r"""Gets the physical_port_number of this NetworkPort.

        网络端口的物理端口号

        :return: The physical_port_number of this NetworkPort.
        :rtype: int
        """
        return self._physical_port_number

    @physical_port_number.setter
    def physical_port_number(self, physical_port_number):
        r"""Sets the physical_port_number of this NetworkPort.

        网络端口的物理端口号

        :param physical_port_number: The physical_port_number of this NetworkPort.
        :type physical_port_number: int
        """
        self._physical_port_number = physical_port_number

    @property
    def link_status(self):
        r"""Gets the link_status of this NetworkPort.

        网络端口的物理连接状态

        :return: The link_status of this NetworkPort.
        :rtype: str
        """
        return self._link_status

    @link_status.setter
    def link_status(self, link_status):
        r"""Sets the link_status of this NetworkPort.

        网络端口的物理连接状态

        :param link_status: The link_status of this NetworkPort.
        :type link_status: str
        """
        self._link_status = link_status

    @property
    def associated_network_addresses(self):
        r"""Gets the associated_network_addresses of this NetworkPort.

        网络端口的网络地址

        :return: The associated_network_addresses of this NetworkPort.
        :rtype: str
        """
        return self._associated_network_addresses

    @associated_network_addresses.setter
    def associated_network_addresses(self, associated_network_addresses):
        r"""Sets the associated_network_addresses of this NetworkPort.

        网络端口的网络地址

        :param associated_network_addresses: The associated_network_addresses of this NetworkPort.
        :type associated_network_addresses: str
        """
        self._associated_network_addresses = associated_network_addresses

    @property
    def active_link_technology(self):
        r"""Gets the active_link_technology of this NetworkPort.

        网络端口的网络协议

        :return: The active_link_technology of this NetworkPort.
        :rtype: str
        """
        return self._active_link_technology

    @active_link_technology.setter
    def active_link_technology(self, active_link_technology):
        r"""Sets the active_link_technology of this NetworkPort.

        网络端口的网络协议

        :param active_link_technology: The active_link_technology of this NetworkPort.
        :type active_link_technology: str
        """
        self._active_link_technology = active_link_technology

    @property
    def port_type(self):
        r"""Gets the port_type of this NetworkPort.

        网络端口的网口类型

        :return: The port_type of this NetworkPort.
        :rtype: str
        """
        return self._port_type

    @port_type.setter
    def port_type(self, port_type):
        r"""Sets the port_type of this NetworkPort.

        网络端口的网口类型

        :param port_type: The port_type of this NetworkPort.
        :type port_type: str
        """
        self._port_type = port_type

    @property
    def port_max_speed(self):
        r"""Gets the port_max_speed of this NetworkPort.

        网络端口的最大速率

        :return: The port_max_speed of this NetworkPort.
        :rtype: str
        """
        return self._port_max_speed

    @port_max_speed.setter
    def port_max_speed(self, port_max_speed):
        r"""Sets the port_max_speed of this NetworkPort.

        网络端口的最大速率

        :param port_max_speed: The port_max_speed of this NetworkPort.
        :type port_max_speed: str
        """
        self._port_max_speed = port_max_speed

    @property
    def firmware_package_version(self):
        r"""Gets the firmware_package_version of this NetworkPort.

        网络端口的固件版本

        :return: The firmware_package_version of this NetworkPort.
        :rtype: str
        """
        return self._firmware_package_version

    @firmware_package_version.setter
    def firmware_package_version(self, firmware_package_version):
        r"""Sets the firmware_package_version of this NetworkPort.

        网络端口的固件版本

        :param firmware_package_version: The firmware_package_version of this NetworkPort.
        :type firmware_package_version: str
        """
        self._firmware_package_version = firmware_package_version

    @property
    def bdf(self):
        r"""Gets the bdf of this NetworkPort.

        网络端口的BDF

        :return: The bdf of this NetworkPort.
        :rtype: str
        """
        return self._bdf

    @bdf.setter
    def bdf(self, bdf):
        r"""Sets the bdf of this NetworkPort.

        网络端口的BDF

        :param bdf: The bdf of this NetworkPort.
        :type bdf: str
        """
        self._bdf = bdf

    @property
    def auto_neg(self):
        r"""Gets the auto_neg of this NetworkPort.

        协议

        :return: The auto_neg of this NetworkPort.
        :rtype: str
        """
        return self._auto_neg

    @auto_neg.setter
    def auto_neg(self, auto_neg):
        r"""Sets the auto_neg of this NetworkPort.

        协议

        :param auto_neg: The auto_neg of this NetworkPort.
        :type auto_neg: str
        """
        self._auto_neg = auto_neg

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
        if not isinstance(other, NetworkPort):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
