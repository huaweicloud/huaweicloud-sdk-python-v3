# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateExternalIdPConfigurationForDirectoryResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'hws_sp_saml_config': 'SPSAMLConfig',
        'idp_certificate_id': 'str',
        'idp_certificate_ids': 'list[str]',
        'idp_id': 'str'
    }

    attribute_map = {
        'hws_sp_saml_config': 'hws_sp_saml_config',
        'idp_certificate_id': 'idp_certificate_id',
        'idp_certificate_ids': 'idp_certificate_ids',
        'idp_id': 'idp_id'
    }

    def __init__(self, hws_sp_saml_config=None, idp_certificate_id=None, idp_certificate_ids=None, idp_id=None):
        r"""CreateExternalIdPConfigurationForDirectoryResponse

        The model defined in huaweicloud sdk

        :param hws_sp_saml_config: 
        :type hws_sp_saml_config: :class:`huaweicloudsdkidentitycenterstore.v1.SPSAMLConfig`
        :param idp_certificate_id: 身份提供商证书全局唯一标识符（ID)
        :type idp_certificate_id: str
        :param idp_certificate_ids: 身份提供商证书全局唯一标识符列表
        :type idp_certificate_ids: list[str]
        :param idp_id: 外部身份提供商的全局唯一标识符（ID）
        :type idp_id: str
        """
        
        super(CreateExternalIdPConfigurationForDirectoryResponse, self).__init__()

        self._hws_sp_saml_config = None
        self._idp_certificate_id = None
        self._idp_certificate_ids = None
        self._idp_id = None
        self.discriminator = None

        if hws_sp_saml_config is not None:
            self.hws_sp_saml_config = hws_sp_saml_config
        if idp_certificate_id is not None:
            self.idp_certificate_id = idp_certificate_id
        if idp_certificate_ids is not None:
            self.idp_certificate_ids = idp_certificate_ids
        if idp_id is not None:
            self.idp_id = idp_id

    @property
    def hws_sp_saml_config(self):
        r"""Gets the hws_sp_saml_config of this CreateExternalIdPConfigurationForDirectoryResponse.

        :return: The hws_sp_saml_config of this CreateExternalIdPConfigurationForDirectoryResponse.
        :rtype: :class:`huaweicloudsdkidentitycenterstore.v1.SPSAMLConfig`
        """
        return self._hws_sp_saml_config

    @hws_sp_saml_config.setter
    def hws_sp_saml_config(self, hws_sp_saml_config):
        r"""Sets the hws_sp_saml_config of this CreateExternalIdPConfigurationForDirectoryResponse.

        :param hws_sp_saml_config: The hws_sp_saml_config of this CreateExternalIdPConfigurationForDirectoryResponse.
        :type hws_sp_saml_config: :class:`huaweicloudsdkidentitycenterstore.v1.SPSAMLConfig`
        """
        self._hws_sp_saml_config = hws_sp_saml_config

    @property
    def idp_certificate_id(self):
        r"""Gets the idp_certificate_id of this CreateExternalIdPConfigurationForDirectoryResponse.

        身份提供商证书全局唯一标识符（ID)

        :return: The idp_certificate_id of this CreateExternalIdPConfigurationForDirectoryResponse.
        :rtype: str
        """
        return self._idp_certificate_id

    @idp_certificate_id.setter
    def idp_certificate_id(self, idp_certificate_id):
        r"""Sets the idp_certificate_id of this CreateExternalIdPConfigurationForDirectoryResponse.

        身份提供商证书全局唯一标识符（ID)

        :param idp_certificate_id: The idp_certificate_id of this CreateExternalIdPConfigurationForDirectoryResponse.
        :type idp_certificate_id: str
        """
        self._idp_certificate_id = idp_certificate_id

    @property
    def idp_certificate_ids(self):
        r"""Gets the idp_certificate_ids of this CreateExternalIdPConfigurationForDirectoryResponse.

        身份提供商证书全局唯一标识符列表

        :return: The idp_certificate_ids of this CreateExternalIdPConfigurationForDirectoryResponse.
        :rtype: list[str]
        """
        return self._idp_certificate_ids

    @idp_certificate_ids.setter
    def idp_certificate_ids(self, idp_certificate_ids):
        r"""Sets the idp_certificate_ids of this CreateExternalIdPConfigurationForDirectoryResponse.

        身份提供商证书全局唯一标识符列表

        :param idp_certificate_ids: The idp_certificate_ids of this CreateExternalIdPConfigurationForDirectoryResponse.
        :type idp_certificate_ids: list[str]
        """
        self._idp_certificate_ids = idp_certificate_ids

    @property
    def idp_id(self):
        r"""Gets the idp_id of this CreateExternalIdPConfigurationForDirectoryResponse.

        外部身份提供商的全局唯一标识符（ID）

        :return: The idp_id of this CreateExternalIdPConfigurationForDirectoryResponse.
        :rtype: str
        """
        return self._idp_id

    @idp_id.setter
    def idp_id(self, idp_id):
        r"""Sets the idp_id of this CreateExternalIdPConfigurationForDirectoryResponse.

        外部身份提供商的全局唯一标识符（ID）

        :param idp_id: The idp_id of this CreateExternalIdPConfigurationForDirectoryResponse.
        :type idp_id: str
        """
        self._idp_id = idp_id

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
        if not isinstance(other, CreateExternalIdPConfigurationForDirectoryResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
