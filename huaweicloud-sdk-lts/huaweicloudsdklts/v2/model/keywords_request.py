# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class KeywordsRequest:

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
        'is_time_range_relative': 'bool'
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
        'is_time_range_relative': 'is_time_range_relative'
    }

    def __init__(self, log_stream_id=None, log_stream_name=None, log_group_id=None, log_group_name=None, keywords=None, condition=None, number=None, search_time_range=None, search_time_range_unit=None, custom_date=None, is_time_range_relative=None):
        r"""KeywordsRequest

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
        self.discriminator = None

        self.log_stream_id = log_stream_id
        if log_stream_name is not None:
            self.log_stream_name = log_stream_name
        self.log_group_id = log_group_id
        if log_group_name is not None:
            self.log_group_name = log_group_name
        self.keywords = keywords
        self.condition = condition
        self.number = number
        self.search_time_range = search_time_range
        self.search_time_range_unit = search_time_range_unit
        if custom_date is not None:
            self.custom_date = custom_date
        if is_time_range_relative is not None:
            self.is_time_range_relative = is_time_range_relative

    @property
    def log_stream_id(self):
        r"""Gets the log_stream_id of this KeywordsRequest.

        日志流id

        :return: The log_stream_id of this KeywordsRequest.
        :rtype: str
        """
        return self._log_stream_id

    @log_stream_id.setter
    def log_stream_id(self, log_stream_id):
        r"""Sets the log_stream_id of this KeywordsRequest.

        日志流id

        :param log_stream_id: The log_stream_id of this KeywordsRequest.
        :type log_stream_id: str
        """
        self._log_stream_id = log_stream_id

    @property
    def log_stream_name(self):
        r"""Gets the log_stream_name of this KeywordsRequest.

        日志流名称

        :return: The log_stream_name of this KeywordsRequest.
        :rtype: str
        """
        return self._log_stream_name

    @log_stream_name.setter
    def log_stream_name(self, log_stream_name):
        r"""Sets the log_stream_name of this KeywordsRequest.

        日志流名称

        :param log_stream_name: The log_stream_name of this KeywordsRequest.
        :type log_stream_name: str
        """
        self._log_stream_name = log_stream_name

    @property
    def log_group_id(self):
        r"""Gets the log_group_id of this KeywordsRequest.

        日志组id

        :return: The log_group_id of this KeywordsRequest.
        :rtype: str
        """
        return self._log_group_id

    @log_group_id.setter
    def log_group_id(self, log_group_id):
        r"""Sets the log_group_id of this KeywordsRequest.

        日志组id

        :param log_group_id: The log_group_id of this KeywordsRequest.
        :type log_group_id: str
        """
        self._log_group_id = log_group_id

    @property
    def log_group_name(self):
        r"""Gets the log_group_name of this KeywordsRequest.

        日志组名称

        :return: The log_group_name of this KeywordsRequest.
        :rtype: str
        """
        return self._log_group_name

    @log_group_name.setter
    def log_group_name(self, log_group_name):
        r"""Sets the log_group_name of this KeywordsRequest.

        日志组名称

        :param log_group_name: The log_group_name of this KeywordsRequest.
        :type log_group_name: str
        """
        self._log_group_name = log_group_name

    @property
    def keywords(self):
        r"""Gets the keywords of this KeywordsRequest.

        关键词

        :return: The keywords of this KeywordsRequest.
        :rtype: str
        """
        return self._keywords

    @keywords.setter
    def keywords(self, keywords):
        r"""Sets the keywords of this KeywordsRequest.

        关键词

        :param keywords: The keywords of this KeywordsRequest.
        :type keywords: str
        """
        self._keywords = keywords

    @property
    def condition(self):
        r"""Gets the condition of this KeywordsRequest.

        条件

        :return: The condition of this KeywordsRequest.
        :rtype: str
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        r"""Sets the condition of this KeywordsRequest.

        条件

        :param condition: The condition of this KeywordsRequest.
        :type condition: str
        """
        self._condition = condition

    @property
    def number(self):
        r"""Gets the number of this KeywordsRequest.

        行数

        :return: The number of this KeywordsRequest.
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number):
        r"""Sets the number of this KeywordsRequest.

        行数

        :param number: The number of this KeywordsRequest.
        :type number: int
        """
        self._number = number

    @property
    def search_time_range(self):
        r"""Gets the search_time_range of this KeywordsRequest.

        查询执行任务时最近数据的时间范围，最大值为60

        :return: The search_time_range of this KeywordsRequest.
        :rtype: int
        """
        return self._search_time_range

    @search_time_range.setter
    def search_time_range(self, search_time_range):
        r"""Sets the search_time_range of this KeywordsRequest.

        查询执行任务时最近数据的时间范围，最大值为60

        :param search_time_range: The search_time_range of this KeywordsRequest.
        :type search_time_range: int
        """
        self._search_time_range = search_time_range

    @property
    def search_time_range_unit(self):
        r"""Gets the search_time_range_unit of this KeywordsRequest.

        查询时间单位

        :return: The search_time_range_unit of this KeywordsRequest.
        :rtype: str
        """
        return self._search_time_range_unit

    @search_time_range_unit.setter
    def search_time_range_unit(self, search_time_range_unit):
        r"""Sets the search_time_range_unit of this KeywordsRequest.

        查询时间单位

        :param search_time_range_unit: The search_time_range_unit of this KeywordsRequest.
        :type search_time_range_unit: str
        """
        self._search_time_range_unit = search_time_range_unit

    @property
    def custom_date(self):
        r"""Gets the custom_date of this KeywordsRequest.

        :return: The custom_date of this KeywordsRequest.
        :rtype: :class:`huaweicloudsdklts.v2.CustomDate`
        """
        return self._custom_date

    @custom_date.setter
    def custom_date(self, custom_date):
        r"""Sets the custom_date of this KeywordsRequest.

        :param custom_date: The custom_date of this KeywordsRequest.
        :type custom_date: :class:`huaweicloudsdklts.v2.CustomDate`
        """
        self._custom_date = custom_date

    @property
    def is_time_range_relative(self):
        r"""Gets the is_time_range_relative of this KeywordsRequest.

        **参数解释：** 是否是相对时间。（暂不开放，后续aom上线该功能后一起开放） **约束限制：** 不涉及。 **取值范围：** - true - false **默认取值：** true

        :return: The is_time_range_relative of this KeywordsRequest.
        :rtype: bool
        """
        return self._is_time_range_relative

    @is_time_range_relative.setter
    def is_time_range_relative(self, is_time_range_relative):
        r"""Sets the is_time_range_relative of this KeywordsRequest.

        **参数解释：** 是否是相对时间。（暂不开放，后续aom上线该功能后一起开放） **约束限制：** 不涉及。 **取值范围：** - true - false **默认取值：** true

        :param is_time_range_relative: The is_time_range_relative of this KeywordsRequest.
        :type is_time_range_relative: bool
        """
        self._is_time_range_relative = is_time_range_relative

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
        if not isinstance(other, KeywordsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
