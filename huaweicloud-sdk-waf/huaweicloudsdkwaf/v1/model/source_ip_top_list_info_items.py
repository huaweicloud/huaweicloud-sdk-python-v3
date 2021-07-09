# coding: utf-8

import re
import six





class SourceIpTopListInfoItems:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'ip': 'str',
        'num': 'int'
    }

    attribute_map = {
        'ip': 'ip',
        'num': 'num'
    }

    def __init__(self, ip=None, num=None):
        """SourceIpTopListInfoItems - a model defined in huaweicloud sdk"""
        
        

        self._ip = None
        self._num = None
        self.discriminator = None

        if ip is not None:
            self.ip = ip
        if num is not None:
            self.num = num

    @property
    def ip(self):
        """Gets the ip of this SourceIpTopListInfoItems.

        攻击源ip地址

        :return: The ip of this SourceIpTopListInfoItems.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this SourceIpTopListInfoItems.

        攻击源ip地址

        :param ip: The ip of this SourceIpTopListInfoItems.
        :type: str
        """
        self._ip = ip

    @property
    def num(self):
        """Gets the num of this SourceIpTopListInfoItems.

        攻击源ip攻击次数

        :return: The num of this SourceIpTopListInfoItems.
        :rtype: int
        """
        return self._num

    @num.setter
    def num(self, num):
        """Sets the num of this SourceIpTopListInfoItems.

        攻击源ip攻击次数

        :param num: The num of this SourceIpTopListInfoItems.
        :type: int
        """
        self._num = num

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
        import simplejson as json
        return json.dumps(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SourceIpTopListInfoItems):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
