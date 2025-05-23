# coding: utf-8

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
        'user_phone': 'str',
        'active_type': 'str',
        'account_expires': 'str',
        'enable_change_password': 'bool',
        'next_login_change_password': 'bool',
        'group_ids': 'list[str]',
        'alias_name': 'str',
        'password_never_expired': 'bool',
        'disabled': 'bool'
    }

    attribute_map = {
        'description': 'description',
        'user_email': 'user_email',
        'user_phone': 'user_phone',
        'active_type': 'active_type',
        'account_expires': 'account_expires',
        'enable_change_password': 'enable_change_password',
        'next_login_change_password': 'next_login_change_password',
        'group_ids': 'group_ids',
        'alias_name': 'alias_name',
        'password_never_expired': 'password_never_expired',
        'disabled': 'disabled'
    }

    def __init__(self, description=None, user_email=None, user_phone=None, active_type=None, account_expires=None, enable_change_password=None, next_login_change_password=None, group_ids=None, alias_name=None, password_never_expired=None, disabled=None):
        r"""EditUserReq

        The model defined in huaweicloud sdk

        :param description: 用户描述。
        :type description: str
        :param user_email: 用户邮箱。
        :type user_email: str
        :param user_phone: 手机号。
        :type user_phone: str
        :param active_type: 激活类型，默认为用户激活。 * USER_ACTIVATE： 用户激活 * ADMIN_ACTIVATE： 管理员激活
        :type active_type: str
        :param account_expires: 账户过期时间，0表示永远不过期。
        :type account_expires: str
        :param enable_change_password: 是否允许修改密码，true表示允许，false表示不允许。
        :type enable_change_password: bool
        :param next_login_change_password: 下次登录是否需要重置密码，true表示需要重置密码，false表示不需要。
        :type next_login_change_password: bool
        :param group_ids: 用户组的专有ID列表。
        :type group_ids: list[str]
        :param alias_name: 别名。
        :type alias_name: str
        :param password_never_expired: 密码是否永不过期，true表示密码永不过期，false表示密码会过期。
        :type password_never_expired: bool
        :param disabled: 账户是否禁用，true表示被禁用，false表示未禁用。
        :type disabled: bool
        """
        
        

        self._description = None
        self._user_email = None
        self._user_phone = None
        self._active_type = None
        self._account_expires = None
        self._enable_change_password = None
        self._next_login_change_password = None
        self._group_ids = None
        self._alias_name = None
        self._password_never_expired = None
        self._disabled = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if user_email is not None:
            self.user_email = user_email
        if user_phone is not None:
            self.user_phone = user_phone
        if active_type is not None:
            self.active_type = active_type
        if account_expires is not None:
            self.account_expires = account_expires
        if enable_change_password is not None:
            self.enable_change_password = enable_change_password
        if next_login_change_password is not None:
            self.next_login_change_password = next_login_change_password
        if group_ids is not None:
            self.group_ids = group_ids
        if alias_name is not None:
            self.alias_name = alias_name
        if password_never_expired is not None:
            self.password_never_expired = password_never_expired
        if disabled is not None:
            self.disabled = disabled

    @property
    def description(self):
        r"""Gets the description of this EditUserReq.

        用户描述。

        :return: The description of this EditUserReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this EditUserReq.

        用户描述。

        :param description: The description of this EditUserReq.
        :type description: str
        """
        self._description = description

    @property
    def user_email(self):
        r"""Gets the user_email of this EditUserReq.

        用户邮箱。

        :return: The user_email of this EditUserReq.
        :rtype: str
        """
        return self._user_email

    @user_email.setter
    def user_email(self, user_email):
        r"""Sets the user_email of this EditUserReq.

        用户邮箱。

        :param user_email: The user_email of this EditUserReq.
        :type user_email: str
        """
        self._user_email = user_email

    @property
    def user_phone(self):
        r"""Gets the user_phone of this EditUserReq.

        手机号。

        :return: The user_phone of this EditUserReq.
        :rtype: str
        """
        return self._user_phone

    @user_phone.setter
    def user_phone(self, user_phone):
        r"""Sets the user_phone of this EditUserReq.

        手机号。

        :param user_phone: The user_phone of this EditUserReq.
        :type user_phone: str
        """
        self._user_phone = user_phone

    @property
    def active_type(self):
        r"""Gets the active_type of this EditUserReq.

        激活类型，默认为用户激活。 * USER_ACTIVATE： 用户激活 * ADMIN_ACTIVATE： 管理员激活

        :return: The active_type of this EditUserReq.
        :rtype: str
        """
        return self._active_type

    @active_type.setter
    def active_type(self, active_type):
        r"""Sets the active_type of this EditUserReq.

        激活类型，默认为用户激活。 * USER_ACTIVATE： 用户激活 * ADMIN_ACTIVATE： 管理员激活

        :param active_type: The active_type of this EditUserReq.
        :type active_type: str
        """
        self._active_type = active_type

    @property
    def account_expires(self):
        r"""Gets the account_expires of this EditUserReq.

        账户过期时间，0表示永远不过期。

        :return: The account_expires of this EditUserReq.
        :rtype: str
        """
        return self._account_expires

    @account_expires.setter
    def account_expires(self, account_expires):
        r"""Sets the account_expires of this EditUserReq.

        账户过期时间，0表示永远不过期。

        :param account_expires: The account_expires of this EditUserReq.
        :type account_expires: str
        """
        self._account_expires = account_expires

    @property
    def enable_change_password(self):
        r"""Gets the enable_change_password of this EditUserReq.

        是否允许修改密码，true表示允许，false表示不允许。

        :return: The enable_change_password of this EditUserReq.
        :rtype: bool
        """
        return self._enable_change_password

    @enable_change_password.setter
    def enable_change_password(self, enable_change_password):
        r"""Sets the enable_change_password of this EditUserReq.

        是否允许修改密码，true表示允许，false表示不允许。

        :param enable_change_password: The enable_change_password of this EditUserReq.
        :type enable_change_password: bool
        """
        self._enable_change_password = enable_change_password

    @property
    def next_login_change_password(self):
        r"""Gets the next_login_change_password of this EditUserReq.

        下次登录是否需要重置密码，true表示需要重置密码，false表示不需要。

        :return: The next_login_change_password of this EditUserReq.
        :rtype: bool
        """
        return self._next_login_change_password

    @next_login_change_password.setter
    def next_login_change_password(self, next_login_change_password):
        r"""Sets the next_login_change_password of this EditUserReq.

        下次登录是否需要重置密码，true表示需要重置密码，false表示不需要。

        :param next_login_change_password: The next_login_change_password of this EditUserReq.
        :type next_login_change_password: bool
        """
        self._next_login_change_password = next_login_change_password

    @property
    def group_ids(self):
        r"""Gets the group_ids of this EditUserReq.

        用户组的专有ID列表。

        :return: The group_ids of this EditUserReq.
        :rtype: list[str]
        """
        return self._group_ids

    @group_ids.setter
    def group_ids(self, group_ids):
        r"""Sets the group_ids of this EditUserReq.

        用户组的专有ID列表。

        :param group_ids: The group_ids of this EditUserReq.
        :type group_ids: list[str]
        """
        self._group_ids = group_ids

    @property
    def alias_name(self):
        r"""Gets the alias_name of this EditUserReq.

        别名。

        :return: The alias_name of this EditUserReq.
        :rtype: str
        """
        return self._alias_name

    @alias_name.setter
    def alias_name(self, alias_name):
        r"""Sets the alias_name of this EditUserReq.

        别名。

        :param alias_name: The alias_name of this EditUserReq.
        :type alias_name: str
        """
        self._alias_name = alias_name

    @property
    def password_never_expired(self):
        r"""Gets the password_never_expired of this EditUserReq.

        密码是否永不过期，true表示密码永不过期，false表示密码会过期。

        :return: The password_never_expired of this EditUserReq.
        :rtype: bool
        """
        return self._password_never_expired

    @password_never_expired.setter
    def password_never_expired(self, password_never_expired):
        r"""Sets the password_never_expired of this EditUserReq.

        密码是否永不过期，true表示密码永不过期，false表示密码会过期。

        :param password_never_expired: The password_never_expired of this EditUserReq.
        :type password_never_expired: bool
        """
        self._password_never_expired = password_never_expired

    @property
    def disabled(self):
        r"""Gets the disabled of this EditUserReq.

        账户是否禁用，true表示被禁用，false表示未禁用。

        :return: The disabled of this EditUserReq.
        :rtype: bool
        """
        return self._disabled

    @disabled.setter
    def disabled(self, disabled):
        r"""Sets the disabled of this EditUserReq.

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
