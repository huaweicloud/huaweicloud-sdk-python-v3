# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GroupMyRoleDto:

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
        'access_level': 'int',
        'role_namecn': 'str',
        'role_namen': 'str',
        'source_id': 'int',
        'source_type': 'str',
        'user_id': 'int',
        'notification_level': 'int',
        'created_at': 'str',
        'updated_at': 'str',
        'created_by_id': 'int',
        'invite_email': 'str',
        'invite_token': 'str',
        'invite_accepted_at': 'str',
        'requested_at': 'str',
        'expires_at': 'str',
        'limited': 'bool',
        'is_project_admin': 'int',
        'is_group_creator': 'int',
        'is_repo_creator': 'int',
        'role_show_flag': 'int'
    }

    attribute_map = {
        'id': 'id',
        'access_level': 'access_level',
        'role_namecn': 'role_namecn',
        'role_namen': 'role_namen',
        'source_id': 'source_id',
        'source_type': 'source_type',
        'user_id': 'user_id',
        'notification_level': 'notification_level',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'created_by_id': 'created_by_id',
        'invite_email': 'invite_email',
        'invite_token': 'invite_token',
        'invite_accepted_at': 'invite_accepted_at',
        'requested_at': 'requested_at',
        'expires_at': 'expires_at',
        'limited': 'limited',
        'is_project_admin': 'isProjectAdmin',
        'is_group_creator': 'isGroupCreator',
        'is_repo_creator': 'isRepoCreator',
        'role_show_flag': 'roleShowFlag'
    }

    def __init__(self, id=None, access_level=None, role_namecn=None, role_namen=None, source_id=None, source_type=None, user_id=None, notification_level=None, created_at=None, updated_at=None, created_by_id=None, invite_email=None, invite_token=None, invite_accepted_at=None, requested_at=None, expires_at=None, limited=None, is_project_admin=None, is_group_creator=None, is_repo_creator=None, role_show_flag=None):
        r"""GroupMyRoleDto

        The model defined in huaweicloud sdk

        :param id: 成员id
        :type id: int
        :param access_level: 成员角色值
        :type access_level: int
        :param role_namecn: 角色中文名称
        :type role_namecn: str
        :param role_namen: 角色名称
        :type role_namen: str
        :param source_id: 来源代码组id
        :type source_id: int
        :param source_type: 来源类型
        :type source_type: str
        :param user_id: 用户id
        :type user_id: int
        :param notification_level: 提示级别
        :type notification_level: int
        :param created_at: 创建时间
        :type created_at: str
        :param updated_at: 更新时间
        :type updated_at: str
        :param created_by_id: 创建者id
        :type created_by_id: int
        :param invite_email: 邀请邮箱
        :type invite_email: str
        :param invite_token: 邀请token
        :type invite_token: str
        :param invite_accepted_at: 邀请接受时间
        :type invite_accepted_at: str
        :param requested_at: 请求时间
        :type requested_at: str
        :param expires_at: 过期时间
        :type expires_at: str
        :param limited: 限制
        :type limited: bool
        :param is_project_admin: 是否为项目管理员
        :type is_project_admin: int
        :param is_group_creator: 是否为组织创建者
        :type is_group_creator: int
        :param is_repo_creator: 是否仓库创建者
        :type is_repo_creator: int
        :param role_show_flag: 展示标记
        :type role_show_flag: int
        """
        
        

        self._id = None
        self._access_level = None
        self._role_namecn = None
        self._role_namen = None
        self._source_id = None
        self._source_type = None
        self._user_id = None
        self._notification_level = None
        self._created_at = None
        self._updated_at = None
        self._created_by_id = None
        self._invite_email = None
        self._invite_token = None
        self._invite_accepted_at = None
        self._requested_at = None
        self._expires_at = None
        self._limited = None
        self._is_project_admin = None
        self._is_group_creator = None
        self._is_repo_creator = None
        self._role_show_flag = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if access_level is not None:
            self.access_level = access_level
        if role_namecn is not None:
            self.role_namecn = role_namecn
        if role_namen is not None:
            self.role_namen = role_namen
        if source_id is not None:
            self.source_id = source_id
        if source_type is not None:
            self.source_type = source_type
        if user_id is not None:
            self.user_id = user_id
        if notification_level is not None:
            self.notification_level = notification_level
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if created_by_id is not None:
            self.created_by_id = created_by_id
        if invite_email is not None:
            self.invite_email = invite_email
        if invite_token is not None:
            self.invite_token = invite_token
        if invite_accepted_at is not None:
            self.invite_accepted_at = invite_accepted_at
        if requested_at is not None:
            self.requested_at = requested_at
        if expires_at is not None:
            self.expires_at = expires_at
        if limited is not None:
            self.limited = limited
        if is_project_admin is not None:
            self.is_project_admin = is_project_admin
        if is_group_creator is not None:
            self.is_group_creator = is_group_creator
        if is_repo_creator is not None:
            self.is_repo_creator = is_repo_creator
        if role_show_flag is not None:
            self.role_show_flag = role_show_flag

    @property
    def id(self):
        r"""Gets the id of this GroupMyRoleDto.

        成员id

        :return: The id of this GroupMyRoleDto.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this GroupMyRoleDto.

        成员id

        :param id: The id of this GroupMyRoleDto.
        :type id: int
        """
        self._id = id

    @property
    def access_level(self):
        r"""Gets the access_level of this GroupMyRoleDto.

        成员角色值

        :return: The access_level of this GroupMyRoleDto.
        :rtype: int
        """
        return self._access_level

    @access_level.setter
    def access_level(self, access_level):
        r"""Sets the access_level of this GroupMyRoleDto.

        成员角色值

        :param access_level: The access_level of this GroupMyRoleDto.
        :type access_level: int
        """
        self._access_level = access_level

    @property
    def role_namecn(self):
        r"""Gets the role_namecn of this GroupMyRoleDto.

        角色中文名称

        :return: The role_namecn of this GroupMyRoleDto.
        :rtype: str
        """
        return self._role_namecn

    @role_namecn.setter
    def role_namecn(self, role_namecn):
        r"""Sets the role_namecn of this GroupMyRoleDto.

        角色中文名称

        :param role_namecn: The role_namecn of this GroupMyRoleDto.
        :type role_namecn: str
        """
        self._role_namecn = role_namecn

    @property
    def role_namen(self):
        r"""Gets the role_namen of this GroupMyRoleDto.

        角色名称

        :return: The role_namen of this GroupMyRoleDto.
        :rtype: str
        """
        return self._role_namen

    @role_namen.setter
    def role_namen(self, role_namen):
        r"""Sets the role_namen of this GroupMyRoleDto.

        角色名称

        :param role_namen: The role_namen of this GroupMyRoleDto.
        :type role_namen: str
        """
        self._role_namen = role_namen

    @property
    def source_id(self):
        r"""Gets the source_id of this GroupMyRoleDto.

        来源代码组id

        :return: The source_id of this GroupMyRoleDto.
        :rtype: int
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        r"""Sets the source_id of this GroupMyRoleDto.

        来源代码组id

        :param source_id: The source_id of this GroupMyRoleDto.
        :type source_id: int
        """
        self._source_id = source_id

    @property
    def source_type(self):
        r"""Gets the source_type of this GroupMyRoleDto.

        来源类型

        :return: The source_type of this GroupMyRoleDto.
        :rtype: str
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        r"""Sets the source_type of this GroupMyRoleDto.

        来源类型

        :param source_type: The source_type of this GroupMyRoleDto.
        :type source_type: str
        """
        self._source_type = source_type

    @property
    def user_id(self):
        r"""Gets the user_id of this GroupMyRoleDto.

        用户id

        :return: The user_id of this GroupMyRoleDto.
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this GroupMyRoleDto.

        用户id

        :param user_id: The user_id of this GroupMyRoleDto.
        :type user_id: int
        """
        self._user_id = user_id

    @property
    def notification_level(self):
        r"""Gets the notification_level of this GroupMyRoleDto.

        提示级别

        :return: The notification_level of this GroupMyRoleDto.
        :rtype: int
        """
        return self._notification_level

    @notification_level.setter
    def notification_level(self, notification_level):
        r"""Sets the notification_level of this GroupMyRoleDto.

        提示级别

        :param notification_level: The notification_level of this GroupMyRoleDto.
        :type notification_level: int
        """
        self._notification_level = notification_level

    @property
    def created_at(self):
        r"""Gets the created_at of this GroupMyRoleDto.

        创建时间

        :return: The created_at of this GroupMyRoleDto.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this GroupMyRoleDto.

        创建时间

        :param created_at: The created_at of this GroupMyRoleDto.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this GroupMyRoleDto.

        更新时间

        :return: The updated_at of this GroupMyRoleDto.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this GroupMyRoleDto.

        更新时间

        :param updated_at: The updated_at of this GroupMyRoleDto.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def created_by_id(self):
        r"""Gets the created_by_id of this GroupMyRoleDto.

        创建者id

        :return: The created_by_id of this GroupMyRoleDto.
        :rtype: int
        """
        return self._created_by_id

    @created_by_id.setter
    def created_by_id(self, created_by_id):
        r"""Sets the created_by_id of this GroupMyRoleDto.

        创建者id

        :param created_by_id: The created_by_id of this GroupMyRoleDto.
        :type created_by_id: int
        """
        self._created_by_id = created_by_id

    @property
    def invite_email(self):
        r"""Gets the invite_email of this GroupMyRoleDto.

        邀请邮箱

        :return: The invite_email of this GroupMyRoleDto.
        :rtype: str
        """
        return self._invite_email

    @invite_email.setter
    def invite_email(self, invite_email):
        r"""Sets the invite_email of this GroupMyRoleDto.

        邀请邮箱

        :param invite_email: The invite_email of this GroupMyRoleDto.
        :type invite_email: str
        """
        self._invite_email = invite_email

    @property
    def invite_token(self):
        r"""Gets the invite_token of this GroupMyRoleDto.

        邀请token

        :return: The invite_token of this GroupMyRoleDto.
        :rtype: str
        """
        return self._invite_token

    @invite_token.setter
    def invite_token(self, invite_token):
        r"""Sets the invite_token of this GroupMyRoleDto.

        邀请token

        :param invite_token: The invite_token of this GroupMyRoleDto.
        :type invite_token: str
        """
        self._invite_token = invite_token

    @property
    def invite_accepted_at(self):
        r"""Gets the invite_accepted_at of this GroupMyRoleDto.

        邀请接受时间

        :return: The invite_accepted_at of this GroupMyRoleDto.
        :rtype: str
        """
        return self._invite_accepted_at

    @invite_accepted_at.setter
    def invite_accepted_at(self, invite_accepted_at):
        r"""Sets the invite_accepted_at of this GroupMyRoleDto.

        邀请接受时间

        :param invite_accepted_at: The invite_accepted_at of this GroupMyRoleDto.
        :type invite_accepted_at: str
        """
        self._invite_accepted_at = invite_accepted_at

    @property
    def requested_at(self):
        r"""Gets the requested_at of this GroupMyRoleDto.

        请求时间

        :return: The requested_at of this GroupMyRoleDto.
        :rtype: str
        """
        return self._requested_at

    @requested_at.setter
    def requested_at(self, requested_at):
        r"""Sets the requested_at of this GroupMyRoleDto.

        请求时间

        :param requested_at: The requested_at of this GroupMyRoleDto.
        :type requested_at: str
        """
        self._requested_at = requested_at

    @property
    def expires_at(self):
        r"""Gets the expires_at of this GroupMyRoleDto.

        过期时间

        :return: The expires_at of this GroupMyRoleDto.
        :rtype: str
        """
        return self._expires_at

    @expires_at.setter
    def expires_at(self, expires_at):
        r"""Sets the expires_at of this GroupMyRoleDto.

        过期时间

        :param expires_at: The expires_at of this GroupMyRoleDto.
        :type expires_at: str
        """
        self._expires_at = expires_at

    @property
    def limited(self):
        r"""Gets the limited of this GroupMyRoleDto.

        限制

        :return: The limited of this GroupMyRoleDto.
        :rtype: bool
        """
        return self._limited

    @limited.setter
    def limited(self, limited):
        r"""Sets the limited of this GroupMyRoleDto.

        限制

        :param limited: The limited of this GroupMyRoleDto.
        :type limited: bool
        """
        self._limited = limited

    @property
    def is_project_admin(self):
        r"""Gets the is_project_admin of this GroupMyRoleDto.

        是否为项目管理员

        :return: The is_project_admin of this GroupMyRoleDto.
        :rtype: int
        """
        return self._is_project_admin

    @is_project_admin.setter
    def is_project_admin(self, is_project_admin):
        r"""Sets the is_project_admin of this GroupMyRoleDto.

        是否为项目管理员

        :param is_project_admin: The is_project_admin of this GroupMyRoleDto.
        :type is_project_admin: int
        """
        self._is_project_admin = is_project_admin

    @property
    def is_group_creator(self):
        r"""Gets the is_group_creator of this GroupMyRoleDto.

        是否为组织创建者

        :return: The is_group_creator of this GroupMyRoleDto.
        :rtype: int
        """
        return self._is_group_creator

    @is_group_creator.setter
    def is_group_creator(self, is_group_creator):
        r"""Sets the is_group_creator of this GroupMyRoleDto.

        是否为组织创建者

        :param is_group_creator: The is_group_creator of this GroupMyRoleDto.
        :type is_group_creator: int
        """
        self._is_group_creator = is_group_creator

    @property
    def is_repo_creator(self):
        r"""Gets the is_repo_creator of this GroupMyRoleDto.

        是否仓库创建者

        :return: The is_repo_creator of this GroupMyRoleDto.
        :rtype: int
        """
        return self._is_repo_creator

    @is_repo_creator.setter
    def is_repo_creator(self, is_repo_creator):
        r"""Sets the is_repo_creator of this GroupMyRoleDto.

        是否仓库创建者

        :param is_repo_creator: The is_repo_creator of this GroupMyRoleDto.
        :type is_repo_creator: int
        """
        self._is_repo_creator = is_repo_creator

    @property
    def role_show_flag(self):
        r"""Gets the role_show_flag of this GroupMyRoleDto.

        展示标记

        :return: The role_show_flag of this GroupMyRoleDto.
        :rtype: int
        """
        return self._role_show_flag

    @role_show_flag.setter
    def role_show_flag(self, role_show_flag):
        r"""Sets the role_show_flag of this GroupMyRoleDto.

        展示标记

        :param role_show_flag: The role_show_flag of this GroupMyRoleDto.
        :type role_show_flag: int
        """
        self._role_show_flag = role_show_flag

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
        if not isinstance(other, GroupMyRoleDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
