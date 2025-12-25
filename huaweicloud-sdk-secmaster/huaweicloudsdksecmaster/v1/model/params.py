# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Params:

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
        'value': 'str',
        'description': 'str',
        'example': 'str',
        'mandatory': 'bool'
    }

    attribute_map = {
        'key': 'key',
        'value': 'value',
        'description': 'description',
        'example': 'example',
        'mandatory': 'mandatory'
    }

    def __init__(self, key=None, value=None, description=None, example=None, mandatory=None):
        r"""Params

        The model defined in huaweicloud sdk

        :param key: 分类映射id
        :type key: str
        :param value: 分类映射id
        :type value: str
        :param description: 描述
        :type description: str
        :param example: 示例
        :type example: str
        :param mandatory: 是否必填
        :type mandatory: bool
        """
        
        

        self._key = None
        self._value = None
        self._description = None
        self._example = None
        self._mandatory = None
        self.discriminator = None

        if key is not None:
            self.key = key
        if value is not None:
            self.value = value
        if description is not None:
            self.description = description
        if example is not None:
            self.example = example
        if mandatory is not None:
            self.mandatory = mandatory

    @property
    def key(self):
        r"""Gets the key of this Params.

        分类映射id

        :return: The key of this Params.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        r"""Sets the key of this Params.

        分类映射id

        :param key: The key of this Params.
        :type key: str
        """
        self._key = key

    @property
    def value(self):
        r"""Gets the value of this Params.

        分类映射id

        :return: The value of this Params.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this Params.

        分类映射id

        :param value: The value of this Params.
        :type value: str
        """
        self._value = value

    @property
    def description(self):
        r"""Gets the description of this Params.

        描述

        :return: The description of this Params.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this Params.

        描述

        :param description: The description of this Params.
        :type description: str
        """
        self._description = description

    @property
    def example(self):
        r"""Gets the example of this Params.

        示例

        :return: The example of this Params.
        :rtype: str
        """
        return self._example

    @example.setter
    def example(self, example):
        r"""Sets the example of this Params.

        示例

        :param example: The example of this Params.
        :type example: str
        """
        self._example = example

    @property
    def mandatory(self):
        r"""Gets the mandatory of this Params.

        是否必填

        :return: The mandatory of this Params.
        :rtype: bool
        """
        return self._mandatory

    @mandatory.setter
    def mandatory(self, mandatory):
        r"""Sets the mandatory of this Params.

        是否必填

        :param mandatory: The mandatory of this Params.
        :type mandatory: bool
        """
        self._mandatory = mandatory

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
        if not isinstance(other, Params):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
