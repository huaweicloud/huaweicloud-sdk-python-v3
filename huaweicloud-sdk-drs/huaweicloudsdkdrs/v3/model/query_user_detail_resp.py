# coding: utf-8

import re
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
        'privileges': 'list[str]',
        'password': 'str',
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
        'roles': 'roles',
        'selected': 'selected'
    }

    def __init__(self, id=None, account=None, comment=None, is_transfer=None, privileges=None, password=None, roles=None, selected=None):
        """QueryUserDetailResp - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._account = None
        self._comment = None
        self._is_transfer = None
        self._privileges = None
        self._password = None
        self._roles = None
        self._selected = None
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
        :type: str
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
        :type: str
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
        :type: str
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
        :type: bool
        """
        self._is_transfer = is_transfer

    @property
    def privileges(self):
        """Gets the privileges of this QueryUserDetailResp.

        权限

        :return: The privileges of this QueryUserDetailResp.
        :rtype: list[str]
        """
        return self._privileges

    @privileges.setter
    def privileges(self, privileges):
        """Sets the privileges of this QueryUserDetailResp.

        权限

        :param privileges: The privileges of this QueryUserDetailResp.
        :type: list[str]
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
        :type: str
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
        :type: list[str]
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
        :type: bool
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
        if not isinstance(other, QueryUserDetailResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
