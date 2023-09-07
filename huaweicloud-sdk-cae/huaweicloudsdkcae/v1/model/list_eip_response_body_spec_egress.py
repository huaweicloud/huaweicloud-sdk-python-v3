# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEipResponseBodySpecEgress:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'bandwidth_size': 'int',
        'ip_list': 'list[str]'
    }

    attribute_map = {
        'bandwidth_size': 'bandwidth_size',
        'ip_list': 'ip_list'
    }

    def __init__(self, bandwidth_size=None, ip_list=None):
        """ListEipResponseBodySpecEgress

        The model defined in huaweicloud sdk

        :param bandwidth_size: 出网IP带宽。
        :type bandwidth_size: int
        :param ip_list: 出网IP列表。
        :type ip_list: list[str]
        """
        
        

        self._bandwidth_size = None
        self._ip_list = None
        self.discriminator = None

        if bandwidth_size is not None:
            self.bandwidth_size = bandwidth_size
        if ip_list is not None:
            self.ip_list = ip_list

    @property
    def bandwidth_size(self):
        """Gets the bandwidth_size of this ListEipResponseBodySpecEgress.

        出网IP带宽。

        :return: The bandwidth_size of this ListEipResponseBodySpecEgress.
        :rtype: int
        """
        return self._bandwidth_size

    @bandwidth_size.setter
    def bandwidth_size(self, bandwidth_size):
        """Sets the bandwidth_size of this ListEipResponseBodySpecEgress.

        出网IP带宽。

        :param bandwidth_size: The bandwidth_size of this ListEipResponseBodySpecEgress.
        :type bandwidth_size: int
        """
        self._bandwidth_size = bandwidth_size

    @property
    def ip_list(self):
        """Gets the ip_list of this ListEipResponseBodySpecEgress.

        出网IP列表。

        :return: The ip_list of this ListEipResponseBodySpecEgress.
        :rtype: list[str]
        """
        return self._ip_list

    @ip_list.setter
    def ip_list(self, ip_list):
        """Sets the ip_list of this ListEipResponseBodySpecEgress.

        出网IP列表。

        :param ip_list: The ip_list of this ListEipResponseBodySpecEgress.
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
        if not isinstance(other, ListEipResponseBodySpecEgress):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
