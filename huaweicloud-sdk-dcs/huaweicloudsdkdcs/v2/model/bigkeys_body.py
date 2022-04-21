# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BigkeysBody:

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
        'unit': 'str'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'shard': 'shard',
        'db': 'db',
        'size': 'size',
        'unit': 'unit'
    }

    def __init__(self, name=None, type=None, shard=None, db=None, size=None, unit=None):
        """BigkeysBody

        The model defined in huaweicloud sdk

        :param name: key名称
        :type name: str
        :param type: key类型
        :type type: str
        :param shard: 大key所在的分片，仅在实例类型为集群时支持,格式为ip:port
        :type shard: str
        :param db: 大key所在的db
        :type db: int
        :param size: key的value大小。
        :type size: int
        :param unit: key大小的单位。type为string时，单位是：byte；type为list/set/zset/hash时，单位是：count
        :type unit: str
        """
        
        

        self._name = None
        self._type = None
        self._shard = None
        self._db = None
        self._size = None
        self._unit = None
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

    @property
    def name(self):
        """Gets the name of this BigkeysBody.

        key名称

        :return: The name of this BigkeysBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BigkeysBody.

        key名称

        :param name: The name of this BigkeysBody.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        """Gets the type of this BigkeysBody.

        key类型

        :return: The type of this BigkeysBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BigkeysBody.

        key类型

        :param type: The type of this BigkeysBody.
        :type type: str
        """
        self._type = type

    @property
    def shard(self):
        """Gets the shard of this BigkeysBody.

        大key所在的分片，仅在实例类型为集群时支持,格式为ip:port

        :return: The shard of this BigkeysBody.
        :rtype: str
        """
        return self._shard

    @shard.setter
    def shard(self, shard):
        """Sets the shard of this BigkeysBody.

        大key所在的分片，仅在实例类型为集群时支持,格式为ip:port

        :param shard: The shard of this BigkeysBody.
        :type shard: str
        """
        self._shard = shard

    @property
    def db(self):
        """Gets the db of this BigkeysBody.

        大key所在的db

        :return: The db of this BigkeysBody.
        :rtype: int
        """
        return self._db

    @db.setter
    def db(self, db):
        """Sets the db of this BigkeysBody.

        大key所在的db

        :param db: The db of this BigkeysBody.
        :type db: int
        """
        self._db = db

    @property
    def size(self):
        """Gets the size of this BigkeysBody.

        key的value大小。

        :return: The size of this BigkeysBody.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this BigkeysBody.

        key的value大小。

        :param size: The size of this BigkeysBody.
        :type size: int
        """
        self._size = size

    @property
    def unit(self):
        """Gets the unit of this BigkeysBody.

        key大小的单位。type为string时，单位是：byte；type为list/set/zset/hash时，单位是：count

        :return: The unit of this BigkeysBody.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this BigkeysBody.

        key大小的单位。type为string时，单位是：byte；type为list/set/zset/hash时，单位是：count

        :param unit: The unit of this BigkeysBody.
        :type unit: str
        """
        self._unit = unit

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
        if not isinstance(other, BigkeysBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
