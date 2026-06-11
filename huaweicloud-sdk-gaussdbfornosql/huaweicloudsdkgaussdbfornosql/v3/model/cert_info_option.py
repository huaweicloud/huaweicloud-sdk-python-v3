# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CertInfoOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cert_id': 'str',
        'cert_type': 'str'
    }

    attribute_map = {
        'cert_id': 'cert_id',
        'cert_type': 'cert_type'
    }

    def __init__(self, cert_id=None, cert_type=None):
        r"""CertInfoOption

        The model defined in huaweicloud sdk

        :param cert_id: **参数解释：** 证书ID。 **取值范围：** 根据CCM证书列表接口获取证书ID。
        :type cert_id: str
        :param cert_type: **参数解释：** 证书类型。 **取值范围：**   - PCA：CCM PCA 证书。   - SSL：CCM SSL 证书。
        :type cert_type: str
        """
        
        

        self._cert_id = None
        self._cert_type = None
        self.discriminator = None

        self.cert_id = cert_id
        self.cert_type = cert_type

    @property
    def cert_id(self):
        r"""Gets the cert_id of this CertInfoOption.

        **参数解释：** 证书ID。 **取值范围：** 根据CCM证书列表接口获取证书ID。

        :return: The cert_id of this CertInfoOption.
        :rtype: str
        """
        return self._cert_id

    @cert_id.setter
    def cert_id(self, cert_id):
        r"""Sets the cert_id of this CertInfoOption.

        **参数解释：** 证书ID。 **取值范围：** 根据CCM证书列表接口获取证书ID。

        :param cert_id: The cert_id of this CertInfoOption.
        :type cert_id: str
        """
        self._cert_id = cert_id

    @property
    def cert_type(self):
        r"""Gets the cert_type of this CertInfoOption.

        **参数解释：** 证书类型。 **取值范围：**   - PCA：CCM PCA 证书。   - SSL：CCM SSL 证书。

        :return: The cert_type of this CertInfoOption.
        :rtype: str
        """
        return self._cert_type

    @cert_type.setter
    def cert_type(self, cert_type):
        r"""Sets the cert_type of this CertInfoOption.

        **参数解释：** 证书类型。 **取值范围：**   - PCA：CCM PCA 证书。   - SSL：CCM SSL 证书。

        :param cert_type: The cert_type of this CertInfoOption.
        :type cert_type: str
        """
        self._cert_type = cert_type

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
        if not isinstance(other, CertInfoOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
