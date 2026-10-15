# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListBigKeysRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'stat_type': 'str',
        'start_at': 'int',
        'end_at': 'int',
        'key_types': 'list[str]',
        'key_name': 'str',
        'db_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'sort_field': 'str',
        'asc': 'bool',
        'x_language': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'stat_type': 'stat_type',
        'start_at': 'start_at',
        'end_at': 'end_at',
        'key_types': 'key_types',
        'key_name': 'key_name',
        'db_id': 'db_id',
        'offset': 'offset',
        'limit': 'limit',
        'sort_field': 'sort_field',
        'asc': 'asc',
        'x_language': 'X-Language'
    }

    def __init__(self, instance_id=None, stat_type=None, start_at=None, end_at=None, key_types=None, key_name=None, db_id=None, offset=None, limit=None, sort_field=None, asc=None, x_language=None):
        r"""ListBigKeysRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param stat_type: 统计维度。size-按长度，storage-按存储占用
        :type stat_type: str
        :param start_at: 开始时间（毫秒时间戳）
        :type start_at: int
        :param end_at: 结束时间（毫秒时间戳）
        :type end_at: int
        :param key_types: key类型过滤（多选）。取值：string、hash、list、zset、set、stream、exhash
        :type key_types: list[str]
        :param key_name: key名称过滤（模糊匹配）
        :type key_name: str
        :param db_id: 数据库ID过滤
        :type db_id: str
        :param offset: 偏移量，默认0
        :type offset: int
        :param limit: 每页条数，默认20，最大1000
        :type limit: int
        :param sort_field: 排序字段，默认size
        :type sort_field: str
        :param asc: 是否升序，默认false（降序）
        :type asc: bool
        :param x_language: 请求语言类型。en-us：英文。zh-cn：中文。
        :type x_language: str
        """
        
        

        self._instance_id = None
        self._stat_type = None
        self._start_at = None
        self._end_at = None
        self._key_types = None
        self._key_name = None
        self._db_id = None
        self._offset = None
        self._limit = None
        self._sort_field = None
        self._asc = None
        self._x_language = None
        self.discriminator = None

        self.instance_id = instance_id
        self.stat_type = stat_type
        self.start_at = start_at
        self.end_at = end_at
        if key_types is not None:
            self.key_types = key_types
        if key_name is not None:
            self.key_name = key_name
        if db_id is not None:
            self.db_id = db_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if sort_field is not None:
            self.sort_field = sort_field
        if asc is not None:
            self.asc = asc
        if x_language is not None:
            self.x_language = x_language

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListBigKeysRequest.

        实例ID

        :return: The instance_id of this ListBigKeysRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListBigKeysRequest.

        实例ID

        :param instance_id: The instance_id of this ListBigKeysRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def stat_type(self):
        r"""Gets the stat_type of this ListBigKeysRequest.

        统计维度。size-按长度，storage-按存储占用

        :return: The stat_type of this ListBigKeysRequest.
        :rtype: str
        """
        return self._stat_type

    @stat_type.setter
    def stat_type(self, stat_type):
        r"""Sets the stat_type of this ListBigKeysRequest.

        统计维度。size-按长度，storage-按存储占用

        :param stat_type: The stat_type of this ListBigKeysRequest.
        :type stat_type: str
        """
        self._stat_type = stat_type

    @property
    def start_at(self):
        r"""Gets the start_at of this ListBigKeysRequest.

        开始时间（毫秒时间戳）

        :return: The start_at of this ListBigKeysRequest.
        :rtype: int
        """
        return self._start_at

    @start_at.setter
    def start_at(self, start_at):
        r"""Sets the start_at of this ListBigKeysRequest.

        开始时间（毫秒时间戳）

        :param start_at: The start_at of this ListBigKeysRequest.
        :type start_at: int
        """
        self._start_at = start_at

    @property
    def end_at(self):
        r"""Gets the end_at of this ListBigKeysRequest.

        结束时间（毫秒时间戳）

        :return: The end_at of this ListBigKeysRequest.
        :rtype: int
        """
        return self._end_at

    @end_at.setter
    def end_at(self, end_at):
        r"""Sets the end_at of this ListBigKeysRequest.

        结束时间（毫秒时间戳）

        :param end_at: The end_at of this ListBigKeysRequest.
        :type end_at: int
        """
        self._end_at = end_at

    @property
    def key_types(self):
        r"""Gets the key_types of this ListBigKeysRequest.

        key类型过滤（多选）。取值：string、hash、list、zset、set、stream、exhash

        :return: The key_types of this ListBigKeysRequest.
        :rtype: list[str]
        """
        return self._key_types

    @key_types.setter
    def key_types(self, key_types):
        r"""Sets the key_types of this ListBigKeysRequest.

        key类型过滤（多选）。取值：string、hash、list、zset、set、stream、exhash

        :param key_types: The key_types of this ListBigKeysRequest.
        :type key_types: list[str]
        """
        self._key_types = key_types

    @property
    def key_name(self):
        r"""Gets the key_name of this ListBigKeysRequest.

        key名称过滤（模糊匹配）

        :return: The key_name of this ListBigKeysRequest.
        :rtype: str
        """
        return self._key_name

    @key_name.setter
    def key_name(self, key_name):
        r"""Sets the key_name of this ListBigKeysRequest.

        key名称过滤（模糊匹配）

        :param key_name: The key_name of this ListBigKeysRequest.
        :type key_name: str
        """
        self._key_name = key_name

    @property
    def db_id(self):
        r"""Gets the db_id of this ListBigKeysRequest.

        数据库ID过滤

        :return: The db_id of this ListBigKeysRequest.
        :rtype: str
        """
        return self._db_id

    @db_id.setter
    def db_id(self, db_id):
        r"""Sets the db_id of this ListBigKeysRequest.

        数据库ID过滤

        :param db_id: The db_id of this ListBigKeysRequest.
        :type db_id: str
        """
        self._db_id = db_id

    @property
    def offset(self):
        r"""Gets the offset of this ListBigKeysRequest.

        偏移量，默认0

        :return: The offset of this ListBigKeysRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListBigKeysRequest.

        偏移量，默认0

        :param offset: The offset of this ListBigKeysRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListBigKeysRequest.

        每页条数，默认20，最大1000

        :return: The limit of this ListBigKeysRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListBigKeysRequest.

        每页条数，默认20，最大1000

        :param limit: The limit of this ListBigKeysRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def sort_field(self):
        r"""Gets the sort_field of this ListBigKeysRequest.

        排序字段，默认size

        :return: The sort_field of this ListBigKeysRequest.
        :rtype: str
        """
        return self._sort_field

    @sort_field.setter
    def sort_field(self, sort_field):
        r"""Sets the sort_field of this ListBigKeysRequest.

        排序字段，默认size

        :param sort_field: The sort_field of this ListBigKeysRequest.
        :type sort_field: str
        """
        self._sort_field = sort_field

    @property
    def asc(self):
        r"""Gets the asc of this ListBigKeysRequest.

        是否升序，默认false（降序）

        :return: The asc of this ListBigKeysRequest.
        :rtype: bool
        """
        return self._asc

    @asc.setter
    def asc(self, asc):
        r"""Sets the asc of this ListBigKeysRequest.

        是否升序，默认false（降序）

        :param asc: The asc of this ListBigKeysRequest.
        :type asc: bool
        """
        self._asc = asc

    @property
    def x_language(self):
        r"""Gets the x_language of this ListBigKeysRequest.

        请求语言类型。en-us：英文。zh-cn：中文。

        :return: The x_language of this ListBigKeysRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ListBigKeysRequest.

        请求语言类型。en-us：英文。zh-cn：中文。

        :param x_language: The x_language of this ListBigKeysRequest.
        :type x_language: str
        """
        self._x_language = x_language

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
        if not isinstance(other, ListBigKeysRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
