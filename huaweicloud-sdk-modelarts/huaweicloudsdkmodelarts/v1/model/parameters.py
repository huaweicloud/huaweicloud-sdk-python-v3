# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Parameters:

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
        'value': 'str',
        'description': 'str',
        'constraint': 'ParametersConstraint',
        'i18n_description': 'I18nDescription'
    }

    attribute_map = {
        'name': 'name',
        'value': 'value',
        'description': 'description',
        'constraint': 'constraint',
        'i18n_description': 'i18n_description'
    }

    def __init__(self, name=None, value=None, description=None, constraint=None, i18n_description=None):
        r"""Parameters

        The model defined in huaweicloud sdk

        :param name: 参数名称。
        :type name: str
        :param value: 参数值。
        :type value: str
        :param description: 参数描述信息。
        :type description: str
        :param constraint: 
        :type constraint: :class:`huaweicloudsdkmodelarts.v1.ParametersConstraint`
        :param i18n_description: 
        :type i18n_description: :class:`huaweicloudsdkmodelarts.v1.I18nDescription`
        """
        
        

        self._name = None
        self._value = None
        self._description = None
        self._constraint = None
        self._i18n_description = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if value is not None:
            self.value = value
        if description is not None:
            self.description = description
        if constraint is not None:
            self.constraint = constraint
        if i18n_description is not None:
            self.i18n_description = i18n_description

    @property
    def name(self):
        r"""Gets the name of this Parameters.

        参数名称。

        :return: The name of this Parameters.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Parameters.

        参数名称。

        :param name: The name of this Parameters.
        :type name: str
        """
        self._name = name

    @property
    def value(self):
        r"""Gets the value of this Parameters.

        参数值。

        :return: The value of this Parameters.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this Parameters.

        参数值。

        :param value: The value of this Parameters.
        :type value: str
        """
        self._value = value

    @property
    def description(self):
        r"""Gets the description of this Parameters.

        参数描述信息。

        :return: The description of this Parameters.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this Parameters.

        参数描述信息。

        :param description: The description of this Parameters.
        :type description: str
        """
        self._description = description

    @property
    def constraint(self):
        r"""Gets the constraint of this Parameters.

        :return: The constraint of this Parameters.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ParametersConstraint`
        """
        return self._constraint

    @constraint.setter
    def constraint(self, constraint):
        r"""Sets the constraint of this Parameters.

        :param constraint: The constraint of this Parameters.
        :type constraint: :class:`huaweicloudsdkmodelarts.v1.ParametersConstraint`
        """
        self._constraint = constraint

    @property
    def i18n_description(self):
        r"""Gets the i18n_description of this Parameters.

        :return: The i18n_description of this Parameters.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.I18nDescription`
        """
        return self._i18n_description

    @i18n_description.setter
    def i18n_description(self, i18n_description):
        r"""Sets the i18n_description of this Parameters.

        :param i18n_description: The i18n_description of this Parameters.
        :type i18n_description: :class:`huaweicloudsdkmodelarts.v1.I18nDescription`
        """
        self._i18n_description = i18n_description

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
        if not isinstance(other, Parameters):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
