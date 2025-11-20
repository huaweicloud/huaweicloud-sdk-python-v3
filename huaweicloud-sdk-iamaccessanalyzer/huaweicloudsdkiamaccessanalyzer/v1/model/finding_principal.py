# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FindingPrincipal:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'identifier': 'str',
        'type': 'str'
    }

    attribute_map = {
        'identifier': 'identifier',
        'type': 'type'
    }

    def __init__(self, identifier=None, type=None):
        r"""FindingPrincipal

        The model defined in huaweicloud sdk

        :param identifier: 主体身份的标识符。
        :type identifier: str
        :param type: 主体身份的类型。 - all_principal：所有主体 - account：账号 - all_user_in_account： 账号下所有用户 - all_agency_in_account： 账号下所有委托 - all_identity_provider_in_account：账号下所有身份提供商 - specific_user：特定用户 - specific_agency：特定委托 - specific_group：特定用户组 - specific_identity_provider：特定身份提供商 
        :type type: str
        """
        
        

        self._identifier = None
        self._type = None
        self.discriminator = None

        self.identifier = identifier
        self.type = type

    @property
    def identifier(self):
        r"""Gets the identifier of this FindingPrincipal.

        主体身份的标识符。

        :return: The identifier of this FindingPrincipal.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        r"""Sets the identifier of this FindingPrincipal.

        主体身份的标识符。

        :param identifier: The identifier of this FindingPrincipal.
        :type identifier: str
        """
        self._identifier = identifier

    @property
    def type(self):
        r"""Gets the type of this FindingPrincipal.

        主体身份的类型。 - all_principal：所有主体 - account：账号 - all_user_in_account： 账号下所有用户 - all_agency_in_account： 账号下所有委托 - all_identity_provider_in_account：账号下所有身份提供商 - specific_user：特定用户 - specific_agency：特定委托 - specific_group：特定用户组 - specific_identity_provider：特定身份提供商 

        :return: The type of this FindingPrincipal.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this FindingPrincipal.

        主体身份的类型。 - all_principal：所有主体 - account：账号 - all_user_in_account： 账号下所有用户 - all_agency_in_account： 账号下所有委托 - all_identity_provider_in_account：账号下所有身份提供商 - specific_user：特定用户 - specific_agency：特定委托 - specific_group：特定用户组 - specific_identity_provider：特定身份提供商 

        :param type: The type of this FindingPrincipal.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, FindingPrincipal):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
