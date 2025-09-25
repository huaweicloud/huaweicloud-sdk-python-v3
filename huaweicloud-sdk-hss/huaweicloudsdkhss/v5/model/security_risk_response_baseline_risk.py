# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SecurityRiskResponseBaselineRisk:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'risk_list': 'list[RiskListInfo]',
        'deduct_score': 'float',
        'policy_list': 'list[PolicyInfo]',
        'existed_pwd_host_num': 'int',
        'un_scanned_baseline_host_num': 'int',
        'total_risk_num': 'int'
    }

    attribute_map = {
        'risk_list': 'risk_list',
        'deduct_score': 'deduct_score',
        'policy_list': 'policy_list',
        'existed_pwd_host_num': 'existed_pwd_host_num',
        'un_scanned_baseline_host_num': 'un_scanned_baseline_host_num',
        'total_risk_num': 'total_risk_num'
    }

    def __init__(self, risk_list=None, deduct_score=None, policy_list=None, existed_pwd_host_num=None, un_scanned_baseline_host_num=None, total_risk_num=None):
        r"""SecurityRiskResponseBaselineRisk

        The model defined in huaweicloud sdk

        :param risk_list: **参数解释**： 基线风险列表 **取值范围**: 最小值0，最大值4 
        :type risk_list: list[:class:`huaweicloudsdkhss.v5.RiskListInfo`]
        :param deduct_score: **参数解释**： 扣分 **取值范围**: 最小值0，最大值20 
        :type deduct_score: float
        :param policy_list: **参数解释**： 未开启的策略列表 **取值范围**: 最小值0，最大值32 
        :type policy_list: list[:class:`huaweicloudsdkhss.v5.PolicyInfo`]
        :param existed_pwd_host_num: **参数解释**： 存在弱口令主机数量 **取值范围**: 最小值0，最大值2147483647 
        :type existed_pwd_host_num: int
        :param un_scanned_baseline_host_num: **参数解释**： 未进行基线配置检查的主机数 **取值范围**: 最小值0，最大值2147483647 
        :type un_scanned_baseline_host_num: int
        :param total_risk_num: **参数解释**： 风险总数 **取值范围**: 最小值0，最大值2147483647 
        :type total_risk_num: int
        """
        
        

        self._risk_list = None
        self._deduct_score = None
        self._policy_list = None
        self._existed_pwd_host_num = None
        self._un_scanned_baseline_host_num = None
        self._total_risk_num = None
        self.discriminator = None

        if risk_list is not None:
            self.risk_list = risk_list
        if deduct_score is not None:
            self.deduct_score = deduct_score
        if policy_list is not None:
            self.policy_list = policy_list
        if existed_pwd_host_num is not None:
            self.existed_pwd_host_num = existed_pwd_host_num
        if un_scanned_baseline_host_num is not None:
            self.un_scanned_baseline_host_num = un_scanned_baseline_host_num
        if total_risk_num is not None:
            self.total_risk_num = total_risk_num

    @property
    def risk_list(self):
        r"""Gets the risk_list of this SecurityRiskResponseBaselineRisk.

        **参数解释**： 基线风险列表 **取值范围**: 最小值0，最大值4 

        :return: The risk_list of this SecurityRiskResponseBaselineRisk.
        :rtype: list[:class:`huaweicloudsdkhss.v5.RiskListInfo`]
        """
        return self._risk_list

    @risk_list.setter
    def risk_list(self, risk_list):
        r"""Sets the risk_list of this SecurityRiskResponseBaselineRisk.

        **参数解释**： 基线风险列表 **取值范围**: 最小值0，最大值4 

        :param risk_list: The risk_list of this SecurityRiskResponseBaselineRisk.
        :type risk_list: list[:class:`huaweicloudsdkhss.v5.RiskListInfo`]
        """
        self._risk_list = risk_list

    @property
    def deduct_score(self):
        r"""Gets the deduct_score of this SecurityRiskResponseBaselineRisk.

        **参数解释**： 扣分 **取值范围**: 最小值0，最大值20 

        :return: The deduct_score of this SecurityRiskResponseBaselineRisk.
        :rtype: float
        """
        return self._deduct_score

    @deduct_score.setter
    def deduct_score(self, deduct_score):
        r"""Sets the deduct_score of this SecurityRiskResponseBaselineRisk.

        **参数解释**： 扣分 **取值范围**: 最小值0，最大值20 

        :param deduct_score: The deduct_score of this SecurityRiskResponseBaselineRisk.
        :type deduct_score: float
        """
        self._deduct_score = deduct_score

    @property
    def policy_list(self):
        r"""Gets the policy_list of this SecurityRiskResponseBaselineRisk.

        **参数解释**： 未开启的策略列表 **取值范围**: 最小值0，最大值32 

        :return: The policy_list of this SecurityRiskResponseBaselineRisk.
        :rtype: list[:class:`huaweicloudsdkhss.v5.PolicyInfo`]
        """
        return self._policy_list

    @policy_list.setter
    def policy_list(self, policy_list):
        r"""Sets the policy_list of this SecurityRiskResponseBaselineRisk.

        **参数解释**： 未开启的策略列表 **取值范围**: 最小值0，最大值32 

        :param policy_list: The policy_list of this SecurityRiskResponseBaselineRisk.
        :type policy_list: list[:class:`huaweicloudsdkhss.v5.PolicyInfo`]
        """
        self._policy_list = policy_list

    @property
    def existed_pwd_host_num(self):
        r"""Gets the existed_pwd_host_num of this SecurityRiskResponseBaselineRisk.

        **参数解释**： 存在弱口令主机数量 **取值范围**: 最小值0，最大值2147483647 

        :return: The existed_pwd_host_num of this SecurityRiskResponseBaselineRisk.
        :rtype: int
        """
        return self._existed_pwd_host_num

    @existed_pwd_host_num.setter
    def existed_pwd_host_num(self, existed_pwd_host_num):
        r"""Sets the existed_pwd_host_num of this SecurityRiskResponseBaselineRisk.

        **参数解释**： 存在弱口令主机数量 **取值范围**: 最小值0，最大值2147483647 

        :param existed_pwd_host_num: The existed_pwd_host_num of this SecurityRiskResponseBaselineRisk.
        :type existed_pwd_host_num: int
        """
        self._existed_pwd_host_num = existed_pwd_host_num

    @property
    def un_scanned_baseline_host_num(self):
        r"""Gets the un_scanned_baseline_host_num of this SecurityRiskResponseBaselineRisk.

        **参数解释**： 未进行基线配置检查的主机数 **取值范围**: 最小值0，最大值2147483647 

        :return: The un_scanned_baseline_host_num of this SecurityRiskResponseBaselineRisk.
        :rtype: int
        """
        return self._un_scanned_baseline_host_num

    @un_scanned_baseline_host_num.setter
    def un_scanned_baseline_host_num(self, un_scanned_baseline_host_num):
        r"""Sets the un_scanned_baseline_host_num of this SecurityRiskResponseBaselineRisk.

        **参数解释**： 未进行基线配置检查的主机数 **取值范围**: 最小值0，最大值2147483647 

        :param un_scanned_baseline_host_num: The un_scanned_baseline_host_num of this SecurityRiskResponseBaselineRisk.
        :type un_scanned_baseline_host_num: int
        """
        self._un_scanned_baseline_host_num = un_scanned_baseline_host_num

    @property
    def total_risk_num(self):
        r"""Gets the total_risk_num of this SecurityRiskResponseBaselineRisk.

        **参数解释**： 风险总数 **取值范围**: 最小值0，最大值2147483647 

        :return: The total_risk_num of this SecurityRiskResponseBaselineRisk.
        :rtype: int
        """
        return self._total_risk_num

    @total_risk_num.setter
    def total_risk_num(self, total_risk_num):
        r"""Sets the total_risk_num of this SecurityRiskResponseBaselineRisk.

        **参数解释**： 风险总数 **取值范围**: 最小值0，最大值2147483647 

        :param total_risk_num: The total_risk_num of this SecurityRiskResponseBaselineRisk.
        :type total_risk_num: int
        """
        self._total_risk_num = total_risk_num

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
        if not isinstance(other, SecurityRiskResponseBaselineRisk):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
