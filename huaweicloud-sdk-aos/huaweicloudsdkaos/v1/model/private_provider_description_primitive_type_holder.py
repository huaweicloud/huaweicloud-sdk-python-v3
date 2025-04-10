# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PrivateProviderDescriptionPrimitiveTypeHolder:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'provider_description': 'str'
    }

    attribute_map = {
        'provider_description': 'provider_description'
    }

    def __init__(self, provider_description=None):
        r"""PrivateProviderDescriptionPrimitiveTypeHolder

        The model defined in huaweicloud sdk

        :param provider_description: 私有provider（private-provider）的描述。可用于客户识别被管理的私有provider。
        :type provider_description: str
        """
        
        

        self._provider_description = None
        self.discriminator = None

        if provider_description is not None:
            self.provider_description = provider_description

    @property
    def provider_description(self):
        r"""Gets the provider_description of this PrivateProviderDescriptionPrimitiveTypeHolder.

        私有provider（private-provider）的描述。可用于客户识别被管理的私有provider。

        :return: The provider_description of this PrivateProviderDescriptionPrimitiveTypeHolder.
        :rtype: str
        """
        return self._provider_description

    @provider_description.setter
    def provider_description(self, provider_description):
        r"""Sets the provider_description of this PrivateProviderDescriptionPrimitiveTypeHolder.

        私有provider（private-provider）的描述。可用于客户识别被管理的私有provider。

        :param provider_description: The provider_description of this PrivateProviderDescriptionPrimitiveTypeHolder.
        :type provider_description: str
        """
        self._provider_description = provider_description

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
        if not isinstance(other, PrivateProviderDescriptionPrimitiveTypeHolder):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
