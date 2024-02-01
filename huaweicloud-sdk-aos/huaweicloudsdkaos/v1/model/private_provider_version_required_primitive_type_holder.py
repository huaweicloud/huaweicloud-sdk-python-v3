# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PrivateProviderVersionRequiredPrimitiveTypeHolder:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'provider_version': 'str'
    }

    attribute_map = {
        'provider_version': 'provider_version'
    }

    def __init__(self, provider_version=None):
        """PrivateProviderVersionRequiredPrimitiveTypeHolder

        The model defined in huaweicloud sdk

        :param provider_version: provider的版本号。版本号必须遵循语义化版本号（Semantic Version），为用户自定义
        :type provider_version: str
        """
        
        

        self._provider_version = None
        self.discriminator = None

        self.provider_version = provider_version

    @property
    def provider_version(self):
        """Gets the provider_version of this PrivateProviderVersionRequiredPrimitiveTypeHolder.

        provider的版本号。版本号必须遵循语义化版本号（Semantic Version），为用户自定义

        :return: The provider_version of this PrivateProviderVersionRequiredPrimitiveTypeHolder.
        :rtype: str
        """
        return self._provider_version

    @provider_version.setter
    def provider_version(self, provider_version):
        """Sets the provider_version of this PrivateProviderVersionRequiredPrimitiveTypeHolder.

        provider的版本号。版本号必须遵循语义化版本号（Semantic Version），为用户自定义

        :param provider_version: The provider_version of this PrivateProviderVersionRequiredPrimitiveTypeHolder.
        :type provider_version: str
        """
        self._provider_version = provider_version

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
        if not isinstance(other, PrivateProviderVersionRequiredPrimitiveTypeHolder):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
