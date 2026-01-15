# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BindingVifDetails:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'primary_interface': 'bool',
        'port_filter': 'bool',
        'ovs_hybrid_plug': 'bool',
        'vlan_id': 'str',
        'parent_id': 'str',
        'parent_device_id': 'str'
    }

    attribute_map = {
        'primary_interface': 'primary_interface',
        'port_filter': 'port_filter',
        'ovs_hybrid_plug': 'ovs_hybrid_plug',
        'vlan_id': 'vlan_id',
        'parent_id': 'parent_id',
        'parent_device_id': 'parent_device_id'
    }

    def __init__(self, primary_interface=None, port_filter=None, ovs_hybrid_plug=None, vlan_id=None, parent_id=None, parent_device_id=None):
        r"""BindingVifDetails

        The model defined in huaweicloud sdk

        :param primary_interface: 是否为虚拟机的主网卡。
        :type primary_interface: bool
        :param port_filter: 是否提供端口过滤特性, 如安全组和反MAC/IP欺骗。
        :type port_filter: bool
        :param ovs_hybrid_plug: 是否为ovs/bridge混合模式。
        :type ovs_hybrid_plug: bool
        :param vlan_id: 辅助弹性网卡的vlan ID。
        :type vlan_id: str
        :param parent_id: 辅助弹性网卡的宿主网卡ID。
        :type parent_id: str
        :param parent_device_id: 辅助弹性网卡的宿主网卡所属的设备ID。
        :type parent_device_id: str
        """
        
        

        self._primary_interface = None
        self._port_filter = None
        self._ovs_hybrid_plug = None
        self._vlan_id = None
        self._parent_id = None
        self._parent_device_id = None
        self.discriminator = None

        if primary_interface is not None:
            self.primary_interface = primary_interface
        if port_filter is not None:
            self.port_filter = port_filter
        if ovs_hybrid_plug is not None:
            self.ovs_hybrid_plug = ovs_hybrid_plug
        if vlan_id is not None:
            self.vlan_id = vlan_id
        if parent_id is not None:
            self.parent_id = parent_id
        if parent_device_id is not None:
            self.parent_device_id = parent_device_id

    @property
    def primary_interface(self):
        r"""Gets the primary_interface of this BindingVifDetails.

        是否为虚拟机的主网卡。

        :return: The primary_interface of this BindingVifDetails.
        :rtype: bool
        """
        return self._primary_interface

    @primary_interface.setter
    def primary_interface(self, primary_interface):
        r"""Sets the primary_interface of this BindingVifDetails.

        是否为虚拟机的主网卡。

        :param primary_interface: The primary_interface of this BindingVifDetails.
        :type primary_interface: bool
        """
        self._primary_interface = primary_interface

    @property
    def port_filter(self):
        r"""Gets the port_filter of this BindingVifDetails.

        是否提供端口过滤特性, 如安全组和反MAC/IP欺骗。

        :return: The port_filter of this BindingVifDetails.
        :rtype: bool
        """
        return self._port_filter

    @port_filter.setter
    def port_filter(self, port_filter):
        r"""Sets the port_filter of this BindingVifDetails.

        是否提供端口过滤特性, 如安全组和反MAC/IP欺骗。

        :param port_filter: The port_filter of this BindingVifDetails.
        :type port_filter: bool
        """
        self._port_filter = port_filter

    @property
    def ovs_hybrid_plug(self):
        r"""Gets the ovs_hybrid_plug of this BindingVifDetails.

        是否为ovs/bridge混合模式。

        :return: The ovs_hybrid_plug of this BindingVifDetails.
        :rtype: bool
        """
        return self._ovs_hybrid_plug

    @ovs_hybrid_plug.setter
    def ovs_hybrid_plug(self, ovs_hybrid_plug):
        r"""Sets the ovs_hybrid_plug of this BindingVifDetails.

        是否为ovs/bridge混合模式。

        :param ovs_hybrid_plug: The ovs_hybrid_plug of this BindingVifDetails.
        :type ovs_hybrid_plug: bool
        """
        self._ovs_hybrid_plug = ovs_hybrid_plug

    @property
    def vlan_id(self):
        r"""Gets the vlan_id of this BindingVifDetails.

        辅助弹性网卡的vlan ID。

        :return: The vlan_id of this BindingVifDetails.
        :rtype: str
        """
        return self._vlan_id

    @vlan_id.setter
    def vlan_id(self, vlan_id):
        r"""Sets the vlan_id of this BindingVifDetails.

        辅助弹性网卡的vlan ID。

        :param vlan_id: The vlan_id of this BindingVifDetails.
        :type vlan_id: str
        """
        self._vlan_id = vlan_id

    @property
    def parent_id(self):
        r"""Gets the parent_id of this BindingVifDetails.

        辅助弹性网卡的宿主网卡ID。

        :return: The parent_id of this BindingVifDetails.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        r"""Sets the parent_id of this BindingVifDetails.

        辅助弹性网卡的宿主网卡ID。

        :param parent_id: The parent_id of this BindingVifDetails.
        :type parent_id: str
        """
        self._parent_id = parent_id

    @property
    def parent_device_id(self):
        r"""Gets the parent_device_id of this BindingVifDetails.

        辅助弹性网卡的宿主网卡所属的设备ID。

        :return: The parent_device_id of this BindingVifDetails.
        :rtype: str
        """
        return self._parent_device_id

    @parent_device_id.setter
    def parent_device_id(self, parent_device_id):
        r"""Sets the parent_device_id of this BindingVifDetails.

        辅助弹性网卡的宿主网卡所属的设备ID。

        :param parent_device_id: The parent_device_id of this BindingVifDetails.
        :type parent_device_id: str
        """
        self._parent_device_id = parent_device_id

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
        if not isinstance(other, BindingVifDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
