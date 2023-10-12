# coding: utf-8

import six

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
        'account_type': 'AccountTypeEnum',
        'domain': 'str',
        'email': 'str',
        'telephone_number': 'str'
    }

    attribute_map = {
        'account': 'account',
        'account_type': 'account_type',
        'domain': 'domain',
        'email': 'email',
        'telephone_number': 'telephone_number'
    }

    def __init__(self, account=None, account_type=None, domain=None, email=None, telephone_number=None):
        """AccountInfo

        The model defined in huaweicloud sdk

        :param account: 用户(组)
        :type account: str
        :param account_type: 
        :type account_type: :class:`huaweicloudsdkworkspaceapp.v1.AccountTypeEnum`
        :param domain: 域名城
        :type domain: str
        :param email: 邮箱
        :type email: str
        :param telephone_number: 手机
        :type telephone_number: str
        """
        
        

        self._account = None
        self._account_type = None
        self._domain = None
        self._email = None
        self._telephone_number = None
        self.discriminator = None

        self.account = account
        self.account_type = account_type
        if domain is not None:
            self.domain = domain
        if email is not None:
            self.email = email
        if telephone_number is not None:
            self.telephone_number = telephone_number

    @property
    def account(self):
        """Gets the account of this AccountInfo.

        用户(组)

        :return: The account of this AccountInfo.
        :rtype: str
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this AccountInfo.

        用户(组)

        :param account: The account of this AccountInfo.
        :type account: str
        """
        self._account = account

    @property
    def account_type(self):
        """Gets the account_type of this AccountInfo.

        :return: The account_type of this AccountInfo.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.AccountTypeEnum`
        """
        return self._account_type

    @account_type.setter
    def account_type(self, account_type):
        """Sets the account_type of this AccountInfo.

        :param account_type: The account_type of this AccountInfo.
        :type account_type: :class:`huaweicloudsdkworkspaceapp.v1.AccountTypeEnum`
        """
        self._account_type = account_type

    @property
    def domain(self):
        """Gets the domain of this AccountInfo.

        域名城

        :return: The domain of this AccountInfo.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this AccountInfo.

        域名城

        :param domain: The domain of this AccountInfo.
        :type domain: str
        """
        self._domain = domain

    @property
    def email(self):
        """Gets the email of this AccountInfo.

        邮箱

        :return: The email of this AccountInfo.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this AccountInfo.

        邮箱

        :param email: The email of this AccountInfo.
        :type email: str
        """
        self._email = email

    @property
    def telephone_number(self):
        """Gets the telephone_number of this AccountInfo.

        手机

        :return: The telephone_number of this AccountInfo.
        :rtype: str
        """
        return self._telephone_number

    @telephone_number.setter
    def telephone_number(self, telephone_number):
        """Sets the telephone_number of this AccountInfo.

        手机

        :param telephone_number: The telephone_number of this AccountInfo.
        :type telephone_number: str
        """
        self._telephone_number = telephone_number

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
        if not isinstance(other, AccountInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
