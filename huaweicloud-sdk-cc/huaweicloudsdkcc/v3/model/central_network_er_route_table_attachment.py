# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CentralNetworkErRouteTableAttachment:

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
        'description': 'str',
        'domain_id': 'str',
        'state': 'CentralNetworkConnectionStateEnum',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'central_network_id': 'str',
        'central_network_plane_id': 'str',
        'global_connection_bandwidth_id': 'str',
        'is_frozen': 'bool',
        'bandwidth_type': 'BandwidthTypeEnum',
        'bandwidth_size': 'int',
        'enterprise_router_id': 'str',
        'enterprise_router_project_id': 'str',
        'enterprise_router_region_id': 'str',
        'enterprise_router_attachment_id': 'str',
        'enterprise_router_table_id': 'str',
        'enterprise_router_site_code': 'str',
        'attached_er_table_project_id': 'str',
        'attached_er_table_region_id': 'str',
        'attached_er_id': 'str',
        'attached_er_table_id': 'str',
        'attached_er_attachment_id': 'str',
        'attached_er_table_site_code': 'str',
        'hosted_cloud': 'HostedCloudEnum',
        'approved_state': 'ApprovedStateEnum',
        'reason': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'domain_id': 'domain_id',
        'state': 'state',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'central_network_id': 'central_network_id',
        'central_network_plane_id': 'central_network_plane_id',
        'global_connection_bandwidth_id': 'global_connection_bandwidth_id',
        'is_frozen': 'is_frozen',
        'bandwidth_type': 'bandwidth_type',
        'bandwidth_size': 'bandwidth_size',
        'enterprise_router_id': 'enterprise_router_id',
        'enterprise_router_project_id': 'enterprise_router_project_id',
        'enterprise_router_region_id': 'enterprise_router_region_id',
        'enterprise_router_attachment_id': 'enterprise_router_attachment_id',
        'enterprise_router_table_id': 'enterprise_router_table_id',
        'enterprise_router_site_code': 'enterprise_router_site_code',
        'attached_er_table_project_id': 'attached_er_table_project_id',
        'attached_er_table_region_id': 'attached_er_table_region_id',
        'attached_er_id': 'attached_er_id',
        'attached_er_table_id': 'attached_er_table_id',
        'attached_er_attachment_id': 'attached_er_attachment_id',
        'attached_er_table_site_code': 'attached_er_table_site_code',
        'hosted_cloud': 'hosted_cloud',
        'approved_state': 'approved_state',
        'reason': 'reason'
    }

    def __init__(self, id=None, name=None, description=None, domain_id=None, state=None, created_at=None, updated_at=None, central_network_id=None, central_network_plane_id=None, global_connection_bandwidth_id=None, is_frozen=None, bandwidth_type=None, bandwidth_size=None, enterprise_router_id=None, enterprise_router_project_id=None, enterprise_router_region_id=None, enterprise_router_attachment_id=None, enterprise_router_table_id=None, enterprise_router_site_code=None, attached_er_table_project_id=None, attached_er_table_region_id=None, attached_er_id=None, attached_er_table_id=None, attached_er_attachment_id=None, attached_er_table_site_code=None, hosted_cloud=None, approved_state=None, reason=None):
        r"""CentralNetworkErRouteTableAttachment

        The model defined in huaweicloud sdk

        :param id: 实例ID。
        :type id: str
        :param name: 实例名称。
        :type name: str
        :param description: 实例描述。不支持 &lt;&gt;。
        :type description: str
        :param domain_id: 实例所属账号ID。
        :type domain_id: str
        :param state: 
        :type state: :class:`huaweicloudsdkcc.v3.CentralNetworkConnectionStateEnum`
        :param created_at: 实例创建时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。
        :type created_at: datetime
        :param updated_at: 实例更新时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。
        :type updated_at: datetime
        :param central_network_id: 中心网络ID。
        :type central_network_id: str
        :param central_network_plane_id: 中心网络平面ID。
        :type central_network_plane_id: str
        :param global_connection_bandwidth_id: 全域互联带宽ID。
        :type global_connection_bandwidth_id: str
        :param is_frozen: 是否冻结。
        :type is_frozen: bool
        :param bandwidth_type: 
        :type bandwidth_type: :class:`huaweicloudsdkcc.v3.BandwidthTypeEnum`
        :param bandwidth_size: 带宽值，单位Mbps。
        :type bandwidth_size: int
        :param enterprise_router_id: 企业路由器的ID。
        :type enterprise_router_id: str
        :param enterprise_router_project_id: 企业路由器的项目ID。
        :type enterprise_router_project_id: str
        :param enterprise_router_region_id: ER路由器的regionID。
        :type enterprise_router_region_id: str
        :param enterprise_router_attachment_id: 企业路由器的连接ID。
        :type enterprise_router_attachment_id: str
        :param enterprise_router_table_id: 企业路由器的路由表ID。
        :type enterprise_router_table_id: str
        :param enterprise_router_site_code: 中心网络企业路由器的站点编码。
        :type enterprise_router_site_code: str
        :param attached_er_table_project_id: 被挂载的企业路由器的项目ID。
        :type attached_er_table_project_id: str
        :param attached_er_table_region_id: ER路由器的regionID。
        :type attached_er_table_region_id: str
        :param attached_er_id: 被挂载的企业路由器ID。
        :type attached_er_id: str
        :param attached_er_table_id: 被挂载的企业路由器的路由表ID。
        :type attached_er_table_id: str
        :param attached_er_attachment_id: 被挂载的企业路由器的连接ID。
        :type attached_er_attachment_id: str
        :param attached_er_table_site_code: 被挂载的企业路由器的站点编码。
        :type attached_er_table_site_code: str
        :param hosted_cloud: 
        :type hosted_cloud: :class:`huaweicloudsdkcc.v3.HostedCloudEnum`
        :param approved_state: 
        :type approved_state: :class:`huaweicloudsdkcc.v3.ApprovedStateEnum`
        :param reason: 审批拒绝创建企业路由表附件的原因。
        :type reason: str
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._domain_id = None
        self._state = None
        self._created_at = None
        self._updated_at = None
        self._central_network_id = None
        self._central_network_plane_id = None
        self._global_connection_bandwidth_id = None
        self._is_frozen = None
        self._bandwidth_type = None
        self._bandwidth_size = None
        self._enterprise_router_id = None
        self._enterprise_router_project_id = None
        self._enterprise_router_region_id = None
        self._enterprise_router_attachment_id = None
        self._enterprise_router_table_id = None
        self._enterprise_router_site_code = None
        self._attached_er_table_project_id = None
        self._attached_er_table_region_id = None
        self._attached_er_id = None
        self._attached_er_table_id = None
        self._attached_er_attachment_id = None
        self._attached_er_table_site_code = None
        self._hosted_cloud = None
        self._approved_state = None
        self._reason = None
        self.discriminator = None

        self.id = id
        self.name = name
        if description is not None:
            self.description = description
        self.domain_id = domain_id
        self.state = state
        self.created_at = created_at
        self.updated_at = updated_at
        self.central_network_id = central_network_id
        self.central_network_plane_id = central_network_plane_id
        if global_connection_bandwidth_id is not None:
            self.global_connection_bandwidth_id = global_connection_bandwidth_id
        self.is_frozen = is_frozen
        self.bandwidth_type = bandwidth_type
        if bandwidth_size is not None:
            self.bandwidth_size = bandwidth_size
        self.enterprise_router_id = enterprise_router_id
        self.enterprise_router_project_id = enterprise_router_project_id
        self.enterprise_router_region_id = enterprise_router_region_id
        if enterprise_router_attachment_id is not None:
            self.enterprise_router_attachment_id = enterprise_router_attachment_id
        self.enterprise_router_table_id = enterprise_router_table_id
        self.enterprise_router_site_code = enterprise_router_site_code
        self.attached_er_table_project_id = attached_er_table_project_id
        self.attached_er_table_region_id = attached_er_table_region_id
        self.attached_er_id = attached_er_id
        self.attached_er_table_id = attached_er_table_id
        if attached_er_attachment_id is not None:
            self.attached_er_attachment_id = attached_er_attachment_id
        self.attached_er_table_site_code = attached_er_table_site_code
        if hosted_cloud is not None:
            self.hosted_cloud = hosted_cloud
        self.approved_state = approved_state
        if reason is not None:
            self.reason = reason

    @property
    def id(self):
        r"""Gets the id of this CentralNetworkErRouteTableAttachment.

        实例ID。

        :return: The id of this CentralNetworkErRouteTableAttachment.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CentralNetworkErRouteTableAttachment.

        实例ID。

        :param id: The id of this CentralNetworkErRouteTableAttachment.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this CentralNetworkErRouteTableAttachment.

        实例名称。

        :return: The name of this CentralNetworkErRouteTableAttachment.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CentralNetworkErRouteTableAttachment.

        实例名称。

        :param name: The name of this CentralNetworkErRouteTableAttachment.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this CentralNetworkErRouteTableAttachment.

        实例描述。不支持 <>。

        :return: The description of this CentralNetworkErRouteTableAttachment.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CentralNetworkErRouteTableAttachment.

        实例描述。不支持 <>。

        :param description: The description of this CentralNetworkErRouteTableAttachment.
        :type description: str
        """
        self._description = description

    @property
    def domain_id(self):
        r"""Gets the domain_id of this CentralNetworkErRouteTableAttachment.

        实例所属账号ID。

        :return: The domain_id of this CentralNetworkErRouteTableAttachment.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this CentralNetworkErRouteTableAttachment.

        实例所属账号ID。

        :param domain_id: The domain_id of this CentralNetworkErRouteTableAttachment.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def state(self):
        r"""Gets the state of this CentralNetworkErRouteTableAttachment.

        :return: The state of this CentralNetworkErRouteTableAttachment.
        :rtype: :class:`huaweicloudsdkcc.v3.CentralNetworkConnectionStateEnum`
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this CentralNetworkErRouteTableAttachment.

        :param state: The state of this CentralNetworkErRouteTableAttachment.
        :type state: :class:`huaweicloudsdkcc.v3.CentralNetworkConnectionStateEnum`
        """
        self._state = state

    @property
    def created_at(self):
        r"""Gets the created_at of this CentralNetworkErRouteTableAttachment.

        实例创建时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。

        :return: The created_at of this CentralNetworkErRouteTableAttachment.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this CentralNetworkErRouteTableAttachment.

        实例创建时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。

        :param created_at: The created_at of this CentralNetworkErRouteTableAttachment.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this CentralNetworkErRouteTableAttachment.

        实例更新时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。

        :return: The updated_at of this CentralNetworkErRouteTableAttachment.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this CentralNetworkErRouteTableAttachment.

        实例更新时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。

        :param updated_at: The updated_at of this CentralNetworkErRouteTableAttachment.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

    @property
    def central_network_id(self):
        r"""Gets the central_network_id of this CentralNetworkErRouteTableAttachment.

        中心网络ID。

        :return: The central_network_id of this CentralNetworkErRouteTableAttachment.
        :rtype: str
        """
        return self._central_network_id

    @central_network_id.setter
    def central_network_id(self, central_network_id):
        r"""Sets the central_network_id of this CentralNetworkErRouteTableAttachment.

        中心网络ID。

        :param central_network_id: The central_network_id of this CentralNetworkErRouteTableAttachment.
        :type central_network_id: str
        """
        self._central_network_id = central_network_id

    @property
    def central_network_plane_id(self):
        r"""Gets the central_network_plane_id of this CentralNetworkErRouteTableAttachment.

        中心网络平面ID。

        :return: The central_network_plane_id of this CentralNetworkErRouteTableAttachment.
        :rtype: str
        """
        return self._central_network_plane_id

    @central_network_plane_id.setter
    def central_network_plane_id(self, central_network_plane_id):
        r"""Sets the central_network_plane_id of this CentralNetworkErRouteTableAttachment.

        中心网络平面ID。

        :param central_network_plane_id: The central_network_plane_id of this CentralNetworkErRouteTableAttachment.
        :type central_network_plane_id: str
        """
        self._central_network_plane_id = central_network_plane_id

    @property
    def global_connection_bandwidth_id(self):
        r"""Gets the global_connection_bandwidth_id of this CentralNetworkErRouteTableAttachment.

        全域互联带宽ID。

        :return: The global_connection_bandwidth_id of this CentralNetworkErRouteTableAttachment.
        :rtype: str
        """
        return self._global_connection_bandwidth_id

    @global_connection_bandwidth_id.setter
    def global_connection_bandwidth_id(self, global_connection_bandwidth_id):
        r"""Sets the global_connection_bandwidth_id of this CentralNetworkErRouteTableAttachment.

        全域互联带宽ID。

        :param global_connection_bandwidth_id: The global_connection_bandwidth_id of this CentralNetworkErRouteTableAttachment.
        :type global_connection_bandwidth_id: str
        """
        self._global_connection_bandwidth_id = global_connection_bandwidth_id

    @property
    def is_frozen(self):
        r"""Gets the is_frozen of this CentralNetworkErRouteTableAttachment.

        是否冻结。

        :return: The is_frozen of this CentralNetworkErRouteTableAttachment.
        :rtype: bool
        """
        return self._is_frozen

    @is_frozen.setter
    def is_frozen(self, is_frozen):
        r"""Sets the is_frozen of this CentralNetworkErRouteTableAttachment.

        是否冻结。

        :param is_frozen: The is_frozen of this CentralNetworkErRouteTableAttachment.
        :type is_frozen: bool
        """
        self._is_frozen = is_frozen

    @property
    def bandwidth_type(self):
        r"""Gets the bandwidth_type of this CentralNetworkErRouteTableAttachment.

        :return: The bandwidth_type of this CentralNetworkErRouteTableAttachment.
        :rtype: :class:`huaweicloudsdkcc.v3.BandwidthTypeEnum`
        """
        return self._bandwidth_type

    @bandwidth_type.setter
    def bandwidth_type(self, bandwidth_type):
        r"""Sets the bandwidth_type of this CentralNetworkErRouteTableAttachment.

        :param bandwidth_type: The bandwidth_type of this CentralNetworkErRouteTableAttachment.
        :type bandwidth_type: :class:`huaweicloudsdkcc.v3.BandwidthTypeEnum`
        """
        self._bandwidth_type = bandwidth_type

    @property
    def bandwidth_size(self):
        r"""Gets the bandwidth_size of this CentralNetworkErRouteTableAttachment.

        带宽值，单位Mbps。

        :return: The bandwidth_size of this CentralNetworkErRouteTableAttachment.
        :rtype: int
        """
        return self._bandwidth_size

    @bandwidth_size.setter
    def bandwidth_size(self, bandwidth_size):
        r"""Sets the bandwidth_size of this CentralNetworkErRouteTableAttachment.

        带宽值，单位Mbps。

        :param bandwidth_size: The bandwidth_size of this CentralNetworkErRouteTableAttachment.
        :type bandwidth_size: int
        """
        self._bandwidth_size = bandwidth_size

    @property
    def enterprise_router_id(self):
        r"""Gets the enterprise_router_id of this CentralNetworkErRouteTableAttachment.

        企业路由器的ID。

        :return: The enterprise_router_id of this CentralNetworkErRouteTableAttachment.
        :rtype: str
        """
        return self._enterprise_router_id

    @enterprise_router_id.setter
    def enterprise_router_id(self, enterprise_router_id):
        r"""Sets the enterprise_router_id of this CentralNetworkErRouteTableAttachment.

        企业路由器的ID。

        :param enterprise_router_id: The enterprise_router_id of this CentralNetworkErRouteTableAttachment.
        :type enterprise_router_id: str
        """
        self._enterprise_router_id = enterprise_router_id

    @property
    def enterprise_router_project_id(self):
        r"""Gets the enterprise_router_project_id of this CentralNetworkErRouteTableAttachment.

        企业路由器的项目ID。

        :return: The enterprise_router_project_id of this CentralNetworkErRouteTableAttachment.
        :rtype: str
        """
        return self._enterprise_router_project_id

    @enterprise_router_project_id.setter
    def enterprise_router_project_id(self, enterprise_router_project_id):
        r"""Sets the enterprise_router_project_id of this CentralNetworkErRouteTableAttachment.

        企业路由器的项目ID。

        :param enterprise_router_project_id: The enterprise_router_project_id of this CentralNetworkErRouteTableAttachment.
        :type enterprise_router_project_id: str
        """
        self._enterprise_router_project_id = enterprise_router_project_id

    @property
    def enterprise_router_region_id(self):
        r"""Gets the enterprise_router_region_id of this CentralNetworkErRouteTableAttachment.

        ER路由器的regionID。

        :return: The enterprise_router_region_id of this CentralNetworkErRouteTableAttachment.
        :rtype: str
        """
        return self._enterprise_router_region_id

    @enterprise_router_region_id.setter
    def enterprise_router_region_id(self, enterprise_router_region_id):
        r"""Sets the enterprise_router_region_id of this CentralNetworkErRouteTableAttachment.

        ER路由器的regionID。

        :param enterprise_router_region_id: The enterprise_router_region_id of this CentralNetworkErRouteTableAttachment.
        :type enterprise_router_region_id: str
        """
        self._enterprise_router_region_id = enterprise_router_region_id

    @property
    def enterprise_router_attachment_id(self):
        r"""Gets the enterprise_router_attachment_id of this CentralNetworkErRouteTableAttachment.

        企业路由器的连接ID。

        :return: The enterprise_router_attachment_id of this CentralNetworkErRouteTableAttachment.
        :rtype: str
        """
        return self._enterprise_router_attachment_id

    @enterprise_router_attachment_id.setter
    def enterprise_router_attachment_id(self, enterprise_router_attachment_id):
        r"""Sets the enterprise_router_attachment_id of this CentralNetworkErRouteTableAttachment.

        企业路由器的连接ID。

        :param enterprise_router_attachment_id: The enterprise_router_attachment_id of this CentralNetworkErRouteTableAttachment.
        :type enterprise_router_attachment_id: str
        """
        self._enterprise_router_attachment_id = enterprise_router_attachment_id

    @property
    def enterprise_router_table_id(self):
        r"""Gets the enterprise_router_table_id of this CentralNetworkErRouteTableAttachment.

        企业路由器的路由表ID。

        :return: The enterprise_router_table_id of this CentralNetworkErRouteTableAttachment.
        :rtype: str
        """
        return self._enterprise_router_table_id

    @enterprise_router_table_id.setter
    def enterprise_router_table_id(self, enterprise_router_table_id):
        r"""Sets the enterprise_router_table_id of this CentralNetworkErRouteTableAttachment.

        企业路由器的路由表ID。

        :param enterprise_router_table_id: The enterprise_router_table_id of this CentralNetworkErRouteTableAttachment.
        :type enterprise_router_table_id: str
        """
        self._enterprise_router_table_id = enterprise_router_table_id

    @property
    def enterprise_router_site_code(self):
        r"""Gets the enterprise_router_site_code of this CentralNetworkErRouteTableAttachment.

        中心网络企业路由器的站点编码。

        :return: The enterprise_router_site_code of this CentralNetworkErRouteTableAttachment.
        :rtype: str
        """
        return self._enterprise_router_site_code

    @enterprise_router_site_code.setter
    def enterprise_router_site_code(self, enterprise_router_site_code):
        r"""Sets the enterprise_router_site_code of this CentralNetworkErRouteTableAttachment.

        中心网络企业路由器的站点编码。

        :param enterprise_router_site_code: The enterprise_router_site_code of this CentralNetworkErRouteTableAttachment.
        :type enterprise_router_site_code: str
        """
        self._enterprise_router_site_code = enterprise_router_site_code

    @property
    def attached_er_table_project_id(self):
        r"""Gets the attached_er_table_project_id of this CentralNetworkErRouteTableAttachment.

        被挂载的企业路由器的项目ID。

        :return: The attached_er_table_project_id of this CentralNetworkErRouteTableAttachment.
        :rtype: str
        """
        return self._attached_er_table_project_id

    @attached_er_table_project_id.setter
    def attached_er_table_project_id(self, attached_er_table_project_id):
        r"""Sets the attached_er_table_project_id of this CentralNetworkErRouteTableAttachment.

        被挂载的企业路由器的项目ID。

        :param attached_er_table_project_id: The attached_er_table_project_id of this CentralNetworkErRouteTableAttachment.
        :type attached_er_table_project_id: str
        """
        self._attached_er_table_project_id = attached_er_table_project_id

    @property
    def attached_er_table_region_id(self):
        r"""Gets the attached_er_table_region_id of this CentralNetworkErRouteTableAttachment.

        ER路由器的regionID。

        :return: The attached_er_table_region_id of this CentralNetworkErRouteTableAttachment.
        :rtype: str
        """
        return self._attached_er_table_region_id

    @attached_er_table_region_id.setter
    def attached_er_table_region_id(self, attached_er_table_region_id):
        r"""Sets the attached_er_table_region_id of this CentralNetworkErRouteTableAttachment.

        ER路由器的regionID。

        :param attached_er_table_region_id: The attached_er_table_region_id of this CentralNetworkErRouteTableAttachment.
        :type attached_er_table_region_id: str
        """
        self._attached_er_table_region_id = attached_er_table_region_id

    @property
    def attached_er_id(self):
        r"""Gets the attached_er_id of this CentralNetworkErRouteTableAttachment.

        被挂载的企业路由器ID。

        :return: The attached_er_id of this CentralNetworkErRouteTableAttachment.
        :rtype: str
        """
        return self._attached_er_id

    @attached_er_id.setter
    def attached_er_id(self, attached_er_id):
        r"""Sets the attached_er_id of this CentralNetworkErRouteTableAttachment.

        被挂载的企业路由器ID。

        :param attached_er_id: The attached_er_id of this CentralNetworkErRouteTableAttachment.
        :type attached_er_id: str
        """
        self._attached_er_id = attached_er_id

    @property
    def attached_er_table_id(self):
        r"""Gets the attached_er_table_id of this CentralNetworkErRouteTableAttachment.

        被挂载的企业路由器的路由表ID。

        :return: The attached_er_table_id of this CentralNetworkErRouteTableAttachment.
        :rtype: str
        """
        return self._attached_er_table_id

    @attached_er_table_id.setter
    def attached_er_table_id(self, attached_er_table_id):
        r"""Sets the attached_er_table_id of this CentralNetworkErRouteTableAttachment.

        被挂载的企业路由器的路由表ID。

        :param attached_er_table_id: The attached_er_table_id of this CentralNetworkErRouteTableAttachment.
        :type attached_er_table_id: str
        """
        self._attached_er_table_id = attached_er_table_id

    @property
    def attached_er_attachment_id(self):
        r"""Gets the attached_er_attachment_id of this CentralNetworkErRouteTableAttachment.

        被挂载的企业路由器的连接ID。

        :return: The attached_er_attachment_id of this CentralNetworkErRouteTableAttachment.
        :rtype: str
        """
        return self._attached_er_attachment_id

    @attached_er_attachment_id.setter
    def attached_er_attachment_id(self, attached_er_attachment_id):
        r"""Sets the attached_er_attachment_id of this CentralNetworkErRouteTableAttachment.

        被挂载的企业路由器的连接ID。

        :param attached_er_attachment_id: The attached_er_attachment_id of this CentralNetworkErRouteTableAttachment.
        :type attached_er_attachment_id: str
        """
        self._attached_er_attachment_id = attached_er_attachment_id

    @property
    def attached_er_table_site_code(self):
        r"""Gets the attached_er_table_site_code of this CentralNetworkErRouteTableAttachment.

        被挂载的企业路由器的站点编码。

        :return: The attached_er_table_site_code of this CentralNetworkErRouteTableAttachment.
        :rtype: str
        """
        return self._attached_er_table_site_code

    @attached_er_table_site_code.setter
    def attached_er_table_site_code(self, attached_er_table_site_code):
        r"""Sets the attached_er_table_site_code of this CentralNetworkErRouteTableAttachment.

        被挂载的企业路由器的站点编码。

        :param attached_er_table_site_code: The attached_er_table_site_code of this CentralNetworkErRouteTableAttachment.
        :type attached_er_table_site_code: str
        """
        self._attached_er_table_site_code = attached_er_table_site_code

    @property
    def hosted_cloud(self):
        r"""Gets the hosted_cloud of this CentralNetworkErRouteTableAttachment.

        :return: The hosted_cloud of this CentralNetworkErRouteTableAttachment.
        :rtype: :class:`huaweicloudsdkcc.v3.HostedCloudEnum`
        """
        return self._hosted_cloud

    @hosted_cloud.setter
    def hosted_cloud(self, hosted_cloud):
        r"""Sets the hosted_cloud of this CentralNetworkErRouteTableAttachment.

        :param hosted_cloud: The hosted_cloud of this CentralNetworkErRouteTableAttachment.
        :type hosted_cloud: :class:`huaweicloudsdkcc.v3.HostedCloudEnum`
        """
        self._hosted_cloud = hosted_cloud

    @property
    def approved_state(self):
        r"""Gets the approved_state of this CentralNetworkErRouteTableAttachment.

        :return: The approved_state of this CentralNetworkErRouteTableAttachment.
        :rtype: :class:`huaweicloudsdkcc.v3.ApprovedStateEnum`
        """
        return self._approved_state

    @approved_state.setter
    def approved_state(self, approved_state):
        r"""Sets the approved_state of this CentralNetworkErRouteTableAttachment.

        :param approved_state: The approved_state of this CentralNetworkErRouteTableAttachment.
        :type approved_state: :class:`huaweicloudsdkcc.v3.ApprovedStateEnum`
        """
        self._approved_state = approved_state

    @property
    def reason(self):
        r"""Gets the reason of this CentralNetworkErRouteTableAttachment.

        审批拒绝创建企业路由表附件的原因。

        :return: The reason of this CentralNetworkErRouteTableAttachment.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        r"""Sets the reason of this CentralNetworkErRouteTableAttachment.

        审批拒绝创建企业路由表附件的原因。

        :param reason: The reason of this CentralNetworkErRouteTableAttachment.
        :type reason: str
        """
        self._reason = reason

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
        if not isinstance(other, CentralNetworkErRouteTableAttachment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
