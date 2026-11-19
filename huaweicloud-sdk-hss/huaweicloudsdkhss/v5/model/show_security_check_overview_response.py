# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSecurityCheckOverviewResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'risk_rating': 'int',
        'severity': 'str',
        'scan_time': 'int',
        'host_num': 'int',
        'risk_num': 'int',
        'scheduled_check_status': 'bool'
    }

    attribute_map = {
        'risk_rating': 'risk_rating',
        'severity': 'severity',
        'scan_time': 'scan_time',
        'host_num': 'host_num',
        'risk_num': 'risk_num',
        'scheduled_check_status': 'scheduled_check_status'
    }

    def __init__(self, risk_rating=None, severity=None, scan_time=None, host_num=None, risk_num=None, scheduled_check_status=None):
        r"""ShowSecurityCheckOverviewResponse

        The model defined in huaweicloud sdk

        :param risk_rating: **参数解释**: 风险评分 **取值范围**: 最小值0，最大值100 
        :type risk_rating: int
        :param severity: **参数解释**: 风险级别 **取值范围**: - Security：安全 - Low：低危 - Medium：中危 - High：高危 
        :type severity: str
        :param scan_time: **参数解释**: 最新检测时间，毫秒级时间戳 **取值范围**: 最小值0，最大值9223372036854775807（UTC时区，从1970-01-01 00:00:00开始计算） 
        :type scan_time: int
        :param host_num: **参数解释**: 防护的服务器数量 **取值范围**: 最小值0，最大值2000000 
        :type host_num: int
        :param risk_num: **参数解释**: 安全风险数量 **取值范围**: 最小值0，最大值2147483647 
        :type risk_num: int
        :param scheduled_check_status: **参数解释**: 定时体检开启状态 **取值范围**: - true：已开启 - false：未开启 
        :type scheduled_check_status: bool
        """
        
        super().__init__()

        self._risk_rating = None
        self._severity = None
        self._scan_time = None
        self._host_num = None
        self._risk_num = None
        self._scheduled_check_status = None
        self.discriminator = None

        if risk_rating is not None:
            self.risk_rating = risk_rating
        if severity is not None:
            self.severity = severity
        if scan_time is not None:
            self.scan_time = scan_time
        if host_num is not None:
            self.host_num = host_num
        if risk_num is not None:
            self.risk_num = risk_num
        if scheduled_check_status is not None:
            self.scheduled_check_status = scheduled_check_status

    @property
    def risk_rating(self):
        r"""Gets the risk_rating of this ShowSecurityCheckOverviewResponse.

        **参数解释**: 风险评分 **取值范围**: 最小值0，最大值100 

        :return: The risk_rating of this ShowSecurityCheckOverviewResponse.
        :rtype: int
        """
        return self._risk_rating

    @risk_rating.setter
    def risk_rating(self, risk_rating):
        r"""Sets the risk_rating of this ShowSecurityCheckOverviewResponse.

        **参数解释**: 风险评分 **取值范围**: 最小值0，最大值100 

        :param risk_rating: The risk_rating of this ShowSecurityCheckOverviewResponse.
        :type risk_rating: int
        """
        self._risk_rating = risk_rating

    @property
    def severity(self):
        r"""Gets the severity of this ShowSecurityCheckOverviewResponse.

        **参数解释**: 风险级别 **取值范围**: - Security：安全 - Low：低危 - Medium：中危 - High：高危 

        :return: The severity of this ShowSecurityCheckOverviewResponse.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        r"""Sets the severity of this ShowSecurityCheckOverviewResponse.

        **参数解释**: 风险级别 **取值范围**: - Security：安全 - Low：低危 - Medium：中危 - High：高危 

        :param severity: The severity of this ShowSecurityCheckOverviewResponse.
        :type severity: str
        """
        self._severity = severity

    @property
    def scan_time(self):
        r"""Gets the scan_time of this ShowSecurityCheckOverviewResponse.

        **参数解释**: 最新检测时间，毫秒级时间戳 **取值范围**: 最小值0，最大值9223372036854775807（UTC时区，从1970-01-01 00:00:00开始计算） 

        :return: The scan_time of this ShowSecurityCheckOverviewResponse.
        :rtype: int
        """
        return self._scan_time

    @scan_time.setter
    def scan_time(self, scan_time):
        r"""Sets the scan_time of this ShowSecurityCheckOverviewResponse.

        **参数解释**: 最新检测时间，毫秒级时间戳 **取值范围**: 最小值0，最大值9223372036854775807（UTC时区，从1970-01-01 00:00:00开始计算） 

        :param scan_time: The scan_time of this ShowSecurityCheckOverviewResponse.
        :type scan_time: int
        """
        self._scan_time = scan_time

    @property
    def host_num(self):
        r"""Gets the host_num of this ShowSecurityCheckOverviewResponse.

        **参数解释**: 防护的服务器数量 **取值范围**: 最小值0，最大值2000000 

        :return: The host_num of this ShowSecurityCheckOverviewResponse.
        :rtype: int
        """
        return self._host_num

    @host_num.setter
    def host_num(self, host_num):
        r"""Sets the host_num of this ShowSecurityCheckOverviewResponse.

        **参数解释**: 防护的服务器数量 **取值范围**: 最小值0，最大值2000000 

        :param host_num: The host_num of this ShowSecurityCheckOverviewResponse.
        :type host_num: int
        """
        self._host_num = host_num

    @property
    def risk_num(self):
        r"""Gets the risk_num of this ShowSecurityCheckOverviewResponse.

        **参数解释**: 安全风险数量 **取值范围**: 最小值0，最大值2147483647 

        :return: The risk_num of this ShowSecurityCheckOverviewResponse.
        :rtype: int
        """
        return self._risk_num

    @risk_num.setter
    def risk_num(self, risk_num):
        r"""Sets the risk_num of this ShowSecurityCheckOverviewResponse.

        **参数解释**: 安全风险数量 **取值范围**: 最小值0，最大值2147483647 

        :param risk_num: The risk_num of this ShowSecurityCheckOverviewResponse.
        :type risk_num: int
        """
        self._risk_num = risk_num

    @property
    def scheduled_check_status(self):
        r"""Gets the scheduled_check_status of this ShowSecurityCheckOverviewResponse.

        **参数解释**: 定时体检开启状态 **取值范围**: - true：已开启 - false：未开启 

        :return: The scheduled_check_status of this ShowSecurityCheckOverviewResponse.
        :rtype: bool
        """
        return self._scheduled_check_status

    @scheduled_check_status.setter
    def scheduled_check_status(self, scheduled_check_status):
        r"""Sets the scheduled_check_status of this ShowSecurityCheckOverviewResponse.

        **参数解释**: 定时体检开启状态 **取值范围**: - true：已开启 - false：未开启 

        :param scheduled_check_status: The scheduled_check_status of this ShowSecurityCheckOverviewResponse.
        :type scheduled_check_status: bool
        """
        self._scheduled_check_status = scheduled_check_status

    def to_dict(self):
        import warnings
        warnings.warn("ShowSecurityCheckOverviewResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowSecurityCheckOverviewResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
