# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSqlInjectionRulesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'rules': 'list[SqlRuleResponseRules]',
        'total': 'int'
    }

    attribute_map = {
        'rules': 'rules',
        'total': 'total'
    }

    def __init__(self, rules=None, total=None):
        r"""ListSqlInjectionRulesResponse

        The model defined in huaweicloud sdk

        :param rules: SQL规则列表
        :type rules: list[:class:`huaweicloudsdkdbss.v1.SqlRuleResponseRules`]
        :param total: 总数
        :type total: int
        """
        
        super(ListSqlInjectionRulesResponse, self).__init__()

        self._rules = None
        self._total = None
        self.discriminator = None

        if rules is not None:
            self.rules = rules
        if total is not None:
            self.total = total

    @property
    def rules(self):
        r"""Gets the rules of this ListSqlInjectionRulesResponse.

        SQL规则列表

        :return: The rules of this ListSqlInjectionRulesResponse.
        :rtype: list[:class:`huaweicloudsdkdbss.v1.SqlRuleResponseRules`]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        r"""Sets the rules of this ListSqlInjectionRulesResponse.

        SQL规则列表

        :param rules: The rules of this ListSqlInjectionRulesResponse.
        :type rules: list[:class:`huaweicloudsdkdbss.v1.SqlRuleResponseRules`]
        """
        self._rules = rules

    @property
    def total(self):
        r"""Gets the total of this ListSqlInjectionRulesResponse.

        总数

        :return: The total of this ListSqlInjectionRulesResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListSqlInjectionRulesResponse.

        总数

        :param total: The total of this ListSqlInjectionRulesResponse.
        :type total: int
        """
        self._total = total

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
        if not isinstance(other, ListSqlInjectionRulesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
