# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportDesktopUsageMetricNewRequest:

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
        'resource_name': 'str',
        'min_idle_days': 'int',
        'max_idle_days': 'int',
        'usage_min_hours': 'int',
        'usage_max_hours': 'int',
        'enterprise_project_id': 'str',
        'sort_field': 'str',
        'sort_type': 'str'
    }

    attribute_map = {
        'start_time': 'start_time',
        'end_time': 'end_time',
        'resource_name': 'resource_name',
        'min_idle_days': 'min_idle_days',
        'max_idle_days': 'max_idle_days',
        'usage_min_hours': 'usage_min_hours',
        'usage_max_hours': 'usage_max_hours',
        'enterprise_project_id': 'enterprise_project_id',
        'sort_field': 'sort_field',
        'sort_type': 'sort_type'
    }

    def __init__(self, start_time=None, end_time=None, resource_name=None, min_idle_days=None, max_idle_days=None, usage_min_hours=None, usage_max_hours=None, enterprise_project_id=None, sort_field=None, sort_type=None):
        r"""ExportDesktopUsageMetricNewRequest

        The model defined in huaweicloud sdk

        :param start_time: 查询起始时间(0时区) 云服务每天凌晨02:00进行聚合运算前一天00:00:00~23:59:59的使用时长,并将周期范围内的数据聚合到周期边界上 跨天的记录会按照统计周期进行计算 假设一天内桌面登录多次，09:00~12:00,13:00~21:00,22:00~01:00(次日): 则当天的累计使用时长数据会被汇聚到23:59:59这个点;总使用时长为 3hours(09:00~12:00)+8hours(13:00~21:00)+2hours(22:00~00:00) 如果查询的from-to不足一个周期内，可能造成查询到数据为空；
        :type start_time: str
        :param end_time: 查询截止时间(0时区)。
        :type end_time: str
        :param resource_name: 资源名称(模糊匹配)。
        :type resource_name: str
        :param min_idle_days: 最小空闲天数。
        :type min_idle_days: int
        :param max_idle_days: 最大空闲天数 min_idle_days、max_idle_days都非空时,max_idle_days必须大于等于min_idle_days否则可能查询不到数据
        :type max_idle_days: int
        :param usage_min_hours: 使用时长(hour)最小值。
        :type usage_min_hours: int
        :param usage_max_hours: 使用时长(hour)最大值(必须大于等于usage_min_hours)。
        :type usage_max_hours: int
        :param enterprise_project_id: 企业项目ID。
        :type enterprise_project_id: str
        :param sort_field: 按照指标进行排序 * &#x60;desktop_usage&#x60; -  按照桌面使用时长排序 * &#x60;desktop_idle_duration&#x60; -  按照桌面空闲周期排序
        :type sort_field: str
        :param sort_type: 按照指标进行排序的方向;需配合sort_field起义使用 * &#x60;DESC&#x60; - 降序返回数据 * &#x60;ASC&#x60; -  升序返回数据
        :type sort_type: str
        """
        
        

        self._start_time = None
        self._end_time = None
        self._resource_name = None
        self._min_idle_days = None
        self._max_idle_days = None
        self._usage_min_hours = None
        self._usage_max_hours = None
        self._enterprise_project_id = None
        self._sort_field = None
        self._sort_type = None
        self.discriminator = None

        self.start_time = start_time
        self.end_time = end_time
        if resource_name is not None:
            self.resource_name = resource_name
        if min_idle_days is not None:
            self.min_idle_days = min_idle_days
        if max_idle_days is not None:
            self.max_idle_days = max_idle_days
        if usage_min_hours is not None:
            self.usage_min_hours = usage_min_hours
        if usage_max_hours is not None:
            self.usage_max_hours = usage_max_hours
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if sort_field is not None:
            self.sort_field = sort_field
        if sort_type is not None:
            self.sort_type = sort_type

    @property
    def start_time(self):
        r"""Gets the start_time of this ExportDesktopUsageMetricNewRequest.

        查询起始时间(0时区) 云服务每天凌晨02:00进行聚合运算前一天00:00:00~23:59:59的使用时长,并将周期范围内的数据聚合到周期边界上 跨天的记录会按照统计周期进行计算 假设一天内桌面登录多次，09:00~12:00,13:00~21:00,22:00~01:00(次日): 则当天的累计使用时长数据会被汇聚到23:59:59这个点;总使用时长为 3hours(09:00~12:00)+8hours(13:00~21:00)+2hours(22:00~00:00) 如果查询的from-to不足一个周期内，可能造成查询到数据为空；

        :return: The start_time of this ExportDesktopUsageMetricNewRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ExportDesktopUsageMetricNewRequest.

        查询起始时间(0时区) 云服务每天凌晨02:00进行聚合运算前一天00:00:00~23:59:59的使用时长,并将周期范围内的数据聚合到周期边界上 跨天的记录会按照统计周期进行计算 假设一天内桌面登录多次，09:00~12:00,13:00~21:00,22:00~01:00(次日): 则当天的累计使用时长数据会被汇聚到23:59:59这个点;总使用时长为 3hours(09:00~12:00)+8hours(13:00~21:00)+2hours(22:00~00:00) 如果查询的from-to不足一个周期内，可能造成查询到数据为空；

        :param start_time: The start_time of this ExportDesktopUsageMetricNewRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ExportDesktopUsageMetricNewRequest.

        查询截止时间(0时区)。

        :return: The end_time of this ExportDesktopUsageMetricNewRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ExportDesktopUsageMetricNewRequest.

        查询截止时间(0时区)。

        :param end_time: The end_time of this ExportDesktopUsageMetricNewRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def resource_name(self):
        r"""Gets the resource_name of this ExportDesktopUsageMetricNewRequest.

        资源名称(模糊匹配)。

        :return: The resource_name of this ExportDesktopUsageMetricNewRequest.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        r"""Sets the resource_name of this ExportDesktopUsageMetricNewRequest.

        资源名称(模糊匹配)。

        :param resource_name: The resource_name of this ExportDesktopUsageMetricNewRequest.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def min_idle_days(self):
        r"""Gets the min_idle_days of this ExportDesktopUsageMetricNewRequest.

        最小空闲天数。

        :return: The min_idle_days of this ExportDesktopUsageMetricNewRequest.
        :rtype: int
        """
        return self._min_idle_days

    @min_idle_days.setter
    def min_idle_days(self, min_idle_days):
        r"""Sets the min_idle_days of this ExportDesktopUsageMetricNewRequest.

        最小空闲天数。

        :param min_idle_days: The min_idle_days of this ExportDesktopUsageMetricNewRequest.
        :type min_idle_days: int
        """
        self._min_idle_days = min_idle_days

    @property
    def max_idle_days(self):
        r"""Gets the max_idle_days of this ExportDesktopUsageMetricNewRequest.

        最大空闲天数 min_idle_days、max_idle_days都非空时,max_idle_days必须大于等于min_idle_days否则可能查询不到数据

        :return: The max_idle_days of this ExportDesktopUsageMetricNewRequest.
        :rtype: int
        """
        return self._max_idle_days

    @max_idle_days.setter
    def max_idle_days(self, max_idle_days):
        r"""Sets the max_idle_days of this ExportDesktopUsageMetricNewRequest.

        最大空闲天数 min_idle_days、max_idle_days都非空时,max_idle_days必须大于等于min_idle_days否则可能查询不到数据

        :param max_idle_days: The max_idle_days of this ExportDesktopUsageMetricNewRequest.
        :type max_idle_days: int
        """
        self._max_idle_days = max_idle_days

    @property
    def usage_min_hours(self):
        r"""Gets the usage_min_hours of this ExportDesktopUsageMetricNewRequest.

        使用时长(hour)最小值。

        :return: The usage_min_hours of this ExportDesktopUsageMetricNewRequest.
        :rtype: int
        """
        return self._usage_min_hours

    @usage_min_hours.setter
    def usage_min_hours(self, usage_min_hours):
        r"""Sets the usage_min_hours of this ExportDesktopUsageMetricNewRequest.

        使用时长(hour)最小值。

        :param usage_min_hours: The usage_min_hours of this ExportDesktopUsageMetricNewRequest.
        :type usage_min_hours: int
        """
        self._usage_min_hours = usage_min_hours

    @property
    def usage_max_hours(self):
        r"""Gets the usage_max_hours of this ExportDesktopUsageMetricNewRequest.

        使用时长(hour)最大值(必须大于等于usage_min_hours)。

        :return: The usage_max_hours of this ExportDesktopUsageMetricNewRequest.
        :rtype: int
        """
        return self._usage_max_hours

    @usage_max_hours.setter
    def usage_max_hours(self, usage_max_hours):
        r"""Sets the usage_max_hours of this ExportDesktopUsageMetricNewRequest.

        使用时长(hour)最大值(必须大于等于usage_min_hours)。

        :param usage_max_hours: The usage_max_hours of this ExportDesktopUsageMetricNewRequest.
        :type usage_max_hours: int
        """
        self._usage_max_hours = usage_max_hours

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ExportDesktopUsageMetricNewRequest.

        企业项目ID。

        :return: The enterprise_project_id of this ExportDesktopUsageMetricNewRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ExportDesktopUsageMetricNewRequest.

        企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this ExportDesktopUsageMetricNewRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def sort_field(self):
        r"""Gets the sort_field of this ExportDesktopUsageMetricNewRequest.

        按照指标进行排序 * `desktop_usage` -  按照桌面使用时长排序 * `desktop_idle_duration` -  按照桌面空闲周期排序

        :return: The sort_field of this ExportDesktopUsageMetricNewRequest.
        :rtype: str
        """
        return self._sort_field

    @sort_field.setter
    def sort_field(self, sort_field):
        r"""Sets the sort_field of this ExportDesktopUsageMetricNewRequest.

        按照指标进行排序 * `desktop_usage` -  按照桌面使用时长排序 * `desktop_idle_duration` -  按照桌面空闲周期排序

        :param sort_field: The sort_field of this ExportDesktopUsageMetricNewRequest.
        :type sort_field: str
        """
        self._sort_field = sort_field

    @property
    def sort_type(self):
        r"""Gets the sort_type of this ExportDesktopUsageMetricNewRequest.

        按照指标进行排序的方向;需配合sort_field起义使用 * `DESC` - 降序返回数据 * `ASC` -  升序返回数据

        :return: The sort_type of this ExportDesktopUsageMetricNewRequest.
        :rtype: str
        """
        return self._sort_type

    @sort_type.setter
    def sort_type(self, sort_type):
        r"""Sets the sort_type of this ExportDesktopUsageMetricNewRequest.

        按照指标进行排序的方向;需配合sort_field起义使用 * `DESC` - 降序返回数据 * `ASC` -  升序返回数据

        :param sort_type: The sort_type of this ExportDesktopUsageMetricNewRequest.
        :type sort_type: str
        """
        self._sort_type = sort_type

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ExportDesktopUsageMetricNewRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
