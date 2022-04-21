# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WeeklyTop10:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'floating_ip_address': 'str',
        'times': 'int'
    }

    attribute_map = {
        'floating_ip_address': 'floating_ip_address',
        'times': 'times'
    }

    def __init__(self, floating_ip_address=None, times=None):
        """WeeklyTop10

        The model defined in huaweicloud sdk

        :param floating_ip_address: 弹性IP地址
        :type floating_ip_address: str
        :param times: DDoS拦截次数，包括清洗和黑洞
        :type times: int
        """
        
        

        self._floating_ip_address = None
        self._times = None
        self.discriminator = None

        self.floating_ip_address = floating_ip_address
        self.times = times

    @property
    def floating_ip_address(self):
        """Gets the floating_ip_address of this WeeklyTop10.

        弹性IP地址

        :return: The floating_ip_address of this WeeklyTop10.
        :rtype: str
        """
        return self._floating_ip_address

    @floating_ip_address.setter
    def floating_ip_address(self, floating_ip_address):
        """Sets the floating_ip_address of this WeeklyTop10.

        弹性IP地址

        :param floating_ip_address: The floating_ip_address of this WeeklyTop10.
        :type floating_ip_address: str
        """
        self._floating_ip_address = floating_ip_address

    @property
    def times(self):
        """Gets the times of this WeeklyTop10.

        DDoS拦截次数，包括清洗和黑洞

        :return: The times of this WeeklyTop10.
        :rtype: int
        """
        return self._times

    @times.setter
    def times(self, times):
        """Sets the times of this WeeklyTop10.

        DDoS拦截次数，包括清洗和黑洞

        :param times: The times of this WeeklyTop10.
        :type times: int
        """
        self._times = times

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
        if not isinstance(other, WeeklyTop10):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
