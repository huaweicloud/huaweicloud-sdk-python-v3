# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAssetDailySummaryLogRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'start_time': 'str',
        'end_time': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'start_time': 'start_time',
        'end_time': 'end_time',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, start_time=None, end_time=None, offset=None, limit=None):
        """ListAssetDailySummaryLogRequest

        The model defined in huaweicloud sdk

        :param start_time: 查询开始时间。仅支持查询一年内的数据，且一次查询的日期跨度不能超过90天。  如果查询指定开始日期的数据，格式为：yyyyMMdd000000。
        :type start_time: str
        :param end_time: 查询结束时间。仅支持查询一年内的数据，且一次查询的日期跨度不能超过90天。  如果查询指定结束日期的数据，格式为：yyyyMMdd000000。
        :type end_time: str
        :param offset: 偏移量，表示查询该偏移量后面的记录。 
        :type offset: int
        :param limit: 查询返回记录的数量限制。 
        :type limit: int
        """
        
        

        self._start_time = None
        self._end_time = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.start_time = start_time
        self.end_time = end_time
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def start_time(self):
        """Gets the start_time of this ListAssetDailySummaryLogRequest.

        查询开始时间。仅支持查询一年内的数据，且一次查询的日期跨度不能超过90天。  如果查询指定开始日期的数据，格式为：yyyyMMdd000000。

        :return: The start_time of this ListAssetDailySummaryLogRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ListAssetDailySummaryLogRequest.

        查询开始时间。仅支持查询一年内的数据，且一次查询的日期跨度不能超过90天。  如果查询指定开始日期的数据，格式为：yyyyMMdd000000。

        :param start_time: The start_time of this ListAssetDailySummaryLogRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ListAssetDailySummaryLogRequest.

        查询结束时间。仅支持查询一年内的数据，且一次查询的日期跨度不能超过90天。  如果查询指定结束日期的数据，格式为：yyyyMMdd000000。

        :return: The end_time of this ListAssetDailySummaryLogRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ListAssetDailySummaryLogRequest.

        查询结束时间。仅支持查询一年内的数据，且一次查询的日期跨度不能超过90天。  如果查询指定结束日期的数据，格式为：yyyyMMdd000000。

        :param end_time: The end_time of this ListAssetDailySummaryLogRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def offset(self):
        """Gets the offset of this ListAssetDailySummaryLogRequest.

        偏移量，表示查询该偏移量后面的记录。 

        :return: The offset of this ListAssetDailySummaryLogRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListAssetDailySummaryLogRequest.

        偏移量，表示查询该偏移量后面的记录。 

        :param offset: The offset of this ListAssetDailySummaryLogRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListAssetDailySummaryLogRequest.

        查询返回记录的数量限制。 

        :return: The limit of this ListAssetDailySummaryLogRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListAssetDailySummaryLogRequest.

        查询返回记录的数量限制。 

        :param limit: The limit of this ListAssetDailySummaryLogRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListAssetDailySummaryLogRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
