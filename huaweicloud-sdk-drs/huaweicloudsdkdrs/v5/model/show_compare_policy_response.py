# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowComparePolicyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'period': 'str',
        'status': 'str',
        'begin_time': 'str',
        'end_time': 'str',
        'compare_type': 'list[str]',
        'next_compare_time': 'str',
        'compare_policy': 'str',
        'interval_hour': 'int'
    }

    attribute_map = {
        'period': 'period',
        'status': 'status',
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'compare_type': 'compare_type',
        'next_compare_time': 'next_compare_time',
        'compare_policy': 'compare_policy',
        'interval_hour': 'interval_hour'
    }

    def __init__(self, period=None, status=None, begin_time=None, end_time=None, compare_type=None, next_compare_time=None, compare_policy=None, interval_hour=None):
        r"""ShowComparePolicyResponse

        The model defined in huaweicloud sdk

        :param period: 对比时间。
        :type period: str
        :param status: 对比策略状态。 - OPEN：开启 - CLOSED：关闭 - NO_SUPPORT：不支持
        :type status: str
        :param begin_time: 对比开始时间。
        :type begin_time: str
        :param end_time: 对比结束时间。
        :type end_time: str
        :param compare_type: 对比类型： - object_comparison：对象对比。 - lines：行对比。 - account：用户对比。
        :type compare_type: list[str]
        :param next_compare_time: 下次对比时间，UTC时间，例如：2023-06-12T08:00:00Z
        :type next_compare_time: str
        :param compare_policy: 对比策略。 - normal：普通对比 - manyToOne：多对一对比
        :type compare_policy: str
        :param interval_hour: 间隔时间。
        :type interval_hour: int
        """
        
        super(ShowComparePolicyResponse, self).__init__()

        self._period = None
        self._status = None
        self._begin_time = None
        self._end_time = None
        self._compare_type = None
        self._next_compare_time = None
        self._compare_policy = None
        self._interval_hour = None
        self.discriminator = None

        if period is not None:
            self.period = period
        if status is not None:
            self.status = status
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time
        if compare_type is not None:
            self.compare_type = compare_type
        if next_compare_time is not None:
            self.next_compare_time = next_compare_time
        if compare_policy is not None:
            self.compare_policy = compare_policy
        if interval_hour is not None:
            self.interval_hour = interval_hour

    @property
    def period(self):
        r"""Gets the period of this ShowComparePolicyResponse.

        对比时间。

        :return: The period of this ShowComparePolicyResponse.
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        r"""Sets the period of this ShowComparePolicyResponse.

        对比时间。

        :param period: The period of this ShowComparePolicyResponse.
        :type period: str
        """
        self._period = period

    @property
    def status(self):
        r"""Gets the status of this ShowComparePolicyResponse.

        对比策略状态。 - OPEN：开启 - CLOSED：关闭 - NO_SUPPORT：不支持

        :return: The status of this ShowComparePolicyResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowComparePolicyResponse.

        对比策略状态。 - OPEN：开启 - CLOSED：关闭 - NO_SUPPORT：不支持

        :param status: The status of this ShowComparePolicyResponse.
        :type status: str
        """
        self._status = status

    @property
    def begin_time(self):
        r"""Gets the begin_time of this ShowComparePolicyResponse.

        对比开始时间。

        :return: The begin_time of this ShowComparePolicyResponse.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        r"""Sets the begin_time of this ShowComparePolicyResponse.

        对比开始时间。

        :param begin_time: The begin_time of this ShowComparePolicyResponse.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ShowComparePolicyResponse.

        对比结束时间。

        :return: The end_time of this ShowComparePolicyResponse.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ShowComparePolicyResponse.

        对比结束时间。

        :param end_time: The end_time of this ShowComparePolicyResponse.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def compare_type(self):
        r"""Gets the compare_type of this ShowComparePolicyResponse.

        对比类型： - object_comparison：对象对比。 - lines：行对比。 - account：用户对比。

        :return: The compare_type of this ShowComparePolicyResponse.
        :rtype: list[str]
        """
        return self._compare_type

    @compare_type.setter
    def compare_type(self, compare_type):
        r"""Sets the compare_type of this ShowComparePolicyResponse.

        对比类型： - object_comparison：对象对比。 - lines：行对比。 - account：用户对比。

        :param compare_type: The compare_type of this ShowComparePolicyResponse.
        :type compare_type: list[str]
        """
        self._compare_type = compare_type

    @property
    def next_compare_time(self):
        r"""Gets the next_compare_time of this ShowComparePolicyResponse.

        下次对比时间，UTC时间，例如：2023-06-12T08:00:00Z

        :return: The next_compare_time of this ShowComparePolicyResponse.
        :rtype: str
        """
        return self._next_compare_time

    @next_compare_time.setter
    def next_compare_time(self, next_compare_time):
        r"""Sets the next_compare_time of this ShowComparePolicyResponse.

        下次对比时间，UTC时间，例如：2023-06-12T08:00:00Z

        :param next_compare_time: The next_compare_time of this ShowComparePolicyResponse.
        :type next_compare_time: str
        """
        self._next_compare_time = next_compare_time

    @property
    def compare_policy(self):
        r"""Gets the compare_policy of this ShowComparePolicyResponse.

        对比策略。 - normal：普通对比 - manyToOne：多对一对比

        :return: The compare_policy of this ShowComparePolicyResponse.
        :rtype: str
        """
        return self._compare_policy

    @compare_policy.setter
    def compare_policy(self, compare_policy):
        r"""Sets the compare_policy of this ShowComparePolicyResponse.

        对比策略。 - normal：普通对比 - manyToOne：多对一对比

        :param compare_policy: The compare_policy of this ShowComparePolicyResponse.
        :type compare_policy: str
        """
        self._compare_policy = compare_policy

    @property
    def interval_hour(self):
        r"""Gets the interval_hour of this ShowComparePolicyResponse.

        间隔时间。

        :return: The interval_hour of this ShowComparePolicyResponse.
        :rtype: int
        """
        return self._interval_hour

    @interval_hour.setter
    def interval_hour(self, interval_hour):
        r"""Sets the interval_hour of this ShowComparePolicyResponse.

        间隔时间。

        :param interval_hour: The interval_hour of this ShowComparePolicyResponse.
        :type interval_hour: int
        """
        self._interval_hour = interval_hour

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
        if not isinstance(other, ShowComparePolicyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
