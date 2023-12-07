# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSubMetricsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'filter': 'str',
        'period': 'int',
        'start_time': 'int',
        'end_time': 'int',
        'subscription_id': 'str',
        'provider_type': 'str',
        'target_id': 'str'
    }

    attribute_map = {
        'filter': 'filter',
        'period': 'period',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'subscription_id': 'subscription_id',
        'provider_type': 'provider_type',
        'target_id': 'target_id'
    }

    def __init__(self, filter=None, period=None, start_time=None, end_time=None, subscription_id=None, provider_type=None, target_id=None):
        """ListSubMetricsRequest

        The model defined in huaweicloud sdk

        :param filter: 指标数据统计方式
        :type filter: str
        :param period: 指标数据统计周期，单位minute。
        :type period: int
        :param start_time: 获取指标数据起始时间
        :type start_time: int
        :param end_time: 获取指标数据结束时间
        :type end_time: int
        :param subscription_id: 事件订阅id
        :type subscription_id: str
        :param provider_type: 事件目标类型/事件通道类型
        :type provider_type: str
        :param target_id: 事件目标id
        :type target_id: str
        """
        
        

        self._filter = None
        self._period = None
        self._start_time = None
        self._end_time = None
        self._subscription_id = None
        self._provider_type = None
        self._target_id = None
        self.discriminator = None

        if filter is not None:
            self.filter = filter
        if period is not None:
            self.period = period
        self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        self.subscription_id = subscription_id
        if provider_type is not None:
            self.provider_type = provider_type
        if target_id is not None:
            self.target_id = target_id

    @property
    def filter(self):
        """Gets the filter of this ListSubMetricsRequest.

        指标数据统计方式

        :return: The filter of this ListSubMetricsRequest.
        :rtype: str
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this ListSubMetricsRequest.

        指标数据统计方式

        :param filter: The filter of this ListSubMetricsRequest.
        :type filter: str
        """
        self._filter = filter

    @property
    def period(self):
        """Gets the period of this ListSubMetricsRequest.

        指标数据统计周期，单位minute。

        :return: The period of this ListSubMetricsRequest.
        :rtype: int
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this ListSubMetricsRequest.

        指标数据统计周期，单位minute。

        :param period: The period of this ListSubMetricsRequest.
        :type period: int
        """
        self._period = period

    @property
    def start_time(self):
        """Gets the start_time of this ListSubMetricsRequest.

        获取指标数据起始时间

        :return: The start_time of this ListSubMetricsRequest.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ListSubMetricsRequest.

        获取指标数据起始时间

        :param start_time: The start_time of this ListSubMetricsRequest.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ListSubMetricsRequest.

        获取指标数据结束时间

        :return: The end_time of this ListSubMetricsRequest.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ListSubMetricsRequest.

        获取指标数据结束时间

        :param end_time: The end_time of this ListSubMetricsRequest.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def subscription_id(self):
        """Gets the subscription_id of this ListSubMetricsRequest.

        事件订阅id

        :return: The subscription_id of this ListSubMetricsRequest.
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        """Sets the subscription_id of this ListSubMetricsRequest.

        事件订阅id

        :param subscription_id: The subscription_id of this ListSubMetricsRequest.
        :type subscription_id: str
        """
        self._subscription_id = subscription_id

    @property
    def provider_type(self):
        """Gets the provider_type of this ListSubMetricsRequest.

        事件目标类型/事件通道类型

        :return: The provider_type of this ListSubMetricsRequest.
        :rtype: str
        """
        return self._provider_type

    @provider_type.setter
    def provider_type(self, provider_type):
        """Sets the provider_type of this ListSubMetricsRequest.

        事件目标类型/事件通道类型

        :param provider_type: The provider_type of this ListSubMetricsRequest.
        :type provider_type: str
        """
        self._provider_type = provider_type

    @property
    def target_id(self):
        """Gets the target_id of this ListSubMetricsRequest.

        事件目标id

        :return: The target_id of this ListSubMetricsRequest.
        :rtype: str
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        """Sets the target_id of this ListSubMetricsRequest.

        事件目标id

        :param target_id: The target_id of this ListSubMetricsRequest.
        :type target_id: str
        """
        self._target_id = target_id

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
        if not isinstance(other, ListSubMetricsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
