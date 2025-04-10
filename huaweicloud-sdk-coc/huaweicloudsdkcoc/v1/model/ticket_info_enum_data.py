# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TicketInfoEnumData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'filed_key': 'str',
        'enum_key': 'str',
        'name_zh': 'str',
        'name_en': 'str'
    }

    attribute_map = {
        'filed_key': 'filed_key',
        'enum_key': 'enum_key',
        'name_zh': 'name_zh',
        'name_en': 'name_en'
    }

    def __init__(self, filed_key=None, enum_key=None, name_zh=None, name_en=None):
        r"""TicketInfoEnumData

        The model defined in huaweicloud sdk

        :param filed_key: 字段KEY 标识哪个字段
        :type filed_key: str
        :param enum_key: 枚举KEY
        :type enum_key: str
        :param name_zh: 中文名称
        :type name_zh: str
        :param name_en: 英文名称
        :type name_en: str
        """
        
        

        self._filed_key = None
        self._enum_key = None
        self._name_zh = None
        self._name_en = None
        self.discriminator = None

        self.filed_key = filed_key
        self.enum_key = enum_key
        self.name_zh = name_zh
        self.name_en = name_en

    @property
    def filed_key(self):
        r"""Gets the filed_key of this TicketInfoEnumData.

        字段KEY 标识哪个字段

        :return: The filed_key of this TicketInfoEnumData.
        :rtype: str
        """
        return self._filed_key

    @filed_key.setter
    def filed_key(self, filed_key):
        r"""Sets the filed_key of this TicketInfoEnumData.

        字段KEY 标识哪个字段

        :param filed_key: The filed_key of this TicketInfoEnumData.
        :type filed_key: str
        """
        self._filed_key = filed_key

    @property
    def enum_key(self):
        r"""Gets the enum_key of this TicketInfoEnumData.

        枚举KEY

        :return: The enum_key of this TicketInfoEnumData.
        :rtype: str
        """
        return self._enum_key

    @enum_key.setter
    def enum_key(self, enum_key):
        r"""Sets the enum_key of this TicketInfoEnumData.

        枚举KEY

        :param enum_key: The enum_key of this TicketInfoEnumData.
        :type enum_key: str
        """
        self._enum_key = enum_key

    @property
    def name_zh(self):
        r"""Gets the name_zh of this TicketInfoEnumData.

        中文名称

        :return: The name_zh of this TicketInfoEnumData.
        :rtype: str
        """
        return self._name_zh

    @name_zh.setter
    def name_zh(self, name_zh):
        r"""Sets the name_zh of this TicketInfoEnumData.

        中文名称

        :param name_zh: The name_zh of this TicketInfoEnumData.
        :type name_zh: str
        """
        self._name_zh = name_zh

    @property
    def name_en(self):
        r"""Gets the name_en of this TicketInfoEnumData.

        英文名称

        :return: The name_en of this TicketInfoEnumData.
        :rtype: str
        """
        return self._name_en

    @name_en.setter
    def name_en(self, name_en):
        r"""Sets the name_en of this TicketInfoEnumData.

        英文名称

        :param name_en: The name_en of this TicketInfoEnumData.
        :type name_en: str
        """
        self._name_en = name_en

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
        if not isinstance(other, TicketInfoEnumData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
