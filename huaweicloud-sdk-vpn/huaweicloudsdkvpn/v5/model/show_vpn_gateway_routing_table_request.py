# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowVpnGatewayRoutingTableRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vgw_id': 'str',
        'limit': 'int',
        'marker': 'str',
        'offset': 'int',
        'is_include_nexthop_resource': 'bool'
    }

    attribute_map = {
        'vgw_id': 'vgw_id',
        'limit': 'limit',
        'marker': 'marker',
        'offset': 'offset',
        'is_include_nexthop_resource': 'is_include_nexthop_resource'
    }

    def __init__(self, vgw_id=None, limit=None, marker=None, offset=None, is_include_nexthop_resource=None):
        r"""ShowVpnGatewayRoutingTableRequest

        The model defined in huaweicloud sdk

        :param vgw_id: VPN网关实例ID
        :type vgw_id: str
        :param limit: 分页查询时每页返回的记录数量
        :type limit: int
        :param marker: 上一页最后一条资源记录的创建时间，为空时为查询第一页。使用说明：必须与limit一起使用。
        :type marker: str
        :param offset: 分页查询的偏移量
        :type offset: int
        :param is_include_nexthop_resource: 是否包含下一跳资源信息
        :type is_include_nexthop_resource: bool
        """
        
        

        self._vgw_id = None
        self._limit = None
        self._marker = None
        self._offset = None
        self._is_include_nexthop_resource = None
        self.discriminator = None

        self.vgw_id = vgw_id
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if offset is not None:
            self.offset = offset
        if is_include_nexthop_resource is not None:
            self.is_include_nexthop_resource = is_include_nexthop_resource

    @property
    def vgw_id(self):
        r"""Gets the vgw_id of this ShowVpnGatewayRoutingTableRequest.

        VPN网关实例ID

        :return: The vgw_id of this ShowVpnGatewayRoutingTableRequest.
        :rtype: str
        """
        return self._vgw_id

    @vgw_id.setter
    def vgw_id(self, vgw_id):
        r"""Sets the vgw_id of this ShowVpnGatewayRoutingTableRequest.

        VPN网关实例ID

        :param vgw_id: The vgw_id of this ShowVpnGatewayRoutingTableRequest.
        :type vgw_id: str
        """
        self._vgw_id = vgw_id

    @property
    def limit(self):
        r"""Gets the limit of this ShowVpnGatewayRoutingTableRequest.

        分页查询时每页返回的记录数量

        :return: The limit of this ShowVpnGatewayRoutingTableRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowVpnGatewayRoutingTableRequest.

        分页查询时每页返回的记录数量

        :param limit: The limit of this ShowVpnGatewayRoutingTableRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ShowVpnGatewayRoutingTableRequest.

        上一页最后一条资源记录的创建时间，为空时为查询第一页。使用说明：必须与limit一起使用。

        :return: The marker of this ShowVpnGatewayRoutingTableRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ShowVpnGatewayRoutingTableRequest.

        上一页最后一条资源记录的创建时间，为空时为查询第一页。使用说明：必须与limit一起使用。

        :param marker: The marker of this ShowVpnGatewayRoutingTableRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def offset(self):
        r"""Gets the offset of this ShowVpnGatewayRoutingTableRequest.

        分页查询的偏移量

        :return: The offset of this ShowVpnGatewayRoutingTableRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ShowVpnGatewayRoutingTableRequest.

        分页查询的偏移量

        :param offset: The offset of this ShowVpnGatewayRoutingTableRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def is_include_nexthop_resource(self):
        r"""Gets the is_include_nexthop_resource of this ShowVpnGatewayRoutingTableRequest.

        是否包含下一跳资源信息

        :return: The is_include_nexthop_resource of this ShowVpnGatewayRoutingTableRequest.
        :rtype: bool
        """
        return self._is_include_nexthop_resource

    @is_include_nexthop_resource.setter
    def is_include_nexthop_resource(self, is_include_nexthop_resource):
        r"""Sets the is_include_nexthop_resource of this ShowVpnGatewayRoutingTableRequest.

        是否包含下一跳资源信息

        :param is_include_nexthop_resource: The is_include_nexthop_resource of this ShowVpnGatewayRoutingTableRequest.
        :type is_include_nexthop_resource: bool
        """
        self._is_include_nexthop_resource = is_include_nexthop_resource

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
        if not isinstance(other, ShowVpnGatewayRoutingTableRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
