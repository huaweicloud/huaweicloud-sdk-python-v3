# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SecurityRiskResponseSecurityProtectRisk:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'un_open_protection_host_num': 'int',
        'deduct_score': 'float',
        'total_risk_num': 'int'
    }

    attribute_map = {
        'un_open_protection_host_num': 'un_open_protection_host_num',
        'deduct_score': 'deduct_score',
        'total_risk_num': 'total_risk_num'
    }

    def __init__(self, un_open_protection_host_num=None, deduct_score=None, total_risk_num=None):
        r"""SecurityRiskResponseSecurityProtectRisk

        The model defined in huaweicloud sdk

        :param un_open_protection_host_num: **参数解释**： 未开主机安全防护主机数 **取值范围**: 最小值0，最大值2147483647 
        :type un_open_protection_host_num: int
        :param deduct_score: **参数解释**： 扣分 **取值范围**: 最小值0，最大值10 
        :type deduct_score: float
        :param total_risk_num: **参数解释**： 风险总数 **取值范围**: 最小值0，最大值2147483647 
        :type total_risk_num: int
        """
        
        

        self._un_open_protection_host_num = None
        self._deduct_score = None
        self._total_risk_num = None
        self.discriminator = None

        if un_open_protection_host_num is not None:
            self.un_open_protection_host_num = un_open_protection_host_num
        if deduct_score is not None:
            self.deduct_score = deduct_score
        if total_risk_num is not None:
            self.total_risk_num = total_risk_num

    @property
    def un_open_protection_host_num(self):
        r"""Gets the un_open_protection_host_num of this SecurityRiskResponseSecurityProtectRisk.

        **参数解释**： 未开主机安全防护主机数 **取值范围**: 最小值0，最大值2147483647 

        :return: The un_open_protection_host_num of this SecurityRiskResponseSecurityProtectRisk.
        :rtype: int
        """
        return self._un_open_protection_host_num

    @un_open_protection_host_num.setter
    def un_open_protection_host_num(self, un_open_protection_host_num):
        r"""Sets the un_open_protection_host_num of this SecurityRiskResponseSecurityProtectRisk.

        **参数解释**： 未开主机安全防护主机数 **取值范围**: 最小值0，最大值2147483647 

        :param un_open_protection_host_num: The un_open_protection_host_num of this SecurityRiskResponseSecurityProtectRisk.
        :type un_open_protection_host_num: int
        """
        self._un_open_protection_host_num = un_open_protection_host_num

    @property
    def deduct_score(self):
        r"""Gets the deduct_score of this SecurityRiskResponseSecurityProtectRisk.

        **参数解释**： 扣分 **取值范围**: 最小值0，最大值10 

        :return: The deduct_score of this SecurityRiskResponseSecurityProtectRisk.
        :rtype: float
        """
        return self._deduct_score

    @deduct_score.setter
    def deduct_score(self, deduct_score):
        r"""Sets the deduct_score of this SecurityRiskResponseSecurityProtectRisk.

        **参数解释**： 扣分 **取值范围**: 最小值0，最大值10 

        :param deduct_score: The deduct_score of this SecurityRiskResponseSecurityProtectRisk.
        :type deduct_score: float
        """
        self._deduct_score = deduct_score

    @property
    def total_risk_num(self):
        r"""Gets the total_risk_num of this SecurityRiskResponseSecurityProtectRisk.

        **参数解释**： 风险总数 **取值范围**: 最小值0，最大值2147483647 

        :return: The total_risk_num of this SecurityRiskResponseSecurityProtectRisk.
        :rtype: int
        """
        return self._total_risk_num

    @total_risk_num.setter
    def total_risk_num(self, total_risk_num):
        r"""Sets the total_risk_num of this SecurityRiskResponseSecurityProtectRisk.

        **参数解释**： 风险总数 **取值范围**: 最小值0，最大值2147483647 

        :param total_risk_num: The total_risk_num of this SecurityRiskResponseSecurityProtectRisk.
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
        if not isinstance(other, SecurityRiskResponseSecurityProtectRisk):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
