# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GroupMyRoleDtoV4:

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
        'is_project_admin': 'is_project_admin',
        'is_group_creator': 'is_group_creator',
        'is_repo_creator': 'is_repo_creator',
        'role_show_flag': 'role_show_flag'
    }

    def __init__(self, id=None, access_level=None, role_namecn=None, role_namen=None, source_id=None, source_type=None, user_id=None, notification_level=None, created_at=None, updated_at=None, is_project_admin=None, is_group_creator=None, is_repo_creator=None, role_show_flag=None):
        r"""GroupMyRoleDtoV4

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 记录id。
        :type id: int
        :param access_level: **参数解释：** 角色。
        :type access_level: int
        :param role_namecn: **参数解释：** 角色中文名称。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type role_namecn: str
        :param role_namen: **参数解释：** 角色英文名称。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type role_namen: str
        :param source_id: **参数解释：** 资源id。
        :type source_id: int
        :param source_type: **参数解释：** 资源类型。 **取值范围：Group Project** 字符串长度不少于1，不超过1000。
        :type source_type: str
        :param user_id: **参数解释：** 用户id。
        :type user_id: int
        :param notification_level: **参数解释：** 通知。
        :type notification_level: int
        :param created_at: **参数解释：** 创建时间。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type created_at: str
        :param updated_at: **参数解释：** 更新时间。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type updated_at: str
        :param is_project_admin: **参数解释：** 是否是项目创建者。
        :type is_project_admin: int
        :param is_group_creator: **参数解释：** 是否是代码组创建者。
        :type is_group_creator: int
        :param is_repo_creator: **参数解释：** 是否是仓库创建者。
        :type is_repo_creator: int
        :param role_show_flag: **参数解释：** 角色展示。
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
        r"""Gets the id of this GroupMyRoleDtoV4.

        **参数解释：** 记录id。

        :return: The id of this GroupMyRoleDtoV4.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this GroupMyRoleDtoV4.

        **参数解释：** 记录id。

        :param id: The id of this GroupMyRoleDtoV4.
        :type id: int
        """
        self._id = id

    @property
    def access_level(self):
        r"""Gets the access_level of this GroupMyRoleDtoV4.

        **参数解释：** 角色。

        :return: The access_level of this GroupMyRoleDtoV4.
        :rtype: int
        """
        return self._access_level

    @access_level.setter
    def access_level(self, access_level):
        r"""Sets the access_level of this GroupMyRoleDtoV4.

        **参数解释：** 角色。

        :param access_level: The access_level of this GroupMyRoleDtoV4.
        :type access_level: int
        """
        self._access_level = access_level

    @property
    def role_namecn(self):
        r"""Gets the role_namecn of this GroupMyRoleDtoV4.

        **参数解释：** 角色中文名称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The role_namecn of this GroupMyRoleDtoV4.
        :rtype: str
        """
        return self._role_namecn

    @role_namecn.setter
    def role_namecn(self, role_namecn):
        r"""Sets the role_namecn of this GroupMyRoleDtoV4.

        **参数解释：** 角色中文名称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param role_namecn: The role_namecn of this GroupMyRoleDtoV4.
        :type role_namecn: str
        """
        self._role_namecn = role_namecn

    @property
    def role_namen(self):
        r"""Gets the role_namen of this GroupMyRoleDtoV4.

        **参数解释：** 角色英文名称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The role_namen of this GroupMyRoleDtoV4.
        :rtype: str
        """
        return self._role_namen

    @role_namen.setter
    def role_namen(self, role_namen):
        r"""Sets the role_namen of this GroupMyRoleDtoV4.

        **参数解释：** 角色英文名称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param role_namen: The role_namen of this GroupMyRoleDtoV4.
        :type role_namen: str
        """
        self._role_namen = role_namen

    @property
    def source_id(self):
        r"""Gets the source_id of this GroupMyRoleDtoV4.

        **参数解释：** 资源id。

        :return: The source_id of this GroupMyRoleDtoV4.
        :rtype: int
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        r"""Sets the source_id of this GroupMyRoleDtoV4.

        **参数解释：** 资源id。

        :param source_id: The source_id of this GroupMyRoleDtoV4.
        :type source_id: int
        """
        self._source_id = source_id

    @property
    def source_type(self):
        r"""Gets the source_type of this GroupMyRoleDtoV4.

        **参数解释：** 资源类型。 **取值范围：Group Project** 字符串长度不少于1，不超过1000。

        :return: The source_type of this GroupMyRoleDtoV4.
        :rtype: str
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        r"""Sets the source_type of this GroupMyRoleDtoV4.

        **参数解释：** 资源类型。 **取值范围：Group Project** 字符串长度不少于1，不超过1000。

        :param source_type: The source_type of this GroupMyRoleDtoV4.
        :type source_type: str
        """
        self._source_type = source_type

    @property
    def user_id(self):
        r"""Gets the user_id of this GroupMyRoleDtoV4.

        **参数解释：** 用户id。

        :return: The user_id of this GroupMyRoleDtoV4.
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this GroupMyRoleDtoV4.

        **参数解释：** 用户id。

        :param user_id: The user_id of this GroupMyRoleDtoV4.
        :type user_id: int
        """
        self._user_id = user_id

    @property
    def notification_level(self):
        r"""Gets the notification_level of this GroupMyRoleDtoV4.

        **参数解释：** 通知。

        :return: The notification_level of this GroupMyRoleDtoV4.
        :rtype: int
        """
        return self._notification_level

    @notification_level.setter
    def notification_level(self, notification_level):
        r"""Sets the notification_level of this GroupMyRoleDtoV4.

        **参数解释：** 通知。

        :param notification_level: The notification_level of this GroupMyRoleDtoV4.
        :type notification_level: int
        """
        self._notification_level = notification_level

    @property
    def created_at(self):
        r"""Gets the created_at of this GroupMyRoleDtoV4.

        **参数解释：** 创建时间。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The created_at of this GroupMyRoleDtoV4.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this GroupMyRoleDtoV4.

        **参数解释：** 创建时间。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param created_at: The created_at of this GroupMyRoleDtoV4.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this GroupMyRoleDtoV4.

        **参数解释：** 更新时间。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The updated_at of this GroupMyRoleDtoV4.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this GroupMyRoleDtoV4.

        **参数解释：** 更新时间。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param updated_at: The updated_at of this GroupMyRoleDtoV4.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def is_project_admin(self):
        r"""Gets the is_project_admin of this GroupMyRoleDtoV4.

        **参数解释：** 是否是项目创建者。

        :return: The is_project_admin of this GroupMyRoleDtoV4.
        :rtype: int
        """
        return self._is_project_admin

    @is_project_admin.setter
    def is_project_admin(self, is_project_admin):
        r"""Sets the is_project_admin of this GroupMyRoleDtoV4.

        **参数解释：** 是否是项目创建者。

        :param is_project_admin: The is_project_admin of this GroupMyRoleDtoV4.
        :type is_project_admin: int
        """
        self._is_project_admin = is_project_admin

    @property
    def is_group_creator(self):
        r"""Gets the is_group_creator of this GroupMyRoleDtoV4.

        **参数解释：** 是否是代码组创建者。

        :return: The is_group_creator of this GroupMyRoleDtoV4.
        :rtype: int
        """
        return self._is_group_creator

    @is_group_creator.setter
    def is_group_creator(self, is_group_creator):
        r"""Sets the is_group_creator of this GroupMyRoleDtoV4.

        **参数解释：** 是否是代码组创建者。

        :param is_group_creator: The is_group_creator of this GroupMyRoleDtoV4.
        :type is_group_creator: int
        """
        self._is_group_creator = is_group_creator

    @property
    def is_repo_creator(self):
        r"""Gets the is_repo_creator of this GroupMyRoleDtoV4.

        **参数解释：** 是否是仓库创建者。

        :return: The is_repo_creator of this GroupMyRoleDtoV4.
        :rtype: int
        """
        return self._is_repo_creator

    @is_repo_creator.setter
    def is_repo_creator(self, is_repo_creator):
        r"""Sets the is_repo_creator of this GroupMyRoleDtoV4.

        **参数解释：** 是否是仓库创建者。

        :param is_repo_creator: The is_repo_creator of this GroupMyRoleDtoV4.
        :type is_repo_creator: int
        """
        self._is_repo_creator = is_repo_creator

    @property
    def role_show_flag(self):
        r"""Gets the role_show_flag of this GroupMyRoleDtoV4.

        **参数解释：** 角色展示。

        :return: The role_show_flag of this GroupMyRoleDtoV4.
        :rtype: int
        """
        return self._role_show_flag

    @role_show_flag.setter
    def role_show_flag(self, role_show_flag):
        r"""Sets the role_show_flag of this GroupMyRoleDtoV4.

        **参数解释：** 角色展示。

        :param role_show_flag: The role_show_flag of this GroupMyRoleDtoV4.
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
        if not isinstance(other, GroupMyRoleDtoV4):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
