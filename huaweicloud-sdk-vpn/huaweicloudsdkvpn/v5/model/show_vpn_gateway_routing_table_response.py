# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowVpnGatewayRoutingTableResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'routing_table': 'list[VpnGatewayRoutingTableEntryVo]',
        'total_count': 'int',
        'page_info': 'PageInfo'
    }

    attribute_map = {
        'routing_table': 'routing_table',
        'total_count': 'total_count',
        'page_info': 'page_info'
    }

    def __init__(self, routing_table=None, total_count=None, page_info=None):
        r"""ShowVpnGatewayRoutingTableResponse

        The model defined in huaweicloud sdk

        :param routing_table: VPN网关的路由表
        :type routing_table: list[:class:`huaweicloudsdkvpn.v5.VpnGatewayRoutingTableEntryVo`]
        :param total_count: 该网关下的路由总条数
        :type total_count: int
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkvpn.v5.PageInfo`
        """
        
        super(ShowVpnGatewayRoutingTableResponse, self).__init__()

        self._routing_table = None
        self._total_count = None
        self._page_info = None
        self.discriminator = None

        if routing_table is not None:
            self.routing_table = routing_table
        if total_count is not None:
            self.total_count = total_count
        if page_info is not None:
            self.page_info = page_info

    @property
    def routing_table(self):
        r"""Gets the routing_table of this ShowVpnGatewayRoutingTableResponse.

        VPN网关的路由表

        :return: The routing_table of this ShowVpnGatewayRoutingTableResponse.
        :rtype: list[:class:`huaweicloudsdkvpn.v5.VpnGatewayRoutingTableEntryVo`]
        """
        return self._routing_table

    @routing_table.setter
    def routing_table(self, routing_table):
        r"""Sets the routing_table of this ShowVpnGatewayRoutingTableResponse.

        VPN网关的路由表

        :param routing_table: The routing_table of this ShowVpnGatewayRoutingTableResponse.
        :type routing_table: list[:class:`huaweicloudsdkvpn.v5.VpnGatewayRoutingTableEntryVo`]
        """
        self._routing_table = routing_table

    @property
    def total_count(self):
        r"""Gets the total_count of this ShowVpnGatewayRoutingTableResponse.

        该网关下的路由总条数

        :return: The total_count of this ShowVpnGatewayRoutingTableResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ShowVpnGatewayRoutingTableResponse.

        该网关下的路由总条数

        :param total_count: The total_count of this ShowVpnGatewayRoutingTableResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def page_info(self):
        r"""Gets the page_info of this ShowVpnGatewayRoutingTableResponse.

        :return: The page_info of this ShowVpnGatewayRoutingTableResponse.
        :rtype: :class:`huaweicloudsdkvpn.v5.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ShowVpnGatewayRoutingTableResponse.

        :param page_info: The page_info of this ShowVpnGatewayRoutingTableResponse.
        :type page_info: :class:`huaweicloudsdkvpn.v5.PageInfo`
        """
        self._page_info = page_info

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
        if not isinstance(other, ShowVpnGatewayRoutingTableResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
