# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRpoStatisticsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'offset': 'int',
        'start_time': 'str',
        'end_time': 'str',
        'resource_type': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'resource_type': 'resource_type'
    }

    def __init__(self, limit=None, offset=None, start_time=None, end_time=None, resource_type=None):
        r"""ListRpoStatisticsRequest

        The model defined in huaweicloud sdk

        :param limit: 每次请求返回结果个数限制，取值范围为[0,1000]的正整数，默认值为1000。
        :type limit: int
        :param offset: 每次请求开始的下标，即偏移量，默认值为0。offset必须为数字，不能为负数。
        :type offset: int
        :param start_time: 开始时间。默认格式为：\&quot;yyyy-MM-dd HH:mm:ss.SSS\&quot;，例：\&quot;2019-04-01 12:00:00.000\&quot;。
        :type start_time: str
        :param end_time: 结束时间。默认格式为：\&quot;yyyy-MM-dd HH:mm:ss.SSS\&quot;，例：\&quot;2019-04-01 12:00:00.000\&quot;。
        :type end_time: str
        :param resource_type: 资源类型。replication：表示查询复制对的RPO超标趋势记录。
        :type resource_type: str
        """
        
        

        self._limit = None
        self._offset = None
        self._start_time = None
        self._end_time = None
        self._resource_type = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if resource_type is not None:
            self.resource_type = resource_type

    @property
    def limit(self):
        r"""Gets the limit of this ListRpoStatisticsRequest.

        每次请求返回结果个数限制，取值范围为[0,1000]的正整数，默认值为1000。

        :return: The limit of this ListRpoStatisticsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListRpoStatisticsRequest.

        每次请求返回结果个数限制，取值范围为[0,1000]的正整数，默认值为1000。

        :param limit: The limit of this ListRpoStatisticsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListRpoStatisticsRequest.

        每次请求开始的下标，即偏移量，默认值为0。offset必须为数字，不能为负数。

        :return: The offset of this ListRpoStatisticsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListRpoStatisticsRequest.

        每次请求开始的下标，即偏移量，默认值为0。offset必须为数字，不能为负数。

        :param offset: The offset of this ListRpoStatisticsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def start_time(self):
        r"""Gets the start_time of this ListRpoStatisticsRequest.

        开始时间。默认格式为：\"yyyy-MM-dd HH:mm:ss.SSS\"，例：\"2019-04-01 12:00:00.000\"。

        :return: The start_time of this ListRpoStatisticsRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListRpoStatisticsRequest.

        开始时间。默认格式为：\"yyyy-MM-dd HH:mm:ss.SSS\"，例：\"2019-04-01 12:00:00.000\"。

        :param start_time: The start_time of this ListRpoStatisticsRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListRpoStatisticsRequest.

        结束时间。默认格式为：\"yyyy-MM-dd HH:mm:ss.SSS\"，例：\"2019-04-01 12:00:00.000\"。

        :return: The end_time of this ListRpoStatisticsRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListRpoStatisticsRequest.

        结束时间。默认格式为：\"yyyy-MM-dd HH:mm:ss.SSS\"，例：\"2019-04-01 12:00:00.000\"。

        :param end_time: The end_time of this ListRpoStatisticsRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def resource_type(self):
        r"""Gets the resource_type of this ListRpoStatisticsRequest.

        资源类型。replication：表示查询复制对的RPO超标趋势记录。

        :return: The resource_type of this ListRpoStatisticsRequest.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this ListRpoStatisticsRequest.

        资源类型。replication：表示查询复制对的RPO超标趋势记录。

        :param resource_type: The resource_type of this ListRpoStatisticsRequest.
        :type resource_type: str
        """
        self._resource_type = resource_type

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
        if not isinstance(other, ListRpoStatisticsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
