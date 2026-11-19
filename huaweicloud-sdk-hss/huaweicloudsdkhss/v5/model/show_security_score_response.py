# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSecurityScoreResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'security_risk_num': 'int',
        'security_score': 'float',
        'detect_time': 'int',
        'free_health_check_total_host_num': 'int'
    }

    attribute_map = {
        'security_risk_num': 'security_risk_num',
        'security_score': 'security_score',
        'detect_time': 'detect_time',
        'free_health_check_total_host_num': 'free_health_check_total_host_num'
    }

    def __init__(self, security_risk_num=None, security_score=None, detect_time=None, free_health_check_total_host_num=None):
        r"""ShowSecurityScoreResponse

        The model defined in huaweicloud sdk

        :param security_risk_num: **参数解释**: 安全风险总数 **取值范围**: 最小值0，最大值2147483647 
        :type security_risk_num: int
        :param security_score: **参数解释**: 安全评分 **取值范围**: 最小值0，最大值100 
        :type security_score: float
        :param detect_time: **参数解释**: 更新时间，毫秒级时间戳 **取值范围**: 最小值0，最大值9223372036854775807 
        :type detect_time: int
        :param free_health_check_total_host_num: **参数解释**: 免费体检主机数 **取值范围**: 最小值0，最大值2147483647 
        :type free_health_check_total_host_num: int
        """
        
        super().__init__()

        self._security_risk_num = None
        self._security_score = None
        self._detect_time = None
        self._free_health_check_total_host_num = None
        self.discriminator = None

        if security_risk_num is not None:
            self.security_risk_num = security_risk_num
        if security_score is not None:
            self.security_score = security_score
        if detect_time is not None:
            self.detect_time = detect_time
        if free_health_check_total_host_num is not None:
            self.free_health_check_total_host_num = free_health_check_total_host_num

    @property
    def security_risk_num(self):
        r"""Gets the security_risk_num of this ShowSecurityScoreResponse.

        **参数解释**: 安全风险总数 **取值范围**: 最小值0，最大值2147483647 

        :return: The security_risk_num of this ShowSecurityScoreResponse.
        :rtype: int
        """
        return self._security_risk_num

    @security_risk_num.setter
    def security_risk_num(self, security_risk_num):
        r"""Sets the security_risk_num of this ShowSecurityScoreResponse.

        **参数解释**: 安全风险总数 **取值范围**: 最小值0，最大值2147483647 

        :param security_risk_num: The security_risk_num of this ShowSecurityScoreResponse.
        :type security_risk_num: int
        """
        self._security_risk_num = security_risk_num

    @property
    def security_score(self):
        r"""Gets the security_score of this ShowSecurityScoreResponse.

        **参数解释**: 安全评分 **取值范围**: 最小值0，最大值100 

        :return: The security_score of this ShowSecurityScoreResponse.
        :rtype: float
        """
        return self._security_score

    @security_score.setter
    def security_score(self, security_score):
        r"""Sets the security_score of this ShowSecurityScoreResponse.

        **参数解释**: 安全评分 **取值范围**: 最小值0，最大值100 

        :param security_score: The security_score of this ShowSecurityScoreResponse.
        :type security_score: float
        """
        self._security_score = security_score

    @property
    def detect_time(self):
        r"""Gets the detect_time of this ShowSecurityScoreResponse.

        **参数解释**: 更新时间，毫秒级时间戳 **取值范围**: 最小值0，最大值9223372036854775807 

        :return: The detect_time of this ShowSecurityScoreResponse.
        :rtype: int
        """
        return self._detect_time

    @detect_time.setter
    def detect_time(self, detect_time):
        r"""Sets the detect_time of this ShowSecurityScoreResponse.

        **参数解释**: 更新时间，毫秒级时间戳 **取值范围**: 最小值0，最大值9223372036854775807 

        :param detect_time: The detect_time of this ShowSecurityScoreResponse.
        :type detect_time: int
        """
        self._detect_time = detect_time

    @property
    def free_health_check_total_host_num(self):
        r"""Gets the free_health_check_total_host_num of this ShowSecurityScoreResponse.

        **参数解释**: 免费体检主机数 **取值范围**: 最小值0，最大值2147483647 

        :return: The free_health_check_total_host_num of this ShowSecurityScoreResponse.
        :rtype: int
        """
        return self._free_health_check_total_host_num

    @free_health_check_total_host_num.setter
    def free_health_check_total_host_num(self, free_health_check_total_host_num):
        r"""Sets the free_health_check_total_host_num of this ShowSecurityScoreResponse.

        **参数解释**: 免费体检主机数 **取值范围**: 最小值0，最大值2147483647 

        :param free_health_check_total_host_num: The free_health_check_total_host_num of this ShowSecurityScoreResponse.
        :type free_health_check_total_host_num: int
        """
        self._free_health_check_total_host_num = free_health_check_total_host_num

    def to_dict(self):
        import warnings
        warnings.warn("ShowSecurityScoreResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowSecurityScoreResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
