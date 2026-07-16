# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UserResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'domain': 'Domain'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'domain': 'domain'
    }

    def __init__(self, id=None, name=None, domain=None):
        r"""UserResponse

        The model defined in huaweicloud sdk

        :param id: **参数解释**：用户ID。 **取值范围**：不涉及。
        :type id: str
        :param name: **参数解释**：用户名。 **取值范围**：不涉及。
        :type name: str
        :param domain: 
        :type domain: :class:`huaweicloudsdkmodelarts.v1.Domain`
        """
        
        

        self._id = None
        self._name = None
        self._domain = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if domain is not None:
            self.domain = domain

    @property
    def id(self):
        r"""Gets the id of this UserResponse.

        **参数解释**：用户ID。 **取值范围**：不涉及。

        :return: The id of this UserResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this UserResponse.

        **参数解释**：用户ID。 **取值范围**：不涉及。

        :param id: The id of this UserResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this UserResponse.

        **参数解释**：用户名。 **取值范围**：不涉及。

        :return: The name of this UserResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UserResponse.

        **参数解释**：用户名。 **取值范围**：不涉及。

        :param name: The name of this UserResponse.
        :type name: str
        """
        self._name = name

    @property
    def domain(self):
        r"""Gets the domain of this UserResponse.

        :return: The domain of this UserResponse.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.Domain`
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        r"""Sets the domain of this UserResponse.

        :param domain: The domain of this UserResponse.
        :type domain: :class:`huaweicloudsdkmodelarts.v1.Domain`
        """
        self._domain = domain

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
        if not isinstance(other, UserResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
