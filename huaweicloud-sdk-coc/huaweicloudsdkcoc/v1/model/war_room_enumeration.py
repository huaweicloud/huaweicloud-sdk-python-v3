# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WarRoomEnumeration:

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
        'name_zh': 'str',
        'name_en': 'str',
        'type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name_zh': 'name_zh',
        'name_en': 'name_en',
        'type': 'type'
    }

    def __init__(self, id=None, name_zh=None, name_en=None, type=None):
        r"""WarRoomEnumeration

        The model defined in huaweicloud sdk

        :param id: 枚举值id
        :type id: str
        :param name_zh: 枚举值中文名
        :type name_zh: str
        :param name_en: 枚举值英文名
        :type name_en: str
        :param type: 枚举类型
        :type type: str
        """
        
        

        self._id = None
        self._name_zh = None
        self._name_en = None
        self._type = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name_zh is not None:
            self.name_zh = name_zh
        if name_en is not None:
            self.name_en = name_en
        if type is not None:
            self.type = type

    @property
    def id(self):
        r"""Gets the id of this WarRoomEnumeration.

        枚举值id

        :return: The id of this WarRoomEnumeration.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this WarRoomEnumeration.

        枚举值id

        :param id: The id of this WarRoomEnumeration.
        :type id: str
        """
        self._id = id

    @property
    def name_zh(self):
        r"""Gets the name_zh of this WarRoomEnumeration.

        枚举值中文名

        :return: The name_zh of this WarRoomEnumeration.
        :rtype: str
        """
        return self._name_zh

    @name_zh.setter
    def name_zh(self, name_zh):
        r"""Sets the name_zh of this WarRoomEnumeration.

        枚举值中文名

        :param name_zh: The name_zh of this WarRoomEnumeration.
        :type name_zh: str
        """
        self._name_zh = name_zh

    @property
    def name_en(self):
        r"""Gets the name_en of this WarRoomEnumeration.

        枚举值英文名

        :return: The name_en of this WarRoomEnumeration.
        :rtype: str
        """
        return self._name_en

    @name_en.setter
    def name_en(self, name_en):
        r"""Sets the name_en of this WarRoomEnumeration.

        枚举值英文名

        :param name_en: The name_en of this WarRoomEnumeration.
        :type name_en: str
        """
        self._name_en = name_en

    @property
    def type(self):
        r"""Gets the type of this WarRoomEnumeration.

        枚举类型

        :return: The type of this WarRoomEnumeration.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this WarRoomEnumeration.

        枚举类型

        :param type: The type of this WarRoomEnumeration.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, WarRoomEnumeration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
