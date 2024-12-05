# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateGdgwRoutetableRequestBodyGdgwRoutetableDelRoutes:

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
        'type': 'str'
    }

    attribute_map = {
        'destination': 'destination',
        'nexthop': 'nexthop',
        'type': 'type'
    }

    def __init__(self, destination=None, nexthop=None, type=None):
        """UpdateGdgwRoutetableRequestBodyGdgwRoutetableDelRoutes

        The model defined in huaweicloud sdk

        :param destination: 目的地址
        :type destination: str
        :param nexthop: 下一跳
        :type nexthop: str
        :param type: 类型
        :type type: str
        """
        
        

        self._destination = None
        self._nexthop = None
        self._type = None
        self.discriminator = None

        self.destination = destination
        self.nexthop = nexthop
        self.type = type

    @property
    def destination(self):
        """Gets the destination of this UpdateGdgwRoutetableRequestBodyGdgwRoutetableDelRoutes.

        目的地址

        :return: The destination of this UpdateGdgwRoutetableRequestBodyGdgwRoutetableDelRoutes.
        :rtype: str
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """Sets the destination of this UpdateGdgwRoutetableRequestBodyGdgwRoutetableDelRoutes.

        目的地址

        :param destination: The destination of this UpdateGdgwRoutetableRequestBodyGdgwRoutetableDelRoutes.
        :type destination: str
        """
        self._destination = destination

    @property
    def nexthop(self):
        """Gets the nexthop of this UpdateGdgwRoutetableRequestBodyGdgwRoutetableDelRoutes.

        下一跳

        :return: The nexthop of this UpdateGdgwRoutetableRequestBodyGdgwRoutetableDelRoutes.
        :rtype: str
        """
        return self._nexthop

    @nexthop.setter
    def nexthop(self, nexthop):
        """Sets the nexthop of this UpdateGdgwRoutetableRequestBodyGdgwRoutetableDelRoutes.

        下一跳

        :param nexthop: The nexthop of this UpdateGdgwRoutetableRequestBodyGdgwRoutetableDelRoutes.
        :type nexthop: str
        """
        self._nexthop = nexthop

    @property
    def type(self):
        """Gets the type of this UpdateGdgwRoutetableRequestBodyGdgwRoutetableDelRoutes.

        类型

        :return: The type of this UpdateGdgwRoutetableRequestBodyGdgwRoutetableDelRoutes.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this UpdateGdgwRoutetableRequestBodyGdgwRoutetableDelRoutes.

        类型

        :param type: The type of this UpdateGdgwRoutetableRequestBodyGdgwRoutetableDelRoutes.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, UpdateGdgwRoutetableRequestBodyGdgwRoutetableDelRoutes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
