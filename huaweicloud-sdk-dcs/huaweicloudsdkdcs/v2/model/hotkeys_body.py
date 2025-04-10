# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HotkeysBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'type': 'str',
        'shard': 'str',
        'db': 'int',
        'size': 'int',
        'unit': 'str',
        'freq': 'int'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'shard': 'shard',
        'db': 'db',
        'size': 'size',
        'unit': 'unit',
        'freq': 'freq'
    }

    def __init__(self, name=None, type=None, shard=None, db=None, size=None, unit=None, freq=None):
        r"""HotkeysBody

        The model defined in huaweicloud sdk

        :param name: key名称
        :type name: str
        :param type: key类型
        :type type: str
        :param shard: 热key所在的分片，仅在实例类型为集群时支持,格式为ip:port
        :type shard: str
        :param db: 热key所在的db
        :type db: int
        :param size: key的value大小。
        :type size: int
        :param unit: key大小的单位。type为string时，单位是：byte；type为list/set/zset/hash时，单位是：count
        :type unit: str
        :param freq: 表示某个key在一段时间的访问频度，会随着访问的频率而变化。  该值并不是简单的访问频率值，而是一个基于概率的对数计数器结果，最大为255(可表示100万次访问)，超过255后如果继续频繁访问该值并不会继续增大，同时默认如果每过一分钟没有访问，该值会衰减1。 
        :type freq: int
        """
        
        

        self._name = None
        self._type = None
        self._shard = None
        self._db = None
        self._size = None
        self._unit = None
        self._freq = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if shard is not None:
            self.shard = shard
        if db is not None:
            self.db = db
        if size is not None:
            self.size = size
        if unit is not None:
            self.unit = unit
        if freq is not None:
            self.freq = freq

    @property
    def name(self):
        r"""Gets the name of this HotkeysBody.

        key名称

        :return: The name of this HotkeysBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this HotkeysBody.

        key名称

        :param name: The name of this HotkeysBody.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this HotkeysBody.

        key类型

        :return: The type of this HotkeysBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this HotkeysBody.

        key类型

        :param type: The type of this HotkeysBody.
        :type type: str
        """
        self._type = type

    @property
    def shard(self):
        r"""Gets the shard of this HotkeysBody.

        热key所在的分片，仅在实例类型为集群时支持,格式为ip:port

        :return: The shard of this HotkeysBody.
        :rtype: str
        """
        return self._shard

    @shard.setter
    def shard(self, shard):
        r"""Sets the shard of this HotkeysBody.

        热key所在的分片，仅在实例类型为集群时支持,格式为ip:port

        :param shard: The shard of this HotkeysBody.
        :type shard: str
        """
        self._shard = shard

    @property
    def db(self):
        r"""Gets the db of this HotkeysBody.

        热key所在的db

        :return: The db of this HotkeysBody.
        :rtype: int
        """
        return self._db

    @db.setter
    def db(self, db):
        r"""Sets the db of this HotkeysBody.

        热key所在的db

        :param db: The db of this HotkeysBody.
        :type db: int
        """
        self._db = db

    @property
    def size(self):
        r"""Gets the size of this HotkeysBody.

        key的value大小。

        :return: The size of this HotkeysBody.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this HotkeysBody.

        key的value大小。

        :param size: The size of this HotkeysBody.
        :type size: int
        """
        self._size = size

    @property
    def unit(self):
        r"""Gets the unit of this HotkeysBody.

        key大小的单位。type为string时，单位是：byte；type为list/set/zset/hash时，单位是：count

        :return: The unit of this HotkeysBody.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        r"""Sets the unit of this HotkeysBody.

        key大小的单位。type为string时，单位是：byte；type为list/set/zset/hash时，单位是：count

        :param unit: The unit of this HotkeysBody.
        :type unit: str
        """
        self._unit = unit

    @property
    def freq(self):
        r"""Gets the freq of this HotkeysBody.

        表示某个key在一段时间的访问频度，会随着访问的频率而变化。  该值并不是简单的访问频率值，而是一个基于概率的对数计数器结果，最大为255(可表示100万次访问)，超过255后如果继续频繁访问该值并不会继续增大，同时默认如果每过一分钟没有访问，该值会衰减1。 

        :return: The freq of this HotkeysBody.
        :rtype: int
        """
        return self._freq

    @freq.setter
    def freq(self, freq):
        r"""Sets the freq of this HotkeysBody.

        表示某个key在一段时间的访问频度，会随着访问的频率而变化。  该值并不是简单的访问频率值，而是一个基于概率的对数计数器结果，最大为255(可表示100万次访问)，超过255后如果继续频繁访问该值并不会继续增大，同时默认如果每过一分钟没有访问，该值会衰减1。 

        :param freq: The freq of this HotkeysBody.
        :type freq: int
        """
        self._freq = freq

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
        if not isinstance(other, HotkeysBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
