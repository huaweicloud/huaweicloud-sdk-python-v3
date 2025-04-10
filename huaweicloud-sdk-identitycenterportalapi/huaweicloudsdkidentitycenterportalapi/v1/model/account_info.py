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
        'account_id': 'str',
        'account_name': 'str',
        'email_address': 'str'
    }

    attribute_map = {
        'account_id': 'account_id',
        'account_name': 'account_name',
        'email_address': 'email_address'
    }

    def __init__(self, account_id=None, account_name=None, email_address=None):
        r"""AccountInfo

        The model defined in huaweicloud sdk

        :param account_id: 分配给用户的账号的全局唯一标识符（ID）
        :type account_id: str
        :param account_name: 分配给用户的账号的名称
        :type account_name: str
        :param email_address: 分配给用户的账号的电子邮箱地址
        :type email_address: str
        """
        
        

        self._account_id = None
        self._account_name = None
        self._email_address = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if account_name is not None:
            self.account_name = account_name
        if email_address is not None:
            self.email_address = email_address

    @property
    def account_id(self):
        r"""Gets the account_id of this AccountInfo.

        分配给用户的账号的全局唯一标识符（ID）

        :return: The account_id of this AccountInfo.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        r"""Sets the account_id of this AccountInfo.

        分配给用户的账号的全局唯一标识符（ID）

        :param account_id: The account_id of this AccountInfo.
        :type account_id: str
        """
        self._account_id = account_id

    @property
    def account_name(self):
        r"""Gets the account_name of this AccountInfo.

        分配给用户的账号的名称

        :return: The account_name of this AccountInfo.
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        r"""Sets the account_name of this AccountInfo.

        分配给用户的账号的名称

        :param account_name: The account_name of this AccountInfo.
        :type account_name: str
        """
        self._account_name = account_name

    @property
    def email_address(self):
        r"""Gets the email_address of this AccountInfo.

        分配给用户的账号的电子邮箱地址

        :return: The email_address of this AccountInfo.
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        r"""Sets the email_address of this AccountInfo.

        分配给用户的账号的电子邮箱地址

        :param email_address: The email_address of this AccountInfo.
        :type email_address: str
        """
        self._email_address = email_address

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
