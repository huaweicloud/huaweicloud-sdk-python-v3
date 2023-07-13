# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Route:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'destination': 'str',
        'nexthop': 'str'
    }

    attribute_map = {
        'destination': 'destination',
        'nexthop': 'nexthop'
    }

    def __init__(self, destination=None, nexthop=None):
        """Route

        The model defined in huaweicloud sdk

        :param destination: 功能说明：路由目的地 取值范围：IP地址段 约束：仅支持配置默认路由，且其取值只能是0.0.0.0/0
        :type destination: str
        :param nexthop: 功能说明：路由下一跳IP地址 取值范围：ipv4地址格式 约束：nexthop仅支持所关联的子网范围内IP地址
        :type nexthop: str
        """
        
        

        self._destination = None
        self._nexthop = None
        self.discriminator = None

        if destination is not None:
            self.destination = destination
        if nexthop is not None:
            self.nexthop = nexthop

    @property
    def destination(self):
        """Gets the destination of this Route.

        功能说明：路由目的地 取值范围：IP地址段 约束：仅支持配置默认路由，且其取值只能是0.0.0.0/0

        :return: The destination of this Route.
        :rtype: str
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """Sets the destination of this Route.

        功能说明：路由目的地 取值范围：IP地址段 约束：仅支持配置默认路由，且其取值只能是0.0.0.0/0

        :param destination: The destination of this Route.
        :type destination: str
        """
        self._destination = destination

    @property
    def nexthop(self):
        """Gets the nexthop of this Route.

        功能说明：路由下一跳IP地址 取值范围：ipv4地址格式 约束：nexthop仅支持所关联的子网范围内IP地址

        :return: The nexthop of this Route.
        :rtype: str
        """
        return self._nexthop

    @nexthop.setter
    def nexthop(self, nexthop):
        """Sets the nexthop of this Route.

        功能说明：路由下一跳IP地址 取值范围：ipv4地址格式 约束：nexthop仅支持所关联的子网范围内IP地址

        :param nexthop: The nexthop of this Route.
        :type nexthop: str
        """
        self._nexthop = nexthop

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
        if not isinstance(other, Route):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
