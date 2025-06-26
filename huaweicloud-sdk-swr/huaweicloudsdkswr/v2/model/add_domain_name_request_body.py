# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddDomainNameRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_name': 'str',
        'certificate_id': 'str'
    }

    attribute_map = {
        'domain_name': 'domain_name',
        'certificate_id': 'certificate_id'
    }

    def __init__(self, domain_name=None, certificate_id=None):
        r"""AddDomainNameRequestBody

        The model defined in huaweicloud sdk

        :param domain_name: 域名，只能由字母、数字、中划线、星号组成， 星号只能在开头，中划线不能在开头或末 尾，至少包含两个字符串，单个字符串不 超过63个字符，字符串间以点分割，且总 长度不超过100个字符。例如： example.com 或 *example.com。
        :type domain_name: str
        :param certificate_id: SCM服务的证书ID
        :type certificate_id: str
        """
        
        

        self._domain_name = None
        self._certificate_id = None
        self.discriminator = None

        self.domain_name = domain_name
        self.certificate_id = certificate_id

    @property
    def domain_name(self):
        r"""Gets the domain_name of this AddDomainNameRequestBody.

        域名，只能由字母、数字、中划线、星号组成， 星号只能在开头，中划线不能在开头或末 尾，至少包含两个字符串，单个字符串不 超过63个字符，字符串间以点分割，且总 长度不超过100个字符。例如： example.com 或 *example.com。

        :return: The domain_name of this AddDomainNameRequestBody.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this AddDomainNameRequestBody.

        域名，只能由字母、数字、中划线、星号组成， 星号只能在开头，中划线不能在开头或末 尾，至少包含两个字符串，单个字符串不 超过63个字符，字符串间以点分割，且总 长度不超过100个字符。例如： example.com 或 *example.com。

        :param domain_name: The domain_name of this AddDomainNameRequestBody.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def certificate_id(self):
        r"""Gets the certificate_id of this AddDomainNameRequestBody.

        SCM服务的证书ID

        :return: The certificate_id of this AddDomainNameRequestBody.
        :rtype: str
        """
        return self._certificate_id

    @certificate_id.setter
    def certificate_id(self, certificate_id):
        r"""Sets the certificate_id of this AddDomainNameRequestBody.

        SCM服务的证书ID

        :param certificate_id: The certificate_id of this AddDomainNameRequestBody.
        :type certificate_id: str
        """
        self._certificate_id = certificate_id

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
        if not isinstance(other, AddDomainNameRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
