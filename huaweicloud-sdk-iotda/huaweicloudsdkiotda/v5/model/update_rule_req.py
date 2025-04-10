# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateRuleReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'rule_name': 'str',
        'description': 'str',
        'select': 'str',
        'where': 'str',
        'active': 'bool'
    }

    attribute_map = {
        'rule_name': 'rule_name',
        'description': 'description',
        'select': 'select',
        'where': 'where',
        'active': 'active'
    }

    def __init__(self, rule_name=None, description=None, select=None, where=None, active=None):
        r"""UpdateRuleReq

        The model defined in huaweicloud sdk

        :param rule_name: **参数说明**：规则名称。 **取值范围**：长度不超过256，只允许中文、字母、数字、以及_?&#39;#().,&amp;%@!-等字符的组合
        :type rule_name: str
        :param description: **参数说明**：用户自定义的规则描述。
        :type description: str
        :param select: **参数说明**：用户自定义sql select语句，最大长度2500，更新sql时，select跟where必须同时传参，如果需要清除该参数的值，输入空字符串，该参数仅供标准版和企业版用户使用。
        :type select: str
        :param where: **参数说明**：用户自定义sql where语句，最大长度2500，更新操作时，select跟where必须同时传参，如果需要清除该参数的值，输入空字符串，该参数仅供标准版和企业版用户使用。
        :type where: str
        :param active: **参数说明**：修改规则条件的状态是否为激活。
        :type active: bool
        """
        
        

        self._rule_name = None
        self._description = None
        self._select = None
        self._where = None
        self._active = None
        self.discriminator = None

        if rule_name is not None:
            self.rule_name = rule_name
        if description is not None:
            self.description = description
        if select is not None:
            self.select = select
        if where is not None:
            self.where = where
        if active is not None:
            self.active = active

    @property
    def rule_name(self):
        r"""Gets the rule_name of this UpdateRuleReq.

        **参数说明**：规则名称。 **取值范围**：长度不超过256，只允许中文、字母、数字、以及_?'#().,&%@!-等字符的组合

        :return: The rule_name of this UpdateRuleReq.
        :rtype: str
        """
        return self._rule_name

    @rule_name.setter
    def rule_name(self, rule_name):
        r"""Sets the rule_name of this UpdateRuleReq.

        **参数说明**：规则名称。 **取值范围**：长度不超过256，只允许中文、字母、数字、以及_?'#().,&%@!-等字符的组合

        :param rule_name: The rule_name of this UpdateRuleReq.
        :type rule_name: str
        """
        self._rule_name = rule_name

    @property
    def description(self):
        r"""Gets the description of this UpdateRuleReq.

        **参数说明**：用户自定义的规则描述。

        :return: The description of this UpdateRuleReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateRuleReq.

        **参数说明**：用户自定义的规则描述。

        :param description: The description of this UpdateRuleReq.
        :type description: str
        """
        self._description = description

    @property
    def select(self):
        r"""Gets the select of this UpdateRuleReq.

        **参数说明**：用户自定义sql select语句，最大长度2500，更新sql时，select跟where必须同时传参，如果需要清除该参数的值，输入空字符串，该参数仅供标准版和企业版用户使用。

        :return: The select of this UpdateRuleReq.
        :rtype: str
        """
        return self._select

    @select.setter
    def select(self, select):
        r"""Sets the select of this UpdateRuleReq.

        **参数说明**：用户自定义sql select语句，最大长度2500，更新sql时，select跟where必须同时传参，如果需要清除该参数的值，输入空字符串，该参数仅供标准版和企业版用户使用。

        :param select: The select of this UpdateRuleReq.
        :type select: str
        """
        self._select = select

    @property
    def where(self):
        r"""Gets the where of this UpdateRuleReq.

        **参数说明**：用户自定义sql where语句，最大长度2500，更新操作时，select跟where必须同时传参，如果需要清除该参数的值，输入空字符串，该参数仅供标准版和企业版用户使用。

        :return: The where of this UpdateRuleReq.
        :rtype: str
        """
        return self._where

    @where.setter
    def where(self, where):
        r"""Sets the where of this UpdateRuleReq.

        **参数说明**：用户自定义sql where语句，最大长度2500，更新操作时，select跟where必须同时传参，如果需要清除该参数的值，输入空字符串，该参数仅供标准版和企业版用户使用。

        :param where: The where of this UpdateRuleReq.
        :type where: str
        """
        self._where = where

    @property
    def active(self):
        r"""Gets the active of this UpdateRuleReq.

        **参数说明**：修改规则条件的状态是否为激活。

        :return: The active of this UpdateRuleReq.
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        r"""Sets the active of this UpdateRuleReq.

        **参数说明**：修改规则条件的状态是否为激活。

        :param active: The active of this UpdateRuleReq.
        :type active: bool
        """
        self._active = active

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
        if not isinstance(other, UpdateRuleReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
