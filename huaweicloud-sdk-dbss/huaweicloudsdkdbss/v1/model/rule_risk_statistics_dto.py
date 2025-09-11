# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RuleRiskStatisticsDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'instance_risk_count': 'list[AuditInsanceRiskCount]',
        'rule_name': 'str'
    }

    attribute_map = {
        'count': 'count',
        'instance_risk_count': 'instance_risk_count',
        'rule_name': 'rule_name'
    }

    def __init__(self, count=None, instance_risk_count=None, rule_name=None):
        r"""RuleRiskStatisticsDto

        The model defined in huaweicloud sdk

        :param count: 数量
        :type count: int
        :param instance_risk_count: 实例数据库风险汇总
        :type instance_risk_count: list[:class:`huaweicloudsdkdbss.v1.AuditInsanceRiskCount`]
        :param rule_name: 规则名称
        :type rule_name: str
        """
        
        

        self._count = None
        self._instance_risk_count = None
        self._rule_name = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if instance_risk_count is not None:
            self.instance_risk_count = instance_risk_count
        if rule_name is not None:
            self.rule_name = rule_name

    @property
    def count(self):
        r"""Gets the count of this RuleRiskStatisticsDto.

        数量

        :return: The count of this RuleRiskStatisticsDto.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this RuleRiskStatisticsDto.

        数量

        :param count: The count of this RuleRiskStatisticsDto.
        :type count: int
        """
        self._count = count

    @property
    def instance_risk_count(self):
        r"""Gets the instance_risk_count of this RuleRiskStatisticsDto.

        实例数据库风险汇总

        :return: The instance_risk_count of this RuleRiskStatisticsDto.
        :rtype: list[:class:`huaweicloudsdkdbss.v1.AuditInsanceRiskCount`]
        """
        return self._instance_risk_count

    @instance_risk_count.setter
    def instance_risk_count(self, instance_risk_count):
        r"""Sets the instance_risk_count of this RuleRiskStatisticsDto.

        实例数据库风险汇总

        :param instance_risk_count: The instance_risk_count of this RuleRiskStatisticsDto.
        :type instance_risk_count: list[:class:`huaweicloudsdkdbss.v1.AuditInsanceRiskCount`]
        """
        self._instance_risk_count = instance_risk_count

    @property
    def rule_name(self):
        r"""Gets the rule_name of this RuleRiskStatisticsDto.

        规则名称

        :return: The rule_name of this RuleRiskStatisticsDto.
        :rtype: str
        """
        return self._rule_name

    @rule_name.setter
    def rule_name(self, rule_name):
        r"""Sets the rule_name of this RuleRiskStatisticsDto.

        规则名称

        :param rule_name: The rule_name of this RuleRiskStatisticsDto.
        :type rule_name: str
        """
        self._rule_name = rule_name

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
        if not isinstance(other, RuleRiskStatisticsDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
