# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CassandraSlowLogDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'node_name': 'str',
        'node_id': 'str',
        'whole_message': 'str',
        'operate_type': 'str',
        'cost_time': 'int',
        'keyspace': 'str',
        'table': 'str',
        'log_time': 'str',
        'line_num': 'str'
    }

    attribute_map = {
        'node_name': 'node_name',
        'node_id': 'node_id',
        'whole_message': 'whole_message',
        'operate_type': 'operate_type',
        'cost_time': 'cost_time',
        'keyspace': 'keyspace',
        'table': 'table',
        'log_time': 'log_time',
        'line_num': 'line_num'
    }

    def __init__(self, node_name=None, node_id=None, whole_message=None, operate_type=None, cost_time=None, keyspace=None, table=None, log_time=None, line_num=None):
        r"""CassandraSlowLogDetail

        The model defined in huaweicloud sdk

        :param node_name: 节点名称。
        :type node_name: str
        :param node_id: 节点ID。
        :type node_id: str
        :param whole_message: 执行语句。
        :type whole_message: str
        :param operate_type: 语句类型。
        :type operate_type: str
        :param cost_time: 执行时间。单位：ms
        :type cost_time: int
        :param keyspace: 数据库键空间
        :type keyspace: str
        :param table: 数据库表名
        :type table: str
        :param log_time: 日志产生时间，UTC时间。 格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。
        :type log_time: str
        :param line_num: 日志单行序列号
        :type line_num: str
        """
        
        

        self._node_name = None
        self._node_id = None
        self._whole_message = None
        self._operate_type = None
        self._cost_time = None
        self._keyspace = None
        self._table = None
        self._log_time = None
        self._line_num = None
        self.discriminator = None

        self.node_name = node_name
        self.node_id = node_id
        self.whole_message = whole_message
        self.operate_type = operate_type
        self.cost_time = cost_time
        self.keyspace = keyspace
        self.table = table
        self.log_time = log_time
        self.line_num = line_num

    @property
    def node_name(self):
        r"""Gets the node_name of this CassandraSlowLogDetail.

        节点名称。

        :return: The node_name of this CassandraSlowLogDetail.
        :rtype: str
        """
        return self._node_name

    @node_name.setter
    def node_name(self, node_name):
        r"""Sets the node_name of this CassandraSlowLogDetail.

        节点名称。

        :param node_name: The node_name of this CassandraSlowLogDetail.
        :type node_name: str
        """
        self._node_name = node_name

    @property
    def node_id(self):
        r"""Gets the node_id of this CassandraSlowLogDetail.

        节点ID。

        :return: The node_id of this CassandraSlowLogDetail.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this CassandraSlowLogDetail.

        节点ID。

        :param node_id: The node_id of this CassandraSlowLogDetail.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def whole_message(self):
        r"""Gets the whole_message of this CassandraSlowLogDetail.

        执行语句。

        :return: The whole_message of this CassandraSlowLogDetail.
        :rtype: str
        """
        return self._whole_message

    @whole_message.setter
    def whole_message(self, whole_message):
        r"""Sets the whole_message of this CassandraSlowLogDetail.

        执行语句。

        :param whole_message: The whole_message of this CassandraSlowLogDetail.
        :type whole_message: str
        """
        self._whole_message = whole_message

    @property
    def operate_type(self):
        r"""Gets the operate_type of this CassandraSlowLogDetail.

        语句类型。

        :return: The operate_type of this CassandraSlowLogDetail.
        :rtype: str
        """
        return self._operate_type

    @operate_type.setter
    def operate_type(self, operate_type):
        r"""Sets the operate_type of this CassandraSlowLogDetail.

        语句类型。

        :param operate_type: The operate_type of this CassandraSlowLogDetail.
        :type operate_type: str
        """
        self._operate_type = operate_type

    @property
    def cost_time(self):
        r"""Gets the cost_time of this CassandraSlowLogDetail.

        执行时间。单位：ms

        :return: The cost_time of this CassandraSlowLogDetail.
        :rtype: int
        """
        return self._cost_time

    @cost_time.setter
    def cost_time(self, cost_time):
        r"""Sets the cost_time of this CassandraSlowLogDetail.

        执行时间。单位：ms

        :param cost_time: The cost_time of this CassandraSlowLogDetail.
        :type cost_time: int
        """
        self._cost_time = cost_time

    @property
    def keyspace(self):
        r"""Gets the keyspace of this CassandraSlowLogDetail.

        数据库键空间

        :return: The keyspace of this CassandraSlowLogDetail.
        :rtype: str
        """
        return self._keyspace

    @keyspace.setter
    def keyspace(self, keyspace):
        r"""Sets the keyspace of this CassandraSlowLogDetail.

        数据库键空间

        :param keyspace: The keyspace of this CassandraSlowLogDetail.
        :type keyspace: str
        """
        self._keyspace = keyspace

    @property
    def table(self):
        r"""Gets the table of this CassandraSlowLogDetail.

        数据库表名

        :return: The table of this CassandraSlowLogDetail.
        :rtype: str
        """
        return self._table

    @table.setter
    def table(self, table):
        r"""Sets the table of this CassandraSlowLogDetail.

        数据库表名

        :param table: The table of this CassandraSlowLogDetail.
        :type table: str
        """
        self._table = table

    @property
    def log_time(self):
        r"""Gets the log_time of this CassandraSlowLogDetail.

        日志产生时间，UTC时间。 格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :return: The log_time of this CassandraSlowLogDetail.
        :rtype: str
        """
        return self._log_time

    @log_time.setter
    def log_time(self, log_time):
        r"""Sets the log_time of this CassandraSlowLogDetail.

        日志产生时间，UTC时间。 格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :param log_time: The log_time of this CassandraSlowLogDetail.
        :type log_time: str
        """
        self._log_time = log_time

    @property
    def line_num(self):
        r"""Gets the line_num of this CassandraSlowLogDetail.

        日志单行序列号

        :return: The line_num of this CassandraSlowLogDetail.
        :rtype: str
        """
        return self._line_num

    @line_num.setter
    def line_num(self, line_num):
        r"""Sets the line_num of this CassandraSlowLogDetail.

        日志单行序列号

        :param line_num: The line_num of this CassandraSlowLogDetail.
        :type line_num: str
        """
        self._line_num = line_num

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
        if not isinstance(other, CassandraSlowLogDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
