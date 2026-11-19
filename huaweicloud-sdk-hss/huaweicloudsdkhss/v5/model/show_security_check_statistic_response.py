# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSecurityCheckStatisticResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_host_num': 'int',
        'risk_host_num': 'int',
        'high_risk_host_num': 'int',
        'medium_risk_host_num': 'int',
        'low_risk_host_num': 'int',
        'safe_host_num': 'int'
    }

    attribute_map = {
        'total_host_num': 'total_host_num',
        'risk_host_num': 'risk_host_num',
        'high_risk_host_num': 'high_risk_host_num',
        'medium_risk_host_num': 'medium_risk_host_num',
        'low_risk_host_num': 'low_risk_host_num',
        'safe_host_num': 'safe_host_num'
    }

    def __init__(self, total_host_num=None, risk_host_num=None, high_risk_host_num=None, medium_risk_host_num=None, low_risk_host_num=None, safe_host_num=None):
        r"""ShowSecurityCheckStatisticResponse

        The model defined in huaweicloud sdk

        :param total_host_num: **参数解释**: 本次体检服务器数量 **取值范围**: 最小值0，最大值2147483647 
        :type total_host_num: int
        :param risk_host_num: **参数解释**: 有安全风险的服务器数量 **取值范围**: 最小值0，最大值2147483647 
        :type risk_host_num: int
        :param high_risk_host_num: **参数解释**: 高危风险的服务器数量 **取值范围**: 最小值0，最大值2147483647 
        :type high_risk_host_num: int
        :param medium_risk_host_num: **参数解释**: 中危风险的服务器数量 **取值范围**: 最小值0，最大值2147483647 
        :type medium_risk_host_num: int
        :param low_risk_host_num: **参数解释**: 低危风险的服务器数量 **取值范围**: 最小值0，最大值2147483647 
        :type low_risk_host_num: int
        :param safe_host_num: **参数解释**: 无风险的服务器数量 **取值范围**: 最小值0，最大值2147483647 
        :type safe_host_num: int
        """
        
        super().__init__()

        self._total_host_num = None
        self._risk_host_num = None
        self._high_risk_host_num = None
        self._medium_risk_host_num = None
        self._low_risk_host_num = None
        self._safe_host_num = None
        self.discriminator = None

        if total_host_num is not None:
            self.total_host_num = total_host_num
        if risk_host_num is not None:
            self.risk_host_num = risk_host_num
        if high_risk_host_num is not None:
            self.high_risk_host_num = high_risk_host_num
        if medium_risk_host_num is not None:
            self.medium_risk_host_num = medium_risk_host_num
        if low_risk_host_num is not None:
            self.low_risk_host_num = low_risk_host_num
        if safe_host_num is not None:
            self.safe_host_num = safe_host_num

    @property
    def total_host_num(self):
        r"""Gets the total_host_num of this ShowSecurityCheckStatisticResponse.

        **参数解释**: 本次体检服务器数量 **取值范围**: 最小值0，最大值2147483647 

        :return: The total_host_num of this ShowSecurityCheckStatisticResponse.
        :rtype: int
        """
        return self._total_host_num

    @total_host_num.setter
    def total_host_num(self, total_host_num):
        r"""Sets the total_host_num of this ShowSecurityCheckStatisticResponse.

        **参数解释**: 本次体检服务器数量 **取值范围**: 最小值0，最大值2147483647 

        :param total_host_num: The total_host_num of this ShowSecurityCheckStatisticResponse.
        :type total_host_num: int
        """
        self._total_host_num = total_host_num

    @property
    def risk_host_num(self):
        r"""Gets the risk_host_num of this ShowSecurityCheckStatisticResponse.

        **参数解释**: 有安全风险的服务器数量 **取值范围**: 最小值0，最大值2147483647 

        :return: The risk_host_num of this ShowSecurityCheckStatisticResponse.
        :rtype: int
        """
        return self._risk_host_num

    @risk_host_num.setter
    def risk_host_num(self, risk_host_num):
        r"""Sets the risk_host_num of this ShowSecurityCheckStatisticResponse.

        **参数解释**: 有安全风险的服务器数量 **取值范围**: 最小值0，最大值2147483647 

        :param risk_host_num: The risk_host_num of this ShowSecurityCheckStatisticResponse.
        :type risk_host_num: int
        """
        self._risk_host_num = risk_host_num

    @property
    def high_risk_host_num(self):
        r"""Gets the high_risk_host_num of this ShowSecurityCheckStatisticResponse.

        **参数解释**: 高危风险的服务器数量 **取值范围**: 最小值0，最大值2147483647 

        :return: The high_risk_host_num of this ShowSecurityCheckStatisticResponse.
        :rtype: int
        """
        return self._high_risk_host_num

    @high_risk_host_num.setter
    def high_risk_host_num(self, high_risk_host_num):
        r"""Sets the high_risk_host_num of this ShowSecurityCheckStatisticResponse.

        **参数解释**: 高危风险的服务器数量 **取值范围**: 最小值0，最大值2147483647 

        :param high_risk_host_num: The high_risk_host_num of this ShowSecurityCheckStatisticResponse.
        :type high_risk_host_num: int
        """
        self._high_risk_host_num = high_risk_host_num

    @property
    def medium_risk_host_num(self):
        r"""Gets the medium_risk_host_num of this ShowSecurityCheckStatisticResponse.

        **参数解释**: 中危风险的服务器数量 **取值范围**: 最小值0，最大值2147483647 

        :return: The medium_risk_host_num of this ShowSecurityCheckStatisticResponse.
        :rtype: int
        """
        return self._medium_risk_host_num

    @medium_risk_host_num.setter
    def medium_risk_host_num(self, medium_risk_host_num):
        r"""Sets the medium_risk_host_num of this ShowSecurityCheckStatisticResponse.

        **参数解释**: 中危风险的服务器数量 **取值范围**: 最小值0，最大值2147483647 

        :param medium_risk_host_num: The medium_risk_host_num of this ShowSecurityCheckStatisticResponse.
        :type medium_risk_host_num: int
        """
        self._medium_risk_host_num = medium_risk_host_num

    @property
    def low_risk_host_num(self):
        r"""Gets the low_risk_host_num of this ShowSecurityCheckStatisticResponse.

        **参数解释**: 低危风险的服务器数量 **取值范围**: 最小值0，最大值2147483647 

        :return: The low_risk_host_num of this ShowSecurityCheckStatisticResponse.
        :rtype: int
        """
        return self._low_risk_host_num

    @low_risk_host_num.setter
    def low_risk_host_num(self, low_risk_host_num):
        r"""Sets the low_risk_host_num of this ShowSecurityCheckStatisticResponse.

        **参数解释**: 低危风险的服务器数量 **取值范围**: 最小值0，最大值2147483647 

        :param low_risk_host_num: The low_risk_host_num of this ShowSecurityCheckStatisticResponse.
        :type low_risk_host_num: int
        """
        self._low_risk_host_num = low_risk_host_num

    @property
    def safe_host_num(self):
        r"""Gets the safe_host_num of this ShowSecurityCheckStatisticResponse.

        **参数解释**: 无风险的服务器数量 **取值范围**: 最小值0，最大值2147483647 

        :return: The safe_host_num of this ShowSecurityCheckStatisticResponse.
        :rtype: int
        """
        return self._safe_host_num

    @safe_host_num.setter
    def safe_host_num(self, safe_host_num):
        r"""Sets the safe_host_num of this ShowSecurityCheckStatisticResponse.

        **参数解释**: 无风险的服务器数量 **取值范围**: 最小值0，最大值2147483647 

        :param safe_host_num: The safe_host_num of this ShowSecurityCheckStatisticResponse.
        :type safe_host_num: int
        """
        self._safe_host_num = safe_host_num

    def to_dict(self):
        import warnings
        warnings.warn("ShowSecurityCheckStatisticResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ShowSecurityCheckStatisticResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
