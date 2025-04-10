# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRdSforMySqlProxyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'proxy_query_info_list': 'list[QueryProxyResponseV3]',
        'max_proxy_num': 'int',
        'max_proxy_node_num': 'int',
        'support_balance_route_mode_for_favored_version': 'bool'
    }

    attribute_map = {
        'proxy_query_info_list': 'proxy_query_info_list',
        'max_proxy_num': 'max_proxy_num',
        'max_proxy_node_num': 'max_proxy_node_num',
        'support_balance_route_mode_for_favored_version': 'support_balance_route_mode_for_favored_version'
    }

    def __init__(self, proxy_query_info_list=None, max_proxy_num=None, max_proxy_node_num=None, support_balance_route_mode_for_favored_version=None):
        r"""ListRdSforMySqlProxyResponse

        The model defined in huaweicloud sdk

        :param proxy_query_info_list: 数据库实例下的数据库代理信息列表。
        :type proxy_query_info_list: list[:class:`huaweicloudsdkrds.v3.QueryProxyResponseV3`]
        :param max_proxy_num: 支持同时开启的数据库代理的最大数量。
        :type max_proxy_num: int
        :param max_proxy_node_num: 单个数据库代理支持选择的代理节点的最大数量。
        :type max_proxy_node_num: int
        :param support_balance_route_mode_for_favored_version: 是否支持创建数据库代理时设置负载均衡路由模式。
        :type support_balance_route_mode_for_favored_version: bool
        """
        
        super(ListRdSforMySqlProxyResponse, self).__init__()

        self._proxy_query_info_list = None
        self._max_proxy_num = None
        self._max_proxy_node_num = None
        self._support_balance_route_mode_for_favored_version = None
        self.discriminator = None

        if proxy_query_info_list is not None:
            self.proxy_query_info_list = proxy_query_info_list
        if max_proxy_num is not None:
            self.max_proxy_num = max_proxy_num
        if max_proxy_node_num is not None:
            self.max_proxy_node_num = max_proxy_node_num
        if support_balance_route_mode_for_favored_version is not None:
            self.support_balance_route_mode_for_favored_version = support_balance_route_mode_for_favored_version

    @property
    def proxy_query_info_list(self):
        r"""Gets the proxy_query_info_list of this ListRdSforMySqlProxyResponse.

        数据库实例下的数据库代理信息列表。

        :return: The proxy_query_info_list of this ListRdSforMySqlProxyResponse.
        :rtype: list[:class:`huaweicloudsdkrds.v3.QueryProxyResponseV3`]
        """
        return self._proxy_query_info_list

    @proxy_query_info_list.setter
    def proxy_query_info_list(self, proxy_query_info_list):
        r"""Sets the proxy_query_info_list of this ListRdSforMySqlProxyResponse.

        数据库实例下的数据库代理信息列表。

        :param proxy_query_info_list: The proxy_query_info_list of this ListRdSforMySqlProxyResponse.
        :type proxy_query_info_list: list[:class:`huaweicloudsdkrds.v3.QueryProxyResponseV3`]
        """
        self._proxy_query_info_list = proxy_query_info_list

    @property
    def max_proxy_num(self):
        r"""Gets the max_proxy_num of this ListRdSforMySqlProxyResponse.

        支持同时开启的数据库代理的最大数量。

        :return: The max_proxy_num of this ListRdSforMySqlProxyResponse.
        :rtype: int
        """
        return self._max_proxy_num

    @max_proxy_num.setter
    def max_proxy_num(self, max_proxy_num):
        r"""Sets the max_proxy_num of this ListRdSforMySqlProxyResponse.

        支持同时开启的数据库代理的最大数量。

        :param max_proxy_num: The max_proxy_num of this ListRdSforMySqlProxyResponse.
        :type max_proxy_num: int
        """
        self._max_proxy_num = max_proxy_num

    @property
    def max_proxy_node_num(self):
        r"""Gets the max_proxy_node_num of this ListRdSforMySqlProxyResponse.

        单个数据库代理支持选择的代理节点的最大数量。

        :return: The max_proxy_node_num of this ListRdSforMySqlProxyResponse.
        :rtype: int
        """
        return self._max_proxy_node_num

    @max_proxy_node_num.setter
    def max_proxy_node_num(self, max_proxy_node_num):
        r"""Sets the max_proxy_node_num of this ListRdSforMySqlProxyResponse.

        单个数据库代理支持选择的代理节点的最大数量。

        :param max_proxy_node_num: The max_proxy_node_num of this ListRdSforMySqlProxyResponse.
        :type max_proxy_node_num: int
        """
        self._max_proxy_node_num = max_proxy_node_num

    @property
    def support_balance_route_mode_for_favored_version(self):
        r"""Gets the support_balance_route_mode_for_favored_version of this ListRdSforMySqlProxyResponse.

        是否支持创建数据库代理时设置负载均衡路由模式。

        :return: The support_balance_route_mode_for_favored_version of this ListRdSforMySqlProxyResponse.
        :rtype: bool
        """
        return self._support_balance_route_mode_for_favored_version

    @support_balance_route_mode_for_favored_version.setter
    def support_balance_route_mode_for_favored_version(self, support_balance_route_mode_for_favored_version):
        r"""Sets the support_balance_route_mode_for_favored_version of this ListRdSforMySqlProxyResponse.

        是否支持创建数据库代理时设置负载均衡路由模式。

        :param support_balance_route_mode_for_favored_version: The support_balance_route_mode_for_favored_version of this ListRdSforMySqlProxyResponse.
        :type support_balance_route_mode_for_favored_version: bool
        """
        self._support_balance_route_mode_for_favored_version = support_balance_route_mode_for_favored_version

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
        if not isinstance(other, ListRdSforMySqlProxyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
