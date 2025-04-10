# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NewExtensionInputs:

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
        'label': 'str',
        'description': 'str',
        'default_value': 'str',
        'required': 'bool',
        'extend_prop': 'ExtensionExtendProp',
        'validation': 'ExtensionValidation'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'label': 'label',
        'description': 'description',
        'default_value': 'default_value',
        'required': 'required',
        'extend_prop': 'extend_prop',
        'validation': 'validation'
    }

    def __init__(self, name=None, type=None, label=None, description=None, default_value=None, required=None, extend_prop=None, validation=None):
        r"""NewExtensionInputs

        The model defined in huaweicloud sdk

        :param name: 名称
        :type name: str
        :param type: 类型
        :type type: str
        :param label: 标签
        :type label: str
        :param description: 说明
        :type description: str
        :param default_value: 默认值
        :type default_value: str
        :param required: 必填
        :type required: bool
        :param extend_prop: 
        :type extend_prop: :class:`huaweicloudsdkcodeartspipeline.v2.ExtensionExtendProp`
        :param validation: 
        :type validation: :class:`huaweicloudsdkcodeartspipeline.v2.ExtensionValidation`
        """
        
        

        self._name = None
        self._type = None
        self._label = None
        self._description = None
        self._default_value = None
        self._required = None
        self._extend_prop = None
        self._validation = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if label is not None:
            self.label = label
        if description is not None:
            self.description = description
        if default_value is not None:
            self.default_value = default_value
        if required is not None:
            self.required = required
        if extend_prop is not None:
            self.extend_prop = extend_prop
        if validation is not None:
            self.validation = validation

    @property
    def name(self):
        r"""Gets the name of this NewExtensionInputs.

        名称

        :return: The name of this NewExtensionInputs.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this NewExtensionInputs.

        名称

        :param name: The name of this NewExtensionInputs.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this NewExtensionInputs.

        类型

        :return: The type of this NewExtensionInputs.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this NewExtensionInputs.

        类型

        :param type: The type of this NewExtensionInputs.
        :type type: str
        """
        self._type = type

    @property
    def label(self):
        r"""Gets the label of this NewExtensionInputs.

        标签

        :return: The label of this NewExtensionInputs.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        r"""Sets the label of this NewExtensionInputs.

        标签

        :param label: The label of this NewExtensionInputs.
        :type label: str
        """
        self._label = label

    @property
    def description(self):
        r"""Gets the description of this NewExtensionInputs.

        说明

        :return: The description of this NewExtensionInputs.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this NewExtensionInputs.

        说明

        :param description: The description of this NewExtensionInputs.
        :type description: str
        """
        self._description = description

    @property
    def default_value(self):
        r"""Gets the default_value of this NewExtensionInputs.

        默认值

        :return: The default_value of this NewExtensionInputs.
        :rtype: str
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        r"""Sets the default_value of this NewExtensionInputs.

        默认值

        :param default_value: The default_value of this NewExtensionInputs.
        :type default_value: str
        """
        self._default_value = default_value

    @property
    def required(self):
        r"""Gets the required of this NewExtensionInputs.

        必填

        :return: The required of this NewExtensionInputs.
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        r"""Sets the required of this NewExtensionInputs.

        必填

        :param required: The required of this NewExtensionInputs.
        :type required: bool
        """
        self._required = required

    @property
    def extend_prop(self):
        r"""Gets the extend_prop of this NewExtensionInputs.

        :return: The extend_prop of this NewExtensionInputs.
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.ExtensionExtendProp`
        """
        return self._extend_prop

    @extend_prop.setter
    def extend_prop(self, extend_prop):
        r"""Sets the extend_prop of this NewExtensionInputs.

        :param extend_prop: The extend_prop of this NewExtensionInputs.
        :type extend_prop: :class:`huaweicloudsdkcodeartspipeline.v2.ExtensionExtendProp`
        """
        self._extend_prop = extend_prop

    @property
    def validation(self):
        r"""Gets the validation of this NewExtensionInputs.

        :return: The validation of this NewExtensionInputs.
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.ExtensionValidation`
        """
        return self._validation

    @validation.setter
    def validation(self, validation):
        r"""Sets the validation of this NewExtensionInputs.

        :param validation: The validation of this NewExtensionInputs.
        :type validation: :class:`huaweicloudsdkcodeartspipeline.v2.ExtensionValidation`
        """
        self._validation = validation

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
        if not isinstance(other, NewExtensionInputs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
