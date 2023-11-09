# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListVpnConnectionsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vpn_id': 'str',
        'eip_id': 'str',
        'vgw_ip': 'str',
        'vgw_id': 'str',
        'enterprise_project_id': 'list[str]',
        'limit': 'int',
        'marker': 'str'
    }

    attribute_map = {
        'vpn_id': 'vpn_id',
        'eip_id': 'eip_id',
        'vgw_ip': 'vgw_ip',
        'vgw_id': 'vgw_id',
        'enterprise_project_id': 'enterprise_project_id',
        'limit': 'limit',
        'marker': 'marker'
    }

    def __init__(self, vpn_id=None, eip_id=None, vgw_ip=None, vgw_id=None, enterprise_project_id=None, limit=None, marker=None):
        """ListVpnConnectionsRequest

        The model defined in huaweicloud sdk

        :param vpn_id: VPN ID
        :type vpn_id: str
        :param eip_id: Eip ID
        :type eip_id: str
        :param vgw_ip: VGW IP
        :type vgw_ip: str
        :param vgw_id: vgw ID
        :type vgw_id: str
        :param enterprise_project_id: 企业项目id
        :type enterprise_project_id: list[str]
        :param limit: 分页查询时每页返回的记录数量
        :type limit: int
        :param marker: 上一页最后一条记录的id，为空时为查询第一页。使用说明：必须与limit一起使用。
        :type marker: str
        """
        
        

        self._vpn_id = None
        self._eip_id = None
        self._vgw_ip = None
        self._vgw_id = None
        self._enterprise_project_id = None
        self._limit = None
        self._marker = None
        self.discriminator = None

        if vpn_id is not None:
            self.vpn_id = vpn_id
        if eip_id is not None:
            self.eip_id = eip_id
        if vgw_ip is not None:
            self.vgw_ip = vgw_ip
        if vgw_id is not None:
            self.vgw_id = vgw_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker

    @property
    def vpn_id(self):
        """Gets the vpn_id of this ListVpnConnectionsRequest.

        VPN ID

        :return: The vpn_id of this ListVpnConnectionsRequest.
        :rtype: str
        """
        return self._vpn_id

    @vpn_id.setter
    def vpn_id(self, vpn_id):
        """Sets the vpn_id of this ListVpnConnectionsRequest.

        VPN ID

        :param vpn_id: The vpn_id of this ListVpnConnectionsRequest.
        :type vpn_id: str
        """
        self._vpn_id = vpn_id

    @property
    def eip_id(self):
        """Gets the eip_id of this ListVpnConnectionsRequest.

        Eip ID

        :return: The eip_id of this ListVpnConnectionsRequest.
        :rtype: str
        """
        return self._eip_id

    @eip_id.setter
    def eip_id(self, eip_id):
        """Sets the eip_id of this ListVpnConnectionsRequest.

        Eip ID

        :param eip_id: The eip_id of this ListVpnConnectionsRequest.
        :type eip_id: str
        """
        self._eip_id = eip_id

    @property
    def vgw_ip(self):
        """Gets the vgw_ip of this ListVpnConnectionsRequest.

        VGW IP

        :return: The vgw_ip of this ListVpnConnectionsRequest.
        :rtype: str
        """
        return self._vgw_ip

    @vgw_ip.setter
    def vgw_ip(self, vgw_ip):
        """Sets the vgw_ip of this ListVpnConnectionsRequest.

        VGW IP

        :param vgw_ip: The vgw_ip of this ListVpnConnectionsRequest.
        :type vgw_ip: str
        """
        self._vgw_ip = vgw_ip

    @property
    def vgw_id(self):
        """Gets the vgw_id of this ListVpnConnectionsRequest.

        vgw ID

        :return: The vgw_id of this ListVpnConnectionsRequest.
        :rtype: str
        """
        return self._vgw_id

    @vgw_id.setter
    def vgw_id(self, vgw_id):
        """Sets the vgw_id of this ListVpnConnectionsRequest.

        vgw ID

        :param vgw_id: The vgw_id of this ListVpnConnectionsRequest.
        :type vgw_id: str
        """
        self._vgw_id = vgw_id

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListVpnConnectionsRequest.

        企业项目id

        :return: The enterprise_project_id of this ListVpnConnectionsRequest.
        :rtype: list[str]
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListVpnConnectionsRequest.

        企业项目id

        :param enterprise_project_id: The enterprise_project_id of this ListVpnConnectionsRequest.
        :type enterprise_project_id: list[str]
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def limit(self):
        """Gets the limit of this ListVpnConnectionsRequest.

        分页查询时每页返回的记录数量

        :return: The limit of this ListVpnConnectionsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListVpnConnectionsRequest.

        分页查询时每页返回的记录数量

        :param limit: The limit of this ListVpnConnectionsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListVpnConnectionsRequest.

        上一页最后一条记录的id，为空时为查询第一页。使用说明：必须与limit一起使用。

        :return: The marker of this ListVpnConnectionsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListVpnConnectionsRequest.

        上一页最后一条记录的id，为空时为查询第一页。使用说明：必须与limit一起使用。

        :param marker: The marker of this ListVpnConnectionsRequest.
        :type marker: str
        """
        self._marker = marker

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
        if not isinstance(other, ListVpnConnectionsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
