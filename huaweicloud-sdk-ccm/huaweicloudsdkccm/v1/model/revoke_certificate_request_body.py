# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RevokeCertificateRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'reason': 'str'
    }

    attribute_map = {
        'reason': 'reason'
    }

    def __init__(self, reason=None):
        """RevokeCertificateRequestBody

        The model defined in huaweicloud sdk

        :param reason: 吊销理由，支持以下选项：   - **UNSPECIFIED** : 吊销时未指定吊销原因，为默认值；   - **KEY_COMPROMISE** : 证书密钥材料泄露；   - **CERTIFICATE_AUTHORITY_COMPROMISE** : 颁发路径上，可能存在CA密钥材料泄露；   - **AFFILIATION_CHANGED** : 证书中的主体或其他信息已经被改变；   - **SUPERSEDED** : 此证书已被取代；   - **CESSATION_OF_OPERATION** : 此证书或颁发路径中的实体已停止运营；   - **CERTIFICATE_HOLD** : 该证书当前不应被视为有效，预计将来可能会生效；   - **PRIVILEGE_WITHDRAWN** : 此证书不再具备其声明的属性的权限；   - **ATTRIBUTE_AUTHORITY_COMPROMISE** : 担保此证书属性的机构可能已受到损害。 &gt; 当不想填写吊销理由时，请求body体请置为\&quot;{}\&quot;，否则将会报异常，默认值为UNSPECIFIED。
        :type reason: str
        """
        
        

        self._reason = None
        self.discriminator = None

        if reason is not None:
            self.reason = reason

    @property
    def reason(self):
        """Gets the reason of this RevokeCertificateRequestBody.

        吊销理由，支持以下选项：   - **UNSPECIFIED** : 吊销时未指定吊销原因，为默认值；   - **KEY_COMPROMISE** : 证书密钥材料泄露；   - **CERTIFICATE_AUTHORITY_COMPROMISE** : 颁发路径上，可能存在CA密钥材料泄露；   - **AFFILIATION_CHANGED** : 证书中的主体或其他信息已经被改变；   - **SUPERSEDED** : 此证书已被取代；   - **CESSATION_OF_OPERATION** : 此证书或颁发路径中的实体已停止运营；   - **CERTIFICATE_HOLD** : 该证书当前不应被视为有效，预计将来可能会生效；   - **PRIVILEGE_WITHDRAWN** : 此证书不再具备其声明的属性的权限；   - **ATTRIBUTE_AUTHORITY_COMPROMISE** : 担保此证书属性的机构可能已受到损害。 > 当不想填写吊销理由时，请求body体请置为\"{}\"，否则将会报异常，默认值为UNSPECIFIED。

        :return: The reason of this RevokeCertificateRequestBody.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this RevokeCertificateRequestBody.

        吊销理由，支持以下选项：   - **UNSPECIFIED** : 吊销时未指定吊销原因，为默认值；   - **KEY_COMPROMISE** : 证书密钥材料泄露；   - **CERTIFICATE_AUTHORITY_COMPROMISE** : 颁发路径上，可能存在CA密钥材料泄露；   - **AFFILIATION_CHANGED** : 证书中的主体或其他信息已经被改变；   - **SUPERSEDED** : 此证书已被取代；   - **CESSATION_OF_OPERATION** : 此证书或颁发路径中的实体已停止运营；   - **CERTIFICATE_HOLD** : 该证书当前不应被视为有效，预计将来可能会生效；   - **PRIVILEGE_WITHDRAWN** : 此证书不再具备其声明的属性的权限；   - **ATTRIBUTE_AUTHORITY_COMPROMISE** : 担保此证书属性的机构可能已受到损害。 > 当不想填写吊销理由时，请求body体请置为\"{}\"，否则将会报异常，默认值为UNSPECIFIED。

        :param reason: The reason of this RevokeCertificateRequestBody.
        :type reason: str
        """
        self._reason = reason

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
        if not isinstance(other, RevokeCertificateRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
