# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EquipmentLanItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'interface_name': 'str',
        'interface_type': 'str',
        'vlan_id': 'int',
        'ip_address': 'str',
        'dhcp': 'bool',
        'start_ip_address': 'str',
        'end_ip_address': 'str',
        'lease_time': 'int',
        'post_to_cloud': 'bool'
    }

    attribute_map = {
        'interface_name': 'interface_name',
        'interface_type': 'interface_type',
        'vlan_id': 'vlan_id',
        'ip_address': 'ip_address',
        'dhcp': 'dhcp',
        'start_ip_address': 'start_ip_address',
        'end_ip_address': 'end_ip_address',
        'lease_time': 'lease_time',
        'post_to_cloud': 'post_to_cloud'
    }

    def __init__(self, interface_name=None, interface_type=None, vlan_id=None, ip_address=None, dhcp=None, start_ip_address=None, end_ip_address=None, lease_time=None, post_to_cloud=None):
        """EquipmentLanItem

        The model defined in huaweicloud sdk

        :param interface_name: 接口名字
        :type interface_name: str
        :param interface_type: 接口类型
        :type interface_type: str
        :param vlan_id: VlanID
        :type vlan_id: int
        :param ip_address: IPv4地址
        :type ip_address: str
        :param dhcp: DHCP开关
        :type dhcp: bool
        :param start_ip_address: DHCP地址池起始IP地址
        :type start_ip_address: str
        :param end_ip_address: DHCP地址池结束IP地址
        :type end_ip_address: str
        :param lease_time: 地址租期(分钟)
        :type lease_time: int
        :param post_to_cloud: 发布到企业连接网络
        :type post_to_cloud: bool
        """
        
        

        self._interface_name = None
        self._interface_type = None
        self._vlan_id = None
        self._ip_address = None
        self._dhcp = None
        self._start_ip_address = None
        self._end_ip_address = None
        self._lease_time = None
        self._post_to_cloud = None
        self.discriminator = None

        self.interface_name = interface_name
        self.interface_type = interface_type
        if vlan_id is not None:
            self.vlan_id = vlan_id
        self.ip_address = ip_address
        self.dhcp = dhcp
        if start_ip_address is not None:
            self.start_ip_address = start_ip_address
        if end_ip_address is not None:
            self.end_ip_address = end_ip_address
        if lease_time is not None:
            self.lease_time = lease_time
        self.post_to_cloud = post_to_cloud

    @property
    def interface_name(self):
        """Gets the interface_name of this EquipmentLanItem.

        接口名字

        :return: The interface_name of this EquipmentLanItem.
        :rtype: str
        """
        return self._interface_name

    @interface_name.setter
    def interface_name(self, interface_name):
        """Sets the interface_name of this EquipmentLanItem.

        接口名字

        :param interface_name: The interface_name of this EquipmentLanItem.
        :type interface_name: str
        """
        self._interface_name = interface_name

    @property
    def interface_type(self):
        """Gets the interface_type of this EquipmentLanItem.

        接口类型

        :return: The interface_type of this EquipmentLanItem.
        :rtype: str
        """
        return self._interface_type

    @interface_type.setter
    def interface_type(self, interface_type):
        """Sets the interface_type of this EquipmentLanItem.

        接口类型

        :param interface_type: The interface_type of this EquipmentLanItem.
        :type interface_type: str
        """
        self._interface_type = interface_type

    @property
    def vlan_id(self):
        """Gets the vlan_id of this EquipmentLanItem.

        VlanID

        :return: The vlan_id of this EquipmentLanItem.
        :rtype: int
        """
        return self._vlan_id

    @vlan_id.setter
    def vlan_id(self, vlan_id):
        """Sets the vlan_id of this EquipmentLanItem.

        VlanID

        :param vlan_id: The vlan_id of this EquipmentLanItem.
        :type vlan_id: int
        """
        self._vlan_id = vlan_id

    @property
    def ip_address(self):
        """Gets the ip_address of this EquipmentLanItem.

        IPv4地址

        :return: The ip_address of this EquipmentLanItem.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this EquipmentLanItem.

        IPv4地址

        :param ip_address: The ip_address of this EquipmentLanItem.
        :type ip_address: str
        """
        self._ip_address = ip_address

    @property
    def dhcp(self):
        """Gets the dhcp of this EquipmentLanItem.

        DHCP开关

        :return: The dhcp of this EquipmentLanItem.
        :rtype: bool
        """
        return self._dhcp

    @dhcp.setter
    def dhcp(self, dhcp):
        """Sets the dhcp of this EquipmentLanItem.

        DHCP开关

        :param dhcp: The dhcp of this EquipmentLanItem.
        :type dhcp: bool
        """
        self._dhcp = dhcp

    @property
    def start_ip_address(self):
        """Gets the start_ip_address of this EquipmentLanItem.

        DHCP地址池起始IP地址

        :return: The start_ip_address of this EquipmentLanItem.
        :rtype: str
        """
        return self._start_ip_address

    @start_ip_address.setter
    def start_ip_address(self, start_ip_address):
        """Sets the start_ip_address of this EquipmentLanItem.

        DHCP地址池起始IP地址

        :param start_ip_address: The start_ip_address of this EquipmentLanItem.
        :type start_ip_address: str
        """
        self._start_ip_address = start_ip_address

    @property
    def end_ip_address(self):
        """Gets the end_ip_address of this EquipmentLanItem.

        DHCP地址池结束IP地址

        :return: The end_ip_address of this EquipmentLanItem.
        :rtype: str
        """
        return self._end_ip_address

    @end_ip_address.setter
    def end_ip_address(self, end_ip_address):
        """Sets the end_ip_address of this EquipmentLanItem.

        DHCP地址池结束IP地址

        :param end_ip_address: The end_ip_address of this EquipmentLanItem.
        :type end_ip_address: str
        """
        self._end_ip_address = end_ip_address

    @property
    def lease_time(self):
        """Gets the lease_time of this EquipmentLanItem.

        地址租期(分钟)

        :return: The lease_time of this EquipmentLanItem.
        :rtype: int
        """
        return self._lease_time

    @lease_time.setter
    def lease_time(self, lease_time):
        """Sets the lease_time of this EquipmentLanItem.

        地址租期(分钟)

        :param lease_time: The lease_time of this EquipmentLanItem.
        :type lease_time: int
        """
        self._lease_time = lease_time

    @property
    def post_to_cloud(self):
        """Gets the post_to_cloud of this EquipmentLanItem.

        发布到企业连接网络

        :return: The post_to_cloud of this EquipmentLanItem.
        :rtype: bool
        """
        return self._post_to_cloud

    @post_to_cloud.setter
    def post_to_cloud(self, post_to_cloud):
        """Sets the post_to_cloud of this EquipmentLanItem.

        发布到企业连接网络

        :param post_to_cloud: The post_to_cloud of this EquipmentLanItem.
        :type post_to_cloud: bool
        """
        self._post_to_cloud = post_to_cloud

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
        if not isinstance(other, EquipmentLanItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
