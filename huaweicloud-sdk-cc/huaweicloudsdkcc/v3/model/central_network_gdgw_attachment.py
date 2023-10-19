# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CentralNetworkGdgwAttachment:

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
        'bandwidth_type': 'BandwidthTypeEnum',
        'bandwidth_size': 'int',
        'is_frozen': 'bool',
        'enterprise_router_id': 'str',
        'enterprise_router_project_id': 'str',
        'enterprise_router_region_id': 'str',
        'enterprise_router_attachment_id': 'str',
        'global_dc_gateway_peer_link_id': 'str',
        'global_dc_gateway_id': 'str',
        'global_dc_gateway_project_id': 'str',
        'global_dc_gateway_region_id': 'str',
        'enterprise_router_site_code': 'str',
        'global_dc_gateway_site_code': 'str'
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
        'bandwidth_type': 'bandwidth_type',
        'bandwidth_size': 'bandwidth_size',
        'is_frozen': 'is_frozen',
        'enterprise_router_id': 'enterprise_router_id',
        'enterprise_router_project_id': 'enterprise_router_project_id',
        'enterprise_router_region_id': 'enterprise_router_region_id',
        'enterprise_router_attachment_id': 'enterprise_router_attachment_id',
        'global_dc_gateway_peer_link_id': 'global_dc_gateway_peer_link_id',
        'global_dc_gateway_id': 'global_dc_gateway_id',
        'global_dc_gateway_project_id': 'global_dc_gateway_project_id',
        'global_dc_gateway_region_id': 'global_dc_gateway_region_id',
        'enterprise_router_site_code': 'enterprise_router_site_code',
        'global_dc_gateway_site_code': 'global_dc_gateway_site_code'
    }

    def __init__(self, id=None, name=None, description=None, domain_id=None, state=None, created_at=None, updated_at=None, central_network_id=None, central_network_plane_id=None, global_connection_bandwidth_id=None, bandwidth_type=None, bandwidth_size=None, is_frozen=None, enterprise_router_id=None, enterprise_router_project_id=None, enterprise_router_region_id=None, enterprise_router_attachment_id=None, global_dc_gateway_peer_link_id=None, global_dc_gateway_id=None, global_dc_gateway_project_id=None, global_dc_gateway_region_id=None, enterprise_router_site_code=None, global_dc_gateway_site_code=None):
        """CentralNetworkGdgwAttachment

        The model defined in huaweicloud sdk

        :param id: 资源ID标识符。
        :type id: str
        :param name: 实例名字。
        :type name: str
        :param description: 实例描述。不支持 &lt;&gt;。
        :type description: str
        :param domain_id: 实例所属帐号ID。
        :type domain_id: str
        :param state: 
        :type state: :class:`huaweicloudsdkcc.v3.CentralNetworkConnectionStateEnum`
        :param created_at: 实例创建时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。
        :type created_at: datetime
        :param updated_at: 实例更新时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。
        :type updated_at: datetime
        :param central_network_id: 资源ID标识符。
        :type central_network_id: str
        :param central_network_plane_id: 资源ID标识符。
        :type central_network_plane_id: str
        :param global_connection_bandwidth_id: 资源ID标识符。
        :type global_connection_bandwidth_id: str
        :param bandwidth_type: 
        :type bandwidth_type: :class:`huaweicloudsdkcc.v3.BandwidthTypeEnum`
        :param bandwidth_size: 带宽值定义，单位Mbps。
        :type bandwidth_size: int
        :param is_frozen: 是否冻结
        :type is_frozen: bool
        :param enterprise_router_id: 资源ID标识符。
        :type enterprise_router_id: str
        :param enterprise_router_project_id: 实例所属项目ID。
        :type enterprise_router_project_id: str
        :param enterprise_router_region_id: RegionID。
        :type enterprise_router_region_id: str
        :param enterprise_router_attachment_id: 资源ID标识符。
        :type enterprise_router_attachment_id: str
        :param global_dc_gateway_peer_link_id: 资源ID标识符。
        :type global_dc_gateway_peer_link_id: str
        :param global_dc_gateway_id: 资源ID标识符。
        :type global_dc_gateway_id: str
        :param global_dc_gateway_project_id: 实例所属项目ID。
        :type global_dc_gateway_project_id: str
        :param global_dc_gateway_region_id: RegionID。
        :type global_dc_gateway_region_id: str
        :param enterprise_router_site_code: 站点编码定义
        :type enterprise_router_site_code: str
        :param global_dc_gateway_site_code: 站点编码定义
        :type global_dc_gateway_site_code: str
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
        self._bandwidth_type = None
        self._bandwidth_size = None
        self._is_frozen = None
        self._enterprise_router_id = None
        self._enterprise_router_project_id = None
        self._enterprise_router_region_id = None
        self._enterprise_router_attachment_id = None
        self._global_dc_gateway_peer_link_id = None
        self._global_dc_gateway_id = None
        self._global_dc_gateway_project_id = None
        self._global_dc_gateway_region_id = None
        self._enterprise_router_site_code = None
        self._global_dc_gateway_site_code = None
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
        self.bandwidth_type = bandwidth_type
        if bandwidth_size is not None:
            self.bandwidth_size = bandwidth_size
        self.is_frozen = is_frozen
        self.enterprise_router_id = enterprise_router_id
        self.enterprise_router_project_id = enterprise_router_project_id
        self.enterprise_router_region_id = enterprise_router_region_id
        if enterprise_router_attachment_id is not None:
            self.enterprise_router_attachment_id = enterprise_router_attachment_id
        if global_dc_gateway_peer_link_id is not None:
            self.global_dc_gateway_peer_link_id = global_dc_gateway_peer_link_id
        self.global_dc_gateway_id = global_dc_gateway_id
        self.global_dc_gateway_project_id = global_dc_gateway_project_id
        self.global_dc_gateway_region_id = global_dc_gateway_region_id
        self.enterprise_router_site_code = enterprise_router_site_code
        self.global_dc_gateway_site_code = global_dc_gateway_site_code

    @property
    def id(self):
        """Gets the id of this CentralNetworkGdgwAttachment.

        资源ID标识符。

        :return: The id of this CentralNetworkGdgwAttachment.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CentralNetworkGdgwAttachment.

        资源ID标识符。

        :param id: The id of this CentralNetworkGdgwAttachment.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this CentralNetworkGdgwAttachment.

        实例名字。

        :return: The name of this CentralNetworkGdgwAttachment.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CentralNetworkGdgwAttachment.

        实例名字。

        :param name: The name of this CentralNetworkGdgwAttachment.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this CentralNetworkGdgwAttachment.

        实例描述。不支持 <>。

        :return: The description of this CentralNetworkGdgwAttachment.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CentralNetworkGdgwAttachment.

        实例描述。不支持 <>。

        :param description: The description of this CentralNetworkGdgwAttachment.
        :type description: str
        """
        self._description = description

    @property
    def domain_id(self):
        """Gets the domain_id of this CentralNetworkGdgwAttachment.

        实例所属帐号ID。

        :return: The domain_id of this CentralNetworkGdgwAttachment.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this CentralNetworkGdgwAttachment.

        实例所属帐号ID。

        :param domain_id: The domain_id of this CentralNetworkGdgwAttachment.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def state(self):
        """Gets the state of this CentralNetworkGdgwAttachment.

        :return: The state of this CentralNetworkGdgwAttachment.
        :rtype: :class:`huaweicloudsdkcc.v3.CentralNetworkConnectionStateEnum`
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this CentralNetworkGdgwAttachment.

        :param state: The state of this CentralNetworkGdgwAttachment.
        :type state: :class:`huaweicloudsdkcc.v3.CentralNetworkConnectionStateEnum`
        """
        self._state = state

    @property
    def created_at(self):
        """Gets the created_at of this CentralNetworkGdgwAttachment.

        实例创建时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。

        :return: The created_at of this CentralNetworkGdgwAttachment.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this CentralNetworkGdgwAttachment.

        实例创建时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。

        :param created_at: The created_at of this CentralNetworkGdgwAttachment.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this CentralNetworkGdgwAttachment.

        实例更新时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。

        :return: The updated_at of this CentralNetworkGdgwAttachment.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this CentralNetworkGdgwAttachment.

        实例更新时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。

        :param updated_at: The updated_at of this CentralNetworkGdgwAttachment.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

    @property
    def central_network_id(self):
        """Gets the central_network_id of this CentralNetworkGdgwAttachment.

        资源ID标识符。

        :return: The central_network_id of this CentralNetworkGdgwAttachment.
        :rtype: str
        """
        return self._central_network_id

    @central_network_id.setter
    def central_network_id(self, central_network_id):
        """Sets the central_network_id of this CentralNetworkGdgwAttachment.

        资源ID标识符。

        :param central_network_id: The central_network_id of this CentralNetworkGdgwAttachment.
        :type central_network_id: str
        """
        self._central_network_id = central_network_id

    @property
    def central_network_plane_id(self):
        """Gets the central_network_plane_id of this CentralNetworkGdgwAttachment.

        资源ID标识符。

        :return: The central_network_plane_id of this CentralNetworkGdgwAttachment.
        :rtype: str
        """
        return self._central_network_plane_id

    @central_network_plane_id.setter
    def central_network_plane_id(self, central_network_plane_id):
        """Sets the central_network_plane_id of this CentralNetworkGdgwAttachment.

        资源ID标识符。

        :param central_network_plane_id: The central_network_plane_id of this CentralNetworkGdgwAttachment.
        :type central_network_plane_id: str
        """
        self._central_network_plane_id = central_network_plane_id

    @property
    def global_connection_bandwidth_id(self):
        """Gets the global_connection_bandwidth_id of this CentralNetworkGdgwAttachment.

        资源ID标识符。

        :return: The global_connection_bandwidth_id of this CentralNetworkGdgwAttachment.
        :rtype: str
        """
        return self._global_connection_bandwidth_id

    @global_connection_bandwidth_id.setter
    def global_connection_bandwidth_id(self, global_connection_bandwidth_id):
        """Sets the global_connection_bandwidth_id of this CentralNetworkGdgwAttachment.

        资源ID标识符。

        :param global_connection_bandwidth_id: The global_connection_bandwidth_id of this CentralNetworkGdgwAttachment.
        :type global_connection_bandwidth_id: str
        """
        self._global_connection_bandwidth_id = global_connection_bandwidth_id

    @property
    def bandwidth_type(self):
        """Gets the bandwidth_type of this CentralNetworkGdgwAttachment.

        :return: The bandwidth_type of this CentralNetworkGdgwAttachment.
        :rtype: :class:`huaweicloudsdkcc.v3.BandwidthTypeEnum`
        """
        return self._bandwidth_type

    @bandwidth_type.setter
    def bandwidth_type(self, bandwidth_type):
        """Sets the bandwidth_type of this CentralNetworkGdgwAttachment.

        :param bandwidth_type: The bandwidth_type of this CentralNetworkGdgwAttachment.
        :type bandwidth_type: :class:`huaweicloudsdkcc.v3.BandwidthTypeEnum`
        """
        self._bandwidth_type = bandwidth_type

    @property
    def bandwidth_size(self):
        """Gets the bandwidth_size of this CentralNetworkGdgwAttachment.

        带宽值定义，单位Mbps。

        :return: The bandwidth_size of this CentralNetworkGdgwAttachment.
        :rtype: int
        """
        return self._bandwidth_size

    @bandwidth_size.setter
    def bandwidth_size(self, bandwidth_size):
        """Sets the bandwidth_size of this CentralNetworkGdgwAttachment.

        带宽值定义，单位Mbps。

        :param bandwidth_size: The bandwidth_size of this CentralNetworkGdgwAttachment.
        :type bandwidth_size: int
        """
        self._bandwidth_size = bandwidth_size

    @property
    def is_frozen(self):
        """Gets the is_frozen of this CentralNetworkGdgwAttachment.

        是否冻结

        :return: The is_frozen of this CentralNetworkGdgwAttachment.
        :rtype: bool
        """
        return self._is_frozen

    @is_frozen.setter
    def is_frozen(self, is_frozen):
        """Sets the is_frozen of this CentralNetworkGdgwAttachment.

        是否冻结

        :param is_frozen: The is_frozen of this CentralNetworkGdgwAttachment.
        :type is_frozen: bool
        """
        self._is_frozen = is_frozen

    @property
    def enterprise_router_id(self):
        """Gets the enterprise_router_id of this CentralNetworkGdgwAttachment.

        资源ID标识符。

        :return: The enterprise_router_id of this CentralNetworkGdgwAttachment.
        :rtype: str
        """
        return self._enterprise_router_id

    @enterprise_router_id.setter
    def enterprise_router_id(self, enterprise_router_id):
        """Sets the enterprise_router_id of this CentralNetworkGdgwAttachment.

        资源ID标识符。

        :param enterprise_router_id: The enterprise_router_id of this CentralNetworkGdgwAttachment.
        :type enterprise_router_id: str
        """
        self._enterprise_router_id = enterprise_router_id

    @property
    def enterprise_router_project_id(self):
        """Gets the enterprise_router_project_id of this CentralNetworkGdgwAttachment.

        实例所属项目ID。

        :return: The enterprise_router_project_id of this CentralNetworkGdgwAttachment.
        :rtype: str
        """
        return self._enterprise_router_project_id

    @enterprise_router_project_id.setter
    def enterprise_router_project_id(self, enterprise_router_project_id):
        """Sets the enterprise_router_project_id of this CentralNetworkGdgwAttachment.

        实例所属项目ID。

        :param enterprise_router_project_id: The enterprise_router_project_id of this CentralNetworkGdgwAttachment.
        :type enterprise_router_project_id: str
        """
        self._enterprise_router_project_id = enterprise_router_project_id

    @property
    def enterprise_router_region_id(self):
        """Gets the enterprise_router_region_id of this CentralNetworkGdgwAttachment.

        RegionID。

        :return: The enterprise_router_region_id of this CentralNetworkGdgwAttachment.
        :rtype: str
        """
        return self._enterprise_router_region_id

    @enterprise_router_region_id.setter
    def enterprise_router_region_id(self, enterprise_router_region_id):
        """Sets the enterprise_router_region_id of this CentralNetworkGdgwAttachment.

        RegionID。

        :param enterprise_router_region_id: The enterprise_router_region_id of this CentralNetworkGdgwAttachment.
        :type enterprise_router_region_id: str
        """
        self._enterprise_router_region_id = enterprise_router_region_id

    @property
    def enterprise_router_attachment_id(self):
        """Gets the enterprise_router_attachment_id of this CentralNetworkGdgwAttachment.

        资源ID标识符。

        :return: The enterprise_router_attachment_id of this CentralNetworkGdgwAttachment.
        :rtype: str
        """
        return self._enterprise_router_attachment_id

    @enterprise_router_attachment_id.setter
    def enterprise_router_attachment_id(self, enterprise_router_attachment_id):
        """Sets the enterprise_router_attachment_id of this CentralNetworkGdgwAttachment.

        资源ID标识符。

        :param enterprise_router_attachment_id: The enterprise_router_attachment_id of this CentralNetworkGdgwAttachment.
        :type enterprise_router_attachment_id: str
        """
        self._enterprise_router_attachment_id = enterprise_router_attachment_id

    @property
    def global_dc_gateway_peer_link_id(self):
        """Gets the global_dc_gateway_peer_link_id of this CentralNetworkGdgwAttachment.

        资源ID标识符。

        :return: The global_dc_gateway_peer_link_id of this CentralNetworkGdgwAttachment.
        :rtype: str
        """
        return self._global_dc_gateway_peer_link_id

    @global_dc_gateway_peer_link_id.setter
    def global_dc_gateway_peer_link_id(self, global_dc_gateway_peer_link_id):
        """Sets the global_dc_gateway_peer_link_id of this CentralNetworkGdgwAttachment.

        资源ID标识符。

        :param global_dc_gateway_peer_link_id: The global_dc_gateway_peer_link_id of this CentralNetworkGdgwAttachment.
        :type global_dc_gateway_peer_link_id: str
        """
        self._global_dc_gateway_peer_link_id = global_dc_gateway_peer_link_id

    @property
    def global_dc_gateway_id(self):
        """Gets the global_dc_gateway_id of this CentralNetworkGdgwAttachment.

        资源ID标识符。

        :return: The global_dc_gateway_id of this CentralNetworkGdgwAttachment.
        :rtype: str
        """
        return self._global_dc_gateway_id

    @global_dc_gateway_id.setter
    def global_dc_gateway_id(self, global_dc_gateway_id):
        """Sets the global_dc_gateway_id of this CentralNetworkGdgwAttachment.

        资源ID标识符。

        :param global_dc_gateway_id: The global_dc_gateway_id of this CentralNetworkGdgwAttachment.
        :type global_dc_gateway_id: str
        """
        self._global_dc_gateway_id = global_dc_gateway_id

    @property
    def global_dc_gateway_project_id(self):
        """Gets the global_dc_gateway_project_id of this CentralNetworkGdgwAttachment.

        实例所属项目ID。

        :return: The global_dc_gateway_project_id of this CentralNetworkGdgwAttachment.
        :rtype: str
        """
        return self._global_dc_gateway_project_id

    @global_dc_gateway_project_id.setter
    def global_dc_gateway_project_id(self, global_dc_gateway_project_id):
        """Sets the global_dc_gateway_project_id of this CentralNetworkGdgwAttachment.

        实例所属项目ID。

        :param global_dc_gateway_project_id: The global_dc_gateway_project_id of this CentralNetworkGdgwAttachment.
        :type global_dc_gateway_project_id: str
        """
        self._global_dc_gateway_project_id = global_dc_gateway_project_id

    @property
    def global_dc_gateway_region_id(self):
        """Gets the global_dc_gateway_region_id of this CentralNetworkGdgwAttachment.

        RegionID。

        :return: The global_dc_gateway_region_id of this CentralNetworkGdgwAttachment.
        :rtype: str
        """
        return self._global_dc_gateway_region_id

    @global_dc_gateway_region_id.setter
    def global_dc_gateway_region_id(self, global_dc_gateway_region_id):
        """Sets the global_dc_gateway_region_id of this CentralNetworkGdgwAttachment.

        RegionID。

        :param global_dc_gateway_region_id: The global_dc_gateway_region_id of this CentralNetworkGdgwAttachment.
        :type global_dc_gateway_region_id: str
        """
        self._global_dc_gateway_region_id = global_dc_gateway_region_id

    @property
    def enterprise_router_site_code(self):
        """Gets the enterprise_router_site_code of this CentralNetworkGdgwAttachment.

        站点编码定义

        :return: The enterprise_router_site_code of this CentralNetworkGdgwAttachment.
        :rtype: str
        """
        return self._enterprise_router_site_code

    @enterprise_router_site_code.setter
    def enterprise_router_site_code(self, enterprise_router_site_code):
        """Sets the enterprise_router_site_code of this CentralNetworkGdgwAttachment.

        站点编码定义

        :param enterprise_router_site_code: The enterprise_router_site_code of this CentralNetworkGdgwAttachment.
        :type enterprise_router_site_code: str
        """
        self._enterprise_router_site_code = enterprise_router_site_code

    @property
    def global_dc_gateway_site_code(self):
        """Gets the global_dc_gateway_site_code of this CentralNetworkGdgwAttachment.

        站点编码定义

        :return: The global_dc_gateway_site_code of this CentralNetworkGdgwAttachment.
        :rtype: str
        """
        return self._global_dc_gateway_site_code

    @global_dc_gateway_site_code.setter
    def global_dc_gateway_site_code(self, global_dc_gateway_site_code):
        """Sets the global_dc_gateway_site_code of this CentralNetworkGdgwAttachment.

        站点编码定义

        :param global_dc_gateway_site_code: The global_dc_gateway_site_code of this CentralNetworkGdgwAttachment.
        :type global_dc_gateway_site_code: str
        """
        self._global_dc_gateway_site_code = global_dc_gateway_site_code

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
        if not isinstance(other, CentralNetworkGdgwAttachment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
