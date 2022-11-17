# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class User:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'user_name': 'str',
        'user_email': 'str',
        'total_desktops': 'int',
        'account_expires': 'str',
        'password_never_expired': 'bool',
        'account_expired': 'bool',
        'enable_change_password': 'bool',
        'next_login_change_password': 'bool',
        'description': 'str',
        'locked': 'bool',
        'disabled': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'user_name': 'user_name',
        'user_email': 'user_email',
        'total_desktops': 'total_desktops',
        'account_expires': 'account_expires',
        'password_never_expired': 'password_never_expired',
        'account_expired': 'account_expired',
        'enable_change_password': 'enable_change_password',
        'next_login_change_password': 'next_login_change_password',
        'description': 'description',
        'locked': 'locked',
        'disabled': 'disabled'
    }

    def __init__(self, id=None, user_name=None, user_email=None, total_desktops=None, account_expires=None, password_never_expired=None, account_expired=None, enable_change_password=None, next_login_change_password=None, description=None, locked=None, disabled=None):
        """User

        The model defined in huaweicloud sdk

        :param id: 用户ID。
        :type id: str
        :param user_name: 桌面用户名。
        :type user_name: str
        :param user_email: 用户邮箱。
        :type user_email: str
        :param total_desktops: 用户绑定桌面云总数。
        :type total_desktops: int
        :param account_expires: 账户过期时间，0表示永远不过期。
        :type account_expires: str
        :param password_never_expired: 密码是否永不过期，true表示密码永不过期，false表示密码会过期。
        :type password_never_expired: bool
        :param account_expired: 帐号是否过期，true表示已过期，false表示未过期。
        :type account_expired: bool
        :param enable_change_password: 是否允许修改密码，true表示允许，false表示不允许。
        :type enable_change_password: bool
        :param next_login_change_password: 下次登录是否需要重置密码，true表示需要重置密码，false表示不需要。
        :type next_login_change_password: bool
        :param description: 用户描述。
        :type description: str
        :param locked: 账户是否被锁定，true表示被锁定，false表示未锁定。
        :type locked: bool
        :param disabled: 账户是否禁用，true表示被禁用，false表示未禁用。
        :type disabled: bool
        """
        
        

        self._id = None
        self._user_name = None
        self._user_email = None
        self._total_desktops = None
        self._account_expires = None
        self._password_never_expired = None
        self._account_expired = None
        self._enable_change_password = None
        self._next_login_change_password = None
        self._description = None
        self._locked = None
        self._disabled = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if user_name is not None:
            self.user_name = user_name
        if user_email is not None:
            self.user_email = user_email
        if total_desktops is not None:
            self.total_desktops = total_desktops
        if account_expires is not None:
            self.account_expires = account_expires
        if password_never_expired is not None:
            self.password_never_expired = password_never_expired
        if account_expired is not None:
            self.account_expired = account_expired
        if enable_change_password is not None:
            self.enable_change_password = enable_change_password
        if next_login_change_password is not None:
            self.next_login_change_password = next_login_change_password
        if description is not None:
            self.description = description
        if locked is not None:
            self.locked = locked
        if disabled is not None:
            self.disabled = disabled

    @property
    def id(self):
        """Gets the id of this User.

        用户ID。

        :return: The id of this User.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this User.

        用户ID。

        :param id: The id of this User.
        :type id: str
        """
        self._id = id

    @property
    def user_name(self):
        """Gets the user_name of this User.

        桌面用户名。

        :return: The user_name of this User.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this User.

        桌面用户名。

        :param user_name: The user_name of this User.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def user_email(self):
        """Gets the user_email of this User.

        用户邮箱。

        :return: The user_email of this User.
        :rtype: str
        """
        return self._user_email

    @user_email.setter
    def user_email(self, user_email):
        """Sets the user_email of this User.

        用户邮箱。

        :param user_email: The user_email of this User.
        :type user_email: str
        """
        self._user_email = user_email

    @property
    def total_desktops(self):
        """Gets the total_desktops of this User.

        用户绑定桌面云总数。

        :return: The total_desktops of this User.
        :rtype: int
        """
        return self._total_desktops

    @total_desktops.setter
    def total_desktops(self, total_desktops):
        """Sets the total_desktops of this User.

        用户绑定桌面云总数。

        :param total_desktops: The total_desktops of this User.
        :type total_desktops: int
        """
        self._total_desktops = total_desktops

    @property
    def account_expires(self):
        """Gets the account_expires of this User.

        账户过期时间，0表示永远不过期。

        :return: The account_expires of this User.
        :rtype: str
        """
        return self._account_expires

    @account_expires.setter
    def account_expires(self, account_expires):
        """Sets the account_expires of this User.

        账户过期时间，0表示永远不过期。

        :param account_expires: The account_expires of this User.
        :type account_expires: str
        """
        self._account_expires = account_expires

    @property
    def password_never_expired(self):
        """Gets the password_never_expired of this User.

        密码是否永不过期，true表示密码永不过期，false表示密码会过期。

        :return: The password_never_expired of this User.
        :rtype: bool
        """
        return self._password_never_expired

    @password_never_expired.setter
    def password_never_expired(self, password_never_expired):
        """Sets the password_never_expired of this User.

        密码是否永不过期，true表示密码永不过期，false表示密码会过期。

        :param password_never_expired: The password_never_expired of this User.
        :type password_never_expired: bool
        """
        self._password_never_expired = password_never_expired

    @property
    def account_expired(self):
        """Gets the account_expired of this User.

        帐号是否过期，true表示已过期，false表示未过期。

        :return: The account_expired of this User.
        :rtype: bool
        """
        return self._account_expired

    @account_expired.setter
    def account_expired(self, account_expired):
        """Sets the account_expired of this User.

        帐号是否过期，true表示已过期，false表示未过期。

        :param account_expired: The account_expired of this User.
        :type account_expired: bool
        """
        self._account_expired = account_expired

    @property
    def enable_change_password(self):
        """Gets the enable_change_password of this User.

        是否允许修改密码，true表示允许，false表示不允许。

        :return: The enable_change_password of this User.
        :rtype: bool
        """
        return self._enable_change_password

    @enable_change_password.setter
    def enable_change_password(self, enable_change_password):
        """Sets the enable_change_password of this User.

        是否允许修改密码，true表示允许，false表示不允许。

        :param enable_change_password: The enable_change_password of this User.
        :type enable_change_password: bool
        """
        self._enable_change_password = enable_change_password

    @property
    def next_login_change_password(self):
        """Gets the next_login_change_password of this User.

        下次登录是否需要重置密码，true表示需要重置密码，false表示不需要。

        :return: The next_login_change_password of this User.
        :rtype: bool
        """
        return self._next_login_change_password

    @next_login_change_password.setter
    def next_login_change_password(self, next_login_change_password):
        """Sets the next_login_change_password of this User.

        下次登录是否需要重置密码，true表示需要重置密码，false表示不需要。

        :param next_login_change_password: The next_login_change_password of this User.
        :type next_login_change_password: bool
        """
        self._next_login_change_password = next_login_change_password

    @property
    def description(self):
        """Gets the description of this User.

        用户描述。

        :return: The description of this User.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this User.

        用户描述。

        :param description: The description of this User.
        :type description: str
        """
        self._description = description

    @property
    def locked(self):
        """Gets the locked of this User.

        账户是否被锁定，true表示被锁定，false表示未锁定。

        :return: The locked of this User.
        :rtype: bool
        """
        return self._locked

    @locked.setter
    def locked(self, locked):
        """Sets the locked of this User.

        账户是否被锁定，true表示被锁定，false表示未锁定。

        :param locked: The locked of this User.
        :type locked: bool
        """
        self._locked = locked

    @property
    def disabled(self):
        """Gets the disabled of this User.

        账户是否禁用，true表示被禁用，false表示未禁用。

        :return: The disabled of this User.
        :rtype: bool
        """
        return self._disabled

    @disabled.setter
    def disabled(self, disabled):
        """Sets the disabled of this User.

        账户是否禁用，true表示被禁用，false表示未禁用。

        :param disabled: The disabled of this User.
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
        if not isinstance(other, User):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
