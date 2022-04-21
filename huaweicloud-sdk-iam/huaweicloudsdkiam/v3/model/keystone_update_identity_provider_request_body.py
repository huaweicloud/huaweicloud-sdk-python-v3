# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class KeystoneUpdateIdentityProviderRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'identity_provider': 'UpdateIdentityproviderOption'
    }

    attribute_map = {
        'identity_provider': 'identity_provider'
    }

    def __init__(self, identity_provider=None):
        """KeystoneUpdateIdentityProviderRequestBody

        The model defined in huaweicloud sdk

        :param identity_provider: 
        :type identity_provider: :class:`huaweicloudsdkiam.v3.UpdateIdentityproviderOption`
        """
        
        

        self._identity_provider = None
        self.discriminator = None

        self.identity_provider = identity_provider

    @property
    def identity_provider(self):
        """Gets the identity_provider of this KeystoneUpdateIdentityProviderRequestBody.


        :return: The identity_provider of this KeystoneUpdateIdentityProviderRequestBody.
        :rtype: :class:`huaweicloudsdkiam.v3.UpdateIdentityproviderOption`
        """
        return self._identity_provider

    @identity_provider.setter
    def identity_provider(self, identity_provider):
        """Sets the identity_provider of this KeystoneUpdateIdentityProviderRequestBody.


        :param identity_provider: The identity_provider of this KeystoneUpdateIdentityProviderRequestBody.
        :type identity_provider: :class:`huaweicloudsdkiam.v3.UpdateIdentityproviderOption`
        """
        self._identity_provider = identity_provider

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
        if not isinstance(other, KeystoneUpdateIdentityProviderRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
