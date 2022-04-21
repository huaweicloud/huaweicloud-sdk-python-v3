# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UserAccountVO:

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
        'privileges': 'list[str]',
        'password': 'str',
        'is_set_password': 'bool',
        'roles': 'list[str]',
        'selected': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'account': 'account',
        'comment': 'comment',
        'is_transfer': 'is_transfer',
        'privileges': 'privileges',
        'password': 'password',
        'is_set_password': 'is_set_password',
        'roles': 'roles',
        'selected': 'selected'
    }

    def __init__(self, id=None, account=None, comment=None, is_transfer=None, privileges=None, password=None, is_set_password=None, roles=None, selected=None):
        """UserAccountVO

        The model defined in huaweicloud sdk

        :param id: 用户账户ID。
        :type id: str
        :param account: 用户
        :type account: str
        :param comment: 说明
        :type comment: str
        :param is_transfer: 是否支持迁移
        :type is_transfer: bool
        :param privileges: 权限列表
        :type privileges: list[str]
        :param password: 密码
        :type password: str
        :param is_set_password: 是否重置密码。
        :type is_set_password: bool
        :param roles: 角色
        :type roles: list[str]
        :param selected: 是否选择。
        :type selected: bool
        """
        
        

        self._id = None
        self._account = None
        self._comment = None
        self._is_transfer = None
        self._privileges = None
        self._password = None
        self._is_set_password = None
        self._roles = None
        self._selected = None
        self.discriminator = None

        self.id = id
        self.account = account
        if comment is not None:
            self.comment = comment
        self.is_transfer = is_transfer
        if privileges is not None:
            self.privileges = privileges
        if password is not None:
            self.password = password
        if is_set_password is not None:
            self.is_set_password = is_set_password
        self.roles = roles
        self.selected = selected

    @property
    def id(self):
        """Gets the id of this UserAccountVO.

        用户账户ID。

        :return: The id of this UserAccountVO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserAccountVO.

        用户账户ID。

        :param id: The id of this UserAccountVO.
        :type id: str
        """
        self._id = id

    @property
    def account(self):
        """Gets the account of this UserAccountVO.

        用户

        :return: The account of this UserAccountVO.
        :rtype: str
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this UserAccountVO.

        用户

        :param account: The account of this UserAccountVO.
        :type account: str
        """
        self._account = account

    @property
    def comment(self):
        """Gets the comment of this UserAccountVO.

        说明

        :return: The comment of this UserAccountVO.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this UserAccountVO.

        说明

        :param comment: The comment of this UserAccountVO.
        :type comment: str
        """
        self._comment = comment

    @property
    def is_transfer(self):
        """Gets the is_transfer of this UserAccountVO.

        是否支持迁移

        :return: The is_transfer of this UserAccountVO.
        :rtype: bool
        """
        return self._is_transfer

    @is_transfer.setter
    def is_transfer(self, is_transfer):
        """Sets the is_transfer of this UserAccountVO.

        是否支持迁移

        :param is_transfer: The is_transfer of this UserAccountVO.
        :type is_transfer: bool
        """
        self._is_transfer = is_transfer

    @property
    def privileges(self):
        """Gets the privileges of this UserAccountVO.

        权限列表

        :return: The privileges of this UserAccountVO.
        :rtype: list[str]
        """
        return self._privileges

    @privileges.setter
    def privileges(self, privileges):
        """Sets the privileges of this UserAccountVO.

        权限列表

        :param privileges: The privileges of this UserAccountVO.
        :type privileges: list[str]
        """
        self._privileges = privileges

    @property
    def password(self):
        """Gets the password of this UserAccountVO.

        密码

        :return: The password of this UserAccountVO.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this UserAccountVO.

        密码

        :param password: The password of this UserAccountVO.
        :type password: str
        """
        self._password = password

    @property
    def is_set_password(self):
        """Gets the is_set_password of this UserAccountVO.

        是否重置密码。

        :return: The is_set_password of this UserAccountVO.
        :rtype: bool
        """
        return self._is_set_password

    @is_set_password.setter
    def is_set_password(self, is_set_password):
        """Sets the is_set_password of this UserAccountVO.

        是否重置密码。

        :param is_set_password: The is_set_password of this UserAccountVO.
        :type is_set_password: bool
        """
        self._is_set_password = is_set_password

    @property
    def roles(self):
        """Gets the roles of this UserAccountVO.

        角色

        :return: The roles of this UserAccountVO.
        :rtype: list[str]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this UserAccountVO.

        角色

        :param roles: The roles of this UserAccountVO.
        :type roles: list[str]
        """
        self._roles = roles

    @property
    def selected(self):
        """Gets the selected of this UserAccountVO.

        是否选择。

        :return: The selected of this UserAccountVO.
        :rtype: bool
        """
        return self._selected

    @selected.setter
    def selected(self, selected):
        """Sets the selected of this UserAccountVO.

        是否选择。

        :param selected: The selected of this UserAccountVO.
        :type selected: bool
        """
        self._selected = selected

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
        if not isinstance(other, UserAccountVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
