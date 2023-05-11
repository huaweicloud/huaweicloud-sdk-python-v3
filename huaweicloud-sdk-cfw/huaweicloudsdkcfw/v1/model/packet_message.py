# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PacketMessage:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'hex_index': 'str',
        'hexs': 'list[str]',
        'utf8_string': 'str'
    }

    attribute_map = {
        'hex_index': 'hex_index',
        'hexs': 'hexs',
        'utf8_string': 'utf8_String'
    }

    def __init__(self, hex_index=None, hexs=None, utf8_string=None):
        """PacketMessage

        The model defined in huaweicloud sdk

        :param hex_index: 16进制index
        :type hex_index: str
        :param hexs: 16进制数列
        :type hexs: list[str]
        :param utf8_string: utf_8字符串
        :type utf8_string: str
        """
        
        

        self._hex_index = None
        self._hexs = None
        self._utf8_string = None
        self.discriminator = None

        if hex_index is not None:
            self.hex_index = hex_index
        if hexs is not None:
            self.hexs = hexs
        if utf8_string is not None:
            self.utf8_string = utf8_string

    @property
    def hex_index(self):
        """Gets the hex_index of this PacketMessage.

        16进制index

        :return: The hex_index of this PacketMessage.
        :rtype: str
        """
        return self._hex_index

    @hex_index.setter
    def hex_index(self, hex_index):
        """Sets the hex_index of this PacketMessage.

        16进制index

        :param hex_index: The hex_index of this PacketMessage.
        :type hex_index: str
        """
        self._hex_index = hex_index

    @property
    def hexs(self):
        """Gets the hexs of this PacketMessage.

        16进制数列

        :return: The hexs of this PacketMessage.
        :rtype: list[str]
        """
        return self._hexs

    @hexs.setter
    def hexs(self, hexs):
        """Sets the hexs of this PacketMessage.

        16进制数列

        :param hexs: The hexs of this PacketMessage.
        :type hexs: list[str]
        """
        self._hexs = hexs

    @property
    def utf8_string(self):
        """Gets the utf8_string of this PacketMessage.

        utf_8字符串

        :return: The utf8_string of this PacketMessage.
        :rtype: str
        """
        return self._utf8_string

    @utf8_string.setter
    def utf8_string(self, utf8_string):
        """Sets the utf8_string of this PacketMessage.

        utf_8字符串

        :param utf8_string: The utf8_string of this PacketMessage.
        :type utf8_string: str
        """
        self._utf8_string = utf8_string

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
        if not isinstance(other, PacketMessage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
