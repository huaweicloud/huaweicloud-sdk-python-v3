# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAuditRuleRisksNewRequest:

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
        'name': 'str',
        'risk_levels': 'str',
        'support_db_classify_rule': 'bool'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'name': 'name',
        'risk_levels': 'risk_levels',
        'support_db_classify_rule': 'support_db_classify_rule'
    }

    def __init__(self, instance_id=None, name=None, risk_levels=None, support_db_classify_rule=None):
        r"""ListAuditRuleRisksNewRequest

        The model defined in huaweicloud sdk

        :param instance_id: **参数解释**： 实例ID。可通过查询实例列表接口ID字段获取 **约束限制**： 不涉及 **取值范围**： 以查询实例列表接口值为准，字符长度32-64。 **默认取值**： 不涉及 
        :type instance_id: str
        :param name: 风险名称
        :type name: str
        :param risk_levels: **参数解释**： 风险级别 **约束限制**： 以取值范围为准 **取值范围**： - LOW：低风险 - MEDIUM：中风险 - HIGH：高风险 - NO_RISK：无风险 **默认取值**： 不涉及 
        :type risk_levels: str
        :param support_db_classify_rule: **参数解释**： 实例前端是否支持按数据库类型展示风险规则 **约束限制**： 以取值范围为准 **取值范围**： - true: 支持 - false: 不支持 **默认取值**： false: 不支持 
        :type support_db_classify_rule: bool
        """
        
        

        self._instance_id = None
        self._name = None
        self._risk_levels = None
        self._support_db_classify_rule = None
        self.discriminator = None

        self.instance_id = instance_id
        if name is not None:
            self.name = name
        if risk_levels is not None:
            self.risk_levels = risk_levels
        if support_db_classify_rule is not None:
            self.support_db_classify_rule = support_db_classify_rule

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListAuditRuleRisksNewRequest.

        **参数解释**： 实例ID。可通过查询实例列表接口ID字段获取 **约束限制**： 不涉及 **取值范围**： 以查询实例列表接口值为准，字符长度32-64。 **默认取值**： 不涉及 

        :return: The instance_id of this ListAuditRuleRisksNewRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListAuditRuleRisksNewRequest.

        **参数解释**： 实例ID。可通过查询实例列表接口ID字段获取 **约束限制**： 不涉及 **取值范围**： 以查询实例列表接口值为准，字符长度32-64。 **默认取值**： 不涉及 

        :param instance_id: The instance_id of this ListAuditRuleRisksNewRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def name(self):
        r"""Gets the name of this ListAuditRuleRisksNewRequest.

        风险名称

        :return: The name of this ListAuditRuleRisksNewRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListAuditRuleRisksNewRequest.

        风险名称

        :param name: The name of this ListAuditRuleRisksNewRequest.
        :type name: str
        """
        self._name = name

    @property
    def risk_levels(self):
        r"""Gets the risk_levels of this ListAuditRuleRisksNewRequest.

        **参数解释**： 风险级别 **约束限制**： 以取值范围为准 **取值范围**： - LOW：低风险 - MEDIUM：中风险 - HIGH：高风险 - NO_RISK：无风险 **默认取值**： 不涉及 

        :return: The risk_levels of this ListAuditRuleRisksNewRequest.
        :rtype: str
        """
        return self._risk_levels

    @risk_levels.setter
    def risk_levels(self, risk_levels):
        r"""Sets the risk_levels of this ListAuditRuleRisksNewRequest.

        **参数解释**： 风险级别 **约束限制**： 以取值范围为准 **取值范围**： - LOW：低风险 - MEDIUM：中风险 - HIGH：高风险 - NO_RISK：无风险 **默认取值**： 不涉及 

        :param risk_levels: The risk_levels of this ListAuditRuleRisksNewRequest.
        :type risk_levels: str
        """
        self._risk_levels = risk_levels

    @property
    def support_db_classify_rule(self):
        r"""Gets the support_db_classify_rule of this ListAuditRuleRisksNewRequest.

        **参数解释**： 实例前端是否支持按数据库类型展示风险规则 **约束限制**： 以取值范围为准 **取值范围**： - true: 支持 - false: 不支持 **默认取值**： false: 不支持 

        :return: The support_db_classify_rule of this ListAuditRuleRisksNewRequest.
        :rtype: bool
        """
        return self._support_db_classify_rule

    @support_db_classify_rule.setter
    def support_db_classify_rule(self, support_db_classify_rule):
        r"""Sets the support_db_classify_rule of this ListAuditRuleRisksNewRequest.

        **参数解释**： 实例前端是否支持按数据库类型展示风险规则 **约束限制**： 以取值范围为准 **取值范围**： - true: 支持 - false: 不支持 **默认取值**： false: 不支持 

        :param support_db_classify_rule: The support_db_classify_rule of this ListAuditRuleRisksNewRequest.
        :type support_db_classify_rule: bool
        """
        self._support_db_classify_rule = support_db_classify_rule

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
        if not isinstance(other, ListAuditRuleRisksNewRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
