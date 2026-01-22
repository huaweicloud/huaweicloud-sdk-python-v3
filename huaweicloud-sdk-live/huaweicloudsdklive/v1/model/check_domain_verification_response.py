# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckDomainVerificationResponse(SdkResponse):

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
        'verify_content': 'str',
        'verify_result': 'bool'
    }

    attribute_map = {
        'domain': 'domain',
        'verify_content': 'verify_content',
        'verify_result': 'verify_result'
    }

    def __init__(self, domain=None, verify_content=None, verify_result=None):
        r"""CheckDomainVerificationResponse

        The model defined in huaweicloud sdk

        :param domain: 主域名
        :type domain: str
        :param verify_content: 校验值，解析值或者文件内容
        :type verify_content: str
        :param verify_result: 验证结果，true为验证成功确认归属，false为归属情况未确认
        :type verify_result: bool
        """
        
        super().__init__()

        self._domain = None
        self._verify_content = None
        self._verify_result = None
        self.discriminator = None

        if domain is not None:
            self.domain = domain
        if verify_content is not None:
            self.verify_content = verify_content
        if verify_result is not None:
            self.verify_result = verify_result

    @property
    def domain(self):
        r"""Gets the domain of this CheckDomainVerificationResponse.

        主域名

        :return: The domain of this CheckDomainVerificationResponse.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        r"""Sets the domain of this CheckDomainVerificationResponse.

        主域名

        :param domain: The domain of this CheckDomainVerificationResponse.
        :type domain: str
        """
        self._domain = domain

    @property
    def verify_content(self):
        r"""Gets the verify_content of this CheckDomainVerificationResponse.

        校验值，解析值或者文件内容

        :return: The verify_content of this CheckDomainVerificationResponse.
        :rtype: str
        """
        return self._verify_content

    @verify_content.setter
    def verify_content(self, verify_content):
        r"""Sets the verify_content of this CheckDomainVerificationResponse.

        校验值，解析值或者文件内容

        :param verify_content: The verify_content of this CheckDomainVerificationResponse.
        :type verify_content: str
        """
        self._verify_content = verify_content

    @property
    def verify_result(self):
        r"""Gets the verify_result of this CheckDomainVerificationResponse.

        验证结果，true为验证成功确认归属，false为归属情况未确认

        :return: The verify_result of this CheckDomainVerificationResponse.
        :rtype: bool
        """
        return self._verify_result

    @verify_result.setter
    def verify_result(self, verify_result):
        r"""Sets the verify_result of this CheckDomainVerificationResponse.

        验证结果，true为验证成功确认归属，false为归属情况未确认

        :param verify_result: The verify_result of this CheckDomainVerificationResponse.
        :type verify_result: bool
        """
        self._verify_result = verify_result

    def to_dict(self):
        import warnings
        warnings.warn("CheckDomainVerificationResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, CheckDomainVerificationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
