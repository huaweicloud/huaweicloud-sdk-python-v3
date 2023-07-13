# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RemoveIpGroupIpRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ip_list': 'list[str]'
    }

    attribute_map = {
        'ip_list': 'ip_list'
    }

    def __init__(self, ip_list=None):
        """RemoveIpGroupIpRequestBody

        The model defined in huaweicloud sdk

        :param ip_list: IP地址组中的IP网段列表，一次最多支持删除20个条目。
        :type ip_list: list[str]
        """
        
        

        self._ip_list = None
        self.discriminator = None

        self.ip_list = ip_list

    @property
    def ip_list(self):
        """Gets the ip_list of this RemoveIpGroupIpRequestBody.

        IP地址组中的IP网段列表，一次最多支持删除20个条目。

        :return: The ip_list of this RemoveIpGroupIpRequestBody.
        :rtype: list[str]
        """
        return self._ip_list

    @ip_list.setter
    def ip_list(self, ip_list):
        """Sets the ip_list of this RemoveIpGroupIpRequestBody.

        IP地址组中的IP网段列表，一次最多支持删除20个条目。

        :param ip_list: The ip_list of this RemoveIpGroupIpRequestBody.
        :type ip_list: list[str]
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
        if not isinstance(other, RemoveIpGroupIpRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
