# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryLtsLogParams:

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
        'labels': 'dict(str, str)',
        'is_count': 'bool',
        'keywords': 'str',
        'line_num': 'str',
        'time__': 'str',
        'is_desc': 'bool',
        'search_type': 'str',
        'limit': 'int',
        'highlight': 'bool',
        'is_iterative': 'bool',
        'query': 'str',
        'is_analysis_query': 'bool'
    }

    attribute_map = {
        'start_time': 'start_time',
        'end_time': 'end_time',
        'labels': 'labels',
        'is_count': 'is_count',
        'keywords': 'keywords',
        'line_num': 'line_num',
        'time__': '__time__',
        'is_desc': 'is_desc',
        'search_type': 'search_type',
        'limit': 'limit',
        'highlight': 'highlight',
        'is_iterative': 'is_iterative',
        'query': 'query',
        'is_analysis_query': 'is_analysis_query'
    }

    def __init__(self, start_time=None, end_time=None, labels=None, is_count=None, keywords=None, line_num=None, time__=None, is_desc=None, search_type=None, limit=None, highlight=None, is_iterative=None, query=None, is_analysis_query=None):
        r"""QueryLtsLogParams

        The model defined in huaweicloud sdk

        :param start_time: 搜索起始时间（UTC时间，毫秒级）。
        :type start_time: str
        :param end_time: 搜索结束时间（UTC时间，毫秒级）。
        :type end_time: str
        :param labels: 日志过滤条件集合，不同日志来源所需字段不同。
        :type labels: dict(str, str)
        :param is_count: 日志条数统计。默认为false(不统计)，true为统计日志条数。
        :type is_count: bool
        :param keywords: 支持关键词精确搜索。关键词指相邻两个分词符之间的单词,例：error
        :type keywords: str
        :param line_num: 日志单行序列号，第一次查询时不需要此参数，后续分页查询时需要使用，可从上次查询的返回信息中获取。line_num应在start_time 和 end_time 之间。
        :type line_num: str
        :param time__: 若已开启自定义时间功能，需要使用该字段进行分页查询。
        :type time__: str
        :param is_desc: 顺序或者倒序查询, 默认为false(顺序查询)
        :type is_desc: bool
        :param search_type: 首次查询为 “init”, 分页查询时为 “forwards”或者“backwards”, 默认为首次查询“init”, 与 is_desc 参数配合进行分页查询。
        :type search_type: str
        :param limit: 表示每次查询的日志条数，不填时默认为50，建议您设置为100。
        :type limit: int
        :param highlight: 日志关键词高亮显示，默认为true（高亮显示），false为取消高亮显示。
        :type highlight: bool
        :param is_iterative: 日志迭代查询，默认为false（不开启迭代），true为开启迭代。
        :type is_iterative: bool
        :param query: 使用带管道符的sql分析语句进行查询，需要query参数is_analysis_query为true时生效。
        :type query: str
        :param is_analysis_query: 是否为带管道符的sql分析语句。当该参数为true时，将依照body体中的query参数内容进行查询，且body体中除start_time与end_time以外的参数失效，分页、排序、查询结果条数等功能请依照sql语法规则实现。查询结果的响应体不同于未启用时的查询方式，将以默认列存的形式返回查询结果。当前仅对内测用户开放。响应示例：{\&quot;analysisLogs\&quot;:[{\&quot;field1\&quot;:\&quot;1\&quot;,\&quot;field2\&quot;:\&quot;2\&quot;,\&quot;field3\&quot;:\&quot;3\&quot;},{\&quot;field1\&quot;:\&quot;1\&quot;,\&quot;field2\&quot;:\&quot;2\&quot;,\&quot;field3\&quot;:\&quot;3\&quot;},{\&quot;field1\&quot;:\&quot;1\&quot;,\&quot;field2\&quot;:\&quot;2\&quot;,\&quot;field3\&quot;:\&quot;3\&quot;}]}
        :type is_analysis_query: bool
        """
        
        

        self._start_time = None
        self._end_time = None
        self._labels = None
        self._is_count = None
        self._keywords = None
        self._line_num = None
        self._time__ = None
        self._is_desc = None
        self._search_type = None
        self._limit = None
        self._highlight = None
        self._is_iterative = None
        self._query = None
        self._is_analysis_query = None
        self.discriminator = None

        self.start_time = start_time
        self.end_time = end_time
        if labels is not None:
            self.labels = labels
        if is_count is not None:
            self.is_count = is_count
        if keywords is not None:
            self.keywords = keywords
        if line_num is not None:
            self.line_num = line_num
        if time__ is not None:
            self.time__ = time__
        if is_desc is not None:
            self.is_desc = is_desc
        if search_type is not None:
            self.search_type = search_type
        if limit is not None:
            self.limit = limit
        if highlight is not None:
            self.highlight = highlight
        if is_iterative is not None:
            self.is_iterative = is_iterative
        if query is not None:
            self.query = query
        if is_analysis_query is not None:
            self.is_analysis_query = is_analysis_query

    @property
    def start_time(self):
        r"""Gets the start_time of this QueryLtsLogParams.

        搜索起始时间（UTC时间，毫秒级）。

        :return: The start_time of this QueryLtsLogParams.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this QueryLtsLogParams.

        搜索起始时间（UTC时间，毫秒级）。

        :param start_time: The start_time of this QueryLtsLogParams.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this QueryLtsLogParams.

        搜索结束时间（UTC时间，毫秒级）。

        :return: The end_time of this QueryLtsLogParams.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this QueryLtsLogParams.

        搜索结束时间（UTC时间，毫秒级）。

        :param end_time: The end_time of this QueryLtsLogParams.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def labels(self):
        r"""Gets the labels of this QueryLtsLogParams.

        日志过滤条件集合，不同日志来源所需字段不同。

        :return: The labels of this QueryLtsLogParams.
        :rtype: dict(str, str)
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        r"""Sets the labels of this QueryLtsLogParams.

        日志过滤条件集合，不同日志来源所需字段不同。

        :param labels: The labels of this QueryLtsLogParams.
        :type labels: dict(str, str)
        """
        self._labels = labels

    @property
    def is_count(self):
        r"""Gets the is_count of this QueryLtsLogParams.

        日志条数统计。默认为false(不统计)，true为统计日志条数。

        :return: The is_count of this QueryLtsLogParams.
        :rtype: bool
        """
        return self._is_count

    @is_count.setter
    def is_count(self, is_count):
        r"""Sets the is_count of this QueryLtsLogParams.

        日志条数统计。默认为false(不统计)，true为统计日志条数。

        :param is_count: The is_count of this QueryLtsLogParams.
        :type is_count: bool
        """
        self._is_count = is_count

    @property
    def keywords(self):
        r"""Gets the keywords of this QueryLtsLogParams.

        支持关键词精确搜索。关键词指相邻两个分词符之间的单词,例：error

        :return: The keywords of this QueryLtsLogParams.
        :rtype: str
        """
        return self._keywords

    @keywords.setter
    def keywords(self, keywords):
        r"""Sets the keywords of this QueryLtsLogParams.

        支持关键词精确搜索。关键词指相邻两个分词符之间的单词,例：error

        :param keywords: The keywords of this QueryLtsLogParams.
        :type keywords: str
        """
        self._keywords = keywords

    @property
    def line_num(self):
        r"""Gets the line_num of this QueryLtsLogParams.

        日志单行序列号，第一次查询时不需要此参数，后续分页查询时需要使用，可从上次查询的返回信息中获取。line_num应在start_time 和 end_time 之间。

        :return: The line_num of this QueryLtsLogParams.
        :rtype: str
        """
        return self._line_num

    @line_num.setter
    def line_num(self, line_num):
        r"""Sets the line_num of this QueryLtsLogParams.

        日志单行序列号，第一次查询时不需要此参数，后续分页查询时需要使用，可从上次查询的返回信息中获取。line_num应在start_time 和 end_time 之间。

        :param line_num: The line_num of this QueryLtsLogParams.
        :type line_num: str
        """
        self._line_num = line_num

    @property
    def time__(self):
        r"""Gets the time__ of this QueryLtsLogParams.

        若已开启自定义时间功能，需要使用该字段进行分页查询。

        :return: The time__ of this QueryLtsLogParams.
        :rtype: str
        """
        return self._time__

    @time__.setter
    def time__(self, time__):
        r"""Sets the time__ of this QueryLtsLogParams.

        若已开启自定义时间功能，需要使用该字段进行分页查询。

        :param time__: The time__ of this QueryLtsLogParams.
        :type time__: str
        """
        self._time__ = time__

    @property
    def is_desc(self):
        r"""Gets the is_desc of this QueryLtsLogParams.

        顺序或者倒序查询, 默认为false(顺序查询)

        :return: The is_desc of this QueryLtsLogParams.
        :rtype: bool
        """
        return self._is_desc

    @is_desc.setter
    def is_desc(self, is_desc):
        r"""Sets the is_desc of this QueryLtsLogParams.

        顺序或者倒序查询, 默认为false(顺序查询)

        :param is_desc: The is_desc of this QueryLtsLogParams.
        :type is_desc: bool
        """
        self._is_desc = is_desc

    @property
    def search_type(self):
        r"""Gets the search_type of this QueryLtsLogParams.

        首次查询为 “init”, 分页查询时为 “forwards”或者“backwards”, 默认为首次查询“init”, 与 is_desc 参数配合进行分页查询。

        :return: The search_type of this QueryLtsLogParams.
        :rtype: str
        """
        return self._search_type

    @search_type.setter
    def search_type(self, search_type):
        r"""Sets the search_type of this QueryLtsLogParams.

        首次查询为 “init”, 分页查询时为 “forwards”或者“backwards”, 默认为首次查询“init”, 与 is_desc 参数配合进行分页查询。

        :param search_type: The search_type of this QueryLtsLogParams.
        :type search_type: str
        """
        self._search_type = search_type

    @property
    def limit(self):
        r"""Gets the limit of this QueryLtsLogParams.

        表示每次查询的日志条数，不填时默认为50，建议您设置为100。

        :return: The limit of this QueryLtsLogParams.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this QueryLtsLogParams.

        表示每次查询的日志条数，不填时默认为50，建议您设置为100。

        :param limit: The limit of this QueryLtsLogParams.
        :type limit: int
        """
        self._limit = limit

    @property
    def highlight(self):
        r"""Gets the highlight of this QueryLtsLogParams.

        日志关键词高亮显示，默认为true（高亮显示），false为取消高亮显示。

        :return: The highlight of this QueryLtsLogParams.
        :rtype: bool
        """
        return self._highlight

    @highlight.setter
    def highlight(self, highlight):
        r"""Sets the highlight of this QueryLtsLogParams.

        日志关键词高亮显示，默认为true（高亮显示），false为取消高亮显示。

        :param highlight: The highlight of this QueryLtsLogParams.
        :type highlight: bool
        """
        self._highlight = highlight

    @property
    def is_iterative(self):
        r"""Gets the is_iterative of this QueryLtsLogParams.

        日志迭代查询，默认为false（不开启迭代），true为开启迭代。

        :return: The is_iterative of this QueryLtsLogParams.
        :rtype: bool
        """
        return self._is_iterative

    @is_iterative.setter
    def is_iterative(self, is_iterative):
        r"""Sets the is_iterative of this QueryLtsLogParams.

        日志迭代查询，默认为false（不开启迭代），true为开启迭代。

        :param is_iterative: The is_iterative of this QueryLtsLogParams.
        :type is_iterative: bool
        """
        self._is_iterative = is_iterative

    @property
    def query(self):
        r"""Gets the query of this QueryLtsLogParams.

        使用带管道符的sql分析语句进行查询，需要query参数is_analysis_query为true时生效。

        :return: The query of this QueryLtsLogParams.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        r"""Sets the query of this QueryLtsLogParams.

        使用带管道符的sql分析语句进行查询，需要query参数is_analysis_query为true时生效。

        :param query: The query of this QueryLtsLogParams.
        :type query: str
        """
        self._query = query

    @property
    def is_analysis_query(self):
        r"""Gets the is_analysis_query of this QueryLtsLogParams.

        是否为带管道符的sql分析语句。当该参数为true时，将依照body体中的query参数内容进行查询，且body体中除start_time与end_time以外的参数失效，分页、排序、查询结果条数等功能请依照sql语法规则实现。查询结果的响应体不同于未启用时的查询方式，将以默认列存的形式返回查询结果。当前仅对内测用户开放。响应示例：{\"analysisLogs\":[{\"field1\":\"1\",\"field2\":\"2\",\"field3\":\"3\"},{\"field1\":\"1\",\"field2\":\"2\",\"field3\":\"3\"},{\"field1\":\"1\",\"field2\":\"2\",\"field3\":\"3\"}]}

        :return: The is_analysis_query of this QueryLtsLogParams.
        :rtype: bool
        """
        return self._is_analysis_query

    @is_analysis_query.setter
    def is_analysis_query(self, is_analysis_query):
        r"""Sets the is_analysis_query of this QueryLtsLogParams.

        是否为带管道符的sql分析语句。当该参数为true时，将依照body体中的query参数内容进行查询，且body体中除start_time与end_time以外的参数失效，分页、排序、查询结果条数等功能请依照sql语法规则实现。查询结果的响应体不同于未启用时的查询方式，将以默认列存的形式返回查询结果。当前仅对内测用户开放。响应示例：{\"analysisLogs\":[{\"field1\":\"1\",\"field2\":\"2\",\"field3\":\"3\"},{\"field1\":\"1\",\"field2\":\"2\",\"field3\":\"3\"},{\"field1\":\"1\",\"field2\":\"2\",\"field3\":\"3\"}]}

        :param is_analysis_query: The is_analysis_query of this QueryLtsLogParams.
        :type is_analysis_query: bool
        """
        self._is_analysis_query = is_analysis_query

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
        if not isinstance(other, QueryLtsLogParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
