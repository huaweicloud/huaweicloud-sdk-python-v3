# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RiskListInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'severity': 'str',
        'risk_num': 'int',
        'effected_host_num': 'int'
    }

    attribute_map = {
        'severity': 'severity',
        'risk_num': 'risk_num',
        'effected_host_num': 'effected_host_num'
    }

    def __init__(self, severity=None, risk_num=None, effected_host_num=None):
        r"""RiskListInfo

        The model defined in huaweicloud sdk

        :param severity: **参数解释**： 风险级别 **取值范围**: 字符长度0-32位 
        :type severity: str
        :param risk_num: **参数解释**： 风险数量 **取值范围**: 最小值0，最大值2147483647 
        :type risk_num: int
        :param effected_host_num: **参数解释**： 受影响资产数量 **取值范围**: 最小值0，最大值2147483647 
        :type effected_host_num: int
        """
        
        

        self._severity = None
        self._risk_num = None
        self._effected_host_num = None
        self.discriminator = None

        if severity is not None:
            self.severity = severity
        if risk_num is not None:
            self.risk_num = risk_num
        if effected_host_num is not None:
            self.effected_host_num = effected_host_num

    @property
    def severity(self):
        r"""Gets the severity of this RiskListInfo.

        **参数解释**： 风险级别 **取值范围**: 字符长度0-32位 

        :return: The severity of this RiskListInfo.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        r"""Sets the severity of this RiskListInfo.

        **参数解释**： 风险级别 **取值范围**: 字符长度0-32位 

        :param severity: The severity of this RiskListInfo.
        :type severity: str
        """
        self._severity = severity

    @property
    def risk_num(self):
        r"""Gets the risk_num of this RiskListInfo.

        **参数解释**： 风险数量 **取值范围**: 最小值0，最大值2147483647 

        :return: The risk_num of this RiskListInfo.
        :rtype: int
        """
        return self._risk_num

    @risk_num.setter
    def risk_num(self, risk_num):
        r"""Sets the risk_num of this RiskListInfo.

        **参数解释**： 风险数量 **取值范围**: 最小值0，最大值2147483647 

        :param risk_num: The risk_num of this RiskListInfo.
        :type risk_num: int
        """
        self._risk_num = risk_num

    @property
    def effected_host_num(self):
        r"""Gets the effected_host_num of this RiskListInfo.

        **参数解释**： 受影响资产数量 **取值范围**: 最小值0，最大值2147483647 

        :return: The effected_host_num of this RiskListInfo.
        :rtype: int
        """
        return self._effected_host_num

    @effected_host_num.setter
    def effected_host_num(self, effected_host_num):
        r"""Sets the effected_host_num of this RiskListInfo.

        **参数解释**： 受影响资产数量 **取值范围**: 最小值0，最大值2147483647 

        :param effected_host_num: The effected_host_num of this RiskListInfo.
        :type effected_host_num: int
        """
        self._effected_host_num = effected_host_num

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
        if not isinstance(other, RiskListInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
