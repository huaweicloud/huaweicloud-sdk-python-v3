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
        'gdgw_routetable': 'list[ShowGdgwRoutetable]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'request_id': 'request_id',
        'gdgw_routetable': 'gdgw_routetable',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, request_id=None, gdgw_routetable=None, x_request_id=None):
        """ListGdgwRouteTablesResponse

        The model defined in huaweicloud sdk

        :param request_id: 请求ID
        :type request_id: str
        :param gdgw_routetable: 路由表详细对象
        :type gdgw_routetable: list[:class:`huaweicloudsdkdc.v3.ShowGdgwRoutetable`]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ListGdgwRouteTablesResponse, self).__init__()

        self._request_id = None
        self._gdgw_routetable = None
        self._x_request_id = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if gdgw_routetable is not None:
            self.gdgw_routetable = gdgw_routetable
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def request_id(self):
        """Gets the request_id of this ListGdgwRouteTablesResponse.

        请求ID

        :return: The request_id of this ListGdgwRouteTablesResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ListGdgwRouteTablesResponse.

        请求ID

        :param request_id: The request_id of this ListGdgwRouteTablesResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def gdgw_routetable(self):
        """Gets the gdgw_routetable of this ListGdgwRouteTablesResponse.

        路由表详细对象

        :return: The gdgw_routetable of this ListGdgwRouteTablesResponse.
        :rtype: list[:class:`huaweicloudsdkdc.v3.ShowGdgwRoutetable`]
        """
        return self._gdgw_routetable

    @gdgw_routetable.setter
    def gdgw_routetable(self, gdgw_routetable):
        """Sets the gdgw_routetable of this ListGdgwRouteTablesResponse.

        路由表详细对象

        :param gdgw_routetable: The gdgw_routetable of this ListGdgwRouteTablesResponse.
        :type gdgw_routetable: list[:class:`huaweicloudsdkdc.v3.ShowGdgwRoutetable`]
        """
        self._gdgw_routetable = gdgw_routetable

    @property
    def x_request_id(self):
        """Gets the x_request_id of this ListGdgwRouteTablesResponse.

        :return: The x_request_id of this ListGdgwRouteTablesResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this ListGdgwRouteTablesResponse.

        :param x_request_id: The x_request_id of this ListGdgwRouteTablesResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
