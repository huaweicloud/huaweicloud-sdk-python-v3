# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MemberListV4Members:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_id': 'str',
        'domain_name': 'str',
        'user_id': 'str',
        'user_name': 'str',
        'user_num_id': 'int',
        'role_id': 'int',
        'nick_name': 'str',
        'role_name': 'str',
        'user_type': 'str',
        'forbidden': 'int'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'domain_name': 'domain_name',
        'user_id': 'user_id',
        'user_name': 'user_name',
        'user_num_id': 'user_num_id',
        'role_id': 'role_id',
        'nick_name': 'nick_name',
        'role_name': 'role_name',
        'user_type': 'user_type',
        'forbidden': 'forbidden'
    }

    def __init__(self, domain_id=None, domain_name=None, user_id=None, user_name=None, user_num_id=None, role_id=None, nick_name=None, role_name=None, user_type=None, forbidden=None):
        """MemberListV4Members

        The model defined in huaweicloud sdk

        :param domain_id: 租户id
        :type domain_id: str
        :param domain_name: 租户名
        :type domain_name: str
        :param user_id: 用户id
        :type user_id: str
        :param user_name: 用户名
        :type user_name: str
        :param user_num_id: 创建人numId
        :type user_num_id: int
        :param role_id: 成员角色, -1 项目创建者, 3 项目经理, 4 开发人员, 5 测试经理, 6 测试人员, 7 参与者, 8 浏览者, 9 运维经理
        :type role_id: int
        :param nick_name: 用户昵称
        :type nick_name: str
        :param role_name: 用户角色
        :type role_name: str
        :param user_type: 用户类型, User iam用户, Federation 联邦账号,
        :type user_type: str
        :param forbidden: 是否是禁用账号，1 禁用账号， 0非禁用账号
        :type forbidden: int
        """
        
        

        self._domain_id = None
        self._domain_name = None
        self._user_id = None
        self._user_name = None
        self._user_num_id = None
        self._role_id = None
        self._nick_name = None
        self._role_name = None
        self._user_type = None
        self._forbidden = None
        self.discriminator = None

        if domain_id is not None:
            self.domain_id = domain_id
        if domain_name is not None:
            self.domain_name = domain_name
        if user_id is not None:
            self.user_id = user_id
        if user_name is not None:
            self.user_name = user_name
        if user_num_id is not None:
            self.user_num_id = user_num_id
        if role_id is not None:
            self.role_id = role_id
        if nick_name is not None:
            self.nick_name = nick_name
        if role_name is not None:
            self.role_name = role_name
        if user_type is not None:
            self.user_type = user_type
        if forbidden is not None:
            self.forbidden = forbidden

    @property
    def domain_id(self):
        """Gets the domain_id of this MemberListV4Members.

        租户id

        :return: The domain_id of this MemberListV4Members.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this MemberListV4Members.

        租户id

        :param domain_id: The domain_id of this MemberListV4Members.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def domain_name(self):
        """Gets the domain_name of this MemberListV4Members.

        租户名

        :return: The domain_name of this MemberListV4Members.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this MemberListV4Members.

        租户名

        :param domain_name: The domain_name of this MemberListV4Members.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def user_id(self):
        """Gets the user_id of this MemberListV4Members.

        用户id

        :return: The user_id of this MemberListV4Members.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this MemberListV4Members.

        用户id

        :param user_id: The user_id of this MemberListV4Members.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def user_name(self):
        """Gets the user_name of this MemberListV4Members.

        用户名

        :return: The user_name of this MemberListV4Members.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this MemberListV4Members.

        用户名

        :param user_name: The user_name of this MemberListV4Members.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def user_num_id(self):
        """Gets the user_num_id of this MemberListV4Members.

        创建人numId

        :return: The user_num_id of this MemberListV4Members.
        :rtype: int
        """
        return self._user_num_id

    @user_num_id.setter
    def user_num_id(self, user_num_id):
        """Sets the user_num_id of this MemberListV4Members.

        创建人numId

        :param user_num_id: The user_num_id of this MemberListV4Members.
        :type user_num_id: int
        """
        self._user_num_id = user_num_id

    @property
    def role_id(self):
        """Gets the role_id of this MemberListV4Members.

        成员角色, -1 项目创建者, 3 项目经理, 4 开发人员, 5 测试经理, 6 测试人员, 7 参与者, 8 浏览者, 9 运维经理

        :return: The role_id of this MemberListV4Members.
        :rtype: int
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id):
        """Sets the role_id of this MemberListV4Members.

        成员角色, -1 项目创建者, 3 项目经理, 4 开发人员, 5 测试经理, 6 测试人员, 7 参与者, 8 浏览者, 9 运维经理

        :param role_id: The role_id of this MemberListV4Members.
        :type role_id: int
        """
        self._role_id = role_id

    @property
    def nick_name(self):
        """Gets the nick_name of this MemberListV4Members.

        用户昵称

        :return: The nick_name of this MemberListV4Members.
        :rtype: str
        """
        return self._nick_name

    @nick_name.setter
    def nick_name(self, nick_name):
        """Sets the nick_name of this MemberListV4Members.

        用户昵称

        :param nick_name: The nick_name of this MemberListV4Members.
        :type nick_name: str
        """
        self._nick_name = nick_name

    @property
    def role_name(self):
        """Gets the role_name of this MemberListV4Members.

        用户角色

        :return: The role_name of this MemberListV4Members.
        :rtype: str
        """
        return self._role_name

    @role_name.setter
    def role_name(self, role_name):
        """Sets the role_name of this MemberListV4Members.

        用户角色

        :param role_name: The role_name of this MemberListV4Members.
        :type role_name: str
        """
        self._role_name = role_name

    @property
    def user_type(self):
        """Gets the user_type of this MemberListV4Members.

        用户类型, User iam用户, Federation 联邦账号,

        :return: The user_type of this MemberListV4Members.
        :rtype: str
        """
        return self._user_type

    @user_type.setter
    def user_type(self, user_type):
        """Sets the user_type of this MemberListV4Members.

        用户类型, User iam用户, Federation 联邦账号,

        :param user_type: The user_type of this MemberListV4Members.
        :type user_type: str
        """
        self._user_type = user_type

    @property
    def forbidden(self):
        """Gets the forbidden of this MemberListV4Members.

        是否是禁用账号，1 禁用账号， 0非禁用账号

        :return: The forbidden of this MemberListV4Members.
        :rtype: int
        """
        return self._forbidden

    @forbidden.setter
    def forbidden(self, forbidden):
        """Sets the forbidden of this MemberListV4Members.

        是否是禁用账号，1 禁用账号， 0非禁用账号

        :param forbidden: The forbidden of this MemberListV4Members.
        :type forbidden: int
        """
        self._forbidden = forbidden

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
        if not isinstance(other, MemberListV4Members):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
