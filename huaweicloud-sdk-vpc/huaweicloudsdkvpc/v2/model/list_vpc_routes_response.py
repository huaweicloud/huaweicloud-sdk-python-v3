# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListVpcRoutesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'routes': 'list[VpcRoute]',
        'routes_links': 'list[NeutronPageLink]'
    }

    attribute_map = {
        'routes': 'routes',
        'routes_links': 'routes_links'
    }

    def __init__(self, routes=None, routes_links=None):
        """ListVpcRoutesResponse

        The model defined in huaweicloud sdk

        :param routes: route对象列表
        :type routes: list[:class:`huaweicloudsdkvpc.v2.VpcRoute`]
        :param routes_links: 分页信息
        :type routes_links: list[:class:`huaweicloudsdkvpc.v2.NeutronPageLink`]
        """
        
        super(ListVpcRoutesResponse, self).__init__()

        self._routes = None
        self._routes_links = None
        self.discriminator = None

        if routes is not None:
            self.routes = routes
        if routes_links is not None:
            self.routes_links = routes_links

    @property
    def routes(self):
        """Gets the routes of this ListVpcRoutesResponse.

        route对象列表

        :return: The routes of this ListVpcRoutesResponse.
        :rtype: list[:class:`huaweicloudsdkvpc.v2.VpcRoute`]
        """
        return self._routes

    @routes.setter
    def routes(self, routes):
        """Sets the routes of this ListVpcRoutesResponse.

        route对象列表

        :param routes: The routes of this ListVpcRoutesResponse.
        :type routes: list[:class:`huaweicloudsdkvpc.v2.VpcRoute`]
        """
        self._routes = routes

    @property
    def routes_links(self):
        """Gets the routes_links of this ListVpcRoutesResponse.

        分页信息

        :return: The routes_links of this ListVpcRoutesResponse.
        :rtype: list[:class:`huaweicloudsdkvpc.v2.NeutronPageLink`]
        """
        return self._routes_links

    @routes_links.setter
    def routes_links(self, routes_links):
        """Sets the routes_links of this ListVpcRoutesResponse.

        分页信息

        :param routes_links: The routes_links of this ListVpcRoutesResponse.
        :type routes_links: list[:class:`huaweicloudsdkvpc.v2.NeutronPageLink`]
        """
        self._routes_links = routes_links

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
        if not isinstance(other, ListVpcRoutesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
