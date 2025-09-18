# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NewExtensionOutputs:

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
        'description': 'str',
        'prop': 'dict(str, str)'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'description': 'description',
        'prop': 'prop'
    }

    def __init__(self, name=None, type=None, description=None, prop=None):
        r"""NewExtensionOutputs

        The model defined in huaweicloud sdk

        :param name: **参数解释**： 名称。 **取值范围**： 不涉及。 
        :type name: str
        :param type: **参数解释**： 类型。 **取值范围**： 不涉及。 
        :type type: str
        :param description: **参数解释**： 描述。 **取值范围**： 不涉及。 
        :type description: str
        :param prop: **参数解释**： 扩展信息定义。 **取值范围**： 不涉及。 
        :type prop: dict(str, str)
        """
        
        

        self._name = None
        self._type = None
        self._description = None
        self._prop = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if description is not None:
            self.description = description
        if prop is not None:
            self.prop = prop

    @property
    def name(self):
        r"""Gets the name of this NewExtensionOutputs.

        **参数解释**： 名称。 **取值范围**： 不涉及。 

        :return: The name of this NewExtensionOutputs.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this NewExtensionOutputs.

        **参数解释**： 名称。 **取值范围**： 不涉及。 

        :param name: The name of this NewExtensionOutputs.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this NewExtensionOutputs.

        **参数解释**： 类型。 **取值范围**： 不涉及。 

        :return: The type of this NewExtensionOutputs.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this NewExtensionOutputs.

        **参数解释**： 类型。 **取值范围**： 不涉及。 

        :param type: The type of this NewExtensionOutputs.
        :type type: str
        """
        self._type = type

    @property
    def description(self):
        r"""Gets the description of this NewExtensionOutputs.

        **参数解释**： 描述。 **取值范围**： 不涉及。 

        :return: The description of this NewExtensionOutputs.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this NewExtensionOutputs.

        **参数解释**： 描述。 **取值范围**： 不涉及。 

        :param description: The description of this NewExtensionOutputs.
        :type description: str
        """
        self._description = description

    @property
    def prop(self):
        r"""Gets the prop of this NewExtensionOutputs.

        **参数解释**： 扩展信息定义。 **取值范围**： 不涉及。 

        :return: The prop of this NewExtensionOutputs.
        :rtype: dict(str, str)
        """
        return self._prop

    @prop.setter
    def prop(self, prop):
        r"""Sets the prop of this NewExtensionOutputs.

        **参数解释**： 扩展信息定义。 **取值范围**： 不涉及。 

        :param prop: The prop of this NewExtensionOutputs.
        :type prop: dict(str, str)
        """
        self._prop = prop

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
        if not isinstance(other, NewExtensionOutputs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
