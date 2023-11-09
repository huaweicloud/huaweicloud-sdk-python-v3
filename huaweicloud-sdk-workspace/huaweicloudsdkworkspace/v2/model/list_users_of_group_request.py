# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListUsersOfGroupRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user_name': 'str',
        'group_id': 'str',
        'description': 'str',
        'active_type': 'str',
        'limit': 'str',
        'offset': 'str'
    }

    attribute_map = {
        'user_name': 'user_name',
        'group_id': 'group_id',
        'description': 'description',
        'active_type': 'active_type',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, user_name=None, group_id=None, description=None, active_type=None, limit=None, offset=None):
        """ListUsersOfGroupRequest

        The model defined in huaweicloud sdk

        :param user_name: 用户名支持模糊查询。
        :type user_name: str
        :param group_id: 用户组ID。
        :type group_id: str
        :param description: 用户描述支持模糊查询。
        :type description: str
        :param active_type: 激活类型。 - USER_ACTIVATE：用户激活 - ADMIN_ACTIVATE：管理员激活
        :type active_type: str
        :param limit: 用于分页查询，返回桌面数量限制。如果不指定或为0，默认2000，最大2000。
        :type limit: str
        :param offset: 用于分页查询，查询的起始记录序号，从0开始。
        :type offset: str
        """
        
        

        self._user_name = None
        self._group_id = None
        self._description = None
        self._active_type = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        if user_name is not None:
            self.user_name = user_name
        self.group_id = group_id
        if description is not None:
            self.description = description
        if active_type is not None:
            self.active_type = active_type
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def user_name(self):
        """Gets the user_name of this ListUsersOfGroupRequest.

        用户名支持模糊查询。

        :return: The user_name of this ListUsersOfGroupRequest.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this ListUsersOfGroupRequest.

        用户名支持模糊查询。

        :param user_name: The user_name of this ListUsersOfGroupRequest.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def group_id(self):
        """Gets the group_id of this ListUsersOfGroupRequest.

        用户组ID。

        :return: The group_id of this ListUsersOfGroupRequest.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this ListUsersOfGroupRequest.

        用户组ID。

        :param group_id: The group_id of this ListUsersOfGroupRequest.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def description(self):
        """Gets the description of this ListUsersOfGroupRequest.

        用户描述支持模糊查询。

        :return: The description of this ListUsersOfGroupRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ListUsersOfGroupRequest.

        用户描述支持模糊查询。

        :param description: The description of this ListUsersOfGroupRequest.
        :type description: str
        """
        self._description = description

    @property
    def active_type(self):
        """Gets the active_type of this ListUsersOfGroupRequest.

        激活类型。 - USER_ACTIVATE：用户激活 - ADMIN_ACTIVATE：管理员激活

        :return: The active_type of this ListUsersOfGroupRequest.
        :rtype: str
        """
        return self._active_type

    @active_type.setter
    def active_type(self, active_type):
        """Sets the active_type of this ListUsersOfGroupRequest.

        激活类型。 - USER_ACTIVATE：用户激活 - ADMIN_ACTIVATE：管理员激活

        :param active_type: The active_type of this ListUsersOfGroupRequest.
        :type active_type: str
        """
        self._active_type = active_type

    @property
    def limit(self):
        """Gets the limit of this ListUsersOfGroupRequest.

        用于分页查询，返回桌面数量限制。如果不指定或为0，默认2000，最大2000。

        :return: The limit of this ListUsersOfGroupRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListUsersOfGroupRequest.

        用于分页查询，返回桌面数量限制。如果不指定或为0，默认2000，最大2000。

        :param limit: The limit of this ListUsersOfGroupRequest.
        :type limit: str
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListUsersOfGroupRequest.

        用于分页查询，查询的起始记录序号，从0开始。

        :return: The offset of this ListUsersOfGroupRequest.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListUsersOfGroupRequest.

        用于分页查询，查询的起始记录序号，从0开始。

        :param offset: The offset of this ListUsersOfGroupRequest.
        :type offset: str
        """
        self._offset = offset

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
        if not isinstance(other, ListUsersOfGroupRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
