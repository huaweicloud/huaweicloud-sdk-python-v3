# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UsersDetailsResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user_id': 'str',
        'org_id': 'str',
        'user_name': 'str',
        'name': 'str',
        'mobile': 'str',
        'email': 'str',
        'pwd_must_modify': 'bool',
        'pwd_change_at': 'str',
        'created_at': 'str',
        'updated_at': 'str',
        'disabled': 'str',
        'grade': 'str',
        'locked': 'str',
        'extension': 'str',
        'user_org_relation_list': 'list[UserOrgRelationListResult]'
    }

    attribute_map = {
        'user_id': 'user_id',
        'org_id': 'org_id',
        'user_name': 'user_name',
        'name': 'name',
        'mobile': 'mobile',
        'email': 'email',
        'pwd_must_modify': 'pwd_must_modify',
        'pwd_change_at': 'pwd_change_at',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'disabled': 'disabled',
        'grade': 'grade',
        'locked': 'locked',
        'extension': 'extension',
        'user_org_relation_list': 'user_org_relation_list'
    }

    def __init__(self, user_id=None, org_id=None, user_name=None, name=None, mobile=None, email=None, pwd_must_modify=None, pwd_change_at=None, created_at=None, updated_at=None, disabled=None, grade=None, locked=None, extension=None, user_org_relation_list=None):
        r"""UsersDetailsResult

        The model defined in huaweicloud sdk

        :param user_id: 用户id。
        :type user_id: str
        :param org_id: 用户所属组织。
        :type org_id: str
        :param user_name: 用户名。
        :type user_name: str
        :param name: 姓名。
        :type name: str
        :param mobile: 手机号。
        :type mobile: str
        :param email: 邮箱。
        :type email: str
        :param pwd_must_modify: 首次登录是否强制修改密码。
        :type pwd_must_modify: bool
        :param pwd_change_at: 密码修改时间。
        :type pwd_change_at: str
        :param created_at: 创建时间。
        :type created_at: str
        :param updated_at: 最后一次修改时间。
        :type updated_at: str
        :param disabled: 是否禁用。
        :type disabled: str
        :param grade: 可信等级。
        :type grade: str
        :param locked: 是否锁定。
        :type locked: str
        :param extension: 自定义扩展属性。
        :type extension: str
        :param user_org_relation_list: 用户组织关系集合。
        :type user_org_relation_list: list[:class:`huaweicloudsdkcsms.v1.UserOrgRelationListResult`]
        """
        
        

        self._user_id = None
        self._org_id = None
        self._user_name = None
        self._name = None
        self._mobile = None
        self._email = None
        self._pwd_must_modify = None
        self._pwd_change_at = None
        self._created_at = None
        self._updated_at = None
        self._disabled = None
        self._grade = None
        self._locked = None
        self._extension = None
        self._user_org_relation_list = None
        self.discriminator = None

        if user_id is not None:
            self.user_id = user_id
        if org_id is not None:
            self.org_id = org_id
        if user_name is not None:
            self.user_name = user_name
        if name is not None:
            self.name = name
        if mobile is not None:
            self.mobile = mobile
        if email is not None:
            self.email = email
        if pwd_must_modify is not None:
            self.pwd_must_modify = pwd_must_modify
        if pwd_change_at is not None:
            self.pwd_change_at = pwd_change_at
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if disabled is not None:
            self.disabled = disabled
        if grade is not None:
            self.grade = grade
        if locked is not None:
            self.locked = locked
        if extension is not None:
            self.extension = extension
        if user_org_relation_list is not None:
            self.user_org_relation_list = user_org_relation_list

    @property
    def user_id(self):
        r"""Gets the user_id of this UsersDetailsResult.

        用户id。

        :return: The user_id of this UsersDetailsResult.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this UsersDetailsResult.

        用户id。

        :param user_id: The user_id of this UsersDetailsResult.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def org_id(self):
        r"""Gets the org_id of this UsersDetailsResult.

        用户所属组织。

        :return: The org_id of this UsersDetailsResult.
        :rtype: str
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        r"""Sets the org_id of this UsersDetailsResult.

        用户所属组织。

        :param org_id: The org_id of this UsersDetailsResult.
        :type org_id: str
        """
        self._org_id = org_id

    @property
    def user_name(self):
        r"""Gets the user_name of this UsersDetailsResult.

        用户名。

        :return: The user_name of this UsersDetailsResult.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this UsersDetailsResult.

        用户名。

        :param user_name: The user_name of this UsersDetailsResult.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def name(self):
        r"""Gets the name of this UsersDetailsResult.

        姓名。

        :return: The name of this UsersDetailsResult.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UsersDetailsResult.

        姓名。

        :param name: The name of this UsersDetailsResult.
        :type name: str
        """
        self._name = name

    @property
    def mobile(self):
        r"""Gets the mobile of this UsersDetailsResult.

        手机号。

        :return: The mobile of this UsersDetailsResult.
        :rtype: str
        """
        return self._mobile

    @mobile.setter
    def mobile(self, mobile):
        r"""Sets the mobile of this UsersDetailsResult.

        手机号。

        :param mobile: The mobile of this UsersDetailsResult.
        :type mobile: str
        """
        self._mobile = mobile

    @property
    def email(self):
        r"""Gets the email of this UsersDetailsResult.

        邮箱。

        :return: The email of this UsersDetailsResult.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        r"""Sets the email of this UsersDetailsResult.

        邮箱。

        :param email: The email of this UsersDetailsResult.
        :type email: str
        """
        self._email = email

    @property
    def pwd_must_modify(self):
        r"""Gets the pwd_must_modify of this UsersDetailsResult.

        首次登录是否强制修改密码。

        :return: The pwd_must_modify of this UsersDetailsResult.
        :rtype: bool
        """
        return self._pwd_must_modify

    @pwd_must_modify.setter
    def pwd_must_modify(self, pwd_must_modify):
        r"""Sets the pwd_must_modify of this UsersDetailsResult.

        首次登录是否强制修改密码。

        :param pwd_must_modify: The pwd_must_modify of this UsersDetailsResult.
        :type pwd_must_modify: bool
        """
        self._pwd_must_modify = pwd_must_modify

    @property
    def pwd_change_at(self):
        r"""Gets the pwd_change_at of this UsersDetailsResult.

        密码修改时间。

        :return: The pwd_change_at of this UsersDetailsResult.
        :rtype: str
        """
        return self._pwd_change_at

    @pwd_change_at.setter
    def pwd_change_at(self, pwd_change_at):
        r"""Sets the pwd_change_at of this UsersDetailsResult.

        密码修改时间。

        :param pwd_change_at: The pwd_change_at of this UsersDetailsResult.
        :type pwd_change_at: str
        """
        self._pwd_change_at = pwd_change_at

    @property
    def created_at(self):
        r"""Gets the created_at of this UsersDetailsResult.

        创建时间。

        :return: The created_at of this UsersDetailsResult.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this UsersDetailsResult.

        创建时间。

        :param created_at: The created_at of this UsersDetailsResult.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this UsersDetailsResult.

        最后一次修改时间。

        :return: The updated_at of this UsersDetailsResult.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this UsersDetailsResult.

        最后一次修改时间。

        :param updated_at: The updated_at of this UsersDetailsResult.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def disabled(self):
        r"""Gets the disabled of this UsersDetailsResult.

        是否禁用。

        :return: The disabled of this UsersDetailsResult.
        :rtype: str
        """
        return self._disabled

    @disabled.setter
    def disabled(self, disabled):
        r"""Sets the disabled of this UsersDetailsResult.

        是否禁用。

        :param disabled: The disabled of this UsersDetailsResult.
        :type disabled: str
        """
        self._disabled = disabled

    @property
    def grade(self):
        r"""Gets the grade of this UsersDetailsResult.

        可信等级。

        :return: The grade of this UsersDetailsResult.
        :rtype: str
        """
        return self._grade

    @grade.setter
    def grade(self, grade):
        r"""Sets the grade of this UsersDetailsResult.

        可信等级。

        :param grade: The grade of this UsersDetailsResult.
        :type grade: str
        """
        self._grade = grade

    @property
    def locked(self):
        r"""Gets the locked of this UsersDetailsResult.

        是否锁定。

        :return: The locked of this UsersDetailsResult.
        :rtype: str
        """
        return self._locked

    @locked.setter
    def locked(self, locked):
        r"""Sets the locked of this UsersDetailsResult.

        是否锁定。

        :param locked: The locked of this UsersDetailsResult.
        :type locked: str
        """
        self._locked = locked

    @property
    def extension(self):
        r"""Gets the extension of this UsersDetailsResult.

        自定义扩展属性。

        :return: The extension of this UsersDetailsResult.
        :rtype: str
        """
        return self._extension

    @extension.setter
    def extension(self, extension):
        r"""Sets the extension of this UsersDetailsResult.

        自定义扩展属性。

        :param extension: The extension of this UsersDetailsResult.
        :type extension: str
        """
        self._extension = extension

    @property
    def user_org_relation_list(self):
        r"""Gets the user_org_relation_list of this UsersDetailsResult.

        用户组织关系集合。

        :return: The user_org_relation_list of this UsersDetailsResult.
        :rtype: list[:class:`huaweicloudsdkcsms.v1.UserOrgRelationListResult`]
        """
        return self._user_org_relation_list

    @user_org_relation_list.setter
    def user_org_relation_list(self, user_org_relation_list):
        r"""Sets the user_org_relation_list of this UsersDetailsResult.

        用户组织关系集合。

        :param user_org_relation_list: The user_org_relation_list of this UsersDetailsResult.
        :type user_org_relation_list: list[:class:`huaweicloudsdkcsms.v1.UserOrgRelationListResult`]
        """
        self._user_org_relation_list = user_org_relation_list

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
        if not isinstance(other, UsersDetailsResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
