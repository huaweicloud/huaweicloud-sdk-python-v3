# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryBodyParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'category': 'str',
        'end_time': 'int',
        'hide_syslog': 'int',
        'key_word': 'str',
        'line_num': 'str',
        'page_size_size': 'str',
        'search_key': 'SearchKey',
        'start_time': 'int',
        'type': 'str',
        'is_desc': 'bool'
    }

    attribute_map = {
        'category': 'category',
        'end_time': 'endTime',
        'hide_syslog': 'hideSyslog',
        'key_word': 'keyWord',
        'line_num': 'lineNum',
        'page_size_size': 'pageSize/size',
        'search_key': 'searchKey',
        'start_time': 'startTime',
        'type': 'type',
        'is_desc': 'isDesc'
    }

    def __init__(self, category=None, end_time=None, hide_syslog=None, key_word=None, line_num=None, page_size_size=None, search_key=None, start_time=None, type=None, is_desc=None):
        """QueryBodyParam

        The model defined in huaweicloud sdk

        :param category: 取值范围 app_log,node _log,custom_log 日志类型字段:app_log:应用日志 node_log:主机日志 custom_log:自定义配置路径日志。
        :type category: str
        :param end_time: 搜索结束时间(UTC时间，毫秒级)。
        :type end_time: int
        :param hide_syslog: 取值范围 0、1 。搜索时是否隐藏系统日志，默认0为隐藏1为显示。
        :type hide_syslog: int
        :param key_word: 1.支持关键词精确搜索。关键词指相邻两个分词符之间的单词。 2.支持关键词模糊匹配搜索，例如输入“RROR”或“ERRO?”或“*ROR*”或“ERR*”或“ER*OR”。 3.支持短语精确搜索，例如输入“Start to refresh alm Statistic”。 4.支持关键词的“与”、“或”组合搜索。格式为“query&amp;&amp;logs”或“query||logs”。 说明： 当前默认分词符有  , &#39;\&quot;;&#x3D;()[]{}@&amp;&lt;&gt;/:\\n\\t\\r
        :type key_word: str
        :param line_num: 日志单行序列号第一次查询时不需要此参数，后续分页查询时需要使用可从上次查询的返回信息中获取.
        :type line_num: str
        :param page_size_size: 表示每次查询的日志条数不填时默认为5000，建议您设置为100。 第一次查询时使用pageSize 后续分页查询时使用size。
        :type page_size_size: str
        :param search_key: 
        :type search_key: :class:`huaweicloudsdkaom.v2.SearchKey`
        :param start_time: 搜索起始时间(UTC时间，毫秒级)。
        :type start_time: int
        :param type: 表示此次查询为分页查询，第一次查询时不需要此参数，后续分页查询时需要使用。
        :type type: str
        :param is_desc: 标识按照lineNum升序查询还是降序查询。  true：降序（lineNum由大到小：时间从新到老）。  false：升序（lineNum由小到大：即时间从老到新）。
        :type is_desc: bool
        """
        
        

        self._category = None
        self._end_time = None
        self._hide_syslog = None
        self._key_word = None
        self._line_num = None
        self._page_size_size = None
        self._search_key = None
        self._start_time = None
        self._type = None
        self._is_desc = None
        self.discriminator = None

        self.category = category
        self.end_time = end_time
        if hide_syslog is not None:
            self.hide_syslog = hide_syslog
        if key_word is not None:
            self.key_word = key_word
        if line_num is not None:
            self.line_num = line_num
        if page_size_size is not None:
            self.page_size_size = page_size_size
        self.search_key = search_key
        self.start_time = start_time
        if type is not None:
            self.type = type
        if is_desc is not None:
            self.is_desc = is_desc

    @property
    def category(self):
        """Gets the category of this QueryBodyParam.

        取值范围 app_log,node _log,custom_log 日志类型字段:app_log:应用日志 node_log:主机日志 custom_log:自定义配置路径日志。

        :return: The category of this QueryBodyParam.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this QueryBodyParam.

        取值范围 app_log,node _log,custom_log 日志类型字段:app_log:应用日志 node_log:主机日志 custom_log:自定义配置路径日志。

        :param category: The category of this QueryBodyParam.
        :type category: str
        """
        self._category = category

    @property
    def end_time(self):
        """Gets the end_time of this QueryBodyParam.

        搜索结束时间(UTC时间，毫秒级)。

        :return: The end_time of this QueryBodyParam.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this QueryBodyParam.

        搜索结束时间(UTC时间，毫秒级)。

        :param end_time: The end_time of this QueryBodyParam.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def hide_syslog(self):
        """Gets the hide_syslog of this QueryBodyParam.

        取值范围 0、1 。搜索时是否隐藏系统日志，默认0为隐藏1为显示。

        :return: The hide_syslog of this QueryBodyParam.
        :rtype: int
        """
        return self._hide_syslog

    @hide_syslog.setter
    def hide_syslog(self, hide_syslog):
        """Sets the hide_syslog of this QueryBodyParam.

        取值范围 0、1 。搜索时是否隐藏系统日志，默认0为隐藏1为显示。

        :param hide_syslog: The hide_syslog of this QueryBodyParam.
        :type hide_syslog: int
        """
        self._hide_syslog = hide_syslog

    @property
    def key_word(self):
        """Gets the key_word of this QueryBodyParam.

        1.支持关键词精确搜索。关键词指相邻两个分词符之间的单词。 2.支持关键词模糊匹配搜索，例如输入“RROR”或“ERRO?”或“*ROR*”或“ERR*”或“ER*OR”。 3.支持短语精确搜索，例如输入“Start to refresh alm Statistic”。 4.支持关键词的“与”、“或”组合搜索。格式为“query&&logs”或“query||logs”。 说明： 当前默认分词符有  , '\";=()[]{}@&<>/:\\n\\t\\r

        :return: The key_word of this QueryBodyParam.
        :rtype: str
        """
        return self._key_word

    @key_word.setter
    def key_word(self, key_word):
        """Sets the key_word of this QueryBodyParam.

        1.支持关键词精确搜索。关键词指相邻两个分词符之间的单词。 2.支持关键词模糊匹配搜索，例如输入“RROR”或“ERRO?”或“*ROR*”或“ERR*”或“ER*OR”。 3.支持短语精确搜索，例如输入“Start to refresh alm Statistic”。 4.支持关键词的“与”、“或”组合搜索。格式为“query&&logs”或“query||logs”。 说明： 当前默认分词符有  , '\";=()[]{}@&<>/:\\n\\t\\r

        :param key_word: The key_word of this QueryBodyParam.
        :type key_word: str
        """
        self._key_word = key_word

    @property
    def line_num(self):
        """Gets the line_num of this QueryBodyParam.

        日志单行序列号第一次查询时不需要此参数，后续分页查询时需要使用可从上次查询的返回信息中获取.

        :return: The line_num of this QueryBodyParam.
        :rtype: str
        """
        return self._line_num

    @line_num.setter
    def line_num(self, line_num):
        """Sets the line_num of this QueryBodyParam.

        日志单行序列号第一次查询时不需要此参数，后续分页查询时需要使用可从上次查询的返回信息中获取.

        :param line_num: The line_num of this QueryBodyParam.
        :type line_num: str
        """
        self._line_num = line_num

    @property
    def page_size_size(self):
        """Gets the page_size_size of this QueryBodyParam.

        表示每次查询的日志条数不填时默认为5000，建议您设置为100。 第一次查询时使用pageSize 后续分页查询时使用size。

        :return: The page_size_size of this QueryBodyParam.
        :rtype: str
        """
        return self._page_size_size

    @page_size_size.setter
    def page_size_size(self, page_size_size):
        """Sets the page_size_size of this QueryBodyParam.

        表示每次查询的日志条数不填时默认为5000，建议您设置为100。 第一次查询时使用pageSize 后续分页查询时使用size。

        :param page_size_size: The page_size_size of this QueryBodyParam.
        :type page_size_size: str
        """
        self._page_size_size = page_size_size

    @property
    def search_key(self):
        """Gets the search_key of this QueryBodyParam.

        :return: The search_key of this QueryBodyParam.
        :rtype: :class:`huaweicloudsdkaom.v2.SearchKey`
        """
        return self._search_key

    @search_key.setter
    def search_key(self, search_key):
        """Sets the search_key of this QueryBodyParam.

        :param search_key: The search_key of this QueryBodyParam.
        :type search_key: :class:`huaweicloudsdkaom.v2.SearchKey`
        """
        self._search_key = search_key

    @property
    def start_time(self):
        """Gets the start_time of this QueryBodyParam.

        搜索起始时间(UTC时间，毫秒级)。

        :return: The start_time of this QueryBodyParam.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this QueryBodyParam.

        搜索起始时间(UTC时间，毫秒级)。

        :param start_time: The start_time of this QueryBodyParam.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def type(self):
        """Gets the type of this QueryBodyParam.

        表示此次查询为分页查询，第一次查询时不需要此参数，后续分页查询时需要使用。

        :return: The type of this QueryBodyParam.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this QueryBodyParam.

        表示此次查询为分页查询，第一次查询时不需要此参数，后续分页查询时需要使用。

        :param type: The type of this QueryBodyParam.
        :type type: str
        """
        self._type = type

    @property
    def is_desc(self):
        """Gets the is_desc of this QueryBodyParam.

        标识按照lineNum升序查询还是降序查询。  true：降序（lineNum由大到小：时间从新到老）。  false：升序（lineNum由小到大：即时间从老到新）。

        :return: The is_desc of this QueryBodyParam.
        :rtype: bool
        """
        return self._is_desc

    @is_desc.setter
    def is_desc(self, is_desc):
        """Sets the is_desc of this QueryBodyParam.

        标识按照lineNum升序查询还是降序查询。  true：降序（lineNum由大到小：时间从新到老）。  false：升序（lineNum由小到大：即时间从老到新）。

        :param is_desc: The is_desc of this QueryBodyParam.
        :type is_desc: bool
        """
        self._is_desc = is_desc

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
        if not isinstance(other, QueryBodyParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
