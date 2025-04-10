# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LtsLogSlowQueryRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'node_id': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'limit': 'int',
        'line_num': 'str',
        'operate_type': 'str',
        'database': 'str'
    }

    attribute_map = {
        'node_id': 'node_id',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'limit': 'limit',
        'line_num': 'line_num',
        'operate_type': 'operate_type',
        'database': 'database'
    }

    def __init__(self, node_id=None, start_time=None, end_time=None, limit=None, line_num=None, operate_type=None, database=None):
        r"""LtsLogSlowQueryRequest

        The model defined in huaweicloud sdk

        :param node_id: 节点ID。
        :type node_id: str
        :param start_time: 开始时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。
        :type start_time: str
        :param end_time: 结束时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。
        :type end_time: str
        :param limit: 查询记录数。
        :type limit: int
        :param line_num: 日志单行序列号，第一次查询时不需要此参数,后续分页查询时需要使用,可从上次查询的返回信息中获取。
        :type line_num: str
        :param operate_type: SQL语句类型，取空值，表示查询所有语句类型，也可指定如下日志类型： - INSERT - UPDATE - SELECT - DELETE - ALTER - DROP - CREATE
        :type operate_type: str
        :param database: 所属数据库。
        :type database: str
        """
        
        

        self._node_id = None
        self._start_time = None
        self._end_time = None
        self._limit = None
        self._line_num = None
        self._operate_type = None
        self._database = None
        self.discriminator = None

        self.node_id = node_id
        self.start_time = start_time
        self.end_time = end_time
        self.limit = limit
        if line_num is not None:
            self.line_num = line_num
        if operate_type is not None:
            self.operate_type = operate_type
        if database is not None:
            self.database = database

    @property
    def node_id(self):
        r"""Gets the node_id of this LtsLogSlowQueryRequest.

        节点ID。

        :return: The node_id of this LtsLogSlowQueryRequest.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this LtsLogSlowQueryRequest.

        节点ID。

        :param node_id: The node_id of this LtsLogSlowQueryRequest.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def start_time(self):
        r"""Gets the start_time of this LtsLogSlowQueryRequest.

        开始时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。

        :return: The start_time of this LtsLogSlowQueryRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this LtsLogSlowQueryRequest.

        开始时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。

        :param start_time: The start_time of this LtsLogSlowQueryRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this LtsLogSlowQueryRequest.

        结束时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。

        :return: The end_time of this LtsLogSlowQueryRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this LtsLogSlowQueryRequest.

        结束时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。

        :param end_time: The end_time of this LtsLogSlowQueryRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def limit(self):
        r"""Gets the limit of this LtsLogSlowQueryRequest.

        查询记录数。

        :return: The limit of this LtsLogSlowQueryRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this LtsLogSlowQueryRequest.

        查询记录数。

        :param limit: The limit of this LtsLogSlowQueryRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def line_num(self):
        r"""Gets the line_num of this LtsLogSlowQueryRequest.

        日志单行序列号，第一次查询时不需要此参数,后续分页查询时需要使用,可从上次查询的返回信息中获取。

        :return: The line_num of this LtsLogSlowQueryRequest.
        :rtype: str
        """
        return self._line_num

    @line_num.setter
    def line_num(self, line_num):
        r"""Sets the line_num of this LtsLogSlowQueryRequest.

        日志单行序列号，第一次查询时不需要此参数,后续分页查询时需要使用,可从上次查询的返回信息中获取。

        :param line_num: The line_num of this LtsLogSlowQueryRequest.
        :type line_num: str
        """
        self._line_num = line_num

    @property
    def operate_type(self):
        r"""Gets the operate_type of this LtsLogSlowQueryRequest.

        SQL语句类型，取空值，表示查询所有语句类型，也可指定如下日志类型： - INSERT - UPDATE - SELECT - DELETE - ALTER - DROP - CREATE

        :return: The operate_type of this LtsLogSlowQueryRequest.
        :rtype: str
        """
        return self._operate_type

    @operate_type.setter
    def operate_type(self, operate_type):
        r"""Sets the operate_type of this LtsLogSlowQueryRequest.

        SQL语句类型，取空值，表示查询所有语句类型，也可指定如下日志类型： - INSERT - UPDATE - SELECT - DELETE - ALTER - DROP - CREATE

        :param operate_type: The operate_type of this LtsLogSlowQueryRequest.
        :type operate_type: str
        """
        self._operate_type = operate_type

    @property
    def database(self):
        r"""Gets the database of this LtsLogSlowQueryRequest.

        所属数据库。

        :return: The database of this LtsLogSlowQueryRequest.
        :rtype: str
        """
        return self._database

    @database.setter
    def database(self, database):
        r"""Sets the database of this LtsLogSlowQueryRequest.

        所属数据库。

        :param database: The database of this LtsLogSlowQueryRequest.
        :type database: str
        """
        self._database = database

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
        if not isinstance(other, LtsLogSlowQueryRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
