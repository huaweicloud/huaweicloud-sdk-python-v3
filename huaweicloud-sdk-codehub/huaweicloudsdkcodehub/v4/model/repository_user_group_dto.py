# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RepositoryUserGroupDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user_group_name': 'str',
        'user_group_id': 'str',
        'project_id': 'str',
        'user_count': 'str',
        'description': 'str'
    }

    attribute_map = {
        'user_group_name': 'user_group_name',
        'user_group_id': 'user_group_id',
        'project_id': 'project_id',
        'user_count': 'user_count',
        'description': 'description'
    }

    def __init__(self, user_group_name=None, user_group_id=None, project_id=None, user_count=None, description=None):
        r"""RepositoryUserGroupDto

        The model defined in huaweicloud sdk

        :param user_group_name: **参数解释：** 成员组名称 **约束限制：** 不涉及。
        :type user_group_name: str
        :param user_group_id: **参数解释：** 成员组id。 **约束限制：** 不涉及。
        :type user_group_id: str
        :param project_id: **参数解释：** 项目id。 **约束限制：** 不涉及。
        :type project_id: str
        :param user_count: **参数解释：** 成员组用户数量。 **约束限制：** 不涉及。
        :type user_count: str
        :param description: **参数解释：** 成员组描述。 **约束限制：** 不涉及。
        :type description: str
        """
        
        

        self._user_group_name = None
        self._user_group_id = None
        self._project_id = None
        self._user_count = None
        self._description = None
        self.discriminator = None

        if user_group_name is not None:
            self.user_group_name = user_group_name
        if user_group_id is not None:
            self.user_group_id = user_group_id
        if project_id is not None:
            self.project_id = project_id
        if user_count is not None:
            self.user_count = user_count
        if description is not None:
            self.description = description

    @property
    def user_group_name(self):
        r"""Gets the user_group_name of this RepositoryUserGroupDto.

        **参数解释：** 成员组名称 **约束限制：** 不涉及。

        :return: The user_group_name of this RepositoryUserGroupDto.
        :rtype: str
        """
        return self._user_group_name

    @user_group_name.setter
    def user_group_name(self, user_group_name):
        r"""Sets the user_group_name of this RepositoryUserGroupDto.

        **参数解释：** 成员组名称 **约束限制：** 不涉及。

        :param user_group_name: The user_group_name of this RepositoryUserGroupDto.
        :type user_group_name: str
        """
        self._user_group_name = user_group_name

    @property
    def user_group_id(self):
        r"""Gets the user_group_id of this RepositoryUserGroupDto.

        **参数解释：** 成员组id。 **约束限制：** 不涉及。

        :return: The user_group_id of this RepositoryUserGroupDto.
        :rtype: str
        """
        return self._user_group_id

    @user_group_id.setter
    def user_group_id(self, user_group_id):
        r"""Sets the user_group_id of this RepositoryUserGroupDto.

        **参数解释：** 成员组id。 **约束限制：** 不涉及。

        :param user_group_id: The user_group_id of this RepositoryUserGroupDto.
        :type user_group_id: str
        """
        self._user_group_id = user_group_id

    @property
    def project_id(self):
        r"""Gets the project_id of this RepositoryUserGroupDto.

        **参数解释：** 项目id。 **约束限制：** 不涉及。

        :return: The project_id of this RepositoryUserGroupDto.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this RepositoryUserGroupDto.

        **参数解释：** 项目id。 **约束限制：** 不涉及。

        :param project_id: The project_id of this RepositoryUserGroupDto.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def user_count(self):
        r"""Gets the user_count of this RepositoryUserGroupDto.

        **参数解释：** 成员组用户数量。 **约束限制：** 不涉及。

        :return: The user_count of this RepositoryUserGroupDto.
        :rtype: str
        """
        return self._user_count

    @user_count.setter
    def user_count(self, user_count):
        r"""Sets the user_count of this RepositoryUserGroupDto.

        **参数解释：** 成员组用户数量。 **约束限制：** 不涉及。

        :param user_count: The user_count of this RepositoryUserGroupDto.
        :type user_count: str
        """
        self._user_count = user_count

    @property
    def description(self):
        r"""Gets the description of this RepositoryUserGroupDto.

        **参数解释：** 成员组描述。 **约束限制：** 不涉及。

        :return: The description of this RepositoryUserGroupDto.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this RepositoryUserGroupDto.

        **参数解释：** 成员组描述。 **约束限制：** 不涉及。

        :param description: The description of this RepositoryUserGroupDto.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, RepositoryUserGroupDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
