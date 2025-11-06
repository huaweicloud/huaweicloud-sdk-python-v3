# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRoutesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'route_resps': 'list[RouteRespsResource]',
        'total_size': 'int'
    }

    attribute_map = {
        'route_resps': 'routeResps',
        'total_size': 'totalSize'
    }

    def __init__(self, route_resps=None, total_size=None):
        r"""ListRoutesResponse

        The model defined in huaweicloud sdk

        :param route_resps: 路由IP。
        :type route_resps: list[:class:`huaweicloudsdkcss.v1.RouteRespsResource`]
        :param total_size: 路由总数。
        :type total_size: int
        """
        
        super().__init__()

        self._route_resps = None
        self._total_size = None
        self.discriminator = None

        if route_resps is not None:
            self.route_resps = route_resps
        if total_size is not None:
            self.total_size = total_size

    @property
    def route_resps(self):
        r"""Gets the route_resps of this ListRoutesResponse.

        路由IP。

        :return: The route_resps of this ListRoutesResponse.
        :rtype: list[:class:`huaweicloudsdkcss.v1.RouteRespsResource`]
        """
        return self._route_resps

    @route_resps.setter
    def route_resps(self, route_resps):
        r"""Sets the route_resps of this ListRoutesResponse.

        路由IP。

        :param route_resps: The route_resps of this ListRoutesResponse.
        :type route_resps: list[:class:`huaweicloudsdkcss.v1.RouteRespsResource`]
        """
        self._route_resps = route_resps

    @property
    def total_size(self):
        r"""Gets the total_size of this ListRoutesResponse.

        路由总数。

        :return: The total_size of this ListRoutesResponse.
        :rtype: int
        """
        return self._total_size

    @total_size.setter
    def total_size(self, total_size):
        r"""Sets the total_size of this ListRoutesResponse.

        路由总数。

        :param total_size: The total_size of this ListRoutesResponse.
        :type total_size: int
        """
        self._total_size = total_size

    def to_dict(self):
        import warnings
        warnings.warn("ListRoutesResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListRoutesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
