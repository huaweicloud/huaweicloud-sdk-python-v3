# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SecurityCheckHostResultResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'host_info': 'SecurityCheckHostInfo',
        'severity': 'str',
        'risk_rating': 'int',
        'risk_num': 'int',
        'scan_time': 'int'
    }

    attribute_map = {
        'host_info': 'host_info',
        'severity': 'severity',
        'risk_rating': 'risk_rating',
        'risk_num': 'risk_num',
        'scan_time': 'scan_time'
    }

    def __init__(self, host_info=None, severity=None, risk_rating=None, risk_num=None, scan_time=None):
        r"""SecurityCheckHostResultResponseInfo

        The model defined in huaweicloud sdk

        :param host_info: 
        :type host_info: :class:`huaweicloudsdkhss.v5.SecurityCheckHostInfo`
        :param severity: **参数解释**： 风险级别 **取值范围**： - high：高危 - medium：中危 - low：低危 - safe：安全，无风险 
        :type severity: str
        :param risk_rating: **参数解释**： 风险评分 **取值范围**： 不涉及 
        :type risk_rating: int
        :param risk_num: **参数解释**： 风险数量 **取值范围**： 不涉及 
        :type risk_num: int
        :param scan_time: **参数解释**： 最新检测时间 **取值范围**： 不涉及 
        :type scan_time: int
        """
        
        

        self._host_info = None
        self._severity = None
        self._risk_rating = None
        self._risk_num = None
        self._scan_time = None
        self.discriminator = None

        if host_info is not None:
            self.host_info = host_info
        if severity is not None:
            self.severity = severity
        if risk_rating is not None:
            self.risk_rating = risk_rating
        if risk_num is not None:
            self.risk_num = risk_num
        if scan_time is not None:
            self.scan_time = scan_time

    @property
    def host_info(self):
        r"""Gets the host_info of this SecurityCheckHostResultResponseInfo.

        :return: The host_info of this SecurityCheckHostResultResponseInfo.
        :rtype: :class:`huaweicloudsdkhss.v5.SecurityCheckHostInfo`
        """
        return self._host_info

    @host_info.setter
    def host_info(self, host_info):
        r"""Sets the host_info of this SecurityCheckHostResultResponseInfo.

        :param host_info: The host_info of this SecurityCheckHostResultResponseInfo.
        :type host_info: :class:`huaweicloudsdkhss.v5.SecurityCheckHostInfo`
        """
        self._host_info = host_info

    @property
    def severity(self):
        r"""Gets the severity of this SecurityCheckHostResultResponseInfo.

        **参数解释**： 风险级别 **取值范围**： - high：高危 - medium：中危 - low：低危 - safe：安全，无风险 

        :return: The severity of this SecurityCheckHostResultResponseInfo.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        r"""Sets the severity of this SecurityCheckHostResultResponseInfo.

        **参数解释**： 风险级别 **取值范围**： - high：高危 - medium：中危 - low：低危 - safe：安全，无风险 

        :param severity: The severity of this SecurityCheckHostResultResponseInfo.
        :type severity: str
        """
        self._severity = severity

    @property
    def risk_rating(self):
        r"""Gets the risk_rating of this SecurityCheckHostResultResponseInfo.

        **参数解释**： 风险评分 **取值范围**： 不涉及 

        :return: The risk_rating of this SecurityCheckHostResultResponseInfo.
        :rtype: int
        """
        return self._risk_rating

    @risk_rating.setter
    def risk_rating(self, risk_rating):
        r"""Sets the risk_rating of this SecurityCheckHostResultResponseInfo.

        **参数解释**： 风险评分 **取值范围**： 不涉及 

        :param risk_rating: The risk_rating of this SecurityCheckHostResultResponseInfo.
        :type risk_rating: int
        """
        self._risk_rating = risk_rating

    @property
    def risk_num(self):
        r"""Gets the risk_num of this SecurityCheckHostResultResponseInfo.

        **参数解释**： 风险数量 **取值范围**： 不涉及 

        :return: The risk_num of this SecurityCheckHostResultResponseInfo.
        :rtype: int
        """
        return self._risk_num

    @risk_num.setter
    def risk_num(self, risk_num):
        r"""Sets the risk_num of this SecurityCheckHostResultResponseInfo.

        **参数解释**： 风险数量 **取值范围**： 不涉及 

        :param risk_num: The risk_num of this SecurityCheckHostResultResponseInfo.
        :type risk_num: int
        """
        self._risk_num = risk_num

    @property
    def scan_time(self):
        r"""Gets the scan_time of this SecurityCheckHostResultResponseInfo.

        **参数解释**： 最新检测时间 **取值范围**： 不涉及 

        :return: The scan_time of this SecurityCheckHostResultResponseInfo.
        :rtype: int
        """
        return self._scan_time

    @scan_time.setter
    def scan_time(self, scan_time):
        r"""Sets the scan_time of this SecurityCheckHostResultResponseInfo.

        **参数解释**： 最新检测时间 **取值范围**： 不涉及 

        :param scan_time: The scan_time of this SecurityCheckHostResultResponseInfo.
        :type scan_time: int
        """
        self._scan_time = scan_time

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
        if not isinstance(other, SecurityCheckHostResultResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
