# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IdentityProviderConfigDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'issuer_url': 'str',
        'metadata_url': 'str',
        'remote_login_url': 'str',
        'remote_logout_url': 'str'
    }

    attribute_map = {
        'issuer_url': 'issuer_url',
        'metadata_url': 'metadata_url',
        'remote_login_url': 'remote_login_url',
        'remote_logout_url': 'remote_logout_url'
    }

    def __init__(self, issuer_url=None, metadata_url=None, remote_login_url=None, remote_logout_url=None):
        r"""IdentityProviderConfigDto

        The model defined in huaweicloud sdk

        :param issuer_url: 身份提供商issuer
        :type issuer_url: str
        :param metadata_url: 身份提供商元数据
        :type metadata_url: str
        :param remote_login_url: 身份提供商远程登录链接
        :type remote_login_url: str
        :param remote_logout_url: 身份提供商远程登出链接
        :type remote_logout_url: str
        """
        
        

        self._issuer_url = None
        self._metadata_url = None
        self._remote_login_url = None
        self._remote_logout_url = None
        self.discriminator = None

        self.issuer_url = issuer_url
        self.metadata_url = metadata_url
        self.remote_login_url = remote_login_url
        self.remote_logout_url = remote_logout_url

    @property
    def issuer_url(self):
        r"""Gets the issuer_url of this IdentityProviderConfigDto.

        身份提供商issuer

        :return: The issuer_url of this IdentityProviderConfigDto.
        :rtype: str
        """
        return self._issuer_url

    @issuer_url.setter
    def issuer_url(self, issuer_url):
        r"""Sets the issuer_url of this IdentityProviderConfigDto.

        身份提供商issuer

        :param issuer_url: The issuer_url of this IdentityProviderConfigDto.
        :type issuer_url: str
        """
        self._issuer_url = issuer_url

    @property
    def metadata_url(self):
        r"""Gets the metadata_url of this IdentityProviderConfigDto.

        身份提供商元数据

        :return: The metadata_url of this IdentityProviderConfigDto.
        :rtype: str
        """
        return self._metadata_url

    @metadata_url.setter
    def metadata_url(self, metadata_url):
        r"""Sets the metadata_url of this IdentityProviderConfigDto.

        身份提供商元数据

        :param metadata_url: The metadata_url of this IdentityProviderConfigDto.
        :type metadata_url: str
        """
        self._metadata_url = metadata_url

    @property
    def remote_login_url(self):
        r"""Gets the remote_login_url of this IdentityProviderConfigDto.

        身份提供商远程登录链接

        :return: The remote_login_url of this IdentityProviderConfigDto.
        :rtype: str
        """
        return self._remote_login_url

    @remote_login_url.setter
    def remote_login_url(self, remote_login_url):
        r"""Sets the remote_login_url of this IdentityProviderConfigDto.

        身份提供商远程登录链接

        :param remote_login_url: The remote_login_url of this IdentityProviderConfigDto.
        :type remote_login_url: str
        """
        self._remote_login_url = remote_login_url

    @property
    def remote_logout_url(self):
        r"""Gets the remote_logout_url of this IdentityProviderConfigDto.

        身份提供商远程登出链接

        :return: The remote_logout_url of this IdentityProviderConfigDto.
        :rtype: str
        """
        return self._remote_logout_url

    @remote_logout_url.setter
    def remote_logout_url(self, remote_logout_url):
        r"""Sets the remote_logout_url of this IdentityProviderConfigDto.

        身份提供商远程登出链接

        :param remote_logout_url: The remote_logout_url of this IdentityProviderConfigDto.
        :type remote_logout_url: str
        """
        self._remote_logout_url = remote_logout_url

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
        if not isinstance(other, IdentityProviderConfigDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
