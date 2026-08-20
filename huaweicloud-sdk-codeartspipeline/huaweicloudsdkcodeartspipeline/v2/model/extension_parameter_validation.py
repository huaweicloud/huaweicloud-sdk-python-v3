# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExtensionParameterValidation:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_required': 'bool',
        'pattern': 'str',
        'pattern_description': 'str'
    }

    attribute_map = {
        'is_required': 'isRequired',
        'pattern': 'pattern',
        'pattern_description': 'patternDescription'
    }

    def __init__(self, is_required=None, pattern=None, pattern_description=None):
        r"""ExtensionParameterValidation

        The model defined in huaweicloud sdk

        :param is_required: 是否必填
        :type is_required: bool
        :param pattern: 正则校验
        :type pattern: str
        :param pattern_description: 校验说明
        :type pattern_description: str
        """
        
        

        self._is_required = None
        self._pattern = None
        self._pattern_description = None
        self.discriminator = None

        if is_required is not None:
            self.is_required = is_required
        if pattern is not None:
            self.pattern = pattern
        if pattern_description is not None:
            self.pattern_description = pattern_description

    @property
    def is_required(self):
        r"""Gets the is_required of this ExtensionParameterValidation.

        是否必填

        :return: The is_required of this ExtensionParameterValidation.
        :rtype: bool
        """
        return self._is_required

    @is_required.setter
    def is_required(self, is_required):
        r"""Sets the is_required of this ExtensionParameterValidation.

        是否必填

        :param is_required: The is_required of this ExtensionParameterValidation.
        :type is_required: bool
        """
        self._is_required = is_required

    @property
    def pattern(self):
        r"""Gets the pattern of this ExtensionParameterValidation.

        正则校验

        :return: The pattern of this ExtensionParameterValidation.
        :rtype: str
        """
        return self._pattern

    @pattern.setter
    def pattern(self, pattern):
        r"""Sets the pattern of this ExtensionParameterValidation.

        正则校验

        :param pattern: The pattern of this ExtensionParameterValidation.
        :type pattern: str
        """
        self._pattern = pattern

    @property
    def pattern_description(self):
        r"""Gets the pattern_description of this ExtensionParameterValidation.

        校验说明

        :return: The pattern_description of this ExtensionParameterValidation.
        :rtype: str
        """
        return self._pattern_description

    @pattern_description.setter
    def pattern_description(self, pattern_description):
        r"""Sets the pattern_description of this ExtensionParameterValidation.

        校验说明

        :param pattern_description: The pattern_description of this ExtensionParameterValidation.
        :type pattern_description: str
        """
        self._pattern_description = pattern_description

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
        if not isinstance(other, ExtensionParameterValidation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
