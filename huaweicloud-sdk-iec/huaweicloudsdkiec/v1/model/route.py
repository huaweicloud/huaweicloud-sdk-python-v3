# coding: utf-8

import re
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
        'type': 'str',
        'destination': 'str',
        'nexthop': 'str',
        'description': 'str'
    }

    attribute_map = {
        'type': 'type',
        'destination': 'destination',
        'nexthop': 'nexthop',
        'description': 'description'
    }

    def __init__(self, type=None, destination=None, nexthop=None, description=None):
        """Route

        The model defined in huaweicloud sdk

        :param type: 路由的类型  取值范围：     1）ecs：弹性云服务器     2）vip：虚拟IP     3）local：系统路由，不可修改和删除
        :type type: str
        :param destination: 路由的目的网段  约束：合法的CIDR格式
        :type destination: str
        :param nexthop: 路由下一跳对象的ID  取值范围：     1）当type为ecs时，传入ecs实例ID；     2）当type为vip时，取值为vip对应的IP地址；
        :type nexthop: str
        :param description: 路由的描述信息  取值范围：0-255个字符，不能包含“&lt;”和“&gt;”
        :type description: str
        """
        
        

        self._type = None
        self._destination = None
        self._nexthop = None
        self._description = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if destination is not None:
            self.destination = destination
        if nexthop is not None:
            self.nexthop = nexthop
        if description is not None:
            self.description = description

    @property
    def type(self):
        """Gets the type of this Route.

        路由的类型  取值范围：     1）ecs：弹性云服务器     2）vip：虚拟IP     3）local：系统路由，不可修改和删除

        :return: The type of this Route.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Route.

        路由的类型  取值范围：     1）ecs：弹性云服务器     2）vip：虚拟IP     3）local：系统路由，不可修改和删除

        :param type: The type of this Route.
        :type type: str
        """
        self._type = type

    @property
    def destination(self):
        """Gets the destination of this Route.

        路由的目的网段  约束：合法的CIDR格式

        :return: The destination of this Route.
        :rtype: str
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """Sets the destination of this Route.

        路由的目的网段  约束：合法的CIDR格式

        :param destination: The destination of this Route.
        :type destination: str
        """
        self._destination = destination

    @property
    def nexthop(self):
        """Gets the nexthop of this Route.

        路由下一跳对象的ID  取值范围：     1）当type为ecs时，传入ecs实例ID；     2）当type为vip时，取值为vip对应的IP地址；

        :return: The nexthop of this Route.
        :rtype: str
        """
        return self._nexthop

    @nexthop.setter
    def nexthop(self, nexthop):
        """Sets the nexthop of this Route.

        路由下一跳对象的ID  取值范围：     1）当type为ecs时，传入ecs实例ID；     2）当type为vip时，取值为vip对应的IP地址；

        :param nexthop: The nexthop of this Route.
        :type nexthop: str
        """
        self._nexthop = nexthop

    @property
    def description(self):
        """Gets the description of this Route.

        路由的描述信息  取值范围：0-255个字符，不能包含“<”和“>”

        :return: The description of this Route.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Route.

        路由的描述信息  取值范围：0-255个字符，不能包含“<”和“>”

        :param description: The description of this Route.
        :type description: str
        """
        self._description = description

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
