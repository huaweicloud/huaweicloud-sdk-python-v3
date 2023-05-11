# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryUserDetailResp:

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
        'account': 'str',
        'comment': 'str',
        'is_transfer': 'bool',
        'privileges': 'str',
        'password': 'str',
        'roles': 'list[str]',
        'selected': 'bool',
        'no_privileges': 'str',
        'parent_account': 'str',
        'no_parent_account': 'str'
    }

    attribute_map = {
        'id': 'id',
        'account': 'account',
        'comment': 'comment',
        'is_transfer': 'is_transfer',
        'privileges': 'privileges',
        'password': 'password',
        'roles': 'roles',
        'selected': 'selected',
        'no_privileges': 'no_privileges',
        'parent_account': 'parent_account',
        'no_parent_account': 'no_parent_account'
    }

    def __init__(self, id=None, account=None, comment=None, is_transfer=None, privileges=None, password=None, roles=None, selected=None, no_privileges=None, parent_account=None, no_parent_account=None):
        """QueryUserDetailResp

        The model defined in huaweicloud sdk

        :param id: 用户账户id。
        :type id: str
        :param account: 账户。
        :type account: str
        :param comment: 说明。
        :type comment: str
        :param is_transfer: 是否支持迁移
        :type is_transfer: bool
        :param privileges: 权限
        :type privileges: str
        :param password: 密码。
        :type password: str
        :param roles: 账号拥有的角色
        :type roles: list[str]
        :param selected: 是否选择。
        :type selected: bool
        :param no_privileges: 无法同步的用户权限
        :type no_privileges: str
        :param parent_account: 父用户
        :type parent_account: str
        :param no_parent_account: 无法同步父子关系的父用户
        :type no_parent_account: str
        """
        
        

        self._id = None
        self._account = None
        self._comment = None
        self._is_transfer = None
        self._privileges = None
        self._password = None
        self._roles = None
        self._selected = None
        self._no_privileges = None
        self._parent_account = None
        self._no_parent_account = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if account is not None:
            self.account = account
        if comment is not None:
            self.comment = comment
        if is_transfer is not None:
            self.is_transfer = is_transfer
        if privileges is not None:
            self.privileges = privileges
        if password is not None:
            self.password = password
        if roles is not None:
            self.roles = roles
        if selected is not None:
            self.selected = selected
        if no_privileges is not None:
            self.no_privileges = no_privileges
        if parent_account is not None:
            self.parent_account = parent_account
        if no_parent_account is not None:
            self.no_parent_account = no_parent_account

    @property
    def id(self):
        """Gets the id of this QueryUserDetailResp.

        用户账户id。

        :return: The id of this QueryUserDetailResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this QueryUserDetailResp.

        用户账户id。

        :param id: The id of this QueryUserDetailResp.
        :type id: str
        """
        self._id = id

    @property
    def account(self):
        """Gets the account of this QueryUserDetailResp.

        账户。

        :return: The account of this QueryUserDetailResp.
        :rtype: str
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this QueryUserDetailResp.

        账户。

        :param account: The account of this QueryUserDetailResp.
        :type account: str
        """
        self._account = account

    @property
    def comment(self):
        """Gets the comment of this QueryUserDetailResp.

        说明。

        :return: The comment of this QueryUserDetailResp.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this QueryUserDetailResp.

        说明。

        :param comment: The comment of this QueryUserDetailResp.
        :type comment: str
        """
        self._comment = comment

    @property
    def is_transfer(self):
        """Gets the is_transfer of this QueryUserDetailResp.

        是否支持迁移

        :return: The is_transfer of this QueryUserDetailResp.
        :rtype: bool
        """
        return self._is_transfer

    @is_transfer.setter
    def is_transfer(self, is_transfer):
        """Sets the is_transfer of this QueryUserDetailResp.

        是否支持迁移

        :param is_transfer: The is_transfer of this QueryUserDetailResp.
        :type is_transfer: bool
        """
        self._is_transfer = is_transfer

    @property
    def privileges(self):
        """Gets the privileges of this QueryUserDetailResp.

        权限

        :return: The privileges of this QueryUserDetailResp.
        :rtype: str
        """
        return self._privileges

    @privileges.setter
    def privileges(self, privileges):
        """Sets the privileges of this QueryUserDetailResp.

        权限

        :param privileges: The privileges of this QueryUserDetailResp.
        :type privileges: str
        """
        self._privileges = privileges

    @property
    def password(self):
        """Gets the password of this QueryUserDetailResp.

        密码。

        :return: The password of this QueryUserDetailResp.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this QueryUserDetailResp.

        密码。

        :param password: The password of this QueryUserDetailResp.
        :type password: str
        """
        self._password = password

    @property
    def roles(self):
        """Gets the roles of this QueryUserDetailResp.

        账号拥有的角色

        :return: The roles of this QueryUserDetailResp.
        :rtype: list[str]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this QueryUserDetailResp.

        账号拥有的角色

        :param roles: The roles of this QueryUserDetailResp.
        :type roles: list[str]
        """
        self._roles = roles

    @property
    def selected(self):
        """Gets the selected of this QueryUserDetailResp.

        是否选择。

        :return: The selected of this QueryUserDetailResp.
        :rtype: bool
        """
        return self._selected

    @selected.setter
    def selected(self, selected):
        """Sets the selected of this QueryUserDetailResp.

        是否选择。

        :param selected: The selected of this QueryUserDetailResp.
        :type selected: bool
        """
        self._selected = selected

    @property
    def no_privileges(self):
        """Gets the no_privileges of this QueryUserDetailResp.

        无法同步的用户权限

        :return: The no_privileges of this QueryUserDetailResp.
        :rtype: str
        """
        return self._no_privileges

    @no_privileges.setter
    def no_privileges(self, no_privileges):
        """Sets the no_privileges of this QueryUserDetailResp.

        无法同步的用户权限

        :param no_privileges: The no_privileges of this QueryUserDetailResp.
        :type no_privileges: str
        """
        self._no_privileges = no_privileges

    @property
    def parent_account(self):
        """Gets the parent_account of this QueryUserDetailResp.

        父用户

        :return: The parent_account of this QueryUserDetailResp.
        :rtype: str
        """
        return self._parent_account

    @parent_account.setter
    def parent_account(self, parent_account):
        """Sets the parent_account of this QueryUserDetailResp.

        父用户

        :param parent_account: The parent_account of this QueryUserDetailResp.
        :type parent_account: str
        """
        self._parent_account = parent_account

    @property
    def no_parent_account(self):
        """Gets the no_parent_account of this QueryUserDetailResp.

        无法同步父子关系的父用户

        :return: The no_parent_account of this QueryUserDetailResp.
        :rtype: str
        """
        return self._no_parent_account

    @no_parent_account.setter
    def no_parent_account(self, no_parent_account):
        """Sets the no_parent_account of this QueryUserDetailResp.

        无法同步父子关系的父用户

        :param no_parent_account: The no_parent_account of this QueryUserDetailResp.
        :type no_parent_account: str
        """
        self._no_parent_account = no_parent_account

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
        if not isinstance(other, QueryUserDetailResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
