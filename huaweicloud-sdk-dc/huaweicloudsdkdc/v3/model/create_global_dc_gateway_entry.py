# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateGlobalDcGatewayEntry:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'tenant_id': 'str',
        'name': 'str',
        'description': 'str',
        'enterprise_project_id': 'str',
        'global_center_network_id': 'str',
        'bgp_asn': 'int',
        'region_id': 'str',
        'location_name': 'str',
        'current_peer_link_count': 'int',
        'available_peer_link_count': 'int',
        'tags': 'list[Tag]',
        'admin_state_up': 'bool',
        'status': 'GlobalDcGatewayStatus',
        'created_time': 'datetime',
        'address_family': 'str'
    }

    attribute_map = {
        'id': 'id',
        'tenant_id': 'tenant_id',
        'name': 'name',
        'description': 'description',
        'enterprise_project_id': 'enterprise_project_id',
        'global_center_network_id': 'global_center_network_id',
        'bgp_asn': 'bgp_asn',
        'region_id': 'region_id',
        'location_name': 'location_name',
        'current_peer_link_count': 'current_peer_link_count',
        'available_peer_link_count': 'available_peer_link_count',
        'tags': 'tags',
        'admin_state_up': 'admin_state_up',
        'status': 'status',
        'created_time': 'created_time',
        'address_family': 'address_family'
    }

    def __init__(self, id=None, tenant_id=None, name=None, description=None, enterprise_project_id=None, global_center_network_id=None, bgp_asn=None, region_id=None, location_name=None, current_peer_link_count=None, available_peer_link_count=None, tags=None, admin_state_up=None, status=None, created_time=None, address_family=None):
        r"""CreateGlobalDcGatewayEntry

        The model defined in huaweicloud sdk

        :param id: 专线全域接入网关（global-dc-gateway）ID
        :type id: str
        :param tenant_id: 项目ID。
        :type tenant_id: str
        :param name: global-dc-gateway名字。
        :type name: str
        :param description: 描述信息
        :type description: str
        :param enterprise_project_id: global-dc-gateway所属的企业项目ID。
        :type enterprise_project_id: str
        :param global_center_network_id: DGW加载的全球中心网络实例的ID
        :type global_center_network_id: str
        :param bgp_asn: DGW对应BGP的ASN编号
        :type bgp_asn: int
        :param region_id: DGW所属Region
        :type region_id: str
        :param location_name: DGW创建网关设备归属的位置
        :type location_name: str
        :param current_peer_link_count: 全域接入网关(GDGW)上关联连接的数量，表示DGW挂载ER的数量
        :type current_peer_link_count: int
        :param available_peer_link_count: 该全域接入网关上GDGW允许创建关联连接（PeerLink）的数量
        :type available_peer_link_count: int
        :param tags: global-dc-gateway关联TAG。
        :type tags: list[:class:`huaweicloudsdkdc.v3.Tag`]
        :param admin_state_up: 该GDGW的管理状态，true为激活状态、false为冻结状态
        :type admin_state_up: bool
        :param status: 
        :type status: :class:`huaweicloudsdkdc.v3.GlobalDcGatewayStatus`
        :param created_time: 创建时间。
        :type created_time: datetime
        :param address_family: 网关的地址簇，IPv4或者ipv6和IPv4双栈 - ipv4 - dual
        :type address_family: str
        """
        
        

        self._id = None
        self._tenant_id = None
        self._name = None
        self._description = None
        self._enterprise_project_id = None
        self._global_center_network_id = None
        self._bgp_asn = None
        self._region_id = None
        self._location_name = None
        self._current_peer_link_count = None
        self._available_peer_link_count = None
        self._tags = None
        self._admin_state_up = None
        self._status = None
        self._created_time = None
        self._address_family = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if global_center_network_id is not None:
            self.global_center_network_id = global_center_network_id
        if bgp_asn is not None:
            self.bgp_asn = bgp_asn
        if region_id is not None:
            self.region_id = region_id
        if location_name is not None:
            self.location_name = location_name
        if current_peer_link_count is not None:
            self.current_peer_link_count = current_peer_link_count
        if available_peer_link_count is not None:
            self.available_peer_link_count = available_peer_link_count
        if tags is not None:
            self.tags = tags
        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if status is not None:
            self.status = status
        if created_time is not None:
            self.created_time = created_time
        if address_family is not None:
            self.address_family = address_family

    @property
    def id(self):
        r"""Gets the id of this CreateGlobalDcGatewayEntry.

        专线全域接入网关（global-dc-gateway）ID

        :return: The id of this CreateGlobalDcGatewayEntry.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CreateGlobalDcGatewayEntry.

        专线全域接入网关（global-dc-gateway）ID

        :param id: The id of this CreateGlobalDcGatewayEntry.
        :type id: str
        """
        self._id = id

    @property
    def tenant_id(self):
        r"""Gets the tenant_id of this CreateGlobalDcGatewayEntry.

        项目ID。

        :return: The tenant_id of this CreateGlobalDcGatewayEntry.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        r"""Sets the tenant_id of this CreateGlobalDcGatewayEntry.

        项目ID。

        :param tenant_id: The tenant_id of this CreateGlobalDcGatewayEntry.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def name(self):
        r"""Gets the name of this CreateGlobalDcGatewayEntry.

        global-dc-gateway名字。

        :return: The name of this CreateGlobalDcGatewayEntry.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateGlobalDcGatewayEntry.

        global-dc-gateway名字。

        :param name: The name of this CreateGlobalDcGatewayEntry.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this CreateGlobalDcGatewayEntry.

        描述信息

        :return: The description of this CreateGlobalDcGatewayEntry.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateGlobalDcGatewayEntry.

        描述信息

        :param description: The description of this CreateGlobalDcGatewayEntry.
        :type description: str
        """
        self._description = description

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this CreateGlobalDcGatewayEntry.

        global-dc-gateway所属的企业项目ID。

        :return: The enterprise_project_id of this CreateGlobalDcGatewayEntry.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this CreateGlobalDcGatewayEntry.

        global-dc-gateway所属的企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this CreateGlobalDcGatewayEntry.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def global_center_network_id(self):
        r"""Gets the global_center_network_id of this CreateGlobalDcGatewayEntry.

        DGW加载的全球中心网络实例的ID

        :return: The global_center_network_id of this CreateGlobalDcGatewayEntry.
        :rtype: str
        """
        return self._global_center_network_id

    @global_center_network_id.setter
    def global_center_network_id(self, global_center_network_id):
        r"""Sets the global_center_network_id of this CreateGlobalDcGatewayEntry.

        DGW加载的全球中心网络实例的ID

        :param global_center_network_id: The global_center_network_id of this CreateGlobalDcGatewayEntry.
        :type global_center_network_id: str
        """
        self._global_center_network_id = global_center_network_id

    @property
    def bgp_asn(self):
        r"""Gets the bgp_asn of this CreateGlobalDcGatewayEntry.

        DGW对应BGP的ASN编号

        :return: The bgp_asn of this CreateGlobalDcGatewayEntry.
        :rtype: int
        """
        return self._bgp_asn

    @bgp_asn.setter
    def bgp_asn(self, bgp_asn):
        r"""Sets the bgp_asn of this CreateGlobalDcGatewayEntry.

        DGW对应BGP的ASN编号

        :param bgp_asn: The bgp_asn of this CreateGlobalDcGatewayEntry.
        :type bgp_asn: int
        """
        self._bgp_asn = bgp_asn

    @property
    def region_id(self):
        r"""Gets the region_id of this CreateGlobalDcGatewayEntry.

        DGW所属Region

        :return: The region_id of this CreateGlobalDcGatewayEntry.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this CreateGlobalDcGatewayEntry.

        DGW所属Region

        :param region_id: The region_id of this CreateGlobalDcGatewayEntry.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def location_name(self):
        r"""Gets the location_name of this CreateGlobalDcGatewayEntry.

        DGW创建网关设备归属的位置

        :return: The location_name of this CreateGlobalDcGatewayEntry.
        :rtype: str
        """
        return self._location_name

    @location_name.setter
    def location_name(self, location_name):
        r"""Sets the location_name of this CreateGlobalDcGatewayEntry.

        DGW创建网关设备归属的位置

        :param location_name: The location_name of this CreateGlobalDcGatewayEntry.
        :type location_name: str
        """
        self._location_name = location_name

    @property
    def current_peer_link_count(self):
        r"""Gets the current_peer_link_count of this CreateGlobalDcGatewayEntry.

        全域接入网关(GDGW)上关联连接的数量，表示DGW挂载ER的数量

        :return: The current_peer_link_count of this CreateGlobalDcGatewayEntry.
        :rtype: int
        """
        return self._current_peer_link_count

    @current_peer_link_count.setter
    def current_peer_link_count(self, current_peer_link_count):
        r"""Sets the current_peer_link_count of this CreateGlobalDcGatewayEntry.

        全域接入网关(GDGW)上关联连接的数量，表示DGW挂载ER的数量

        :param current_peer_link_count: The current_peer_link_count of this CreateGlobalDcGatewayEntry.
        :type current_peer_link_count: int
        """
        self._current_peer_link_count = current_peer_link_count

    @property
    def available_peer_link_count(self):
        r"""Gets the available_peer_link_count of this CreateGlobalDcGatewayEntry.

        该全域接入网关上GDGW允许创建关联连接（PeerLink）的数量

        :return: The available_peer_link_count of this CreateGlobalDcGatewayEntry.
        :rtype: int
        """
        return self._available_peer_link_count

    @available_peer_link_count.setter
    def available_peer_link_count(self, available_peer_link_count):
        r"""Sets the available_peer_link_count of this CreateGlobalDcGatewayEntry.

        该全域接入网关上GDGW允许创建关联连接（PeerLink）的数量

        :param available_peer_link_count: The available_peer_link_count of this CreateGlobalDcGatewayEntry.
        :type available_peer_link_count: int
        """
        self._available_peer_link_count = available_peer_link_count

    @property
    def tags(self):
        r"""Gets the tags of this CreateGlobalDcGatewayEntry.

        global-dc-gateway关联TAG。

        :return: The tags of this CreateGlobalDcGatewayEntry.
        :rtype: list[:class:`huaweicloudsdkdc.v3.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this CreateGlobalDcGatewayEntry.

        global-dc-gateway关联TAG。

        :param tags: The tags of this CreateGlobalDcGatewayEntry.
        :type tags: list[:class:`huaweicloudsdkdc.v3.Tag`]
        """
        self._tags = tags

    @property
    def admin_state_up(self):
        r"""Gets the admin_state_up of this CreateGlobalDcGatewayEntry.

        该GDGW的管理状态，true为激活状态、false为冻结状态

        :return: The admin_state_up of this CreateGlobalDcGatewayEntry.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        r"""Sets the admin_state_up of this CreateGlobalDcGatewayEntry.

        该GDGW的管理状态，true为激活状态、false为冻结状态

        :param admin_state_up: The admin_state_up of this CreateGlobalDcGatewayEntry.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def status(self):
        r"""Gets the status of this CreateGlobalDcGatewayEntry.

        :return: The status of this CreateGlobalDcGatewayEntry.
        :rtype: :class:`huaweicloudsdkdc.v3.GlobalDcGatewayStatus`
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CreateGlobalDcGatewayEntry.

        :param status: The status of this CreateGlobalDcGatewayEntry.
        :type status: :class:`huaweicloudsdkdc.v3.GlobalDcGatewayStatus`
        """
        self._status = status

    @property
    def created_time(self):
        r"""Gets the created_time of this CreateGlobalDcGatewayEntry.

        创建时间。

        :return: The created_time of this CreateGlobalDcGatewayEntry.
        :rtype: datetime
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        r"""Sets the created_time of this CreateGlobalDcGatewayEntry.

        创建时间。

        :param created_time: The created_time of this CreateGlobalDcGatewayEntry.
        :type created_time: datetime
        """
        self._created_time = created_time

    @property
    def address_family(self):
        r"""Gets the address_family of this CreateGlobalDcGatewayEntry.

        网关的地址簇，IPv4或者ipv6和IPv4双栈 - ipv4 - dual

        :return: The address_family of this CreateGlobalDcGatewayEntry.
        :rtype: str
        """
        return self._address_family

    @address_family.setter
    def address_family(self, address_family):
        r"""Sets the address_family of this CreateGlobalDcGatewayEntry.

        网关的地址簇，IPv4或者ipv6和IPv4双栈 - ipv4 - dual

        :param address_family: The address_family of this CreateGlobalDcGatewayEntry.
        :type address_family: str
        """
        self._address_family = address_family

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
        if not isinstance(other, CreateGlobalDcGatewayEntry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
