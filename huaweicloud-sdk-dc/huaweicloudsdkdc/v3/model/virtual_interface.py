# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VirtualInterface:

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
        'name': 'str',
        'admin_state_up': 'bool',
        'bandwidth': 'int',
        'create_time': 'datetime',
        'update_time': 'datetime',
        'description': 'str',
        'direct_connect_id': 'str',
        'service_type': 'str',
        'status': 'str',
        'tenant_id': 'str',
        'type': 'str',
        'vgw_id': 'str',
        'vlan': 'int',
        'route_limit': 'int',
        'enable_nqa': 'bool',
        'enable_bfd': 'bool',
        'lag_id': 'str',
        'device_id': 'str',
        'enterprise_project_id': 'str',
        'tags': 'list[Tag]',
        'vif_peers': 'list[VifPeer]',
        'extend_attribute': 'VifExtendAttribute'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'admin_state_up': 'admin_state_up',
        'bandwidth': 'bandwidth',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'description': 'description',
        'direct_connect_id': 'direct_connect_id',
        'service_type': 'service_type',
        'status': 'status',
        'tenant_id': 'tenant_id',
        'type': 'type',
        'vgw_id': 'vgw_id',
        'vlan': 'vlan',
        'route_limit': 'route_limit',
        'enable_nqa': 'enable_nqa',
        'enable_bfd': 'enable_bfd',
        'lag_id': 'lag_id',
        'device_id': 'device_id',
        'enterprise_project_id': 'enterprise_project_id',
        'tags': 'tags',
        'vif_peers': 'vif_peers',
        'extend_attribute': 'extend_attribute'
    }

    def __init__(self, id=None, name=None, admin_state_up=None, bandwidth=None, create_time=None, update_time=None, description=None, direct_connect_id=None, service_type=None, status=None, tenant_id=None, type=None, vgw_id=None, vlan=None, route_limit=None, enable_nqa=None, enable_bfd=None, lag_id=None, device_id=None, enterprise_project_id=None, tags=None, vif_peers=None, extend_attribute=None):
        """VirtualInterface

        The model defined in huaweicloud sdk

        :param id: 虚拟接口的ID
        :type id: str
        :param name: 虚拟接口的名字
        :type name: str
        :param admin_state_up: 管理状态：true或false
        :type admin_state_up: bool
        :param bandwidth: 虚拟接口接入带宽
        :type bandwidth: int
        :param create_time: 虚拟接口创建时间
        :type create_time: datetime
        :param update_time: 虚拟接口更新时间
        :type update_time: datetime
        :param description: 虚拟接口的描述
        :type description: str
        :param direct_connect_id: 物理专线的ID
        :type direct_connect_id: str
        :param service_type: 接入网关的类型：包括VGW,GDGW,LGW等
        :type service_type: str
        :param status: 操作状态，合法值是：ACTIVE，DOWN，BUILD，ERROR，PENDING_CREATE，PENDING_UPDATE，PENDING_DELETE，DELETED，AUTHORIZATION，REJECTED
        :type status: str
        :param tenant_id: 租户ID
        :type tenant_id: str
        :param type: 接口类型：private/public,
        :type type: str
        :param vgw_id: 虚拟网关的ID
        :type vgw_id: str
        :param vlan: 同用户网关对接的vlan, 配置范围0-3999
        :type vlan: int
        :param route_limit: VIF远端子网路由配置规格
        :type route_limit: int
        :param enable_nqa: 是否使能nqa功能：true或false
        :type enable_nqa: bool
        :param enable_bfd: 是否使能nqa功能：true或false
        :type enable_bfd: bool
        :param lag_id: VIF关联的链路聚合组ID
        :type lag_id: str
        :param device_id: 归属的设备ID
        :type device_id: str
        :param enterprise_project_id: 实例所属企业项目ID
        :type enterprise_project_id: str
        :param tags: 标签信息
        :type tags: list[:class:`huaweicloudsdkdc.v3.Tag`]
        :param vif_peers: vif的Peer的相关信息
        :type vif_peers: list[:class:`huaweicloudsdkdc.v3.VifPeer`]
        :param extend_attribute: 
        :type extend_attribute: :class:`huaweicloudsdkdc.v3.VifExtendAttribute`
        """
        
        

        self._id = None
        self._name = None
        self._admin_state_up = None
        self._bandwidth = None
        self._create_time = None
        self._update_time = None
        self._description = None
        self._direct_connect_id = None
        self._service_type = None
        self._status = None
        self._tenant_id = None
        self._type = None
        self._vgw_id = None
        self._vlan = None
        self._route_limit = None
        self._enable_nqa = None
        self._enable_bfd = None
        self._lag_id = None
        self._device_id = None
        self._enterprise_project_id = None
        self._tags = None
        self._vif_peers = None
        self._extend_attribute = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if bandwidth is not None:
            self.bandwidth = bandwidth
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if description is not None:
            self.description = description
        if direct_connect_id is not None:
            self.direct_connect_id = direct_connect_id
        if service_type is not None:
            self.service_type = service_type
        if status is not None:
            self.status = status
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if type is not None:
            self.type = type
        if vgw_id is not None:
            self.vgw_id = vgw_id
        if vlan is not None:
            self.vlan = vlan
        if route_limit is not None:
            self.route_limit = route_limit
        if enable_nqa is not None:
            self.enable_nqa = enable_nqa
        if enable_bfd is not None:
            self.enable_bfd = enable_bfd
        if lag_id is not None:
            self.lag_id = lag_id
        if device_id is not None:
            self.device_id = device_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if tags is not None:
            self.tags = tags
        if vif_peers is not None:
            self.vif_peers = vif_peers
        if extend_attribute is not None:
            self.extend_attribute = extend_attribute

    @property
    def id(self):
        """Gets the id of this VirtualInterface.

        虚拟接口的ID

        :return: The id of this VirtualInterface.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VirtualInterface.

        虚拟接口的ID

        :param id: The id of this VirtualInterface.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this VirtualInterface.

        虚拟接口的名字

        :return: The name of this VirtualInterface.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VirtualInterface.

        虚拟接口的名字

        :param name: The name of this VirtualInterface.
        :type name: str
        """
        self._name = name

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this VirtualInterface.

        管理状态：true或false

        :return: The admin_state_up of this VirtualInterface.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this VirtualInterface.

        管理状态：true或false

        :param admin_state_up: The admin_state_up of this VirtualInterface.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def bandwidth(self):
        """Gets the bandwidth of this VirtualInterface.

        虚拟接口接入带宽

        :return: The bandwidth of this VirtualInterface.
        :rtype: int
        """
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, bandwidth):
        """Sets the bandwidth of this VirtualInterface.

        虚拟接口接入带宽

        :param bandwidth: The bandwidth of this VirtualInterface.
        :type bandwidth: int
        """
        self._bandwidth = bandwidth

    @property
    def create_time(self):
        """Gets the create_time of this VirtualInterface.

        虚拟接口创建时间

        :return: The create_time of this VirtualInterface.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this VirtualInterface.

        虚拟接口创建时间

        :param create_time: The create_time of this VirtualInterface.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this VirtualInterface.

        虚拟接口更新时间

        :return: The update_time of this VirtualInterface.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this VirtualInterface.

        虚拟接口更新时间

        :param update_time: The update_time of this VirtualInterface.
        :type update_time: datetime
        """
        self._update_time = update_time

    @property
    def description(self):
        """Gets the description of this VirtualInterface.

        虚拟接口的描述

        :return: The description of this VirtualInterface.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this VirtualInterface.

        虚拟接口的描述

        :param description: The description of this VirtualInterface.
        :type description: str
        """
        self._description = description

    @property
    def direct_connect_id(self):
        """Gets the direct_connect_id of this VirtualInterface.

        物理专线的ID

        :return: The direct_connect_id of this VirtualInterface.
        :rtype: str
        """
        return self._direct_connect_id

    @direct_connect_id.setter
    def direct_connect_id(self, direct_connect_id):
        """Sets the direct_connect_id of this VirtualInterface.

        物理专线的ID

        :param direct_connect_id: The direct_connect_id of this VirtualInterface.
        :type direct_connect_id: str
        """
        self._direct_connect_id = direct_connect_id

    @property
    def service_type(self):
        """Gets the service_type of this VirtualInterface.

        接入网关的类型：包括VGW,GDGW,LGW等

        :return: The service_type of this VirtualInterface.
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        """Sets the service_type of this VirtualInterface.

        接入网关的类型：包括VGW,GDGW,LGW等

        :param service_type: The service_type of this VirtualInterface.
        :type service_type: str
        """
        self._service_type = service_type

    @property
    def status(self):
        """Gets the status of this VirtualInterface.

        操作状态，合法值是：ACTIVE，DOWN，BUILD，ERROR，PENDING_CREATE，PENDING_UPDATE，PENDING_DELETE，DELETED，AUTHORIZATION，REJECTED

        :return: The status of this VirtualInterface.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this VirtualInterface.

        操作状态，合法值是：ACTIVE，DOWN，BUILD，ERROR，PENDING_CREATE，PENDING_UPDATE，PENDING_DELETE，DELETED，AUTHORIZATION，REJECTED

        :param status: The status of this VirtualInterface.
        :type status: str
        """
        self._status = status

    @property
    def tenant_id(self):
        """Gets the tenant_id of this VirtualInterface.

        租户ID

        :return: The tenant_id of this VirtualInterface.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this VirtualInterface.

        租户ID

        :param tenant_id: The tenant_id of this VirtualInterface.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def type(self):
        """Gets the type of this VirtualInterface.

        接口类型：private/public,

        :return: The type of this VirtualInterface.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this VirtualInterface.

        接口类型：private/public,

        :param type: The type of this VirtualInterface.
        :type type: str
        """
        self._type = type

    @property
    def vgw_id(self):
        """Gets the vgw_id of this VirtualInterface.

        虚拟网关的ID

        :return: The vgw_id of this VirtualInterface.
        :rtype: str
        """
        return self._vgw_id

    @vgw_id.setter
    def vgw_id(self, vgw_id):
        """Sets the vgw_id of this VirtualInterface.

        虚拟网关的ID

        :param vgw_id: The vgw_id of this VirtualInterface.
        :type vgw_id: str
        """
        self._vgw_id = vgw_id

    @property
    def vlan(self):
        """Gets the vlan of this VirtualInterface.

        同用户网关对接的vlan, 配置范围0-3999

        :return: The vlan of this VirtualInterface.
        :rtype: int
        """
        return self._vlan

    @vlan.setter
    def vlan(self, vlan):
        """Sets the vlan of this VirtualInterface.

        同用户网关对接的vlan, 配置范围0-3999

        :param vlan: The vlan of this VirtualInterface.
        :type vlan: int
        """
        self._vlan = vlan

    @property
    def route_limit(self):
        """Gets the route_limit of this VirtualInterface.

        VIF远端子网路由配置规格

        :return: The route_limit of this VirtualInterface.
        :rtype: int
        """
        return self._route_limit

    @route_limit.setter
    def route_limit(self, route_limit):
        """Sets the route_limit of this VirtualInterface.

        VIF远端子网路由配置规格

        :param route_limit: The route_limit of this VirtualInterface.
        :type route_limit: int
        """
        self._route_limit = route_limit

    @property
    def enable_nqa(self):
        """Gets the enable_nqa of this VirtualInterface.

        是否使能nqa功能：true或false

        :return: The enable_nqa of this VirtualInterface.
        :rtype: bool
        """
        return self._enable_nqa

    @enable_nqa.setter
    def enable_nqa(self, enable_nqa):
        """Sets the enable_nqa of this VirtualInterface.

        是否使能nqa功能：true或false

        :param enable_nqa: The enable_nqa of this VirtualInterface.
        :type enable_nqa: bool
        """
        self._enable_nqa = enable_nqa

    @property
    def enable_bfd(self):
        """Gets the enable_bfd of this VirtualInterface.

        是否使能nqa功能：true或false

        :return: The enable_bfd of this VirtualInterface.
        :rtype: bool
        """
        return self._enable_bfd

    @enable_bfd.setter
    def enable_bfd(self, enable_bfd):
        """Sets the enable_bfd of this VirtualInterface.

        是否使能nqa功能：true或false

        :param enable_bfd: The enable_bfd of this VirtualInterface.
        :type enable_bfd: bool
        """
        self._enable_bfd = enable_bfd

    @property
    def lag_id(self):
        """Gets the lag_id of this VirtualInterface.

        VIF关联的链路聚合组ID

        :return: The lag_id of this VirtualInterface.
        :rtype: str
        """
        return self._lag_id

    @lag_id.setter
    def lag_id(self, lag_id):
        """Sets the lag_id of this VirtualInterface.

        VIF关联的链路聚合组ID

        :param lag_id: The lag_id of this VirtualInterface.
        :type lag_id: str
        """
        self._lag_id = lag_id

    @property
    def device_id(self):
        """Gets the device_id of this VirtualInterface.

        归属的设备ID

        :return: The device_id of this VirtualInterface.
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this VirtualInterface.

        归属的设备ID

        :param device_id: The device_id of this VirtualInterface.
        :type device_id: str
        """
        self._device_id = device_id

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this VirtualInterface.

        实例所属企业项目ID

        :return: The enterprise_project_id of this VirtualInterface.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this VirtualInterface.

        实例所属企业项目ID

        :param enterprise_project_id: The enterprise_project_id of this VirtualInterface.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def tags(self):
        """Gets the tags of this VirtualInterface.

        标签信息

        :return: The tags of this VirtualInterface.
        :rtype: list[:class:`huaweicloudsdkdc.v3.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this VirtualInterface.

        标签信息

        :param tags: The tags of this VirtualInterface.
        :type tags: list[:class:`huaweicloudsdkdc.v3.Tag`]
        """
        self._tags = tags

    @property
    def vif_peers(self):
        """Gets the vif_peers of this VirtualInterface.

        vif的Peer的相关信息

        :return: The vif_peers of this VirtualInterface.
        :rtype: list[:class:`huaweicloudsdkdc.v3.VifPeer`]
        """
        return self._vif_peers

    @vif_peers.setter
    def vif_peers(self, vif_peers):
        """Sets the vif_peers of this VirtualInterface.

        vif的Peer的相关信息

        :param vif_peers: The vif_peers of this VirtualInterface.
        :type vif_peers: list[:class:`huaweicloudsdkdc.v3.VifPeer`]
        """
        self._vif_peers = vif_peers

    @property
    def extend_attribute(self):
        """Gets the extend_attribute of this VirtualInterface.

        :return: The extend_attribute of this VirtualInterface.
        :rtype: :class:`huaweicloudsdkdc.v3.VifExtendAttribute`
        """
        return self._extend_attribute

    @extend_attribute.setter
    def extend_attribute(self, extend_attribute):
        """Sets the extend_attribute of this VirtualInterface.

        :param extend_attribute: The extend_attribute of this VirtualInterface.
        :type extend_attribute: :class:`huaweicloudsdkdc.v3.VifExtendAttribute`
        """
        self._extend_attribute = extend_attribute

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
        if not isinstance(other, VirtualInterface):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
