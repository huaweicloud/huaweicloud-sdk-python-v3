# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TimelineTrafficStatisticsRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'start_time': 'int',
        'end_time': 'int',
        'period': 'int',
        'resource_type': 'str',
        'search_type': 'str',
        'resource_id': 'str'
    }

    attribute_map = {
        'start_time': 'start_time',
        'end_time': 'end_time',
        'period': 'period',
        'resource_type': 'resource_type',
        'search_type': 'search_type',
        'resource_id': 'resource_id'
    }

    def __init__(self, start_time=None, end_time=None, period=None, resource_type=None, search_type=None, resource_id=None):
        """TimelineTrafficStatisticsRequestBody

        The model defined in huaweicloud sdk

        :param start_time: 开始时间时间戳，毫秒时间，最多支持30天范围内的查询
        :type start_time: int
        :param end_time: 结束时间时间戳，毫秒时间
        :type end_time: int
        :param period: 查询时间间隔，单位为小时，范围为1-24
        :type period: int
        :param resource_type: 资源类型，log_group / log_stream / tenant
        :type resource_type: str
        :param search_type: 查询流量类型值为：write，index，storage
        :type search_type: str
        :param resource_id: 资源ID
        :type resource_id: str
        """
        
        

        self._start_time = None
        self._end_time = None
        self._period = None
        self._resource_type = None
        self._search_type = None
        self._resource_id = None
        self.discriminator = None

        self.start_time = start_time
        self.end_time = end_time
        self.period = period
        self.resource_type = resource_type
        self.search_type = search_type
        if resource_id is not None:
            self.resource_id = resource_id

    @property
    def start_time(self):
        """Gets the start_time of this TimelineTrafficStatisticsRequestBody.

        开始时间时间戳，毫秒时间，最多支持30天范围内的查询

        :return: The start_time of this TimelineTrafficStatisticsRequestBody.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this TimelineTrafficStatisticsRequestBody.

        开始时间时间戳，毫秒时间，最多支持30天范围内的查询

        :param start_time: The start_time of this TimelineTrafficStatisticsRequestBody.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this TimelineTrafficStatisticsRequestBody.

        结束时间时间戳，毫秒时间

        :return: The end_time of this TimelineTrafficStatisticsRequestBody.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this TimelineTrafficStatisticsRequestBody.

        结束时间时间戳，毫秒时间

        :param end_time: The end_time of this TimelineTrafficStatisticsRequestBody.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def period(self):
        """Gets the period of this TimelineTrafficStatisticsRequestBody.

        查询时间间隔，单位为小时，范围为1-24

        :return: The period of this TimelineTrafficStatisticsRequestBody.
        :rtype: int
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this TimelineTrafficStatisticsRequestBody.

        查询时间间隔，单位为小时，范围为1-24

        :param period: The period of this TimelineTrafficStatisticsRequestBody.
        :type period: int
        """
        self._period = period

    @property
    def resource_type(self):
        """Gets the resource_type of this TimelineTrafficStatisticsRequestBody.

        资源类型，log_group / log_stream / tenant

        :return: The resource_type of this TimelineTrafficStatisticsRequestBody.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this TimelineTrafficStatisticsRequestBody.

        资源类型，log_group / log_stream / tenant

        :param resource_type: The resource_type of this TimelineTrafficStatisticsRequestBody.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def search_type(self):
        """Gets the search_type of this TimelineTrafficStatisticsRequestBody.

        查询流量类型值为：write，index，storage

        :return: The search_type of this TimelineTrafficStatisticsRequestBody.
        :rtype: str
        """
        return self._search_type

    @search_type.setter
    def search_type(self, search_type):
        """Sets the search_type of this TimelineTrafficStatisticsRequestBody.

        查询流量类型值为：write，index，storage

        :param search_type: The search_type of this TimelineTrafficStatisticsRequestBody.
        :type search_type: str
        """
        self._search_type = search_type

    @property
    def resource_id(self):
        """Gets the resource_id of this TimelineTrafficStatisticsRequestBody.

        资源ID

        :return: The resource_id of this TimelineTrafficStatisticsRequestBody.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this TimelineTrafficStatisticsRequestBody.

        资源ID

        :param resource_id: The resource_id of this TimelineTrafficStatisticsRequestBody.
        :type resource_id: str
        """
        self._resource_id = resource_id

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
        if not isinstance(other, TimelineTrafficStatisticsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
