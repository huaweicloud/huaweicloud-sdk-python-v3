# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListGdgwRouteTablesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'request_id': 'str',
        'gdgw_routetables': 'list[CommonRoutetable]',
        'total_count': 'int',
        'page_info': 'PageInfo'
    }

    attribute_map = {
        'request_id': 'request_id',
        'gdgw_routetables': 'gdgw_routetables',
        'total_count': 'total_count',
        'page_info': 'page_info'
    }

    def __init__(self, request_id=None, gdgw_routetables=None, total_count=None, page_info=None):
        r"""ListGdgwRouteTablesResponse

        The model defined in huaweicloud sdk

        :param request_id: 请求id
        :type request_id: str
        :param gdgw_routetables: 全域接入网关路由表
        :type gdgw_routetables: list[:class:`huaweicloudsdkdc.v3.CommonRoutetable`]
        :param total_count: 总记录数。
        :type total_count: int
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkdc.v3.PageInfo`
        """
        
        super(ListGdgwRouteTablesResponse, self).__init__()

        self._request_id = None
        self._gdgw_routetables = None
        self._total_count = None
        self._page_info = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if gdgw_routetables is not None:
            self.gdgw_routetables = gdgw_routetables
        if total_count is not None:
            self.total_count = total_count
        if page_info is not None:
            self.page_info = page_info

    @property
    def request_id(self):
        r"""Gets the request_id of this ListGdgwRouteTablesResponse.

        请求id

        :return: The request_id of this ListGdgwRouteTablesResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this ListGdgwRouteTablesResponse.

        请求id

        :param request_id: The request_id of this ListGdgwRouteTablesResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def gdgw_routetables(self):
        r"""Gets the gdgw_routetables of this ListGdgwRouteTablesResponse.

        全域接入网关路由表

        :return: The gdgw_routetables of this ListGdgwRouteTablesResponse.
        :rtype: list[:class:`huaweicloudsdkdc.v3.CommonRoutetable`]
        """
        return self._gdgw_routetables

    @gdgw_routetables.setter
    def gdgw_routetables(self, gdgw_routetables):
        r"""Sets the gdgw_routetables of this ListGdgwRouteTablesResponse.

        全域接入网关路由表

        :param gdgw_routetables: The gdgw_routetables of this ListGdgwRouteTablesResponse.
        :type gdgw_routetables: list[:class:`huaweicloudsdkdc.v3.CommonRoutetable`]
        """
        self._gdgw_routetables = gdgw_routetables

    @property
    def total_count(self):
        r"""Gets the total_count of this ListGdgwRouteTablesResponse.

        总记录数。

        :return: The total_count of this ListGdgwRouteTablesResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListGdgwRouteTablesResponse.

        总记录数。

        :param total_count: The total_count of this ListGdgwRouteTablesResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def page_info(self):
        r"""Gets the page_info of this ListGdgwRouteTablesResponse.

        :return: The page_info of this ListGdgwRouteTablesResponse.
        :rtype: :class:`huaweicloudsdkdc.v3.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListGdgwRouteTablesResponse.

        :param page_info: The page_info of this ListGdgwRouteTablesResponse.
        :type page_info: :class:`huaweicloudsdkdc.v3.PageInfo`
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
        if not isinstance(other, ListGdgwRouteTablesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
