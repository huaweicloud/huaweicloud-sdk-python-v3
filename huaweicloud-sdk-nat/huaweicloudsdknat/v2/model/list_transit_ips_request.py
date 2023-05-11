# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTransitIpsRequest:

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
        'page_reverse': 'bool',
        'id': 'list[str]',
        'network_interface_id': 'list[str]',
        'ip_address': 'list[str]',
        'gateway_id': 'list[str]',
        'enterprise_project_id': 'list[str]',
        'virsubnet_id': 'list[str]'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker',
        'page_reverse': 'page_reverse',
        'id': 'id',
        'network_interface_id': 'network_interface_id',
        'ip_address': 'ip_address',
        'gateway_id': 'gateway_id',
        'enterprise_project_id': 'enterprise_project_id',
        'virsubnet_id': 'virsubnet_id'
    }

    def __init__(self, limit=None, marker=None, page_reverse=None, id=None, network_interface_id=None, ip_address=None, gateway_id=None, enterprise_project_id=None, virsubnet_id=None):
        """ListTransitIpsRequest

        The model defined in huaweicloud sdk

        :param limit: 功能说明：每页返回的个数。 取值范围：0~2000。 默认值：2000。
        :type limit: int
        :param marker: 功能说明：分页查询起始的资源ID，为空时查询第一页。 值从上一次查询的PageInfo中的next_marker或者previous_marker中获取。
        :type marker: str
        :param page_reverse: 是否查询前一页。
        :type page_reverse: bool
        :param id: 中转IP的ID。
        :type id: list[str]
        :param network_interface_id: 中转IP的网络接口ID。
        :type network_interface_id: list[str]
        :param ip_address: 中转IP地址。
        :type ip_address: list[str]
        :param gateway_id: 中转IP绑定的私网NAT网关实例的ID。
        :type gateway_id: list[str]
        :param enterprise_project_id: 企业项目ID。创建中转IP时，关联的企业项目ID。
        :type enterprise_project_id: list[str]
        :param virsubnet_id: 当前租户子网的ID。
        :type virsubnet_id: list[str]
        """
        
        

        self._limit = None
        self._marker = None
        self._page_reverse = None
        self._id = None
        self._network_interface_id = None
        self._ip_address = None
        self._gateway_id = None
        self._enterprise_project_id = None
        self._virsubnet_id = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if page_reverse is not None:
            self.page_reverse = page_reverse
        if id is not None:
            self.id = id
        if network_interface_id is not None:
            self.network_interface_id = network_interface_id
        if ip_address is not None:
            self.ip_address = ip_address
        if gateway_id is not None:
            self.gateway_id = gateway_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if virsubnet_id is not None:
            self.virsubnet_id = virsubnet_id

    @property
    def limit(self):
        """Gets the limit of this ListTransitIpsRequest.

        功能说明：每页返回的个数。 取值范围：0~2000。 默认值：2000。

        :return: The limit of this ListTransitIpsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListTransitIpsRequest.

        功能说明：每页返回的个数。 取值范围：0~2000。 默认值：2000。

        :param limit: The limit of this ListTransitIpsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListTransitIpsRequest.

        功能说明：分页查询起始的资源ID，为空时查询第一页。 值从上一次查询的PageInfo中的next_marker或者previous_marker中获取。

        :return: The marker of this ListTransitIpsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListTransitIpsRequest.

        功能说明：分页查询起始的资源ID，为空时查询第一页。 值从上一次查询的PageInfo中的next_marker或者previous_marker中获取。

        :param marker: The marker of this ListTransitIpsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def page_reverse(self):
        """Gets the page_reverse of this ListTransitIpsRequest.

        是否查询前一页。

        :return: The page_reverse of this ListTransitIpsRequest.
        :rtype: bool
        """
        return self._page_reverse

    @page_reverse.setter
    def page_reverse(self, page_reverse):
        """Sets the page_reverse of this ListTransitIpsRequest.

        是否查询前一页。

        :param page_reverse: The page_reverse of this ListTransitIpsRequest.
        :type page_reverse: bool
        """
        self._page_reverse = page_reverse

    @property
    def id(self):
        """Gets the id of this ListTransitIpsRequest.

        中转IP的ID。

        :return: The id of this ListTransitIpsRequest.
        :rtype: list[str]
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListTransitIpsRequest.

        中转IP的ID。

        :param id: The id of this ListTransitIpsRequest.
        :type id: list[str]
        """
        self._id = id

    @property
    def network_interface_id(self):
        """Gets the network_interface_id of this ListTransitIpsRequest.

        中转IP的网络接口ID。

        :return: The network_interface_id of this ListTransitIpsRequest.
        :rtype: list[str]
        """
        return self._network_interface_id

    @network_interface_id.setter
    def network_interface_id(self, network_interface_id):
        """Sets the network_interface_id of this ListTransitIpsRequest.

        中转IP的网络接口ID。

        :param network_interface_id: The network_interface_id of this ListTransitIpsRequest.
        :type network_interface_id: list[str]
        """
        self._network_interface_id = network_interface_id

    @property
    def ip_address(self):
        """Gets the ip_address of this ListTransitIpsRequest.

        中转IP地址。

        :return: The ip_address of this ListTransitIpsRequest.
        :rtype: list[str]
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this ListTransitIpsRequest.

        中转IP地址。

        :param ip_address: The ip_address of this ListTransitIpsRequest.
        :type ip_address: list[str]
        """
        self._ip_address = ip_address

    @property
    def gateway_id(self):
        """Gets the gateway_id of this ListTransitIpsRequest.

        中转IP绑定的私网NAT网关实例的ID。

        :return: The gateway_id of this ListTransitIpsRequest.
        :rtype: list[str]
        """
        return self._gateway_id

    @gateway_id.setter
    def gateway_id(self, gateway_id):
        """Sets the gateway_id of this ListTransitIpsRequest.

        中转IP绑定的私网NAT网关实例的ID。

        :param gateway_id: The gateway_id of this ListTransitIpsRequest.
        :type gateway_id: list[str]
        """
        self._gateway_id = gateway_id

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListTransitIpsRequest.

        企业项目ID。创建中转IP时，关联的企业项目ID。

        :return: The enterprise_project_id of this ListTransitIpsRequest.
        :rtype: list[str]
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListTransitIpsRequest.

        企业项目ID。创建中转IP时，关联的企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this ListTransitIpsRequest.
        :type enterprise_project_id: list[str]
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def virsubnet_id(self):
        """Gets the virsubnet_id of this ListTransitIpsRequest.

        当前租户子网的ID。

        :return: The virsubnet_id of this ListTransitIpsRequest.
        :rtype: list[str]
        """
        return self._virsubnet_id

    @virsubnet_id.setter
    def virsubnet_id(self, virsubnet_id):
        """Sets the virsubnet_id of this ListTransitIpsRequest.

        当前租户子网的ID。

        :param virsubnet_id: The virsubnet_id of this ListTransitIpsRequest.
        :type virsubnet_id: list[str]
        """
        self._virsubnet_id = virsubnet_id

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
        if not isinstance(other, ListTransitIpsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
