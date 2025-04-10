# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProviderAgencyUrnPrimitiveTypeHolder:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'provider_agency_urn': 'str'
    }

    attribute_map = {
        'provider_agency_urn': 'provider_agency_urn'
    }

    def __init__(self, provider_agency_urn=None):
        r"""ProviderAgencyUrnPrimitiveTypeHolder

        The model defined in huaweicloud sdk

        :param provider_agency_urn: 自定义provider所绑定的IAM委托URN，provider_agency_name和provider_agency_urn最多只能提供一个。
        :type provider_agency_urn: str
        """
        
        

        self._provider_agency_urn = None
        self.discriminator = None

        if provider_agency_urn is not None:
            self.provider_agency_urn = provider_agency_urn

    @property
    def provider_agency_urn(self):
        r"""Gets the provider_agency_urn of this ProviderAgencyUrnPrimitiveTypeHolder.

        自定义provider所绑定的IAM委托URN，provider_agency_name和provider_agency_urn最多只能提供一个。

        :return: The provider_agency_urn of this ProviderAgencyUrnPrimitiveTypeHolder.
        :rtype: str
        """
        return self._provider_agency_urn

    @provider_agency_urn.setter
    def provider_agency_urn(self, provider_agency_urn):
        r"""Sets the provider_agency_urn of this ProviderAgencyUrnPrimitiveTypeHolder.

        自定义provider所绑定的IAM委托URN，provider_agency_name和provider_agency_urn最多只能提供一个。

        :param provider_agency_urn: The provider_agency_urn of this ProviderAgencyUrnPrimitiveTypeHolder.
        :type provider_agency_urn: str
        """
        self._provider_agency_urn = provider_agency_urn

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
        if not isinstance(other, ProviderAgencyUrnPrimitiveTypeHolder):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
