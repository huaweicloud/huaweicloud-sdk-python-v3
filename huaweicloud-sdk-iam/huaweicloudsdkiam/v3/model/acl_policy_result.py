# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AclPolicyResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'allow_address_netmasks': 'list[AllowAddressNetmasksResult]',
        'allow_ip_ranges': 'list[AllowIpRangesResult]'
    }

    attribute_map = {
        'allow_address_netmasks': 'allow_address_netmasks',
        'allow_ip_ranges': 'allow_ip_ranges'
    }

    def __init__(self, allow_address_netmasks=None, allow_ip_ranges=None):
        r"""AclPolicyResult

        The model defined in huaweicloud sdk

        :param allow_address_netmasks: 允许访问的IP地址或网段。
        :type allow_address_netmasks: list[:class:`huaweicloudsdkiam.v3.AllowAddressNetmasksResult`]
        :param allow_ip_ranges: 允许访问的IP地址区间。
        :type allow_ip_ranges: list[:class:`huaweicloudsdkiam.v3.AllowIpRangesResult`]
        """
        
        

        self._allow_address_netmasks = None
        self._allow_ip_ranges = None
        self.discriminator = None

        if allow_address_netmasks is not None:
            self.allow_address_netmasks = allow_address_netmasks
        if allow_ip_ranges is not None:
            self.allow_ip_ranges = allow_ip_ranges

    @property
    def allow_address_netmasks(self):
        r"""Gets the allow_address_netmasks of this AclPolicyResult.

        允许访问的IP地址或网段。

        :return: The allow_address_netmasks of this AclPolicyResult.
        :rtype: list[:class:`huaweicloudsdkiam.v3.AllowAddressNetmasksResult`]
        """
        return self._allow_address_netmasks

    @allow_address_netmasks.setter
    def allow_address_netmasks(self, allow_address_netmasks):
        r"""Sets the allow_address_netmasks of this AclPolicyResult.

        允许访问的IP地址或网段。

        :param allow_address_netmasks: The allow_address_netmasks of this AclPolicyResult.
        :type allow_address_netmasks: list[:class:`huaweicloudsdkiam.v3.AllowAddressNetmasksResult`]
        """
        self._allow_address_netmasks = allow_address_netmasks

    @property
    def allow_ip_ranges(self):
        r"""Gets the allow_ip_ranges of this AclPolicyResult.

        允许访问的IP地址区间。

        :return: The allow_ip_ranges of this AclPolicyResult.
        :rtype: list[:class:`huaweicloudsdkiam.v3.AllowIpRangesResult`]
        """
        return self._allow_ip_ranges

    @allow_ip_ranges.setter
    def allow_ip_ranges(self, allow_ip_ranges):
        r"""Sets the allow_ip_ranges of this AclPolicyResult.

        允许访问的IP地址区间。

        :param allow_ip_ranges: The allow_ip_ranges of this AclPolicyResult.
        :type allow_ip_ranges: list[:class:`huaweicloudsdkiam.v3.AllowIpRangesResult`]
        """
        self._allow_ip_ranges = allow_ip_ranges

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
        if not isinstance(other, AclPolicyResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
