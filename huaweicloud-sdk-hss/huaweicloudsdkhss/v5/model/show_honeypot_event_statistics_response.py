# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowHoneypotEventStatisticsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'risky_host_num': 'int',
        'protection_host_num': 'int',
        'critical_risky_num': 'int',
        'high_risky_num': 'int',
        'medium_risky_num': 'int',
        'low_risky_num': 'int'
    }

    attribute_map = {
        'risky_host_num': 'risky_host_num',
        'protection_host_num': 'protection_host_num',
        'critical_risky_num': 'critical_risky_num',
        'high_risky_num': 'high_risky_num',
        'medium_risky_num': 'medium_risky_num',
        'low_risky_num': 'low_risky_num'
    }

    def __init__(self, risky_host_num=None, protection_host_num=None, critical_risky_num=None, high_risky_num=None, medium_risky_num=None, low_risky_num=None):
        r"""ShowHoneypotEventStatisticsResponse

        The model defined in huaweicloud sdk

        :param risky_host_num: **参数解释**： 存在风险的服务器数量 **取值范围**： 最小值0，最大值2147483647 
        :type risky_host_num: int
        :param protection_host_num: **参数解释**： 防护服务器数量 **取值范围**： 最小值0，最大值2147483647 
        :type protection_host_num: int
        :param critical_risky_num: **参数解释**： 致命风险数量 **取值范围**： 最小值0，最大值2147483647 
        :type critical_risky_num: int
        :param high_risky_num: **参数解释**： 高危风险数量 **取值范围**： 最小值0，最大值2147483647 
        :type high_risky_num: int
        :param medium_risky_num: **参数解释**： 中危风险数量 **取值范围**： 最小值0，最大值2147483647 
        :type medium_risky_num: int
        :param low_risky_num: **参数解释**： 低危风险数量 **取值范围**： 最小值0，最大值2147483647 
        :type low_risky_num: int
        """
        
        super().__init__()

        self._risky_host_num = None
        self._protection_host_num = None
        self._critical_risky_num = None
        self._high_risky_num = None
        self._medium_risky_num = None
        self._low_risky_num = None
        self.discriminator = None

        if risky_host_num is not None:
            self.risky_host_num = risky_host_num
        if protection_host_num is not None:
            self.protection_host_num = protection_host_num
        if critical_risky_num is not None:
            self.critical_risky_num = critical_risky_num
        if high_risky_num is not None:
            self.high_risky_num = high_risky_num
        if medium_risky_num is not None:
            self.medium_risky_num = medium_risky_num
        if low_risky_num is not None:
            self.low_risky_num = low_risky_num

    @property
    def risky_host_num(self):
        r"""Gets the risky_host_num of this ShowHoneypotEventStatisticsResponse.

        **参数解释**： 存在风险的服务器数量 **取值范围**： 最小值0，最大值2147483647 

        :return: The risky_host_num of this ShowHoneypotEventStatisticsResponse.
        :rtype: int
        """
        return self._risky_host_num

    @risky_host_num.setter
    def risky_host_num(self, risky_host_num):
        r"""Sets the risky_host_num of this ShowHoneypotEventStatisticsResponse.

        **参数解释**： 存在风险的服务器数量 **取值范围**： 最小值0，最大值2147483647 

        :param risky_host_num: The risky_host_num of this ShowHoneypotEventStatisticsResponse.
        :type risky_host_num: int
        """
        self._risky_host_num = risky_host_num

    @property
    def protection_host_num(self):
        r"""Gets the protection_host_num of this ShowHoneypotEventStatisticsResponse.

        **参数解释**： 防护服务器数量 **取值范围**： 最小值0，最大值2147483647 

        :return: The protection_host_num of this ShowHoneypotEventStatisticsResponse.
        :rtype: int
        """
        return self._protection_host_num

    @protection_host_num.setter
    def protection_host_num(self, protection_host_num):
        r"""Sets the protection_host_num of this ShowHoneypotEventStatisticsResponse.

        **参数解释**： 防护服务器数量 **取值范围**： 最小值0，最大值2147483647 

        :param protection_host_num: The protection_host_num of this ShowHoneypotEventStatisticsResponse.
        :type protection_host_num: int
        """
        self._protection_host_num = protection_host_num

    @property
    def critical_risky_num(self):
        r"""Gets the critical_risky_num of this ShowHoneypotEventStatisticsResponse.

        **参数解释**： 致命风险数量 **取值范围**： 最小值0，最大值2147483647 

        :return: The critical_risky_num of this ShowHoneypotEventStatisticsResponse.
        :rtype: int
        """
        return self._critical_risky_num

    @critical_risky_num.setter
    def critical_risky_num(self, critical_risky_num):
        r"""Sets the critical_risky_num of this ShowHoneypotEventStatisticsResponse.

        **参数解释**： 致命风险数量 **取值范围**： 最小值0，最大值2147483647 

        :param critical_risky_num: The critical_risky_num of this ShowHoneypotEventStatisticsResponse.
        :type critical_risky_num: int
        """
        self._critical_risky_num = critical_risky_num

    @property
    def high_risky_num(self):
        r"""Gets the high_risky_num of this ShowHoneypotEventStatisticsResponse.

        **参数解释**： 高危风险数量 **取值范围**： 最小值0，最大值2147483647 

        :return: The high_risky_num of this ShowHoneypotEventStatisticsResponse.
        :rtype: int
        """
        return self._high_risky_num

    @high_risky_num.setter
    def high_risky_num(self, high_risky_num):
        r"""Sets the high_risky_num of this ShowHoneypotEventStatisticsResponse.

        **参数解释**： 高危风险数量 **取值范围**： 最小值0，最大值2147483647 

        :param high_risky_num: The high_risky_num of this ShowHoneypotEventStatisticsResponse.
        :type high_risky_num: int
        """
        self._high_risky_num = high_risky_num

    @property
    def medium_risky_num(self):
        r"""Gets the medium_risky_num of this ShowHoneypotEventStatisticsResponse.

        **参数解释**： 中危风险数量 **取值范围**： 最小值0，最大值2147483647 

        :return: The medium_risky_num of this ShowHoneypotEventStatisticsResponse.
        :rtype: int
        """
        return self._medium_risky_num

    @medium_risky_num.setter
    def medium_risky_num(self, medium_risky_num):
        r"""Sets the medium_risky_num of this ShowHoneypotEventStatisticsResponse.

        **参数解释**： 中危风险数量 **取值范围**： 最小值0，最大值2147483647 

        :param medium_risky_num: The medium_risky_num of this ShowHoneypotEventStatisticsResponse.
        :type medium_risky_num: int
        """
        self._medium_risky_num = medium_risky_num

    @property
    def low_risky_num(self):
        r"""Gets the low_risky_num of this ShowHoneypotEventStatisticsResponse.

        **参数解释**： 低危风险数量 **取值范围**： 最小值0，最大值2147483647 

        :return: The low_risky_num of this ShowHoneypotEventStatisticsResponse.
        :rtype: int
        """
        return self._low_risky_num

    @low_risky_num.setter
    def low_risky_num(self, low_risky_num):
        r"""Sets the low_risky_num of this ShowHoneypotEventStatisticsResponse.

        **参数解释**： 低危风险数量 **取值范围**： 最小值0，最大值2147483647 

        :param low_risky_num: The low_risky_num of this ShowHoneypotEventStatisticsResponse.
        :type low_risky_num: int
        """
        self._low_risky_num = low_risky_num

    def to_dict(self):
        import warnings
        warnings.warn("ShowHoneypotEventStatisticsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowHoneypotEventStatisticsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
