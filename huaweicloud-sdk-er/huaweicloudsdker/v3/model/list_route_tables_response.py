# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRouteTablesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'route_tables': 'list[RouteTable]',
        'request_id': 'str',
        'page_info': 'PageInfo'
    }

    attribute_map = {
        'route_tables': 'route_tables',
        'request_id': 'request_id',
        'page_info': 'page_info'
    }

    def __init__(self, route_tables=None, request_id=None, page_info=None):
        """ListRouteTablesResponse

        The model defined in huaweicloud sdk

        :param route_tables: 路由表列表
        :type route_tables: list[:class:`huaweicloudsdker.v3.RouteTable`]
        :param request_id: 请求ID
        :type request_id: str
        :param page_info: 
        :type page_info: :class:`huaweicloudsdker.v3.PageInfo`
        """
        
        super(ListRouteTablesResponse, self).__init__()

        self._route_tables = None
        self._request_id = None
        self._page_info = None
        self.discriminator = None

        if route_tables is not None:
            self.route_tables = route_tables
        if request_id is not None:
            self.request_id = request_id
        if page_info is not None:
            self.page_info = page_info

    @property
    def route_tables(self):
        """Gets the route_tables of this ListRouteTablesResponse.

        路由表列表

        :return: The route_tables of this ListRouteTablesResponse.
        :rtype: list[:class:`huaweicloudsdker.v3.RouteTable`]
        """
        return self._route_tables

    @route_tables.setter
    def route_tables(self, route_tables):
        """Sets the route_tables of this ListRouteTablesResponse.

        路由表列表

        :param route_tables: The route_tables of this ListRouteTablesResponse.
        :type route_tables: list[:class:`huaweicloudsdker.v3.RouteTable`]
        """
        self._route_tables = route_tables

    @property
    def request_id(self):
        """Gets the request_id of this ListRouteTablesResponse.

        请求ID

        :return: The request_id of this ListRouteTablesResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ListRouteTablesResponse.

        请求ID

        :param request_id: The request_id of this ListRouteTablesResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def page_info(self):
        """Gets the page_info of this ListRouteTablesResponse.


        :return: The page_info of this ListRouteTablesResponse.
        :rtype: :class:`huaweicloudsdker.v3.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        """Sets the page_info of this ListRouteTablesResponse.


        :param page_info: The page_info of this ListRouteTablesResponse.
        :type page_info: :class:`huaweicloudsdker.v3.PageInfo`
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
        if not isinstance(other, ListRouteTablesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
