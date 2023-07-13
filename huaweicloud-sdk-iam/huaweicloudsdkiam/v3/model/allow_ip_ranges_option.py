# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AllowIpRangesOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'description': 'str',
        'ip_range': 'str'
    }

    attribute_map = {
        'description': 'description',
        'ip_range': 'ip_range'
    }

    def __init__(self, description=None, ip_range=None):
        """AllowIpRangesOption

        The model defined in huaweicloud sdk

        :param description: 描述信息。
        :type description: str
        :param ip_range: IP地址区间,例如:0.0.0.0-255.255.255.255。
        :type ip_range: str
        """
        
        

        self._description = None
        self._ip_range = None
        self.discriminator = None

        if description is not None:
            self.description = description
        self.ip_range = ip_range

    @property
    def description(self):
        """Gets the description of this AllowIpRangesOption.

        描述信息。

        :return: The description of this AllowIpRangesOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AllowIpRangesOption.

        描述信息。

        :param description: The description of this AllowIpRangesOption.
        :type description: str
        """
        self._description = description

    @property
    def ip_range(self):
        """Gets the ip_range of this AllowIpRangesOption.

        IP地址区间,例如:0.0.0.0-255.255.255.255。

        :return: The ip_range of this AllowIpRangesOption.
        :rtype: str
        """
        return self._ip_range

    @ip_range.setter
    def ip_range(self, ip_range):
        """Sets the ip_range of this AllowIpRangesOption.

        IP地址区间,例如:0.0.0.0-255.255.255.255。

        :param ip_range: The ip_range of this AllowIpRangesOption.
        :type ip_range: str
        """
        self._ip_range = ip_range

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
        if not isinstance(other, AllowIpRangesOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
