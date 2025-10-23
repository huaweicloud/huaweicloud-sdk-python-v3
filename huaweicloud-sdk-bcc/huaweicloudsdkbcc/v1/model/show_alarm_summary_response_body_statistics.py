# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAlarmSummaryResponseBodyStatistics:

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
        'counts': 'int'
    }

    attribute_map = {
        'severity': 'severity',
        'counts': 'counts'
    }

    def __init__(self, severity=None, counts=None):
        r"""ShowAlarmSummaryResponseBodyStatistics

        The model defined in huaweicloud sdk

        :param severity: 告警级别，取值范围:1,2,3,4
        :type severity: str
        :param counts: 告警数量
        :type counts: int
        """
        
        

        self._severity = None
        self._counts = None
        self.discriminator = None

        self.severity = severity
        self.counts = counts

    @property
    def severity(self):
        r"""Gets the severity of this ShowAlarmSummaryResponseBodyStatistics.

        告警级别，取值范围:1,2,3,4

        :return: The severity of this ShowAlarmSummaryResponseBodyStatistics.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        r"""Sets the severity of this ShowAlarmSummaryResponseBodyStatistics.

        告警级别，取值范围:1,2,3,4

        :param severity: The severity of this ShowAlarmSummaryResponseBodyStatistics.
        :type severity: str
        """
        self._severity = severity

    @property
    def counts(self):
        r"""Gets the counts of this ShowAlarmSummaryResponseBodyStatistics.

        告警数量

        :return: The counts of this ShowAlarmSummaryResponseBodyStatistics.
        :rtype: int
        """
        return self._counts

    @counts.setter
    def counts(self, counts):
        r"""Sets the counts of this ShowAlarmSummaryResponseBodyStatistics.

        告警数量

        :param counts: The counts of this ShowAlarmSummaryResponseBodyStatistics.
        :type counts: int
        """
        self._counts = counts

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
        if not isinstance(other, ShowAlarmSummaryResponseBodyStatistics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
