# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchQueryField:

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
        'alias': 'str'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'alias': 'alias'
    }

    def __init__(self, name=None, type=None, alias=None):
        r"""SearchQueryField

        The model defined in huaweicloud sdk

        :param name: 字段名
        :type name: str
        :param type: **参数解释**: 数据类型 - boolean 布尔型 - byte 字节型 - short 短整型 - integer 整型 - long 长整型 - float 单精度浮点型 - half_float 半精度浮点型 - scaled_float 缩放浮点型 - double 双精度浮点型 - keyword 关键字型 - text 文本型 - date 日期型 - ip IP地址型 - binary 二进制型 - object 对象型 - nested 嵌套型  **约束限制** 不涉及 **取值范围**: - boolean - byte - short - integer - long - float - half_float - scaled_float - double - keyword - text - date - ip - binary - object - nested  **默认值** 不涉及       
        :type type: str
        :param alias: 字段别名
        :type alias: str
        """
        
        

        self._name = None
        self._type = None
        self._alias = None
        self.discriminator = None

        self.name = name
        self.type = type
        if alias is not None:
            self.alias = alias

    @property
    def name(self):
        r"""Gets the name of this SearchQueryField.

        字段名

        :return: The name of this SearchQueryField.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this SearchQueryField.

        字段名

        :param name: The name of this SearchQueryField.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this SearchQueryField.

        **参数解释**: 数据类型 - boolean 布尔型 - byte 字节型 - short 短整型 - integer 整型 - long 长整型 - float 单精度浮点型 - half_float 半精度浮点型 - scaled_float 缩放浮点型 - double 双精度浮点型 - keyword 关键字型 - text 文本型 - date 日期型 - ip IP地址型 - binary 二进制型 - object 对象型 - nested 嵌套型  **约束限制** 不涉及 **取值范围**: - boolean - byte - short - integer - long - float - half_float - scaled_float - double - keyword - text - date - ip - binary - object - nested  **默认值** 不涉及       

        :return: The type of this SearchQueryField.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this SearchQueryField.

        **参数解释**: 数据类型 - boolean 布尔型 - byte 字节型 - short 短整型 - integer 整型 - long 长整型 - float 单精度浮点型 - half_float 半精度浮点型 - scaled_float 缩放浮点型 - double 双精度浮点型 - keyword 关键字型 - text 文本型 - date 日期型 - ip IP地址型 - binary 二进制型 - object 对象型 - nested 嵌套型  **约束限制** 不涉及 **取值范围**: - boolean - byte - short - integer - long - float - half_float - scaled_float - double - keyword - text - date - ip - binary - object - nested  **默认值** 不涉及       

        :param type: The type of this SearchQueryField.
        :type type: str
        """
        self._type = type

    @property
    def alias(self):
        r"""Gets the alias of this SearchQueryField.

        字段别名

        :return: The alias of this SearchQueryField.
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        r"""Sets the alias of this SearchQueryField.

        字段别名

        :param alias: The alias of this SearchQueryField.
        :type alias: str
        """
        self._alias = alias

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
        if not isinstance(other, SearchQueryField):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
