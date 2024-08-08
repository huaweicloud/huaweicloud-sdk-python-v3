# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImageAccountInfo:

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
        'account_type': 'str',
        'domain': 'str'
    }

    attribute_map = {
        'account': 'account',
        'account_type': 'account_type',
        'domain': 'domain'
    }

    def __init__(self, account=None, account_type=None, domain=None):
        """ImageAccountInfo

        The model defined in huaweicloud sdk

        :param account: 用户(组)。
        :type account: str
        :param account_type: 用户类型： * &#x60;USER&#x60; - 用户 * &#x60;USER_GROUP&#x60; - 用户组
        :type account_type: str
        :param domain: 域名城。
        :type domain: str
        """
        
        

        self._account = None
        self._account_type = None
        self._domain = None
        self.discriminator = None

        self.account = account
        self.account_type = account_type
        if domain is not None:
            self.domain = domain

    @property
    def account(self):
        """Gets the account of this ImageAccountInfo.

        用户(组)。

        :return: The account of this ImageAccountInfo.
        :rtype: str
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this ImageAccountInfo.

        用户(组)。

        :param account: The account of this ImageAccountInfo.
        :type account: str
        """
        self._account = account

    @property
    def account_type(self):
        """Gets the account_type of this ImageAccountInfo.

        用户类型： * `USER` - 用户 * `USER_GROUP` - 用户组

        :return: The account_type of this ImageAccountInfo.
        :rtype: str
        """
        return self._account_type

    @account_type.setter
    def account_type(self, account_type):
        """Sets the account_type of this ImageAccountInfo.

        用户类型： * `USER` - 用户 * `USER_GROUP` - 用户组

        :param account_type: The account_type of this ImageAccountInfo.
        :type account_type: str
        """
        self._account_type = account_type

    @property
    def domain(self):
        """Gets the domain of this ImageAccountInfo.

        域名城。

        :return: The domain of this ImageAccountInfo.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this ImageAccountInfo.

        域名城。

        :param domain: The domain of this ImageAccountInfo.
        :type domain: str
        """
        self._domain = domain

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
        if not isinstance(other, ImageAccountInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
