# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LargestKey:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'key': 'str',
        'type': 'str',
        'bytes': 'int',
        'num_of_elem': 'int'
    }

    attribute_map = {
        'key': 'key',
        'type': 'type',
        'bytes': 'bytes',
        'num_of_elem': 'num_of_elem'
    }

    def __init__(self, key=None, type=None, bytes=None, num_of_elem=None):
        r"""LargestKey

        The model defined in huaweicloud sdk

        :param key: **参数解释**： Key名称。 **取值范围**： 不涉及。 
        :type key: str
        :param type: **参数解释**： Key的数据类型。 **取值范围**： string list set zset hash 
        :type type: str
        :param bytes: **参数解释**： Key的大小，单位：Bytes。 **取值范围**： 不涉及。 
        :type bytes: int
        :param num_of_elem: **参数解释**： 元素数量或元素大小（String类型为元素大小，单位：Bytes。非String类型为元素数量）。 **取值范围**： 不涉及。 
        :type num_of_elem: int
        """
        
        

        self._key = None
        self._type = None
        self._bytes = None
        self._num_of_elem = None
        self.discriminator = None

        if key is not None:
            self.key = key
        if type is not None:
            self.type = type
        if bytes is not None:
            self.bytes = bytes
        if num_of_elem is not None:
            self.num_of_elem = num_of_elem

    @property
    def key(self):
        r"""Gets the key of this LargestKey.

        **参数解释**： Key名称。 **取值范围**： 不涉及。 

        :return: The key of this LargestKey.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        r"""Sets the key of this LargestKey.

        **参数解释**： Key名称。 **取值范围**： 不涉及。 

        :param key: The key of this LargestKey.
        :type key: str
        """
        self._key = key

    @property
    def type(self):
        r"""Gets the type of this LargestKey.

        **参数解释**： Key的数据类型。 **取值范围**： string list set zset hash 

        :return: The type of this LargestKey.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this LargestKey.

        **参数解释**： Key的数据类型。 **取值范围**： string list set zset hash 

        :param type: The type of this LargestKey.
        :type type: str
        """
        self._type = type

    @property
    def bytes(self):
        r"""Gets the bytes of this LargestKey.

        **参数解释**： Key的大小，单位：Bytes。 **取值范围**： 不涉及。 

        :return: The bytes of this LargestKey.
        :rtype: int
        """
        return self._bytes

    @bytes.setter
    def bytes(self, bytes):
        r"""Sets the bytes of this LargestKey.

        **参数解释**： Key的大小，单位：Bytes。 **取值范围**： 不涉及。 

        :param bytes: The bytes of this LargestKey.
        :type bytes: int
        """
        self._bytes = bytes

    @property
    def num_of_elem(self):
        r"""Gets the num_of_elem of this LargestKey.

        **参数解释**： 元素数量或元素大小（String类型为元素大小，单位：Bytes。非String类型为元素数量）。 **取值范围**： 不涉及。 

        :return: The num_of_elem of this LargestKey.
        :rtype: int
        """
        return self._num_of_elem

    @num_of_elem.setter
    def num_of_elem(self, num_of_elem):
        r"""Sets the num_of_elem of this LargestKey.

        **参数解释**： 元素数量或元素大小（String类型为元素大小，单位：Bytes。非String类型为元素数量）。 **取值范围**： 不涉及。 

        :param num_of_elem: The num_of_elem of this LargestKey.
        :type num_of_elem: int
        """
        self._num_of_elem = num_of_elem

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
        if not isinstance(other, LargestKey):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
