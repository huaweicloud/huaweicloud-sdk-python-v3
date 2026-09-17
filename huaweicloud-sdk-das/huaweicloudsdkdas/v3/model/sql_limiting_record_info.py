# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SqlLimitingRecordInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'item_id': 'str',
        'type': 'str',
        'key_str': 'str',
        'max_connection': 'str',
        'max_waiting': 'str',
        'cur_connection': 'int',
        'cur_reject': 'int',
        'total_reject': 'int',
        'create_at': 'str',
        'query_id': 'str'
    }

    attribute_map = {
        'item_id': 'item_id',
        'type': 'type',
        'key_str': 'key_str',
        'max_connection': 'max_connection',
        'max_waiting': 'max_waiting',
        'cur_connection': 'cur_connection',
        'cur_reject': 'cur_reject',
        'total_reject': 'total_reject',
        'create_at': 'create_at',
        'query_id': 'query_id'
    }

    def __init__(self, item_id=None, type=None, key_str=None, max_connection=None, max_waiting=None, cur_connection=None, cur_reject=None, total_reject=None, create_at=None, query_id=None):
        r"""SqlLimitingRecordInfo

        The model defined in huaweicloud sdk

        :param item_id: SQL限流规则ID
        :type item_id: str
        :param type: SQL类型
        :type type: str
        :param key_str: 限流规则
        :type key_str: str
        :param max_connection: 最大并发数
        :type max_connection: str
        :param max_waiting: 最大等待时间
        :type max_waiting: str
        :param cur_connection: 当前并发数
        :type cur_connection: int
        :param cur_reject: 当前拦截数
        :type cur_reject: int
        :param total_reject: 总拦截数
        :type total_reject: int
        :param create_at: 创建时间
        :type create_at: str
        :param query_id: PostgreSQL限流语句标准化后唯一标识
        :type query_id: str
        """
        
        

        self._item_id = None
        self._type = None
        self._key_str = None
        self._max_connection = None
        self._max_waiting = None
        self._cur_connection = None
        self._cur_reject = None
        self._total_reject = None
        self._create_at = None
        self._query_id = None
        self.discriminator = None

        if item_id is not None:
            self.item_id = item_id
        if type is not None:
            self.type = type
        if key_str is not None:
            self.key_str = key_str
        if max_connection is not None:
            self.max_connection = max_connection
        if max_waiting is not None:
            self.max_waiting = max_waiting
        if cur_connection is not None:
            self.cur_connection = cur_connection
        if cur_reject is not None:
            self.cur_reject = cur_reject
        if total_reject is not None:
            self.total_reject = total_reject
        if create_at is not None:
            self.create_at = create_at
        if query_id is not None:
            self.query_id = query_id

    @property
    def item_id(self):
        r"""Gets the item_id of this SqlLimitingRecordInfo.

        SQL限流规则ID

        :return: The item_id of this SqlLimitingRecordInfo.
        :rtype: str
        """
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        r"""Sets the item_id of this SqlLimitingRecordInfo.

        SQL限流规则ID

        :param item_id: The item_id of this SqlLimitingRecordInfo.
        :type item_id: str
        """
        self._item_id = item_id

    @property
    def type(self):
        r"""Gets the type of this SqlLimitingRecordInfo.

        SQL类型

        :return: The type of this SqlLimitingRecordInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this SqlLimitingRecordInfo.

        SQL类型

        :param type: The type of this SqlLimitingRecordInfo.
        :type type: str
        """
        self._type = type

    @property
    def key_str(self):
        r"""Gets the key_str of this SqlLimitingRecordInfo.

        限流规则

        :return: The key_str of this SqlLimitingRecordInfo.
        :rtype: str
        """
        return self._key_str

    @key_str.setter
    def key_str(self, key_str):
        r"""Sets the key_str of this SqlLimitingRecordInfo.

        限流规则

        :param key_str: The key_str of this SqlLimitingRecordInfo.
        :type key_str: str
        """
        self._key_str = key_str

    @property
    def max_connection(self):
        r"""Gets the max_connection of this SqlLimitingRecordInfo.

        最大并发数

        :return: The max_connection of this SqlLimitingRecordInfo.
        :rtype: str
        """
        return self._max_connection

    @max_connection.setter
    def max_connection(self, max_connection):
        r"""Sets the max_connection of this SqlLimitingRecordInfo.

        最大并发数

        :param max_connection: The max_connection of this SqlLimitingRecordInfo.
        :type max_connection: str
        """
        self._max_connection = max_connection

    @property
    def max_waiting(self):
        r"""Gets the max_waiting of this SqlLimitingRecordInfo.

        最大等待时间

        :return: The max_waiting of this SqlLimitingRecordInfo.
        :rtype: str
        """
        return self._max_waiting

    @max_waiting.setter
    def max_waiting(self, max_waiting):
        r"""Sets the max_waiting of this SqlLimitingRecordInfo.

        最大等待时间

        :param max_waiting: The max_waiting of this SqlLimitingRecordInfo.
        :type max_waiting: str
        """
        self._max_waiting = max_waiting

    @property
    def cur_connection(self):
        r"""Gets the cur_connection of this SqlLimitingRecordInfo.

        当前并发数

        :return: The cur_connection of this SqlLimitingRecordInfo.
        :rtype: int
        """
        return self._cur_connection

    @cur_connection.setter
    def cur_connection(self, cur_connection):
        r"""Sets the cur_connection of this SqlLimitingRecordInfo.

        当前并发数

        :param cur_connection: The cur_connection of this SqlLimitingRecordInfo.
        :type cur_connection: int
        """
        self._cur_connection = cur_connection

    @property
    def cur_reject(self):
        r"""Gets the cur_reject of this SqlLimitingRecordInfo.

        当前拦截数

        :return: The cur_reject of this SqlLimitingRecordInfo.
        :rtype: int
        """
        return self._cur_reject

    @cur_reject.setter
    def cur_reject(self, cur_reject):
        r"""Sets the cur_reject of this SqlLimitingRecordInfo.

        当前拦截数

        :param cur_reject: The cur_reject of this SqlLimitingRecordInfo.
        :type cur_reject: int
        """
        self._cur_reject = cur_reject

    @property
    def total_reject(self):
        r"""Gets the total_reject of this SqlLimitingRecordInfo.

        总拦截数

        :return: The total_reject of this SqlLimitingRecordInfo.
        :rtype: int
        """
        return self._total_reject

    @total_reject.setter
    def total_reject(self, total_reject):
        r"""Sets the total_reject of this SqlLimitingRecordInfo.

        总拦截数

        :param total_reject: The total_reject of this SqlLimitingRecordInfo.
        :type total_reject: int
        """
        self._total_reject = total_reject

    @property
    def create_at(self):
        r"""Gets the create_at of this SqlLimitingRecordInfo.

        创建时间

        :return: The create_at of this SqlLimitingRecordInfo.
        :rtype: str
        """
        return self._create_at

    @create_at.setter
    def create_at(self, create_at):
        r"""Sets the create_at of this SqlLimitingRecordInfo.

        创建时间

        :param create_at: The create_at of this SqlLimitingRecordInfo.
        :type create_at: str
        """
        self._create_at = create_at

    @property
    def query_id(self):
        r"""Gets the query_id of this SqlLimitingRecordInfo.

        PostgreSQL限流语句标准化后唯一标识

        :return: The query_id of this SqlLimitingRecordInfo.
        :rtype: str
        """
        return self._query_id

    @query_id.setter
    def query_id(self, query_id):
        r"""Sets the query_id of this SqlLimitingRecordInfo.

        PostgreSQL限流语句标准化后唯一标识

        :param query_id: The query_id of this SqlLimitingRecordInfo.
        :type query_id: str
        """
        self._query_id = query_id

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SqlLimitingRecordInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
