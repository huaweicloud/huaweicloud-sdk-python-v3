# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EffectiveRoute:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'route_id': 'str',
        'destination': 'str',
        'next_hops': 'list[RouteAttachment]',
        'is_blackhole': 'bool',
        'route_type': 'str'
    }

    attribute_map = {
        'route_id': 'route_id',
        'destination': 'destination',
        'next_hops': 'next_hops',
        'is_blackhole': 'is_blackhole',
        'route_type': 'route_type'
    }

    def __init__(self, route_id=None, destination=None, next_hops=None, is_blackhole=None, route_type=None):
        """EffectiveRoute

        The model defined in huaweicloud sdk

        :param route_id: 路由ID
        :type route_id: str
        :param destination: 路由目的地
        :type destination: str
        :param next_hops: 路由下一跳列表
        :type next_hops: list[:class:`huaweicloudsdker.v3.RouteAttachment`]
        :param is_blackhole: 是否黑洞路由
        :type is_blackhole: bool
        :param route_type: 路由类型
        :type route_type: str
        """
        
        

        self._route_id = None
        self._destination = None
        self._next_hops = None
        self._is_blackhole = None
        self._route_type = None
        self.discriminator = None

        if route_id is not None:
            self.route_id = route_id
        if destination is not None:
            self.destination = destination
        if next_hops is not None:
            self.next_hops = next_hops
        if is_blackhole is not None:
            self.is_blackhole = is_blackhole
        if route_type is not None:
            self.route_type = route_type

    @property
    def route_id(self):
        """Gets the route_id of this EffectiveRoute.

        路由ID

        :return: The route_id of this EffectiveRoute.
        :rtype: str
        """
        return self._route_id

    @route_id.setter
    def route_id(self, route_id):
        """Sets the route_id of this EffectiveRoute.

        路由ID

        :param route_id: The route_id of this EffectiveRoute.
        :type route_id: str
        """
        self._route_id = route_id

    @property
    def destination(self):
        """Gets the destination of this EffectiveRoute.

        路由目的地

        :return: The destination of this EffectiveRoute.
        :rtype: str
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """Sets the destination of this EffectiveRoute.

        路由目的地

        :param destination: The destination of this EffectiveRoute.
        :type destination: str
        """
        self._destination = destination

    @property
    def next_hops(self):
        """Gets the next_hops of this EffectiveRoute.

        路由下一跳列表

        :return: The next_hops of this EffectiveRoute.
        :rtype: list[:class:`huaweicloudsdker.v3.RouteAttachment`]
        """
        return self._next_hops

    @next_hops.setter
    def next_hops(self, next_hops):
        """Sets the next_hops of this EffectiveRoute.

        路由下一跳列表

        :param next_hops: The next_hops of this EffectiveRoute.
        :type next_hops: list[:class:`huaweicloudsdker.v3.RouteAttachment`]
        """
        self._next_hops = next_hops

    @property
    def is_blackhole(self):
        """Gets the is_blackhole of this EffectiveRoute.

        是否黑洞路由

        :return: The is_blackhole of this EffectiveRoute.
        :rtype: bool
        """
        return self._is_blackhole

    @is_blackhole.setter
    def is_blackhole(self, is_blackhole):
        """Sets the is_blackhole of this EffectiveRoute.

        是否黑洞路由

        :param is_blackhole: The is_blackhole of this EffectiveRoute.
        :type is_blackhole: bool
        """
        self._is_blackhole = is_blackhole

    @property
    def route_type(self):
        """Gets the route_type of this EffectiveRoute.

        路由类型

        :return: The route_type of this EffectiveRoute.
        :rtype: str
        """
        return self._route_type

    @route_type.setter
    def route_type(self, route_type):
        """Sets the route_type of this EffectiveRoute.

        路由类型

        :param route_type: The route_type of this EffectiveRoute.
        :type route_type: str
        """
        self._route_type = route_type

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
        if not isinstance(other, EffectiveRoute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
