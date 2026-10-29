# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTaskDefectsStatisticResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'severity': 'StatisticSeverityV2',
        'status': 'StatisticStatusV2',
        'last_check_time': 'str',
        'last_check_finish_time': 'str'
    }

    attribute_map = {
        'severity': 'severity',
        'status': 'status',
        'last_check_time': 'last_check_time',
        'last_check_finish_time': 'last_check_finish_time'
    }

    def __init__(self, severity=None, status=None, last_check_time=None, last_check_finish_time=None):
        r"""ShowTaskDefectsStatisticResponse

        The model defined in huaweicloud sdk

        :param severity: 
        :type severity: :class:`huaweicloudsdkcodeartscheck.v2.StatisticSeverityV2`
        :param status: 
        :type status: :class:`huaweicloudsdkcodeartscheck.v2.StatisticStatusV2`
        :param last_check_time: **参数解释：** 检查开始时间，使用UTC时间，格式为yyyy-MM-ddTHH:mm:ssZ。例如：2020-09-25T12:05:00Z。 **取值范围：** 不涉及。
        :type last_check_time: str
        :param last_check_finish_time: **参数解释：** 检查结束时间，使用UTC时间，格式为yyyy-MM-ddTHH:mm:ssZ。例如：2020-09-25T12:05:00Z。 **取值范围：** 不涉及。
        :type last_check_finish_time: str
        """
        
        super().__init__()

        self._severity = None
        self._status = None
        self._last_check_time = None
        self._last_check_finish_time = None
        self.discriminator = None

        if severity is not None:
            self.severity = severity
        if status is not None:
            self.status = status
        if last_check_time is not None:
            self.last_check_time = last_check_time
        if last_check_finish_time is not None:
            self.last_check_finish_time = last_check_finish_time

    @property
    def severity(self):
        r"""Gets the severity of this ShowTaskDefectsStatisticResponse.

        :return: The severity of this ShowTaskDefectsStatisticResponse.
        :rtype: :class:`huaweicloudsdkcodeartscheck.v2.StatisticSeverityV2`
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        r"""Sets the severity of this ShowTaskDefectsStatisticResponse.

        :param severity: The severity of this ShowTaskDefectsStatisticResponse.
        :type severity: :class:`huaweicloudsdkcodeartscheck.v2.StatisticSeverityV2`
        """
        self._severity = severity

    @property
    def status(self):
        r"""Gets the status of this ShowTaskDefectsStatisticResponse.

        :return: The status of this ShowTaskDefectsStatisticResponse.
        :rtype: :class:`huaweicloudsdkcodeartscheck.v2.StatisticStatusV2`
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowTaskDefectsStatisticResponse.

        :param status: The status of this ShowTaskDefectsStatisticResponse.
        :type status: :class:`huaweicloudsdkcodeartscheck.v2.StatisticStatusV2`
        """
        self._status = status

    @property
    def last_check_time(self):
        r"""Gets the last_check_time of this ShowTaskDefectsStatisticResponse.

        **参数解释：** 检查开始时间，使用UTC时间，格式为yyyy-MM-ddTHH:mm:ssZ。例如：2020-09-25T12:05:00Z。 **取值范围：** 不涉及。

        :return: The last_check_time of this ShowTaskDefectsStatisticResponse.
        :rtype: str
        """
        return self._last_check_time

    @last_check_time.setter
    def last_check_time(self, last_check_time):
        r"""Sets the last_check_time of this ShowTaskDefectsStatisticResponse.

        **参数解释：** 检查开始时间，使用UTC时间，格式为yyyy-MM-ddTHH:mm:ssZ。例如：2020-09-25T12:05:00Z。 **取值范围：** 不涉及。

        :param last_check_time: The last_check_time of this ShowTaskDefectsStatisticResponse.
        :type last_check_time: str
        """
        self._last_check_time = last_check_time

    @property
    def last_check_finish_time(self):
        r"""Gets the last_check_finish_time of this ShowTaskDefectsStatisticResponse.

        **参数解释：** 检查结束时间，使用UTC时间，格式为yyyy-MM-ddTHH:mm:ssZ。例如：2020-09-25T12:05:00Z。 **取值范围：** 不涉及。

        :return: The last_check_finish_time of this ShowTaskDefectsStatisticResponse.
        :rtype: str
        """
        return self._last_check_finish_time

    @last_check_finish_time.setter
    def last_check_finish_time(self, last_check_finish_time):
        r"""Sets the last_check_finish_time of this ShowTaskDefectsStatisticResponse.

        **参数解释：** 检查结束时间，使用UTC时间，格式为yyyy-MM-ddTHH:mm:ssZ。例如：2020-09-25T12:05:00Z。 **取值范围：** 不涉及。

        :param last_check_finish_time: The last_check_finish_time of this ShowTaskDefectsStatisticResponse.
        :type last_check_finish_time: str
        """
        self._last_check_finish_time = last_check_finish_time

    def to_dict(self):
        import warnings
        warnings.warn("ShowTaskDefectsStatisticResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowTaskDefectsStatisticResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
