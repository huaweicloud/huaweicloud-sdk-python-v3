# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateIgnoreRuleRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'domain': 'list[str]',
        'conditions': 'list[CreateCondition]',
        'mode': 'int',
        'rule': 'str',
        'description': 'str'
    }

    attribute_map = {
        'domain': 'domain',
        'conditions': 'conditions',
        'mode': 'mode',
        'rule': 'rule',
        'description': 'description'
    }

    def __init__(self, domain=None, conditions=None, mode=None, rule=None, description=None):
        """CreateIgnoreRuleRequestBody

        The model defined in huaweicloud sdk

        :param domain: 防护域名或防护网站，数组长度为0时，代表规则对全部域名或防护网站生效
        :type domain: list[str]
        :param conditions: 条件列表
        :type conditions: list[:class:`huaweicloudsdkwaf.v1.CreateCondition`]
        :param mode: 固定值为1,代表v2版本误报屏蔽规则，v1版本仅用于兼容旧版本，不支持创建
        :type mode: int
        :param rule: 屏蔽的内置规则id（内置规则id通常可以在Web应用防火墙控制台的防护策略-&gt;策略名称-&gt;Web基础防护-&gt;防护规则中查询，也可以在防护事件的事件详情中看到查询规则id）
        :type rule: str
        :param description: 屏蔽规则描述
        :type description: str
        """
        
        

        self._domain = None
        self._conditions = None
        self._mode = None
        self._rule = None
        self._description = None
        self.discriminator = None

        self.domain = domain
        self.conditions = conditions
        self.mode = mode
        self.rule = rule
        if description is not None:
            self.description = description

    @property
    def domain(self):
        """Gets the domain of this CreateIgnoreRuleRequestBody.

        防护域名或防护网站，数组长度为0时，代表规则对全部域名或防护网站生效

        :return: The domain of this CreateIgnoreRuleRequestBody.
        :rtype: list[str]
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this CreateIgnoreRuleRequestBody.

        防护域名或防护网站，数组长度为0时，代表规则对全部域名或防护网站生效

        :param domain: The domain of this CreateIgnoreRuleRequestBody.
        :type domain: list[str]
        """
        self._domain = domain

    @property
    def conditions(self):
        """Gets the conditions of this CreateIgnoreRuleRequestBody.

        条件列表

        :return: The conditions of this CreateIgnoreRuleRequestBody.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.CreateCondition`]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this CreateIgnoreRuleRequestBody.

        条件列表

        :param conditions: The conditions of this CreateIgnoreRuleRequestBody.
        :type conditions: list[:class:`huaweicloudsdkwaf.v1.CreateCondition`]
        """
        self._conditions = conditions

    @property
    def mode(self):
        """Gets the mode of this CreateIgnoreRuleRequestBody.

        固定值为1,代表v2版本误报屏蔽规则，v1版本仅用于兼容旧版本，不支持创建

        :return: The mode of this CreateIgnoreRuleRequestBody.
        :rtype: int
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this CreateIgnoreRuleRequestBody.

        固定值为1,代表v2版本误报屏蔽规则，v1版本仅用于兼容旧版本，不支持创建

        :param mode: The mode of this CreateIgnoreRuleRequestBody.
        :type mode: int
        """
        self._mode = mode

    @property
    def rule(self):
        """Gets the rule of this CreateIgnoreRuleRequestBody.

        屏蔽的内置规则id（内置规则id通常可以在Web应用防火墙控制台的防护策略->策略名称->Web基础防护->防护规则中查询，也可以在防护事件的事件详情中看到查询规则id）

        :return: The rule of this CreateIgnoreRuleRequestBody.
        :rtype: str
        """
        return self._rule

    @rule.setter
    def rule(self, rule):
        """Sets the rule of this CreateIgnoreRuleRequestBody.

        屏蔽的内置规则id（内置规则id通常可以在Web应用防火墙控制台的防护策略->策略名称->Web基础防护->防护规则中查询，也可以在防护事件的事件详情中看到查询规则id）

        :param rule: The rule of this CreateIgnoreRuleRequestBody.
        :type rule: str
        """
        self._rule = rule

    @property
    def description(self):
        """Gets the description of this CreateIgnoreRuleRequestBody.

        屏蔽规则描述

        :return: The description of this CreateIgnoreRuleRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateIgnoreRuleRequestBody.

        屏蔽规则描述

        :param description: The description of this CreateIgnoreRuleRequestBody.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, CreateIgnoreRuleRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
