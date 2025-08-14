# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetSpConfigurationForDirectoryResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sp_oidc_config': 'SPOIDCConfig',
        'sp_saml_config': 'SPSAMLConfig'
    }

    attribute_map = {
        'sp_oidc_config': 'sp_oidc_config',
        'sp_saml_config': 'sp_saml_config'
    }

    def __init__(self, sp_oidc_config=None, sp_saml_config=None):
        r"""GetSpConfigurationForDirectoryResponse

        The model defined in huaweicloud sdk

        :param sp_oidc_config: 
        :type sp_oidc_config: :class:`huaweicloudsdkidentitycenterstore.v1.SPOIDCConfig`
        :param sp_saml_config: 
        :type sp_saml_config: :class:`huaweicloudsdkidentitycenterstore.v1.SPSAMLConfig`
        """
        
        super(GetSpConfigurationForDirectoryResponse, self).__init__()

        self._sp_oidc_config = None
        self._sp_saml_config = None
        self.discriminator = None

        if sp_oidc_config is not None:
            self.sp_oidc_config = sp_oidc_config
        if sp_saml_config is not None:
            self.sp_saml_config = sp_saml_config

    @property
    def sp_oidc_config(self):
        r"""Gets the sp_oidc_config of this GetSpConfigurationForDirectoryResponse.

        :return: The sp_oidc_config of this GetSpConfigurationForDirectoryResponse.
        :rtype: :class:`huaweicloudsdkidentitycenterstore.v1.SPOIDCConfig`
        """
        return self._sp_oidc_config

    @sp_oidc_config.setter
    def sp_oidc_config(self, sp_oidc_config):
        r"""Sets the sp_oidc_config of this GetSpConfigurationForDirectoryResponse.

        :param sp_oidc_config: The sp_oidc_config of this GetSpConfigurationForDirectoryResponse.
        :type sp_oidc_config: :class:`huaweicloudsdkidentitycenterstore.v1.SPOIDCConfig`
        """
        self._sp_oidc_config = sp_oidc_config

    @property
    def sp_saml_config(self):
        r"""Gets the sp_saml_config of this GetSpConfigurationForDirectoryResponse.

        :return: The sp_saml_config of this GetSpConfigurationForDirectoryResponse.
        :rtype: :class:`huaweicloudsdkidentitycenterstore.v1.SPSAMLConfig`
        """
        return self._sp_saml_config

    @sp_saml_config.setter
    def sp_saml_config(self, sp_saml_config):
        r"""Sets the sp_saml_config of this GetSpConfigurationForDirectoryResponse.

        :param sp_saml_config: The sp_saml_config of this GetSpConfigurationForDirectoryResponse.
        :type sp_saml_config: :class:`huaweicloudsdkidentitycenterstore.v1.SPSAMLConfig`
        """
        self._sp_saml_config = sp_saml_config

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
        if not isinstance(other, GetSpConfigurationForDirectoryResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
