# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DatabaseUser:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'login': 'bool',
        'user_type': 'str'
    }

    attribute_map = {
        'name': 'name',
        'login': 'login',
        'user_type': 'user_type'
    }

    def __init__(self, name=None, login=None, user_type=None):
        r"""DatabaseUser

        The model defined in huaweicloud sdk

        :param name: **参数解释**： 用户名。 **取值范围**： 不涉及。
        :type name: str
        :param login: **参数解释**： 是否可以登录。 **取值范围**： 不涉及。
        :type login: bool
        :param user_type: **参数解释**： 用户类型。 **取值范围**： COMMON：表示普通数据库用户。 IAM：表示IAM同步的数据库用户。 OneAccess: 表示OneAccess用户。
        :type user_type: str
        """
        
        

        self._name = None
        self._login = None
        self._user_type = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if login is not None:
            self.login = login
        if user_type is not None:
            self.user_type = user_type

    @property
    def name(self):
        r"""Gets the name of this DatabaseUser.

        **参数解释**： 用户名。 **取值范围**： 不涉及。

        :return: The name of this DatabaseUser.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this DatabaseUser.

        **参数解释**： 用户名。 **取值范围**： 不涉及。

        :param name: The name of this DatabaseUser.
        :type name: str
        """
        self._name = name

    @property
    def login(self):
        r"""Gets the login of this DatabaseUser.

        **参数解释**： 是否可以登录。 **取值范围**： 不涉及。

        :return: The login of this DatabaseUser.
        :rtype: bool
        """
        return self._login

    @login.setter
    def login(self, login):
        r"""Sets the login of this DatabaseUser.

        **参数解释**： 是否可以登录。 **取值范围**： 不涉及。

        :param login: The login of this DatabaseUser.
        :type login: bool
        """
        self._login = login

    @property
    def user_type(self):
        r"""Gets the user_type of this DatabaseUser.

        **参数解释**： 用户类型。 **取值范围**： COMMON：表示普通数据库用户。 IAM：表示IAM同步的数据库用户。 OneAccess: 表示OneAccess用户。

        :return: The user_type of this DatabaseUser.
        :rtype: str
        """
        return self._user_type

    @user_type.setter
    def user_type(self, user_type):
        r"""Sets the user_type of this DatabaseUser.

        **参数解释**： 用户类型。 **取值范围**： COMMON：表示普通数据库用户。 IAM：表示IAM同步的数据库用户。 OneAccess: 表示OneAccess用户。

        :param user_type: The user_type of this DatabaseUser.
        :type user_type: str
        """
        self._user_type = user_type

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
        if not isinstance(other, DatabaseUser):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
