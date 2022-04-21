# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateRoutingRuleRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'rule_id': 'str',
        'body': 'UpdateRuleReq'
    }

    attribute_map = {
        'instance_id': 'Instance-Id',
        'rule_id': 'rule_id',
        'body': 'body'
    }

    def __init__(self, instance_id=None, rule_id=None, body=None):
        """UpdateRoutingRuleRequest

        The model defined in huaweicloud sdk

        :param instance_id: **参数说明**：实例ID。物理多租下各实例的唯一标识，一般华为云租户无需携带该参数，仅在物理多租场景下从管理面访问API时需要携带该参数。
        :type instance_id: str
        :param rule_id: **参数说明**：规则条件ID。 **取值范围**：长度不超过36，只允许字母、数字、下划线（_）、连接符（-）的组合。
        :type rule_id: str
        :param body: Body of the UpdateRoutingRuleRequest
        :type body: :class:`huaweicloudsdkiotda.v5.UpdateRuleReq`
        """
        
        

        self._instance_id = None
        self._rule_id = None
        self._body = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        self.rule_id = rule_id
        if body is not None:
            self.body = body

    @property
    def instance_id(self):
        """Gets the instance_id of this UpdateRoutingRuleRequest.

        **参数说明**：实例ID。物理多租下各实例的唯一标识，一般华为云租户无需携带该参数，仅在物理多租场景下从管理面访问API时需要携带该参数。

        :return: The instance_id of this UpdateRoutingRuleRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this UpdateRoutingRuleRequest.

        **参数说明**：实例ID。物理多租下各实例的唯一标识，一般华为云租户无需携带该参数，仅在物理多租场景下从管理面访问API时需要携带该参数。

        :param instance_id: The instance_id of this UpdateRoutingRuleRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def rule_id(self):
        """Gets the rule_id of this UpdateRoutingRuleRequest.

        **参数说明**：规则条件ID。 **取值范围**：长度不超过36，只允许字母、数字、下划线（_）、连接符（-）的组合。

        :return: The rule_id of this UpdateRoutingRuleRequest.
        :rtype: str
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        """Sets the rule_id of this UpdateRoutingRuleRequest.

        **参数说明**：规则条件ID。 **取值范围**：长度不超过36，只允许字母、数字、下划线（_）、连接符（-）的组合。

        :param rule_id: The rule_id of this UpdateRoutingRuleRequest.
        :type rule_id: str
        """
        self._rule_id = rule_id

    @property
    def body(self):
        """Gets the body of this UpdateRoutingRuleRequest.


        :return: The body of this UpdateRoutingRuleRequest.
        :rtype: :class:`huaweicloudsdkiotda.v5.UpdateRuleReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateRoutingRuleRequest.


        :param body: The body of this UpdateRoutingRuleRequest.
        :type body: :class:`huaweicloudsdkiotda.v5.UpdateRuleReq`
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
        if not isinstance(other, UpdateRoutingRuleRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
