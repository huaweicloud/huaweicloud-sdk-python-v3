# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class KeyTypeByte:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'bytes': 'int'
    }

    attribute_map = {
        'type': 'type',
        'bytes': 'bytes'
    }

    def __init__(self, type=None, bytes=None):
        r"""KeyTypeByte

        The model defined in huaweicloud sdk

        :param type: **参数解释**： Key的数据类型。 **取值范围**： string list set zset hash 
        :type type: str
        :param bytes: **参数解释**： 每种数据类型Key的总大小，单位：Bytes。 **取值范围**： 不涉及。 
        :type bytes: int
        """
        
        

        self._type = None
        self._bytes = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if bytes is not None:
            self.bytes = bytes

    @property
    def type(self):
        r"""Gets the type of this KeyTypeByte.

        **参数解释**： Key的数据类型。 **取值范围**： string list set zset hash 

        :return: The type of this KeyTypeByte.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this KeyTypeByte.

        **参数解释**： Key的数据类型。 **取值范围**： string list set zset hash 

        :param type: The type of this KeyTypeByte.
        :type type: str
        """
        self._type = type

    @property
    def bytes(self):
        r"""Gets the bytes of this KeyTypeByte.

        **参数解释**： 每种数据类型Key的总大小，单位：Bytes。 **取值范围**： 不涉及。 

        :return: The bytes of this KeyTypeByte.
        :rtype: int
        """
        return self._bytes

    @bytes.setter
    def bytes(self, bytes):
        r"""Sets the bytes of this KeyTypeByte.

        **参数解释**： 每种数据类型Key的总大小，单位：Bytes。 **取值范围**： 不涉及。 

        :param bytes: The bytes of this KeyTypeByte.
        :type bytes: int
        """
        self._bytes = bytes

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
        if not isinstance(other, KeyTypeByte):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
