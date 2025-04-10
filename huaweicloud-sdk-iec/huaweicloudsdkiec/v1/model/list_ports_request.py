# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPortsRequest:

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
        'offset': 'int',
        'network_id': 'str',
        'id': 'str',
        'name': 'str',
        'admin_state_up': 'bool',
        'fixed_ips': 'list[str]',
        'mac_address': 'str',
        'device_id': 'str',
        'device_owner': 'str',
        'status': 'str',
        'security_groups': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'network_id': 'network_id',
        'id': 'id',
        'name': 'name',
        'admin_state_up': 'admin_state_up',
        'fixed_ips': 'fixed_ips',
        'mac_address': 'mac_address',
        'device_id': 'device_id',
        'device_owner': 'device_owner',
        'status': 'status',
        'security_groups': 'security_groups'
    }

    def __init__(self, limit=None, offset=None, network_id=None, id=None, name=None, admin_state_up=None, fixed_ips=None, mac_address=None, device_id=None, device_owner=None, status=None, security_groups=None):
        r"""ListPortsRequest

        The model defined in huaweicloud sdk

        :param limit: 查询返回端口列表数量。取值范围：0~1000。
        :type limit: int
        :param offset: 查询的偏移量。
        :type offset: int
        :param network_id: 子网的neutron的network的ID。
        :type network_id: str
        :param id: 按照端口ID过滤查询
        :type id: str
        :param name: 按照name过滤查询  取值范围：最大长度不超过255
        :type name: str
        :param admin_state_up: 按照admin_state_up进行过滤  约束：只支持true
        :type admin_state_up: bool
        :param fixed_ips: 根据绑定的IP查询端口。按照fixed_ips&#x3D;ip_address或者fixed_ips&#x3D;subnet_id过滤查询，示例：fixed_ips&#x3D;ip_address&#x3D;xxx&amp;fixed_ips&#x3D;subnet_id&#x3D;xxxx
        :type fixed_ips: list[str]
        :param mac_address: 根据网卡的mac地址查询端口。
        :type mac_address: str
        :param device_id: 根据设备ID查询端口。
        :type device_id: str
        :param device_owner: 根据设备主查询端口。
        :type device_owner: str
        :param status: 按照status过滤查询  取值范围：ACTIVE、BUILD、DOWN
        :type status: str
        :param security_groups: 根据安全组信息ID查询端口。
        :type security_groups: str
        """
        
        

        self._limit = None
        self._offset = None
        self._network_id = None
        self._id = None
        self._name = None
        self._admin_state_up = None
        self._fixed_ips = None
        self._mac_address = None
        self._device_id = None
        self._device_owner = None
        self._status = None
        self._security_groups = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if network_id is not None:
            self.network_id = network_id
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if fixed_ips is not None:
            self.fixed_ips = fixed_ips
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

    @property
    def limit(self):
        r"""Gets the limit of this ListPortsRequest.

        查询返回端口列表数量。取值范围：0~1000。

        :return: The limit of this ListPortsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListPortsRequest.

        查询返回端口列表数量。取值范围：0~1000。

        :param limit: The limit of this ListPortsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListPortsRequest.

        查询的偏移量。

        :return: The offset of this ListPortsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListPortsRequest.

        查询的偏移量。

        :param offset: The offset of this ListPortsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def network_id(self):
        r"""Gets the network_id of this ListPortsRequest.

        子网的neutron的network的ID。

        :return: The network_id of this ListPortsRequest.
        :rtype: str
        """
        return self._network_id

    @network_id.setter
    def network_id(self, network_id):
        r"""Sets the network_id of this ListPortsRequest.

        子网的neutron的network的ID。

        :param network_id: The network_id of this ListPortsRequest.
        :type network_id: str
        """
        self._network_id = network_id

    @property
    def id(self):
        r"""Gets the id of this ListPortsRequest.

        按照端口ID过滤查询

        :return: The id of this ListPortsRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListPortsRequest.

        按照端口ID过滤查询

        :param id: The id of this ListPortsRequest.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ListPortsRequest.

        按照name过滤查询  取值范围：最大长度不超过255

        :return: The name of this ListPortsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListPortsRequest.

        按照name过滤查询  取值范围：最大长度不超过255

        :param name: The name of this ListPortsRequest.
        :type name: str
        """
        self._name = name

    @property
    def admin_state_up(self):
        r"""Gets the admin_state_up of this ListPortsRequest.

        按照admin_state_up进行过滤  约束：只支持true

        :return: The admin_state_up of this ListPortsRequest.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        r"""Sets the admin_state_up of this ListPortsRequest.

        按照admin_state_up进行过滤  约束：只支持true

        :param admin_state_up: The admin_state_up of this ListPortsRequest.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def fixed_ips(self):
        r"""Gets the fixed_ips of this ListPortsRequest.

        根据绑定的IP查询端口。按照fixed_ips=ip_address或者fixed_ips=subnet_id过滤查询，示例：fixed_ips=ip_address=xxx&fixed_ips=subnet_id=xxxx

        :return: The fixed_ips of this ListPortsRequest.
        :rtype: list[str]
        """
        return self._fixed_ips

    @fixed_ips.setter
    def fixed_ips(self, fixed_ips):
        r"""Sets the fixed_ips of this ListPortsRequest.

        根据绑定的IP查询端口。按照fixed_ips=ip_address或者fixed_ips=subnet_id过滤查询，示例：fixed_ips=ip_address=xxx&fixed_ips=subnet_id=xxxx

        :param fixed_ips: The fixed_ips of this ListPortsRequest.
        :type fixed_ips: list[str]
        """
        self._fixed_ips = fixed_ips

    @property
    def mac_address(self):
        r"""Gets the mac_address of this ListPortsRequest.

        根据网卡的mac地址查询端口。

        :return: The mac_address of this ListPortsRequest.
        :rtype: str
        """
        return self._mac_address

    @mac_address.setter
    def mac_address(self, mac_address):
        r"""Sets the mac_address of this ListPortsRequest.

        根据网卡的mac地址查询端口。

        :param mac_address: The mac_address of this ListPortsRequest.
        :type mac_address: str
        """
        self._mac_address = mac_address

    @property
    def device_id(self):
        r"""Gets the device_id of this ListPortsRequest.

        根据设备ID查询端口。

        :return: The device_id of this ListPortsRequest.
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        r"""Sets the device_id of this ListPortsRequest.

        根据设备ID查询端口。

        :param device_id: The device_id of this ListPortsRequest.
        :type device_id: str
        """
        self._device_id = device_id

    @property
    def device_owner(self):
        r"""Gets the device_owner of this ListPortsRequest.

        根据设备主查询端口。

        :return: The device_owner of this ListPortsRequest.
        :rtype: str
        """
        return self._device_owner

    @device_owner.setter
    def device_owner(self, device_owner):
        r"""Sets the device_owner of this ListPortsRequest.

        根据设备主查询端口。

        :param device_owner: The device_owner of this ListPortsRequest.
        :type device_owner: str
        """
        self._device_owner = device_owner

    @property
    def status(self):
        r"""Gets the status of this ListPortsRequest.

        按照status过滤查询  取值范围：ACTIVE、BUILD、DOWN

        :return: The status of this ListPortsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListPortsRequest.

        按照status过滤查询  取值范围：ACTIVE、BUILD、DOWN

        :param status: The status of this ListPortsRequest.
        :type status: str
        """
        self._status = status

    @property
    def security_groups(self):
        r"""Gets the security_groups of this ListPortsRequest.

        根据安全组信息ID查询端口。

        :return: The security_groups of this ListPortsRequest.
        :rtype: str
        """
        return self._security_groups

    @security_groups.setter
    def security_groups(self, security_groups):
        r"""Sets the security_groups of this ListPortsRequest.

        根据安全组信息ID查询端口。

        :param security_groups: The security_groups of this ListPortsRequest.
        :type security_groups: str
        """
        self._security_groups = security_groups

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
        if not isinstance(other, ListPortsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
