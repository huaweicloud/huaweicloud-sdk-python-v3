# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CoveredIPVO:

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
        'covered_ip': 'str'
    }

    attribute_map = {
        'ip': 'ip',
        'covered_ip': 'covered_Ip'
    }

    def __init__(self, ip=None, covered_ip=None):
        """CoveredIPVO

        The model defined in huaweicloud sdk

        :param ip: ip地址
        :type ip: str
        :param covered_ip: 覆盖ip地址。
        :type covered_ip: str
        """
        
        

        self._ip = None
        self._covered_ip = None
        self.discriminator = None

        if ip is not None:
            self.ip = ip
        if covered_ip is not None:
            self.covered_ip = covered_ip

    @property
    def ip(self):
        """Gets the ip of this CoveredIPVO.

        ip地址

        :return: The ip of this CoveredIPVO.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this CoveredIPVO.

        ip地址

        :param ip: The ip of this CoveredIPVO.
        :type ip: str
        """
        self._ip = ip

    @property
    def covered_ip(self):
        """Gets the covered_ip of this CoveredIPVO.

        覆盖ip地址。

        :return: The covered_ip of this CoveredIPVO.
        :rtype: str
        """
        return self._covered_ip

    @covered_ip.setter
    def covered_ip(self, covered_ip):
        """Sets the covered_ip of this CoveredIPVO.

        覆盖ip地址。

        :param covered_ip: The covered_ip of this CoveredIPVO.
        :type covered_ip: str
        """
        self._covered_ip = covered_ip

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
        if not isinstance(other, CoveredIPVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
