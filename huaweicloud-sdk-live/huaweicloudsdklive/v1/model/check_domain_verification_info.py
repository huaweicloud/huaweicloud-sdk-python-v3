# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckDomainVerificationInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain': 'str',
        'verify_type': 'str'
    }

    attribute_map = {
        'domain': 'domain',
        'verify_type': 'verify_type'
    }

    def __init__(self, domain=None, verify_type=None):
        r"""CheckDomainVerificationInfo

        The model defined in huaweicloud sdk

        :param domain: 直播域名
        :type domain: str
        :param verify_type: 验证方式，DNS：DNS解析验证；FILE：文件验证
        :type verify_type: str
        """
        
        

        self._domain = None
        self._verify_type = None
        self.discriminator = None

        self.domain = domain
        self.verify_type = verify_type

    @property
    def domain(self):
        r"""Gets the domain of this CheckDomainVerificationInfo.

        直播域名

        :return: The domain of this CheckDomainVerificationInfo.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        r"""Sets the domain of this CheckDomainVerificationInfo.

        直播域名

        :param domain: The domain of this CheckDomainVerificationInfo.
        :type domain: str
        """
        self._domain = domain

    @property
    def verify_type(self):
        r"""Gets the verify_type of this CheckDomainVerificationInfo.

        验证方式，DNS：DNS解析验证；FILE：文件验证

        :return: The verify_type of this CheckDomainVerificationInfo.
        :rtype: str
        """
        return self._verify_type

    @verify_type.setter
    def verify_type(self, verify_type):
        r"""Sets the verify_type of this CheckDomainVerificationInfo.

        验证方式，DNS：DNS解析验证；FILE：文件验证

        :param verify_type: The verify_type of this CheckDomainVerificationInfo.
        :type verify_type: str
        """
        self._verify_type = verify_type

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
        if not isinstance(other, CheckDomainVerificationInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
