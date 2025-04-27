# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateResolverRuleRequestBody:

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
        'ipaddresses': 'list[IpInfo]'
    }

    attribute_map = {
        'name': 'name',
        'ipaddresses': 'ipaddresses'
    }

    def __init__(self, name=None, ipaddresses=None):
        r"""UpdateResolverRuleRequestBody

        The model defined in huaweicloud sdk

        :param name: 规则名称。 取值范围：1-64个字符，支持数字、字母、中文、_（下划线）、-（中划线）、.（点）。
        :type name: str
        :param ipaddresses: 规则的目标IP地址。
        :type ipaddresses: list[:class:`huaweicloudsdkdns.v2.IpInfo`]
        """
        
        

        self._name = None
        self._ipaddresses = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if ipaddresses is not None:
            self.ipaddresses = ipaddresses

    @property
    def name(self):
        r"""Gets the name of this UpdateResolverRuleRequestBody.

        规则名称。 取值范围：1-64个字符，支持数字、字母、中文、_（下划线）、-（中划线）、.（点）。

        :return: The name of this UpdateResolverRuleRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateResolverRuleRequestBody.

        规则名称。 取值范围：1-64个字符，支持数字、字母、中文、_（下划线）、-（中划线）、.（点）。

        :param name: The name of this UpdateResolverRuleRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def ipaddresses(self):
        r"""Gets the ipaddresses of this UpdateResolverRuleRequestBody.

        规则的目标IP地址。

        :return: The ipaddresses of this UpdateResolverRuleRequestBody.
        :rtype: list[:class:`huaweicloudsdkdns.v2.IpInfo`]
        """
        return self._ipaddresses

    @ipaddresses.setter
    def ipaddresses(self, ipaddresses):
        r"""Sets the ipaddresses of this UpdateResolverRuleRequestBody.

        规则的目标IP地址。

        :param ipaddresses: The ipaddresses of this UpdateResolverRuleRequestBody.
        :type ipaddresses: list[:class:`huaweicloudsdkdns.v2.IpInfo`]
        """
        self._ipaddresses = ipaddresses

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
        if not isinstance(other, UpdateResolverRuleRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
