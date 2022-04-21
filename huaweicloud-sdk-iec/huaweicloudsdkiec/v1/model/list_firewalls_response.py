# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFirewallsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'firewalls': 'list[Firewall]'
    }

    attribute_map = {
        'count': 'count',
        'firewalls': 'firewalls'
    }

    def __init__(self, count=None, firewalls=None):
        """ListFirewallsResponse

        The model defined in huaweicloud sdk

        :param count: 网络ACL数量。
        :type count: int
        :param firewalls: 网络ACL列表。
        :type firewalls: list[:class:`huaweicloudsdkiec.v1.Firewall`]
        """
        
        super(ListFirewallsResponse, self).__init__()

        self._count = None
        self._firewalls = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if firewalls is not None:
            self.firewalls = firewalls

    @property
    def count(self):
        """Gets the count of this ListFirewallsResponse.

        网络ACL数量。

        :return: The count of this ListFirewallsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListFirewallsResponse.

        网络ACL数量。

        :param count: The count of this ListFirewallsResponse.
        :type count: int
        """
        self._count = count

    @property
    def firewalls(self):
        """Gets the firewalls of this ListFirewallsResponse.

        网络ACL列表。

        :return: The firewalls of this ListFirewallsResponse.
        :rtype: list[:class:`huaweicloudsdkiec.v1.Firewall`]
        """
        return self._firewalls

    @firewalls.setter
    def firewalls(self, firewalls):
        """Sets the firewalls of this ListFirewallsResponse.

        网络ACL列表。

        :param firewalls: The firewalls of this ListFirewallsResponse.
        :type firewalls: list[:class:`huaweicloudsdkiec.v1.Firewall`]
        """
        self._firewalls = firewalls

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
        if not isinstance(other, ListFirewallsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
