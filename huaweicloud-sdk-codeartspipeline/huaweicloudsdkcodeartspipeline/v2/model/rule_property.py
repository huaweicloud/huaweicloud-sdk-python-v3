# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RuleProperty:

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
        'name': 'str',
        'operator': 'str',
        'value': 'str',
        'value_type': 'str',
        'is_valid': 'bool'
    }

    attribute_map = {
        'key': 'key',
        'type': 'type',
        'name': 'name',
        'operator': 'operator',
        'value': 'value',
        'value_type': 'value_type',
        'is_valid': 'is_valid'
    }

    def __init__(self, key=None, type=None, name=None, operator=None, value=None, value_type=None, is_valid=None):
        r"""RuleProperty

        The model defined in huaweicloud sdk

        :param key: **参数解释**： 属性键。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 
        :type key: str
        :param type: **参数解释**： 类型。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 
        :type type: str
        :param name: **参数解释**： 展示名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 
        :type name: str
        :param operator: **参数解释**： 比较运算符。 **约束限制**： 不涉及。 **取值范围**： - ‘&#x3D;’：等于。 - ‘&gt;’：大于。 - ‘&lt;’：小于。 - ‘&gt;&#x3D;’：大于等于。 - ‘&lt;&#x3D;’：小于等于。 - ‘!&#x3D;’：不等于。 - ‘in’：包含其中。 - ‘not in’：不被包含。 **默认取值**： 不涉及。 
        :type operator: str
        :param value: **参数解释**： 属性值。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 
        :type value: str
        :param value_type: **参数解释**： 数据类型。 **约束限制**： 不涉及。 **取值范围**： - float：数值型。 - string：字符型。 **默认取值**： 不涉及。 
        :type value_type: str
        :param is_valid: **参数解释**： 属性是否启用。 **约束限制**： 不涉及。 **取值范围**： - true：启用。 - false：未启用。 **默认取值**： false。 
        :type is_valid: bool
        """
        
        

        self._key = None
        self._type = None
        self._name = None
        self._operator = None
        self._value = None
        self._value_type = None
        self._is_valid = None
        self.discriminator = None

        self.key = key
        self.type = type
        self.name = name
        if operator is not None:
            self.operator = operator
        self.value = value
        self.value_type = value_type
        if is_valid is not None:
            self.is_valid = is_valid

    @property
    def key(self):
        r"""Gets the key of this RuleProperty.

        **参数解释**： 属性键。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :return: The key of this RuleProperty.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        r"""Sets the key of this RuleProperty.

        **参数解释**： 属性键。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :param key: The key of this RuleProperty.
        :type key: str
        """
        self._key = key

    @property
    def type(self):
        r"""Gets the type of this RuleProperty.

        **参数解释**： 类型。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :return: The type of this RuleProperty.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this RuleProperty.

        **参数解释**： 类型。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :param type: The type of this RuleProperty.
        :type type: str
        """
        self._type = type

    @property
    def name(self):
        r"""Gets the name of this RuleProperty.

        **参数解释**： 展示名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :return: The name of this RuleProperty.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this RuleProperty.

        **参数解释**： 展示名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :param name: The name of this RuleProperty.
        :type name: str
        """
        self._name = name

    @property
    def operator(self):
        r"""Gets the operator of this RuleProperty.

        **参数解释**： 比较运算符。 **约束限制**： 不涉及。 **取值范围**： - ‘=’：等于。 - ‘>’：大于。 - ‘<’：小于。 - ‘>=’：大于等于。 - ‘<=’：小于等于。 - ‘!=’：不等于。 - ‘in’：包含其中。 - ‘not in’：不被包含。 **默认取值**： 不涉及。 

        :return: The operator of this RuleProperty.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        r"""Sets the operator of this RuleProperty.

        **参数解释**： 比较运算符。 **约束限制**： 不涉及。 **取值范围**： - ‘=’：等于。 - ‘>’：大于。 - ‘<’：小于。 - ‘>=’：大于等于。 - ‘<=’：小于等于。 - ‘!=’：不等于。 - ‘in’：包含其中。 - ‘not in’：不被包含。 **默认取值**： 不涉及。 

        :param operator: The operator of this RuleProperty.
        :type operator: str
        """
        self._operator = operator

    @property
    def value(self):
        r"""Gets the value of this RuleProperty.

        **参数解释**： 属性值。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :return: The value of this RuleProperty.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this RuleProperty.

        **参数解释**： 属性值。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :param value: The value of this RuleProperty.
        :type value: str
        """
        self._value = value

    @property
    def value_type(self):
        r"""Gets the value_type of this RuleProperty.

        **参数解释**： 数据类型。 **约束限制**： 不涉及。 **取值范围**： - float：数值型。 - string：字符型。 **默认取值**： 不涉及。 

        :return: The value_type of this RuleProperty.
        :rtype: str
        """
        return self._value_type

    @value_type.setter
    def value_type(self, value_type):
        r"""Sets the value_type of this RuleProperty.

        **参数解释**： 数据类型。 **约束限制**： 不涉及。 **取值范围**： - float：数值型。 - string：字符型。 **默认取值**： 不涉及。 

        :param value_type: The value_type of this RuleProperty.
        :type value_type: str
        """
        self._value_type = value_type

    @property
    def is_valid(self):
        r"""Gets the is_valid of this RuleProperty.

        **参数解释**： 属性是否启用。 **约束限制**： 不涉及。 **取值范围**： - true：启用。 - false：未启用。 **默认取值**： false。 

        :return: The is_valid of this RuleProperty.
        :rtype: bool
        """
        return self._is_valid

    @is_valid.setter
    def is_valid(self, is_valid):
        r"""Sets the is_valid of this RuleProperty.

        **参数解释**： 属性是否启用。 **约束限制**： 不涉及。 **取值范围**： - true：启用。 - false：未启用。 **默认取值**： false。 

        :param is_valid: The is_valid of this RuleProperty.
        :type is_valid: bool
        """
        self._is_valid = is_valid

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
        if not isinstance(other, RuleProperty):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
