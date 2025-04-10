# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchStatisticResourceInfoRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'offset': 'int',
        'limit': 'int',
        'time_unit': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'category': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'time_unit': 'timeUnit',
        'start_time': 'startTime',
        'end_time': 'endTime',
        'category': 'category'
    }

    def __init__(self, offset=None, limit=None, time_unit=None, start_time=None, end_time=None, category=None):
        r"""SearchStatisticResourceInfoRequest

        The model defined in huaweicloud sdk

        :param offset: 查询偏移量。 * 取值：大于等于0，默认值为0 * 大于等于最大条目数量，则返回最后一页数据，页数根据总条目数和limit计算得出
        :type offset: int
        :param limit: 查询的条目数量。 * 取值：1-500，默认值为20
        :type limit: int
        :param time_unit: 查询时间维度，取值： * D: 按日查询 * M: 按月查询
        :type time_unit: str
        :param start_time: 查询时间范围的开始时间，格式根据timeUnit的取值而定。 * timeUnit &#x3D; D，格式：yyyy-MM-dd，此情况下startTime与endTime间隔最多31日 * timeUnit &#x3D; M，格式：yyyy-MM，此情况下startTime与endTime间隔最多12个月
        :type start_time: str
        :param end_time: 查询时间范围的结束时间，格式根据timeUnit的取值而定。 * timeUnit &#x3D; D，格式：yyyy-MM-dd，此情况下startTime与endTime间隔最多31日 * timeUnit &#x3D; M，格式：yyyy-MM，此情况下startTime与endTime间隔最多12个月
        :type end_time: str
        :param category: 查询分类，取值： * used_vmr_info: 已购VMR资源使用统计数据 * used_live_info: 已购直播端口资源使用统计数据 * used_record_info: 已购录播资源使用统计数据 * used_pstn_info: 已购电话外呼资源使用统计数据
        :type category: str
        """
        
        

        self._offset = None
        self._limit = None
        self._time_unit = None
        self._start_time = None
        self._end_time = None
        self._category = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        self.time_unit = time_unit
        self.start_time = start_time
        self.end_time = end_time
        self.category = category

    @property
    def offset(self):
        r"""Gets the offset of this SearchStatisticResourceInfoRequest.

        查询偏移量。 * 取值：大于等于0，默认值为0 * 大于等于最大条目数量，则返回最后一页数据，页数根据总条目数和limit计算得出

        :return: The offset of this SearchStatisticResourceInfoRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this SearchStatisticResourceInfoRequest.

        查询偏移量。 * 取值：大于等于0，默认值为0 * 大于等于最大条目数量，则返回最后一页数据，页数根据总条目数和limit计算得出

        :param offset: The offset of this SearchStatisticResourceInfoRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this SearchStatisticResourceInfoRequest.

        查询的条目数量。 * 取值：1-500，默认值为20

        :return: The limit of this SearchStatisticResourceInfoRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this SearchStatisticResourceInfoRequest.

        查询的条目数量。 * 取值：1-500，默认值为20

        :param limit: The limit of this SearchStatisticResourceInfoRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def time_unit(self):
        r"""Gets the time_unit of this SearchStatisticResourceInfoRequest.

        查询时间维度，取值： * D: 按日查询 * M: 按月查询

        :return: The time_unit of this SearchStatisticResourceInfoRequest.
        :rtype: str
        """
        return self._time_unit

    @time_unit.setter
    def time_unit(self, time_unit):
        r"""Sets the time_unit of this SearchStatisticResourceInfoRequest.

        查询时间维度，取值： * D: 按日查询 * M: 按月查询

        :param time_unit: The time_unit of this SearchStatisticResourceInfoRequest.
        :type time_unit: str
        """
        self._time_unit = time_unit

    @property
    def start_time(self):
        r"""Gets the start_time of this SearchStatisticResourceInfoRequest.

        查询时间范围的开始时间，格式根据timeUnit的取值而定。 * timeUnit = D，格式：yyyy-MM-dd，此情况下startTime与endTime间隔最多31日 * timeUnit = M，格式：yyyy-MM，此情况下startTime与endTime间隔最多12个月

        :return: The start_time of this SearchStatisticResourceInfoRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this SearchStatisticResourceInfoRequest.

        查询时间范围的开始时间，格式根据timeUnit的取值而定。 * timeUnit = D，格式：yyyy-MM-dd，此情况下startTime与endTime间隔最多31日 * timeUnit = M，格式：yyyy-MM，此情况下startTime与endTime间隔最多12个月

        :param start_time: The start_time of this SearchStatisticResourceInfoRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this SearchStatisticResourceInfoRequest.

        查询时间范围的结束时间，格式根据timeUnit的取值而定。 * timeUnit = D，格式：yyyy-MM-dd，此情况下startTime与endTime间隔最多31日 * timeUnit = M，格式：yyyy-MM，此情况下startTime与endTime间隔最多12个月

        :return: The end_time of this SearchStatisticResourceInfoRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this SearchStatisticResourceInfoRequest.

        查询时间范围的结束时间，格式根据timeUnit的取值而定。 * timeUnit = D，格式：yyyy-MM-dd，此情况下startTime与endTime间隔最多31日 * timeUnit = M，格式：yyyy-MM，此情况下startTime与endTime间隔最多12个月

        :param end_time: The end_time of this SearchStatisticResourceInfoRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def category(self):
        r"""Gets the category of this SearchStatisticResourceInfoRequest.

        查询分类，取值： * used_vmr_info: 已购VMR资源使用统计数据 * used_live_info: 已购直播端口资源使用统计数据 * used_record_info: 已购录播资源使用统计数据 * used_pstn_info: 已购电话外呼资源使用统计数据

        :return: The category of this SearchStatisticResourceInfoRequest.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this SearchStatisticResourceInfoRequest.

        查询分类，取值： * used_vmr_info: 已购VMR资源使用统计数据 * used_live_info: 已购直播端口资源使用统计数据 * used_record_info: 已购录播资源使用统计数据 * used_pstn_info: 已购电话外呼资源使用统计数据

        :param category: The category of this SearchStatisticResourceInfoRequest.
        :type category: str
        """
        self._category = category

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
        if not isinstance(other, SearchStatisticResourceInfoRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
