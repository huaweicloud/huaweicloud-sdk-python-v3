# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Parameter:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'param_name': 'str',
        'param_type': 'str',
        'param_group': 'str',
        'default_value': 'str',
        'id': 'str',
        'encryption': 'bool',
        'hint': 'str',
        'quote_param': 'bool',
        'required': 'bool',
        'description': 'str'
    }

    attribute_map = {
        'param_name': 'param_name',
        'param_type': 'param_type',
        'param_group': 'param_group',
        'default_value': 'default_value',
        'id': 'id',
        'encryption': 'encryption',
        'hint': 'hint',
        'quote_param': 'quote_param',
        'required': 'required',
        'description': 'description'
    }

    def __init__(self, param_name=None, param_type=None, param_group=None, default_value=None, id=None, encryption=None, hint=None, quote_param=None, required=None, description=None):
        r"""Parameter

        The model defined in huaweicloud sdk

        :param param_name: 参数名称。
        :type param_name: str
        :param param_type: 参数类型。
        :type param_type: str
        :param param_group: 参数分组。
        :type param_group: str
        :param default_value: 参数初始值。
        :type default_value: str
        :param id: 参数id。
        :type id: str
        :param encryption: 是否加密。
        :type encryption: bool
        :param hint: 参数提示。
        :type hint: str
        :param quote_param: 是否从参数库选择。
        :type quote_param: bool
        :param required: 是否为必填参数。
        :type required: bool
        :param description: 参数描述。
        :type description: str
        """
        
        

        self._param_name = None
        self._param_type = None
        self._param_group = None
        self._default_value = None
        self._id = None
        self._encryption = None
        self._hint = None
        self._quote_param = None
        self._required = None
        self._description = None
        self.discriminator = None

        self.param_name = param_name
        if param_type is not None:
            self.param_type = param_type
        if param_group is not None:
            self.param_group = param_group
        if default_value is not None:
            self.default_value = default_value
        if id is not None:
            self.id = id
        self.encryption = encryption
        if hint is not None:
            self.hint = hint
        self.quote_param = quote_param
        self.required = required
        if description is not None:
            self.description = description

    @property
    def param_name(self):
        r"""Gets the param_name of this Parameter.

        参数名称。

        :return: The param_name of this Parameter.
        :rtype: str
        """
        return self._param_name

    @param_name.setter
    def param_name(self, param_name):
        r"""Sets the param_name of this Parameter.

        参数名称。

        :param param_name: The param_name of this Parameter.
        :type param_name: str
        """
        self._param_name = param_name

    @property
    def param_type(self):
        r"""Gets the param_type of this Parameter.

        参数类型。

        :return: The param_type of this Parameter.
        :rtype: str
        """
        return self._param_type

    @param_type.setter
    def param_type(self, param_type):
        r"""Sets the param_type of this Parameter.

        参数类型。

        :param param_type: The param_type of this Parameter.
        :type param_type: str
        """
        self._param_type = param_type

    @property
    def param_group(self):
        r"""Gets the param_group of this Parameter.

        参数分组。

        :return: The param_group of this Parameter.
        :rtype: str
        """
        return self._param_group

    @param_group.setter
    def param_group(self, param_group):
        r"""Sets the param_group of this Parameter.

        参数分组。

        :param param_group: The param_group of this Parameter.
        :type param_group: str
        """
        self._param_group = param_group

    @property
    def default_value(self):
        r"""Gets the default_value of this Parameter.

        参数初始值。

        :return: The default_value of this Parameter.
        :rtype: str
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        r"""Sets the default_value of this Parameter.

        参数初始值。

        :param default_value: The default_value of this Parameter.
        :type default_value: str
        """
        self._default_value = default_value

    @property
    def id(self):
        r"""Gets the id of this Parameter.

        参数id。

        :return: The id of this Parameter.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this Parameter.

        参数id。

        :param id: The id of this Parameter.
        :type id: str
        """
        self._id = id

    @property
    def encryption(self):
        r"""Gets the encryption of this Parameter.

        是否加密。

        :return: The encryption of this Parameter.
        :rtype: bool
        """
        return self._encryption

    @encryption.setter
    def encryption(self, encryption):
        r"""Sets the encryption of this Parameter.

        是否加密。

        :param encryption: The encryption of this Parameter.
        :type encryption: bool
        """
        self._encryption = encryption

    @property
    def hint(self):
        r"""Gets the hint of this Parameter.

        参数提示。

        :return: The hint of this Parameter.
        :rtype: str
        """
        return self._hint

    @hint.setter
    def hint(self, hint):
        r"""Sets the hint of this Parameter.

        参数提示。

        :param hint: The hint of this Parameter.
        :type hint: str
        """
        self._hint = hint

    @property
    def quote_param(self):
        r"""Gets the quote_param of this Parameter.

        是否从参数库选择。

        :return: The quote_param of this Parameter.
        :rtype: bool
        """
        return self._quote_param

    @quote_param.setter
    def quote_param(self, quote_param):
        r"""Sets the quote_param of this Parameter.

        是否从参数库选择。

        :param quote_param: The quote_param of this Parameter.
        :type quote_param: bool
        """
        self._quote_param = quote_param

    @property
    def required(self):
        r"""Gets the required of this Parameter.

        是否为必填参数。

        :return: The required of this Parameter.
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        r"""Sets the required of this Parameter.

        是否为必填参数。

        :param required: The required of this Parameter.
        :type required: bool
        """
        self._required = required

    @property
    def description(self):
        r"""Gets the description of this Parameter.

        参数描述。

        :return: The description of this Parameter.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this Parameter.

        参数描述。

        :param description: The description of this Parameter.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, Parameter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
