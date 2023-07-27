# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UserBasicDto:

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
        'avatar_path': 'str',
        'email': 'str',
        'name_cn': 'str',
        'web_url': 'str',
        'nick_name': 'str',
        'tenant_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'username': 'username',
        'state': 'state',
        'avatar_url': 'avatar_url',
        'avatar_path': 'avatar_path',
        'email': 'email',
        'name_cn': 'name_cn',
        'web_url': 'web_url',
        'nick_name': 'nick_name',
        'tenant_name': 'tenant_name'
    }

    def __init__(self, id=None, name=None, username=None, state=None, avatar_url=None, avatar_path=None, email=None, name_cn=None, web_url=None, nick_name=None, tenant_name=None):
        """UserBasicDto

        The model defined in huaweicloud sdk

        :param id: 用户id
        :type id: int
        :param name: 姓名
        :type name: str
        :param username: 用户名
        :type username: str
        :param state: 状态
        :type state: str
        :param avatar_url: 头像url
        :type avatar_url: str
        :param avatar_path: 头像路径
        :type avatar_path: str
        :param email: 邮箱
        :type email: str
        :param name_cn: 中文名
        :type name_cn: str
        :param web_url: 主页
        :type web_url: str
        :param nick_name: 昵称
        :type nick_name: str
        :param tenant_name: 租户名称
        :type tenant_name: str
        """
        
        

        self._id = None
        self._name = None
        self._username = None
        self._state = None
        self._avatar_url = None
        self._avatar_path = None
        self._email = None
        self._name_cn = None
        self._web_url = None
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
        if avatar_path is not None:
            self.avatar_path = avatar_path
        if email is not None:
            self.email = email
        if name_cn is not None:
            self.name_cn = name_cn
        if web_url is not None:
            self.web_url = web_url
        if nick_name is not None:
            self.nick_name = nick_name
        if tenant_name is not None:
            self.tenant_name = tenant_name

    @property
    def id(self):
        """Gets the id of this UserBasicDto.

        用户id

        :return: The id of this UserBasicDto.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserBasicDto.

        用户id

        :param id: The id of this UserBasicDto.
        :type id: int
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this UserBasicDto.

        姓名

        :return: The name of this UserBasicDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UserBasicDto.

        姓名

        :param name: The name of this UserBasicDto.
        :type name: str
        """
        self._name = name

    @property
    def username(self):
        """Gets the username of this UserBasicDto.

        用户名

        :return: The username of this UserBasicDto.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this UserBasicDto.

        用户名

        :param username: The username of this UserBasicDto.
        :type username: str
        """
        self._username = username

    @property
    def state(self):
        """Gets the state of this UserBasicDto.

        状态

        :return: The state of this UserBasicDto.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this UserBasicDto.

        状态

        :param state: The state of this UserBasicDto.
        :type state: str
        """
        self._state = state

    @property
    def avatar_url(self):
        """Gets the avatar_url of this UserBasicDto.

        头像url

        :return: The avatar_url of this UserBasicDto.
        :rtype: str
        """
        return self._avatar_url

    @avatar_url.setter
    def avatar_url(self, avatar_url):
        """Sets the avatar_url of this UserBasicDto.

        头像url

        :param avatar_url: The avatar_url of this UserBasicDto.
        :type avatar_url: str
        """
        self._avatar_url = avatar_url

    @property
    def avatar_path(self):
        """Gets the avatar_path of this UserBasicDto.

        头像路径

        :return: The avatar_path of this UserBasicDto.
        :rtype: str
        """
        return self._avatar_path

    @avatar_path.setter
    def avatar_path(self, avatar_path):
        """Sets the avatar_path of this UserBasicDto.

        头像路径

        :param avatar_path: The avatar_path of this UserBasicDto.
        :type avatar_path: str
        """
        self._avatar_path = avatar_path

    @property
    def email(self):
        """Gets the email of this UserBasicDto.

        邮箱

        :return: The email of this UserBasicDto.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this UserBasicDto.

        邮箱

        :param email: The email of this UserBasicDto.
        :type email: str
        """
        self._email = email

    @property
    def name_cn(self):
        """Gets the name_cn of this UserBasicDto.

        中文名

        :return: The name_cn of this UserBasicDto.
        :rtype: str
        """
        return self._name_cn

    @name_cn.setter
    def name_cn(self, name_cn):
        """Sets the name_cn of this UserBasicDto.

        中文名

        :param name_cn: The name_cn of this UserBasicDto.
        :type name_cn: str
        """
        self._name_cn = name_cn

    @property
    def web_url(self):
        """Gets the web_url of this UserBasicDto.

        主页

        :return: The web_url of this UserBasicDto.
        :rtype: str
        """
        return self._web_url

    @web_url.setter
    def web_url(self, web_url):
        """Sets the web_url of this UserBasicDto.

        主页

        :param web_url: The web_url of this UserBasicDto.
        :type web_url: str
        """
        self._web_url = web_url

    @property
    def nick_name(self):
        """Gets the nick_name of this UserBasicDto.

        昵称

        :return: The nick_name of this UserBasicDto.
        :rtype: str
        """
        return self._nick_name

    @nick_name.setter
    def nick_name(self, nick_name):
        """Sets the nick_name of this UserBasicDto.

        昵称

        :param nick_name: The nick_name of this UserBasicDto.
        :type nick_name: str
        """
        self._nick_name = nick_name

    @property
    def tenant_name(self):
        """Gets the tenant_name of this UserBasicDto.

        租户名称

        :return: The tenant_name of this UserBasicDto.
        :rtype: str
        """
        return self._tenant_name

    @tenant_name.setter
    def tenant_name(self, tenant_name):
        """Sets the tenant_name of this UserBasicDto.

        租户名称

        :param tenant_name: The tenant_name of this UserBasicDto.
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
        if not isinstance(other, UserBasicDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
