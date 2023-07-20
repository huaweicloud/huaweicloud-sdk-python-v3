# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListStaticRoutesRequest:

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
        'attachment_id': 'list[str]',
        'resource_type': 'list[str]',
        'sort_key': 'list[str]',
        'sort_dir': 'list[str]'
    }

    attribute_map = {
        'route_table_id': 'route_table_id',
        'limit': 'limit',
        'marker': 'marker',
        'destination': 'destination',
        'attachment_id': 'attachment_id',
        'resource_type': 'resource_type',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir'
    }

    def __init__(self, route_table_id=None, limit=None, marker=None, destination=None, attachment_id=None, resource_type=None, sort_key=None, sort_dir=None):
        """ListStaticRoutesRequest

        The model defined in huaweicloud sdk

        :param route_table_id: 路由表ID
        :type route_table_id: str
        :param limit: 每页返回的个数。 取值范围：0~2000。
        :type limit: int
        :param marker: 上一页最后一条记录的企业路由器实例的id，为空时为查询第一页。 使用说明：必须与limit一起使用。
        :type marker: str
        :param destination: 路由目的地址
        :type destination: list[str]
        :param attachment_id: 连接ID
        :type attachment_id: list[str]
        :param resource_type: - vpc：虚拟私有云 - vpn：vpn网关 - vgw：云专线的虚拟网关 - peering：对等连接，通过云连接CC加载不同区域的企业路由器来创建“对等连接（Peering）”连接 -  -  -  -
        :type resource_type: list[str]
        :param sort_key: 按关键字排序，默认按照id排序，可选值:id|name|state
        :type sort_key: list[str]
        :param sort_dir: 返回结果按照升序或降序排列，默认为asc,降序为desc
        :type sort_dir: list[str]
        """
        
        

        self._route_table_id = None
        self._limit = None
        self._marker = None
        self._destination = None
        self._attachment_id = None
        self._resource_type = None
        self._sort_key = None
        self._sort_dir = None
        self.discriminator = None

        self.route_table_id = route_table_id
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if destination is not None:
            self.destination = destination
        if attachment_id is not None:
            self.attachment_id = attachment_id
        if resource_type is not None:
            self.resource_type = resource_type
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_dir is not None:
            self.sort_dir = sort_dir

    @property
    def route_table_id(self):
        """Gets the route_table_id of this ListStaticRoutesRequest.

        路由表ID

        :return: The route_table_id of this ListStaticRoutesRequest.
        :rtype: str
        """
        return self._route_table_id

    @route_table_id.setter
    def route_table_id(self, route_table_id):
        """Sets the route_table_id of this ListStaticRoutesRequest.

        路由表ID

        :param route_table_id: The route_table_id of this ListStaticRoutesRequest.
        :type route_table_id: str
        """
        self._route_table_id = route_table_id

    @property
    def limit(self):
        """Gets the limit of this ListStaticRoutesRequest.

        每页返回的个数。 取值范围：0~2000。

        :return: The limit of this ListStaticRoutesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListStaticRoutesRequest.

        每页返回的个数。 取值范围：0~2000。

        :param limit: The limit of this ListStaticRoutesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListStaticRoutesRequest.

        上一页最后一条记录的企业路由器实例的id，为空时为查询第一页。 使用说明：必须与limit一起使用。

        :return: The marker of this ListStaticRoutesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListStaticRoutesRequest.

        上一页最后一条记录的企业路由器实例的id，为空时为查询第一页。 使用说明：必须与limit一起使用。

        :param marker: The marker of this ListStaticRoutesRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def destination(self):
        """Gets the destination of this ListStaticRoutesRequest.

        路由目的地址

        :return: The destination of this ListStaticRoutesRequest.
        :rtype: list[str]
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """Sets the destination of this ListStaticRoutesRequest.

        路由目的地址

        :param destination: The destination of this ListStaticRoutesRequest.
        :type destination: list[str]
        """
        self._destination = destination

    @property
    def attachment_id(self):
        """Gets the attachment_id of this ListStaticRoutesRequest.

        连接ID

        :return: The attachment_id of this ListStaticRoutesRequest.
        :rtype: list[str]
        """
        return self._attachment_id

    @attachment_id.setter
    def attachment_id(self, attachment_id):
        """Sets the attachment_id of this ListStaticRoutesRequest.

        连接ID

        :param attachment_id: The attachment_id of this ListStaticRoutesRequest.
        :type attachment_id: list[str]
        """
        self._attachment_id = attachment_id

    @property
    def resource_type(self):
        """Gets the resource_type of this ListStaticRoutesRequest.

        - vpc：虚拟私有云 - vpn：vpn网关 - vgw：云专线的虚拟网关 - peering：对等连接，通过云连接CC加载不同区域的企业路由器来创建“对等连接（Peering）”连接 -  -  -  -

        :return: The resource_type of this ListStaticRoutesRequest.
        :rtype: list[str]
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this ListStaticRoutesRequest.

        - vpc：虚拟私有云 - vpn：vpn网关 - vgw：云专线的虚拟网关 - peering：对等连接，通过云连接CC加载不同区域的企业路由器来创建“对等连接（Peering）”连接 -  -  -  -

        :param resource_type: The resource_type of this ListStaticRoutesRequest.
        :type resource_type: list[str]
        """
        self._resource_type = resource_type

    @property
    def sort_key(self):
        """Gets the sort_key of this ListStaticRoutesRequest.

        按关键字排序，默认按照id排序，可选值:id|name|state

        :return: The sort_key of this ListStaticRoutesRequest.
        :rtype: list[str]
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        """Sets the sort_key of this ListStaticRoutesRequest.

        按关键字排序，默认按照id排序，可选值:id|name|state

        :param sort_key: The sort_key of this ListStaticRoutesRequest.
        :type sort_key: list[str]
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        """Gets the sort_dir of this ListStaticRoutesRequest.

        返回结果按照升序或降序排列，默认为asc,降序为desc

        :return: The sort_dir of this ListStaticRoutesRequest.
        :rtype: list[str]
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        """Sets the sort_dir of this ListStaticRoutesRequest.

        返回结果按照升序或降序排列，默认为asc,降序为desc

        :param sort_dir: The sort_dir of this ListStaticRoutesRequest.
        :type sort_dir: list[str]
        """
        self._sort_dir = sort_dir

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
        if not isinstance(other, ListStaticRoutesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
