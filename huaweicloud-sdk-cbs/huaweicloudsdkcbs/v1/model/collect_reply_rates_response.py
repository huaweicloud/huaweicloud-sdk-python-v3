# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CollectReplyRatesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'interval': 'str',
        'time_zone': 'str',
        'total': 'ReplyRatesTotal',
        'intervals': 'list[ReplyRatesIntervals]',
        'startutc': 'int',
        'endutc': 'int'
    }

    attribute_map = {
        'interval': 'interval',
        'time_zone': 'time_zone',
        'total': 'total',
        'intervals': 'intervals',
        'startutc': 'startutc',
        'endutc': 'endutc'
    }

    def __init__(self, interval=None, time_zone=None, total=None, intervals=None, startutc=None, endutc=None):
        r"""CollectReplyRatesResponse

        The model defined in huaweicloud sdk

        :param interval: 统计周期目前支持year、month、week、day。 调用失败时无此字段。
        :type interval: str
        :param time_zone: 所在时区，例如：中国东八区为\&quot;+08:00\&quot;；美国西五区为\&quot;-05:00\&quot;;默认为\&quot;UTC\&quot;。 调用失败时无此字段。
        :type time_zone: str
        :param total: 
        :type total: :class:`huaweicloudsdkcbs.v1.ReplyRatesTotal`
        :param intervals: 会话间隔统计数据。
        :type intervals: list[:class:`huaweicloudsdkcbs.v1.ReplyRatesIntervals`]
        :param startutc: 统计开始的utc时间。
        :type startutc: int
        :param endutc: 统计结束的utc时间。
        :type endutc: int
        """
        
        super(CollectReplyRatesResponse, self).__init__()

        self._interval = None
        self._time_zone = None
        self._total = None
        self._intervals = None
        self._startutc = None
        self._endutc = None
        self.discriminator = None

        if interval is not None:
            self.interval = interval
        if time_zone is not None:
            self.time_zone = time_zone
        if total is not None:
            self.total = total
        if intervals is not None:
            self.intervals = intervals
        if startutc is not None:
            self.startutc = startutc
        if endutc is not None:
            self.endutc = endutc

    @property
    def interval(self):
        r"""Gets the interval of this CollectReplyRatesResponse.

        统计周期目前支持year、month、week、day。 调用失败时无此字段。

        :return: The interval of this CollectReplyRatesResponse.
        :rtype: str
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        r"""Sets the interval of this CollectReplyRatesResponse.

        统计周期目前支持year、month、week、day。 调用失败时无此字段。

        :param interval: The interval of this CollectReplyRatesResponse.
        :type interval: str
        """
        self._interval = interval

    @property
    def time_zone(self):
        r"""Gets the time_zone of this CollectReplyRatesResponse.

        所在时区，例如：中国东八区为\"+08:00\"；美国西五区为\"-05:00\";默认为\"UTC\"。 调用失败时无此字段。

        :return: The time_zone of this CollectReplyRatesResponse.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        r"""Sets the time_zone of this CollectReplyRatesResponse.

        所在时区，例如：中国东八区为\"+08:00\"；美国西五区为\"-05:00\";默认为\"UTC\"。 调用失败时无此字段。

        :param time_zone: The time_zone of this CollectReplyRatesResponse.
        :type time_zone: str
        """
        self._time_zone = time_zone

    @property
    def total(self):
        r"""Gets the total of this CollectReplyRatesResponse.

        :return: The total of this CollectReplyRatesResponse.
        :rtype: :class:`huaweicloudsdkcbs.v1.ReplyRatesTotal`
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this CollectReplyRatesResponse.

        :param total: The total of this CollectReplyRatesResponse.
        :type total: :class:`huaweicloudsdkcbs.v1.ReplyRatesTotal`
        """
        self._total = total

    @property
    def intervals(self):
        r"""Gets the intervals of this CollectReplyRatesResponse.

        会话间隔统计数据。

        :return: The intervals of this CollectReplyRatesResponse.
        :rtype: list[:class:`huaweicloudsdkcbs.v1.ReplyRatesIntervals`]
        """
        return self._intervals

    @intervals.setter
    def intervals(self, intervals):
        r"""Sets the intervals of this CollectReplyRatesResponse.

        会话间隔统计数据。

        :param intervals: The intervals of this CollectReplyRatesResponse.
        :type intervals: list[:class:`huaweicloudsdkcbs.v1.ReplyRatesIntervals`]
        """
        self._intervals = intervals

    @property
    def startutc(self):
        r"""Gets the startutc of this CollectReplyRatesResponse.

        统计开始的utc时间。

        :return: The startutc of this CollectReplyRatesResponse.
        :rtype: int
        """
        return self._startutc

    @startutc.setter
    def startutc(self, startutc):
        r"""Sets the startutc of this CollectReplyRatesResponse.

        统计开始的utc时间。

        :param startutc: The startutc of this CollectReplyRatesResponse.
        :type startutc: int
        """
        self._startutc = startutc

    @property
    def endutc(self):
        r"""Gets the endutc of this CollectReplyRatesResponse.

        统计结束的utc时间。

        :return: The endutc of this CollectReplyRatesResponse.
        :rtype: int
        """
        return self._endutc

    @endutc.setter
    def endutc(self, endutc):
        r"""Sets the endutc of this CollectReplyRatesResponse.

        统计结束的utc时间。

        :param endutc: The endutc of this CollectReplyRatesResponse.
        :type endutc: int
        """
        self._endutc = endutc

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
        if not isinstance(other, CollectReplyRatesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
