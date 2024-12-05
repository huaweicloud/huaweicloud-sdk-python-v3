# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExternalUpdatePeerLink:

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

    def __init__(self, id=None, tenant_id=None, name=None, description=None, global_dc_gateway_id=None, bandwidth_info=None, peer_site=None, status=None, reason=None, created_time=None, updated_time=None):
        """ExternalUpdatePeerLink

        The model defined in huaweicloud sdk

        :param id: 
        :type id: str
        :param tenant_id: 
        :type tenant_id: str
        :param name: 
        :type name: str
        :param description: 
        :type description: str
        :param global_dc_gateway_id: 
        :type global_dc_gateway_id: str
        :param bandwidth_info: 
        :type bandwidth_info: :class:`huaweicloudsdkdc.v3.BandwidthInfoExternal`
        :param peer_site: 
        :type peer_site: :class:`huaweicloudsdkdc.v3.PeerSiteExternal`
        :param status: 
        :type status: str
        :param reason: 
        :type reason: str
        :param created_time: 
        :type created_time: datetime
        :param updated_time: 
        :type updated_time: datetime
        """
        
        

        self._id = None
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
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if global_dc_gateway_id is not None:
            self.global_dc_gateway_id = global_dc_gateway_id
        if bandwidth_info is not None:
            self.bandwidth_info = bandwidth_info
        if peer_site is not None:
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
        """Gets the id of this ExternalUpdatePeerLink.

        :return: The id of this ExternalUpdatePeerLink.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ExternalUpdatePeerLink.

        :param id: The id of this ExternalUpdatePeerLink.
        :type id: str
        """
        self._id = id

    @property
    def tenant_id(self):
        """Gets the tenant_id of this ExternalUpdatePeerLink.

        :return: The tenant_id of this ExternalUpdatePeerLink.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this ExternalUpdatePeerLink.

        :param tenant_id: The tenant_id of this ExternalUpdatePeerLink.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def name(self):
        """Gets the name of this ExternalUpdatePeerLink.

        :return: The name of this ExternalUpdatePeerLink.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ExternalUpdatePeerLink.

        :param name: The name of this ExternalUpdatePeerLink.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this ExternalUpdatePeerLink.

        :return: The description of this ExternalUpdatePeerLink.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ExternalUpdatePeerLink.

        :param description: The description of this ExternalUpdatePeerLink.
        :type description: str
        """
        self._description = description

    @property
    def global_dc_gateway_id(self):
        """Gets the global_dc_gateway_id of this ExternalUpdatePeerLink.

        :return: The global_dc_gateway_id of this ExternalUpdatePeerLink.
        :rtype: str
        """
        return self._global_dc_gateway_id

    @global_dc_gateway_id.setter
    def global_dc_gateway_id(self, global_dc_gateway_id):
        """Sets the global_dc_gateway_id of this ExternalUpdatePeerLink.

        :param global_dc_gateway_id: The global_dc_gateway_id of this ExternalUpdatePeerLink.
        :type global_dc_gateway_id: str
        """
        self._global_dc_gateway_id = global_dc_gateway_id

    @property
    def bandwidth_info(self):
        """Gets the bandwidth_info of this ExternalUpdatePeerLink.

        :return: The bandwidth_info of this ExternalUpdatePeerLink.
        :rtype: :class:`huaweicloudsdkdc.v3.BandwidthInfoExternal`
        """
        return self._bandwidth_info

    @bandwidth_info.setter
    def bandwidth_info(self, bandwidth_info):
        """Sets the bandwidth_info of this ExternalUpdatePeerLink.

        :param bandwidth_info: The bandwidth_info of this ExternalUpdatePeerLink.
        :type bandwidth_info: :class:`huaweicloudsdkdc.v3.BandwidthInfoExternal`
        """
        self._bandwidth_info = bandwidth_info

    @property
    def peer_site(self):
        """Gets the peer_site of this ExternalUpdatePeerLink.

        :return: The peer_site of this ExternalUpdatePeerLink.
        :rtype: :class:`huaweicloudsdkdc.v3.PeerSiteExternal`
        """
        return self._peer_site

    @peer_site.setter
    def peer_site(self, peer_site):
        """Sets the peer_site of this ExternalUpdatePeerLink.

        :param peer_site: The peer_site of this ExternalUpdatePeerLink.
        :type peer_site: :class:`huaweicloudsdkdc.v3.PeerSiteExternal`
        """
        self._peer_site = peer_site

    @property
    def status(self):
        """Gets the status of this ExternalUpdatePeerLink.

        :return: The status of this ExternalUpdatePeerLink.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ExternalUpdatePeerLink.

        :param status: The status of this ExternalUpdatePeerLink.
        :type status: str
        """
        self._status = status

    @property
    def reason(self):
        """Gets the reason of this ExternalUpdatePeerLink.

        :return: The reason of this ExternalUpdatePeerLink.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this ExternalUpdatePeerLink.

        :param reason: The reason of this ExternalUpdatePeerLink.
        :type reason: str
        """
        self._reason = reason

    @property
    def created_time(self):
        """Gets the created_time of this ExternalUpdatePeerLink.

        :return: The created_time of this ExternalUpdatePeerLink.
        :rtype: datetime
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this ExternalUpdatePeerLink.

        :param created_time: The created_time of this ExternalUpdatePeerLink.
        :type created_time: datetime
        """
        self._created_time = created_time

    @property
    def updated_time(self):
        """Gets the updated_time of this ExternalUpdatePeerLink.

        :return: The updated_time of this ExternalUpdatePeerLink.
        :rtype: datetime
        """
        return self._updated_time

    @updated_time.setter
    def updated_time(self, updated_time):
        """Sets the updated_time of this ExternalUpdatePeerLink.

        :param updated_time: The updated_time of this ExternalUpdatePeerLink.
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
        if not isinstance(other, ExternalUpdatePeerLink):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
