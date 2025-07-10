# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAlarmStatisticsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'critical_count': 'int',
        'major_count': 'int',
        'minor_count': 'int',
        'info_count': 'int',
        'total': 'int'
    }

    attribute_map = {
        'critical_count': 'critical_count',
        'major_count': 'major_count',
        'minor_count': 'minor_count',
        'info_count': 'info_count',
        'total': 'total'
    }

    def __init__(self, critical_count=None, major_count=None, minor_count=None, info_count=None, total=None):
        r"""ListAlarmStatisticsResponse

        The model defined in huaweicloud sdk

        :param critical_count: 紧急告警记录列表总数。
        :type critical_count: int
        :param major_count: 重要告警记录列表总数。
        :type major_count: int
        :param minor_count: 次要告警记录列表总数。
        :type minor_count: int
        :param info_count: 提示告警记录列表总数。
        :type info_count: int
        :param total: 告警记录列表总数。
        :type total: int
        """
        
        super(ListAlarmStatisticsResponse, self).__init__()

        self._critical_count = None
        self._major_count = None
        self._minor_count = None
        self._info_count = None
        self._total = None
        self.discriminator = None

        if critical_count is not None:
            self.critical_count = critical_count
        if major_count is not None:
            self.major_count = major_count
        if minor_count is not None:
            self.minor_count = minor_count
        if info_count is not None:
            self.info_count = info_count
        if total is not None:
            self.total = total

    @property
    def critical_count(self):
        r"""Gets the critical_count of this ListAlarmStatisticsResponse.

        紧急告警记录列表总数。

        :return: The critical_count of this ListAlarmStatisticsResponse.
        :rtype: int
        """
        return self._critical_count

    @critical_count.setter
    def critical_count(self, critical_count):
        r"""Sets the critical_count of this ListAlarmStatisticsResponse.

        紧急告警记录列表总数。

        :param critical_count: The critical_count of this ListAlarmStatisticsResponse.
        :type critical_count: int
        """
        self._critical_count = critical_count

    @property
    def major_count(self):
        r"""Gets the major_count of this ListAlarmStatisticsResponse.

        重要告警记录列表总数。

        :return: The major_count of this ListAlarmStatisticsResponse.
        :rtype: int
        """
        return self._major_count

    @major_count.setter
    def major_count(self, major_count):
        r"""Sets the major_count of this ListAlarmStatisticsResponse.

        重要告警记录列表总数。

        :param major_count: The major_count of this ListAlarmStatisticsResponse.
        :type major_count: int
        """
        self._major_count = major_count

    @property
    def minor_count(self):
        r"""Gets the minor_count of this ListAlarmStatisticsResponse.

        次要告警记录列表总数。

        :return: The minor_count of this ListAlarmStatisticsResponse.
        :rtype: int
        """
        return self._minor_count

    @minor_count.setter
    def minor_count(self, minor_count):
        r"""Sets the minor_count of this ListAlarmStatisticsResponse.

        次要告警记录列表总数。

        :param minor_count: The minor_count of this ListAlarmStatisticsResponse.
        :type minor_count: int
        """
        self._minor_count = minor_count

    @property
    def info_count(self):
        r"""Gets the info_count of this ListAlarmStatisticsResponse.

        提示告警记录列表总数。

        :return: The info_count of this ListAlarmStatisticsResponse.
        :rtype: int
        """
        return self._info_count

    @info_count.setter
    def info_count(self, info_count):
        r"""Sets the info_count of this ListAlarmStatisticsResponse.

        提示告警记录列表总数。

        :param info_count: The info_count of this ListAlarmStatisticsResponse.
        :type info_count: int
        """
        self._info_count = info_count

    @property
    def total(self):
        r"""Gets the total of this ListAlarmStatisticsResponse.

        告警记录列表总数。

        :return: The total of this ListAlarmStatisticsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListAlarmStatisticsResponse.

        告警记录列表总数。

        :param total: The total of this ListAlarmStatisticsResponse.
        :type total: int
        """
        self._total = total

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
        if not isinstance(other, ListAlarmStatisticsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
