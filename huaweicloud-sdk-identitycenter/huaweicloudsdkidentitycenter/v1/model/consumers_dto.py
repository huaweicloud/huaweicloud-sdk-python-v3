# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConsumersDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'binding': 'str',
        'default_value': 'bool',
        'location': 'str'
    }

    attribute_map = {
        'binding': 'binding',
        'default_value': 'default_value',
        'location': 'location'
    }

    def __init__(self, binding=None, default_value=None, location=None):
        r"""ConsumersDto

        The model defined in huaweicloud sdk

        :param binding: SAML传输协议
        :type binding: str
        :param default_value: 是否是默认接收方
        :type default_value: bool
        :param location: SAML ACS Url
        :type location: str
        """
        
        

        self._binding = None
        self._default_value = None
        self._location = None
        self.discriminator = None

        self.binding = binding
        self.default_value = default_value
        self.location = location

    @property
    def binding(self):
        r"""Gets the binding of this ConsumersDto.

        SAML传输协议

        :return: The binding of this ConsumersDto.
        :rtype: str
        """
        return self._binding

    @binding.setter
    def binding(self, binding):
        r"""Sets the binding of this ConsumersDto.

        SAML传输协议

        :param binding: The binding of this ConsumersDto.
        :type binding: str
        """
        self._binding = binding

    @property
    def default_value(self):
        r"""Gets the default_value of this ConsumersDto.

        是否是默认接收方

        :return: The default_value of this ConsumersDto.
        :rtype: bool
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        r"""Sets the default_value of this ConsumersDto.

        是否是默认接收方

        :param default_value: The default_value of this ConsumersDto.
        :type default_value: bool
        """
        self._default_value = default_value

    @property
    def location(self):
        r"""Gets the location of this ConsumersDto.

        SAML ACS Url

        :return: The location of this ConsumersDto.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        r"""Sets the location of this ConsumersDto.

        SAML ACS Url

        :param location: The location of this ConsumersDto.
        :type location: str
        """
        self._location = location

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
        if not isinstance(other, ConsumersDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
