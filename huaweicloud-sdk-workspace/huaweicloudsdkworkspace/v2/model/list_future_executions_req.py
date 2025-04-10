# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFutureExecutionsReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'scheduled_type': 'str',
        'day_interval': 'int',
        'week_list': 'str',
        'month_list': 'str',
        'date_list': 'str',
        'scheduled_date': 'str',
        'scheduled_time': 'str',
        'expire_time': 'str',
        'gray_count': 'int',
        'gray_desktop_ids': 'list[str]',
        'gray_fail_threshold': 'int',
        'life_cycle_type': 'str',
        'time_zone': 'str'
    }

    attribute_map = {
        'scheduled_type': 'scheduled_type',
        'day_interval': 'day_interval',
        'week_list': 'week_list',
        'month_list': 'month_list',
        'date_list': 'date_list',
        'scheduled_date': 'scheduled_date',
        'scheduled_time': 'scheduled_time',
        'expire_time': 'expire_time',
        'gray_count': 'gray_count',
        'gray_desktop_ids': 'gray_desktop_ids',
        'gray_fail_threshold': 'gray_fail_threshold',
        'life_cycle_type': 'life_cycle_type',
        'time_zone': 'time_zone'
    }

    def __init__(self, scheduled_type=None, day_interval=None, week_list=None, month_list=None, date_list=None, scheduled_date=None, scheduled_time=None, expire_time=None, gray_count=None, gray_desktop_ids=None, gray_fail_threshold=None, life_cycle_type=None, time_zone=None):
        r"""ListFutureExecutionsReq

        The model defined in huaweicloud sdk

        :param scheduled_type: 执行周期类型，可选值为： - FIXED_TIME：指定时间。 - DAY：按天。 - WEEK：按周。 - MONTH：按月。 - LIFE_CYCLE：指定场景下触发。
        :type scheduled_type: str
        :param day_interval: 周期按天时：按x天间隔执行。
        :type day_interval: int
        :param week_list: 周期按周时：取值1~7，分别对应周日~周六，英文逗号分隔，如1,2,7。
        :type week_list: str
        :param month_list: 周期按月时：取值1~12，英文逗号分隔，如1,3,12。
        :type month_list: str
        :param date_list: 周期按月时：取值1~31及L(代表当月最后一天)，英文逗号分隔，如1,2,28,L。
        :type date_list: str
        :param scheduled_date: 周期指定时间时：表示指定的日期，格式为yyyy-MM-dd。
        :type scheduled_date: str
        :param scheduled_time: 指定的执行时间点，格式为HH:mm:ss。
        :type scheduled_time: str
        :param expire_time: 到期时间，格式为yyyy-MM-dd HH:mm:ss。
        :type expire_time: str
        :param gray_count: 灰度对象数量，优先级高于gray_desktop_ids。只支持脚本执行。
        :type gray_count: int
        :param gray_desktop_ids: 灰度执行的桌面id列表，优先级低于gray_count。只支持脚本执行。
        :type gray_desktop_ids: list[str]
        :param gray_fail_threshold: 灰度失败阈值，灰度执行失败次数达到该值时，不执行下一批任务。只支持脚本执行。
        :type gray_fail_threshold: int
        :param life_cycle_type: 触发场景。POST_CREATE_DESKTOP_SUCCESS：创建桌面成功后，POST_REBUILD_DESKTOP_SUCCESS：重建桌面成功后，POST_REATTACH_DESKTOP_SUCCESS：触发重建的分配用户任务成功后，POST_DESKTOP_DISCONNECTED：桌面断开连接后。
        :type life_cycle_type: str
        :param time_zone: 时区。
        :type time_zone: str
        """
        
        

        self._scheduled_type = None
        self._day_interval = None
        self._week_list = None
        self._month_list = None
        self._date_list = None
        self._scheduled_date = None
        self._scheduled_time = None
        self._expire_time = None
        self._gray_count = None
        self._gray_desktop_ids = None
        self._gray_fail_threshold = None
        self._life_cycle_type = None
        self._time_zone = None
        self.discriminator = None

        if scheduled_type is not None:
            self.scheduled_type = scheduled_type
        if day_interval is not None:
            self.day_interval = day_interval
        if week_list is not None:
            self.week_list = week_list
        if month_list is not None:
            self.month_list = month_list
        if date_list is not None:
            self.date_list = date_list
        if scheduled_date is not None:
            self.scheduled_date = scheduled_date
        if scheduled_time is not None:
            self.scheduled_time = scheduled_time
        if expire_time is not None:
            self.expire_time = expire_time
        if gray_count is not None:
            self.gray_count = gray_count
        if gray_desktop_ids is not None:
            self.gray_desktop_ids = gray_desktop_ids
        if gray_fail_threshold is not None:
            self.gray_fail_threshold = gray_fail_threshold
        if life_cycle_type is not None:
            self.life_cycle_type = life_cycle_type
        if time_zone is not None:
            self.time_zone = time_zone

    @property
    def scheduled_type(self):
        r"""Gets the scheduled_type of this ListFutureExecutionsReq.

        执行周期类型，可选值为： - FIXED_TIME：指定时间。 - DAY：按天。 - WEEK：按周。 - MONTH：按月。 - LIFE_CYCLE：指定场景下触发。

        :return: The scheduled_type of this ListFutureExecutionsReq.
        :rtype: str
        """
        return self._scheduled_type

    @scheduled_type.setter
    def scheduled_type(self, scheduled_type):
        r"""Sets the scheduled_type of this ListFutureExecutionsReq.

        执行周期类型，可选值为： - FIXED_TIME：指定时间。 - DAY：按天。 - WEEK：按周。 - MONTH：按月。 - LIFE_CYCLE：指定场景下触发。

        :param scheduled_type: The scheduled_type of this ListFutureExecutionsReq.
        :type scheduled_type: str
        """
        self._scheduled_type = scheduled_type

    @property
    def day_interval(self):
        r"""Gets the day_interval of this ListFutureExecutionsReq.

        周期按天时：按x天间隔执行。

        :return: The day_interval of this ListFutureExecutionsReq.
        :rtype: int
        """
        return self._day_interval

    @day_interval.setter
    def day_interval(self, day_interval):
        r"""Sets the day_interval of this ListFutureExecutionsReq.

        周期按天时：按x天间隔执行。

        :param day_interval: The day_interval of this ListFutureExecutionsReq.
        :type day_interval: int
        """
        self._day_interval = day_interval

    @property
    def week_list(self):
        r"""Gets the week_list of this ListFutureExecutionsReq.

        周期按周时：取值1~7，分别对应周日~周六，英文逗号分隔，如1,2,7。

        :return: The week_list of this ListFutureExecutionsReq.
        :rtype: str
        """
        return self._week_list

    @week_list.setter
    def week_list(self, week_list):
        r"""Sets the week_list of this ListFutureExecutionsReq.

        周期按周时：取值1~7，分别对应周日~周六，英文逗号分隔，如1,2,7。

        :param week_list: The week_list of this ListFutureExecutionsReq.
        :type week_list: str
        """
        self._week_list = week_list

    @property
    def month_list(self):
        r"""Gets the month_list of this ListFutureExecutionsReq.

        周期按月时：取值1~12，英文逗号分隔，如1,3,12。

        :return: The month_list of this ListFutureExecutionsReq.
        :rtype: str
        """
        return self._month_list

    @month_list.setter
    def month_list(self, month_list):
        r"""Sets the month_list of this ListFutureExecutionsReq.

        周期按月时：取值1~12，英文逗号分隔，如1,3,12。

        :param month_list: The month_list of this ListFutureExecutionsReq.
        :type month_list: str
        """
        self._month_list = month_list

    @property
    def date_list(self):
        r"""Gets the date_list of this ListFutureExecutionsReq.

        周期按月时：取值1~31及L(代表当月最后一天)，英文逗号分隔，如1,2,28,L。

        :return: The date_list of this ListFutureExecutionsReq.
        :rtype: str
        """
        return self._date_list

    @date_list.setter
    def date_list(self, date_list):
        r"""Sets the date_list of this ListFutureExecutionsReq.

        周期按月时：取值1~31及L(代表当月最后一天)，英文逗号分隔，如1,2,28,L。

        :param date_list: The date_list of this ListFutureExecutionsReq.
        :type date_list: str
        """
        self._date_list = date_list

    @property
    def scheduled_date(self):
        r"""Gets the scheduled_date of this ListFutureExecutionsReq.

        周期指定时间时：表示指定的日期，格式为yyyy-MM-dd。

        :return: The scheduled_date of this ListFutureExecutionsReq.
        :rtype: str
        """
        return self._scheduled_date

    @scheduled_date.setter
    def scheduled_date(self, scheduled_date):
        r"""Sets the scheduled_date of this ListFutureExecutionsReq.

        周期指定时间时：表示指定的日期，格式为yyyy-MM-dd。

        :param scheduled_date: The scheduled_date of this ListFutureExecutionsReq.
        :type scheduled_date: str
        """
        self._scheduled_date = scheduled_date

    @property
    def scheduled_time(self):
        r"""Gets the scheduled_time of this ListFutureExecutionsReq.

        指定的执行时间点，格式为HH:mm:ss。

        :return: The scheduled_time of this ListFutureExecutionsReq.
        :rtype: str
        """
        return self._scheduled_time

    @scheduled_time.setter
    def scheduled_time(self, scheduled_time):
        r"""Sets the scheduled_time of this ListFutureExecutionsReq.

        指定的执行时间点，格式为HH:mm:ss。

        :param scheduled_time: The scheduled_time of this ListFutureExecutionsReq.
        :type scheduled_time: str
        """
        self._scheduled_time = scheduled_time

    @property
    def expire_time(self):
        r"""Gets the expire_time of this ListFutureExecutionsReq.

        到期时间，格式为yyyy-MM-dd HH:mm:ss。

        :return: The expire_time of this ListFutureExecutionsReq.
        :rtype: str
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        r"""Sets the expire_time of this ListFutureExecutionsReq.

        到期时间，格式为yyyy-MM-dd HH:mm:ss。

        :param expire_time: The expire_time of this ListFutureExecutionsReq.
        :type expire_time: str
        """
        self._expire_time = expire_time

    @property
    def gray_count(self):
        r"""Gets the gray_count of this ListFutureExecutionsReq.

        灰度对象数量，优先级高于gray_desktop_ids。只支持脚本执行。

        :return: The gray_count of this ListFutureExecutionsReq.
        :rtype: int
        """
        return self._gray_count

    @gray_count.setter
    def gray_count(self, gray_count):
        r"""Sets the gray_count of this ListFutureExecutionsReq.

        灰度对象数量，优先级高于gray_desktop_ids。只支持脚本执行。

        :param gray_count: The gray_count of this ListFutureExecutionsReq.
        :type gray_count: int
        """
        self._gray_count = gray_count

    @property
    def gray_desktop_ids(self):
        r"""Gets the gray_desktop_ids of this ListFutureExecutionsReq.

        灰度执行的桌面id列表，优先级低于gray_count。只支持脚本执行。

        :return: The gray_desktop_ids of this ListFutureExecutionsReq.
        :rtype: list[str]
        """
        return self._gray_desktop_ids

    @gray_desktop_ids.setter
    def gray_desktop_ids(self, gray_desktop_ids):
        r"""Sets the gray_desktop_ids of this ListFutureExecutionsReq.

        灰度执行的桌面id列表，优先级低于gray_count。只支持脚本执行。

        :param gray_desktop_ids: The gray_desktop_ids of this ListFutureExecutionsReq.
        :type gray_desktop_ids: list[str]
        """
        self._gray_desktop_ids = gray_desktop_ids

    @property
    def gray_fail_threshold(self):
        r"""Gets the gray_fail_threshold of this ListFutureExecutionsReq.

        灰度失败阈值，灰度执行失败次数达到该值时，不执行下一批任务。只支持脚本执行。

        :return: The gray_fail_threshold of this ListFutureExecutionsReq.
        :rtype: int
        """
        return self._gray_fail_threshold

    @gray_fail_threshold.setter
    def gray_fail_threshold(self, gray_fail_threshold):
        r"""Sets the gray_fail_threshold of this ListFutureExecutionsReq.

        灰度失败阈值，灰度执行失败次数达到该值时，不执行下一批任务。只支持脚本执行。

        :param gray_fail_threshold: The gray_fail_threshold of this ListFutureExecutionsReq.
        :type gray_fail_threshold: int
        """
        self._gray_fail_threshold = gray_fail_threshold

    @property
    def life_cycle_type(self):
        r"""Gets the life_cycle_type of this ListFutureExecutionsReq.

        触发场景。POST_CREATE_DESKTOP_SUCCESS：创建桌面成功后，POST_REBUILD_DESKTOP_SUCCESS：重建桌面成功后，POST_REATTACH_DESKTOP_SUCCESS：触发重建的分配用户任务成功后，POST_DESKTOP_DISCONNECTED：桌面断开连接后。

        :return: The life_cycle_type of this ListFutureExecutionsReq.
        :rtype: str
        """
        return self._life_cycle_type

    @life_cycle_type.setter
    def life_cycle_type(self, life_cycle_type):
        r"""Sets the life_cycle_type of this ListFutureExecutionsReq.

        触发场景。POST_CREATE_DESKTOP_SUCCESS：创建桌面成功后，POST_REBUILD_DESKTOP_SUCCESS：重建桌面成功后，POST_REATTACH_DESKTOP_SUCCESS：触发重建的分配用户任务成功后，POST_DESKTOP_DISCONNECTED：桌面断开连接后。

        :param life_cycle_type: The life_cycle_type of this ListFutureExecutionsReq.
        :type life_cycle_type: str
        """
        self._life_cycle_type = life_cycle_type

    @property
    def time_zone(self):
        r"""Gets the time_zone of this ListFutureExecutionsReq.

        时区。

        :return: The time_zone of this ListFutureExecutionsReq.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        r"""Sets the time_zone of this ListFutureExecutionsReq.

        时区。

        :param time_zone: The time_zone of this ListFutureExecutionsReq.
        :type time_zone: str
        """
        self._time_zone = time_zone

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
        if not isinstance(other, ListFutureExecutionsReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
