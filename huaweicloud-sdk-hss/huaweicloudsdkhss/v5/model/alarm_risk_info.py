# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AlarmRiskInfo:

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
        'total_risk_num': 'int'
    }

    attribute_map = {
        'risk_list': 'risk_list',
        'deduct_score': 'deduct_score',
        'policy_list': 'policy_list',
        'total_risk_num': 'total_risk_num'
    }

    def __init__(self, risk_list=None, deduct_score=None, policy_list=None, total_risk_num=None):
        r"""AlarmRiskInfo

        The model defined in huaweicloud sdk

        :param risk_list: **参数解释**： 风险列表 **取值范围**: 最小值0，最大值4 
        :type risk_list: list[:class:`huaweicloudsdkhss.v5.RiskListInfo`]
        :param deduct_score: **参数解释**： 扣分 **取值范围**: 最小值0，最大值30 
        :type deduct_score: float
        :param policy_list: **参数解释**：  策略信息  **取值范围**:  最小值0，最大值32 
        :type policy_list: list[:class:`huaweicloudsdkhss.v5.PolicyInfo`]
        :param total_risk_num: **参数解释**： 风险总数 **取值范围**: 最小值0，最大值2147483647 
        :type total_risk_num: int
        """
        
        

        self._risk_list = None
        self._deduct_score = None
        self._policy_list = None
        self._total_risk_num = None
        self.discriminator = None

        if risk_list is not None:
            self.risk_list = risk_list
        if deduct_score is not None:
            self.deduct_score = deduct_score
        if policy_list is not None:
            self.policy_list = policy_list
        if total_risk_num is not None:
            self.total_risk_num = total_risk_num

    @property
    def risk_list(self):
        r"""Gets the risk_list of this AlarmRiskInfo.

        **参数解释**： 风险列表 **取值范围**: 最小值0，最大值4 

        :return: The risk_list of this AlarmRiskInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.RiskListInfo`]
        """
        return self._risk_list

    @risk_list.setter
    def risk_list(self, risk_list):
        r"""Sets the risk_list of this AlarmRiskInfo.

        **参数解释**： 风险列表 **取值范围**: 最小值0，最大值4 

        :param risk_list: The risk_list of this AlarmRiskInfo.
        :type risk_list: list[:class:`huaweicloudsdkhss.v5.RiskListInfo`]
        """
        self._risk_list = risk_list

    @property
    def deduct_score(self):
        r"""Gets the deduct_score of this AlarmRiskInfo.

        **参数解释**： 扣分 **取值范围**: 最小值0，最大值30 

        :return: The deduct_score of this AlarmRiskInfo.
        :rtype: float
        """
        return self._deduct_score

    @deduct_score.setter
    def deduct_score(self, deduct_score):
        r"""Sets the deduct_score of this AlarmRiskInfo.

        **参数解释**： 扣分 **取值范围**: 最小值0，最大值30 

        :param deduct_score: The deduct_score of this AlarmRiskInfo.
        :type deduct_score: float
        """
        self._deduct_score = deduct_score

    @property
    def policy_list(self):
        r"""Gets the policy_list of this AlarmRiskInfo.

        **参数解释**：  策略信息  **取值范围**:  最小值0，最大值32 

        :return: The policy_list of this AlarmRiskInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.PolicyInfo`]
        """
        return self._policy_list

    @policy_list.setter
    def policy_list(self, policy_list):
        r"""Sets the policy_list of this AlarmRiskInfo.

        **参数解释**：  策略信息  **取值范围**:  最小值0，最大值32 

        :param policy_list: The policy_list of this AlarmRiskInfo.
        :type policy_list: list[:class:`huaweicloudsdkhss.v5.PolicyInfo`]
        """
        self._policy_list = policy_list

    @property
    def total_risk_num(self):
        r"""Gets the total_risk_num of this AlarmRiskInfo.

        **参数解释**： 风险总数 **取值范围**: 最小值0，最大值2147483647 

        :return: The total_risk_num of this AlarmRiskInfo.
        :rtype: int
        """
        return self._total_risk_num

    @total_risk_num.setter
    def total_risk_num(self, total_risk_num):
        r"""Sets the total_risk_num of this AlarmRiskInfo.

        **参数解释**： 风险总数 **取值范围**: 最小值0，最大值2147483647 

        :param total_risk_num: The total_risk_num of this AlarmRiskInfo.
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
        if not isinstance(other, AlarmRiskInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
