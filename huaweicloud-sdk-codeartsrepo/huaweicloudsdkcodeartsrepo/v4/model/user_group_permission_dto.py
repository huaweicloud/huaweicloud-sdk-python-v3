# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UserGroupPermissionDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'can_create_group': 'bool',
        'can_craete_project': 'bool',
        'can_set_group': 'bool',
        'group_id': 'int',
        'group_visibility': 'str'
    }

    attribute_map = {
        'can_create_group': 'can_create_group',
        'can_craete_project': 'can_craete_project',
        'can_set_group': 'can_set_group',
        'group_id': 'group_id',
        'group_visibility': 'group_visibility'
    }

    def __init__(self, can_create_group=None, can_craete_project=None, can_set_group=None, group_id=None, group_visibility=None):
        r"""UserGroupPermissionDto

        The model defined in huaweicloud sdk

        :param can_create_group: **参数解释：** 是否可以创建代码组。
        :type can_create_group: bool
        :param can_craete_project: **参数解释：** 是否可以创建仓库。
        :type can_craete_project: bool
        :param can_set_group: **参数解释：** 是否可以设置代码组。
        :type can_set_group: bool
        :param group_id: **参数解释：** 代码组id。
        :type group_id: int
        :param group_visibility: **参数解释：** 可见性, private public。
        :type group_visibility: str
        """
        
        

        self._can_create_group = None
        self._can_craete_project = None
        self._can_set_group = None
        self._group_id = None
        self._group_visibility = None
        self.discriminator = None

        if can_create_group is not None:
            self.can_create_group = can_create_group
        if can_craete_project is not None:
            self.can_craete_project = can_craete_project
        if can_set_group is not None:
            self.can_set_group = can_set_group
        if group_id is not None:
            self.group_id = group_id
        if group_visibility is not None:
            self.group_visibility = group_visibility

    @property
    def can_create_group(self):
        r"""Gets the can_create_group of this UserGroupPermissionDto.

        **参数解释：** 是否可以创建代码组。

        :return: The can_create_group of this UserGroupPermissionDto.
        :rtype: bool
        """
        return self._can_create_group

    @can_create_group.setter
    def can_create_group(self, can_create_group):
        r"""Sets the can_create_group of this UserGroupPermissionDto.

        **参数解释：** 是否可以创建代码组。

        :param can_create_group: The can_create_group of this UserGroupPermissionDto.
        :type can_create_group: bool
        """
        self._can_create_group = can_create_group

    @property
    def can_craete_project(self):
        r"""Gets the can_craete_project of this UserGroupPermissionDto.

        **参数解释：** 是否可以创建仓库。

        :return: The can_craete_project of this UserGroupPermissionDto.
        :rtype: bool
        """
        return self._can_craete_project

    @can_craete_project.setter
    def can_craete_project(self, can_craete_project):
        r"""Sets the can_craete_project of this UserGroupPermissionDto.

        **参数解释：** 是否可以创建仓库。

        :param can_craete_project: The can_craete_project of this UserGroupPermissionDto.
        :type can_craete_project: bool
        """
        self._can_craete_project = can_craete_project

    @property
    def can_set_group(self):
        r"""Gets the can_set_group of this UserGroupPermissionDto.

        **参数解释：** 是否可以设置代码组。

        :return: The can_set_group of this UserGroupPermissionDto.
        :rtype: bool
        """
        return self._can_set_group

    @can_set_group.setter
    def can_set_group(self, can_set_group):
        r"""Sets the can_set_group of this UserGroupPermissionDto.

        **参数解释：** 是否可以设置代码组。

        :param can_set_group: The can_set_group of this UserGroupPermissionDto.
        :type can_set_group: bool
        """
        self._can_set_group = can_set_group

    @property
    def group_id(self):
        r"""Gets the group_id of this UserGroupPermissionDto.

        **参数解释：** 代码组id。

        :return: The group_id of this UserGroupPermissionDto.
        :rtype: int
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this UserGroupPermissionDto.

        **参数解释：** 代码组id。

        :param group_id: The group_id of this UserGroupPermissionDto.
        :type group_id: int
        """
        self._group_id = group_id

    @property
    def group_visibility(self):
        r"""Gets the group_visibility of this UserGroupPermissionDto.

        **参数解释：** 可见性, private public。

        :return: The group_visibility of this UserGroupPermissionDto.
        :rtype: str
        """
        return self._group_visibility

    @group_visibility.setter
    def group_visibility(self, group_visibility):
        r"""Sets the group_visibility of this UserGroupPermissionDto.

        **参数解释：** 可见性, private public。

        :param group_visibility: The group_visibility of this UserGroupPermissionDto.
        :type group_visibility: str
        """
        self._group_visibility = group_visibility

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
        if not isinstance(other, UserGroupPermissionDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
