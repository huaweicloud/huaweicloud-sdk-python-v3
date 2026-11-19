# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ContainerRiskInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'baseline_risk_num': 'int',
        'vul_total_num': 'int',
        'critical_vul_num': 'int'
    }

    attribute_map = {
        'baseline_risk_num': 'baseline_risk_num',
        'vul_total_num': 'vul_total_num',
        'critical_vul_num': 'critical_vul_num'
    }

    def __init__(self, baseline_risk_num=None, vul_total_num=None, critical_vul_num=None):
        r"""ContainerRiskInfo

        The model defined in huaweicloud sdk

        :param baseline_risk_num: **参数解释**: 基线风险数量 **取值范围**: 最小值0，最大值2147483647 
        :type baseline_risk_num: int
        :param vul_total_num: **参数解释**: 漏洞总数 **取值范围**: 最小值0，最大值2147483647 
        :type vul_total_num: int
        :param critical_vul_num: **参数解释**: 紧急漏洞数量 **取值范围**: 最小值0，最大值2147483647 
        :type critical_vul_num: int
        """
        
        

        self._baseline_risk_num = None
        self._vul_total_num = None
        self._critical_vul_num = None
        self.discriminator = None

        if baseline_risk_num is not None:
            self.baseline_risk_num = baseline_risk_num
        if vul_total_num is not None:
            self.vul_total_num = vul_total_num
        if critical_vul_num is not None:
            self.critical_vul_num = critical_vul_num

    @property
    def baseline_risk_num(self):
        r"""Gets the baseline_risk_num of this ContainerRiskInfo.

        **参数解释**: 基线风险数量 **取值范围**: 最小值0，最大值2147483647 

        :return: The baseline_risk_num of this ContainerRiskInfo.
        :rtype: int
        """
        return self._baseline_risk_num

    @baseline_risk_num.setter
    def baseline_risk_num(self, baseline_risk_num):
        r"""Sets the baseline_risk_num of this ContainerRiskInfo.

        **参数解释**: 基线风险数量 **取值范围**: 最小值0，最大值2147483647 

        :param baseline_risk_num: The baseline_risk_num of this ContainerRiskInfo.
        :type baseline_risk_num: int
        """
        self._baseline_risk_num = baseline_risk_num

    @property
    def vul_total_num(self):
        r"""Gets the vul_total_num of this ContainerRiskInfo.

        **参数解释**: 漏洞总数 **取值范围**: 最小值0，最大值2147483647 

        :return: The vul_total_num of this ContainerRiskInfo.
        :rtype: int
        """
        return self._vul_total_num

    @vul_total_num.setter
    def vul_total_num(self, vul_total_num):
        r"""Sets the vul_total_num of this ContainerRiskInfo.

        **参数解释**: 漏洞总数 **取值范围**: 最小值0，最大值2147483647 

        :param vul_total_num: The vul_total_num of this ContainerRiskInfo.
        :type vul_total_num: int
        """
        self._vul_total_num = vul_total_num

    @property
    def critical_vul_num(self):
        r"""Gets the critical_vul_num of this ContainerRiskInfo.

        **参数解释**: 紧急漏洞数量 **取值范围**: 最小值0，最大值2147483647 

        :return: The critical_vul_num of this ContainerRiskInfo.
        :rtype: int
        """
        return self._critical_vul_num

    @critical_vul_num.setter
    def critical_vul_num(self, critical_vul_num):
        r"""Sets the critical_vul_num of this ContainerRiskInfo.

        **参数解释**: 紧急漏洞数量 **取值范围**: 最小值0，最大值2147483647 

        :param critical_vul_num: The critical_vul_num of this ContainerRiskInfo.
        :type critical_vul_num: int
        """
        self._critical_vul_num = critical_vul_num

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ContainerRiskInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
