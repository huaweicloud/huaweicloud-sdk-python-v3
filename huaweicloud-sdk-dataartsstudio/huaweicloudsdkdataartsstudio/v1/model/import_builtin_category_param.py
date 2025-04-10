# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImportBuiltinCategoryParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'rule_secrecy_level_list': 'list[ImportRuleSecrecyLevelDto]'
    }

    attribute_map = {
        'rule_secrecy_level_list': 'rule_secrecy_level_list'
    }

    def __init__(self, rule_secrecy_level_list=None):
        r"""ImportBuiltinCategoryParam

        The model defined in huaweicloud sdk

        :param rule_secrecy_level_list: 规则对应密级的列表，需要将所有未导入的内置规则导入。
        :type rule_secrecy_level_list: list[:class:`huaweicloudsdkdataartsstudio.v1.ImportRuleSecrecyLevelDto`]
        """
        
        

        self._rule_secrecy_level_list = None
        self.discriminator = None

        if rule_secrecy_level_list is not None:
            self.rule_secrecy_level_list = rule_secrecy_level_list

    @property
    def rule_secrecy_level_list(self):
        r"""Gets the rule_secrecy_level_list of this ImportBuiltinCategoryParam.

        规则对应密级的列表，需要将所有未导入的内置规则导入。

        :return: The rule_secrecy_level_list of this ImportBuiltinCategoryParam.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.ImportRuleSecrecyLevelDto`]
        """
        return self._rule_secrecy_level_list

    @rule_secrecy_level_list.setter
    def rule_secrecy_level_list(self, rule_secrecy_level_list):
        r"""Sets the rule_secrecy_level_list of this ImportBuiltinCategoryParam.

        规则对应密级的列表，需要将所有未导入的内置规则导入。

        :param rule_secrecy_level_list: The rule_secrecy_level_list of this ImportBuiltinCategoryParam.
        :type rule_secrecy_level_list: list[:class:`huaweicloudsdkdataartsstudio.v1.ImportRuleSecrecyLevelDto`]
        """
        self._rule_secrecy_level_list = rule_secrecy_level_list

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
        if not isinstance(other, ImportBuiltinCategoryParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
