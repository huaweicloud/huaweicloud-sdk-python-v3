# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MemberRoleVo:

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
        'extension_count': 'int',
        'role': 'str',
        'role_id': 'int',
        'role_value': 'str',
        'user_id': 'str',
        'user_name': 'str'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'extension_count': 'extension_count',
        'role': 'role',
        'role_id': 'role_id',
        'role_value': 'role_value',
        'user_id': 'user_id',
        'user_name': 'user_name'
    }

    def __init__(self, domain_id=None, extension_count=None, role=None, role_id=None, role_value=None, user_id=None, user_name=None):
        r"""MemberRoleVo

        The model defined in huaweicloud sdk

        :param domain_id: 租户ID
        :type domain_id: str
        :param extension_count: 插件数量
        :type extension_count: int
        :param role: 角色名称
        :type role: str
        :param role_id: 角色ID
        :type role_id: int
        :param role_value: 发布商或插件ID
        :type role_value: str
        :param user_id: 用户ID
        :type user_id: str
        :param user_name: 用户名
        :type user_name: str
        """
        
        

        self._domain_id = None
        self._extension_count = None
        self._role = None
        self._role_id = None
        self._role_value = None
        self._user_id = None
        self._user_name = None
        self.discriminator = None

        if domain_id is not None:
            self.domain_id = domain_id
        if extension_count is not None:
            self.extension_count = extension_count
        if role is not None:
            self.role = role
        if role_id is not None:
            self.role_id = role_id
        if role_value is not None:
            self.role_value = role_value
        if user_id is not None:
            self.user_id = user_id
        if user_name is not None:
            self.user_name = user_name

    @property
    def domain_id(self):
        r"""Gets the domain_id of this MemberRoleVo.

        租户ID

        :return: The domain_id of this MemberRoleVo.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this MemberRoleVo.

        租户ID

        :param domain_id: The domain_id of this MemberRoleVo.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def extension_count(self):
        r"""Gets the extension_count of this MemberRoleVo.

        插件数量

        :return: The extension_count of this MemberRoleVo.
        :rtype: int
        """
        return self._extension_count

    @extension_count.setter
    def extension_count(self, extension_count):
        r"""Sets the extension_count of this MemberRoleVo.

        插件数量

        :param extension_count: The extension_count of this MemberRoleVo.
        :type extension_count: int
        """
        self._extension_count = extension_count

    @property
    def role(self):
        r"""Gets the role of this MemberRoleVo.

        角色名称

        :return: The role of this MemberRoleVo.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        r"""Sets the role of this MemberRoleVo.

        角色名称

        :param role: The role of this MemberRoleVo.
        :type role: str
        """
        self._role = role

    @property
    def role_id(self):
        r"""Gets the role_id of this MemberRoleVo.

        角色ID

        :return: The role_id of this MemberRoleVo.
        :rtype: int
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id):
        r"""Sets the role_id of this MemberRoleVo.

        角色ID

        :param role_id: The role_id of this MemberRoleVo.
        :type role_id: int
        """
        self._role_id = role_id

    @property
    def role_value(self):
        r"""Gets the role_value of this MemberRoleVo.

        发布商或插件ID

        :return: The role_value of this MemberRoleVo.
        :rtype: str
        """
        return self._role_value

    @role_value.setter
    def role_value(self, role_value):
        r"""Sets the role_value of this MemberRoleVo.

        发布商或插件ID

        :param role_value: The role_value of this MemberRoleVo.
        :type role_value: str
        """
        self._role_value = role_value

    @property
    def user_id(self):
        r"""Gets the user_id of this MemberRoleVo.

        用户ID

        :return: The user_id of this MemberRoleVo.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this MemberRoleVo.

        用户ID

        :param user_id: The user_id of this MemberRoleVo.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def user_name(self):
        r"""Gets the user_name of this MemberRoleVo.

        用户名

        :return: The user_name of this MemberRoleVo.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this MemberRoleVo.

        用户名

        :param user_name: The user_name of this MemberRoleVo.
        :type user_name: str
        """
        self._user_name = user_name

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
        if not isinstance(other, MemberRoleVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
