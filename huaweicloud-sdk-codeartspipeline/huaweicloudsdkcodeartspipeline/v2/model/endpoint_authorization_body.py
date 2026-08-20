# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EndpointAuthorizationBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'parameters': 'object',
        'scheme': 'str'
    }

    attribute_map = {
        'parameters': 'parameters',
        'scheme': 'scheme'
    }

    def __init__(self, parameters=None, scheme=None):
        r"""EndpointAuthorizationBody

        The model defined in huaweicloud sdk

        :param parameters: **参数解释**： 鉴权参数。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 
        :type parameters: object
        :param scheme: **参数解释**： 鉴权模式。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 
        :type scheme: str
        """
        
        

        self._parameters = None
        self._scheme = None
        self.discriminator = None

        if parameters is not None:
            self.parameters = parameters
        if scheme is not None:
            self.scheme = scheme

    @property
    def parameters(self):
        r"""Gets the parameters of this EndpointAuthorizationBody.

        **参数解释**： 鉴权参数。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :return: The parameters of this EndpointAuthorizationBody.
        :rtype: object
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        r"""Sets the parameters of this EndpointAuthorizationBody.

        **参数解释**： 鉴权参数。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :param parameters: The parameters of this EndpointAuthorizationBody.
        :type parameters: object
        """
        self._parameters = parameters

    @property
    def scheme(self):
        r"""Gets the scheme of this EndpointAuthorizationBody.

        **参数解释**： 鉴权模式。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :return: The scheme of this EndpointAuthorizationBody.
        :rtype: str
        """
        return self._scheme

    @scheme.setter
    def scheme(self, scheme):
        r"""Sets the scheme of this EndpointAuthorizationBody.

        **参数解释**： 鉴权模式。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :param scheme: The scheme of this EndpointAuthorizationBody.
        :type scheme: str
        """
        self._scheme = scheme

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
        if not isinstance(other, EndpointAuthorizationBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
