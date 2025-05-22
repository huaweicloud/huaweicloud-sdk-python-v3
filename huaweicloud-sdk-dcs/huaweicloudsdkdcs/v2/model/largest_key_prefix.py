# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LargestKeyPrefix:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'key_prefix': 'str',
        'type': 'str',
        'bytes': 'int',
        'num': 'int'
    }

    attribute_map = {
        'key_prefix': 'key_prefix',
        'type': 'type',
        'bytes': 'bytes',
        'num': 'num'
    }

    def __init__(self, key_prefix=None, type=None, bytes=None, num=None):
        r"""LargestKeyPrefix

        The model defined in huaweicloud sdk

        :param key_prefix: **参数解释**： 前缀名称。 **取值范围**： 不涉及。 
        :type key_prefix: str
        :param type: **参数解释**： Key的数据类型。 **取值范围**： string list set zset hash 
        :type type: str
        :param bytes: **参数解释**： Key的大小，单位：Bytes。 **取值范围**： 不涉及。 
        :type bytes: int
        :param num: **参数解释**： 相同前缀key的数量。 **取值范围**： 不涉及。 
        :type num: int
        """
        
        

        self._key_prefix = None
        self._type = None
        self._bytes = None
        self._num = None
        self.discriminator = None

        if key_prefix is not None:
            self.key_prefix = key_prefix
        if type is not None:
            self.type = type
        if bytes is not None:
            self.bytes = bytes
        if num is not None:
            self.num = num

    @property
    def key_prefix(self):
        r"""Gets the key_prefix of this LargestKeyPrefix.

        **参数解释**： 前缀名称。 **取值范围**： 不涉及。 

        :return: The key_prefix of this LargestKeyPrefix.
        :rtype: str
        """
        return self._key_prefix

    @key_prefix.setter
    def key_prefix(self, key_prefix):
        r"""Sets the key_prefix of this LargestKeyPrefix.

        **参数解释**： 前缀名称。 **取值范围**： 不涉及。 

        :param key_prefix: The key_prefix of this LargestKeyPrefix.
        :type key_prefix: str
        """
        self._key_prefix = key_prefix

    @property
    def type(self):
        r"""Gets the type of this LargestKeyPrefix.

        **参数解释**： Key的数据类型。 **取值范围**： string list set zset hash 

        :return: The type of this LargestKeyPrefix.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this LargestKeyPrefix.

        **参数解释**： Key的数据类型。 **取值范围**： string list set zset hash 

        :param type: The type of this LargestKeyPrefix.
        :type type: str
        """
        self._type = type

    @property
    def bytes(self):
        r"""Gets the bytes of this LargestKeyPrefix.

        **参数解释**： Key的大小，单位：Bytes。 **取值范围**： 不涉及。 

        :return: The bytes of this LargestKeyPrefix.
        :rtype: int
        """
        return self._bytes

    @bytes.setter
    def bytes(self, bytes):
        r"""Sets the bytes of this LargestKeyPrefix.

        **参数解释**： Key的大小，单位：Bytes。 **取值范围**： 不涉及。 

        :param bytes: The bytes of this LargestKeyPrefix.
        :type bytes: int
        """
        self._bytes = bytes

    @property
    def num(self):
        r"""Gets the num of this LargestKeyPrefix.

        **参数解释**： 相同前缀key的数量。 **取值范围**： 不涉及。 

        :return: The num of this LargestKeyPrefix.
        :rtype: int
        """
        return self._num

    @num.setter
    def num(self, num):
        r"""Sets the num of this LargestKeyPrefix.

        **参数解释**： 相同前缀key的数量。 **取值范围**： 不涉及。 

        :param num: The num of this LargestKeyPrefix.
        :type num: int
        """
        self._num = num

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
        if not isinstance(other, LargestKeyPrefix):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
