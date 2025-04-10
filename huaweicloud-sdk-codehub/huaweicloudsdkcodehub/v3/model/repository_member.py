# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RepositoryMember:

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
        'domain_id': 'str',
        'domain_name': 'str',
        'email': 'str',
        'enabled': 'str',
        'name': 'str',
        'role': 'int',
        'user_id': 'str'
    }

    attribute_map = {
        'description': 'description',
        'domain_id': 'domain_id',
        'domain_name': 'domain_name',
        'email': 'email',
        'enabled': 'enabled',
        'name': 'name',
        'role': 'role',
        'user_id': 'user_id'
    }

    def __init__(self, description=None, domain_id=None, domain_name=None, email=None, enabled=None, name=None, role=None, user_id=None):
        r"""RepositoryMember

        The model defined in huaweicloud sdk

        :param description: 仓库成员描述
        :type description: str
        :param domain_id: 租户id
        :type domain_id: str
        :param domain_name: 租户名
        :type domain_name: str
        :param email: 邮箱地址
        :type email: str
        :param enabled: 成员是否可用
        :type enabled: str
        :param name: 用户名
        :type name: str
        :param role: 仓库用户权限，取值范围：30-&gt;普通成员，40-&gt;管理员
        :type role: int
        :param user_id: 用户id
        :type user_id: str
        """
        
        

        self._description = None
        self._domain_id = None
        self._domain_name = None
        self._email = None
        self._enabled = None
        self._name = None
        self._role = None
        self._user_id = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if domain_id is not None:
            self.domain_id = domain_id
        if domain_name is not None:
            self.domain_name = domain_name
        if email is not None:
            self.email = email
        if enabled is not None:
            self.enabled = enabled
        if name is not None:
            self.name = name
        if role is not None:
            self.role = role
        if user_id is not None:
            self.user_id = user_id

    @property
    def description(self):
        r"""Gets the description of this RepositoryMember.

        仓库成员描述

        :return: The description of this RepositoryMember.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this RepositoryMember.

        仓库成员描述

        :param description: The description of this RepositoryMember.
        :type description: str
        """
        self._description = description

    @property
    def domain_id(self):
        r"""Gets the domain_id of this RepositoryMember.

        租户id

        :return: The domain_id of this RepositoryMember.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this RepositoryMember.

        租户id

        :param domain_id: The domain_id of this RepositoryMember.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def domain_name(self):
        r"""Gets the domain_name of this RepositoryMember.

        租户名

        :return: The domain_name of this RepositoryMember.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this RepositoryMember.

        租户名

        :param domain_name: The domain_name of this RepositoryMember.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def email(self):
        r"""Gets the email of this RepositoryMember.

        邮箱地址

        :return: The email of this RepositoryMember.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        r"""Sets the email of this RepositoryMember.

        邮箱地址

        :param email: The email of this RepositoryMember.
        :type email: str
        """
        self._email = email

    @property
    def enabled(self):
        r"""Gets the enabled of this RepositoryMember.

        成员是否可用

        :return: The enabled of this RepositoryMember.
        :rtype: str
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this RepositoryMember.

        成员是否可用

        :param enabled: The enabled of this RepositoryMember.
        :type enabled: str
        """
        self._enabled = enabled

    @property
    def name(self):
        r"""Gets the name of this RepositoryMember.

        用户名

        :return: The name of this RepositoryMember.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this RepositoryMember.

        用户名

        :param name: The name of this RepositoryMember.
        :type name: str
        """
        self._name = name

    @property
    def role(self):
        r"""Gets the role of this RepositoryMember.

        仓库用户权限，取值范围：30->普通成员，40->管理员

        :return: The role of this RepositoryMember.
        :rtype: int
        """
        return self._role

    @role.setter
    def role(self, role):
        r"""Sets the role of this RepositoryMember.

        仓库用户权限，取值范围：30->普通成员，40->管理员

        :param role: The role of this RepositoryMember.
        :type role: int
        """
        self._role = role

    @property
    def user_id(self):
        r"""Gets the user_id of this RepositoryMember.

        用户id

        :return: The user_id of this RepositoryMember.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this RepositoryMember.

        用户id

        :param user_id: The user_id of this RepositoryMember.
        :type user_id: str
        """
        self._user_id = user_id

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
        if not isinstance(other, RepositoryMember):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
