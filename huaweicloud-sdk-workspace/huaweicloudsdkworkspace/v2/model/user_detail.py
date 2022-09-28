# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UserDetail:

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
        'id': 'str',
        'user_name': 'str',
        'user_email': 'str',
        'object_sid': 'str',
        'sam_account_name': 'str',
        'user_principal_name': 'str',
        'full_name': 'str',
        'distinguished_name': 'str',
        'account_type': 'int',
        'when_created': 'str',
        'account_expires': 'int',
        'user_expired': 'bool',
        'locked': 'bool',
        'enabled_change_password': 'bool',
        'password_never_expired': 'bool',
        'next_login_change_password': 'bool',
        'disabled': 'bool',
        'group_names': 'list[str]',
        'total_desktops': 'int'
    }

    attribute_map = {
        'description': 'description',
        'id': 'id',
        'user_name': 'user_name',
        'user_email': 'user_email',
        'object_sid': 'object_sid',
        'sam_account_name': 'sam_account_name',
        'user_principal_name': 'user_principal_name',
        'full_name': 'full_name',
        'distinguished_name': 'distinguished_name',
        'account_type': 'account_type',
        'when_created': 'when_created',
        'account_expires': 'account_expires',
        'user_expired': 'user_expired',
        'locked': 'locked',
        'enabled_change_password': 'enabled_change_password',
        'password_never_expired': 'password_never_expired',
        'next_login_change_password': 'next_login_change_password',
        'disabled': 'disabled',
        'group_names': 'group_names',
        'total_desktops': 'total_desktops'
    }

    def __init__(self, description=None, id=None, user_name=None, user_email=None, object_sid=None, sam_account_name=None, user_principal_name=None, full_name=None, distinguished_name=None, account_type=None, when_created=None, account_expires=None, user_expired=None, locked=None, enabled_change_password=None, password_never_expired=None, next_login_change_password=None, disabled=None, group_names=None, total_desktops=None):
        """UserDetail

        The model defined in huaweicloud sdk

        :param description: 用户描述。
        :type description: str
        :param id: 用户id。
        :type id: str
        :param user_name: 桌面用户名。
        :type user_name: str
        :param user_email: 用户邮箱。
        :type user_email: str
        :param object_sid: 用户sid。
        :type object_sid: str
        :param sam_account_name: 登录名(windows以前版本)。
        :type sam_account_name: str
        :param user_principal_name: 用户登录名。
        :type user_principal_name: str
        :param full_name: 全名。
        :type full_name: str
        :param distinguished_name: 用户在域树上的唯一位置。
        :type distinguished_name: str
        :param account_type: 帐号类型(0：用户；1：用户组)。
        :type account_type: int
        :param when_created: UTC时间毫秒数对应的字符。
        :type when_created: str
        :param account_expires: 账号有效期最后一天对应的UTC时间，以毫秒为单位。
        :type account_expires: int
        :param user_expired: 账户是否过期，true表示过期，false表示未过期。
        :type user_expired: bool
        :param locked: 账户是否被锁定，true表示被锁定，false表示未锁定。
        :type locked: bool
        :param enabled_change_password: 是否允许修改密码，true表示允许修改密码，false表示不允许。
        :type enabled_change_password: bool
        :param password_never_expired: 密码是否永不过期，true表示密码永不过期，false表示密码会过期。
        :type password_never_expired: bool
        :param next_login_change_password: 下次登录是否需要重置密码，true表示需要重置密码，false表示不需要。
        :type next_login_change_password: bool
        :param disabled: 账户是否禁用，true表示被禁用，false表示未禁用。
        :type disabled: bool
        :param group_names: 加入的组列表。
        :type group_names: list[str]
        :param total_desktops: 用户绑定桌面云总数。
        :type total_desktops: int
        """
        
        

        self._description = None
        self._id = None
        self._user_name = None
        self._user_email = None
        self._object_sid = None
        self._sam_account_name = None
        self._user_principal_name = None
        self._full_name = None
        self._distinguished_name = None
        self._account_type = None
        self._when_created = None
        self._account_expires = None
        self._user_expired = None
        self._locked = None
        self._enabled_change_password = None
        self._password_never_expired = None
        self._next_login_change_password = None
        self._disabled = None
        self._group_names = None
        self._total_desktops = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        if user_name is not None:
            self.user_name = user_name
        if user_email is not None:
            self.user_email = user_email
        if object_sid is not None:
            self.object_sid = object_sid
        if sam_account_name is not None:
            self.sam_account_name = sam_account_name
        if user_principal_name is not None:
            self.user_principal_name = user_principal_name
        if full_name is not None:
            self.full_name = full_name
        if distinguished_name is not None:
            self.distinguished_name = distinguished_name
        if account_type is not None:
            self.account_type = account_type
        if when_created is not None:
            self.when_created = when_created
        if account_expires is not None:
            self.account_expires = account_expires
        if user_expired is not None:
            self.user_expired = user_expired
        if locked is not None:
            self.locked = locked
        if enabled_change_password is not None:
            self.enabled_change_password = enabled_change_password
        if password_never_expired is not None:
            self.password_never_expired = password_never_expired
        if next_login_change_password is not None:
            self.next_login_change_password = next_login_change_password
        if disabled is not None:
            self.disabled = disabled
        if group_names is not None:
            self.group_names = group_names
        if total_desktops is not None:
            self.total_desktops = total_desktops

    @property
    def description(self):
        """Gets the description of this UserDetail.

        用户描述。

        :return: The description of this UserDetail.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UserDetail.

        用户描述。

        :param description: The description of this UserDetail.
        :type description: str
        """
        self._description = description

    @property
    def id(self):
        """Gets the id of this UserDetail.

        用户id。

        :return: The id of this UserDetail.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserDetail.

        用户id。

        :param id: The id of this UserDetail.
        :type id: str
        """
        self._id = id

    @property
    def user_name(self):
        """Gets the user_name of this UserDetail.

        桌面用户名。

        :return: The user_name of this UserDetail.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this UserDetail.

        桌面用户名。

        :param user_name: The user_name of this UserDetail.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def user_email(self):
        """Gets the user_email of this UserDetail.

        用户邮箱。

        :return: The user_email of this UserDetail.
        :rtype: str
        """
        return self._user_email

    @user_email.setter
    def user_email(self, user_email):
        """Sets the user_email of this UserDetail.

        用户邮箱。

        :param user_email: The user_email of this UserDetail.
        :type user_email: str
        """
        self._user_email = user_email

    @property
    def object_sid(self):
        """Gets the object_sid of this UserDetail.

        用户sid。

        :return: The object_sid of this UserDetail.
        :rtype: str
        """
        return self._object_sid

    @object_sid.setter
    def object_sid(self, object_sid):
        """Sets the object_sid of this UserDetail.

        用户sid。

        :param object_sid: The object_sid of this UserDetail.
        :type object_sid: str
        """
        self._object_sid = object_sid

    @property
    def sam_account_name(self):
        """Gets the sam_account_name of this UserDetail.

        登录名(windows以前版本)。

        :return: The sam_account_name of this UserDetail.
        :rtype: str
        """
        return self._sam_account_name

    @sam_account_name.setter
    def sam_account_name(self, sam_account_name):
        """Sets the sam_account_name of this UserDetail.

        登录名(windows以前版本)。

        :param sam_account_name: The sam_account_name of this UserDetail.
        :type sam_account_name: str
        """
        self._sam_account_name = sam_account_name

    @property
    def user_principal_name(self):
        """Gets the user_principal_name of this UserDetail.

        用户登录名。

        :return: The user_principal_name of this UserDetail.
        :rtype: str
        """
        return self._user_principal_name

    @user_principal_name.setter
    def user_principal_name(self, user_principal_name):
        """Sets the user_principal_name of this UserDetail.

        用户登录名。

        :param user_principal_name: The user_principal_name of this UserDetail.
        :type user_principal_name: str
        """
        self._user_principal_name = user_principal_name

    @property
    def full_name(self):
        """Gets the full_name of this UserDetail.

        全名。

        :return: The full_name of this UserDetail.
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this UserDetail.

        全名。

        :param full_name: The full_name of this UserDetail.
        :type full_name: str
        """
        self._full_name = full_name

    @property
    def distinguished_name(self):
        """Gets the distinguished_name of this UserDetail.

        用户在域树上的唯一位置。

        :return: The distinguished_name of this UserDetail.
        :rtype: str
        """
        return self._distinguished_name

    @distinguished_name.setter
    def distinguished_name(self, distinguished_name):
        """Sets the distinguished_name of this UserDetail.

        用户在域树上的唯一位置。

        :param distinguished_name: The distinguished_name of this UserDetail.
        :type distinguished_name: str
        """
        self._distinguished_name = distinguished_name

    @property
    def account_type(self):
        """Gets the account_type of this UserDetail.

        帐号类型(0：用户；1：用户组)。

        :return: The account_type of this UserDetail.
        :rtype: int
        """
        return self._account_type

    @account_type.setter
    def account_type(self, account_type):
        """Sets the account_type of this UserDetail.

        帐号类型(0：用户；1：用户组)。

        :param account_type: The account_type of this UserDetail.
        :type account_type: int
        """
        self._account_type = account_type

    @property
    def when_created(self):
        """Gets the when_created of this UserDetail.

        UTC时间毫秒数对应的字符。

        :return: The when_created of this UserDetail.
        :rtype: str
        """
        return self._when_created

    @when_created.setter
    def when_created(self, when_created):
        """Sets the when_created of this UserDetail.

        UTC时间毫秒数对应的字符。

        :param when_created: The when_created of this UserDetail.
        :type when_created: str
        """
        self._when_created = when_created

    @property
    def account_expires(self):
        """Gets the account_expires of this UserDetail.

        账号有效期最后一天对应的UTC时间，以毫秒为单位。

        :return: The account_expires of this UserDetail.
        :rtype: int
        """
        return self._account_expires

    @account_expires.setter
    def account_expires(self, account_expires):
        """Sets the account_expires of this UserDetail.

        账号有效期最后一天对应的UTC时间，以毫秒为单位。

        :param account_expires: The account_expires of this UserDetail.
        :type account_expires: int
        """
        self._account_expires = account_expires

    @property
    def user_expired(self):
        """Gets the user_expired of this UserDetail.

        账户是否过期，true表示过期，false表示未过期。

        :return: The user_expired of this UserDetail.
        :rtype: bool
        """
        return self._user_expired

    @user_expired.setter
    def user_expired(self, user_expired):
        """Sets the user_expired of this UserDetail.

        账户是否过期，true表示过期，false表示未过期。

        :param user_expired: The user_expired of this UserDetail.
        :type user_expired: bool
        """
        self._user_expired = user_expired

    @property
    def locked(self):
        """Gets the locked of this UserDetail.

        账户是否被锁定，true表示被锁定，false表示未锁定。

        :return: The locked of this UserDetail.
        :rtype: bool
        """
        return self._locked

    @locked.setter
    def locked(self, locked):
        """Sets the locked of this UserDetail.

        账户是否被锁定，true表示被锁定，false表示未锁定。

        :param locked: The locked of this UserDetail.
        :type locked: bool
        """
        self._locked = locked

    @property
    def enabled_change_password(self):
        """Gets the enabled_change_password of this UserDetail.

        是否允许修改密码，true表示允许修改密码，false表示不允许。

        :return: The enabled_change_password of this UserDetail.
        :rtype: bool
        """
        return self._enabled_change_password

    @enabled_change_password.setter
    def enabled_change_password(self, enabled_change_password):
        """Sets the enabled_change_password of this UserDetail.

        是否允许修改密码，true表示允许修改密码，false表示不允许。

        :param enabled_change_password: The enabled_change_password of this UserDetail.
        :type enabled_change_password: bool
        """
        self._enabled_change_password = enabled_change_password

    @property
    def password_never_expired(self):
        """Gets the password_never_expired of this UserDetail.

        密码是否永不过期，true表示密码永不过期，false表示密码会过期。

        :return: The password_never_expired of this UserDetail.
        :rtype: bool
        """
        return self._password_never_expired

    @password_never_expired.setter
    def password_never_expired(self, password_never_expired):
        """Sets the password_never_expired of this UserDetail.

        密码是否永不过期，true表示密码永不过期，false表示密码会过期。

        :param password_never_expired: The password_never_expired of this UserDetail.
        :type password_never_expired: bool
        """
        self._password_never_expired = password_never_expired

    @property
    def next_login_change_password(self):
        """Gets the next_login_change_password of this UserDetail.

        下次登录是否需要重置密码，true表示需要重置密码，false表示不需要。

        :return: The next_login_change_password of this UserDetail.
        :rtype: bool
        """
        return self._next_login_change_password

    @next_login_change_password.setter
    def next_login_change_password(self, next_login_change_password):
        """Sets the next_login_change_password of this UserDetail.

        下次登录是否需要重置密码，true表示需要重置密码，false表示不需要。

        :param next_login_change_password: The next_login_change_password of this UserDetail.
        :type next_login_change_password: bool
        """
        self._next_login_change_password = next_login_change_password

    @property
    def disabled(self):
        """Gets the disabled of this UserDetail.

        账户是否禁用，true表示被禁用，false表示未禁用。

        :return: The disabled of this UserDetail.
        :rtype: bool
        """
        return self._disabled

    @disabled.setter
    def disabled(self, disabled):
        """Sets the disabled of this UserDetail.

        账户是否禁用，true表示被禁用，false表示未禁用。

        :param disabled: The disabled of this UserDetail.
        :type disabled: bool
        """
        self._disabled = disabled

    @property
    def group_names(self):
        """Gets the group_names of this UserDetail.

        加入的组列表。

        :return: The group_names of this UserDetail.
        :rtype: list[str]
        """
        return self._group_names

    @group_names.setter
    def group_names(self, group_names):
        """Sets the group_names of this UserDetail.

        加入的组列表。

        :param group_names: The group_names of this UserDetail.
        :type group_names: list[str]
        """
        self._group_names = group_names

    @property
    def total_desktops(self):
        """Gets the total_desktops of this UserDetail.

        用户绑定桌面云总数。

        :return: The total_desktops of this UserDetail.
        :rtype: int
        """
        return self._total_desktops

    @total_desktops.setter
    def total_desktops(self, total_desktops):
        """Sets the total_desktops of this UserDetail.

        用户绑定桌面云总数。

        :param total_desktops: The total_desktops of this UserDetail.
        :type total_desktops: int
        """
        self._total_desktops = total_desktops

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
        if not isinstance(other, UserDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
