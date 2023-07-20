# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEffectiveRoutesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'route_table_id': 'str',
        'limit': 'int',
        'marker': 'str',
        'destination': 'list[str]',
        'resource_type': 'list[str]'
    }

    attribute_map = {
        'route_table_id': 'route_table_id',
        'limit': 'limit',
        'marker': 'marker',
        'destination': 'destination',
        'resource_type': 'resource_type'
    }

    def __init__(self, route_table_id=None, limit=None, marker=None, destination=None, resource_type=None):
        """ListEffectiveRoutesRequest

        The model defined in huaweicloud sdk

        :param route_table_id: 路由表ID
        :type route_table_id: str
        :param limit: 每页返回的个数。 取值范围：0~2000。
        :type limit: int
        :param marker: 上一页最后一条记录的企业路由器实例的id，为空时为查询第一页。 使用说明：必须与limit一起使用。
        :type marker: str
        :param destination: 路由目的地址
        :type destination: list[str]
        :param resource_type: - vpc：虚拟私有云 - vpn：vpn网关 - vgw：云专线的虚拟网关 - peering：对等连接，通过云连接CC加载不同区域的企业路由器来创建“对等连接（Peering）”连接 -  -  -  -
        :type resource_type: list[str]
        """
        
        

        self._route_table_id = None
        self._limit = None
        self._marker = None
        self._destination = None
        self._resource_type = None
        self.discriminator = None

        self.route_table_id = route_table_id
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if destination is not None:
            self.destination = destination
        if resource_type is not None:
            self.resource_type = resource_type

    @property
    def route_table_id(self):
        """Gets the route_table_id of this ListEffectiveRoutesRequest.

        路由表ID

        :return: The route_table_id of this ListEffectiveRoutesRequest.
        :rtype: str
        """
        return self._route_table_id

    @route_table_id.setter
    def route_table_id(self, route_table_id):
        """Sets the route_table_id of this ListEffectiveRoutesRequest.

        路由表ID

        :param route_table_id: The route_table_id of this ListEffectiveRoutesRequest.
        :type route_table_id: str
        """
        self._route_table_id = route_table_id

    @property
    def limit(self):
        """Gets the limit of this ListEffectiveRoutesRequest.

        每页返回的个数。 取值范围：0~2000。

        :return: The limit of this ListEffectiveRoutesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListEffectiveRoutesRequest.

        每页返回的个数。 取值范围：0~2000。

        :param limit: The limit of this ListEffectiveRoutesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListEffectiveRoutesRequest.

        上一页最后一条记录的企业路由器实例的id，为空时为查询第一页。 使用说明：必须与limit一起使用。

        :return: The marker of this ListEffectiveRoutesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListEffectiveRoutesRequest.

        上一页最后一条记录的企业路由器实例的id，为空时为查询第一页。 使用说明：必须与limit一起使用。

        :param marker: The marker of this ListEffectiveRoutesRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def destination(self):
        """Gets the destination of this ListEffectiveRoutesRequest.

        路由目的地址

        :return: The destination of this ListEffectiveRoutesRequest.
        :rtype: list[str]
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """Sets the destination of this ListEffectiveRoutesRequest.

        路由目的地址

        :param destination: The destination of this ListEffectiveRoutesRequest.
        :type destination: list[str]
        """
        self._destination = destination

    @property
    def resource_type(self):
        """Gets the resource_type of this ListEffectiveRoutesRequest.

        - vpc：虚拟私有云 - vpn：vpn网关 - vgw：云专线的虚拟网关 - peering：对等连接，通过云连接CC加载不同区域的企业路由器来创建“对等连接（Peering）”连接 -  -  -  -

        :return: The resource_type of this ListEffectiveRoutesRequest.
        :rtype: list[str]
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this ListEffectiveRoutesRequest.

        - vpc：虚拟私有云 - vpn：vpn网关 - vgw：云专线的虚拟网关 - peering：对等连接，通过云连接CC加载不同区域的企业路由器来创建“对等连接（Peering）”连接 -  -  -  -

        :param resource_type: The resource_type of this ListEffectiveRoutesRequest.
        :type resource_type: list[str]
        """
        self._resource_type = resource_type

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
        if not isinstance(other, ListEffectiveRoutesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
