# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateTenantVpcIgwRequestBodyVpcIgw:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'enable_ipv6': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'enable_ipv6': 'enable_ipv6'
    }

    def __init__(self, name=None, enable_ipv6=None):
        r"""UpdateTenantVpcIgwRequestBodyVpcIgw

        The model defined in huaweicloud sdk

        :param name: 虚拟IGW的名称
        :type name: str
        :param enable_ipv6: 是否使能ipv6
        :type enable_ipv6: bool
        """
        
        

        self._name = None
        self._enable_ipv6 = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if enable_ipv6 is not None:
            self.enable_ipv6 = enable_ipv6

    @property
    def name(self):
        r"""Gets the name of this UpdateTenantVpcIgwRequestBodyVpcIgw.

        虚拟IGW的名称

        :return: The name of this UpdateTenantVpcIgwRequestBodyVpcIgw.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateTenantVpcIgwRequestBodyVpcIgw.

        虚拟IGW的名称

        :param name: The name of this UpdateTenantVpcIgwRequestBodyVpcIgw.
        :type name: str
        """
        self._name = name

    @property
    def enable_ipv6(self):
        r"""Gets the enable_ipv6 of this UpdateTenantVpcIgwRequestBodyVpcIgw.

        是否使能ipv6

        :return: The enable_ipv6 of this UpdateTenantVpcIgwRequestBodyVpcIgw.
        :rtype: bool
        """
        return self._enable_ipv6

    @enable_ipv6.setter
    def enable_ipv6(self, enable_ipv6):
        r"""Sets the enable_ipv6 of this UpdateTenantVpcIgwRequestBodyVpcIgw.

        是否使能ipv6

        :param enable_ipv6: The enable_ipv6 of this UpdateTenantVpcIgwRequestBodyVpcIgw.
        :type enable_ipv6: bool
        """
        self._enable_ipv6 = enable_ipv6

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
        if not isinstance(other, UpdateTenantVpcIgwRequestBodyVpcIgw):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
