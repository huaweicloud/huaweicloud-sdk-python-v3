# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateIDPReqBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'idp_saml_metadata': 'str',
        'idp_certificate': 'str',
        'idp_saml_config': 'object'
    }

    attribute_map = {
        'idp_saml_metadata': 'idp_saml_metadata',
        'idp_certificate': 'idp_certificate',
        'idp_saml_config': 'idp_saml_config'
    }

    def __init__(self, idp_saml_metadata=None, idp_certificate=None, idp_saml_config=None):
        r"""CreateIDPReqBody

        The model defined in huaweicloud sdk

        :param idp_saml_metadata: 身份提供商SAML元数据，与身份提供商SAML配置二选一
        :type idp_saml_metadata: str
        :param idp_certificate: 身份提供商证书，与身份提供商SAML配置联合使用
        :type idp_certificate: str
        :param idp_saml_config: 身份提供商SAML配置信息，与身份提供商SAML元数据二选一
        :type idp_saml_config: :class:`huaweicloudsdkidentitycenterstore.v1.object`
        """
        
        

        self._idp_saml_metadata = None
        self._idp_certificate = None
        self._idp_saml_config = None
        self.discriminator = None

        if idp_saml_metadata is not None:
            self.idp_saml_metadata = idp_saml_metadata
        if idp_certificate is not None:
            self.idp_certificate = idp_certificate
        if idp_saml_config is not None:
            self.idp_saml_config = idp_saml_config

    @property
    def idp_saml_metadata(self):
        r"""Gets the idp_saml_metadata of this CreateIDPReqBody.

        身份提供商SAML元数据，与身份提供商SAML配置二选一

        :return: The idp_saml_metadata of this CreateIDPReqBody.
        :rtype: str
        """
        return self._idp_saml_metadata

    @idp_saml_metadata.setter
    def idp_saml_metadata(self, idp_saml_metadata):
        r"""Sets the idp_saml_metadata of this CreateIDPReqBody.

        身份提供商SAML元数据，与身份提供商SAML配置二选一

        :param idp_saml_metadata: The idp_saml_metadata of this CreateIDPReqBody.
        :type idp_saml_metadata: str
        """
        self._idp_saml_metadata = idp_saml_metadata

    @property
    def idp_certificate(self):
        r"""Gets the idp_certificate of this CreateIDPReqBody.

        身份提供商证书，与身份提供商SAML配置联合使用

        :return: The idp_certificate of this CreateIDPReqBody.
        :rtype: str
        """
        return self._idp_certificate

    @idp_certificate.setter
    def idp_certificate(self, idp_certificate):
        r"""Sets the idp_certificate of this CreateIDPReqBody.

        身份提供商证书，与身份提供商SAML配置联合使用

        :param idp_certificate: The idp_certificate of this CreateIDPReqBody.
        :type idp_certificate: str
        """
        self._idp_certificate = idp_certificate

    @property
    def idp_saml_config(self):
        r"""Gets the idp_saml_config of this CreateIDPReqBody.

        身份提供商SAML配置信息，与身份提供商SAML元数据二选一

        :return: The idp_saml_config of this CreateIDPReqBody.
        :rtype: :class:`huaweicloudsdkidentitycenterstore.v1.object`
        """
        return self._idp_saml_config

    @idp_saml_config.setter
    def idp_saml_config(self, idp_saml_config):
        r"""Sets the idp_saml_config of this CreateIDPReqBody.

        身份提供商SAML配置信息，与身份提供商SAML元数据二选一

        :param idp_saml_config: The idp_saml_config of this CreateIDPReqBody.
        :type idp_saml_config: :class:`huaweicloudsdkidentitycenterstore.v1.object`
        """
        self._idp_saml_config = idp_saml_config

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
        if not isinstance(other, CreateIDPReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
