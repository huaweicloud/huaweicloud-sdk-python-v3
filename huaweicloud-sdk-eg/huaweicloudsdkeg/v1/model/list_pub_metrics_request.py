# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPubMetricsRequest:

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
        'channel_id': 'str',
        'provider_type': 'str',
        'source_name': 'str'
    }

    attribute_map = {
        'filter': 'filter',
        'period': 'period',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'channel_id': 'channel_id',
        'provider_type': 'provider_type',
        'source_name': 'source_name'
    }

    def __init__(self, filter=None, period=None, start_time=None, end_time=None, channel_id=None, provider_type=None, source_name=None):
        """ListPubMetricsRequest

        The model defined in huaweicloud sdk

        :param filter: 指标数据统计方式
        :type filter: str
        :param period: 指标数据统计周期（单位minute）
        :type period: int
        :param start_time: 获取指标数据起始时间
        :type start_time: int
        :param end_time: 获取指标数据结束时间
        :type end_time: int
        :param channel_id: 事件通道id
        :type channel_id: str
        :param provider_type: 事件目标类型/事件通道类型
        :type provider_type: str
        :param source_name: 事件源名称
        :type source_name: str
        """
        
        

        self._filter = None
        self._period = None
        self._start_time = None
        self._end_time = None
        self._channel_id = None
        self._provider_type = None
        self._source_name = None
        self.discriminator = None

        if filter is not None:
            self.filter = filter
        if period is not None:
            self.period = period
        self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        self.channel_id = channel_id
        if provider_type is not None:
            self.provider_type = provider_type
        if source_name is not None:
            self.source_name = source_name

    @property
    def filter(self):
        """Gets the filter of this ListPubMetricsRequest.

        指标数据统计方式

        :return: The filter of this ListPubMetricsRequest.
        :rtype: str
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this ListPubMetricsRequest.

        指标数据统计方式

        :param filter: The filter of this ListPubMetricsRequest.
        :type filter: str
        """
        self._filter = filter

    @property
    def period(self):
        """Gets the period of this ListPubMetricsRequest.

        指标数据统计周期（单位minute）

        :return: The period of this ListPubMetricsRequest.
        :rtype: int
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this ListPubMetricsRequest.

        指标数据统计周期（单位minute）

        :param period: The period of this ListPubMetricsRequest.
        :type period: int
        """
        self._period = period

    @property
    def start_time(self):
        """Gets the start_time of this ListPubMetricsRequest.

        获取指标数据起始时间

        :return: The start_time of this ListPubMetricsRequest.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ListPubMetricsRequest.

        获取指标数据起始时间

        :param start_time: The start_time of this ListPubMetricsRequest.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ListPubMetricsRequest.

        获取指标数据结束时间

        :return: The end_time of this ListPubMetricsRequest.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ListPubMetricsRequest.

        获取指标数据结束时间

        :param end_time: The end_time of this ListPubMetricsRequest.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def channel_id(self):
        """Gets the channel_id of this ListPubMetricsRequest.

        事件通道id

        :return: The channel_id of this ListPubMetricsRequest.
        :rtype: str
        """
        return self._channel_id

    @channel_id.setter
    def channel_id(self, channel_id):
        """Sets the channel_id of this ListPubMetricsRequest.

        事件通道id

        :param channel_id: The channel_id of this ListPubMetricsRequest.
        :type channel_id: str
        """
        self._channel_id = channel_id

    @property
    def provider_type(self):
        """Gets the provider_type of this ListPubMetricsRequest.

        事件目标类型/事件通道类型

        :return: The provider_type of this ListPubMetricsRequest.
        :rtype: str
        """
        return self._provider_type

    @provider_type.setter
    def provider_type(self, provider_type):
        """Sets the provider_type of this ListPubMetricsRequest.

        事件目标类型/事件通道类型

        :param provider_type: The provider_type of this ListPubMetricsRequest.
        :type provider_type: str
        """
        self._provider_type = provider_type

    @property
    def source_name(self):
        """Gets the source_name of this ListPubMetricsRequest.

        事件源名称

        :return: The source_name of this ListPubMetricsRequest.
        :rtype: str
        """
        return self._source_name

    @source_name.setter
    def source_name(self, source_name):
        """Sets the source_name of this ListPubMetricsRequest.

        事件源名称

        :param source_name: The source_name of this ListPubMetricsRequest.
        :type source_name: str
        """
        self._source_name = source_name

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
        if not isinstance(other, ListPubMetricsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
