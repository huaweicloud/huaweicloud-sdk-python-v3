# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AccountBaseline:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []
    sensitive_list.append('account_name')
    sensitive_list.append('account_id')
    sensitive_list.append('phone')
    sensitive_list.append('account_email')

    openapi_types = {
        'account_name': 'str',
        'account_id': 'str',
        'phone': 'str',
        'account_email': 'str',
        'account_type': 'str'
    }

    attribute_map = {
        'account_name': 'account_name',
        'account_id': 'account_id',
        'phone': 'phone',
        'account_email': 'account_email',
        'account_type': 'account_type'
    }

    def __init__(self, account_name=None, account_id=None, phone=None, account_email=None, account_type=None):
        r"""AccountBaseline

        The model defined in huaweicloud sdk

        :param account_name: 纳管账号名称。
        :type account_name: str
        :param account_id: 纳管账号的唯一标识符（ID）。
        :type account_id: str
        :param phone: 手机号码。
        :type phone: str
        :param account_email: 纳管账号邮箱。
        :type account_email: str
        :param account_type: 纳管账号类型。类型包括LOGGING，SECURITY。
        :type account_type: str
        """
        
        

        self._account_name = None
        self._account_id = None
        self._phone = None
        self._account_email = None
        self._account_type = None
        self.discriminator = None

        self.account_name = account_name
        if account_id is not None:
            self.account_id = account_id
        if phone is not None:
            self.phone = phone
        if account_email is not None:
            self.account_email = account_email
        self.account_type = account_type

    @property
    def account_name(self):
        r"""Gets the account_name of this AccountBaseline.

        纳管账号名称。

        :return: The account_name of this AccountBaseline.
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        r"""Sets the account_name of this AccountBaseline.

        纳管账号名称。

        :param account_name: The account_name of this AccountBaseline.
        :type account_name: str
        """
        self._account_name = account_name

    @property
    def account_id(self):
        r"""Gets the account_id of this AccountBaseline.

        纳管账号的唯一标识符（ID）。

        :return: The account_id of this AccountBaseline.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        r"""Sets the account_id of this AccountBaseline.

        纳管账号的唯一标识符（ID）。

        :param account_id: The account_id of this AccountBaseline.
        :type account_id: str
        """
        self._account_id = account_id

    @property
    def phone(self):
        r"""Gets the phone of this AccountBaseline.

        手机号码。

        :return: The phone of this AccountBaseline.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        r"""Sets the phone of this AccountBaseline.

        手机号码。

        :param phone: The phone of this AccountBaseline.
        :type phone: str
        """
        self._phone = phone

    @property
    def account_email(self):
        r"""Gets the account_email of this AccountBaseline.

        纳管账号邮箱。

        :return: The account_email of this AccountBaseline.
        :rtype: str
        """
        return self._account_email

    @account_email.setter
    def account_email(self, account_email):
        r"""Sets the account_email of this AccountBaseline.

        纳管账号邮箱。

        :param account_email: The account_email of this AccountBaseline.
        :type account_email: str
        """
        self._account_email = account_email

    @property
    def account_type(self):
        r"""Gets the account_type of this AccountBaseline.

        纳管账号类型。类型包括LOGGING，SECURITY。

        :return: The account_type of this AccountBaseline.
        :rtype: str
        """
        return self._account_type

    @account_type.setter
    def account_type(self, account_type):
        r"""Sets the account_type of this AccountBaseline.

        纳管账号类型。类型包括LOGGING，SECURITY。

        :param account_type: The account_type of this AccountBaseline.
        :type account_type: str
        """
        self._account_type = account_type

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
        if not isinstance(other, AccountBaseline):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
