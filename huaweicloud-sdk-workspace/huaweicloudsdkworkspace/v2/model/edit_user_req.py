# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EditUserReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'description': 'str',
        'user_email': 'str',
        'account_expires': 'str',
        'enable_change_password': 'bool',
        'next_login_change_password': 'bool',
        'password_never_expired': 'bool',
        'disabled': 'bool'
    }

    attribute_map = {
        'description': 'description',
        'user_email': 'user_email',
        'account_expires': 'account_expires',
        'enable_change_password': 'enable_change_password',
        'next_login_change_password': 'next_login_change_password',
        'password_never_expired': 'password_never_expired',
        'disabled': 'disabled'
    }

    def __init__(self, description=None, user_email=None, account_expires=None, enable_change_password=None, next_login_change_password=None, password_never_expired=None, disabled=None):
        """EditUserReq

        The model defined in huaweicloud sdk

        :param description: 用户描述。
        :type description: str
        :param user_email: 用户邮箱。
        :type user_email: str
        :param account_expires: 账户过期时间，0表示永远不过期。
        :type account_expires: str
        :param enable_change_password: 是否允许修改密码，true表示允许，false表示不允许。
        :type enable_change_password: bool
        :param next_login_change_password: 下次登录是否需要重置密码，true表示需要重置密码，false表示不需要。
        :type next_login_change_password: bool
        :param password_never_expired: 密码是否永不过期，true表示密码永不过期，false表示密码会过期。
        :type password_never_expired: bool
        :param disabled: 账户是否禁用，true表示被禁用，false表示未禁用。
        :type disabled: bool
        """
        
        

        self._description = None
        self._user_email = None
        self._account_expires = None
        self._enable_change_password = None
        self._next_login_change_password = None
        self._password_never_expired = None
        self._disabled = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if user_email is not None:
            self.user_email = user_email
        if account_expires is not None:
            self.account_expires = account_expires
        if enable_change_password is not None:
            self.enable_change_password = enable_change_password
        if next_login_change_password is not None:
            self.next_login_change_password = next_login_change_password
        if password_never_expired is not None:
            self.password_never_expired = password_never_expired
        if disabled is not None:
            self.disabled = disabled

    @property
    def description(self):
        """Gets the description of this EditUserReq.

        用户描述。

        :return: The description of this EditUserReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this EditUserReq.

        用户描述。

        :param description: The description of this EditUserReq.
        :type description: str
        """
        self._description = description

    @property
    def user_email(self):
        """Gets the user_email of this EditUserReq.

        用户邮箱。

        :return: The user_email of this EditUserReq.
        :rtype: str
        """
        return self._user_email

    @user_email.setter
    def user_email(self, user_email):
        """Sets the user_email of this EditUserReq.

        用户邮箱。

        :param user_email: The user_email of this EditUserReq.
        :type user_email: str
        """
        self._user_email = user_email

    @property
    def account_expires(self):
        """Gets the account_expires of this EditUserReq.

        账户过期时间，0表示永远不过期。

        :return: The account_expires of this EditUserReq.
        :rtype: str
        """
        return self._account_expires

    @account_expires.setter
    def account_expires(self, account_expires):
        """Sets the account_expires of this EditUserReq.

        账户过期时间，0表示永远不过期。

        :param account_expires: The account_expires of this EditUserReq.
        :type account_expires: str
        """
        self._account_expires = account_expires

    @property
    def enable_change_password(self):
        """Gets the enable_change_password of this EditUserReq.

        是否允许修改密码，true表示允许，false表示不允许。

        :return: The enable_change_password of this EditUserReq.
        :rtype: bool
        """
        return self._enable_change_password

    @enable_change_password.setter
    def enable_change_password(self, enable_change_password):
        """Sets the enable_change_password of this EditUserReq.

        是否允许修改密码，true表示允许，false表示不允许。

        :param enable_change_password: The enable_change_password of this EditUserReq.
        :type enable_change_password: bool
        """
        self._enable_change_password = enable_change_password

    @property
    def next_login_change_password(self):
        """Gets the next_login_change_password of this EditUserReq.

        下次登录是否需要重置密码，true表示需要重置密码，false表示不需要。

        :return: The next_login_change_password of this EditUserReq.
        :rtype: bool
        """
        return self._next_login_change_password

    @next_login_change_password.setter
    def next_login_change_password(self, next_login_change_password):
        """Sets the next_login_change_password of this EditUserReq.

        下次登录是否需要重置密码，true表示需要重置密码，false表示不需要。

        :param next_login_change_password: The next_login_change_password of this EditUserReq.
        :type next_login_change_password: bool
        """
        self._next_login_change_password = next_login_change_password

    @property
    def password_never_expired(self):
        """Gets the password_never_expired of this EditUserReq.

        密码是否永不过期，true表示密码永不过期，false表示密码会过期。

        :return: The password_never_expired of this EditUserReq.
        :rtype: bool
        """
        return self._password_never_expired

    @password_never_expired.setter
    def password_never_expired(self, password_never_expired):
        """Sets the password_never_expired of this EditUserReq.

        密码是否永不过期，true表示密码永不过期，false表示密码会过期。

        :param password_never_expired: The password_never_expired of this EditUserReq.
        :type password_never_expired: bool
        """
        self._password_never_expired = password_never_expired

    @property
    def disabled(self):
        """Gets the disabled of this EditUserReq.

        账户是否禁用，true表示被禁用，false表示未禁用。

        :return: The disabled of this EditUserReq.
        :rtype: bool
        """
        return self._disabled

    @disabled.setter
    def disabled(self, disabled):
        """Sets the disabled of this EditUserReq.

        账户是否禁用，true表示被禁用，false表示未禁用。

        :param disabled: The disabled of this EditUserReq.
        :type disabled: bool
        """
        self._disabled = disabled

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
        if not isinstance(other, EditUserReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
