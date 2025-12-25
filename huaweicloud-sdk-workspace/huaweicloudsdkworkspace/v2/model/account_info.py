# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AccountInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'account': 'str',
        'domain': 'str',
        'account_type': 'str',
        'platform_type': 'str'
    }

    attribute_map = {
        'account': 'account',
        'domain': 'domain',
        'account_type': 'account_type',
        'platform_type': 'platform_type'
    }

    def __init__(self, account=None, domain=None, account_type=None, platform_type=None):
        r"""AccountInfo

        The model defined in huaweicloud sdk

        :param account: 账户，账户的格式必须为:账户(组)的形式。
        :type account: str
        :param domain: 域名(用户组必填，不填时使用默认值 local.com)。
        :type domain: str
        :param account_type: 账户类型： * &#39;SIMPLE&#39; - 普通用户 * &#39;USER_GROUP&#39; - 用户组
        :type account_type: str
        :param platform_type: 平台类型： * &#x60;AD&#x60; - AD域 * &#x60;LOCAL&#x60; - LiteAs
        :type platform_type: str
        """
        
        

        self._account = None
        self._domain = None
        self._account_type = None
        self._platform_type = None
        self.discriminator = None

        self.account = account
        if domain is not None:
            self.domain = domain
        self.account_type = account_type
        if platform_type is not None:
            self.platform_type = platform_type

    @property
    def account(self):
        r"""Gets the account of this AccountInfo.

        账户，账户的格式必须为:账户(组)的形式。

        :return: The account of this AccountInfo.
        :rtype: str
        """
        return self._account

    @account.setter
    def account(self, account):
        r"""Sets the account of this AccountInfo.

        账户，账户的格式必须为:账户(组)的形式。

        :param account: The account of this AccountInfo.
        :type account: str
        """
        self._account = account

    @property
    def domain(self):
        r"""Gets the domain of this AccountInfo.

        域名(用户组必填，不填时使用默认值 local.com)。

        :return: The domain of this AccountInfo.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        r"""Sets the domain of this AccountInfo.

        域名(用户组必填，不填时使用默认值 local.com)。

        :param domain: The domain of this AccountInfo.
        :type domain: str
        """
        self._domain = domain

    @property
    def account_type(self):
        r"""Gets the account_type of this AccountInfo.

        账户类型： * 'SIMPLE' - 普通用户 * 'USER_GROUP' - 用户组

        :return: The account_type of this AccountInfo.
        :rtype: str
        """
        return self._account_type

    @account_type.setter
    def account_type(self, account_type):
        r"""Sets the account_type of this AccountInfo.

        账户类型： * 'SIMPLE' - 普通用户 * 'USER_GROUP' - 用户组

        :param account_type: The account_type of this AccountInfo.
        :type account_type: str
        """
        self._account_type = account_type

    @property
    def platform_type(self):
        r"""Gets the platform_type of this AccountInfo.

        平台类型： * `AD` - AD域 * `LOCAL` - LiteAs

        :return: The platform_type of this AccountInfo.
        :rtype: str
        """
        return self._platform_type

    @platform_type.setter
    def platform_type(self, platform_type):
        r"""Sets the platform_type of this AccountInfo.

        平台类型： * `AD` - AD域 * `LOCAL` - LiteAs

        :param platform_type: The platform_type of this AccountInfo.
        :type platform_type: str
        """
        self._platform_type = platform_type

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
        if not isinstance(other, AccountInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
