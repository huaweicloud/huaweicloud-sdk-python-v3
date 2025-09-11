# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RuleAddSqlRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'risk_level': 'str',
        'rule_name': 'str',
        'sql_regex': 'str',
        'status': 'str'
    }

    attribute_map = {
        'risk_level': 'risk_level',
        'rule_name': 'rule_name',
        'sql_regex': 'sql_regex',
        'status': 'status'
    }

    def __init__(self, risk_level=None, rule_name=None, sql_regex=None, status=None):
        r"""RuleAddSqlRequest

        The model defined in huaweicloud sdk

        :param risk_level: 风险等级  - LOW：低  - MEDIUM：中  - HIGH：高 - NO_RISK：无
        :type risk_level: str
        :param rule_name: 规则名称
        :type rule_name: str
        :param sql_regex: 正则表达式
        :type sql_regex: str
        :param status: 状态  - ON：开启  - OFF：关闭
        :type status: str
        """
        
        

        self._risk_level = None
        self._rule_name = None
        self._sql_regex = None
        self._status = None
        self.discriminator = None

        self.risk_level = risk_level
        self.rule_name = rule_name
        self.sql_regex = sql_regex
        self.status = status

    @property
    def risk_level(self):
        r"""Gets the risk_level of this RuleAddSqlRequest.

        风险等级  - LOW：低  - MEDIUM：中  - HIGH：高 - NO_RISK：无

        :return: The risk_level of this RuleAddSqlRequest.
        :rtype: str
        """
        return self._risk_level

    @risk_level.setter
    def risk_level(self, risk_level):
        r"""Sets the risk_level of this RuleAddSqlRequest.

        风险等级  - LOW：低  - MEDIUM：中  - HIGH：高 - NO_RISK：无

        :param risk_level: The risk_level of this RuleAddSqlRequest.
        :type risk_level: str
        """
        self._risk_level = risk_level

    @property
    def rule_name(self):
        r"""Gets the rule_name of this RuleAddSqlRequest.

        规则名称

        :return: The rule_name of this RuleAddSqlRequest.
        :rtype: str
        """
        return self._rule_name

    @rule_name.setter
    def rule_name(self, rule_name):
        r"""Sets the rule_name of this RuleAddSqlRequest.

        规则名称

        :param rule_name: The rule_name of this RuleAddSqlRequest.
        :type rule_name: str
        """
        self._rule_name = rule_name

    @property
    def sql_regex(self):
        r"""Gets the sql_regex of this RuleAddSqlRequest.

        正则表达式

        :return: The sql_regex of this RuleAddSqlRequest.
        :rtype: str
        """
        return self._sql_regex

    @sql_regex.setter
    def sql_regex(self, sql_regex):
        r"""Sets the sql_regex of this RuleAddSqlRequest.

        正则表达式

        :param sql_regex: The sql_regex of this RuleAddSqlRequest.
        :type sql_regex: str
        """
        self._sql_regex = sql_regex

    @property
    def status(self):
        r"""Gets the status of this RuleAddSqlRequest.

        状态  - ON：开启  - OFF：关闭

        :return: The status of this RuleAddSqlRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this RuleAddSqlRequest.

        状态  - ON：开启  - OFF：关闭

        :param status: The status of this RuleAddSqlRequest.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, RuleAddSqlRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
