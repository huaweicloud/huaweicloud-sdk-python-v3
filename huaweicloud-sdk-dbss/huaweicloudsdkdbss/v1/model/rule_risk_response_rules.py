# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RuleRiskResponseRules:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'type': 'str',
        'feature': 'str',
        'status': 'str',
        'rank': 'int',
        'risk_level': 'str',
        'rule_type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'type': 'type',
        'feature': 'feature',
        'status': 'status',
        'rank': 'rank',
        'risk_level': 'risk_level',
        'rule_type': 'rule_type'
    }

    def __init__(self, id=None, name=None, type=None, feature=None, status=None, rank=None, risk_level=None, rule_type=None):
        r"""RuleRiskResponseRules

        The model defined in huaweicloud sdk

        :param id: 风险规则ID
        :type id: str
        :param name: 风险规则名称
        :type name: str
        :param type: 风险规则类型
        :type type: str
        :param feature: 风险规则特征
        :type feature: str
        :param status: 风险规则状态。 - ON: 开启 - OFF: 关闭
        :type status: str
        :param rank: 风险规则优先级。数字越小优先级越高。
        :type rank: int
        :param risk_level: 风险级别 - LOW - MEDIUM - HIGH - NO_RISK]
        :type risk_level: str
        :param rule_type: 规则类型
        :type rule_type: str
        """
        
        

        self._id = None
        self._name = None
        self._type = None
        self._feature = None
        self._status = None
        self._rank = None
        self._risk_level = None
        self._rule_type = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.type = type
        if feature is not None:
            self.feature = feature
        self.status = status
        if rank is not None:
            self.rank = rank
        if risk_level is not None:
            self.risk_level = risk_level
        if rule_type is not None:
            self.rule_type = rule_type

    @property
    def id(self):
        r"""Gets the id of this RuleRiskResponseRules.

        风险规则ID

        :return: The id of this RuleRiskResponseRules.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this RuleRiskResponseRules.

        风险规则ID

        :param id: The id of this RuleRiskResponseRules.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this RuleRiskResponseRules.

        风险规则名称

        :return: The name of this RuleRiskResponseRules.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this RuleRiskResponseRules.

        风险规则名称

        :param name: The name of this RuleRiskResponseRules.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this RuleRiskResponseRules.

        风险规则类型

        :return: The type of this RuleRiskResponseRules.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this RuleRiskResponseRules.

        风险规则类型

        :param type: The type of this RuleRiskResponseRules.
        :type type: str
        """
        self._type = type

    @property
    def feature(self):
        r"""Gets the feature of this RuleRiskResponseRules.

        风险规则特征

        :return: The feature of this RuleRiskResponseRules.
        :rtype: str
        """
        return self._feature

    @feature.setter
    def feature(self, feature):
        r"""Sets the feature of this RuleRiskResponseRules.

        风险规则特征

        :param feature: The feature of this RuleRiskResponseRules.
        :type feature: str
        """
        self._feature = feature

    @property
    def status(self):
        r"""Gets the status of this RuleRiskResponseRules.

        风险规则状态。 - ON: 开启 - OFF: 关闭

        :return: The status of this RuleRiskResponseRules.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this RuleRiskResponseRules.

        风险规则状态。 - ON: 开启 - OFF: 关闭

        :param status: The status of this RuleRiskResponseRules.
        :type status: str
        """
        self._status = status

    @property
    def rank(self):
        r"""Gets the rank of this RuleRiskResponseRules.

        风险规则优先级。数字越小优先级越高。

        :return: The rank of this RuleRiskResponseRules.
        :rtype: int
        """
        return self._rank

    @rank.setter
    def rank(self, rank):
        r"""Sets the rank of this RuleRiskResponseRules.

        风险规则优先级。数字越小优先级越高。

        :param rank: The rank of this RuleRiskResponseRules.
        :type rank: int
        """
        self._rank = rank

    @property
    def risk_level(self):
        r"""Gets the risk_level of this RuleRiskResponseRules.

        风险级别 - LOW - MEDIUM - HIGH - NO_RISK]

        :return: The risk_level of this RuleRiskResponseRules.
        :rtype: str
        """
        return self._risk_level

    @risk_level.setter
    def risk_level(self, risk_level):
        r"""Sets the risk_level of this RuleRiskResponseRules.

        风险级别 - LOW - MEDIUM - HIGH - NO_RISK]

        :param risk_level: The risk_level of this RuleRiskResponseRules.
        :type risk_level: str
        """
        self._risk_level = risk_level

    @property
    def rule_type(self):
        r"""Gets the rule_type of this RuleRiskResponseRules.

        规则类型

        :return: The rule_type of this RuleRiskResponseRules.
        :rtype: str
        """
        return self._rule_type

    @rule_type.setter
    def rule_type(self, rule_type):
        r"""Sets the rule_type of this RuleRiskResponseRules.

        规则类型

        :param rule_type: The rule_type of this RuleRiskResponseRules.
        :type rule_type: str
        """
        self._rule_type = rule_type

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
        if not isinstance(other, RuleRiskResponseRules):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
