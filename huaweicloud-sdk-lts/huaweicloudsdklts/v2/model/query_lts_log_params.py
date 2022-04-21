# coding: utf-8

import re
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
        'is_desc': 'bool',
        'search_type': 'str',
        'limit': 'int',
        'highlight': 'bool'
    }

    attribute_map = {
        'start_time': 'start_time',
        'end_time': 'end_time',
        'labels': 'labels',
        'is_count': 'is_count',
        'keywords': 'keywords',
        'line_num': 'line_num',
        'is_desc': 'is_desc',
        'search_type': 'search_type',
        'limit': 'limit',
        'highlight': 'highlight'
    }

    def __init__(self, start_time=None, end_time=None, labels=None, is_count=None, keywords=None, line_num=None, is_desc=None, search_type=None, limit=None, highlight=None):
        """QueryLtsLogParams

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
        :param is_desc: 顺序或者倒序查询, 默认为false(顺序查询)
        :type is_desc: bool
        :param search_type: 首次查询为 “init”, 分页查询时为 “forwards”或者“backwards”, 默认为首次查询“init”, 与 is_desc 参数配合进行分页查询。
        :type search_type: str
        :param limit: 表示每次查询的日志条数，不填时默认为50，建议您设置为100。
        :type limit: int
        :param highlight: 日志关键词高亮显示，默认为true（高亮显示），false为取消高亮显示。
        :type highlight: bool
        """
        
        

        self._start_time = None
        self._end_time = None
        self._labels = None
        self._is_count = None
        self._keywords = None
        self._line_num = None
        self._is_desc = None
        self._search_type = None
        self._limit = None
        self._highlight = None
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
        if is_desc is not None:
            self.is_desc = is_desc
        if search_type is not None:
            self.search_type = search_type
        if limit is not None:
            self.limit = limit
        if highlight is not None:
            self.highlight = highlight

    @property
    def start_time(self):
        """Gets the start_time of this QueryLtsLogParams.

        搜索起始时间（UTC时间，毫秒级）。

        :return: The start_time of this QueryLtsLogParams.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this QueryLtsLogParams.

        搜索起始时间（UTC时间，毫秒级）。

        :param start_time: The start_time of this QueryLtsLogParams.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this QueryLtsLogParams.

        搜索结束时间（UTC时间，毫秒级）。

        :return: The end_time of this QueryLtsLogParams.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this QueryLtsLogParams.

        搜索结束时间（UTC时间，毫秒级）。

        :param end_time: The end_time of this QueryLtsLogParams.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def labels(self):
        """Gets the labels of this QueryLtsLogParams.

        日志过滤条件集合，不同日志来源所需字段不同。

        :return: The labels of this QueryLtsLogParams.
        :rtype: dict(str, str)
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this QueryLtsLogParams.

        日志过滤条件集合，不同日志来源所需字段不同。

        :param labels: The labels of this QueryLtsLogParams.
        :type labels: dict(str, str)
        """
        self._labels = labels

    @property
    def is_count(self):
        """Gets the is_count of this QueryLtsLogParams.

        日志条数统计。默认为false(不统计)，true为统计日志条数。

        :return: The is_count of this QueryLtsLogParams.
        :rtype: bool
        """
        return self._is_count

    @is_count.setter
    def is_count(self, is_count):
        """Sets the is_count of this QueryLtsLogParams.

        日志条数统计。默认为false(不统计)，true为统计日志条数。

        :param is_count: The is_count of this QueryLtsLogParams.
        :type is_count: bool
        """
        self._is_count = is_count

    @property
    def keywords(self):
        """Gets the keywords of this QueryLtsLogParams.

        支持关键词精确搜索。关键词指相邻两个分词符之间的单词,例：error

        :return: The keywords of this QueryLtsLogParams.
        :rtype: str
        """
        return self._keywords

    @keywords.setter
    def keywords(self, keywords):
        """Sets the keywords of this QueryLtsLogParams.

        支持关键词精确搜索。关键词指相邻两个分词符之间的单词,例：error

        :param keywords: The keywords of this QueryLtsLogParams.
        :type keywords: str
        """
        self._keywords = keywords

    @property
    def line_num(self):
        """Gets the line_num of this QueryLtsLogParams.

        日志单行序列号，第一次查询时不需要此参数，后续分页查询时需要使用，可从上次查询的返回信息中获取。line_num应在start_time 和 end_time 之间。

        :return: The line_num of this QueryLtsLogParams.
        :rtype: str
        """
        return self._line_num

    @line_num.setter
    def line_num(self, line_num):
        """Sets the line_num of this QueryLtsLogParams.

        日志单行序列号，第一次查询时不需要此参数，后续分页查询时需要使用，可从上次查询的返回信息中获取。line_num应在start_time 和 end_time 之间。

        :param line_num: The line_num of this QueryLtsLogParams.
        :type line_num: str
        """
        self._line_num = line_num

    @property
    def is_desc(self):
        """Gets the is_desc of this QueryLtsLogParams.

        顺序或者倒序查询, 默认为false(顺序查询)

        :return: The is_desc of this QueryLtsLogParams.
        :rtype: bool
        """
        return self._is_desc

    @is_desc.setter
    def is_desc(self, is_desc):
        """Sets the is_desc of this QueryLtsLogParams.

        顺序或者倒序查询, 默认为false(顺序查询)

        :param is_desc: The is_desc of this QueryLtsLogParams.
        :type is_desc: bool
        """
        self._is_desc = is_desc

    @property
    def search_type(self):
        """Gets the search_type of this QueryLtsLogParams.

        首次查询为 “init”, 分页查询时为 “forwards”或者“backwards”, 默认为首次查询“init”, 与 is_desc 参数配合进行分页查询。

        :return: The search_type of this QueryLtsLogParams.
        :rtype: str
        """
        return self._search_type

    @search_type.setter
    def search_type(self, search_type):
        """Sets the search_type of this QueryLtsLogParams.

        首次查询为 “init”, 分页查询时为 “forwards”或者“backwards”, 默认为首次查询“init”, 与 is_desc 参数配合进行分页查询。

        :param search_type: The search_type of this QueryLtsLogParams.
        :type search_type: str
        """
        self._search_type = search_type

    @property
    def limit(self):
        """Gets the limit of this QueryLtsLogParams.

        表示每次查询的日志条数，不填时默认为50，建议您设置为100。

        :return: The limit of this QueryLtsLogParams.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this QueryLtsLogParams.

        表示每次查询的日志条数，不填时默认为50，建议您设置为100。

        :param limit: The limit of this QueryLtsLogParams.
        :type limit: int
        """
        self._limit = limit

    @property
    def highlight(self):
        """Gets the highlight of this QueryLtsLogParams.

        日志关键词高亮显示，默认为true（高亮显示），false为取消高亮显示。

        :return: The highlight of this QueryLtsLogParams.
        :rtype: bool
        """
        return self._highlight

    @highlight.setter
    def highlight(self, highlight):
        """Sets the highlight of this QueryLtsLogParams.

        日志关键词高亮显示，默认为true（高亮显示），false为取消高亮显示。

        :param highlight: The highlight of this QueryLtsLogParams.
        :type highlight: bool
        """
        self._highlight = highlight

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
