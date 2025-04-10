# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateNatGatewayDnatRuleRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dnat_rule_id': 'str',
        'body': 'UpdateNatGatewayDnatRuleRequestBody'
    }

    attribute_map = {
        'dnat_rule_id': 'dnat_rule_id',
        'body': 'body'
    }

    def __init__(self, dnat_rule_id=None, body=None):
        r"""UpdateNatGatewayDnatRuleRequest

        The model defined in huaweicloud sdk

        :param dnat_rule_id: DNAT规则的ID。
        :type dnat_rule_id: str
        :param body: Body of the UpdateNatGatewayDnatRuleRequest
        :type body: :class:`huaweicloudsdknat.v2.UpdateNatGatewayDnatRuleRequestBody`
        """
        
        

        self._dnat_rule_id = None
        self._body = None
        self.discriminator = None

        self.dnat_rule_id = dnat_rule_id
        if body is not None:
            self.body = body

    @property
    def dnat_rule_id(self):
        r"""Gets the dnat_rule_id of this UpdateNatGatewayDnatRuleRequest.

        DNAT规则的ID。

        :return: The dnat_rule_id of this UpdateNatGatewayDnatRuleRequest.
        :rtype: str
        """
        return self._dnat_rule_id

    @dnat_rule_id.setter
    def dnat_rule_id(self, dnat_rule_id):
        r"""Sets the dnat_rule_id of this UpdateNatGatewayDnatRuleRequest.

        DNAT规则的ID。

        :param dnat_rule_id: The dnat_rule_id of this UpdateNatGatewayDnatRuleRequest.
        :type dnat_rule_id: str
        """
        self._dnat_rule_id = dnat_rule_id

    @property
    def body(self):
        r"""Gets the body of this UpdateNatGatewayDnatRuleRequest.

        :return: The body of this UpdateNatGatewayDnatRuleRequest.
        :rtype: :class:`huaweicloudsdknat.v2.UpdateNatGatewayDnatRuleRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateNatGatewayDnatRuleRequest.

        :param body: The body of this UpdateNatGatewayDnatRuleRequest.
        :type body: :class:`huaweicloudsdknat.v2.UpdateNatGatewayDnatRuleRequestBody`
        """
        self._body = body

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
        if not isinstance(other, UpdateNatGatewayDnatRuleRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
