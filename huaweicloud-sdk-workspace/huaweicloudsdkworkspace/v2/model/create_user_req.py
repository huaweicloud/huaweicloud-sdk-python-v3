# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateUserReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user_name': 'str',
        'user_email': 'str',
        'account_expires': 'str',
        'enable_change_password': 'bool',
        'next_login_change_password': 'bool',
        'group_ids': 'list[str]',
        'description': 'str',
        'alias_name': 'str'
    }

    attribute_map = {
        'user_name': 'user_name',
        'user_email': 'user_email',
        'account_expires': 'account_expires',
        'enable_change_password': 'enable_change_password',
        'next_login_change_password': 'next_login_change_password',
        'group_ids': 'group_ids',
        'description': 'description',
        'alias_name': 'alias_name'
    }

    def __init__(self, user_name=None, user_email=None, account_expires=None, enable_change_password=None, next_login_change_password=None, group_ids=None, description=None, alias_name=None):
        """CreateUserReq

        The model defined in huaweicloud sdk

        :param user_name: 用户名称。
        :type user_name: str
        :param user_email: 用户邮箱。
        :type user_email: str
        :param account_expires: 账户过期时间，0表示永远不过期。时间格式：yyyy-MM-ddTHH:mm:ssZ或yyyy-MM-ddTHH:mm:ss.SSSZ。
        :type account_expires: str
        :param enable_change_password: 是否允许用户更改密码，缺省值为true。
        :type enable_change_password: bool
        :param next_login_change_password: 下次登录是否必须更改密码，缺省值为true。
        :type next_login_change_password: bool
        :param group_ids: 用户组的专有ID列表。
        :type group_ids: list[str]
        :param description: 用户描述，字符串长度区间[0, 255]。
        :type description: str
        :param alias_name: 别名。
        :type alias_name: str
        """
        
        

        self._user_name = None
        self._user_email = None
        self._account_expires = None
        self._enable_change_password = None
        self._next_login_change_password = None
        self._group_ids = None
        self._description = None
        self._alias_name = None
        self.discriminator = None

        self.user_name = user_name
        if user_email is not None:
            self.user_email = user_email
        if account_expires is not None:
            self.account_expires = account_expires
        if enable_change_password is not None:
            self.enable_change_password = enable_change_password
        if next_login_change_password is not None:
            self.next_login_change_password = next_login_change_password
        if group_ids is not None:
            self.group_ids = group_ids
        if description is not None:
            self.description = description
        if alias_name is not None:
            self.alias_name = alias_name

    @property
    def user_name(self):
        """Gets the user_name of this CreateUserReq.

        用户名称。

        :return: The user_name of this CreateUserReq.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this CreateUserReq.

        用户名称。

        :param user_name: The user_name of this CreateUserReq.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def user_email(self):
        """Gets the user_email of this CreateUserReq.

        用户邮箱。

        :return: The user_email of this CreateUserReq.
        :rtype: str
        """
        return self._user_email

    @user_email.setter
    def user_email(self, user_email):
        """Sets the user_email of this CreateUserReq.

        用户邮箱。

        :param user_email: The user_email of this CreateUserReq.
        :type user_email: str
        """
        self._user_email = user_email

    @property
    def account_expires(self):
        """Gets the account_expires of this CreateUserReq.

        账户过期时间，0表示永远不过期。时间格式：yyyy-MM-ddTHH:mm:ssZ或yyyy-MM-ddTHH:mm:ss.SSSZ。

        :return: The account_expires of this CreateUserReq.
        :rtype: str
        """
        return self._account_expires

    @account_expires.setter
    def account_expires(self, account_expires):
        """Sets the account_expires of this CreateUserReq.

        账户过期时间，0表示永远不过期。时间格式：yyyy-MM-ddTHH:mm:ssZ或yyyy-MM-ddTHH:mm:ss.SSSZ。

        :param account_expires: The account_expires of this CreateUserReq.
        :type account_expires: str
        """
        self._account_expires = account_expires

    @property
    def enable_change_password(self):
        """Gets the enable_change_password of this CreateUserReq.

        是否允许用户更改密码，缺省值为true。

        :return: The enable_change_password of this CreateUserReq.
        :rtype: bool
        """
        return self._enable_change_password

    @enable_change_password.setter
    def enable_change_password(self, enable_change_password):
        """Sets the enable_change_password of this CreateUserReq.

        是否允许用户更改密码，缺省值为true。

        :param enable_change_password: The enable_change_password of this CreateUserReq.
        :type enable_change_password: bool
        """
        self._enable_change_password = enable_change_password

    @property
    def next_login_change_password(self):
        """Gets the next_login_change_password of this CreateUserReq.

        下次登录是否必须更改密码，缺省值为true。

        :return: The next_login_change_password of this CreateUserReq.
        :rtype: bool
        """
        return self._next_login_change_password

    @next_login_change_password.setter
    def next_login_change_password(self, next_login_change_password):
        """Sets the next_login_change_password of this CreateUserReq.

        下次登录是否必须更改密码，缺省值为true。

        :param next_login_change_password: The next_login_change_password of this CreateUserReq.
        :type next_login_change_password: bool
        """
        self._next_login_change_password = next_login_change_password

    @property
    def group_ids(self):
        """Gets the group_ids of this CreateUserReq.

        用户组的专有ID列表。

        :return: The group_ids of this CreateUserReq.
        :rtype: list[str]
        """
        return self._group_ids

    @group_ids.setter
    def group_ids(self, group_ids):
        """Sets the group_ids of this CreateUserReq.

        用户组的专有ID列表。

        :param group_ids: The group_ids of this CreateUserReq.
        :type group_ids: list[str]
        """
        self._group_ids = group_ids

    @property
    def description(self):
        """Gets the description of this CreateUserReq.

        用户描述，字符串长度区间[0, 255]。

        :return: The description of this CreateUserReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateUserReq.

        用户描述，字符串长度区间[0, 255]。

        :param description: The description of this CreateUserReq.
        :type description: str
        """
        self._description = description

    @property
    def alias_name(self):
        """Gets the alias_name of this CreateUserReq.

        别名。

        :return: The alias_name of this CreateUserReq.
        :rtype: str
        """
        return self._alias_name

    @alias_name.setter
    def alias_name(self, alias_name):
        """Sets the alias_name of this CreateUserReq.

        别名。

        :param alias_name: The alias_name of this CreateUserReq.
        :type alias_name: str
        """
        self._alias_name = alias_name

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
        if not isinstance(other, CreateUserReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
