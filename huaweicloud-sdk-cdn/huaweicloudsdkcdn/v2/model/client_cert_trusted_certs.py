# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClientCertTrustedCerts:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'trusted_cert': 'str'
    }

    attribute_map = {
        'trusted_cert': 'trusted_cert'
    }

    def __init__(self, trusted_cert=None):
        r"""ClientCertTrustedCerts

        The model defined in huaweicloud sdk

        :param trusted_cert: **参数解释：** 客户端CA证书的内容 **约束限制：** 仅支持PEM格式 **取值范围：** 不涉及
        :type trusted_cert: str
        """
        
        

        self._trusted_cert = None
        self.discriminator = None

        if trusted_cert is not None:
            self.trusted_cert = trusted_cert

    @property
    def trusted_cert(self):
        r"""Gets the trusted_cert of this ClientCertTrustedCerts.

        **参数解释：** 客户端CA证书的内容 **约束限制：** 仅支持PEM格式 **取值范围：** 不涉及

        :return: The trusted_cert of this ClientCertTrustedCerts.
        :rtype: str
        """
        return self._trusted_cert

    @trusted_cert.setter
    def trusted_cert(self, trusted_cert):
        r"""Sets the trusted_cert of this ClientCertTrustedCerts.

        **参数解释：** 客户端CA证书的内容 **约束限制：** 仅支持PEM格式 **取值范围：** 不涉及

        :param trusted_cert: The trusted_cert of this ClientCertTrustedCerts.
        :type trusted_cert: str
        """
        self._trusted_cert = trusted_cert

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ClientCertTrustedCerts):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
