# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateRuleNewRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_name': 'str',
        'rule_id': 'str',
        'body': 'UpdateRuleRequest'
    }

    attribute_map = {
        'domain_name': 'domain_name',
        'rule_id': 'rule_id',
        'body': 'body'
    }

    def __init__(self, domain_name=None, rule_id=None, body=None):
        r"""UpdateRuleNewRequest

        The model defined in huaweicloud sdk

        :param domain_name: **参数解释：** 加速域名 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type domain_name: str
        :param rule_id: **参数解释：** 规则ID，可以通过查询规则引擎列表接口获取 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type rule_id: str
        :param body: Body of the UpdateRuleNewRequest
        :type body: :class:`huaweicloudsdkcdn.v2.UpdateRuleRequest`
        """
        
        

        self._domain_name = None
        self._rule_id = None
        self._body = None
        self.discriminator = None

        self.domain_name = domain_name
        self.rule_id = rule_id
        if body is not None:
            self.body = body

    @property
    def domain_name(self):
        r"""Gets the domain_name of this UpdateRuleNewRequest.

        **参数解释：** 加速域名 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The domain_name of this UpdateRuleNewRequest.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this UpdateRuleNewRequest.

        **参数解释：** 加速域名 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param domain_name: The domain_name of this UpdateRuleNewRequest.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def rule_id(self):
        r"""Gets the rule_id of this UpdateRuleNewRequest.

        **参数解释：** 规则ID，可以通过查询规则引擎列表接口获取 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The rule_id of this UpdateRuleNewRequest.
        :rtype: str
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        r"""Sets the rule_id of this UpdateRuleNewRequest.

        **参数解释：** 规则ID，可以通过查询规则引擎列表接口获取 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param rule_id: The rule_id of this UpdateRuleNewRequest.
        :type rule_id: str
        """
        self._rule_id = rule_id

    @property
    def body(self):
        r"""Gets the body of this UpdateRuleNewRequest.

        :return: The body of this UpdateRuleNewRequest.
        :rtype: :class:`huaweicloudsdkcdn.v2.UpdateRuleRequest`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateRuleNewRequest.

        :param body: The body of this UpdateRuleNewRequest.
        :type body: :class:`huaweicloudsdkcdn.v2.UpdateRuleRequest`
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
        if not isinstance(other, UpdateRuleNewRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
