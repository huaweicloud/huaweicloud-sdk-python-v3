# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AccelerateIp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ip_type': 'str',
        'ip_address': 'str',
        'area': 'Area'
    }

    attribute_map = {
        'ip_type': 'ip_type',
        'ip_address': 'ip_address',
        'area': 'area'
    }

    def __init__(self, ip_type=None, ip_address=None, area=None):
        """AccelerateIp

        The model defined in huaweicloud sdk

        :param ip_type: IP地址类型。
        :type ip_type: str
        :param ip_address: IP地址。
        :type ip_address: str
        :param area: 
        :type area: :class:`huaweicloudsdkga.v1.Area`
        """
        
        

        self._ip_type = None
        self._ip_address = None
        self._area = None
        self.discriminator = None

        self.ip_type = ip_type
        if ip_address is not None:
            self.ip_address = ip_address
        if area is not None:
            self.area = area

    @property
    def ip_type(self):
        """Gets the ip_type of this AccelerateIp.

        IP地址类型。

        :return: The ip_type of this AccelerateIp.
        :rtype: str
        """
        return self._ip_type

    @ip_type.setter
    def ip_type(self, ip_type):
        """Sets the ip_type of this AccelerateIp.

        IP地址类型。

        :param ip_type: The ip_type of this AccelerateIp.
        :type ip_type: str
        """
        self._ip_type = ip_type

    @property
    def ip_address(self):
        """Gets the ip_address of this AccelerateIp.

        IP地址。

        :return: The ip_address of this AccelerateIp.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this AccelerateIp.

        IP地址。

        :param ip_address: The ip_address of this AccelerateIp.
        :type ip_address: str
        """
        self._ip_address = ip_address

    @property
    def area(self):
        """Gets the area of this AccelerateIp.

        :return: The area of this AccelerateIp.
        :rtype: :class:`huaweicloudsdkga.v1.Area`
        """
        return self._area

    @area.setter
    def area(self, area):
        """Sets the area of this AccelerateIp.

        :param area: The area of this AccelerateIp.
        :type area: :class:`huaweicloudsdkga.v1.Area`
        """
        self._area = area

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
        if not isinstance(other, AccelerateIp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
