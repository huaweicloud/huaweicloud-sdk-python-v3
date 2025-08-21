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
        'name_cn': 'str',
        'email': 'str',
        'state': 'str',
        'updated_at': 'str',
        'avatar_url': 'str',
        'tenant_name': 'str',
        'approver_comment': 'str'
    }

    attribute_map = {
        'id': 'id',
        'username': 'username',
        'name': 'name',
        'nick_name': 'nick_name',
        'name_cn': 'name_cn',
        'email': 'email',
        'state': 'state',
        'updated_at': 'updated_at',
        'avatar_url': 'avatar_url',
        'tenant_name': 'tenant_name',
        'approver_comment': 'approver_comment'
    }

    def __init__(self, id=None, username=None, name=None, nick_name=None, name_cn=None, email=None, state=None, updated_at=None, avatar_url=None, tenant_name=None, approver_comment=None):
        r"""ApprovalUserDto

        The model defined in huaweicloud sdk

        :param id: 用户id
        :type id: int
        :param username: 用户名称
        :type username: str
        :param name: 用户名称
        :type name: str
        :param nick_name: 用户昵称
        :type nick_name: str
        :param name_cn: 中文名称
        :type name_cn: str
        :param email: 电子邮箱
        :type email: str
        :param state: 状态
        :type state: str
        :param updated_at: 更新时间
        :type updated_at: str
        :param avatar_url: 头像url
        :type avatar_url: str
        :param tenant_name: 租户名称
        :type tenant_name: str
        :param approver_comment: 审核意见
        :type approver_comment: str
        """
        
        

        self._id = None
        self._username = None
        self._name = None
        self._nick_name = None
        self._name_cn = None
        self._email = None
        self._state = None
        self._updated_at = None
        self._avatar_url = None
        self._tenant_name = None
        self._approver_comment = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if username is not None:
            self.username = username
        if name is not None:
            self.name = name
        if nick_name is not None:
            self.nick_name = nick_name
        if name_cn is not None:
            self.name_cn = name_cn
        if email is not None:
            self.email = email
        if state is not None:
            self.state = state
        if updated_at is not None:
            self.updated_at = updated_at
        if avatar_url is not None:
            self.avatar_url = avatar_url
        if tenant_name is not None:
            self.tenant_name = tenant_name
        if approver_comment is not None:
            self.approver_comment = approver_comment

    @property
    def id(self):
        r"""Gets the id of this ApprovalUserDto.

        用户id

        :return: The id of this ApprovalUserDto.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ApprovalUserDto.

        用户id

        :param id: The id of this ApprovalUserDto.
        :type id: int
        """
        self._id = id

    @property
    def username(self):
        r"""Gets the username of this ApprovalUserDto.

        用户名称

        :return: The username of this ApprovalUserDto.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        r"""Sets the username of this ApprovalUserDto.

        用户名称

        :param username: The username of this ApprovalUserDto.
        :type username: str
        """
        self._username = username

    @property
    def name(self):
        r"""Gets the name of this ApprovalUserDto.

        用户名称

        :return: The name of this ApprovalUserDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ApprovalUserDto.

        用户名称

        :param name: The name of this ApprovalUserDto.
        :type name: str
        """
        self._name = name

    @property
    def nick_name(self):
        r"""Gets the nick_name of this ApprovalUserDto.

        用户昵称

        :return: The nick_name of this ApprovalUserDto.
        :rtype: str
        """
        return self._nick_name

    @nick_name.setter
    def nick_name(self, nick_name):
        r"""Sets the nick_name of this ApprovalUserDto.

        用户昵称

        :param nick_name: The nick_name of this ApprovalUserDto.
        :type nick_name: str
        """
        self._nick_name = nick_name

    @property
    def name_cn(self):
        r"""Gets the name_cn of this ApprovalUserDto.

        中文名称

        :return: The name_cn of this ApprovalUserDto.
        :rtype: str
        """
        return self._name_cn

    @name_cn.setter
    def name_cn(self, name_cn):
        r"""Sets the name_cn of this ApprovalUserDto.

        中文名称

        :param name_cn: The name_cn of this ApprovalUserDto.
        :type name_cn: str
        """
        self._name_cn = name_cn

    @property
    def email(self):
        r"""Gets the email of this ApprovalUserDto.

        电子邮箱

        :return: The email of this ApprovalUserDto.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        r"""Sets the email of this ApprovalUserDto.

        电子邮箱

        :param email: The email of this ApprovalUserDto.
        :type email: str
        """
        self._email = email

    @property
    def state(self):
        r"""Gets the state of this ApprovalUserDto.

        状态

        :return: The state of this ApprovalUserDto.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this ApprovalUserDto.

        状态

        :param state: The state of this ApprovalUserDto.
        :type state: str
        """
        self._state = state

    @property
    def updated_at(self):
        r"""Gets the updated_at of this ApprovalUserDto.

        更新时间

        :return: The updated_at of this ApprovalUserDto.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this ApprovalUserDto.

        更新时间

        :param updated_at: The updated_at of this ApprovalUserDto.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def avatar_url(self):
        r"""Gets the avatar_url of this ApprovalUserDto.

        头像url

        :return: The avatar_url of this ApprovalUserDto.
        :rtype: str
        """
        return self._avatar_url

    @avatar_url.setter
    def avatar_url(self, avatar_url):
        r"""Sets the avatar_url of this ApprovalUserDto.

        头像url

        :param avatar_url: The avatar_url of this ApprovalUserDto.
        :type avatar_url: str
        """
        self._avatar_url = avatar_url

    @property
    def tenant_name(self):
        r"""Gets the tenant_name of this ApprovalUserDto.

        租户名称

        :return: The tenant_name of this ApprovalUserDto.
        :rtype: str
        """
        return self._tenant_name

    @tenant_name.setter
    def tenant_name(self, tenant_name):
        r"""Sets the tenant_name of this ApprovalUserDto.

        租户名称

        :param tenant_name: The tenant_name of this ApprovalUserDto.
        :type tenant_name: str
        """
        self._tenant_name = tenant_name

    @property
    def approver_comment(self):
        r"""Gets the approver_comment of this ApprovalUserDto.

        审核意见

        :return: The approver_comment of this ApprovalUserDto.
        :rtype: str
        """
        return self._approver_comment

    @approver_comment.setter
    def approver_comment(self, approver_comment):
        r"""Sets the approver_comment of this ApprovalUserDto.

        审核意见

        :param approver_comment: The approver_comment of this ApprovalUserDto.
        :type approver_comment: str
        """
        self._approver_comment = approver_comment

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
