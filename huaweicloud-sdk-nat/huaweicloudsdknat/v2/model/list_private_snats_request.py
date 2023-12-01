# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPrivateSnatsRequest:

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
        'description': 'list[str]',
        'gateway_id': 'list[str]',
        'cidr': 'list[str]',
        'virsubnet_id': 'list[str]',
        'transit_ip_id': 'list[str]',
        'transit_ip_address': 'list[str]',
        'enterprise_project_id': 'list[str]'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker',
        'page_reverse': 'page_reverse',
        'id': 'id',
        'description': 'description',
        'gateway_id': 'gateway_id',
        'cidr': 'cidr',
        'virsubnet_id': 'virsubnet_id',
        'transit_ip_id': 'transit_ip_id',
        'transit_ip_address': 'transit_ip_address',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, limit=None, marker=None, page_reverse=None, id=None, description=None, gateway_id=None, cidr=None, virsubnet_id=None, transit_ip_id=None, transit_ip_address=None, enterprise_project_id=None):
        """ListPrivateSnatsRequest

        The model defined in huaweicloud sdk

        :param limit: 功能说明：每页返回的个数。 取值范围：0~2000。 默认值：2000。
        :type limit: int
        :param marker: 功能说明：分页查询起始的资源ID，为空时查询第一页。 值从上一次查询的PageInfo中的next_marker或者previous_marker中获取。
        :type marker: str
        :param page_reverse: 是否查询前一页。
        :type page_reverse: bool
        :param id: SNAT规则的ID。
        :type id: list[str]
        :param description: SNAT规则的描述。长度范围小于等于255个字符，不能包含“&lt;”和“&gt;”。
        :type description: list[str]
        :param gateway_id: 私网NAT网关实例的ID。
        :type gateway_id: list[str]
        :param cidr: 规则匹配的CIDR。
        :type cidr: list[str]
        :param virsubnet_id: 规则匹配的子网的ID。
        :type virsubnet_id: list[str]
        :param transit_ip_id: 中转IP的ID。
        :type transit_ip_id: list[str]
        :param transit_ip_address: 中转IP地址。
        :type transit_ip_address: list[str]
        :param enterprise_project_id: 企业项目ID。创建SNAT规则时，关联的企业项目ID。
        :type enterprise_project_id: list[str]
        """
        
        

        self._limit = None
        self._marker = None
        self._page_reverse = None
        self._id = None
        self._description = None
        self._gateway_id = None
        self._cidr = None
        self._virsubnet_id = None
        self._transit_ip_id = None
        self._transit_ip_address = None
        self._enterprise_project_id = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if page_reverse is not None:
            self.page_reverse = page_reverse
        if id is not None:
            self.id = id
        if description is not None:
            self.description = description
        if gateway_id is not None:
            self.gateway_id = gateway_id
        if cidr is not None:
            self.cidr = cidr
        if virsubnet_id is not None:
            self.virsubnet_id = virsubnet_id
        if transit_ip_id is not None:
            self.transit_ip_id = transit_ip_id
        if transit_ip_address is not None:
            self.transit_ip_address = transit_ip_address
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def limit(self):
        """Gets the limit of this ListPrivateSnatsRequest.

        功能说明：每页返回的个数。 取值范围：0~2000。 默认值：2000。

        :return: The limit of this ListPrivateSnatsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListPrivateSnatsRequest.

        功能说明：每页返回的个数。 取值范围：0~2000。 默认值：2000。

        :param limit: The limit of this ListPrivateSnatsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListPrivateSnatsRequest.

        功能说明：分页查询起始的资源ID，为空时查询第一页。 值从上一次查询的PageInfo中的next_marker或者previous_marker中获取。

        :return: The marker of this ListPrivateSnatsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListPrivateSnatsRequest.

        功能说明：分页查询起始的资源ID，为空时查询第一页。 值从上一次查询的PageInfo中的next_marker或者previous_marker中获取。

        :param marker: The marker of this ListPrivateSnatsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def page_reverse(self):
        """Gets the page_reverse of this ListPrivateSnatsRequest.

        是否查询前一页。

        :return: The page_reverse of this ListPrivateSnatsRequest.
        :rtype: bool
        """
        return self._page_reverse

    @page_reverse.setter
    def page_reverse(self, page_reverse):
        """Sets the page_reverse of this ListPrivateSnatsRequest.

        是否查询前一页。

        :param page_reverse: The page_reverse of this ListPrivateSnatsRequest.
        :type page_reverse: bool
        """
        self._page_reverse = page_reverse

    @property
    def id(self):
        """Gets the id of this ListPrivateSnatsRequest.

        SNAT规则的ID。

        :return: The id of this ListPrivateSnatsRequest.
        :rtype: list[str]
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListPrivateSnatsRequest.

        SNAT规则的ID。

        :param id: The id of this ListPrivateSnatsRequest.
        :type id: list[str]
        """
        self._id = id

    @property
    def description(self):
        """Gets the description of this ListPrivateSnatsRequest.

        SNAT规则的描述。长度范围小于等于255个字符，不能包含“<”和“>”。

        :return: The description of this ListPrivateSnatsRequest.
        :rtype: list[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ListPrivateSnatsRequest.

        SNAT规则的描述。长度范围小于等于255个字符，不能包含“<”和“>”。

        :param description: The description of this ListPrivateSnatsRequest.
        :type description: list[str]
        """
        self._description = description

    @property
    def gateway_id(self):
        """Gets the gateway_id of this ListPrivateSnatsRequest.

        私网NAT网关实例的ID。

        :return: The gateway_id of this ListPrivateSnatsRequest.
        :rtype: list[str]
        """
        return self._gateway_id

    @gateway_id.setter
    def gateway_id(self, gateway_id):
        """Sets the gateway_id of this ListPrivateSnatsRequest.

        私网NAT网关实例的ID。

        :param gateway_id: The gateway_id of this ListPrivateSnatsRequest.
        :type gateway_id: list[str]
        """
        self._gateway_id = gateway_id

    @property
    def cidr(self):
        """Gets the cidr of this ListPrivateSnatsRequest.

        规则匹配的CIDR。

        :return: The cidr of this ListPrivateSnatsRequest.
        :rtype: list[str]
        """
        return self._cidr

    @cidr.setter
    def cidr(self, cidr):
        """Sets the cidr of this ListPrivateSnatsRequest.

        规则匹配的CIDR。

        :param cidr: The cidr of this ListPrivateSnatsRequest.
        :type cidr: list[str]
        """
        self._cidr = cidr

    @property
    def virsubnet_id(self):
        """Gets the virsubnet_id of this ListPrivateSnatsRequest.

        规则匹配的子网的ID。

        :return: The virsubnet_id of this ListPrivateSnatsRequest.
        :rtype: list[str]
        """
        return self._virsubnet_id

    @virsubnet_id.setter
    def virsubnet_id(self, virsubnet_id):
        """Sets the virsubnet_id of this ListPrivateSnatsRequest.

        规则匹配的子网的ID。

        :param virsubnet_id: The virsubnet_id of this ListPrivateSnatsRequest.
        :type virsubnet_id: list[str]
        """
        self._virsubnet_id = virsubnet_id

    @property
    def transit_ip_id(self):
        """Gets the transit_ip_id of this ListPrivateSnatsRequest.

        中转IP的ID。

        :return: The transit_ip_id of this ListPrivateSnatsRequest.
        :rtype: list[str]
        """
        return self._transit_ip_id

    @transit_ip_id.setter
    def transit_ip_id(self, transit_ip_id):
        """Sets the transit_ip_id of this ListPrivateSnatsRequest.

        中转IP的ID。

        :param transit_ip_id: The transit_ip_id of this ListPrivateSnatsRequest.
        :type transit_ip_id: list[str]
        """
        self._transit_ip_id = transit_ip_id

    @property
    def transit_ip_address(self):
        """Gets the transit_ip_address of this ListPrivateSnatsRequest.

        中转IP地址。

        :return: The transit_ip_address of this ListPrivateSnatsRequest.
        :rtype: list[str]
        """
        return self._transit_ip_address

    @transit_ip_address.setter
    def transit_ip_address(self, transit_ip_address):
        """Sets the transit_ip_address of this ListPrivateSnatsRequest.

        中转IP地址。

        :param transit_ip_address: The transit_ip_address of this ListPrivateSnatsRequest.
        :type transit_ip_address: list[str]
        """
        self._transit_ip_address = transit_ip_address

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListPrivateSnatsRequest.

        企业项目ID。创建SNAT规则时，关联的企业项目ID。

        :return: The enterprise_project_id of this ListPrivateSnatsRequest.
        :rtype: list[str]
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListPrivateSnatsRequest.

        企业项目ID。创建SNAT规则时，关联的企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this ListPrivateSnatsRequest.
        :type enterprise_project_id: list[str]
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, ListPrivateSnatsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
