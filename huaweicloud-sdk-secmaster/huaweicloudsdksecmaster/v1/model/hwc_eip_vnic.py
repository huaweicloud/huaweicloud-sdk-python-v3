# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HwcEipVnic:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'private_ip_address': 'str',
        'device_id': 'str',
        'device_owner': 'str',
        'vpc_id': 'str',
        'port_id': 'str',
        'port_profile': 'str',
        'mac': 'str',
        'vtep': 'str',
        'vni': 'str',
        'instance_id': 'str',
        'instance_type': 'str'
    }

    attribute_map = {
        'private_ip_address': 'private_ip_address',
        'device_id': 'device_id',
        'device_owner': 'device_owner',
        'vpc_id': 'vpc_id',
        'port_id': 'port_id',
        'port_profile': 'port_profile',
        'mac': 'mac',
        'vtep': 'vtep',
        'vni': 'vni',
        'instance_id': 'instance_id',
        'instance_type': 'instance_type'
    }

    def __init__(self, private_ip_address=None, device_id=None, device_owner=None, vpc_id=None, port_id=None, port_profile=None, mac=None, vtep=None, vni=None, instance_id=None, instance_type=None):
        r"""HwcEipVnic

        The model defined in huaweicloud sdk

        :param private_ip_address: 私网IP地址
        :type private_ip_address: str
        :param device_id: 端口所属设备ID
        :type device_id: str
        :param device_owner: 设备所属 取值范围：合法设备所属 network:dhcp network:VIP_PORT network:router_interface_distributed network:router_centralized_snat 约束：不支持设置和更新,由系统自动维护
        :type device_owner: str
        :param vpc_id: 虚拟私有云ID
        :type vpc_id: str
        :param port_id: 端口ID
        :type port_id: str
        :param port_profile: 端口profile信息
        :type port_profile: str
        :param mac: 端口MAC地址
        :type mac: str
        :param vtep: VTEP IP
        :type vtep: str
        :param vni: VXLAN ID
        :type vni: str
        :param instance_id: 端口所属实例ID,例如RDS实例ID
        :type instance_id: str
        :param instance_type: 端口所属实例类型,例如“RDS”
        :type instance_type: str
        """
        
        

        self._private_ip_address = None
        self._device_id = None
        self._device_owner = None
        self._vpc_id = None
        self._port_id = None
        self._port_profile = None
        self._mac = None
        self._vtep = None
        self._vni = None
        self._instance_id = None
        self._instance_type = None
        self.discriminator = None

        if private_ip_address is not None:
            self.private_ip_address = private_ip_address
        if device_id is not None:
            self.device_id = device_id
        if device_owner is not None:
            self.device_owner = device_owner
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if port_id is not None:
            self.port_id = port_id
        if port_profile is not None:
            self.port_profile = port_profile
        if mac is not None:
            self.mac = mac
        if vtep is not None:
            self.vtep = vtep
        if vni is not None:
            self.vni = vni
        if instance_id is not None:
            self.instance_id = instance_id
        if instance_type is not None:
            self.instance_type = instance_type

    @property
    def private_ip_address(self):
        r"""Gets the private_ip_address of this HwcEipVnic.

        私网IP地址

        :return: The private_ip_address of this HwcEipVnic.
        :rtype: str
        """
        return self._private_ip_address

    @private_ip_address.setter
    def private_ip_address(self, private_ip_address):
        r"""Sets the private_ip_address of this HwcEipVnic.

        私网IP地址

        :param private_ip_address: The private_ip_address of this HwcEipVnic.
        :type private_ip_address: str
        """
        self._private_ip_address = private_ip_address

    @property
    def device_id(self):
        r"""Gets the device_id of this HwcEipVnic.

        端口所属设备ID

        :return: The device_id of this HwcEipVnic.
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        r"""Sets the device_id of this HwcEipVnic.

        端口所属设备ID

        :param device_id: The device_id of this HwcEipVnic.
        :type device_id: str
        """
        self._device_id = device_id

    @property
    def device_owner(self):
        r"""Gets the device_owner of this HwcEipVnic.

        设备所属 取值范围：合法设备所属 network:dhcp network:VIP_PORT network:router_interface_distributed network:router_centralized_snat 约束：不支持设置和更新,由系统自动维护

        :return: The device_owner of this HwcEipVnic.
        :rtype: str
        """
        return self._device_owner

    @device_owner.setter
    def device_owner(self, device_owner):
        r"""Sets the device_owner of this HwcEipVnic.

        设备所属 取值范围：合法设备所属 network:dhcp network:VIP_PORT network:router_interface_distributed network:router_centralized_snat 约束：不支持设置和更新,由系统自动维护

        :param device_owner: The device_owner of this HwcEipVnic.
        :type device_owner: str
        """
        self._device_owner = device_owner

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this HwcEipVnic.

        虚拟私有云ID

        :return: The vpc_id of this HwcEipVnic.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this HwcEipVnic.

        虚拟私有云ID

        :param vpc_id: The vpc_id of this HwcEipVnic.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def port_id(self):
        r"""Gets the port_id of this HwcEipVnic.

        端口ID

        :return: The port_id of this HwcEipVnic.
        :rtype: str
        """
        return self._port_id

    @port_id.setter
    def port_id(self, port_id):
        r"""Sets the port_id of this HwcEipVnic.

        端口ID

        :param port_id: The port_id of this HwcEipVnic.
        :type port_id: str
        """
        self._port_id = port_id

    @property
    def port_profile(self):
        r"""Gets the port_profile of this HwcEipVnic.

        端口profile信息

        :return: The port_profile of this HwcEipVnic.
        :rtype: str
        """
        return self._port_profile

    @port_profile.setter
    def port_profile(self, port_profile):
        r"""Sets the port_profile of this HwcEipVnic.

        端口profile信息

        :param port_profile: The port_profile of this HwcEipVnic.
        :type port_profile: str
        """
        self._port_profile = port_profile

    @property
    def mac(self):
        r"""Gets the mac of this HwcEipVnic.

        端口MAC地址

        :return: The mac of this HwcEipVnic.
        :rtype: str
        """
        return self._mac

    @mac.setter
    def mac(self, mac):
        r"""Sets the mac of this HwcEipVnic.

        端口MAC地址

        :param mac: The mac of this HwcEipVnic.
        :type mac: str
        """
        self._mac = mac

    @property
    def vtep(self):
        r"""Gets the vtep of this HwcEipVnic.

        VTEP IP

        :return: The vtep of this HwcEipVnic.
        :rtype: str
        """
        return self._vtep

    @vtep.setter
    def vtep(self, vtep):
        r"""Sets the vtep of this HwcEipVnic.

        VTEP IP

        :param vtep: The vtep of this HwcEipVnic.
        :type vtep: str
        """
        self._vtep = vtep

    @property
    def vni(self):
        r"""Gets the vni of this HwcEipVnic.

        VXLAN ID

        :return: The vni of this HwcEipVnic.
        :rtype: str
        """
        return self._vni

    @vni.setter
    def vni(self, vni):
        r"""Sets the vni of this HwcEipVnic.

        VXLAN ID

        :param vni: The vni of this HwcEipVnic.
        :type vni: str
        """
        self._vni = vni

    @property
    def instance_id(self):
        r"""Gets the instance_id of this HwcEipVnic.

        端口所属实例ID,例如RDS实例ID

        :return: The instance_id of this HwcEipVnic.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this HwcEipVnic.

        端口所属实例ID,例如RDS实例ID

        :param instance_id: The instance_id of this HwcEipVnic.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def instance_type(self):
        r"""Gets the instance_type of this HwcEipVnic.

        端口所属实例类型,例如“RDS”

        :return: The instance_type of this HwcEipVnic.
        :rtype: str
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        r"""Sets the instance_type of this HwcEipVnic.

        端口所属实例类型,例如“RDS”

        :param instance_type: The instance_type of this HwcEipVnic.
        :type instance_type: str
        """
        self._instance_type = instance_type

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
        if not isinstance(other, HwcEipVnic):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
