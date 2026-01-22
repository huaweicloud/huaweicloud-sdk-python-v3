# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReportHistoryVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'report_id': 'str',
        'send_time': 'int',
        'statistic_period': 'StatisticPeriod'
    }

    attribute_map = {
        'report_id': 'report_id',
        'send_time': 'send_time',
        'statistic_period': 'statistic_period'
    }

    def __init__(self, report_id=None, send_time=None, statistic_period=None):
        r"""ReportHistoryVO

        The model defined in huaweicloud sdk

        :param report_id: **参数解释**： 报告ID **取值范围**： 不涉及
        :type report_id: str
        :param send_time: **参数解释**： 发送时间 **取值范围**： 不涉及
        :type send_time: int
        :param statistic_period: 
        :type statistic_period: :class:`huaweicloudsdkcfw.v1.StatisticPeriod`
        """
        
        

        self._report_id = None
        self._send_time = None
        self._statistic_period = None
        self.discriminator = None

        if report_id is not None:
            self.report_id = report_id
        if send_time is not None:
            self.send_time = send_time
        if statistic_period is not None:
            self.statistic_period = statistic_period

    @property
    def report_id(self):
        r"""Gets the report_id of this ReportHistoryVO.

        **参数解释**： 报告ID **取值范围**： 不涉及

        :return: The report_id of this ReportHistoryVO.
        :rtype: str
        """
        return self._report_id

    @report_id.setter
    def report_id(self, report_id):
        r"""Sets the report_id of this ReportHistoryVO.

        **参数解释**： 报告ID **取值范围**： 不涉及

        :param report_id: The report_id of this ReportHistoryVO.
        :type report_id: str
        """
        self._report_id = report_id

    @property
    def send_time(self):
        r"""Gets the send_time of this ReportHistoryVO.

        **参数解释**： 发送时间 **取值范围**： 不涉及

        :return: The send_time of this ReportHistoryVO.
        :rtype: int
        """
        return self._send_time

    @send_time.setter
    def send_time(self, send_time):
        r"""Sets the send_time of this ReportHistoryVO.

        **参数解释**： 发送时间 **取值范围**： 不涉及

        :param send_time: The send_time of this ReportHistoryVO.
        :type send_time: int
        """
        self._send_time = send_time

    @property
    def statistic_period(self):
        r"""Gets the statistic_period of this ReportHistoryVO.

        :return: The statistic_period of this ReportHistoryVO.
        :rtype: :class:`huaweicloudsdkcfw.v1.StatisticPeriod`
        """
        return self._statistic_period

    @statistic_period.setter
    def statistic_period(self, statistic_period):
        r"""Sets the statistic_period of this ReportHistoryVO.

        :param statistic_period: The statistic_period of this ReportHistoryVO.
        :type statistic_period: :class:`huaweicloudsdkcfw.v1.StatisticPeriod`
        """
        self._statistic_period = statistic_period

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
        if not isinstance(other, ReportHistoryVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
