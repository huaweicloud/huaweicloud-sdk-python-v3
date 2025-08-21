# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TemplateParamVariable:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'default': 'object',
        'name': 'str',
        'description': 'str',
        'nullable': 'bool',
        'sensitive': 'bool',
        'type': 'str',
        'validations': 'list[TemplateParamVariableValidation]'
    }

    attribute_map = {
        'default': 'default',
        'name': 'name',
        'description': 'description',
        'nullable': 'nullable',
        'sensitive': 'sensitive',
        'type': 'type',
        'validations': 'validations'
    }

    def __init__(self, default=None, name=None, description=None, nullable=None, sensitive=None, type=None, validations=None):
        r"""TemplateParamVariable

        The model defined in huaweicloud sdk

        :param default: 变量默认值。
        :type default: object
        :param name: 变量名称。
        :type name: str
        :param description: 变量描述。
        :type description: str
        :param nullable: 变量是否可以为空。
        :type nullable: bool
        :param sensitive: 变量是否为敏感字段。
        :type sensitive: bool
        :param type: 变量类型。
        :type type: str
        :param validations: 模板的部署参数变量的校验规则。
        :type validations: list[:class:`huaweicloudsdkrgc.v1.TemplateParamVariableValidation`]
        """
        
        

        self._default = None
        self._name = None
        self._description = None
        self._nullable = None
        self._sensitive = None
        self._type = None
        self._validations = None
        self.discriminator = None

        if default is not None:
            self.default = default
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if nullable is not None:
            self.nullable = nullable
        if sensitive is not None:
            self.sensitive = sensitive
        if type is not None:
            self.type = type
        if validations is not None:
            self.validations = validations

    @property
    def default(self):
        r"""Gets the default of this TemplateParamVariable.

        变量默认值。

        :return: The default of this TemplateParamVariable.
        :rtype: object
        """
        return self._default

    @default.setter
    def default(self, default):
        r"""Sets the default of this TemplateParamVariable.

        变量默认值。

        :param default: The default of this TemplateParamVariable.
        :type default: object
        """
        self._default = default

    @property
    def name(self):
        r"""Gets the name of this TemplateParamVariable.

        变量名称。

        :return: The name of this TemplateParamVariable.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this TemplateParamVariable.

        变量名称。

        :param name: The name of this TemplateParamVariable.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this TemplateParamVariable.

        变量描述。

        :return: The description of this TemplateParamVariable.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this TemplateParamVariable.

        变量描述。

        :param description: The description of this TemplateParamVariable.
        :type description: str
        """
        self._description = description

    @property
    def nullable(self):
        r"""Gets the nullable of this TemplateParamVariable.

        变量是否可以为空。

        :return: The nullable of this TemplateParamVariable.
        :rtype: bool
        """
        return self._nullable

    @nullable.setter
    def nullable(self, nullable):
        r"""Sets the nullable of this TemplateParamVariable.

        变量是否可以为空。

        :param nullable: The nullable of this TemplateParamVariable.
        :type nullable: bool
        """
        self._nullable = nullable

    @property
    def sensitive(self):
        r"""Gets the sensitive of this TemplateParamVariable.

        变量是否为敏感字段。

        :return: The sensitive of this TemplateParamVariable.
        :rtype: bool
        """
        return self._sensitive

    @sensitive.setter
    def sensitive(self, sensitive):
        r"""Sets the sensitive of this TemplateParamVariable.

        变量是否为敏感字段。

        :param sensitive: The sensitive of this TemplateParamVariable.
        :type sensitive: bool
        """
        self._sensitive = sensitive

    @property
    def type(self):
        r"""Gets the type of this TemplateParamVariable.

        变量类型。

        :return: The type of this TemplateParamVariable.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this TemplateParamVariable.

        变量类型。

        :param type: The type of this TemplateParamVariable.
        :type type: str
        """
        self._type = type

    @property
    def validations(self):
        r"""Gets the validations of this TemplateParamVariable.

        模板的部署参数变量的校验规则。

        :return: The validations of this TemplateParamVariable.
        :rtype: list[:class:`huaweicloudsdkrgc.v1.TemplateParamVariableValidation`]
        """
        return self._validations

    @validations.setter
    def validations(self, validations):
        r"""Sets the validations of this TemplateParamVariable.

        模板的部署参数变量的校验规则。

        :param validations: The validations of this TemplateParamVariable.
        :type validations: list[:class:`huaweicloudsdkrgc.v1.TemplateParamVariableValidation`]
        """
        self._validations = validations

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
        if not isinstance(other, TemplateParamVariable):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
