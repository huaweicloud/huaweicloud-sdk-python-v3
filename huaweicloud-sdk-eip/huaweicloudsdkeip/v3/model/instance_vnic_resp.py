# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstanceVnicResp:

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
        'mac': 'str',
        'vtep': 'str',
        'vni': 'int',
        'instance_id': 'str',
        'instance_type': 'str',
        'port_profile': 'str'
    }

    attribute_map = {
        'private_ip_address': 'private_ip_address',
        'device_id': 'device_id',
        'device_owner': 'device_owner',
        'vpc_id': 'vpc_id',
        'port_id': 'port_id',
        'mac': 'mac',
        'vtep': 'vtep',
        'vni': 'vni',
        'instance_id': 'instance_id',
        'instance_type': 'instance_type',
        'port_profile': 'port_profile'
    }

    def __init__(self, private_ip_address=None, device_id=None, device_owner=None, vpc_id=None, port_id=None, mac=None, vtep=None, vni=None, instance_id=None, instance_type=None, port_profile=None):
        """InstanceVnicResp

        The model defined in huaweicloud sdk

        :param private_ip_address: 实例port的ip地址
        :type private_ip_address: str
        :param device_id: port的device_id
        :type device_id: str
        :param device_owner: port的device_owner
        :type device_owner: str
        :param vpc_id: port的vpc_id
        :type vpc_id: str
        :param port_id: port的uuid
        :type port_id: str
        :param mac: port的mac地址
        :type mac: str
        :param vtep: port的vtep地址
        :type vtep: str
        :param vni: port的vni
        :type vni: int
        :param instance_id: port的实例id
        :type instance_id: str
        :param instance_type: port的实例类型
        :type instance_type: str
        :param port_profile: port的profile
        :type port_profile: str
        """
        
        

        self._private_ip_address = None
        self._device_id = None
        self._device_owner = None
        self._vpc_id = None
        self._port_id = None
        self._mac = None
        self._vtep = None
        self._vni = None
        self._instance_id = None
        self._instance_type = None
        self._port_profile = None
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
        if port_profile is not None:
            self.port_profile = port_profile

    @property
    def private_ip_address(self):
        """Gets the private_ip_address of this InstanceVnicResp.

        实例port的ip地址

        :return: The private_ip_address of this InstanceVnicResp.
        :rtype: str
        """
        return self._private_ip_address

    @private_ip_address.setter
    def private_ip_address(self, private_ip_address):
        """Sets the private_ip_address of this InstanceVnicResp.

        实例port的ip地址

        :param private_ip_address: The private_ip_address of this InstanceVnicResp.
        :type private_ip_address: str
        """
        self._private_ip_address = private_ip_address

    @property
    def device_id(self):
        """Gets the device_id of this InstanceVnicResp.

        port的device_id

        :return: The device_id of this InstanceVnicResp.
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this InstanceVnicResp.

        port的device_id

        :param device_id: The device_id of this InstanceVnicResp.
        :type device_id: str
        """
        self._device_id = device_id

    @property
    def device_owner(self):
        """Gets the device_owner of this InstanceVnicResp.

        port的device_owner

        :return: The device_owner of this InstanceVnicResp.
        :rtype: str
        """
        return self._device_owner

    @device_owner.setter
    def device_owner(self, device_owner):
        """Sets the device_owner of this InstanceVnicResp.

        port的device_owner

        :param device_owner: The device_owner of this InstanceVnicResp.
        :type device_owner: str
        """
        self._device_owner = device_owner

    @property
    def vpc_id(self):
        """Gets the vpc_id of this InstanceVnicResp.

        port的vpc_id

        :return: The vpc_id of this InstanceVnicResp.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this InstanceVnicResp.

        port的vpc_id

        :param vpc_id: The vpc_id of this InstanceVnicResp.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def port_id(self):
        """Gets the port_id of this InstanceVnicResp.

        port的uuid

        :return: The port_id of this InstanceVnicResp.
        :rtype: str
        """
        return self._port_id

    @port_id.setter
    def port_id(self, port_id):
        """Sets the port_id of this InstanceVnicResp.

        port的uuid

        :param port_id: The port_id of this InstanceVnicResp.
        :type port_id: str
        """
        self._port_id = port_id

    @property
    def mac(self):
        """Gets the mac of this InstanceVnicResp.

        port的mac地址

        :return: The mac of this InstanceVnicResp.
        :rtype: str
        """
        return self._mac

    @mac.setter
    def mac(self, mac):
        """Sets the mac of this InstanceVnicResp.

        port的mac地址

        :param mac: The mac of this InstanceVnicResp.
        :type mac: str
        """
        self._mac = mac

    @property
    def vtep(self):
        """Gets the vtep of this InstanceVnicResp.

        port的vtep地址

        :return: The vtep of this InstanceVnicResp.
        :rtype: str
        """
        return self._vtep

    @vtep.setter
    def vtep(self, vtep):
        """Sets the vtep of this InstanceVnicResp.

        port的vtep地址

        :param vtep: The vtep of this InstanceVnicResp.
        :type vtep: str
        """
        self._vtep = vtep

    @property
    def vni(self):
        """Gets the vni of this InstanceVnicResp.

        port的vni

        :return: The vni of this InstanceVnicResp.
        :rtype: int
        """
        return self._vni

    @vni.setter
    def vni(self, vni):
        """Sets the vni of this InstanceVnicResp.

        port的vni

        :param vni: The vni of this InstanceVnicResp.
        :type vni: int
        """
        self._vni = vni

    @property
    def instance_id(self):
        """Gets the instance_id of this InstanceVnicResp.

        port的实例id

        :return: The instance_id of this InstanceVnicResp.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this InstanceVnicResp.

        port的实例id

        :param instance_id: The instance_id of this InstanceVnicResp.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def instance_type(self):
        """Gets the instance_type of this InstanceVnicResp.

        port的实例类型

        :return: The instance_type of this InstanceVnicResp.
        :rtype: str
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        """Sets the instance_type of this InstanceVnicResp.

        port的实例类型

        :param instance_type: The instance_type of this InstanceVnicResp.
        :type instance_type: str
        """
        self._instance_type = instance_type

    @property
    def port_profile(self):
        """Gets the port_profile of this InstanceVnicResp.

        port的profile

        :return: The port_profile of this InstanceVnicResp.
        :rtype: str
        """
        return self._port_profile

    @port_profile.setter
    def port_profile(self, port_profile):
        """Sets the port_profile of this InstanceVnicResp.

        port的profile

        :param port_profile: The port_profile of this InstanceVnicResp.
        :type port_profile: str
        """
        self._port_profile = port_profile

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
        if not isinstance(other, InstanceVnicResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
