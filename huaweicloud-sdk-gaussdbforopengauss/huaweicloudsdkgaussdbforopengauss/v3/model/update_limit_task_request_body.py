# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateLimitTaskRequestBody:

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
        'key_words': 'str',
        'parallel_size': 'int',
        'task_name': 'str',
        'cpu_utilization': 'int',
        'memory_utilization': 'int',
        'databases': 'str'
    }

    attribute_map = {
        'start_time': 'start_time',
        'end_time': 'end_time',
        'key_words': 'key_words',
        'parallel_size': 'parallel_size',
        'task_name': 'task_name',
        'cpu_utilization': 'cpu_utilization',
        'memory_utilization': 'memory_utilization',
        'databases': 'databases'
    }

    def __init__(self, start_time=None, end_time=None, key_words=None, parallel_size=None, task_name=None, cpu_utilization=None, memory_utilization=None, databases=None):
        r"""UpdateLimitTaskRequestBody

        The model defined in huaweicloud sdk

        :param start_time: 任务开始时间，格式为yyyy-mm-ddThh:mm:ssZ，如果存在更改，需大于当前时间前俩分钟，当前时间指UTC时，SQL范围必传。
        :type start_time: str
        :param end_time: 任务结束时间,格式为yyyy-mm-ddThh:mm:ssZ，大于任务开始时间，当前时间指UTC时间，SQL范围必传。
        :type end_time: str
        :param key_words: 关键词，当且仅当类型为SQL_TYPE，必传，多个关键词以逗号隔开，数量范围为[2，100]个，每个关键词长度范围[2，64]位，关键词不允许包含 \&quot; 或 \\ 或 {} 或 null值 以及非首尾的空格符。
        :type key_words: str
        :param parallel_size: 并发数，大于等于零的正整数，取值范围[0, 2147483647]。
        :type parallel_size: int
        :param task_name: 限流任务名，只能为英文字母大小写，下划线，数字和$符，最大长度为100个字符。
        :type task_name: str
        :param cpu_utilization: cpu利用率阈值，正整数，取值范围[0,100）,如果类型为SESSION_ACTIVE_MAX_COUNT，必传，不支持和内存利用率阈值同时为0，如果选择只限制CPU、内存中的其中一个，则另一个必须传值0。
        :type cpu_utilization: int
        :param memory_utilization: 内存利用率阈值，正整数，取值范围[0,100）,如果类型为SESSION_ACTIVE_MAX_COUNT，必传，不支持和cpu利用率阈值同时为0，如果选择只限制CPU、内存中的其中一个，则另一个必须传值0。
        :type memory_utilization: int
        :param databases: CN节点数据库组，每个数据库字符串以逗号形式隔开。
        :type databases: str
        """
        
        

        self._start_time = None
        self._end_time = None
        self._key_words = None
        self._parallel_size = None
        self._task_name = None
        self._cpu_utilization = None
        self._memory_utilization = None
        self._databases = None
        self.discriminator = None

        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if key_words is not None:
            self.key_words = key_words
        if parallel_size is not None:
            self.parallel_size = parallel_size
        if task_name is not None:
            self.task_name = task_name
        if cpu_utilization is not None:
            self.cpu_utilization = cpu_utilization
        if memory_utilization is not None:
            self.memory_utilization = memory_utilization
        if databases is not None:
            self.databases = databases

    @property
    def start_time(self):
        r"""Gets the start_time of this UpdateLimitTaskRequestBody.

        任务开始时间，格式为yyyy-mm-ddThh:mm:ssZ，如果存在更改，需大于当前时间前俩分钟，当前时间指UTC时，SQL范围必传。

        :return: The start_time of this UpdateLimitTaskRequestBody.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this UpdateLimitTaskRequestBody.

        任务开始时间，格式为yyyy-mm-ddThh:mm:ssZ，如果存在更改，需大于当前时间前俩分钟，当前时间指UTC时，SQL范围必传。

        :param start_time: The start_time of this UpdateLimitTaskRequestBody.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this UpdateLimitTaskRequestBody.

        任务结束时间,格式为yyyy-mm-ddThh:mm:ssZ，大于任务开始时间，当前时间指UTC时间，SQL范围必传。

        :return: The end_time of this UpdateLimitTaskRequestBody.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this UpdateLimitTaskRequestBody.

        任务结束时间,格式为yyyy-mm-ddThh:mm:ssZ，大于任务开始时间，当前时间指UTC时间，SQL范围必传。

        :param end_time: The end_time of this UpdateLimitTaskRequestBody.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def key_words(self):
        r"""Gets the key_words of this UpdateLimitTaskRequestBody.

        关键词，当且仅当类型为SQL_TYPE，必传，多个关键词以逗号隔开，数量范围为[2，100]个，每个关键词长度范围[2，64]位，关键词不允许包含 \" 或 \\ 或 {} 或 null值 以及非首尾的空格符。

        :return: The key_words of this UpdateLimitTaskRequestBody.
        :rtype: str
        """
        return self._key_words

    @key_words.setter
    def key_words(self, key_words):
        r"""Sets the key_words of this UpdateLimitTaskRequestBody.

        关键词，当且仅当类型为SQL_TYPE，必传，多个关键词以逗号隔开，数量范围为[2，100]个，每个关键词长度范围[2，64]位，关键词不允许包含 \" 或 \\ 或 {} 或 null值 以及非首尾的空格符。

        :param key_words: The key_words of this UpdateLimitTaskRequestBody.
        :type key_words: str
        """
        self._key_words = key_words

    @property
    def parallel_size(self):
        r"""Gets the parallel_size of this UpdateLimitTaskRequestBody.

        并发数，大于等于零的正整数，取值范围[0, 2147483647]。

        :return: The parallel_size of this UpdateLimitTaskRequestBody.
        :rtype: int
        """
        return self._parallel_size

    @parallel_size.setter
    def parallel_size(self, parallel_size):
        r"""Sets the parallel_size of this UpdateLimitTaskRequestBody.

        并发数，大于等于零的正整数，取值范围[0, 2147483647]。

        :param parallel_size: The parallel_size of this UpdateLimitTaskRequestBody.
        :type parallel_size: int
        """
        self._parallel_size = parallel_size

    @property
    def task_name(self):
        r"""Gets the task_name of this UpdateLimitTaskRequestBody.

        限流任务名，只能为英文字母大小写，下划线，数字和$符，最大长度为100个字符。

        :return: The task_name of this UpdateLimitTaskRequestBody.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        r"""Sets the task_name of this UpdateLimitTaskRequestBody.

        限流任务名，只能为英文字母大小写，下划线，数字和$符，最大长度为100个字符。

        :param task_name: The task_name of this UpdateLimitTaskRequestBody.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def cpu_utilization(self):
        r"""Gets the cpu_utilization of this UpdateLimitTaskRequestBody.

        cpu利用率阈值，正整数，取值范围[0,100）,如果类型为SESSION_ACTIVE_MAX_COUNT，必传，不支持和内存利用率阈值同时为0，如果选择只限制CPU、内存中的其中一个，则另一个必须传值0。

        :return: The cpu_utilization of this UpdateLimitTaskRequestBody.
        :rtype: int
        """
        return self._cpu_utilization

    @cpu_utilization.setter
    def cpu_utilization(self, cpu_utilization):
        r"""Sets the cpu_utilization of this UpdateLimitTaskRequestBody.

        cpu利用率阈值，正整数，取值范围[0,100）,如果类型为SESSION_ACTIVE_MAX_COUNT，必传，不支持和内存利用率阈值同时为0，如果选择只限制CPU、内存中的其中一个，则另一个必须传值0。

        :param cpu_utilization: The cpu_utilization of this UpdateLimitTaskRequestBody.
        :type cpu_utilization: int
        """
        self._cpu_utilization = cpu_utilization

    @property
    def memory_utilization(self):
        r"""Gets the memory_utilization of this UpdateLimitTaskRequestBody.

        内存利用率阈值，正整数，取值范围[0,100）,如果类型为SESSION_ACTIVE_MAX_COUNT，必传，不支持和cpu利用率阈值同时为0，如果选择只限制CPU、内存中的其中一个，则另一个必须传值0。

        :return: The memory_utilization of this UpdateLimitTaskRequestBody.
        :rtype: int
        """
        return self._memory_utilization

    @memory_utilization.setter
    def memory_utilization(self, memory_utilization):
        r"""Sets the memory_utilization of this UpdateLimitTaskRequestBody.

        内存利用率阈值，正整数，取值范围[0,100）,如果类型为SESSION_ACTIVE_MAX_COUNT，必传，不支持和cpu利用率阈值同时为0，如果选择只限制CPU、内存中的其中一个，则另一个必须传值0。

        :param memory_utilization: The memory_utilization of this UpdateLimitTaskRequestBody.
        :type memory_utilization: int
        """
        self._memory_utilization = memory_utilization

    @property
    def databases(self):
        r"""Gets the databases of this UpdateLimitTaskRequestBody.

        CN节点数据库组，每个数据库字符串以逗号形式隔开。

        :return: The databases of this UpdateLimitTaskRequestBody.
        :rtype: str
        """
        return self._databases

    @databases.setter
    def databases(self, databases):
        r"""Sets the databases of this UpdateLimitTaskRequestBody.

        CN节点数据库组，每个数据库字符串以逗号形式隔开。

        :param databases: The databases of this UpdateLimitTaskRequestBody.
        :type databases: str
        """
        self._databases = databases

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
        if not isinstance(other, UpdateLimitTaskRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
