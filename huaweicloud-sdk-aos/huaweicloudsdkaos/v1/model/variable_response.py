# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VariableResponse:

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
        'default': 'object',
        'sensitive': 'bool',
        'nullable': 'bool',
        'validations': 'list[VariableValidationResponse]'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'description': 'description',
        'default': 'default',
        'sensitive': 'sensitive',
        'nullable': 'nullable',
        'validations': 'validations'
    }

    def __init__(self, name=None, type=None, description=None, default=None, sensitive=None, nullable=None, validations=None):
        """VariableResponse

        The model defined in huaweicloud sdk

        :param name: 参数的名字
        :type name: str
        :param type: 参数类型
        :type type: str
        :param description: 描述参数的用途
        :type description: str
        :param default: 参数默认值。该类型与type保持一致
        :type default: object
        :param sensitive: 参数是否为敏感字段
        :type sensitive: bool
        :param nullable: 参数是否可设置为null
        :type nullable: bool
        :param validations: 参数校验模块
        :type validations: list[:class:`huaweicloudsdkaos.v1.VariableValidationResponse`]
        """
        
        

        self._name = None
        self._type = None
        self._description = None
        self._default = None
        self._sensitive = None
        self._nullable = None
        self._validations = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if description is not None:
            self.description = description
        if default is not None:
            self.default = default
        if sensitive is not None:
            self.sensitive = sensitive
        if nullable is not None:
            self.nullable = nullable
        if validations is not None:
            self.validations = validations

    @property
    def name(self):
        """Gets the name of this VariableResponse.

        参数的名字

        :return: The name of this VariableResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VariableResponse.

        参数的名字

        :param name: The name of this VariableResponse.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        """Gets the type of this VariableResponse.

        参数类型

        :return: The type of this VariableResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this VariableResponse.

        参数类型

        :param type: The type of this VariableResponse.
        :type type: str
        """
        self._type = type

    @property
    def description(self):
        """Gets the description of this VariableResponse.

        描述参数的用途

        :return: The description of this VariableResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this VariableResponse.

        描述参数的用途

        :param description: The description of this VariableResponse.
        :type description: str
        """
        self._description = description

    @property
    def default(self):
        """Gets the default of this VariableResponse.

        参数默认值。该类型与type保持一致

        :return: The default of this VariableResponse.
        :rtype: object
        """
        return self._default

    @default.setter
    def default(self, default):
        """Sets the default of this VariableResponse.

        参数默认值。该类型与type保持一致

        :param default: The default of this VariableResponse.
        :type default: object
        """
        self._default = default

    @property
    def sensitive(self):
        """Gets the sensitive of this VariableResponse.

        参数是否为敏感字段

        :return: The sensitive of this VariableResponse.
        :rtype: bool
        """
        return self._sensitive

    @sensitive.setter
    def sensitive(self, sensitive):
        """Sets the sensitive of this VariableResponse.

        参数是否为敏感字段

        :param sensitive: The sensitive of this VariableResponse.
        :type sensitive: bool
        """
        self._sensitive = sensitive

    @property
    def nullable(self):
        """Gets the nullable of this VariableResponse.

        参数是否可设置为null

        :return: The nullable of this VariableResponse.
        :rtype: bool
        """
        return self._nullable

    @nullable.setter
    def nullable(self, nullable):
        """Sets the nullable of this VariableResponse.

        参数是否可设置为null

        :param nullable: The nullable of this VariableResponse.
        :type nullable: bool
        """
        self._nullable = nullable

    @property
    def validations(self):
        """Gets the validations of this VariableResponse.

        参数校验模块

        :return: The validations of this VariableResponse.
        :rtype: list[:class:`huaweicloudsdkaos.v1.VariableValidationResponse`]
        """
        return self._validations

    @validations.setter
    def validations(self, validations):
        """Sets the validations of this VariableResponse.

        参数校验模块

        :param validations: The validations of this VariableResponse.
        :type validations: list[:class:`huaweicloudsdkaos.v1.VariableValidationResponse`]
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
        if not isinstance(other, VariableResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
