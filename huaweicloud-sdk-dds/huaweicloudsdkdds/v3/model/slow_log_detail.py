# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SlowLogDetail:

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
        'lock_time': 'int',
        'docs_returned': 'int',
        'docs_scanned': 'int',
        'database': 'str',
        'collection': 'str',
        'log_time': 'str',
        'line_num': 'str'
    }

    attribute_map = {
        'node_name': 'node_name',
        'node_id': 'node_id',
        'whole_message': 'whole_message',
        'operate_type': 'operate_type',
        'cost_time': 'cost_time',
        'lock_time': 'lock_time',
        'docs_returned': 'docs_returned',
        'docs_scanned': 'docs_scanned',
        'database': 'database',
        'collection': 'collection',
        'log_time': 'log_time',
        'line_num': 'line_num'
    }

    def __init__(self, node_name=None, node_id=None, whole_message=None, operate_type=None, cost_time=None, lock_time=None, docs_returned=None, docs_scanned=None, database=None, collection=None, log_time=None, line_num=None):
        """SlowLogDetail

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
        :param lock_time: 等待锁时间。单位：us
        :type lock_time: int
        :param docs_returned: 返回的文档数。
        :type docs_returned: int
        :param docs_scanned: 扫描的文档数。
        :type docs_scanned: int
        :param database: 日志所属的数据库库名。
        :type database: str
        :param collection: 日志所属的数据库表名。
        :type collection: str
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
        self._lock_time = None
        self._docs_returned = None
        self._docs_scanned = None
        self._database = None
        self._collection = None
        self._log_time = None
        self._line_num = None
        self.discriminator = None

        self.node_name = node_name
        self.node_id = node_id
        self.whole_message = whole_message
        self.operate_type = operate_type
        self.cost_time = cost_time
        self.lock_time = lock_time
        self.docs_returned = docs_returned
        self.docs_scanned = docs_scanned
        self.database = database
        self.collection = collection
        self.log_time = log_time
        self.line_num = line_num

    @property
    def node_name(self):
        """Gets the node_name of this SlowLogDetail.

        节点名称。

        :return: The node_name of this SlowLogDetail.
        :rtype: str
        """
        return self._node_name

    @node_name.setter
    def node_name(self, node_name):
        """Sets the node_name of this SlowLogDetail.

        节点名称。

        :param node_name: The node_name of this SlowLogDetail.
        :type node_name: str
        """
        self._node_name = node_name

    @property
    def node_id(self):
        """Gets the node_id of this SlowLogDetail.

        节点ID。

        :return: The node_id of this SlowLogDetail.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this SlowLogDetail.

        节点ID。

        :param node_id: The node_id of this SlowLogDetail.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def whole_message(self):
        """Gets the whole_message of this SlowLogDetail.

        执行语句。

        :return: The whole_message of this SlowLogDetail.
        :rtype: str
        """
        return self._whole_message

    @whole_message.setter
    def whole_message(self, whole_message):
        """Sets the whole_message of this SlowLogDetail.

        执行语句。

        :param whole_message: The whole_message of this SlowLogDetail.
        :type whole_message: str
        """
        self._whole_message = whole_message

    @property
    def operate_type(self):
        """Gets the operate_type of this SlowLogDetail.

        语句类型。

        :return: The operate_type of this SlowLogDetail.
        :rtype: str
        """
        return self._operate_type

    @operate_type.setter
    def operate_type(self, operate_type):
        """Sets the operate_type of this SlowLogDetail.

        语句类型。

        :param operate_type: The operate_type of this SlowLogDetail.
        :type operate_type: str
        """
        self._operate_type = operate_type

    @property
    def cost_time(self):
        """Gets the cost_time of this SlowLogDetail.

        执行时间。单位：ms

        :return: The cost_time of this SlowLogDetail.
        :rtype: int
        """
        return self._cost_time

    @cost_time.setter
    def cost_time(self, cost_time):
        """Sets the cost_time of this SlowLogDetail.

        执行时间。单位：ms

        :param cost_time: The cost_time of this SlowLogDetail.
        :type cost_time: int
        """
        self._cost_time = cost_time

    @property
    def lock_time(self):
        """Gets the lock_time of this SlowLogDetail.

        等待锁时间。单位：us

        :return: The lock_time of this SlowLogDetail.
        :rtype: int
        """
        return self._lock_time

    @lock_time.setter
    def lock_time(self, lock_time):
        """Sets the lock_time of this SlowLogDetail.

        等待锁时间。单位：us

        :param lock_time: The lock_time of this SlowLogDetail.
        :type lock_time: int
        """
        self._lock_time = lock_time

    @property
    def docs_returned(self):
        """Gets the docs_returned of this SlowLogDetail.

        返回的文档数。

        :return: The docs_returned of this SlowLogDetail.
        :rtype: int
        """
        return self._docs_returned

    @docs_returned.setter
    def docs_returned(self, docs_returned):
        """Sets the docs_returned of this SlowLogDetail.

        返回的文档数。

        :param docs_returned: The docs_returned of this SlowLogDetail.
        :type docs_returned: int
        """
        self._docs_returned = docs_returned

    @property
    def docs_scanned(self):
        """Gets the docs_scanned of this SlowLogDetail.

        扫描的文档数。

        :return: The docs_scanned of this SlowLogDetail.
        :rtype: int
        """
        return self._docs_scanned

    @docs_scanned.setter
    def docs_scanned(self, docs_scanned):
        """Sets the docs_scanned of this SlowLogDetail.

        扫描的文档数。

        :param docs_scanned: The docs_scanned of this SlowLogDetail.
        :type docs_scanned: int
        """
        self._docs_scanned = docs_scanned

    @property
    def database(self):
        """Gets the database of this SlowLogDetail.

        日志所属的数据库库名。

        :return: The database of this SlowLogDetail.
        :rtype: str
        """
        return self._database

    @database.setter
    def database(self, database):
        """Sets the database of this SlowLogDetail.

        日志所属的数据库库名。

        :param database: The database of this SlowLogDetail.
        :type database: str
        """
        self._database = database

    @property
    def collection(self):
        """Gets the collection of this SlowLogDetail.

        日志所属的数据库表名。

        :return: The collection of this SlowLogDetail.
        :rtype: str
        """
        return self._collection

    @collection.setter
    def collection(self, collection):
        """Sets the collection of this SlowLogDetail.

        日志所属的数据库表名。

        :param collection: The collection of this SlowLogDetail.
        :type collection: str
        """
        self._collection = collection

    @property
    def log_time(self):
        """Gets the log_time of this SlowLogDetail.

        日志产生时间，UTC时间。 格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :return: The log_time of this SlowLogDetail.
        :rtype: str
        """
        return self._log_time

    @log_time.setter
    def log_time(self, log_time):
        """Sets the log_time of this SlowLogDetail.

        日志产生时间，UTC时间。 格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :param log_time: The log_time of this SlowLogDetail.
        :type log_time: str
        """
        self._log_time = log_time

    @property
    def line_num(self):
        """Gets the line_num of this SlowLogDetail.

        日志单行序列号

        :return: The line_num of this SlowLogDetail.
        :rtype: str
        """
        return self._line_num

    @line_num.setter
    def line_num(self, line_num):
        """Sets the line_num of this SlowLogDetail.

        日志单行序列号

        :param line_num: The line_num of this SlowLogDetail.
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
        if not isinstance(other, SlowLogDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
