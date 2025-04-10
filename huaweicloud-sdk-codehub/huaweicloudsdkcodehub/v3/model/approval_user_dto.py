# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApprovalUserDto:

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
        'username': 'str',
        'name': 'str',
        'nick_name': 'str',
        'state': 'str'
    }

    attribute_map = {
        'id': 'id',
        'username': 'username',
        'name': 'name',
        'nick_name': 'nick_name',
        'state': 'state'
    }

    def __init__(self, id=None, username=None, name=None, nick_name=None, state=None):
        r"""ApprovalUserDto

        The model defined in huaweicloud sdk

        :param id: id
        :type id: int
        :param username: 用户名
        :type username: str
        :param name: 名称
        :type name: str
        :param nick_name: 昵称
        :type nick_name: str
        :param state: 检视状态
        :type state: str
        """
        
        

        self._id = None
        self._username = None
        self._name = None
        self._nick_name = None
        self._state = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if username is not None:
            self.username = username
        if name is not None:
            self.name = name
        if nick_name is not None:
            self.nick_name = nick_name
        if state is not None:
            self.state = state

    @property
    def id(self):
        r"""Gets the id of this ApprovalUserDto.

        id

        :return: The id of this ApprovalUserDto.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ApprovalUserDto.

        id

        :param id: The id of this ApprovalUserDto.
        :type id: int
        """
        self._id = id

    @property
    def username(self):
        r"""Gets the username of this ApprovalUserDto.

        用户名

        :return: The username of this ApprovalUserDto.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        r"""Sets the username of this ApprovalUserDto.

        用户名

        :param username: The username of this ApprovalUserDto.
        :type username: str
        """
        self._username = username

    @property
    def name(self):
        r"""Gets the name of this ApprovalUserDto.

        名称

        :return: The name of this ApprovalUserDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ApprovalUserDto.

        名称

        :param name: The name of this ApprovalUserDto.
        :type name: str
        """
        self._name = name

    @property
    def nick_name(self):
        r"""Gets the nick_name of this ApprovalUserDto.

        昵称

        :return: The nick_name of this ApprovalUserDto.
        :rtype: str
        """
        return self._nick_name

    @nick_name.setter
    def nick_name(self, nick_name):
        r"""Sets the nick_name of this ApprovalUserDto.

        昵称

        :param nick_name: The nick_name of this ApprovalUserDto.
        :type nick_name: str
        """
        self._nick_name = nick_name

    @property
    def state(self):
        r"""Gets the state of this ApprovalUserDto.

        检视状态

        :return: The state of this ApprovalUserDto.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this ApprovalUserDto.

        检视状态

        :param state: The state of this ApprovalUserDto.
        :type state: str
        """
        self._state = state

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
        if not isinstance(other, ApprovalUserDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
