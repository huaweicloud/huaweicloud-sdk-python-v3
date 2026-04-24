# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateStsCredentialProviderReqBody:

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
        'agency_urn': 'str',
        'tags': 'list[Tag]'
    }

    attribute_map = {
        'name': 'name',
        'agency_urn': 'agency_urn',
        'tags': 'tags'
    }

    def __init__(self, name=None, agency_urn=None, tags=None):
        r"""CreateStsCredentialProviderReqBody

        The model defined in huaweicloud sdk

        :param name: The name of the credential provider.
        :type name: str
        :param agency_urn: The URN of the agency used to obtain IAM temporary credentials.
        :type agency_urn: str
        :param tags: 自定义标签列表。
        :type tags: list[:class:`huaweicloudsdkagentidentity.v1.Tag`]
        """
        
        

        self._name = None
        self._agency_urn = None
        self._tags = None
        self.discriminator = None

        self.name = name
        self.agency_urn = agency_urn
        if tags is not None:
            self.tags = tags

    @property
    def name(self):
        r"""Gets the name of this CreateStsCredentialProviderReqBody.

        The name of the credential provider.

        :return: The name of this CreateStsCredentialProviderReqBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateStsCredentialProviderReqBody.

        The name of the credential provider.

        :param name: The name of this CreateStsCredentialProviderReqBody.
        :type name: str
        """
        self._name = name

    @property
    def agency_urn(self):
        r"""Gets the agency_urn of this CreateStsCredentialProviderReqBody.

        The URN of the agency used to obtain IAM temporary credentials.

        :return: The agency_urn of this CreateStsCredentialProviderReqBody.
        :rtype: str
        """
        return self._agency_urn

    @agency_urn.setter
    def agency_urn(self, agency_urn):
        r"""Sets the agency_urn of this CreateStsCredentialProviderReqBody.

        The URN of the agency used to obtain IAM temporary credentials.

        :param agency_urn: The agency_urn of this CreateStsCredentialProviderReqBody.
        :type agency_urn: str
        """
        self._agency_urn = agency_urn

    @property
    def tags(self):
        r"""Gets the tags of this CreateStsCredentialProviderReqBody.

        自定义标签列表。

        :return: The tags of this CreateStsCredentialProviderReqBody.
        :rtype: list[:class:`huaweicloudsdkagentidentity.v1.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this CreateStsCredentialProviderReqBody.

        自定义标签列表。

        :param tags: The tags of this CreateStsCredentialProviderReqBody.
        :type tags: list[:class:`huaweicloudsdkagentidentity.v1.Tag`]
        """
        self._tags = tags

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
        if not isinstance(other, CreateStsCredentialProviderReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
