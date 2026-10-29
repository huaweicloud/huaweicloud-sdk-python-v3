# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class KeywordsResBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'log_stream_id': 'str',
        'log_stream_name': 'str',
        'log_group_id': 'str',
        'log_group_name': 'str',
        'keywords': 'str',
        'condition': 'str',
        'number': 'int',
        'search_time_range': 'int',
        'search_time_range_unit': 'str',
        'custom_date': 'CustomDate',
        'is_time_range_relative': 'bool',
        'conditions': 'list[KeywordsAlarmConditions]',
        'log_group_name_alias': 'str',
        'log_stream_name_alias': 'str',
        'eps_id': 'str',
        'time_range': 'TimeRange'
    }

    attribute_map = {
        'log_stream_id': 'log_stream_id',
        'log_stream_name': 'log_stream_name',
        'log_group_id': 'log_group_id',
        'log_group_name': 'log_group_name',
        'keywords': 'keywords',
        'condition': 'condition',
        'number': 'number',
        'search_time_range': 'search_time_range',
        'search_time_range_unit': 'search_time_range_unit',
        'custom_date': 'custom_date',
        'is_time_range_relative': 'is_time_range_relative',
        'conditions': 'conditions',
        'log_group_name_alias': 'log_group_name_alias',
        'log_stream_name_alias': 'log_stream_name_alias',
        'eps_id': 'eps_id',
        'time_range': 'time_range'
    }

    def __init__(self, log_stream_id=None, log_stream_name=None, log_group_id=None, log_group_name=None, keywords=None, condition=None, number=None, search_time_range=None, search_time_range_unit=None, custom_date=None, is_time_range_relative=None, conditions=None, log_group_name_alias=None, log_stream_name_alias=None, eps_id=None, time_range=None):
        r"""KeywordsResBody

        The model defined in huaweicloud sdk

        :param log_stream_id: 日志流id
        :type log_stream_id: str
        :param log_stream_name: 日志流名称
        :type log_stream_name: str
        :param log_group_id: 日志组id
        :type log_group_id: str
        :param log_group_name: 日志组名称
        :type log_group_name: str
        :param keywords: 关键词
        :type keywords: str
        :param condition: 条件
        :type condition: str
        :param number: 行数
        :type number: int
        :param search_time_range: 查询执行任务时最近数据的时间范围，最大值为60
        :type search_time_range: int
        :param search_time_range_unit: 查询时间单位
        :type search_time_range_unit: str
        :param custom_date: 
        :type custom_date: :class:`huaweicloudsdklts.v2.CustomDate`
        :param is_time_range_relative: **参数解释：** 是否是相对时间。（暂不开放，后续aom上线该功能后一起开放） **约束限制：** 不涉及。 **取值范围：** - true - false **默认取值：** true
        :type is_time_range_relative: bool
        :param conditions: **参数解释：** 支持根据不同条件触发不同级别的告警。当使用该参数时，将优先使用该参数中的条件触发告警，无视keywords_alarm_level参数以及keywords_requests中的condition、number参数。 **约束限制：** 不涉及。
        :type conditions: list[:class:`huaweicloudsdklts.v2.KeywordsAlarmConditions`]
        :param log_group_name_alias: **参数解释：** 日志组别名。 **取值范围：** 不涉及。
        :type log_group_name_alias: str
        :param log_stream_name_alias: **参数解释：** 日志流别名。 **取值范围：** 不涉及。
        :type log_stream_name_alias: str
        :param eps_id: **参数解释：** 企业项目ID。 **取值范围：** 不涉及。
        :type eps_id: str
        :param time_range: 
        :type time_range: :class:`huaweicloudsdklts.v2.TimeRange`
        """
        
        

        self._log_stream_id = None
        self._log_stream_name = None
        self._log_group_id = None
        self._log_group_name = None
        self._keywords = None
        self._condition = None
        self._number = None
        self._search_time_range = None
        self._search_time_range_unit = None
        self._custom_date = None
        self._is_time_range_relative = None
        self._conditions = None
        self._log_group_name_alias = None
        self._log_stream_name_alias = None
        self._eps_id = None
        self._time_range = None
        self.discriminator = None

        if log_stream_id is not None:
            self.log_stream_id = log_stream_id
        if log_stream_name is not None:
            self.log_stream_name = log_stream_name
        if log_group_id is not None:
            self.log_group_id = log_group_id
        if log_group_name is not None:
            self.log_group_name = log_group_name
        if keywords is not None:
            self.keywords = keywords
        if condition is not None:
            self.condition = condition
        if number is not None:
            self.number = number
        if search_time_range is not None:
            self.search_time_range = search_time_range
        if search_time_range_unit is not None:
            self.search_time_range_unit = search_time_range_unit
        if custom_date is not None:
            self.custom_date = custom_date
        if is_time_range_relative is not None:
            self.is_time_range_relative = is_time_range_relative
        if conditions is not None:
            self.conditions = conditions
        if log_group_name_alias is not None:
            self.log_group_name_alias = log_group_name_alias
        if log_stream_name_alias is not None:
            self.log_stream_name_alias = log_stream_name_alias
        if eps_id is not None:
            self.eps_id = eps_id
        if time_range is not None:
            self.time_range = time_range

    @property
    def log_stream_id(self):
        r"""Gets the log_stream_id of this KeywordsResBody.

        日志流id

        :return: The log_stream_id of this KeywordsResBody.
        :rtype: str
        """
        return self._log_stream_id

    @log_stream_id.setter
    def log_stream_id(self, log_stream_id):
        r"""Sets the log_stream_id of this KeywordsResBody.

        日志流id

        :param log_stream_id: The log_stream_id of this KeywordsResBody.
        :type log_stream_id: str
        """
        self._log_stream_id = log_stream_id

    @property
    def log_stream_name(self):
        r"""Gets the log_stream_name of this KeywordsResBody.

        日志流名称

        :return: The log_stream_name of this KeywordsResBody.
        :rtype: str
        """
        return self._log_stream_name

    @log_stream_name.setter
    def log_stream_name(self, log_stream_name):
        r"""Sets the log_stream_name of this KeywordsResBody.

        日志流名称

        :param log_stream_name: The log_stream_name of this KeywordsResBody.
        :type log_stream_name: str
        """
        self._log_stream_name = log_stream_name

    @property
    def log_group_id(self):
        r"""Gets the log_group_id of this KeywordsResBody.

        日志组id

        :return: The log_group_id of this KeywordsResBody.
        :rtype: str
        """
        return self._log_group_id

    @log_group_id.setter
    def log_group_id(self, log_group_id):
        r"""Sets the log_group_id of this KeywordsResBody.

        日志组id

        :param log_group_id: The log_group_id of this KeywordsResBody.
        :type log_group_id: str
        """
        self._log_group_id = log_group_id

    @property
    def log_group_name(self):
        r"""Gets the log_group_name of this KeywordsResBody.

        日志组名称

        :return: The log_group_name of this KeywordsResBody.
        :rtype: str
        """
        return self._log_group_name

    @log_group_name.setter
    def log_group_name(self, log_group_name):
        r"""Sets the log_group_name of this KeywordsResBody.

        日志组名称

        :param log_group_name: The log_group_name of this KeywordsResBody.
        :type log_group_name: str
        """
        self._log_group_name = log_group_name

    @property
    def keywords(self):
        r"""Gets the keywords of this KeywordsResBody.

        关键词

        :return: The keywords of this KeywordsResBody.
        :rtype: str
        """
        return self._keywords

    @keywords.setter
    def keywords(self, keywords):
        r"""Sets the keywords of this KeywordsResBody.

        关键词

        :param keywords: The keywords of this KeywordsResBody.
        :type keywords: str
        """
        self._keywords = keywords

    @property
    def condition(self):
        r"""Gets the condition of this KeywordsResBody.

        条件

        :return: The condition of this KeywordsResBody.
        :rtype: str
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        r"""Sets the condition of this KeywordsResBody.

        条件

        :param condition: The condition of this KeywordsResBody.
        :type condition: str
        """
        self._condition = condition

    @property
    def number(self):
        r"""Gets the number of this KeywordsResBody.

        行数

        :return: The number of this KeywordsResBody.
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number):
        r"""Sets the number of this KeywordsResBody.

        行数

        :param number: The number of this KeywordsResBody.
        :type number: int
        """
        self._number = number

    @property
    def search_time_range(self):
        r"""Gets the search_time_range of this KeywordsResBody.

        查询执行任务时最近数据的时间范围，最大值为60

        :return: The search_time_range of this KeywordsResBody.
        :rtype: int
        """
        return self._search_time_range

    @search_time_range.setter
    def search_time_range(self, search_time_range):
        r"""Sets the search_time_range of this KeywordsResBody.

        查询执行任务时最近数据的时间范围，最大值为60

        :param search_time_range: The search_time_range of this KeywordsResBody.
        :type search_time_range: int
        """
        self._search_time_range = search_time_range

    @property
    def search_time_range_unit(self):
        r"""Gets the search_time_range_unit of this KeywordsResBody.

        查询时间单位

        :return: The search_time_range_unit of this KeywordsResBody.
        :rtype: str
        """
        return self._search_time_range_unit

    @search_time_range_unit.setter
    def search_time_range_unit(self, search_time_range_unit):
        r"""Sets the search_time_range_unit of this KeywordsResBody.

        查询时间单位

        :param search_time_range_unit: The search_time_range_unit of this KeywordsResBody.
        :type search_time_range_unit: str
        """
        self._search_time_range_unit = search_time_range_unit

    @property
    def custom_date(self):
        r"""Gets the custom_date of this KeywordsResBody.

        :return: The custom_date of this KeywordsResBody.
        :rtype: :class:`huaweicloudsdklts.v2.CustomDate`
        """
        return self._custom_date

    @custom_date.setter
    def custom_date(self, custom_date):
        r"""Sets the custom_date of this KeywordsResBody.

        :param custom_date: The custom_date of this KeywordsResBody.
        :type custom_date: :class:`huaweicloudsdklts.v2.CustomDate`
        """
        self._custom_date = custom_date

    @property
    def is_time_range_relative(self):
        r"""Gets the is_time_range_relative of this KeywordsResBody.

        **参数解释：** 是否是相对时间。（暂不开放，后续aom上线该功能后一起开放） **约束限制：** 不涉及。 **取值范围：** - true - false **默认取值：** true

        :return: The is_time_range_relative of this KeywordsResBody.
        :rtype: bool
        """
        return self._is_time_range_relative

    @is_time_range_relative.setter
    def is_time_range_relative(self, is_time_range_relative):
        r"""Sets the is_time_range_relative of this KeywordsResBody.

        **参数解释：** 是否是相对时间。（暂不开放，后续aom上线该功能后一起开放） **约束限制：** 不涉及。 **取值范围：** - true - false **默认取值：** true

        :param is_time_range_relative: The is_time_range_relative of this KeywordsResBody.
        :type is_time_range_relative: bool
        """
        self._is_time_range_relative = is_time_range_relative

    @property
    def conditions(self):
        r"""Gets the conditions of this KeywordsResBody.

        **参数解释：** 支持根据不同条件触发不同级别的告警。当使用该参数时，将优先使用该参数中的条件触发告警，无视keywords_alarm_level参数以及keywords_requests中的condition、number参数。 **约束限制：** 不涉及。

        :return: The conditions of this KeywordsResBody.
        :rtype: list[:class:`huaweicloudsdklts.v2.KeywordsAlarmConditions`]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        r"""Sets the conditions of this KeywordsResBody.

        **参数解释：** 支持根据不同条件触发不同级别的告警。当使用该参数时，将优先使用该参数中的条件触发告警，无视keywords_alarm_level参数以及keywords_requests中的condition、number参数。 **约束限制：** 不涉及。

        :param conditions: The conditions of this KeywordsResBody.
        :type conditions: list[:class:`huaweicloudsdklts.v2.KeywordsAlarmConditions`]
        """
        self._conditions = conditions

    @property
    def log_group_name_alias(self):
        r"""Gets the log_group_name_alias of this KeywordsResBody.

        **参数解释：** 日志组别名。 **取值范围：** 不涉及。

        :return: The log_group_name_alias of this KeywordsResBody.
        :rtype: str
        """
        return self._log_group_name_alias

    @log_group_name_alias.setter
    def log_group_name_alias(self, log_group_name_alias):
        r"""Sets the log_group_name_alias of this KeywordsResBody.

        **参数解释：** 日志组别名。 **取值范围：** 不涉及。

        :param log_group_name_alias: The log_group_name_alias of this KeywordsResBody.
        :type log_group_name_alias: str
        """
        self._log_group_name_alias = log_group_name_alias

    @property
    def log_stream_name_alias(self):
        r"""Gets the log_stream_name_alias of this KeywordsResBody.

        **参数解释：** 日志流别名。 **取值范围：** 不涉及。

        :return: The log_stream_name_alias of this KeywordsResBody.
        :rtype: str
        """
        return self._log_stream_name_alias

    @log_stream_name_alias.setter
    def log_stream_name_alias(self, log_stream_name_alias):
        r"""Sets the log_stream_name_alias of this KeywordsResBody.

        **参数解释：** 日志流别名。 **取值范围：** 不涉及。

        :param log_stream_name_alias: The log_stream_name_alias of this KeywordsResBody.
        :type log_stream_name_alias: str
        """
        self._log_stream_name_alias = log_stream_name_alias

    @property
    def eps_id(self):
        r"""Gets the eps_id of this KeywordsResBody.

        **参数解释：** 企业项目ID。 **取值范围：** 不涉及。

        :return: The eps_id of this KeywordsResBody.
        :rtype: str
        """
        return self._eps_id

    @eps_id.setter
    def eps_id(self, eps_id):
        r"""Sets the eps_id of this KeywordsResBody.

        **参数解释：** 企业项目ID。 **取值范围：** 不涉及。

        :param eps_id: The eps_id of this KeywordsResBody.
        :type eps_id: str
        """
        self._eps_id = eps_id

    @property
    def time_range(self):
        r"""Gets the time_range of this KeywordsResBody.

        :return: The time_range of this KeywordsResBody.
        :rtype: :class:`huaweicloudsdklts.v2.TimeRange`
        """
        return self._time_range

    @time_range.setter
    def time_range(self, time_range):
        r"""Sets the time_range of this KeywordsResBody.

        :param time_range: The time_range of this KeywordsResBody.
        :type time_range: :class:`huaweicloudsdklts.v2.TimeRange`
        """
        self._time_range = time_range

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
        if not isinstance(other, KeywordsResBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
