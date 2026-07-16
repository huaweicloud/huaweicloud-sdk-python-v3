# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTrainingJobEventsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'training_job_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'order': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'x_language': 'str',
        'level': 'str',
        'pattern': 'str'
    }

    attribute_map = {
        'training_job_id': 'training_job_id',
        'offset': 'offset',
        'limit': 'limit',
        'order': 'order',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'x_language': 'X-Language',
        'level': 'level',
        'pattern': 'pattern'
    }

    def __init__(self, training_job_id=None, offset=None, limit=None, order=None, start_time=None, end_time=None, x_language=None, level=None, pattern=None):
        r"""ListTrainingJobEventsRequest

        The model defined in huaweicloud sdk

        :param training_job_id: 训练作业ID。获取方法请参见[查询训练作业列表](ListTrainingJobs.xml)。
        :type training_job_id: str
        :param offset: 数据条目偏移量。
        :type offset: int
        :param limit: 指定每一页返回的最大条目数，取值范围[1,100]，默认为50。
        :type limit: int
        :param order: instance order
        :type order: str
        :param start_time: 开始时间，需要与结束时间一起传入。
        :type start_time: str
        :param end_time: 结束时间，需要与开始时间一起传入。
        :type end_time: str
        :param x_language: 语言。
        :type x_language: str
        :param level: 指定返回的事件级别，取值范围[Info Error Warning]。
        :type level: str
        :param pattern: 指定事件信息包含的内容，最长256个字符。
        :type pattern: str
        """
        
        

        self._training_job_id = None
        self._offset = None
        self._limit = None
        self._order = None
        self._start_time = None
        self._end_time = None
        self._x_language = None
        self._level = None
        self._pattern = None
        self.discriminator = None

        self.training_job_id = training_job_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if order is not None:
            self.order = order
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if x_language is not None:
            self.x_language = x_language
        if level is not None:
            self.level = level
        if pattern is not None:
            self.pattern = pattern

    @property
    def training_job_id(self):
        r"""Gets the training_job_id of this ListTrainingJobEventsRequest.

        训练作业ID。获取方法请参见[查询训练作业列表](ListTrainingJobs.xml)。

        :return: The training_job_id of this ListTrainingJobEventsRequest.
        :rtype: str
        """
        return self._training_job_id

    @training_job_id.setter
    def training_job_id(self, training_job_id):
        r"""Sets the training_job_id of this ListTrainingJobEventsRequest.

        训练作业ID。获取方法请参见[查询训练作业列表](ListTrainingJobs.xml)。

        :param training_job_id: The training_job_id of this ListTrainingJobEventsRequest.
        :type training_job_id: str
        """
        self._training_job_id = training_job_id

    @property
    def offset(self):
        r"""Gets the offset of this ListTrainingJobEventsRequest.

        数据条目偏移量。

        :return: The offset of this ListTrainingJobEventsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListTrainingJobEventsRequest.

        数据条目偏移量。

        :param offset: The offset of this ListTrainingJobEventsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListTrainingJobEventsRequest.

        指定每一页返回的最大条目数，取值范围[1,100]，默认为50。

        :return: The limit of this ListTrainingJobEventsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListTrainingJobEventsRequest.

        指定每一页返回的最大条目数，取值范围[1,100]，默认为50。

        :param limit: The limit of this ListTrainingJobEventsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def order(self):
        r"""Gets the order of this ListTrainingJobEventsRequest.

        instance order

        :return: The order of this ListTrainingJobEventsRequest.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        r"""Sets the order of this ListTrainingJobEventsRequest.

        instance order

        :param order: The order of this ListTrainingJobEventsRequest.
        :type order: str
        """
        self._order = order

    @property
    def start_time(self):
        r"""Gets the start_time of this ListTrainingJobEventsRequest.

        开始时间，需要与结束时间一起传入。

        :return: The start_time of this ListTrainingJobEventsRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListTrainingJobEventsRequest.

        开始时间，需要与结束时间一起传入。

        :param start_time: The start_time of this ListTrainingJobEventsRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListTrainingJobEventsRequest.

        结束时间，需要与开始时间一起传入。

        :return: The end_time of this ListTrainingJobEventsRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListTrainingJobEventsRequest.

        结束时间，需要与开始时间一起传入。

        :param end_time: The end_time of this ListTrainingJobEventsRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def x_language(self):
        r"""Gets the x_language of this ListTrainingJobEventsRequest.

        语言。

        :return: The x_language of this ListTrainingJobEventsRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ListTrainingJobEventsRequest.

        语言。

        :param x_language: The x_language of this ListTrainingJobEventsRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def level(self):
        r"""Gets the level of this ListTrainingJobEventsRequest.

        指定返回的事件级别，取值范围[Info Error Warning]。

        :return: The level of this ListTrainingJobEventsRequest.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        r"""Sets the level of this ListTrainingJobEventsRequest.

        指定返回的事件级别，取值范围[Info Error Warning]。

        :param level: The level of this ListTrainingJobEventsRequest.
        :type level: str
        """
        self._level = level

    @property
    def pattern(self):
        r"""Gets the pattern of this ListTrainingJobEventsRequest.

        指定事件信息包含的内容，最长256个字符。

        :return: The pattern of this ListTrainingJobEventsRequest.
        :rtype: str
        """
        return self._pattern

    @pattern.setter
    def pattern(self, pattern):
        r"""Sets the pattern of this ListTrainingJobEventsRequest.

        指定事件信息包含的内容，最长256个字符。

        :param pattern: The pattern of this ListTrainingJobEventsRequest.
        :type pattern: str
        """
        self._pattern = pattern

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
        if not isinstance(other, ListTrainingJobEventsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
