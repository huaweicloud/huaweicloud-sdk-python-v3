# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModifyComparePolicyReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'action': 'str',
        'period': 'str',
        'begin_time': 'str',
        'end_time': 'str',
        'compare_type': 'list[str]',
        'compare_policy': 'str',
        'interval_hour': 'int'
    }

    attribute_map = {
        'action': 'action',
        'period': 'period',
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'compare_type': 'compare_type',
        'compare_policy': 'compare_policy',
        'interval_hour': 'interval_hour'
    }

    def __init__(self, action=None, period=None, begin_time=None, end_time=None, compare_type=None, compare_policy=None, interval_hour=None):
        r"""ModifyComparePolicyReq

        The model defined in huaweicloud sdk

        :param action: 对比策略开关-open|close。
        :type action: str
        :param period: 对比策略周期。 - 每周对比：格式示例：“* * 1,3,5” ，其中“1,3,5”对应星期一、星期三、星期五，根据实际填写。 - 每天对比：固定填写“* * 1,2,3,4,5,6,7”。 - 按小时对比：固定填写“* * 1,2,3,4,5,6,7”。
        :type period: str
        :param begin_time: 对比策略生效开始时间，UTC时间，24小时制，时间格式HH:mm:ss，例如：00:00:00，表示UTC时间的00:00:00，北京时间（UTC+08:00）的08:00:00。
        :type begin_time: str
        :param end_time: 对比策略生效结束时间，UTC时间，24小时制，时间格式HH:mm:ss，例如：04:00:00，表示UTC时间的04:00:00，北京时间（UTC+08:00）的12:00:00。
        :type end_time: str
        :param compare_type: 对比类型列表： - object_comparison：对象对比。 - lines：行对比。 - account：用户对比。
        :type compare_type: list[str]
        :param compare_policy: 对比策略： - normal：普通对比。 - manyToOne：多对一对比。
        :type compare_policy: str
        :param interval_hour: 间隔时间，按小时对比时填写，表示每隔多久执行一次对比，单位是小时。
        :type interval_hour: int
        """
        
        

        self._action = None
        self._period = None
        self._begin_time = None
        self._end_time = None
        self._compare_type = None
        self._compare_policy = None
        self._interval_hour = None
        self.discriminator = None

        self.action = action
        if period is not None:
            self.period = period
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time
        if compare_type is not None:
            self.compare_type = compare_type
        if compare_policy is not None:
            self.compare_policy = compare_policy
        if interval_hour is not None:
            self.interval_hour = interval_hour

    @property
    def action(self):
        r"""Gets the action of this ModifyComparePolicyReq.

        对比策略开关-open|close。

        :return: The action of this ModifyComparePolicyReq.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this ModifyComparePolicyReq.

        对比策略开关-open|close。

        :param action: The action of this ModifyComparePolicyReq.
        :type action: str
        """
        self._action = action

    @property
    def period(self):
        r"""Gets the period of this ModifyComparePolicyReq.

        对比策略周期。 - 每周对比：格式示例：“* * 1,3,5” ，其中“1,3,5”对应星期一、星期三、星期五，根据实际填写。 - 每天对比：固定填写“* * 1,2,3,4,5,6,7”。 - 按小时对比：固定填写“* * 1,2,3,4,5,6,7”。

        :return: The period of this ModifyComparePolicyReq.
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        r"""Sets the period of this ModifyComparePolicyReq.

        对比策略周期。 - 每周对比：格式示例：“* * 1,3,5” ，其中“1,3,5”对应星期一、星期三、星期五，根据实际填写。 - 每天对比：固定填写“* * 1,2,3,4,5,6,7”。 - 按小时对比：固定填写“* * 1,2,3,4,5,6,7”。

        :param period: The period of this ModifyComparePolicyReq.
        :type period: str
        """
        self._period = period

    @property
    def begin_time(self):
        r"""Gets the begin_time of this ModifyComparePolicyReq.

        对比策略生效开始时间，UTC时间，24小时制，时间格式HH:mm:ss，例如：00:00:00，表示UTC时间的00:00:00，北京时间（UTC+08:00）的08:00:00。

        :return: The begin_time of this ModifyComparePolicyReq.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        r"""Sets the begin_time of this ModifyComparePolicyReq.

        对比策略生效开始时间，UTC时间，24小时制，时间格式HH:mm:ss，例如：00:00:00，表示UTC时间的00:00:00，北京时间（UTC+08:00）的08:00:00。

        :param begin_time: The begin_time of this ModifyComparePolicyReq.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ModifyComparePolicyReq.

        对比策略生效结束时间，UTC时间，24小时制，时间格式HH:mm:ss，例如：04:00:00，表示UTC时间的04:00:00，北京时间（UTC+08:00）的12:00:00。

        :return: The end_time of this ModifyComparePolicyReq.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ModifyComparePolicyReq.

        对比策略生效结束时间，UTC时间，24小时制，时间格式HH:mm:ss，例如：04:00:00，表示UTC时间的04:00:00，北京时间（UTC+08:00）的12:00:00。

        :param end_time: The end_time of this ModifyComparePolicyReq.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def compare_type(self):
        r"""Gets the compare_type of this ModifyComparePolicyReq.

        对比类型列表： - object_comparison：对象对比。 - lines：行对比。 - account：用户对比。

        :return: The compare_type of this ModifyComparePolicyReq.
        :rtype: list[str]
        """
        return self._compare_type

    @compare_type.setter
    def compare_type(self, compare_type):
        r"""Sets the compare_type of this ModifyComparePolicyReq.

        对比类型列表： - object_comparison：对象对比。 - lines：行对比。 - account：用户对比。

        :param compare_type: The compare_type of this ModifyComparePolicyReq.
        :type compare_type: list[str]
        """
        self._compare_type = compare_type

    @property
    def compare_policy(self):
        r"""Gets the compare_policy of this ModifyComparePolicyReq.

        对比策略： - normal：普通对比。 - manyToOne：多对一对比。

        :return: The compare_policy of this ModifyComparePolicyReq.
        :rtype: str
        """
        return self._compare_policy

    @compare_policy.setter
    def compare_policy(self, compare_policy):
        r"""Sets the compare_policy of this ModifyComparePolicyReq.

        对比策略： - normal：普通对比。 - manyToOne：多对一对比。

        :param compare_policy: The compare_policy of this ModifyComparePolicyReq.
        :type compare_policy: str
        """
        self._compare_policy = compare_policy

    @property
    def interval_hour(self):
        r"""Gets the interval_hour of this ModifyComparePolicyReq.

        间隔时间，按小时对比时填写，表示每隔多久执行一次对比，单位是小时。

        :return: The interval_hour of this ModifyComparePolicyReq.
        :rtype: int
        """
        return self._interval_hour

    @interval_hour.setter
    def interval_hour(self, interval_hour):
        r"""Sets the interval_hour of this ModifyComparePolicyReq.

        间隔时间，按小时对比时填写，表示每隔多久执行一次对比，单位是小时。

        :param interval_hour: The interval_hour of this ModifyComparePolicyReq.
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
        if not isinstance(other, ModifyComparePolicyReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
