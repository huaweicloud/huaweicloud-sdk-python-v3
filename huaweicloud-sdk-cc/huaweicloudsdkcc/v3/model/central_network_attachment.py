# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CentralNetworkAttachment:

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
        'attachment_instance_type': 'AttachmentInstanceTypeEnum',
        'attachment_instance_id': 'str',
        'attachment_id': 'str',
        'attachment_instance_project_id': 'str',
        'attachment_instance_region_id': 'str',
        'attachment_instance_site_code': 'str',
        'enterprise_router_site_code': 'str',
        'specification_value': 'CentralNetworkAttachmentSpecificationValueInfo'
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
        'attachment_instance_type': 'attachment_instance_type',
        'attachment_instance_id': 'attachment_instance_id',
        'attachment_id': 'attachment_id',
        'attachment_instance_project_id': 'attachment_instance_project_id',
        'attachment_instance_region_id': 'attachment_instance_region_id',
        'attachment_instance_site_code': 'attachment_instance_site_code',
        'enterprise_router_site_code': 'enterprise_router_site_code',
        'specification_value': 'specification_value'
    }

    def __init__(self, id=None, name=None, description=None, domain_id=None, state=None, created_at=None, updated_at=None, central_network_id=None, central_network_plane_id=None, global_connection_bandwidth_id=None, bandwidth_type=None, bandwidth_size=None, is_frozen=None, enterprise_router_id=None, enterprise_router_project_id=None, enterprise_router_region_id=None, enterprise_router_attachment_id=None, attachment_instance_type=None, attachment_instance_id=None, attachment_id=None, attachment_instance_project_id=None, attachment_instance_region_id=None, attachment_instance_site_code=None, enterprise_router_site_code=None, specification_value=None):
        r"""CentralNetworkAttachment

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
        :param bandwidth_type: 
        :type bandwidth_type: :class:`huaweicloudsdkcc.v3.BandwidthTypeEnum`
        :param bandwidth_size: 带宽值，单位Mbps。
        :type bandwidth_size: int
        :param is_frozen: 是否冻结。
        :type is_frozen: bool
        :param enterprise_router_id: 企业路由器的ID。
        :type enterprise_router_id: str
        :param enterprise_router_project_id: 企业路由器的项目ID。
        :type enterprise_router_project_id: str
        :param enterprise_router_region_id: ER路由器的regionID。
        :type enterprise_router_region_id: str
        :param enterprise_router_attachment_id: 企业路由器的连接ID。
        :type enterprise_router_attachment_id: str
        :param attachment_instance_type: 
        :type attachment_instance_type: :class:`huaweicloudsdkcc.v3.AttachmentInstanceTypeEnum`
        :param attachment_instance_id: 中心网络附件对端实例ID，企业路由器的路由表ID或者GDGW的ID。
        :type attachment_instance_id: str
        :param attachment_id: 中心网络附件对端实例的连接ID，企业路由器的连接ID或者GDGW的连接ID。
        :type attachment_id: str
        :param attachment_instance_project_id: 中心网络附件对端实例的项目ID。
        :type attachment_instance_project_id: str
        :param attachment_instance_region_id: 中心网络附件对端实例的regionID。
        :type attachment_instance_region_id: str
        :param attachment_instance_site_code: 中心网络附件对端实例的站点编码。
        :type attachment_instance_site_code: str
        :param enterprise_router_site_code: 中心网络企业路由器的站点编码。
        :type enterprise_router_site_code: str
        :param specification_value: 
        :type specification_value: :class:`huaweicloudsdkcc.v3.CentralNetworkAttachmentSpecificationValueInfo`
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
        self._attachment_instance_type = None
        self._attachment_instance_id = None
        self._attachment_id = None
        self._attachment_instance_project_id = None
        self._attachment_instance_region_id = None
        self._attachment_instance_site_code = None
        self._enterprise_router_site_code = None
        self._specification_value = None
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
        self.attachment_instance_type = attachment_instance_type
        self.attachment_instance_id = attachment_instance_id
        if attachment_id is not None:
            self.attachment_id = attachment_id
        self.attachment_instance_project_id = attachment_instance_project_id
        self.attachment_instance_region_id = attachment_instance_region_id
        self.attachment_instance_site_code = attachment_instance_site_code
        self.enterprise_router_site_code = enterprise_router_site_code
        if specification_value is not None:
            self.specification_value = specification_value

    @property
    def id(self):
        r"""Gets the id of this CentralNetworkAttachment.

        实例ID。

        :return: The id of this CentralNetworkAttachment.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CentralNetworkAttachment.

        实例ID。

        :param id: The id of this CentralNetworkAttachment.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this CentralNetworkAttachment.

        实例名称。

        :return: The name of this CentralNetworkAttachment.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CentralNetworkAttachment.

        实例名称。

        :param name: The name of this CentralNetworkAttachment.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this CentralNetworkAttachment.

        实例描述。不支持 <>。

        :return: The description of this CentralNetworkAttachment.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CentralNetworkAttachment.

        实例描述。不支持 <>。

        :param description: The description of this CentralNetworkAttachment.
        :type description: str
        """
        self._description = description

    @property
    def domain_id(self):
        r"""Gets the domain_id of this CentralNetworkAttachment.

        实例所属账号ID。

        :return: The domain_id of this CentralNetworkAttachment.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this CentralNetworkAttachment.

        实例所属账号ID。

        :param domain_id: The domain_id of this CentralNetworkAttachment.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def state(self):
        r"""Gets the state of this CentralNetworkAttachment.

        :return: The state of this CentralNetworkAttachment.
        :rtype: :class:`huaweicloudsdkcc.v3.CentralNetworkConnectionStateEnum`
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this CentralNetworkAttachment.

        :param state: The state of this CentralNetworkAttachment.
        :type state: :class:`huaweicloudsdkcc.v3.CentralNetworkConnectionStateEnum`
        """
        self._state = state

    @property
    def created_at(self):
        r"""Gets the created_at of this CentralNetworkAttachment.

        实例创建时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。

        :return: The created_at of this CentralNetworkAttachment.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this CentralNetworkAttachment.

        实例创建时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。

        :param created_at: The created_at of this CentralNetworkAttachment.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this CentralNetworkAttachment.

        实例更新时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。

        :return: The updated_at of this CentralNetworkAttachment.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this CentralNetworkAttachment.

        实例更新时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。

        :param updated_at: The updated_at of this CentralNetworkAttachment.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

    @property
    def central_network_id(self):
        r"""Gets the central_network_id of this CentralNetworkAttachment.

        中心网络ID。

        :return: The central_network_id of this CentralNetworkAttachment.
        :rtype: str
        """
        return self._central_network_id

    @central_network_id.setter
    def central_network_id(self, central_network_id):
        r"""Sets the central_network_id of this CentralNetworkAttachment.

        中心网络ID。

        :param central_network_id: The central_network_id of this CentralNetworkAttachment.
        :type central_network_id: str
        """
        self._central_network_id = central_network_id

    @property
    def central_network_plane_id(self):
        r"""Gets the central_network_plane_id of this CentralNetworkAttachment.

        中心网络平面ID。

        :return: The central_network_plane_id of this CentralNetworkAttachment.
        :rtype: str
        """
        return self._central_network_plane_id

    @central_network_plane_id.setter
    def central_network_plane_id(self, central_network_plane_id):
        r"""Sets the central_network_plane_id of this CentralNetworkAttachment.

        中心网络平面ID。

        :param central_network_plane_id: The central_network_plane_id of this CentralNetworkAttachment.
        :type central_network_plane_id: str
        """
        self._central_network_plane_id = central_network_plane_id

    @property
    def global_connection_bandwidth_id(self):
        r"""Gets the global_connection_bandwidth_id of this CentralNetworkAttachment.

        全域互联带宽ID。

        :return: The global_connection_bandwidth_id of this CentralNetworkAttachment.
        :rtype: str
        """
        return self._global_connection_bandwidth_id

    @global_connection_bandwidth_id.setter
    def global_connection_bandwidth_id(self, global_connection_bandwidth_id):
        r"""Sets the global_connection_bandwidth_id of this CentralNetworkAttachment.

        全域互联带宽ID。

        :param global_connection_bandwidth_id: The global_connection_bandwidth_id of this CentralNetworkAttachment.
        :type global_connection_bandwidth_id: str
        """
        self._global_connection_bandwidth_id = global_connection_bandwidth_id

    @property
    def bandwidth_type(self):
        r"""Gets the bandwidth_type of this CentralNetworkAttachment.

        :return: The bandwidth_type of this CentralNetworkAttachment.
        :rtype: :class:`huaweicloudsdkcc.v3.BandwidthTypeEnum`
        """
        return self._bandwidth_type

    @bandwidth_type.setter
    def bandwidth_type(self, bandwidth_type):
        r"""Sets the bandwidth_type of this CentralNetworkAttachment.

        :param bandwidth_type: The bandwidth_type of this CentralNetworkAttachment.
        :type bandwidth_type: :class:`huaweicloudsdkcc.v3.BandwidthTypeEnum`
        """
        self._bandwidth_type = bandwidth_type

    @property
    def bandwidth_size(self):
        r"""Gets the bandwidth_size of this CentralNetworkAttachment.

        带宽值，单位Mbps。

        :return: The bandwidth_size of this CentralNetworkAttachment.
        :rtype: int
        """
        return self._bandwidth_size

    @bandwidth_size.setter
    def bandwidth_size(self, bandwidth_size):
        r"""Sets the bandwidth_size of this CentralNetworkAttachment.

        带宽值，单位Mbps。

        :param bandwidth_size: The bandwidth_size of this CentralNetworkAttachment.
        :type bandwidth_size: int
        """
        self._bandwidth_size = bandwidth_size

    @property
    def is_frozen(self):
        r"""Gets the is_frozen of this CentralNetworkAttachment.

        是否冻结。

        :return: The is_frozen of this CentralNetworkAttachment.
        :rtype: bool
        """
        return self._is_frozen

    @is_frozen.setter
    def is_frozen(self, is_frozen):
        r"""Sets the is_frozen of this CentralNetworkAttachment.

        是否冻结。

        :param is_frozen: The is_frozen of this CentralNetworkAttachment.
        :type is_frozen: bool
        """
        self._is_frozen = is_frozen

    @property
    def enterprise_router_id(self):
        r"""Gets the enterprise_router_id of this CentralNetworkAttachment.

        企业路由器的ID。

        :return: The enterprise_router_id of this CentralNetworkAttachment.
        :rtype: str
        """
        return self._enterprise_router_id

    @enterprise_router_id.setter
    def enterprise_router_id(self, enterprise_router_id):
        r"""Sets the enterprise_router_id of this CentralNetworkAttachment.

        企业路由器的ID。

        :param enterprise_router_id: The enterprise_router_id of this CentralNetworkAttachment.
        :type enterprise_router_id: str
        """
        self._enterprise_router_id = enterprise_router_id

    @property
    def enterprise_router_project_id(self):
        r"""Gets the enterprise_router_project_id of this CentralNetworkAttachment.

        企业路由器的项目ID。

        :return: The enterprise_router_project_id of this CentralNetworkAttachment.
        :rtype: str
        """
        return self._enterprise_router_project_id

    @enterprise_router_project_id.setter
    def enterprise_router_project_id(self, enterprise_router_project_id):
        r"""Sets the enterprise_router_project_id of this CentralNetworkAttachment.

        企业路由器的项目ID。

        :param enterprise_router_project_id: The enterprise_router_project_id of this CentralNetworkAttachment.
        :type enterprise_router_project_id: str
        """
        self._enterprise_router_project_id = enterprise_router_project_id

    @property
    def enterprise_router_region_id(self):
        r"""Gets the enterprise_router_region_id of this CentralNetworkAttachment.

        ER路由器的regionID。

        :return: The enterprise_router_region_id of this CentralNetworkAttachment.
        :rtype: str
        """
        return self._enterprise_router_region_id

    @enterprise_router_region_id.setter
    def enterprise_router_region_id(self, enterprise_router_region_id):
        r"""Sets the enterprise_router_region_id of this CentralNetworkAttachment.

        ER路由器的regionID。

        :param enterprise_router_region_id: The enterprise_router_region_id of this CentralNetworkAttachment.
        :type enterprise_router_region_id: str
        """
        self._enterprise_router_region_id = enterprise_router_region_id

    @property
    def enterprise_router_attachment_id(self):
        r"""Gets the enterprise_router_attachment_id of this CentralNetworkAttachment.

        企业路由器的连接ID。

        :return: The enterprise_router_attachment_id of this CentralNetworkAttachment.
        :rtype: str
        """
        return self._enterprise_router_attachment_id

    @enterprise_router_attachment_id.setter
    def enterprise_router_attachment_id(self, enterprise_router_attachment_id):
        r"""Sets the enterprise_router_attachment_id of this CentralNetworkAttachment.

        企业路由器的连接ID。

        :param enterprise_router_attachment_id: The enterprise_router_attachment_id of this CentralNetworkAttachment.
        :type enterprise_router_attachment_id: str
        """
        self._enterprise_router_attachment_id = enterprise_router_attachment_id

    @property
    def attachment_instance_type(self):
        r"""Gets the attachment_instance_type of this CentralNetworkAttachment.

        :return: The attachment_instance_type of this CentralNetworkAttachment.
        :rtype: :class:`huaweicloudsdkcc.v3.AttachmentInstanceTypeEnum`
        """
        return self._attachment_instance_type

    @attachment_instance_type.setter
    def attachment_instance_type(self, attachment_instance_type):
        r"""Sets the attachment_instance_type of this CentralNetworkAttachment.

        :param attachment_instance_type: The attachment_instance_type of this CentralNetworkAttachment.
        :type attachment_instance_type: :class:`huaweicloudsdkcc.v3.AttachmentInstanceTypeEnum`
        """
        self._attachment_instance_type = attachment_instance_type

    @property
    def attachment_instance_id(self):
        r"""Gets the attachment_instance_id of this CentralNetworkAttachment.

        中心网络附件对端实例ID，企业路由器的路由表ID或者GDGW的ID。

        :return: The attachment_instance_id of this CentralNetworkAttachment.
        :rtype: str
        """
        return self._attachment_instance_id

    @attachment_instance_id.setter
    def attachment_instance_id(self, attachment_instance_id):
        r"""Sets the attachment_instance_id of this CentralNetworkAttachment.

        中心网络附件对端实例ID，企业路由器的路由表ID或者GDGW的ID。

        :param attachment_instance_id: The attachment_instance_id of this CentralNetworkAttachment.
        :type attachment_instance_id: str
        """
        self._attachment_instance_id = attachment_instance_id

    @property
    def attachment_id(self):
        r"""Gets the attachment_id of this CentralNetworkAttachment.

        中心网络附件对端实例的连接ID，企业路由器的连接ID或者GDGW的连接ID。

        :return: The attachment_id of this CentralNetworkAttachment.
        :rtype: str
        """
        return self._attachment_id

    @attachment_id.setter
    def attachment_id(self, attachment_id):
        r"""Sets the attachment_id of this CentralNetworkAttachment.

        中心网络附件对端实例的连接ID，企业路由器的连接ID或者GDGW的连接ID。

        :param attachment_id: The attachment_id of this CentralNetworkAttachment.
        :type attachment_id: str
        """
        self._attachment_id = attachment_id

    @property
    def attachment_instance_project_id(self):
        r"""Gets the attachment_instance_project_id of this CentralNetworkAttachment.

        中心网络附件对端实例的项目ID。

        :return: The attachment_instance_project_id of this CentralNetworkAttachment.
        :rtype: str
        """
        return self._attachment_instance_project_id

    @attachment_instance_project_id.setter
    def attachment_instance_project_id(self, attachment_instance_project_id):
        r"""Sets the attachment_instance_project_id of this CentralNetworkAttachment.

        中心网络附件对端实例的项目ID。

        :param attachment_instance_project_id: The attachment_instance_project_id of this CentralNetworkAttachment.
        :type attachment_instance_project_id: str
        """
        self._attachment_instance_project_id = attachment_instance_project_id

    @property
    def attachment_instance_region_id(self):
        r"""Gets the attachment_instance_region_id of this CentralNetworkAttachment.

        中心网络附件对端实例的regionID。

        :return: The attachment_instance_region_id of this CentralNetworkAttachment.
        :rtype: str
        """
        return self._attachment_instance_region_id

    @attachment_instance_region_id.setter
    def attachment_instance_region_id(self, attachment_instance_region_id):
        r"""Sets the attachment_instance_region_id of this CentralNetworkAttachment.

        中心网络附件对端实例的regionID。

        :param attachment_instance_region_id: The attachment_instance_region_id of this CentralNetworkAttachment.
        :type attachment_instance_region_id: str
        """
        self._attachment_instance_region_id = attachment_instance_region_id

    @property
    def attachment_instance_site_code(self):
        r"""Gets the attachment_instance_site_code of this CentralNetworkAttachment.

        中心网络附件对端实例的站点编码。

        :return: The attachment_instance_site_code of this CentralNetworkAttachment.
        :rtype: str
        """
        return self._attachment_instance_site_code

    @attachment_instance_site_code.setter
    def attachment_instance_site_code(self, attachment_instance_site_code):
        r"""Sets the attachment_instance_site_code of this CentralNetworkAttachment.

        中心网络附件对端实例的站点编码。

        :param attachment_instance_site_code: The attachment_instance_site_code of this CentralNetworkAttachment.
        :type attachment_instance_site_code: str
        """
        self._attachment_instance_site_code = attachment_instance_site_code

    @property
    def enterprise_router_site_code(self):
        r"""Gets the enterprise_router_site_code of this CentralNetworkAttachment.

        中心网络企业路由器的站点编码。

        :return: The enterprise_router_site_code of this CentralNetworkAttachment.
        :rtype: str
        """
        return self._enterprise_router_site_code

    @enterprise_router_site_code.setter
    def enterprise_router_site_code(self, enterprise_router_site_code):
        r"""Sets the enterprise_router_site_code of this CentralNetworkAttachment.

        中心网络企业路由器的站点编码。

        :param enterprise_router_site_code: The enterprise_router_site_code of this CentralNetworkAttachment.
        :type enterprise_router_site_code: str
        """
        self._enterprise_router_site_code = enterprise_router_site_code

    @property
    def specification_value(self):
        r"""Gets the specification_value of this CentralNetworkAttachment.

        :return: The specification_value of this CentralNetworkAttachment.
        :rtype: :class:`huaweicloudsdkcc.v3.CentralNetworkAttachmentSpecificationValueInfo`
        """
        return self._specification_value

    @specification_value.setter
    def specification_value(self, specification_value):
        r"""Sets the specification_value of this CentralNetworkAttachment.

        :param specification_value: The specification_value of this CentralNetworkAttachment.
        :type specification_value: :class:`huaweicloudsdkcc.v3.CentralNetworkAttachmentSpecificationValueInfo`
        """
        self._specification_value = specification_value

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
        if not isinstance(other, CentralNetworkAttachment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
