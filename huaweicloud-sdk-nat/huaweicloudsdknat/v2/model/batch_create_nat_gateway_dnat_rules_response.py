# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchCreateNatGatewayDnatRulesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dnat_rules': 'list[NatGatewayDnatRuleResponseBody]'
    }

    attribute_map = {
        'dnat_rules': 'dnat_rules'
    }

    def __init__(self, dnat_rules=None):
        """BatchCreateNatGatewayDnatRulesResponse

        The model defined in huaweicloud sdk

        :param dnat_rules: DNAT规则批量创建对象的响应体。
        :type dnat_rules: list[:class:`huaweicloudsdknat.v2.NatGatewayDnatRuleResponseBody`]
        """
        
        super(BatchCreateNatGatewayDnatRulesResponse, self).__init__()

        self._dnat_rules = None
        self.discriminator = None

        if dnat_rules is not None:
            self.dnat_rules = dnat_rules

    @property
    def dnat_rules(self):
        """Gets the dnat_rules of this BatchCreateNatGatewayDnatRulesResponse.

        DNAT规则批量创建对象的响应体。

        :return: The dnat_rules of this BatchCreateNatGatewayDnatRulesResponse.
        :rtype: list[:class:`huaweicloudsdknat.v2.NatGatewayDnatRuleResponseBody`]
        """
        return self._dnat_rules

    @dnat_rules.setter
    def dnat_rules(self, dnat_rules):
        """Sets the dnat_rules of this BatchCreateNatGatewayDnatRulesResponse.

        DNAT规则批量创建对象的响应体。

        :param dnat_rules: The dnat_rules of this BatchCreateNatGatewayDnatRulesResponse.
        :type dnat_rules: list[:class:`huaweicloudsdknat.v2.NatGatewayDnatRuleResponseBody`]
        """
        self._dnat_rules = dnat_rules

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
        if not isinstance(other, BatchCreateNatGatewayDnatRulesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
