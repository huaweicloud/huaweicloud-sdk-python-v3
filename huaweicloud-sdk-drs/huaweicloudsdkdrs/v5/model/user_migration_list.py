# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UserMigrationList:

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
        'is_set_password': 'bool',
        'password': 'str'
    }

    attribute_map = {
        'id': 'id',
        'account': 'account',
        'is_set_password': 'is_set_password',
        'password': 'password'
    }

    def __init__(self, id=None, account=None, is_set_password=None, password=None):
        r"""UserMigrationList

        The model defined in huaweicloud sdk

        :param id: 用户ID。
        :type id: str
        :param account: 用户。
        :type account: str
        :param is_set_password: 是否重置该用户密码。当前支持的场景： - 实时迁移场景：MySQL迁移。
        :type is_set_password: bool
        :param password: 重置后的密码。统一重置密码或单个用户重置密码为true时必填，约束：密码不能为空。
        :type password: str
        """
        
        

        self._id = None
        self._account = None
        self._is_set_password = None
        self._password = None
        self.discriminator = None

        self.id = id
        self.account = account
        if is_set_password is not None:
            self.is_set_password = is_set_password
        if password is not None:
            self.password = password

    @property
    def id(self):
        r"""Gets the id of this UserMigrationList.

        用户ID。

        :return: The id of this UserMigrationList.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this UserMigrationList.

        用户ID。

        :param id: The id of this UserMigrationList.
        :type id: str
        """
        self._id = id

    @property
    def account(self):
        r"""Gets the account of this UserMigrationList.

        用户。

        :return: The account of this UserMigrationList.
        :rtype: str
        """
        return self._account

    @account.setter
    def account(self, account):
        r"""Sets the account of this UserMigrationList.

        用户。

        :param account: The account of this UserMigrationList.
        :type account: str
        """
        self._account = account

    @property
    def is_set_password(self):
        r"""Gets the is_set_password of this UserMigrationList.

        是否重置该用户密码。当前支持的场景： - 实时迁移场景：MySQL迁移。

        :return: The is_set_password of this UserMigrationList.
        :rtype: bool
        """
        return self._is_set_password

    @is_set_password.setter
    def is_set_password(self, is_set_password):
        r"""Sets the is_set_password of this UserMigrationList.

        是否重置该用户密码。当前支持的场景： - 实时迁移场景：MySQL迁移。

        :param is_set_password: The is_set_password of this UserMigrationList.
        :type is_set_password: bool
        """
        self._is_set_password = is_set_password

    @property
    def password(self):
        r"""Gets the password of this UserMigrationList.

        重置后的密码。统一重置密码或单个用户重置密码为true时必填，约束：密码不能为空。

        :return: The password of this UserMigrationList.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        r"""Sets the password of this UserMigrationList.

        重置后的密码。统一重置密码或单个用户重置密码为true时必填，约束：密码不能为空。

        :param password: The password of this UserMigrationList.
        :type password: str
        """
        self._password = password

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
        if not isinstance(other, UserMigrationList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
