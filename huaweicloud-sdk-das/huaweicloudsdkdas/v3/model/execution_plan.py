# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExecutionPlan:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'select_type': 'str',
        'table': 'str',
        'partitions': 'str',
        'type': 'str',
        'possible_keys': 'str',
        'key': 'str',
        'key_len': 'str',
        'ref': 'str',
        'rows': 'str',
        'filtered': 'str',
        'extra': 'str'
    }

    attribute_map = {
        'id': 'id',
        'select_type': 'select_type',
        'table': 'table',
        'partitions': 'partitions',
        'type': 'type',
        'possible_keys': 'possible_keys',
        'key': 'key',
        'key_len': 'key_len',
        'ref': 'ref',
        'rows': 'rows',
        'filtered': 'filtered',
        'extra': 'extra'
    }

    def __init__(self, id=None, select_type=None, table=None, partitions=None, type=None, possible_keys=None, key=None, key_len=None, ref=None, rows=None, filtered=None, extra=None):
        """ExecutionPlan

        The model defined in huaweicloud sdk

        :param id: id
        :type id: str
        :param select_type: select子句的类型
        :type select_type: str
        :param table: 数据库表
        :type table: str
        :param partitions: 查询将匹配记录的分区
        :type partitions: str
        :param type: 访问类型
        :type type: str
        :param possible_keys: 可能使用的键(索引)
        :type possible_keys: str
        :param key: 实际使用的键(索引)
        :type key: str
        :param key_len: 决定使用的键的长度
        :type key_len: str
        :param ref: 使用哪个列或常数与键一起来选择行
        :type ref: str
        :param rows: MySQL认为它执行查询时必须检查的行数
        :type rows: str
        :param filtered: 按表条件过滤的表行的估计百分比
        :type filtered: str
        :param extra: 其他信息
        :type extra: str
        """
        
        

        self._id = None
        self._select_type = None
        self._table = None
        self._partitions = None
        self._type = None
        self._possible_keys = None
        self._key = None
        self._key_len = None
        self._ref = None
        self._rows = None
        self._filtered = None
        self._extra = None
        self.discriminator = None

        self.id = id
        self.select_type = select_type
        self.table = table
        self.partitions = partitions
        self.type = type
        self.possible_keys = possible_keys
        self.key = key
        self.key_len = key_len
        self.ref = ref
        self.rows = rows
        self.filtered = filtered
        self.extra = extra

    @property
    def id(self):
        """Gets the id of this ExecutionPlan.

        id

        :return: The id of this ExecutionPlan.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ExecutionPlan.

        id

        :param id: The id of this ExecutionPlan.
        :type id: str
        """
        self._id = id

    @property
    def select_type(self):
        """Gets the select_type of this ExecutionPlan.

        select子句的类型

        :return: The select_type of this ExecutionPlan.
        :rtype: str
        """
        return self._select_type

    @select_type.setter
    def select_type(self, select_type):
        """Sets the select_type of this ExecutionPlan.

        select子句的类型

        :param select_type: The select_type of this ExecutionPlan.
        :type select_type: str
        """
        self._select_type = select_type

    @property
    def table(self):
        """Gets the table of this ExecutionPlan.

        数据库表

        :return: The table of this ExecutionPlan.
        :rtype: str
        """
        return self._table

    @table.setter
    def table(self, table):
        """Sets the table of this ExecutionPlan.

        数据库表

        :param table: The table of this ExecutionPlan.
        :type table: str
        """
        self._table = table

    @property
    def partitions(self):
        """Gets the partitions of this ExecutionPlan.

        查询将匹配记录的分区

        :return: The partitions of this ExecutionPlan.
        :rtype: str
        """
        return self._partitions

    @partitions.setter
    def partitions(self, partitions):
        """Sets the partitions of this ExecutionPlan.

        查询将匹配记录的分区

        :param partitions: The partitions of this ExecutionPlan.
        :type partitions: str
        """
        self._partitions = partitions

    @property
    def type(self):
        """Gets the type of this ExecutionPlan.

        访问类型

        :return: The type of this ExecutionPlan.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ExecutionPlan.

        访问类型

        :param type: The type of this ExecutionPlan.
        :type type: str
        """
        self._type = type

    @property
    def possible_keys(self):
        """Gets the possible_keys of this ExecutionPlan.

        可能使用的键(索引)

        :return: The possible_keys of this ExecutionPlan.
        :rtype: str
        """
        return self._possible_keys

    @possible_keys.setter
    def possible_keys(self, possible_keys):
        """Sets the possible_keys of this ExecutionPlan.

        可能使用的键(索引)

        :param possible_keys: The possible_keys of this ExecutionPlan.
        :type possible_keys: str
        """
        self._possible_keys = possible_keys

    @property
    def key(self):
        """Gets the key of this ExecutionPlan.

        实际使用的键(索引)

        :return: The key of this ExecutionPlan.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this ExecutionPlan.

        实际使用的键(索引)

        :param key: The key of this ExecutionPlan.
        :type key: str
        """
        self._key = key

    @property
    def key_len(self):
        """Gets the key_len of this ExecutionPlan.

        决定使用的键的长度

        :return: The key_len of this ExecutionPlan.
        :rtype: str
        """
        return self._key_len

    @key_len.setter
    def key_len(self, key_len):
        """Sets the key_len of this ExecutionPlan.

        决定使用的键的长度

        :param key_len: The key_len of this ExecutionPlan.
        :type key_len: str
        """
        self._key_len = key_len

    @property
    def ref(self):
        """Gets the ref of this ExecutionPlan.

        使用哪个列或常数与键一起来选择行

        :return: The ref of this ExecutionPlan.
        :rtype: str
        """
        return self._ref

    @ref.setter
    def ref(self, ref):
        """Sets the ref of this ExecutionPlan.

        使用哪个列或常数与键一起来选择行

        :param ref: The ref of this ExecutionPlan.
        :type ref: str
        """
        self._ref = ref

    @property
    def rows(self):
        """Gets the rows of this ExecutionPlan.

        MySQL认为它执行查询时必须检查的行数

        :return: The rows of this ExecutionPlan.
        :rtype: str
        """
        return self._rows

    @rows.setter
    def rows(self, rows):
        """Sets the rows of this ExecutionPlan.

        MySQL认为它执行查询时必须检查的行数

        :param rows: The rows of this ExecutionPlan.
        :type rows: str
        """
        self._rows = rows

    @property
    def filtered(self):
        """Gets the filtered of this ExecutionPlan.

        按表条件过滤的表行的估计百分比

        :return: The filtered of this ExecutionPlan.
        :rtype: str
        """
        return self._filtered

    @filtered.setter
    def filtered(self, filtered):
        """Sets the filtered of this ExecutionPlan.

        按表条件过滤的表行的估计百分比

        :param filtered: The filtered of this ExecutionPlan.
        :type filtered: str
        """
        self._filtered = filtered

    @property
    def extra(self):
        """Gets the extra of this ExecutionPlan.

        其他信息

        :return: The extra of this ExecutionPlan.
        :rtype: str
        """
        return self._extra

    @extra.setter
    def extra(self, extra):
        """Sets the extra of this ExecutionPlan.

        其他信息

        :param extra: The extra of this ExecutionPlan.
        :type extra: str
        """
        self._extra = extra

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
        if not isinstance(other, ExecutionPlan):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
