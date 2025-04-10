# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowEquipmentStaticRouteInfoResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'static_routes': 'list[StaticRouteItem]'
    }

    attribute_map = {
        'static_routes': 'static_routes'
    }

    def __init__(self, static_routes=None):
        r"""ShowEquipmentStaticRouteInfoResponse

        The model defined in huaweicloud sdk

        :param static_routes: 设备静态路由配置列表
        :type static_routes: list[:class:`huaweicloudsdkec.v1.StaticRouteItem`]
        """
        
        super(ShowEquipmentStaticRouteInfoResponse, self).__init__()

        self._static_routes = None
        self.discriminator = None

        if static_routes is not None:
            self.static_routes = static_routes

    @property
    def static_routes(self):
        r"""Gets the static_routes of this ShowEquipmentStaticRouteInfoResponse.

        设备静态路由配置列表

        :return: The static_routes of this ShowEquipmentStaticRouteInfoResponse.
        :rtype: list[:class:`huaweicloudsdkec.v1.StaticRouteItem`]
        """
        return self._static_routes

    @static_routes.setter
    def static_routes(self, static_routes):
        r"""Sets the static_routes of this ShowEquipmentStaticRouteInfoResponse.

        设备静态路由配置列表

        :param static_routes: The static_routes of this ShowEquipmentStaticRouteInfoResponse.
        :type static_routes: list[:class:`huaweicloudsdkec.v1.StaticRouteItem`]
        """
        self._static_routes = static_routes

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
        if not isinstance(other, ShowEquipmentStaticRouteInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
