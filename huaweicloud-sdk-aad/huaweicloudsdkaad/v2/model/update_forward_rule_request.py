# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateForwardRuleRequest:

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
        'ip': 'str',
        'body': 'UpdateForwardRuleRequestBody'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'rule_id': 'rule_id',
        'ip': 'ip',
        'body': 'body'
    }

    def __init__(self, instance_id=None, rule_id=None, ip=None, body=None):
        r"""UpdateForwardRuleRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例id
        :type instance_id: str
        :param rule_id: 规则id
        :type rule_id: str
        :param ip: 高防ip
        :type ip: str
        :param body: Body of the UpdateForwardRuleRequest
        :type body: :class:`huaweicloudsdkaad.v2.UpdateForwardRuleRequestBody`
        """
        
        

        self._instance_id = None
        self._rule_id = None
        self._ip = None
        self._body = None
        self.discriminator = None

        self.instance_id = instance_id
        self.rule_id = rule_id
        self.ip = ip
        if body is not None:
            self.body = body

    @property
    def instance_id(self):
        r"""Gets the instance_id of this UpdateForwardRuleRequest.

        实例id

        :return: The instance_id of this UpdateForwardRuleRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this UpdateForwardRuleRequest.

        实例id

        :param instance_id: The instance_id of this UpdateForwardRuleRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def rule_id(self):
        r"""Gets the rule_id of this UpdateForwardRuleRequest.

        规则id

        :return: The rule_id of this UpdateForwardRuleRequest.
        :rtype: str
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        r"""Sets the rule_id of this UpdateForwardRuleRequest.

        规则id

        :param rule_id: The rule_id of this UpdateForwardRuleRequest.
        :type rule_id: str
        """
        self._rule_id = rule_id

    @property
    def ip(self):
        r"""Gets the ip of this UpdateForwardRuleRequest.

        高防ip

        :return: The ip of this UpdateForwardRuleRequest.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        r"""Sets the ip of this UpdateForwardRuleRequest.

        高防ip

        :param ip: The ip of this UpdateForwardRuleRequest.
        :type ip: str
        """
        self._ip = ip

    @property
    def body(self):
        r"""Gets the body of this UpdateForwardRuleRequest.

        :return: The body of this UpdateForwardRuleRequest.
        :rtype: :class:`huaweicloudsdkaad.v2.UpdateForwardRuleRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateForwardRuleRequest.

        :param body: The body of this UpdateForwardRuleRequest.
        :type body: :class:`huaweicloudsdkaad.v2.UpdateForwardRuleRequestBody`
        """
        self._body = body

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdateForwardRuleRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
