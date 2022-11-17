# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateVpcRouteOption:

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
        'nexthop': 'str',
        'type': 'str',
        'vpc_id': 'str'
    }

    attribute_map = {
        'destination': 'destination',
        'nexthop': 'nexthop',
        'type': 'type',
        'vpc_id': 'vpc_id'
    }

    def __init__(self, destination=None, nexthop=None, type=None, vpc_id=None):
        """CreateVpcRouteOption

        The model defined in huaweicloud sdk

        :param destination: 路由目的地址CIDR，如192.168.200.0/24。
        :type destination: str
        :param nexthop: 功能说明：路由下一跳  取值范围：如果type为peering类型，则nexthop为peering的ID
        :type nexthop: str
        :param type: 功能说明：路由类型  取值范围：peering
        :type type: str
        :param vpc_id: 请求添加路由的VPC ID
        :type vpc_id: str
        """
        
        

        self._destination = None
        self._nexthop = None
        self._type = None
        self._vpc_id = None
        self.discriminator = None

        self.destination = destination
        self.nexthop = nexthop
        self.type = type
        self.vpc_id = vpc_id

    @property
    def destination(self):
        """Gets the destination of this CreateVpcRouteOption.

        路由目的地址CIDR，如192.168.200.0/24。

        :return: The destination of this CreateVpcRouteOption.
        :rtype: str
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """Sets the destination of this CreateVpcRouteOption.

        路由目的地址CIDR，如192.168.200.0/24。

        :param destination: The destination of this CreateVpcRouteOption.
        :type destination: str
        """
        self._destination = destination

    @property
    def nexthop(self):
        """Gets the nexthop of this CreateVpcRouteOption.

        功能说明：路由下一跳  取值范围：如果type为peering类型，则nexthop为peering的ID

        :return: The nexthop of this CreateVpcRouteOption.
        :rtype: str
        """
        return self._nexthop

    @nexthop.setter
    def nexthop(self, nexthop):
        """Sets the nexthop of this CreateVpcRouteOption.

        功能说明：路由下一跳  取值范围：如果type为peering类型，则nexthop为peering的ID

        :param nexthop: The nexthop of this CreateVpcRouteOption.
        :type nexthop: str
        """
        self._nexthop = nexthop

    @property
    def type(self):
        """Gets the type of this CreateVpcRouteOption.

        功能说明：路由类型  取值范围：peering

        :return: The type of this CreateVpcRouteOption.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreateVpcRouteOption.

        功能说明：路由类型  取值范围：peering

        :param type: The type of this CreateVpcRouteOption.
        :type type: str
        """
        self._type = type

    @property
    def vpc_id(self):
        """Gets the vpc_id of this CreateVpcRouteOption.

        请求添加路由的VPC ID

        :return: The vpc_id of this CreateVpcRouteOption.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this CreateVpcRouteOption.

        请求添加路由的VPC ID

        :param vpc_id: The vpc_id of this CreateVpcRouteOption.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

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
        if not isinstance(other, CreateVpcRouteOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
