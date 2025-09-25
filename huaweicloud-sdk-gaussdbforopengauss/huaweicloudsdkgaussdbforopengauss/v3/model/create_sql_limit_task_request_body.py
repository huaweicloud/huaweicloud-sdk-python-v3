# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSqlLimitTaskRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_scope': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'limit_type': 'str',
        'limit_type_value': 'str',
        'key_words': 'str',
        'task_name': 'str',
        'parallel_size': 'int',
        'cpu_utilization': 'int',
        'memory_utilization': 'int',
        'databases': 'str',
        'node_infos': 'list[CreateLimitTaskNodeOption]'
    }

    attribute_map = {
        'task_scope': 'task_scope',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'limit_type': 'limit_type',
        'limit_type_value': 'limit_type_value',
        'key_words': 'key_words',
        'task_name': 'task_name',
        'parallel_size': 'parallel_size',
        'cpu_utilization': 'cpu_utilization',
        'memory_utilization': 'memory_utilization',
        'databases': 'databases',
        'node_infos': 'node_infos'
    }

    def __init__(self, task_scope=None, start_time=None, end_time=None, limit_type=None, limit_type_value=None, key_words=None, task_name=None, parallel_size=None, cpu_utilization=None, memory_utilization=None, databases=None, node_infos=None):
        r"""CreateSqlLimitTaskRequestBody

        The model defined in huaweicloud sdk

        :param task_scope: **参数解释**: 限流任务范围，目前支持SQL、SESSION级别范围。 **约束限制**: 不涉及。 **取值范围**: - SQL - SESSION  **默认取值**: 不涉及。
        :type task_scope: str
        :param start_time: **参数解释**: 任务开始时间，如果该值小于当前时间，会取当前时间的前两分钟。 **约束限制**: 当“task_scope”为SQL时必传。 **取值范围**: 格式必须为yyyy-mm-ddThh:mm:ssZ，当前时间指UTC时间。 **默认取值**: 不涉及。
        :type start_time: str
        :param end_time: **参数解释**: 任务结束时间。 **约束限制**: 当“task_scope”为SQL时必传。 **取值范围**: 大于任务开始时间，格式必须为yyyy-mm-ddThh:mm:ssZ，当前时间指UTC时间。 **默认取值**: 不涉及。
        :type end_time: str
        :param limit_type: **参数解释**: 限流类型。 **约束限制**: 不涉及。 **取值范围**: - 当“task_scope”为SQL时，可选SQL_ID、SQL_TYPE类型。 - 当“task_scope”为SESSION时，可选SESSION_ACTIVE_MAX_COUNT类型。  **默认取值**: 不涉及。
        :type limit_type: str
        :param limit_type_value: **参数解释**: 限流类型值。 **约束限制**: 不涉及。 **取值范围**: - 当“limit_type”为SQL_ID类型时，该值为选中模板的sql_id。 - 当“limit_type”为SQL_TYPE类型时，值为SQL类型，目前支持select，update，insert，delete，merge。 - 当“limit_type”为SESSION_ACTIVE_MAX_COUNT类型时，只支持CPU_OR_MEMORY一种值。  **默认取值**: 不涉及。
        :type limit_type_value: str
        :param key_words: **参数解释**: 关键词。 **约束限制**: 当且仅当“limit_type”为SQL_TYPE时，必传。 **取值范围**: 多个关键词以逗号隔开，数量范围为[2，100]个，每个关键词长度范围[2，64]位，关键词不允许包含 \&quot; 或 \\ 或 {} 或 null值以及非首尾的空格符。 **默认取值**: 不涉及。
        :type key_words: str
        :param task_name: **参数解释**: 限流任务名。 **约束限制**: 不涉及。 **取值范围**: 只能为英文字母大小写，下划线，数字和$符，最大长度为100个字符。 **默认取值**: 不涉及。
        :type task_name: str
        :param parallel_size: **参数解释**: 并发数。 **约束限制**: 不涉及。 **取值范围**: 大于等于零的整数，取值范围[0, 2147483647]。 **默认取值**: 不涉及。
        :type parallel_size: int
        :param cpu_utilization: **参数解释**: CPU利用率阈值。 **约束限制**: 如果“limit_type”为SESSION_ACTIVE_MAX_COUNT，必传。不支持和内存利用率阈值同时为0，如果选择只限制CPU、内存中的其中一个，则另一个必须传值0。 **取值范围**: 整数，取值范围[0,100）。 **默认取值**: 不涉及。
        :type cpu_utilization: int
        :param memory_utilization: **参数解释**: 内存利用率阈值。 **约束限制**: 如果“limit_type”为SESSION_ACTIVE_MAX_COUNT，必传。不支持和CPU利用率阈值同时为0，如果选择只限制CPU、内存中的其中一个，则另一个必须传值0。 **取值范围**: 整数，取值范围[0,100）。 **默认取值**: 不涉及。
        :type memory_utilization: int
        :param databases: **参数解释**: 数据库名称，限流只对指定的数据库生效，多个数据库名称用英文逗号分割。 **约束限制**: 当“limit_type”为SQL_TYPE类型时，databases参数必选。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type databases: str
        :param node_infos: **参数解释**: CN节点信息列表 **约束限制**: 如果“limit_type”为SQL_ID，则“node_infos”必选。
        :type node_infos: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.CreateLimitTaskNodeOption`]
        """
        
        

        self._task_scope = None
        self._start_time = None
        self._end_time = None
        self._limit_type = None
        self._limit_type_value = None
        self._key_words = None
        self._task_name = None
        self._parallel_size = None
        self._cpu_utilization = None
        self._memory_utilization = None
        self._databases = None
        self._node_infos = None
        self.discriminator = None

        self.task_scope = task_scope
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        self.limit_type = limit_type
        if limit_type_value is not None:
            self.limit_type_value = limit_type_value
        if key_words is not None:
            self.key_words = key_words
        self.task_name = task_name
        self.parallel_size = parallel_size
        if cpu_utilization is not None:
            self.cpu_utilization = cpu_utilization
        if memory_utilization is not None:
            self.memory_utilization = memory_utilization
        if databases is not None:
            self.databases = databases
        if node_infos is not None:
            self.node_infos = node_infos

    @property
    def task_scope(self):
        r"""Gets the task_scope of this CreateSqlLimitTaskRequestBody.

        **参数解释**: 限流任务范围，目前支持SQL、SESSION级别范围。 **约束限制**: 不涉及。 **取值范围**: - SQL - SESSION  **默认取值**: 不涉及。

        :return: The task_scope of this CreateSqlLimitTaskRequestBody.
        :rtype: str
        """
        return self._task_scope

    @task_scope.setter
    def task_scope(self, task_scope):
        r"""Sets the task_scope of this CreateSqlLimitTaskRequestBody.

        **参数解释**: 限流任务范围，目前支持SQL、SESSION级别范围。 **约束限制**: 不涉及。 **取值范围**: - SQL - SESSION  **默认取值**: 不涉及。

        :param task_scope: The task_scope of this CreateSqlLimitTaskRequestBody.
        :type task_scope: str
        """
        self._task_scope = task_scope

    @property
    def start_time(self):
        r"""Gets the start_time of this CreateSqlLimitTaskRequestBody.

        **参数解释**: 任务开始时间，如果该值小于当前时间，会取当前时间的前两分钟。 **约束限制**: 当“task_scope”为SQL时必传。 **取值范围**: 格式必须为yyyy-mm-ddThh:mm:ssZ，当前时间指UTC时间。 **默认取值**: 不涉及。

        :return: The start_time of this CreateSqlLimitTaskRequestBody.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this CreateSqlLimitTaskRequestBody.

        **参数解释**: 任务开始时间，如果该值小于当前时间，会取当前时间的前两分钟。 **约束限制**: 当“task_scope”为SQL时必传。 **取值范围**: 格式必须为yyyy-mm-ddThh:mm:ssZ，当前时间指UTC时间。 **默认取值**: 不涉及。

        :param start_time: The start_time of this CreateSqlLimitTaskRequestBody.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this CreateSqlLimitTaskRequestBody.

        **参数解释**: 任务结束时间。 **约束限制**: 当“task_scope”为SQL时必传。 **取值范围**: 大于任务开始时间，格式必须为yyyy-mm-ddThh:mm:ssZ，当前时间指UTC时间。 **默认取值**: 不涉及。

        :return: The end_time of this CreateSqlLimitTaskRequestBody.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this CreateSqlLimitTaskRequestBody.

        **参数解释**: 任务结束时间。 **约束限制**: 当“task_scope”为SQL时必传。 **取值范围**: 大于任务开始时间，格式必须为yyyy-mm-ddThh:mm:ssZ，当前时间指UTC时间。 **默认取值**: 不涉及。

        :param end_time: The end_time of this CreateSqlLimitTaskRequestBody.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def limit_type(self):
        r"""Gets the limit_type of this CreateSqlLimitTaskRequestBody.

        **参数解释**: 限流类型。 **约束限制**: 不涉及。 **取值范围**: - 当“task_scope”为SQL时，可选SQL_ID、SQL_TYPE类型。 - 当“task_scope”为SESSION时，可选SESSION_ACTIVE_MAX_COUNT类型。  **默认取值**: 不涉及。

        :return: The limit_type of this CreateSqlLimitTaskRequestBody.
        :rtype: str
        """
        return self._limit_type

    @limit_type.setter
    def limit_type(self, limit_type):
        r"""Sets the limit_type of this CreateSqlLimitTaskRequestBody.

        **参数解释**: 限流类型。 **约束限制**: 不涉及。 **取值范围**: - 当“task_scope”为SQL时，可选SQL_ID、SQL_TYPE类型。 - 当“task_scope”为SESSION时，可选SESSION_ACTIVE_MAX_COUNT类型。  **默认取值**: 不涉及。

        :param limit_type: The limit_type of this CreateSqlLimitTaskRequestBody.
        :type limit_type: str
        """
        self._limit_type = limit_type

    @property
    def limit_type_value(self):
        r"""Gets the limit_type_value of this CreateSqlLimitTaskRequestBody.

        **参数解释**: 限流类型值。 **约束限制**: 不涉及。 **取值范围**: - 当“limit_type”为SQL_ID类型时，该值为选中模板的sql_id。 - 当“limit_type”为SQL_TYPE类型时，值为SQL类型，目前支持select，update，insert，delete，merge。 - 当“limit_type”为SESSION_ACTIVE_MAX_COUNT类型时，只支持CPU_OR_MEMORY一种值。  **默认取值**: 不涉及。

        :return: The limit_type_value of this CreateSqlLimitTaskRequestBody.
        :rtype: str
        """
        return self._limit_type_value

    @limit_type_value.setter
    def limit_type_value(self, limit_type_value):
        r"""Sets the limit_type_value of this CreateSqlLimitTaskRequestBody.

        **参数解释**: 限流类型值。 **约束限制**: 不涉及。 **取值范围**: - 当“limit_type”为SQL_ID类型时，该值为选中模板的sql_id。 - 当“limit_type”为SQL_TYPE类型时，值为SQL类型，目前支持select，update，insert，delete，merge。 - 当“limit_type”为SESSION_ACTIVE_MAX_COUNT类型时，只支持CPU_OR_MEMORY一种值。  **默认取值**: 不涉及。

        :param limit_type_value: The limit_type_value of this CreateSqlLimitTaskRequestBody.
        :type limit_type_value: str
        """
        self._limit_type_value = limit_type_value

    @property
    def key_words(self):
        r"""Gets the key_words of this CreateSqlLimitTaskRequestBody.

        **参数解释**: 关键词。 **约束限制**: 当且仅当“limit_type”为SQL_TYPE时，必传。 **取值范围**: 多个关键词以逗号隔开，数量范围为[2，100]个，每个关键词长度范围[2，64]位，关键词不允许包含 \" 或 \\ 或 {} 或 null值以及非首尾的空格符。 **默认取值**: 不涉及。

        :return: The key_words of this CreateSqlLimitTaskRequestBody.
        :rtype: str
        """
        return self._key_words

    @key_words.setter
    def key_words(self, key_words):
        r"""Sets the key_words of this CreateSqlLimitTaskRequestBody.

        **参数解释**: 关键词。 **约束限制**: 当且仅当“limit_type”为SQL_TYPE时，必传。 **取值范围**: 多个关键词以逗号隔开，数量范围为[2，100]个，每个关键词长度范围[2，64]位，关键词不允许包含 \" 或 \\ 或 {} 或 null值以及非首尾的空格符。 **默认取值**: 不涉及。

        :param key_words: The key_words of this CreateSqlLimitTaskRequestBody.
        :type key_words: str
        """
        self._key_words = key_words

    @property
    def task_name(self):
        r"""Gets the task_name of this CreateSqlLimitTaskRequestBody.

        **参数解释**: 限流任务名。 **约束限制**: 不涉及。 **取值范围**: 只能为英文字母大小写，下划线，数字和$符，最大长度为100个字符。 **默认取值**: 不涉及。

        :return: The task_name of this CreateSqlLimitTaskRequestBody.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        r"""Sets the task_name of this CreateSqlLimitTaskRequestBody.

        **参数解释**: 限流任务名。 **约束限制**: 不涉及。 **取值范围**: 只能为英文字母大小写，下划线，数字和$符，最大长度为100个字符。 **默认取值**: 不涉及。

        :param task_name: The task_name of this CreateSqlLimitTaskRequestBody.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def parallel_size(self):
        r"""Gets the parallel_size of this CreateSqlLimitTaskRequestBody.

        **参数解释**: 并发数。 **约束限制**: 不涉及。 **取值范围**: 大于等于零的整数，取值范围[0, 2147483647]。 **默认取值**: 不涉及。

        :return: The parallel_size of this CreateSqlLimitTaskRequestBody.
        :rtype: int
        """
        return self._parallel_size

    @parallel_size.setter
    def parallel_size(self, parallel_size):
        r"""Sets the parallel_size of this CreateSqlLimitTaskRequestBody.

        **参数解释**: 并发数。 **约束限制**: 不涉及。 **取值范围**: 大于等于零的整数，取值范围[0, 2147483647]。 **默认取值**: 不涉及。

        :param parallel_size: The parallel_size of this CreateSqlLimitTaskRequestBody.
        :type parallel_size: int
        """
        self._parallel_size = parallel_size

    @property
    def cpu_utilization(self):
        r"""Gets the cpu_utilization of this CreateSqlLimitTaskRequestBody.

        **参数解释**: CPU利用率阈值。 **约束限制**: 如果“limit_type”为SESSION_ACTIVE_MAX_COUNT，必传。不支持和内存利用率阈值同时为0，如果选择只限制CPU、内存中的其中一个，则另一个必须传值0。 **取值范围**: 整数，取值范围[0,100）。 **默认取值**: 不涉及。

        :return: The cpu_utilization of this CreateSqlLimitTaskRequestBody.
        :rtype: int
        """
        return self._cpu_utilization

    @cpu_utilization.setter
    def cpu_utilization(self, cpu_utilization):
        r"""Sets the cpu_utilization of this CreateSqlLimitTaskRequestBody.

        **参数解释**: CPU利用率阈值。 **约束限制**: 如果“limit_type”为SESSION_ACTIVE_MAX_COUNT，必传。不支持和内存利用率阈值同时为0，如果选择只限制CPU、内存中的其中一个，则另一个必须传值0。 **取值范围**: 整数，取值范围[0,100）。 **默认取值**: 不涉及。

        :param cpu_utilization: The cpu_utilization of this CreateSqlLimitTaskRequestBody.
        :type cpu_utilization: int
        """
        self._cpu_utilization = cpu_utilization

    @property
    def memory_utilization(self):
        r"""Gets the memory_utilization of this CreateSqlLimitTaskRequestBody.

        **参数解释**: 内存利用率阈值。 **约束限制**: 如果“limit_type”为SESSION_ACTIVE_MAX_COUNT，必传。不支持和CPU利用率阈值同时为0，如果选择只限制CPU、内存中的其中一个，则另一个必须传值0。 **取值范围**: 整数，取值范围[0,100）。 **默认取值**: 不涉及。

        :return: The memory_utilization of this CreateSqlLimitTaskRequestBody.
        :rtype: int
        """
        return self._memory_utilization

    @memory_utilization.setter
    def memory_utilization(self, memory_utilization):
        r"""Sets the memory_utilization of this CreateSqlLimitTaskRequestBody.

        **参数解释**: 内存利用率阈值。 **约束限制**: 如果“limit_type”为SESSION_ACTIVE_MAX_COUNT，必传。不支持和CPU利用率阈值同时为0，如果选择只限制CPU、内存中的其中一个，则另一个必须传值0。 **取值范围**: 整数，取值范围[0,100）。 **默认取值**: 不涉及。

        :param memory_utilization: The memory_utilization of this CreateSqlLimitTaskRequestBody.
        :type memory_utilization: int
        """
        self._memory_utilization = memory_utilization

    @property
    def databases(self):
        r"""Gets the databases of this CreateSqlLimitTaskRequestBody.

        **参数解释**: 数据库名称，限流只对指定的数据库生效，多个数据库名称用英文逗号分割。 **约束限制**: 当“limit_type”为SQL_TYPE类型时，databases参数必选。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The databases of this CreateSqlLimitTaskRequestBody.
        :rtype: str
        """
        return self._databases

    @databases.setter
    def databases(self, databases):
        r"""Sets the databases of this CreateSqlLimitTaskRequestBody.

        **参数解释**: 数据库名称，限流只对指定的数据库生效，多个数据库名称用英文逗号分割。 **约束限制**: 当“limit_type”为SQL_TYPE类型时，databases参数必选。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param databases: The databases of this CreateSqlLimitTaskRequestBody.
        :type databases: str
        """
        self._databases = databases

    @property
    def node_infos(self):
        r"""Gets the node_infos of this CreateSqlLimitTaskRequestBody.

        **参数解释**: CN节点信息列表 **约束限制**: 如果“limit_type”为SQL_ID，则“node_infos”必选。

        :return: The node_infos of this CreateSqlLimitTaskRequestBody.
        :rtype: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.CreateLimitTaskNodeOption`]
        """
        return self._node_infos

    @node_infos.setter
    def node_infos(self, node_infos):
        r"""Sets the node_infos of this CreateSqlLimitTaskRequestBody.

        **参数解释**: CN节点信息列表 **约束限制**: 如果“limit_type”为SQL_ID，则“node_infos”必选。

        :param node_infos: The node_infos of this CreateSqlLimitTaskRequestBody.
        :type node_infos: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.CreateLimitTaskNodeOption`]
        """
        self._node_infos = node_infos

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
        if not isinstance(other, CreateSqlLimitTaskRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
