# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportUserGroupUsersNewRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_id': 'str',
        'user_name': 'str',
        'description': 'str',
        'active_type': 'str',
        'group_name': 'str',
        'language': 'str',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'group_id': 'group_id',
        'user_name': 'user_name',
        'description': 'description',
        'active_type': 'active_type',
        'group_name': 'group_name',
        'language': 'language',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, group_id=None, user_name=None, description=None, active_type=None, group_name=None, language=None, enterprise_project_id=None):
        r"""ExportUserGroupUsersNewRequest

        The model defined in huaweicloud sdk

        :param group_id: 桌面用户组ID。
        :type group_id: str
        :param user_name: 用户名支持模糊查询。
        :type user_name: str
        :param description: 用户描述支持模糊查询。
        :type description: str
        :param active_type: 激活类型。 - USER_ACTIVATE：用户激活 - ADMIN_ACTIVATE：管理员激活
        :type active_type: str
        :param group_name: 用户组名。
        :type group_name: str
        :param language: 语言。 - zh_CN：中文 - en_US：英文
        :type language: str
        :param enterprise_project_id: 企业项目ID。
        :type enterprise_project_id: str
        """
        
        

        self._group_id = None
        self._user_name = None
        self._description = None
        self._active_type = None
        self._group_name = None
        self._language = None
        self._enterprise_project_id = None
        self.discriminator = None

        self.group_id = group_id
        if user_name is not None:
            self.user_name = user_name
        if description is not None:
            self.description = description
        if active_type is not None:
            self.active_type = active_type
        if group_name is not None:
            self.group_name = group_name
        if language is not None:
            self.language = language
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def group_id(self):
        r"""Gets the group_id of this ExportUserGroupUsersNewRequest.

        桌面用户组ID。

        :return: The group_id of this ExportUserGroupUsersNewRequest.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this ExportUserGroupUsersNewRequest.

        桌面用户组ID。

        :param group_id: The group_id of this ExportUserGroupUsersNewRequest.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def user_name(self):
        r"""Gets the user_name of this ExportUserGroupUsersNewRequest.

        用户名支持模糊查询。

        :return: The user_name of this ExportUserGroupUsersNewRequest.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this ExportUserGroupUsersNewRequest.

        用户名支持模糊查询。

        :param user_name: The user_name of this ExportUserGroupUsersNewRequest.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def description(self):
        r"""Gets the description of this ExportUserGroupUsersNewRequest.

        用户描述支持模糊查询。

        :return: The description of this ExportUserGroupUsersNewRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ExportUserGroupUsersNewRequest.

        用户描述支持模糊查询。

        :param description: The description of this ExportUserGroupUsersNewRequest.
        :type description: str
        """
        self._description = description

    @property
    def active_type(self):
        r"""Gets the active_type of this ExportUserGroupUsersNewRequest.

        激活类型。 - USER_ACTIVATE：用户激活 - ADMIN_ACTIVATE：管理员激活

        :return: The active_type of this ExportUserGroupUsersNewRequest.
        :rtype: str
        """
        return self._active_type

    @active_type.setter
    def active_type(self, active_type):
        r"""Sets the active_type of this ExportUserGroupUsersNewRequest.

        激活类型。 - USER_ACTIVATE：用户激活 - ADMIN_ACTIVATE：管理员激活

        :param active_type: The active_type of this ExportUserGroupUsersNewRequest.
        :type active_type: str
        """
        self._active_type = active_type

    @property
    def group_name(self):
        r"""Gets the group_name of this ExportUserGroupUsersNewRequest.

        用户组名。

        :return: The group_name of this ExportUserGroupUsersNewRequest.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this ExportUserGroupUsersNewRequest.

        用户组名。

        :param group_name: The group_name of this ExportUserGroupUsersNewRequest.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def language(self):
        r"""Gets the language of this ExportUserGroupUsersNewRequest.

        语言。 - zh_CN：中文 - en_US：英文

        :return: The language of this ExportUserGroupUsersNewRequest.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        r"""Sets the language of this ExportUserGroupUsersNewRequest.

        语言。 - zh_CN：中文 - en_US：英文

        :param language: The language of this ExportUserGroupUsersNewRequest.
        :type language: str
        """
        self._language = language

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ExportUserGroupUsersNewRequest.

        企业项目ID。

        :return: The enterprise_project_id of this ExportUserGroupUsersNewRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ExportUserGroupUsersNewRequest.

        企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this ExportUserGroupUsersNewRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, ExportUserGroupUsersNewRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
