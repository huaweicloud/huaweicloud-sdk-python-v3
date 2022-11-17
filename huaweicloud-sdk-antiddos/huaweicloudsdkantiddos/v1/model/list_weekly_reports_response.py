# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListWeeklyReportsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ddos_intercept_times': 'int',
        'weekdata': 'list[WeeklyCount]',
        'top10': 'list[WeeklyTop10]'
    }

    attribute_map = {
        'ddos_intercept_times': 'ddos_intercept_times',
        'weekdata': 'weekdata',
        'top10': 'top10'
    }

    def __init__(self, ddos_intercept_times=None, weekdata=None, top10=None):
        """ListWeeklyReportsResponse

        The model defined in huaweicloud sdk

        :param ddos_intercept_times: 一周内DDoS拦截次数
        :type ddos_intercept_times: int
        :param weekdata: 一周的攻击次数统计数据
        :type weekdata: list[:class:`huaweicloudsdkantiddos.v1.WeeklyCount`]
        :param top10: 被攻击次数排名前10的IP地址
        :type top10: list[:class:`huaweicloudsdkantiddos.v1.WeeklyTop10`]
        """
        
        super(ListWeeklyReportsResponse, self).__init__()

        self._ddos_intercept_times = None
        self._weekdata = None
        self._top10 = None
        self.discriminator = None

        if ddos_intercept_times is not None:
            self.ddos_intercept_times = ddos_intercept_times
        if weekdata is not None:
            self.weekdata = weekdata
        if top10 is not None:
            self.top10 = top10

    @property
    def ddos_intercept_times(self):
        """Gets the ddos_intercept_times of this ListWeeklyReportsResponse.

        一周内DDoS拦截次数

        :return: The ddos_intercept_times of this ListWeeklyReportsResponse.
        :rtype: int
        """
        return self._ddos_intercept_times

    @ddos_intercept_times.setter
    def ddos_intercept_times(self, ddos_intercept_times):
        """Sets the ddos_intercept_times of this ListWeeklyReportsResponse.

        一周内DDoS拦截次数

        :param ddos_intercept_times: The ddos_intercept_times of this ListWeeklyReportsResponse.
        :type ddos_intercept_times: int
        """
        self._ddos_intercept_times = ddos_intercept_times

    @property
    def weekdata(self):
        """Gets the weekdata of this ListWeeklyReportsResponse.

        一周的攻击次数统计数据

        :return: The weekdata of this ListWeeklyReportsResponse.
        :rtype: list[:class:`huaweicloudsdkantiddos.v1.WeeklyCount`]
        """
        return self._weekdata

    @weekdata.setter
    def weekdata(self, weekdata):
        """Sets the weekdata of this ListWeeklyReportsResponse.

        一周的攻击次数统计数据

        :param weekdata: The weekdata of this ListWeeklyReportsResponse.
        :type weekdata: list[:class:`huaweicloudsdkantiddos.v1.WeeklyCount`]
        """
        self._weekdata = weekdata

    @property
    def top10(self):
        """Gets the top10 of this ListWeeklyReportsResponse.

        被攻击次数排名前10的IP地址

        :return: The top10 of this ListWeeklyReportsResponse.
        :rtype: list[:class:`huaweicloudsdkantiddos.v1.WeeklyTop10`]
        """
        return self._top10

    @top10.setter
    def top10(self, top10):
        """Sets the top10 of this ListWeeklyReportsResponse.

        被攻击次数排名前10的IP地址

        :param top10: The top10 of this ListWeeklyReportsResponse.
        :type top10: list[:class:`huaweicloudsdkantiddos.v1.WeeklyTop10`]
        """
        self._top10 = top10

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
        if not isinstance(other, ListWeeklyReportsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
