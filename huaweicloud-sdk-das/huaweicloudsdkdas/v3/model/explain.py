# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Explain:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'select_type': 'str',
        'table': 'str',
        'type': 'str',
        'possible_keys': 'str',
        'key': 'str',
        'key_len': 'str',
        'ref': 'str',
        'rows': 'int',
        'filtered': 'float',
        'extra': 'str'
    }

    attribute_map = {
        'id': 'id',
        'select_type': 'select_type',
        'table': 'table',
        'type': 'type',
        'possible_keys': 'possible_keys',
        'key': 'key',
        'key_len': 'key_len',
        'ref': 'ref',
        'rows': 'rows',
        'filtered': 'filtered',
        'extra': 'extra'
    }

    def __init__(self, id=None, select_type=None, table=None, type=None, possible_keys=None, key=None, key_len=None, ref=None, rows=None, filtered=None, extra=None):
        """Explain

        The model defined in huaweicloud sdk

        :param id: select子句的编号
        :type id: int
        :param select_type: select子句的类型
        :type select_type: str
        :param table: SQL优化器选择的表join顺序。
        :type table: str
        :param type: 查找表中行的访问类型(从好到坏依次为：null&gt;system&gt;const&gt;eq_ref&gt;ref&gt;range&gt;index&gt;all)。
        :type type: str
        :param possible_keys: 有助于高效查找行的索引。
        :type possible_keys: str
        :param key: 出于最小化查询成本考虑，SQL优化器实际使用的索引
        :type key: str
        :param key_len: key列所示索引的长度（字节）
        :type key_len: str
        :param ref: 在使用key列所示索引查找数据时用到的列或常量
        :type ref: str
        :param rows: key列所示索引的长度（字节）
        :type rows: int
        :param filtered: sql解析的额外信息：当出现using index时，说明SQL使用覆盖索引，性能较好；而当出现 using filesort、using temporary、using where时，说明查询需要优化。
        :type filtered: float
        :param extra: sql解析的额外信息：当出现using index时，说明SQL使用覆盖索引，性能较好；而当出现 using filesort、using temporary、using where时，说明查询需要优化。
        :type extra: str
        """
        
        

        self._id = None
        self._select_type = None
        self._table = None
        self._type = None
        self._possible_keys = None
        self._key = None
        self._key_len = None
        self._ref = None
        self._rows = None
        self._filtered = None
        self._extra = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if select_type is not None:
            self.select_type = select_type
        if table is not None:
            self.table = table
        if type is not None:
            self.type = type
        if possible_keys is not None:
            self.possible_keys = possible_keys
        if key is not None:
            self.key = key
        if key_len is not None:
            self.key_len = key_len
        if ref is not None:
            self.ref = ref
        if rows is not None:
            self.rows = rows
        if filtered is not None:
            self.filtered = filtered
        if extra is not None:
            self.extra = extra

    @property
    def id(self):
        """Gets the id of this Explain.

        select子句的编号

        :return: The id of this Explain.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Explain.

        select子句的编号

        :param id: The id of this Explain.
        :type id: int
        """
        self._id = id

    @property
    def select_type(self):
        """Gets the select_type of this Explain.

        select子句的类型

        :return: The select_type of this Explain.
        :rtype: str
        """
        return self._select_type

    @select_type.setter
    def select_type(self, select_type):
        """Sets the select_type of this Explain.

        select子句的类型

        :param select_type: The select_type of this Explain.
        :type select_type: str
        """
        self._select_type = select_type

    @property
    def table(self):
        """Gets the table of this Explain.

        SQL优化器选择的表join顺序。

        :return: The table of this Explain.
        :rtype: str
        """
        return self._table

    @table.setter
    def table(self, table):
        """Sets the table of this Explain.

        SQL优化器选择的表join顺序。

        :param table: The table of this Explain.
        :type table: str
        """
        self._table = table

    @property
    def type(self):
        """Gets the type of this Explain.

        查找表中行的访问类型(从好到坏依次为：null>system>const>eq_ref>ref>range>index>all)。

        :return: The type of this Explain.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Explain.

        查找表中行的访问类型(从好到坏依次为：null>system>const>eq_ref>ref>range>index>all)。

        :param type: The type of this Explain.
        :type type: str
        """
        self._type = type

    @property
    def possible_keys(self):
        """Gets the possible_keys of this Explain.

        有助于高效查找行的索引。

        :return: The possible_keys of this Explain.
        :rtype: str
        """
        return self._possible_keys

    @possible_keys.setter
    def possible_keys(self, possible_keys):
        """Sets the possible_keys of this Explain.

        有助于高效查找行的索引。

        :param possible_keys: The possible_keys of this Explain.
        :type possible_keys: str
        """
        self._possible_keys = possible_keys

    @property
    def key(self):
        """Gets the key of this Explain.

        出于最小化查询成本考虑，SQL优化器实际使用的索引

        :return: The key of this Explain.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this Explain.

        出于最小化查询成本考虑，SQL优化器实际使用的索引

        :param key: The key of this Explain.
        :type key: str
        """
        self._key = key

    @property
    def key_len(self):
        """Gets the key_len of this Explain.

        key列所示索引的长度（字节）

        :return: The key_len of this Explain.
        :rtype: str
        """
        return self._key_len

    @key_len.setter
    def key_len(self, key_len):
        """Sets the key_len of this Explain.

        key列所示索引的长度（字节）

        :param key_len: The key_len of this Explain.
        :type key_len: str
        """
        self._key_len = key_len

    @property
    def ref(self):
        """Gets the ref of this Explain.

        在使用key列所示索引查找数据时用到的列或常量

        :return: The ref of this Explain.
        :rtype: str
        """
        return self._ref

    @ref.setter
    def ref(self, ref):
        """Sets the ref of this Explain.

        在使用key列所示索引查找数据时用到的列或常量

        :param ref: The ref of this Explain.
        :type ref: str
        """
        self._ref = ref

    @property
    def rows(self):
        """Gets the rows of this Explain.

        key列所示索引的长度（字节）

        :return: The rows of this Explain.
        :rtype: int
        """
        return self._rows

    @rows.setter
    def rows(self, rows):
        """Sets the rows of this Explain.

        key列所示索引的长度（字节）

        :param rows: The rows of this Explain.
        :type rows: int
        """
        self._rows = rows

    @property
    def filtered(self):
        """Gets the filtered of this Explain.

        sql解析的额外信息：当出现using index时，说明SQL使用覆盖索引，性能较好；而当出现 using filesort、using temporary、using where时，说明查询需要优化。

        :return: The filtered of this Explain.
        :rtype: float
        """
        return self._filtered

    @filtered.setter
    def filtered(self, filtered):
        """Sets the filtered of this Explain.

        sql解析的额外信息：当出现using index时，说明SQL使用覆盖索引，性能较好；而当出现 using filesort、using temporary、using where时，说明查询需要优化。

        :param filtered: The filtered of this Explain.
        :type filtered: float
        """
        self._filtered = filtered

    @property
    def extra(self):
        """Gets the extra of this Explain.

        sql解析的额外信息：当出现using index时，说明SQL使用覆盖索引，性能较好；而当出现 using filesort、using temporary、using where时，说明查询需要优化。

        :return: The extra of this Explain.
        :rtype: str
        """
        return self._extra

    @extra.setter
    def extra(self, extra):
        """Sets the extra of this Explain.

        sql解析的额外信息：当出现using index时，说明SQL使用覆盖索引，性能较好；而当出现 using filesort、using temporary、using where时，说明查询需要优化。

        :param extra: The extra of this Explain.
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
        if not isinstance(other, Explain):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
