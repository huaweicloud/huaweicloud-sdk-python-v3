# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RuleInstanceProperty:

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
        'value_type': 'str'
    }

    attribute_map = {
        'key': 'key',
        'type': 'type',
        'name': 'name',
        'operator': 'operator',
        'value': 'value',
        'value_type': 'value_type'
    }

    def __init__(self, key=None, type=None, name=None, operator=None, value=None, value_type=None):
        r"""RuleInstanceProperty

        The model defined in huaweicloud sdk

        :param key: **参数解释**： 规则属性键。 **取值范围**： 不涉及。 
        :type key: str
        :param type: **参数解释**： 规则类型。 **取值范围**： 不涉及。 
        :type type: str
        :param name: **参数解释**： 展示名称。 **取值范围**： 不涉及。 
        :type name: str
        :param operator: **参数解释**： 比较运算符。 **取值范围**： 不涉及。 
        :type operator: str
        :param value: **参数解释**： 属性值。 **取值范围**： 不涉及。 
        :type value: str
        :param value_type: **参数解释**： 数据类型。 **取值范围**： 不涉及。 
        :type value_type: str
        """
        
        

        self._key = None
        self._type = None
        self._name = None
        self._operator = None
        self._value = None
        self._value_type = None
        self.discriminator = None

        self.key = key
        self.type = type
        self.name = name
        if operator is not None:
            self.operator = operator
        self.value = value
        self.value_type = value_type

    @property
    def key(self):
        r"""Gets the key of this RuleInstanceProperty.

        **参数解释**： 规则属性键。 **取值范围**： 不涉及。 

        :return: The key of this RuleInstanceProperty.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        r"""Sets the key of this RuleInstanceProperty.

        **参数解释**： 规则属性键。 **取值范围**： 不涉及。 

        :param key: The key of this RuleInstanceProperty.
        :type key: str
        """
        self._key = key

    @property
    def type(self):
        r"""Gets the type of this RuleInstanceProperty.

        **参数解释**： 规则类型。 **取值范围**： 不涉及。 

        :return: The type of this RuleInstanceProperty.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this RuleInstanceProperty.

        **参数解释**： 规则类型。 **取值范围**： 不涉及。 

        :param type: The type of this RuleInstanceProperty.
        :type type: str
        """
        self._type = type

    @property
    def name(self):
        r"""Gets the name of this RuleInstanceProperty.

        **参数解释**： 展示名称。 **取值范围**： 不涉及。 

        :return: The name of this RuleInstanceProperty.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this RuleInstanceProperty.

        **参数解释**： 展示名称。 **取值范围**： 不涉及。 

        :param name: The name of this RuleInstanceProperty.
        :type name: str
        """
        self._name = name

    @property
    def operator(self):
        r"""Gets the operator of this RuleInstanceProperty.

        **参数解释**： 比较运算符。 **取值范围**： 不涉及。 

        :return: The operator of this RuleInstanceProperty.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        r"""Sets the operator of this RuleInstanceProperty.

        **参数解释**： 比较运算符。 **取值范围**： 不涉及。 

        :param operator: The operator of this RuleInstanceProperty.
        :type operator: str
        """
        self._operator = operator

    @property
    def value(self):
        r"""Gets the value of this RuleInstanceProperty.

        **参数解释**： 属性值。 **取值范围**： 不涉及。 

        :return: The value of this RuleInstanceProperty.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this RuleInstanceProperty.

        **参数解释**： 属性值。 **取值范围**： 不涉及。 

        :param value: The value of this RuleInstanceProperty.
        :type value: str
        """
        self._value = value

    @property
    def value_type(self):
        r"""Gets the value_type of this RuleInstanceProperty.

        **参数解释**： 数据类型。 **取值范围**： 不涉及。 

        :return: The value_type of this RuleInstanceProperty.
        :rtype: str
        """
        return self._value_type

    @value_type.setter
    def value_type(self, value_type):
        r"""Sets the value_type of this RuleInstanceProperty.

        **参数解释**： 数据类型。 **取值范围**： 不涉及。 

        :param value_type: The value_type of this RuleInstanceProperty.
        :type value_type: str
        """
        self._value_type = value_type

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
        if not isinstance(other, RuleInstanceProperty):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
