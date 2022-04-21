# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchDeleteIpListOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'ip_list': 'list[IpGroupIp]'
    }

    attribute_map = {
        'ip_list': 'ip_list'
    }

    def __init__(self, ip_list=None):
        """BatchDeleteIpListOption

        The model defined in huaweicloud sdk

        :param ip_list: IP列表。
        :type ip_list: list[:class:`huaweicloudsdkelb.v3.IpGroupIp`]
        """
        
        

        self._ip_list = None
        self.discriminator = None

        if ip_list is not None:
            self.ip_list = ip_list

    @property
    def ip_list(self):
        """Gets the ip_list of this BatchDeleteIpListOption.

        IP列表。

        :return: The ip_list of this BatchDeleteIpListOption.
        :rtype: list[:class:`huaweicloudsdkelb.v3.IpGroupIp`]
        """
        return self._ip_list

    @ip_list.setter
    def ip_list(self, ip_list):
        """Sets the ip_list of this BatchDeleteIpListOption.

        IP列表。

        :param ip_list: The ip_list of this BatchDeleteIpListOption.
        :type ip_list: list[:class:`huaweicloudsdkelb.v3.IpGroupIp`]
        """
        self._ip_list = ip_list

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
        if not isinstance(other, BatchDeleteIpListOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
