# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListHandleAffectBaselineRequestBodyCheckRuleList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'check_name': 'str',
        'check_rule_id': 'str',
        'standard': 'str'
    }

    attribute_map = {
        'check_name': 'check_name',
        'check_rule_id': 'check_rule_id',
        'standard': 'standard'
    }

    def __init__(self, check_name=None, check_rule_id=None, standard=None):
        r"""ListHandleAffectBaselineRequestBodyCheckRuleList

        The model defined in huaweicloud sdk

        :param check_name: **参数解释** 基线检查的名称 **约束限制** 不涉及 **取值范围**   字符长度0-256位 **默认取值** 不涉及
        :type check_name: str
        :param check_rule_id: **参数解释** 检查项id **约束限制** 不涉及 **取值范围**   字符长度0-256位 **默认取值** 不涉及
        :type check_rule_id: str
        :param standard: **参数解释** 基线检查标准类型 **约束限制** 不涉及 **取值范围**   - cn_standard : 等保合规标准 - hw_standard : 云安全实践标准 - cis_standard : 通用安全标准 **默认取值** 不涉及
        :type standard: str
        """
        
        

        self._check_name = None
        self._check_rule_id = None
        self._standard = None
        self.discriminator = None

        if check_name is not None:
            self.check_name = check_name
        if check_rule_id is not None:
            self.check_rule_id = check_rule_id
        if standard is not None:
            self.standard = standard

    @property
    def check_name(self):
        r"""Gets the check_name of this ListHandleAffectBaselineRequestBodyCheckRuleList.

        **参数解释** 基线检查的名称 **约束限制** 不涉及 **取值范围**   字符长度0-256位 **默认取值** 不涉及

        :return: The check_name of this ListHandleAffectBaselineRequestBodyCheckRuleList.
        :rtype: str
        """
        return self._check_name

    @check_name.setter
    def check_name(self, check_name):
        r"""Sets the check_name of this ListHandleAffectBaselineRequestBodyCheckRuleList.

        **参数解释** 基线检查的名称 **约束限制** 不涉及 **取值范围**   字符长度0-256位 **默认取值** 不涉及

        :param check_name: The check_name of this ListHandleAffectBaselineRequestBodyCheckRuleList.
        :type check_name: str
        """
        self._check_name = check_name

    @property
    def check_rule_id(self):
        r"""Gets the check_rule_id of this ListHandleAffectBaselineRequestBodyCheckRuleList.

        **参数解释** 检查项id **约束限制** 不涉及 **取值范围**   字符长度0-256位 **默认取值** 不涉及

        :return: The check_rule_id of this ListHandleAffectBaselineRequestBodyCheckRuleList.
        :rtype: str
        """
        return self._check_rule_id

    @check_rule_id.setter
    def check_rule_id(self, check_rule_id):
        r"""Sets the check_rule_id of this ListHandleAffectBaselineRequestBodyCheckRuleList.

        **参数解释** 检查项id **约束限制** 不涉及 **取值范围**   字符长度0-256位 **默认取值** 不涉及

        :param check_rule_id: The check_rule_id of this ListHandleAffectBaselineRequestBodyCheckRuleList.
        :type check_rule_id: str
        """
        self._check_rule_id = check_rule_id

    @property
    def standard(self):
        r"""Gets the standard of this ListHandleAffectBaselineRequestBodyCheckRuleList.

        **参数解释** 基线检查标准类型 **约束限制** 不涉及 **取值范围**   - cn_standard : 等保合规标准 - hw_standard : 云安全实践标准 - cis_standard : 通用安全标准 **默认取值** 不涉及

        :return: The standard of this ListHandleAffectBaselineRequestBodyCheckRuleList.
        :rtype: str
        """
        return self._standard

    @standard.setter
    def standard(self, standard):
        r"""Sets the standard of this ListHandleAffectBaselineRequestBodyCheckRuleList.

        **参数解释** 基线检查标准类型 **约束限制** 不涉及 **取值范围**   - cn_standard : 等保合规标准 - hw_standard : 云安全实践标准 - cis_standard : 通用安全标准 **默认取值** 不涉及

        :param standard: The standard of this ListHandleAffectBaselineRequestBodyCheckRuleList.
        :type standard: str
        """
        self._standard = standard

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
        if not isinstance(other, ListHandleAffectBaselineRequestBodyCheckRuleList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
