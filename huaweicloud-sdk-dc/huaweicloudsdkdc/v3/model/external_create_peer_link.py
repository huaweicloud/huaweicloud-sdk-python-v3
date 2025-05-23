# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExternalCreatePeerLink:

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
        'instance_id': 'str',
        'tenant_id': 'str',
        'name': 'str',
        'description': 'str',
        'global_dc_gateway_id': 'str',
        'bandwidth_info': 'BandwidthInfoExternal',
        'peer_site': 'PeerSiteExternal',
        'status': 'str',
        'reason': 'str',
        'created_time': 'datetime',
        'updated_time': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'instance_id': 'instance_id',
        'tenant_id': 'tenant_id',
        'name': 'name',
        'description': 'description',
        'global_dc_gateway_id': 'global_dc_gateway_id',
        'bandwidth_info': 'bandwidth_info',
        'peer_site': 'peer_site',
        'status': 'status',
        'reason': 'reason',
        'created_time': 'created_time',
        'updated_time': 'updated_time'
    }

    def __init__(self, id=None, instance_id=None, tenant_id=None, name=None, description=None, global_dc_gateway_id=None, bandwidth_info=None, peer_site=None, status=None, reason=None, created_time=None, updated_time=None):
        r"""ExternalCreatePeerLink

        The model defined in huaweicloud sdk

        :param id: 专线对等连接
        :type id: str
        :param instance_id: 专线对等连接实例ID
        :type instance_id: str
        :param tenant_id: 租户ID
        :type tenant_id: str
        :param name: 名称
        :type name: str
        :param description: 描述信息
        :type description: str
        :param global_dc_gateway_id: 全域接入网关ID
        :type global_dc_gateway_id: str
        :param bandwidth_info: 
        :type bandwidth_info: :class:`huaweicloudsdkdc.v3.BandwidthInfoExternal`
        :param peer_site: 
        :type peer_site: :class:`huaweicloudsdkdc.v3.PeerSiteExternal`
        :param status: &#39;状态信息&#39; - ACTIVE 正常 - ERROR 异常
        :type status: str
        :param reason: 失败原因
        :type reason: str
        :param created_time: 创建时间
        :type created_time: datetime
        :param updated_time: 更新时间
        :type updated_time: datetime
        """
        
        

        self._id = None
        self._instance_id = None
        self._tenant_id = None
        self._name = None
        self._description = None
        self._global_dc_gateway_id = None
        self._bandwidth_info = None
        self._peer_site = None
        self._status = None
        self._reason = None
        self._created_time = None
        self._updated_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if instance_id is not None:
            self.instance_id = instance_id
        if tenant_id is not None:
            self.tenant_id = tenant_id
        self.name = name
        if description is not None:
            self.description = description
        if global_dc_gateway_id is not None:
            self.global_dc_gateway_id = global_dc_gateway_id
        if bandwidth_info is not None:
            self.bandwidth_info = bandwidth_info
        self.peer_site = peer_site
        if status is not None:
            self.status = status
        if reason is not None:
            self.reason = reason
        if created_time is not None:
            self.created_time = created_time
        if updated_time is not None:
            self.updated_time = updated_time

    @property
    def id(self):
        r"""Gets the id of this ExternalCreatePeerLink.

        专线对等连接

        :return: The id of this ExternalCreatePeerLink.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ExternalCreatePeerLink.

        专线对等连接

        :param id: The id of this ExternalCreatePeerLink.
        :type id: str
        """
        self._id = id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ExternalCreatePeerLink.

        专线对等连接实例ID

        :return: The instance_id of this ExternalCreatePeerLink.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ExternalCreatePeerLink.

        专线对等连接实例ID

        :param instance_id: The instance_id of this ExternalCreatePeerLink.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def tenant_id(self):
        r"""Gets the tenant_id of this ExternalCreatePeerLink.

        租户ID

        :return: The tenant_id of this ExternalCreatePeerLink.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        r"""Sets the tenant_id of this ExternalCreatePeerLink.

        租户ID

        :param tenant_id: The tenant_id of this ExternalCreatePeerLink.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def name(self):
        r"""Gets the name of this ExternalCreatePeerLink.

        名称

        :return: The name of this ExternalCreatePeerLink.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ExternalCreatePeerLink.

        名称

        :param name: The name of this ExternalCreatePeerLink.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this ExternalCreatePeerLink.

        描述信息

        :return: The description of this ExternalCreatePeerLink.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ExternalCreatePeerLink.

        描述信息

        :param description: The description of this ExternalCreatePeerLink.
        :type description: str
        """
        self._description = description

    @property
    def global_dc_gateway_id(self):
        r"""Gets the global_dc_gateway_id of this ExternalCreatePeerLink.

        全域接入网关ID

        :return: The global_dc_gateway_id of this ExternalCreatePeerLink.
        :rtype: str
        """
        return self._global_dc_gateway_id

    @global_dc_gateway_id.setter
    def global_dc_gateway_id(self, global_dc_gateway_id):
        r"""Sets the global_dc_gateway_id of this ExternalCreatePeerLink.

        全域接入网关ID

        :param global_dc_gateway_id: The global_dc_gateway_id of this ExternalCreatePeerLink.
        :type global_dc_gateway_id: str
        """
        self._global_dc_gateway_id = global_dc_gateway_id

    @property
    def bandwidth_info(self):
        r"""Gets the bandwidth_info of this ExternalCreatePeerLink.

        :return: The bandwidth_info of this ExternalCreatePeerLink.
        :rtype: :class:`huaweicloudsdkdc.v3.BandwidthInfoExternal`
        """
        return self._bandwidth_info

    @bandwidth_info.setter
    def bandwidth_info(self, bandwidth_info):
        r"""Sets the bandwidth_info of this ExternalCreatePeerLink.

        :param bandwidth_info: The bandwidth_info of this ExternalCreatePeerLink.
        :type bandwidth_info: :class:`huaweicloudsdkdc.v3.BandwidthInfoExternal`
        """
        self._bandwidth_info = bandwidth_info

    @property
    def peer_site(self):
        r"""Gets the peer_site of this ExternalCreatePeerLink.

        :return: The peer_site of this ExternalCreatePeerLink.
        :rtype: :class:`huaweicloudsdkdc.v3.PeerSiteExternal`
        """
        return self._peer_site

    @peer_site.setter
    def peer_site(self, peer_site):
        r"""Sets the peer_site of this ExternalCreatePeerLink.

        :param peer_site: The peer_site of this ExternalCreatePeerLink.
        :type peer_site: :class:`huaweicloudsdkdc.v3.PeerSiteExternal`
        """
        self._peer_site = peer_site

    @property
    def status(self):
        r"""Gets the status of this ExternalCreatePeerLink.

        '状态信息' - ACTIVE 正常 - ERROR 异常

        :return: The status of this ExternalCreatePeerLink.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ExternalCreatePeerLink.

        '状态信息' - ACTIVE 正常 - ERROR 异常

        :param status: The status of this ExternalCreatePeerLink.
        :type status: str
        """
        self._status = status

    @property
    def reason(self):
        r"""Gets the reason of this ExternalCreatePeerLink.

        失败原因

        :return: The reason of this ExternalCreatePeerLink.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        r"""Sets the reason of this ExternalCreatePeerLink.

        失败原因

        :param reason: The reason of this ExternalCreatePeerLink.
        :type reason: str
        """
        self._reason = reason

    @property
    def created_time(self):
        r"""Gets the created_time of this ExternalCreatePeerLink.

        创建时间

        :return: The created_time of this ExternalCreatePeerLink.
        :rtype: datetime
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        r"""Sets the created_time of this ExternalCreatePeerLink.

        创建时间

        :param created_time: The created_time of this ExternalCreatePeerLink.
        :type created_time: datetime
        """
        self._created_time = created_time

    @property
    def updated_time(self):
        r"""Gets the updated_time of this ExternalCreatePeerLink.

        更新时间

        :return: The updated_time of this ExternalCreatePeerLink.
        :rtype: datetime
        """
        return self._updated_time

    @updated_time.setter
    def updated_time(self, updated_time):
        r"""Sets the updated_time of this ExternalCreatePeerLink.

        更新时间

        :param updated_time: The updated_time of this ExternalCreatePeerLink.
        :type updated_time: datetime
        """
        self._updated_time = updated_time

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
        if not isinstance(other, ExternalCreatePeerLink):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
