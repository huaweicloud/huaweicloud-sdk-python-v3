# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NsRecords:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'hostname': 'str',
        'address': 'str',
        'priority': 'int'
    }

    attribute_map = {
        'hostname': 'hostname',
        'address': 'address',
        'priority': 'priority'
    }

    def __init__(self, hostname=None, address=None, priority=None):
        """NsRecords

        The model defined in huaweicloud sdk

        :param hostname: 主机名。  当为内网名称服务器时，此值为空。
        :type hostname: str
        :param address: 名称服务器地址。  当为公网名称服务器时，此值为空。
        :type address: str
        :param priority: 优先级。  示例：  如果priority的值为“1”，表示会第一个采用该域名服务器进行解析。
        :type priority: int
        """
        
        

        self._hostname = None
        self._address = None
        self._priority = None
        self.discriminator = None

        if hostname is not None:
            self.hostname = hostname
        if address is not None:
            self.address = address
        if priority is not None:
            self.priority = priority

    @property
    def hostname(self):
        """Gets the hostname of this NsRecords.

        主机名。  当为内网名称服务器时，此值为空。

        :return: The hostname of this NsRecords.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this NsRecords.

        主机名。  当为内网名称服务器时，此值为空。

        :param hostname: The hostname of this NsRecords.
        :type hostname: str
        """
        self._hostname = hostname

    @property
    def address(self):
        """Gets the address of this NsRecords.

        名称服务器地址。  当为公网名称服务器时，此值为空。

        :return: The address of this NsRecords.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this NsRecords.

        名称服务器地址。  当为公网名称服务器时，此值为空。

        :param address: The address of this NsRecords.
        :type address: str
        """
        self._address = address

    @property
    def priority(self):
        """Gets the priority of this NsRecords.

        优先级。  示例：  如果priority的值为“1”，表示会第一个采用该域名服务器进行解析。

        :return: The priority of this NsRecords.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this NsRecords.

        优先级。  示例：  如果priority的值为“1”，表示会第一个采用该域名服务器进行解析。

        :param priority: The priority of this NsRecords.
        :type priority: int
        """
        self._priority = priority

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
        if not isinstance(other, NsRecords):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
