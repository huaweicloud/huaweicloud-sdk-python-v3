# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NeutronListPortsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'marker': 'str',
        'id': 'str',
        'name': 'str',
        'admin_state_up': 'bool',
        'network_id': 'str',
        'mac_address': 'str',
        'device_id': 'str',
        'device_owner': 'str',
        'status': 'str',
        'security_groups': 'list[str]',
        'fixed_ips': 'list[str]',
        'tenant_id': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker',
        'id': 'id',
        'name': 'name',
        'admin_state_up': 'admin_state_up',
        'network_id': 'network_id',
        'mac_address': 'mac_address',
        'device_id': 'device_id',
        'device_owner': 'device_owner',
        'status': 'status',
        'security_groups': 'security_groups',
        'fixed_ips': 'fixed_ips',
        'tenant_id': 'tenant_id'
    }

    def __init__(self, limit=None, marker=None, id=None, name=None, admin_state_up=None, network_id=None, mac_address=None, device_id=None, device_owner=None, status=None, security_groups=None, fixed_ips=None, tenant_id=None):
        """NeutronListPortsRequest

        The model defined in huaweicloud sdk

        :param limit: 每页返回的个数
        :type limit: int
        :param marker: 分页查询起始的资源ID，为空时查询第一页
        :type marker: str
        :param id: 按照端口的ID过滤查询
        :type id: str
        :param name: 按照端口的名称过滤查询
        :type name: str
        :param admin_state_up: 按照端口的管理状态过滤查询，取值范围：true or false
        :type admin_state_up: bool
        :param network_id: 按照端口所属的网络ID过滤查询
        :type network_id: str
        :param mac_address: 按照端口的mac地址过滤查询
        :type mac_address: str
        :param device_id: 按照端口的设备ID过滤查询
        :type device_id: str
        :param device_owner: 按照端口的设备所属过滤查询
        :type device_owner: str
        :param status: 按照端口状态过滤查询，取值范围：ACTIVE、BUILD、DOWN
        :type status: str
        :param security_groups: 按照安全组ID列表过滤查询
        :type security_groups: list[str]
        :param fixed_ips: 按照端口的IP地址过滤查询，fixed_ips&#x3D;ip_address或者fixed_ips&#x3D;subnet_id过滤查询
        :type fixed_ips: list[str]
        :param tenant_id: 按照端口所属的项目ID过滤查询
        :type tenant_id: str
        """
        
        

        self._limit = None
        self._marker = None
        self._id = None
        self._name = None
        self._admin_state_up = None
        self._network_id = None
        self._mac_address = None
        self._device_id = None
        self._device_owner = None
        self._status = None
        self._security_groups = None
        self._fixed_ips = None
        self._tenant_id = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if network_id is not None:
            self.network_id = network_id
        if mac_address is not None:
            self.mac_address = mac_address
        if device_id is not None:
            self.device_id = device_id
        if device_owner is not None:
            self.device_owner = device_owner
        if status is not None:
            self.status = status
        if security_groups is not None:
            self.security_groups = security_groups
        if fixed_ips is not None:
            self.fixed_ips = fixed_ips
        if tenant_id is not None:
            self.tenant_id = tenant_id

    @property
    def limit(self):
        """Gets the limit of this NeutronListPortsRequest.

        每页返回的个数

        :return: The limit of this NeutronListPortsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this NeutronListPortsRequest.

        每页返回的个数

        :param limit: The limit of this NeutronListPortsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this NeutronListPortsRequest.

        分页查询起始的资源ID，为空时查询第一页

        :return: The marker of this NeutronListPortsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this NeutronListPortsRequest.

        分页查询起始的资源ID，为空时查询第一页

        :param marker: The marker of this NeutronListPortsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def id(self):
        """Gets the id of this NeutronListPortsRequest.

        按照端口的ID过滤查询

        :return: The id of this NeutronListPortsRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NeutronListPortsRequest.

        按照端口的ID过滤查询

        :param id: The id of this NeutronListPortsRequest.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this NeutronListPortsRequest.

        按照端口的名称过滤查询

        :return: The name of this NeutronListPortsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NeutronListPortsRequest.

        按照端口的名称过滤查询

        :param name: The name of this NeutronListPortsRequest.
        :type name: str
        """
        self._name = name

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this NeutronListPortsRequest.

        按照端口的管理状态过滤查询，取值范围：true or false

        :return: The admin_state_up of this NeutronListPortsRequest.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this NeutronListPortsRequest.

        按照端口的管理状态过滤查询，取值范围：true or false

        :param admin_state_up: The admin_state_up of this NeutronListPortsRequest.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def network_id(self):
        """Gets the network_id of this NeutronListPortsRequest.

        按照端口所属的网络ID过滤查询

        :return: The network_id of this NeutronListPortsRequest.
        :rtype: str
        """
        return self._network_id

    @network_id.setter
    def network_id(self, network_id):
        """Sets the network_id of this NeutronListPortsRequest.

        按照端口所属的网络ID过滤查询

        :param network_id: The network_id of this NeutronListPortsRequest.
        :type network_id: str
        """
        self._network_id = network_id

    @property
    def mac_address(self):
        """Gets the mac_address of this NeutronListPortsRequest.

        按照端口的mac地址过滤查询

        :return: The mac_address of this NeutronListPortsRequest.
        :rtype: str
        """
        return self._mac_address

    @mac_address.setter
    def mac_address(self, mac_address):
        """Sets the mac_address of this NeutronListPortsRequest.

        按照端口的mac地址过滤查询

        :param mac_address: The mac_address of this NeutronListPortsRequest.
        :type mac_address: str
        """
        self._mac_address = mac_address

    @property
    def device_id(self):
        """Gets the device_id of this NeutronListPortsRequest.

        按照端口的设备ID过滤查询

        :return: The device_id of this NeutronListPortsRequest.
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this NeutronListPortsRequest.

        按照端口的设备ID过滤查询

        :param device_id: The device_id of this NeutronListPortsRequest.
        :type device_id: str
        """
        self._device_id = device_id

    @property
    def device_owner(self):
        """Gets the device_owner of this NeutronListPortsRequest.

        按照端口的设备所属过滤查询

        :return: The device_owner of this NeutronListPortsRequest.
        :rtype: str
        """
        return self._device_owner

    @device_owner.setter
    def device_owner(self, device_owner):
        """Sets the device_owner of this NeutronListPortsRequest.

        按照端口的设备所属过滤查询

        :param device_owner: The device_owner of this NeutronListPortsRequest.
        :type device_owner: str
        """
        self._device_owner = device_owner

    @property
    def status(self):
        """Gets the status of this NeutronListPortsRequest.

        按照端口状态过滤查询，取值范围：ACTIVE、BUILD、DOWN

        :return: The status of this NeutronListPortsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this NeutronListPortsRequest.

        按照端口状态过滤查询，取值范围：ACTIVE、BUILD、DOWN

        :param status: The status of this NeutronListPortsRequest.
        :type status: str
        """
        self._status = status

    @property
    def security_groups(self):
        """Gets the security_groups of this NeutronListPortsRequest.

        按照安全组ID列表过滤查询

        :return: The security_groups of this NeutronListPortsRequest.
        :rtype: list[str]
        """
        return self._security_groups

    @security_groups.setter
    def security_groups(self, security_groups):
        """Sets the security_groups of this NeutronListPortsRequest.

        按照安全组ID列表过滤查询

        :param security_groups: The security_groups of this NeutronListPortsRequest.
        :type security_groups: list[str]
        """
        self._security_groups = security_groups

    @property
    def fixed_ips(self):
        """Gets the fixed_ips of this NeutronListPortsRequest.

        按照端口的IP地址过滤查询，fixed_ips=ip_address或者fixed_ips=subnet_id过滤查询

        :return: The fixed_ips of this NeutronListPortsRequest.
        :rtype: list[str]
        """
        return self._fixed_ips

    @fixed_ips.setter
    def fixed_ips(self, fixed_ips):
        """Sets the fixed_ips of this NeutronListPortsRequest.

        按照端口的IP地址过滤查询，fixed_ips=ip_address或者fixed_ips=subnet_id过滤查询

        :param fixed_ips: The fixed_ips of this NeutronListPortsRequest.
        :type fixed_ips: list[str]
        """
        self._fixed_ips = fixed_ips

    @property
    def tenant_id(self):
        """Gets the tenant_id of this NeutronListPortsRequest.

        按照端口所属的项目ID过滤查询

        :return: The tenant_id of this NeutronListPortsRequest.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this NeutronListPortsRequest.

        按照端口所属的项目ID过滤查询

        :param tenant_id: The tenant_id of this NeutronListPortsRequest.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

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
        if not isinstance(other, NeutronListPortsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
