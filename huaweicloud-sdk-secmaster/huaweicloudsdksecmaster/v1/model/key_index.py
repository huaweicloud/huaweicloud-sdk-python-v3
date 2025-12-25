# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class KeyIndex:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_chinese_exist': 'bool',
        'properties': 'dict(str, KeyIndex)',
        'type': 'str'
    }

    attribute_map = {
        'is_chinese_exist': 'is_chinese_exist',
        'properties': 'properties',
        'type': 'type'
    }

    def __init__(self, is_chinese_exist=None, properties=None, type=None):
        r"""KeyIndex

        The model defined in huaweicloud sdk

        :param is_chinese_exist: 是否包含中文
        :type is_chinese_exist: bool
        :param properties: 嵌套结构
        :type properties: dict(str, KeyIndex)
        :param type: **参数解释**: 字段类型 - text 全文索引字段 - keyword 关键字类型，适用于精确匹配 - long 长整型 - integer 整型 - double 双精度浮点数 - float 单精度浮点数 - date 日期类型  **约束限制** 不涉及 **取值范围**: - text - keyword - long - integer - double - float - date  **默认值** 不涉及
        :type type: str
        """
        
        

        self._is_chinese_exist = None
        self._properties = None
        self._type = None
        self.discriminator = None

        if is_chinese_exist is not None:
            self.is_chinese_exist = is_chinese_exist
        if properties is not None:
            self.properties = properties
        if type is not None:
            self.type = type

    @property
    def is_chinese_exist(self):
        r"""Gets the is_chinese_exist of this KeyIndex.

        是否包含中文

        :return: The is_chinese_exist of this KeyIndex.
        :rtype: bool
        """
        return self._is_chinese_exist

    @is_chinese_exist.setter
    def is_chinese_exist(self, is_chinese_exist):
        r"""Sets the is_chinese_exist of this KeyIndex.

        是否包含中文

        :param is_chinese_exist: The is_chinese_exist of this KeyIndex.
        :type is_chinese_exist: bool
        """
        self._is_chinese_exist = is_chinese_exist

    @property
    def properties(self):
        r"""Gets the properties of this KeyIndex.

        嵌套结构

        :return: The properties of this KeyIndex.
        :rtype: dict(str, KeyIndex)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        r"""Sets the properties of this KeyIndex.

        嵌套结构

        :param properties: The properties of this KeyIndex.
        :type properties: dict(str, KeyIndex)
        """
        self._properties = properties

    @property
    def type(self):
        r"""Gets the type of this KeyIndex.

        **参数解释**: 字段类型 - text 全文索引字段 - keyword 关键字类型，适用于精确匹配 - long 长整型 - integer 整型 - double 双精度浮点数 - float 单精度浮点数 - date 日期类型  **约束限制** 不涉及 **取值范围**: - text - keyword - long - integer - double - float - date  **默认值** 不涉及

        :return: The type of this KeyIndex.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this KeyIndex.

        **参数解释**: 字段类型 - text 全文索引字段 - keyword 关键字类型，适用于精确匹配 - long 长整型 - integer 整型 - double 双精度浮点数 - float 单精度浮点数 - date 日期类型  **约束限制** 不涉及 **取值范围**: - text - keyword - long - integer - double - float - date  **默认值** 不涉及

        :param type: The type of this KeyIndex.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, KeyIndex):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
