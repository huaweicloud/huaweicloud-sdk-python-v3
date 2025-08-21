# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UserGroupDto:

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
        'user_group_id': 'str',
        'project_id': 'str',
        'tenant_id': 'str',
        'group_type': 'str',
        'member_count': 'int',
        'created_at': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'user_group_id': 'user_group_id',
        'project_id': 'project_id',
        'tenant_id': 'tenant_id',
        'group_type': 'group_type',
        'member_count': 'member_count',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, name=None, user_group_id=None, project_id=None, tenant_id=None, group_type=None, member_count=None, created_at=None, updated_at=None):
        r"""UserGroupDto

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 唯一标识id。
        :type id: int
        :param name: **参数解释：** 名称。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type name: str
        :param user_group_id: **参数解释：** 成员组id。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type user_group_id: str
        :param project_id: **参数解释：** 项目id。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type project_id: str
        :param tenant_id: **参数解释：** 租户id。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type tenant_id: str
        :param group_type: **参数解释：** 代码组类型。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type group_type: str
        :param member_count: **参数解释：** 成员数量。
        :type member_count: int
        :param created_at: **参数解释：** 创建时间。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type created_at: str
        :param updated_at: **参数解释：** 更新时间。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type updated_at: str
        """
        
        

        self._id = None
        self._name = None
        self._user_group_id = None
        self._project_id = None
        self._tenant_id = None
        self._group_type = None
        self._member_count = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if user_group_id is not None:
            self.user_group_id = user_group_id
        if project_id is not None:
            self.project_id = project_id
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if group_type is not None:
            self.group_type = group_type
        if member_count is not None:
            self.member_count = member_count
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def id(self):
        r"""Gets the id of this UserGroupDto.

        **参数解释：** 唯一标识id。

        :return: The id of this UserGroupDto.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this UserGroupDto.

        **参数解释：** 唯一标识id。

        :param id: The id of this UserGroupDto.
        :type id: int
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this UserGroupDto.

        **参数解释：** 名称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The name of this UserGroupDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UserGroupDto.

        **参数解释：** 名称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param name: The name of this UserGroupDto.
        :type name: str
        """
        self._name = name

    @property
    def user_group_id(self):
        r"""Gets the user_group_id of this UserGroupDto.

        **参数解释：** 成员组id。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The user_group_id of this UserGroupDto.
        :rtype: str
        """
        return self._user_group_id

    @user_group_id.setter
    def user_group_id(self, user_group_id):
        r"""Sets the user_group_id of this UserGroupDto.

        **参数解释：** 成员组id。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param user_group_id: The user_group_id of this UserGroupDto.
        :type user_group_id: str
        """
        self._user_group_id = user_group_id

    @property
    def project_id(self):
        r"""Gets the project_id of this UserGroupDto.

        **参数解释：** 项目id。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The project_id of this UserGroupDto.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this UserGroupDto.

        **参数解释：** 项目id。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param project_id: The project_id of this UserGroupDto.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def tenant_id(self):
        r"""Gets the tenant_id of this UserGroupDto.

        **参数解释：** 租户id。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The tenant_id of this UserGroupDto.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        r"""Sets the tenant_id of this UserGroupDto.

        **参数解释：** 租户id。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param tenant_id: The tenant_id of this UserGroupDto.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def group_type(self):
        r"""Gets the group_type of this UserGroupDto.

        **参数解释：** 代码组类型。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The group_type of this UserGroupDto.
        :rtype: str
        """
        return self._group_type

    @group_type.setter
    def group_type(self, group_type):
        r"""Sets the group_type of this UserGroupDto.

        **参数解释：** 代码组类型。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param group_type: The group_type of this UserGroupDto.
        :type group_type: str
        """
        self._group_type = group_type

    @property
    def member_count(self):
        r"""Gets the member_count of this UserGroupDto.

        **参数解释：** 成员数量。

        :return: The member_count of this UserGroupDto.
        :rtype: int
        """
        return self._member_count

    @member_count.setter
    def member_count(self, member_count):
        r"""Sets the member_count of this UserGroupDto.

        **参数解释：** 成员数量。

        :param member_count: The member_count of this UserGroupDto.
        :type member_count: int
        """
        self._member_count = member_count

    @property
    def created_at(self):
        r"""Gets the created_at of this UserGroupDto.

        **参数解释：** 创建时间。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The created_at of this UserGroupDto.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this UserGroupDto.

        **参数解释：** 创建时间。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param created_at: The created_at of this UserGroupDto.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this UserGroupDto.

        **参数解释：** 更新时间。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The updated_at of this UserGroupDto.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this UserGroupDto.

        **参数解释：** 更新时间。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param updated_at: The updated_at of this UserGroupDto.
        :type updated_at: str
        """
        self._updated_at = updated_at

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
        if not isinstance(other, UserGroupDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
