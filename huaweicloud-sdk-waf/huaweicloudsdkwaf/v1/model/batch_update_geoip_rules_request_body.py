# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchUpdateGeoipRulesRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policy_rule_ids': 'list[PolicyRuleIdRequestBodyPolicyRuleIds]',
        'status': 'int',
        'name': 'str',
        'geoip': 'str',
        'white': 'int'
    }

    attribute_map = {
        'policy_rule_ids': 'policy_rule_ids',
        'status': 'status',
        'name': 'name',
        'geoip': 'geoip',
        'white': 'white'
    }

    def __init__(self, policy_rule_ids=None, status=None, name=None, geoip=None, white=None):
        r"""BatchUpdateGeoipRulesRequestBody

        The model defined in huaweicloud sdk

        :param policy_rule_ids: **参数解释：** 策略和规则id数组，关联防护策略与对应的规则集合 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type policy_rule_ids: list[:class:`huaweicloudsdkwaf.v1.PolicyRuleIdRequestBodyPolicyRuleIds`]
        :param status: **参数解释：** 规则状态，控制地理位置访问控制规则的启用/禁用（如1表示启用，0表示禁用） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type status: int
        :param name: **参数解释：** 规则名称，标识地理位置访问控制规则的名称 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type name: str
        :param geoip: **参数解释：** 地理位置，指定需要控制的地域（如省份、城市编码，多个用|分隔） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type geoip: str
        :param white: **参数解释：** 放行或者拦截，1表示放行指定地理位置，2表示拦截指定地理位置 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type white: int
        """
        
        

        self._policy_rule_ids = None
        self._status = None
        self._name = None
        self._geoip = None
        self._white = None
        self.discriminator = None

        if policy_rule_ids is not None:
            self.policy_rule_ids = policy_rule_ids
        if status is not None:
            self.status = status
        if name is not None:
            self.name = name
        if geoip is not None:
            self.geoip = geoip
        if white is not None:
            self.white = white

    @property
    def policy_rule_ids(self):
        r"""Gets the policy_rule_ids of this BatchUpdateGeoipRulesRequestBody.

        **参数解释：** 策略和规则id数组，关联防护策略与对应的规则集合 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The policy_rule_ids of this BatchUpdateGeoipRulesRequestBody.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.PolicyRuleIdRequestBodyPolicyRuleIds`]
        """
        return self._policy_rule_ids

    @policy_rule_ids.setter
    def policy_rule_ids(self, policy_rule_ids):
        r"""Sets the policy_rule_ids of this BatchUpdateGeoipRulesRequestBody.

        **参数解释：** 策略和规则id数组，关联防护策略与对应的规则集合 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param policy_rule_ids: The policy_rule_ids of this BatchUpdateGeoipRulesRequestBody.
        :type policy_rule_ids: list[:class:`huaweicloudsdkwaf.v1.PolicyRuleIdRequestBodyPolicyRuleIds`]
        """
        self._policy_rule_ids = policy_rule_ids

    @property
    def status(self):
        r"""Gets the status of this BatchUpdateGeoipRulesRequestBody.

        **参数解释：** 规则状态，控制地理位置访问控制规则的启用/禁用（如1表示启用，0表示禁用） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The status of this BatchUpdateGeoipRulesRequestBody.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this BatchUpdateGeoipRulesRequestBody.

        **参数解释：** 规则状态，控制地理位置访问控制规则的启用/禁用（如1表示启用，0表示禁用） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param status: The status of this BatchUpdateGeoipRulesRequestBody.
        :type status: int
        """
        self._status = status

    @property
    def name(self):
        r"""Gets the name of this BatchUpdateGeoipRulesRequestBody.

        **参数解释：** 规则名称，标识地理位置访问控制规则的名称 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The name of this BatchUpdateGeoipRulesRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this BatchUpdateGeoipRulesRequestBody.

        **参数解释：** 规则名称，标识地理位置访问控制规则的名称 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param name: The name of this BatchUpdateGeoipRulesRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def geoip(self):
        r"""Gets the geoip of this BatchUpdateGeoipRulesRequestBody.

        **参数解释：** 地理位置，指定需要控制的地域（如省份、城市编码，多个用|分隔） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The geoip of this BatchUpdateGeoipRulesRequestBody.
        :rtype: str
        """
        return self._geoip

    @geoip.setter
    def geoip(self, geoip):
        r"""Sets the geoip of this BatchUpdateGeoipRulesRequestBody.

        **参数解释：** 地理位置，指定需要控制的地域（如省份、城市编码，多个用|分隔） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param geoip: The geoip of this BatchUpdateGeoipRulesRequestBody.
        :type geoip: str
        """
        self._geoip = geoip

    @property
    def white(self):
        r"""Gets the white of this BatchUpdateGeoipRulesRequestBody.

        **参数解释：** 放行或者拦截，1表示放行指定地理位置，2表示拦截指定地理位置 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The white of this BatchUpdateGeoipRulesRequestBody.
        :rtype: int
        """
        return self._white

    @white.setter
    def white(self, white):
        r"""Sets the white of this BatchUpdateGeoipRulesRequestBody.

        **参数解释：** 放行或者拦截，1表示放行指定地理位置，2表示拦截指定地理位置 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param white: The white of this BatchUpdateGeoipRulesRequestBody.
        :type white: int
        """
        self._white = white

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
        if not isinstance(other, BatchUpdateGeoipRulesRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
