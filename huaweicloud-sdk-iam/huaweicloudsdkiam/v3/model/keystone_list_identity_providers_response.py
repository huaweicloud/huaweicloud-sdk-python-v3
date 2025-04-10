# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class KeystoneListIdentityProvidersResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'identity_providers': 'list[IdentityprovidersResult]',
        'links': 'Links'
    }

    attribute_map = {
        'identity_providers': 'identity_providers',
        'links': 'links'
    }

    def __init__(self, identity_providers=None, links=None):
        r"""KeystoneListIdentityProvidersResponse

        The model defined in huaweicloud sdk

        :param identity_providers: 身份提供商信息列表。
        :type identity_providers: list[:class:`huaweicloudsdkiam.v3.IdentityprovidersResult`]
        :param links: 
        :type links: :class:`huaweicloudsdkiam.v3.Links`
        """
        
        super(KeystoneListIdentityProvidersResponse, self).__init__()

        self._identity_providers = None
        self._links = None
        self.discriminator = None

        if identity_providers is not None:
            self.identity_providers = identity_providers
        if links is not None:
            self.links = links

    @property
    def identity_providers(self):
        r"""Gets the identity_providers of this KeystoneListIdentityProvidersResponse.

        身份提供商信息列表。

        :return: The identity_providers of this KeystoneListIdentityProvidersResponse.
        :rtype: list[:class:`huaweicloudsdkiam.v3.IdentityprovidersResult`]
        """
        return self._identity_providers

    @identity_providers.setter
    def identity_providers(self, identity_providers):
        r"""Sets the identity_providers of this KeystoneListIdentityProvidersResponse.

        身份提供商信息列表。

        :param identity_providers: The identity_providers of this KeystoneListIdentityProvidersResponse.
        :type identity_providers: list[:class:`huaweicloudsdkiam.v3.IdentityprovidersResult`]
        """
        self._identity_providers = identity_providers

    @property
    def links(self):
        r"""Gets the links of this KeystoneListIdentityProvidersResponse.

        :return: The links of this KeystoneListIdentityProvidersResponse.
        :rtype: :class:`huaweicloudsdkiam.v3.Links`
        """
        return self._links

    @links.setter
    def links(self, links):
        r"""Sets the links of this KeystoneListIdentityProvidersResponse.

        :param links: The links of this KeystoneListIdentityProvidersResponse.
        :type links: :class:`huaweicloudsdkiam.v3.Links`
        """
        self._links = links

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
        if not isinstance(other, KeystoneListIdentityProvidersResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
