# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UserVO:

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
        'user_num_id': 'int',
        'user_name': 'str',
        'domain_id': 'str',
        'domain_name': 'str',
        'nick_name': 'str',
        'role_id': 'str',
        'role_name': 'str',
        'role_code': 'str'
    }

    attribute_map = {
        'user_id': 'user_id',
        'user_num_id': 'user_num_id',
        'user_name': 'user_name',
        'domain_id': 'domain_id',
        'domain_name': 'domain_name',
        'nick_name': 'nick_name',
        'role_id': 'role_id',
        'role_name': 'role_name',
        'role_code': 'role_code'
    }

    def __init__(self, user_id=None, user_num_id=None, user_name=None, domain_id=None, domain_name=None, nick_name=None, role_id=None, role_name=None, role_code=None):
        r"""UserVO

        The model defined in huaweicloud sdk

        :param user_id: 用户ID。
        :type user_id: str
        :param user_num_id: 用户短ID。
        :type user_num_id: int
        :param user_name: 用户名称。
        :type user_name: str
        :param domain_id: 用户所属域ID。
        :type domain_id: str
        :param domain_name: 租户名称。
        :type domain_name: str
        :param nick_name: 用户昵称。
        :type nick_name: str
        :param role_id: 角色ID，用户在项目中具有多个角色时用英文逗号分隔。
        :type role_id: str
        :param role_name: 用户角色名称，多个角色用英文逗号分隔。
        :type role_name: str
        :param role_code: 用户角色编码，多个角色用英文逗号分隔。
        :type role_code: str
        """
        
        

        self._user_id = None
        self._user_num_id = None
        self._user_name = None
        self._domain_id = None
        self._domain_name = None
        self._nick_name = None
        self._role_id = None
        self._role_name = None
        self._role_code = None
        self.discriminator = None

        if user_id is not None:
            self.user_id = user_id
        if user_num_id is not None:
            self.user_num_id = user_num_id
        if user_name is not None:
            self.user_name = user_name
        if domain_id is not None:
            self.domain_id = domain_id
        if domain_name is not None:
            self.domain_name = domain_name
        if nick_name is not None:
            self.nick_name = nick_name
        if role_id is not None:
            self.role_id = role_id
        if role_name is not None:
            self.role_name = role_name
        if role_code is not None:
            self.role_code = role_code

    @property
    def user_id(self):
        r"""Gets the user_id of this UserVO.

        用户ID。

        :return: The user_id of this UserVO.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this UserVO.

        用户ID。

        :param user_id: The user_id of this UserVO.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def user_num_id(self):
        r"""Gets the user_num_id of this UserVO.

        用户短ID。

        :return: The user_num_id of this UserVO.
        :rtype: int
        """
        return self._user_num_id

    @user_num_id.setter
    def user_num_id(self, user_num_id):
        r"""Sets the user_num_id of this UserVO.

        用户短ID。

        :param user_num_id: The user_num_id of this UserVO.
        :type user_num_id: int
        """
        self._user_num_id = user_num_id

    @property
    def user_name(self):
        r"""Gets the user_name of this UserVO.

        用户名称。

        :return: The user_name of this UserVO.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this UserVO.

        用户名称。

        :param user_name: The user_name of this UserVO.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def domain_id(self):
        r"""Gets the domain_id of this UserVO.

        用户所属域ID。

        :return: The domain_id of this UserVO.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this UserVO.

        用户所属域ID。

        :param domain_id: The domain_id of this UserVO.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def domain_name(self):
        r"""Gets the domain_name of this UserVO.

        租户名称。

        :return: The domain_name of this UserVO.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this UserVO.

        租户名称。

        :param domain_name: The domain_name of this UserVO.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def nick_name(self):
        r"""Gets the nick_name of this UserVO.

        用户昵称。

        :return: The nick_name of this UserVO.
        :rtype: str
        """
        return self._nick_name

    @nick_name.setter
    def nick_name(self, nick_name):
        r"""Sets the nick_name of this UserVO.

        用户昵称。

        :param nick_name: The nick_name of this UserVO.
        :type nick_name: str
        """
        self._nick_name = nick_name

    @property
    def role_id(self):
        r"""Gets the role_id of this UserVO.

        角色ID，用户在项目中具有多个角色时用英文逗号分隔。

        :return: The role_id of this UserVO.
        :rtype: str
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id):
        r"""Sets the role_id of this UserVO.

        角色ID，用户在项目中具有多个角色时用英文逗号分隔。

        :param role_id: The role_id of this UserVO.
        :type role_id: str
        """
        self._role_id = role_id

    @property
    def role_name(self):
        r"""Gets the role_name of this UserVO.

        用户角色名称，多个角色用英文逗号分隔。

        :return: The role_name of this UserVO.
        :rtype: str
        """
        return self._role_name

    @role_name.setter
    def role_name(self, role_name):
        r"""Sets the role_name of this UserVO.

        用户角色名称，多个角色用英文逗号分隔。

        :param role_name: The role_name of this UserVO.
        :type role_name: str
        """
        self._role_name = role_name

    @property
    def role_code(self):
        r"""Gets the role_code of this UserVO.

        用户角色编码，多个角色用英文逗号分隔。

        :return: The role_code of this UserVO.
        :rtype: str
        """
        return self._role_code

    @role_code.setter
    def role_code(self, role_code):
        r"""Sets the role_code of this UserVO.

        用户角色编码，多个角色用英文逗号分隔。

        :param role_code: The role_code of this UserVO.
        :type role_code: str
        """
        self._role_code = role_code

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UserVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
