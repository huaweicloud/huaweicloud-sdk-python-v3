# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RepositoryEventAuthorDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'name': 'str',
        'username': 'str',
        'state': 'str',
        'avatar_url': 'str',
        'name_cn': 'str',
        'nick_name': 'str',
        'tenant_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'username': 'username',
        'state': 'state',
        'avatar_url': 'avatar_url',
        'name_cn': 'name_cn',
        'nick_name': 'nick_name',
        'tenant_name': 'tenant_name'
    }

    def __init__(self, id=None, name=None, username=None, state=None, avatar_url=None, name_cn=None, nick_name=None, tenant_name=None):
        r"""RepositoryEventAuthorDto

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 用户id。
        :type id: int
        :param name: **参数解释：** 用户名称。
        :type name: str
        :param username: **参数解释：** 用户名。
        :type username: str
        :param state: **参数解释：** 状态。
        :type state: str
        :param avatar_url: **参数解释：** 头像地址。
        :type avatar_url: str
        :param name_cn: **参数解释：** 中文名。
        :type name_cn: str
        :param nick_name: **参数解释：** 昵称。
        :type nick_name: str
        :param tenant_name: **参数解释：** 租户名。
        :type tenant_name: str
        """
        
        

        self._id = None
        self._name = None
        self._username = None
        self._state = None
        self._avatar_url = None
        self._name_cn = None
        self._nick_name = None
        self._tenant_name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if username is not None:
            self.username = username
        if state is not None:
            self.state = state
        if avatar_url is not None:
            self.avatar_url = avatar_url
        if name_cn is not None:
            self.name_cn = name_cn
        if nick_name is not None:
            self.nick_name = nick_name
        if tenant_name is not None:
            self.tenant_name = tenant_name

    @property
    def id(self):
        r"""Gets the id of this RepositoryEventAuthorDto.

        **参数解释：** 用户id。

        :return: The id of this RepositoryEventAuthorDto.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this RepositoryEventAuthorDto.

        **参数解释：** 用户id。

        :param id: The id of this RepositoryEventAuthorDto.
        :type id: int
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this RepositoryEventAuthorDto.

        **参数解释：** 用户名称。

        :return: The name of this RepositoryEventAuthorDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this RepositoryEventAuthorDto.

        **参数解释：** 用户名称。

        :param name: The name of this RepositoryEventAuthorDto.
        :type name: str
        """
        self._name = name

    @property
    def username(self):
        r"""Gets the username of this RepositoryEventAuthorDto.

        **参数解释：** 用户名。

        :return: The username of this RepositoryEventAuthorDto.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        r"""Sets the username of this RepositoryEventAuthorDto.

        **参数解释：** 用户名。

        :param username: The username of this RepositoryEventAuthorDto.
        :type username: str
        """
        self._username = username

    @property
    def state(self):
        r"""Gets the state of this RepositoryEventAuthorDto.

        **参数解释：** 状态。

        :return: The state of this RepositoryEventAuthorDto.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this RepositoryEventAuthorDto.

        **参数解释：** 状态。

        :param state: The state of this RepositoryEventAuthorDto.
        :type state: str
        """
        self._state = state

    @property
    def avatar_url(self):
        r"""Gets the avatar_url of this RepositoryEventAuthorDto.

        **参数解释：** 头像地址。

        :return: The avatar_url of this RepositoryEventAuthorDto.
        :rtype: str
        """
        return self._avatar_url

    @avatar_url.setter
    def avatar_url(self, avatar_url):
        r"""Sets the avatar_url of this RepositoryEventAuthorDto.

        **参数解释：** 头像地址。

        :param avatar_url: The avatar_url of this RepositoryEventAuthorDto.
        :type avatar_url: str
        """
        self._avatar_url = avatar_url

    @property
    def name_cn(self):
        r"""Gets the name_cn of this RepositoryEventAuthorDto.

        **参数解释：** 中文名。

        :return: The name_cn of this RepositoryEventAuthorDto.
        :rtype: str
        """
        return self._name_cn

    @name_cn.setter
    def name_cn(self, name_cn):
        r"""Sets the name_cn of this RepositoryEventAuthorDto.

        **参数解释：** 中文名。

        :param name_cn: The name_cn of this RepositoryEventAuthorDto.
        :type name_cn: str
        """
        self._name_cn = name_cn

    @property
    def nick_name(self):
        r"""Gets the nick_name of this RepositoryEventAuthorDto.

        **参数解释：** 昵称。

        :return: The nick_name of this RepositoryEventAuthorDto.
        :rtype: str
        """
        return self._nick_name

    @nick_name.setter
    def nick_name(self, nick_name):
        r"""Sets the nick_name of this RepositoryEventAuthorDto.

        **参数解释：** 昵称。

        :param nick_name: The nick_name of this RepositoryEventAuthorDto.
        :type nick_name: str
        """
        self._nick_name = nick_name

    @property
    def tenant_name(self):
        r"""Gets the tenant_name of this RepositoryEventAuthorDto.

        **参数解释：** 租户名。

        :return: The tenant_name of this RepositoryEventAuthorDto.
        :rtype: str
        """
        return self._tenant_name

    @tenant_name.setter
    def tenant_name(self, tenant_name):
        r"""Sets the tenant_name of this RepositoryEventAuthorDto.

        **参数解释：** 租户名。

        :param tenant_name: The tenant_name of this RepositoryEventAuthorDto.
        :type tenant_name: str
        """
        self._tenant_name = tenant_name

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
        if not isinstance(other, RepositoryEventAuthorDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
