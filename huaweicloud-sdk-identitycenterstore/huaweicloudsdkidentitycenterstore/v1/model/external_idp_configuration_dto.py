# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExternalIdpConfigurationDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'idp_certificate_ids': 'list[IdpCertificateBody]',
        'idp_id': 'str',
        'idp_saml_config': 'IdpSAMLConfig',
        'is_enabled': 'bool'
    }

    attribute_map = {
        'idp_certificate_ids': 'idp_certificate_ids',
        'idp_id': 'idp_id',
        'idp_saml_config': 'idp_saml_config',
        'is_enabled': 'is_enabled'
    }

    def __init__(self, idp_certificate_ids=None, idp_id=None, idp_saml_config=None, is_enabled=None):
        r"""ExternalIdpConfigurationDto

        The model defined in huaweicloud sdk

        :param idp_certificate_ids: 身份提供商证书对应的全局唯一标识符列表
        :type idp_certificate_ids: list[:class:`huaweicloudsdkidentitycenterstore.v1.IdpCertificateBody`]
        :param idp_id: 身份提供商对应的全局唯一标识符（ID）
        :type idp_id: str
        :param idp_saml_config: 
        :type idp_saml_config: :class:`huaweicloudsdkidentitycenterstore.v1.IdpSAMLConfig`
        :param is_enabled: 是否启用身份提供商
        :type is_enabled: bool
        """
        
        

        self._idp_certificate_ids = None
        self._idp_id = None
        self._idp_saml_config = None
        self._is_enabled = None
        self.discriminator = None

        self.idp_certificate_ids = idp_certificate_ids
        self.idp_id = idp_id
        self.idp_saml_config = idp_saml_config
        self.is_enabled = is_enabled

    @property
    def idp_certificate_ids(self):
        r"""Gets the idp_certificate_ids of this ExternalIdpConfigurationDto.

        身份提供商证书对应的全局唯一标识符列表

        :return: The idp_certificate_ids of this ExternalIdpConfigurationDto.
        :rtype: list[:class:`huaweicloudsdkidentitycenterstore.v1.IdpCertificateBody`]
        """
        return self._idp_certificate_ids

    @idp_certificate_ids.setter
    def idp_certificate_ids(self, idp_certificate_ids):
        r"""Sets the idp_certificate_ids of this ExternalIdpConfigurationDto.

        身份提供商证书对应的全局唯一标识符列表

        :param idp_certificate_ids: The idp_certificate_ids of this ExternalIdpConfigurationDto.
        :type idp_certificate_ids: list[:class:`huaweicloudsdkidentitycenterstore.v1.IdpCertificateBody`]
        """
        self._idp_certificate_ids = idp_certificate_ids

    @property
    def idp_id(self):
        r"""Gets the idp_id of this ExternalIdpConfigurationDto.

        身份提供商对应的全局唯一标识符（ID）

        :return: The idp_id of this ExternalIdpConfigurationDto.
        :rtype: str
        """
        return self._idp_id

    @idp_id.setter
    def idp_id(self, idp_id):
        r"""Sets the idp_id of this ExternalIdpConfigurationDto.

        身份提供商对应的全局唯一标识符（ID）

        :param idp_id: The idp_id of this ExternalIdpConfigurationDto.
        :type idp_id: str
        """
        self._idp_id = idp_id

    @property
    def idp_saml_config(self):
        r"""Gets the idp_saml_config of this ExternalIdpConfigurationDto.

        :return: The idp_saml_config of this ExternalIdpConfigurationDto.
        :rtype: :class:`huaweicloudsdkidentitycenterstore.v1.IdpSAMLConfig`
        """
        return self._idp_saml_config

    @idp_saml_config.setter
    def idp_saml_config(self, idp_saml_config):
        r"""Sets the idp_saml_config of this ExternalIdpConfigurationDto.

        :param idp_saml_config: The idp_saml_config of this ExternalIdpConfigurationDto.
        :type idp_saml_config: :class:`huaweicloudsdkidentitycenterstore.v1.IdpSAMLConfig`
        """
        self._idp_saml_config = idp_saml_config

    @property
    def is_enabled(self):
        r"""Gets the is_enabled of this ExternalIdpConfigurationDto.

        是否启用身份提供商

        :return: The is_enabled of this ExternalIdpConfigurationDto.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        r"""Sets the is_enabled of this ExternalIdpConfigurationDto.

        是否启用身份提供商

        :param is_enabled: The is_enabled of this ExternalIdpConfigurationDto.
        :type is_enabled: bool
        """
        self._is_enabled = is_enabled

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
        if not isinstance(other, ExternalIdpConfigurationDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
