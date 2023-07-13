# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpadateIpGroupIpOption:

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
        'description': 'str'
    }

    attribute_map = {
        'ip': 'ip',
        'description': 'description'
    }

    def __init__(self, ip=None, description=None):
        """UpadateIpGroupIpOption

        The model defined in huaweicloud sdk

        :param ip: IP地址。支持IPv4、IPv6。  [不支持IPv6，请勿设置为IPv6地址。](tag:dt,dt_test)
        :type ip: str
        :param description: 备注信息。
        :type description: str
        """
        
        

        self._ip = None
        self._description = None
        self.discriminator = None

        self.ip = ip
        if description is not None:
            self.description = description

    @property
    def ip(self):
        """Gets the ip of this UpadateIpGroupIpOption.

        IP地址。支持IPv4、IPv6。  [不支持IPv6，请勿设置为IPv6地址。](tag:dt,dt_test)

        :return: The ip of this UpadateIpGroupIpOption.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this UpadateIpGroupIpOption.

        IP地址。支持IPv4、IPv6。  [不支持IPv6，请勿设置为IPv6地址。](tag:dt,dt_test)

        :param ip: The ip of this UpadateIpGroupIpOption.
        :type ip: str
        """
        self._ip = ip

    @property
    def description(self):
        """Gets the description of this UpadateIpGroupIpOption.

        备注信息。

        :return: The description of this UpadateIpGroupIpOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpadateIpGroupIpOption.

        备注信息。

        :param description: The description of this UpadateIpGroupIpOption.
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
        if not isinstance(other, UpadateIpGroupIpOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
