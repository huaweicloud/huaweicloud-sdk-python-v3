# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListUserUsageMetricRequest:

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
        'username': 'str',
        'usage_min_hours': 'int',
        'usage_max_hours': 'int',
        'sort_field': 'str',
        'sort_type': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'start_time': 'start_time',
        'end_time': 'end_time',
        'username': 'username',
        'usage_min_hours': 'usage_min_hours',
        'usage_max_hours': 'usage_max_hours',
        'sort_field': 'sort_field',
        'sort_type': 'sort_type',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, start_time=None, end_time=None, username=None, usage_min_hours=None, usage_max_hours=None, sort_field=None, sort_type=None, offset=None, limit=None):
        r"""ListUserUsageMetricRequest

        The model defined in huaweicloud sdk

        :param start_time: 查询起始时间(0时区)。
        :type start_time: str
        :param end_time: 查询截至时间(0时区)。
        :type end_time: str
        :param username: 用户名(模糊匹配)。
        :type username: str
        :param usage_min_hours: 使用时长最小值。
        :type usage_min_hours: int
        :param usage_max_hours: 使用时长最大值 usage_min_hours和usage_max_hours同时存在时,usage_max_hours必须大于等于usage_min_hours
        :type usage_max_hours: int
        :param sort_field: 按照指标进行排序 * &#x60;user_usage&#x60; -  按照用户使用时长排序
        :type sort_field: str
        :param sort_type: 按照指标进行排序的方向;需配合sort_field一起使用 * &#x60;DESC&#x60; - 降序返回数据 * &#x60;ASC&#x60; -  升序返回数据
        :type sort_type: str
        :param offset: 查询的偏移量,默认值0。
        :type offset: int
        :param limit: limit范围[1-100],默认值0。
        :type limit: int
        """
        
        

        self._start_time = None
        self._end_time = None
        self._username = None
        self._usage_min_hours = None
        self._usage_max_hours = None
        self._sort_field = None
        self._sort_type = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.start_time = start_time
        self.end_time = end_time
        if username is not None:
            self.username = username
        if usage_min_hours is not None:
            self.usage_min_hours = usage_min_hours
        if usage_max_hours is not None:
            self.usage_max_hours = usage_max_hours
        if sort_field is not None:
            self.sort_field = sort_field
        if sort_type is not None:
            self.sort_type = sort_type
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def start_time(self):
        r"""Gets the start_time of this ListUserUsageMetricRequest.

        查询起始时间(0时区)。

        :return: The start_time of this ListUserUsageMetricRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListUserUsageMetricRequest.

        查询起始时间(0时区)。

        :param start_time: The start_time of this ListUserUsageMetricRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListUserUsageMetricRequest.

        查询截至时间(0时区)。

        :return: The end_time of this ListUserUsageMetricRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListUserUsageMetricRequest.

        查询截至时间(0时区)。

        :param end_time: The end_time of this ListUserUsageMetricRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def username(self):
        r"""Gets the username of this ListUserUsageMetricRequest.

        用户名(模糊匹配)。

        :return: The username of this ListUserUsageMetricRequest.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        r"""Sets the username of this ListUserUsageMetricRequest.

        用户名(模糊匹配)。

        :param username: The username of this ListUserUsageMetricRequest.
        :type username: str
        """
        self._username = username

    @property
    def usage_min_hours(self):
        r"""Gets the usage_min_hours of this ListUserUsageMetricRequest.

        使用时长最小值。

        :return: The usage_min_hours of this ListUserUsageMetricRequest.
        :rtype: int
        """
        return self._usage_min_hours

    @usage_min_hours.setter
    def usage_min_hours(self, usage_min_hours):
        r"""Sets the usage_min_hours of this ListUserUsageMetricRequest.

        使用时长最小值。

        :param usage_min_hours: The usage_min_hours of this ListUserUsageMetricRequest.
        :type usage_min_hours: int
        """
        self._usage_min_hours = usage_min_hours

    @property
    def usage_max_hours(self):
        r"""Gets the usage_max_hours of this ListUserUsageMetricRequest.

        使用时长最大值 usage_min_hours和usage_max_hours同时存在时,usage_max_hours必须大于等于usage_min_hours

        :return: The usage_max_hours of this ListUserUsageMetricRequest.
        :rtype: int
        """
        return self._usage_max_hours

    @usage_max_hours.setter
    def usage_max_hours(self, usage_max_hours):
        r"""Sets the usage_max_hours of this ListUserUsageMetricRequest.

        使用时长最大值 usage_min_hours和usage_max_hours同时存在时,usage_max_hours必须大于等于usage_min_hours

        :param usage_max_hours: The usage_max_hours of this ListUserUsageMetricRequest.
        :type usage_max_hours: int
        """
        self._usage_max_hours = usage_max_hours

    @property
    def sort_field(self):
        r"""Gets the sort_field of this ListUserUsageMetricRequest.

        按照指标进行排序 * `user_usage` -  按照用户使用时长排序

        :return: The sort_field of this ListUserUsageMetricRequest.
        :rtype: str
        """
        return self._sort_field

    @sort_field.setter
    def sort_field(self, sort_field):
        r"""Sets the sort_field of this ListUserUsageMetricRequest.

        按照指标进行排序 * `user_usage` -  按照用户使用时长排序

        :param sort_field: The sort_field of this ListUserUsageMetricRequest.
        :type sort_field: str
        """
        self._sort_field = sort_field

    @property
    def sort_type(self):
        r"""Gets the sort_type of this ListUserUsageMetricRequest.

        按照指标进行排序的方向;需配合sort_field一起使用 * `DESC` - 降序返回数据 * `ASC` -  升序返回数据

        :return: The sort_type of this ListUserUsageMetricRequest.
        :rtype: str
        """
        return self._sort_type

    @sort_type.setter
    def sort_type(self, sort_type):
        r"""Sets the sort_type of this ListUserUsageMetricRequest.

        按照指标进行排序的方向;需配合sort_field一起使用 * `DESC` - 降序返回数据 * `ASC` -  升序返回数据

        :param sort_type: The sort_type of this ListUserUsageMetricRequest.
        :type sort_type: str
        """
        self._sort_type = sort_type

    @property
    def offset(self):
        r"""Gets the offset of this ListUserUsageMetricRequest.

        查询的偏移量,默认值0。

        :return: The offset of this ListUserUsageMetricRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListUserUsageMetricRequest.

        查询的偏移量,默认值0。

        :param offset: The offset of this ListUserUsageMetricRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListUserUsageMetricRequest.

        limit范围[1-100],默认值0。

        :return: The limit of this ListUserUsageMetricRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListUserUsageMetricRequest.

        limit范围[1-100],默认值0。

        :param limit: The limit of this ListUserUsageMetricRequest.
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
        if not isinstance(other, ListUserUsageMetricRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
