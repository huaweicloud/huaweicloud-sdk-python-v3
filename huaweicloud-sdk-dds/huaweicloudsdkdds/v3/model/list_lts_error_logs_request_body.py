# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListLtsErrorLogsRequestBody:

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
        'limit': 'int',
        'line_num': 'str',
        'severity': 'str',
        'search_type': 'str',
        'node_id': 'str',
        'keywords': 'list[str]'
    }

    attribute_map = {
        'start_time': 'start_time',
        'end_time': 'end_time',
        'limit': 'limit',
        'line_num': 'line_num',
        'severity': 'severity',
        'search_type': 'search_type',
        'node_id': 'node_id',
        'keywords': 'keywords'
    }

    def __init__(self, start_time=None, end_time=None, limit=None, line_num=None, severity=None, search_type=None, node_id=None, keywords=None):
        r"""ListLtsErrorLogsRequestBody

        The model defined in huaweicloud sdk

        :param start_time: 开始时间，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。注：开始时间不得早于当前时间30天。
        :type start_time: str
        :param end_time: 结束时间，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。注：结束时间不能晚于当前时间。
        :type end_time: str
        :param limit: 表示每次查询的日志条数，最大限制100条。
        :type limit: int
        :param line_num: 日志单行序列号，第一次查询时不需要此参数，下一页查询时需要使用，可从上一次查询的返回信息中获取。 说明：当次查询从line_num的下一条日志开始查询，不包含当前line_num日志。
        :type line_num: str
        :param severity: 日志级别，取空值表示查询所有日志级别。
        :type severity: str
        :param search_type: 日志查询方式，需结合line_num使用, 以line_num的日志为起始点: - 取值\&quot;backwards\&quot;时，表示查询上一页limit大小的日志 - 取值\&quot;forwards\&quot;时，表示查询下一页limit大小的日志 - 不传默认\&quot;forwards\&quot;
        :type search_type: str
        :param node_id: 节点ID，取空值，表示查询实例下所有允许查询的节点。 使用请参考《DDS API参考》的“查询实例列表和详情”响应消息表“nodes 数据结构说明”的“id”。允许查询的节点如下： - 集群实例下面的 shard节点 - 副本集、单节点实例下面的所有节点
        :type node_id: str
        :param keywords: 根据多个关键字搜索日志全文，表示同时匹配所有关键字。 - 只支持关键字前缀模糊搜索，最多支持10个关键字。 - 每个关键字最大长度不超过512个字符。
        :type keywords: list[str]
        """
        
        

        self._start_time = None
        self._end_time = None
        self._limit = None
        self._line_num = None
        self._severity = None
        self._search_type = None
        self._node_id = None
        self._keywords = None
        self.discriminator = None

        self.start_time = start_time
        self.end_time = end_time
        self.limit = limit
        if line_num is not None:
            self.line_num = line_num
        if severity is not None:
            self.severity = severity
        if search_type is not None:
            self.search_type = search_type
        if node_id is not None:
            self.node_id = node_id
        if keywords is not None:
            self.keywords = keywords

    @property
    def start_time(self):
        r"""Gets the start_time of this ListLtsErrorLogsRequestBody.

        开始时间，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。注：开始时间不得早于当前时间30天。

        :return: The start_time of this ListLtsErrorLogsRequestBody.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListLtsErrorLogsRequestBody.

        开始时间，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。注：开始时间不得早于当前时间30天。

        :param start_time: The start_time of this ListLtsErrorLogsRequestBody.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListLtsErrorLogsRequestBody.

        结束时间，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。注：结束时间不能晚于当前时间。

        :return: The end_time of this ListLtsErrorLogsRequestBody.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListLtsErrorLogsRequestBody.

        结束时间，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。注：结束时间不能晚于当前时间。

        :param end_time: The end_time of this ListLtsErrorLogsRequestBody.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def limit(self):
        r"""Gets the limit of this ListLtsErrorLogsRequestBody.

        表示每次查询的日志条数，最大限制100条。

        :return: The limit of this ListLtsErrorLogsRequestBody.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListLtsErrorLogsRequestBody.

        表示每次查询的日志条数，最大限制100条。

        :param limit: The limit of this ListLtsErrorLogsRequestBody.
        :type limit: int
        """
        self._limit = limit

    @property
    def line_num(self):
        r"""Gets the line_num of this ListLtsErrorLogsRequestBody.

        日志单行序列号，第一次查询时不需要此参数，下一页查询时需要使用，可从上一次查询的返回信息中获取。 说明：当次查询从line_num的下一条日志开始查询，不包含当前line_num日志。

        :return: The line_num of this ListLtsErrorLogsRequestBody.
        :rtype: str
        """
        return self._line_num

    @line_num.setter
    def line_num(self, line_num):
        r"""Sets the line_num of this ListLtsErrorLogsRequestBody.

        日志单行序列号，第一次查询时不需要此参数，下一页查询时需要使用，可从上一次查询的返回信息中获取。 说明：当次查询从line_num的下一条日志开始查询，不包含当前line_num日志。

        :param line_num: The line_num of this ListLtsErrorLogsRequestBody.
        :type line_num: str
        """
        self._line_num = line_num

    @property
    def severity(self):
        r"""Gets the severity of this ListLtsErrorLogsRequestBody.

        日志级别，取空值表示查询所有日志级别。

        :return: The severity of this ListLtsErrorLogsRequestBody.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        r"""Sets the severity of this ListLtsErrorLogsRequestBody.

        日志级别，取空值表示查询所有日志级别。

        :param severity: The severity of this ListLtsErrorLogsRequestBody.
        :type severity: str
        """
        self._severity = severity

    @property
    def search_type(self):
        r"""Gets the search_type of this ListLtsErrorLogsRequestBody.

        日志查询方式，需结合line_num使用, 以line_num的日志为起始点: - 取值\"backwards\"时，表示查询上一页limit大小的日志 - 取值\"forwards\"时，表示查询下一页limit大小的日志 - 不传默认\"forwards\"

        :return: The search_type of this ListLtsErrorLogsRequestBody.
        :rtype: str
        """
        return self._search_type

    @search_type.setter
    def search_type(self, search_type):
        r"""Sets the search_type of this ListLtsErrorLogsRequestBody.

        日志查询方式，需结合line_num使用, 以line_num的日志为起始点: - 取值\"backwards\"时，表示查询上一页limit大小的日志 - 取值\"forwards\"时，表示查询下一页limit大小的日志 - 不传默认\"forwards\"

        :param search_type: The search_type of this ListLtsErrorLogsRequestBody.
        :type search_type: str
        """
        self._search_type = search_type

    @property
    def node_id(self):
        r"""Gets the node_id of this ListLtsErrorLogsRequestBody.

        节点ID，取空值，表示查询实例下所有允许查询的节点。 使用请参考《DDS API参考》的“查询实例列表和详情”响应消息表“nodes 数据结构说明”的“id”。允许查询的节点如下： - 集群实例下面的 shard节点 - 副本集、单节点实例下面的所有节点

        :return: The node_id of this ListLtsErrorLogsRequestBody.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this ListLtsErrorLogsRequestBody.

        节点ID，取空值，表示查询实例下所有允许查询的节点。 使用请参考《DDS API参考》的“查询实例列表和详情”响应消息表“nodes 数据结构说明”的“id”。允许查询的节点如下： - 集群实例下面的 shard节点 - 副本集、单节点实例下面的所有节点

        :param node_id: The node_id of this ListLtsErrorLogsRequestBody.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def keywords(self):
        r"""Gets the keywords of this ListLtsErrorLogsRequestBody.

        根据多个关键字搜索日志全文，表示同时匹配所有关键字。 - 只支持关键字前缀模糊搜索，最多支持10个关键字。 - 每个关键字最大长度不超过512个字符。

        :return: The keywords of this ListLtsErrorLogsRequestBody.
        :rtype: list[str]
        """
        return self._keywords

    @keywords.setter
    def keywords(self, keywords):
        r"""Sets the keywords of this ListLtsErrorLogsRequestBody.

        根据多个关键字搜索日志全文，表示同时匹配所有关键字。 - 只支持关键字前缀模糊搜索，最多支持10个关键字。 - 每个关键字最大长度不超过512个字符。

        :param keywords: The keywords of this ListLtsErrorLogsRequestBody.
        :type keywords: list[str]
        """
        self._keywords = keywords

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
        if not isinstance(other, ListLtsErrorLogsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
