# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InfluxdbSlowLogDetail:

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
        'node_name': 'str',
        'whole_message': 'str',
        'operate_type': 'str',
        'cost_time': 'str',
        'log_time': 'str',
        'database': 'str',
        'retention_policy': 'str',
        'line_num': 'str'
    }

    attribute_map = {
        'node_id': 'node_id',
        'node_name': 'node_name',
        'whole_message': 'whole_message',
        'operate_type': 'operate_type',
        'cost_time': 'cost_time',
        'log_time': 'log_time',
        'database': 'database',
        'retention_policy': 'retention_policy',
        'line_num': 'line_num'
    }

    def __init__(self, node_id=None, node_name=None, whole_message=None, operate_type=None, cost_time=None, log_time=None, database=None, retention_policy=None, line_num=None):
        """InfluxdbSlowLogDetail

        The model defined in huaweicloud sdk

        :param node_id: 节点ID。
        :type node_id: str
        :param node_name: 节点名称。
        :type node_name: str
        :param whole_message: 执行语句。
        :type whole_message: str
        :param operate_type: 语句类型。
        :type operate_type: str
        :param cost_time: 执行时间。单位：ms
        :type cost_time: str
        :param log_time: 日志产生时间，UTC时间。 格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。
        :type log_time: str
        :param database: 数据库名称。
        :type database: str
        :param retention_policy: 保留策略。
        :type retention_policy: str
        :param line_num: 日志单行序列号。
        :type line_num: str
        """
        
        

        self._node_id = None
        self._node_name = None
        self._whole_message = None
        self._operate_type = None
        self._cost_time = None
        self._log_time = None
        self._database = None
        self._retention_policy = None
        self._line_num = None
        self.discriminator = None

        self.node_id = node_id
        self.node_name = node_name
        self.whole_message = whole_message
        self.operate_type = operate_type
        self.cost_time = cost_time
        self.log_time = log_time
        self.database = database
        self.retention_policy = retention_policy
        self.line_num = line_num

    @property
    def node_id(self):
        """Gets the node_id of this InfluxdbSlowLogDetail.

        节点ID。

        :return: The node_id of this InfluxdbSlowLogDetail.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this InfluxdbSlowLogDetail.

        节点ID。

        :param node_id: The node_id of this InfluxdbSlowLogDetail.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def node_name(self):
        """Gets the node_name of this InfluxdbSlowLogDetail.

        节点名称。

        :return: The node_name of this InfluxdbSlowLogDetail.
        :rtype: str
        """
        return self._node_name

    @node_name.setter
    def node_name(self, node_name):
        """Sets the node_name of this InfluxdbSlowLogDetail.

        节点名称。

        :param node_name: The node_name of this InfluxdbSlowLogDetail.
        :type node_name: str
        """
        self._node_name = node_name

    @property
    def whole_message(self):
        """Gets the whole_message of this InfluxdbSlowLogDetail.

        执行语句。

        :return: The whole_message of this InfluxdbSlowLogDetail.
        :rtype: str
        """
        return self._whole_message

    @whole_message.setter
    def whole_message(self, whole_message):
        """Sets the whole_message of this InfluxdbSlowLogDetail.

        执行语句。

        :param whole_message: The whole_message of this InfluxdbSlowLogDetail.
        :type whole_message: str
        """
        self._whole_message = whole_message

    @property
    def operate_type(self):
        """Gets the operate_type of this InfluxdbSlowLogDetail.

        语句类型。

        :return: The operate_type of this InfluxdbSlowLogDetail.
        :rtype: str
        """
        return self._operate_type

    @operate_type.setter
    def operate_type(self, operate_type):
        """Sets the operate_type of this InfluxdbSlowLogDetail.

        语句类型。

        :param operate_type: The operate_type of this InfluxdbSlowLogDetail.
        :type operate_type: str
        """
        self._operate_type = operate_type

    @property
    def cost_time(self):
        """Gets the cost_time of this InfluxdbSlowLogDetail.

        执行时间。单位：ms

        :return: The cost_time of this InfluxdbSlowLogDetail.
        :rtype: str
        """
        return self._cost_time

    @cost_time.setter
    def cost_time(self, cost_time):
        """Sets the cost_time of this InfluxdbSlowLogDetail.

        执行时间。单位：ms

        :param cost_time: The cost_time of this InfluxdbSlowLogDetail.
        :type cost_time: str
        """
        self._cost_time = cost_time

    @property
    def log_time(self):
        """Gets the log_time of this InfluxdbSlowLogDetail.

        日志产生时间，UTC时间。 格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :return: The log_time of this InfluxdbSlowLogDetail.
        :rtype: str
        """
        return self._log_time

    @log_time.setter
    def log_time(self, log_time):
        """Sets the log_time of this InfluxdbSlowLogDetail.

        日志产生时间，UTC时间。 格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :param log_time: The log_time of this InfluxdbSlowLogDetail.
        :type log_time: str
        """
        self._log_time = log_time

    @property
    def database(self):
        """Gets the database of this InfluxdbSlowLogDetail.

        数据库名称。

        :return: The database of this InfluxdbSlowLogDetail.
        :rtype: str
        """
        return self._database

    @database.setter
    def database(self, database):
        """Sets the database of this InfluxdbSlowLogDetail.

        数据库名称。

        :param database: The database of this InfluxdbSlowLogDetail.
        :type database: str
        """
        self._database = database

    @property
    def retention_policy(self):
        """Gets the retention_policy of this InfluxdbSlowLogDetail.

        保留策略。

        :return: The retention_policy of this InfluxdbSlowLogDetail.
        :rtype: str
        """
        return self._retention_policy

    @retention_policy.setter
    def retention_policy(self, retention_policy):
        """Sets the retention_policy of this InfluxdbSlowLogDetail.

        保留策略。

        :param retention_policy: The retention_policy of this InfluxdbSlowLogDetail.
        :type retention_policy: str
        """
        self._retention_policy = retention_policy

    @property
    def line_num(self):
        """Gets the line_num of this InfluxdbSlowLogDetail.

        日志单行序列号。

        :return: The line_num of this InfluxdbSlowLogDetail.
        :rtype: str
        """
        return self._line_num

    @line_num.setter
    def line_num(self, line_num):
        """Sets the line_num of this InfluxdbSlowLogDetail.

        日志单行序列号。

        :param line_num: The line_num of this InfluxdbSlowLogDetail.
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
        if not isinstance(other, InfluxdbSlowLogDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
