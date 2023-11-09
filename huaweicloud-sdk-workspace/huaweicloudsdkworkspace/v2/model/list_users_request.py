# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListUsersRequest:

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
        'limit': 'str',
        'offset': 'str',
        'description': 'str',
        'active_type': 'str',
        'group_name': 'str'
    }

    attribute_map = {
        'user_name': 'user_name',
        'limit': 'limit',
        'offset': 'offset',
        'description': 'description',
        'active_type': 'active_type',
        'group_name': 'group_name'
    }

    def __init__(self, user_name=None, limit=None, offset=None, description=None, active_type=None, group_name=None):
        """ListUsersRequest

        The model defined in huaweicloud sdk

        :param user_name: 桌面用户名，长度范围为1-20，不能包含特殊字符，不能以数字开头。
        :type user_name: str
        :param limit: 用于分页查询，返回用户数量限制。如果不指定，则返回所有符合条件的用户。
        :type limit: str
        :param offset: 分页查询起始条数。
        :type offset: str
        :param description: 用户描述查询，模糊匹配。
        :type description: str
        :param active_type: 激活类型，默认为用户激活。 * USER_ACTIVATE： 用户激活 * ADMIN_ACTIVATE： 管理员激活
        :type active_type: str
        :param group_name: 桌面用户组名，精确匹配。
        :type group_name: str
        """
        
        

        self._user_name = None
        self._limit = None
        self._offset = None
        self._description = None
        self._active_type = None
        self._group_name = None
        self.discriminator = None

        if user_name is not None:
            self.user_name = user_name
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if description is not None:
            self.description = description
        if active_type is not None:
            self.active_type = active_type
        if group_name is not None:
            self.group_name = group_name

    @property
    def user_name(self):
        """Gets the user_name of this ListUsersRequest.

        桌面用户名，长度范围为1-20，不能包含特殊字符，不能以数字开头。

        :return: The user_name of this ListUsersRequest.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this ListUsersRequest.

        桌面用户名，长度范围为1-20，不能包含特殊字符，不能以数字开头。

        :param user_name: The user_name of this ListUsersRequest.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def limit(self):
        """Gets the limit of this ListUsersRequest.

        用于分页查询，返回用户数量限制。如果不指定，则返回所有符合条件的用户。

        :return: The limit of this ListUsersRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListUsersRequest.

        用于分页查询，返回用户数量限制。如果不指定，则返回所有符合条件的用户。

        :param limit: The limit of this ListUsersRequest.
        :type limit: str
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListUsersRequest.

        分页查询起始条数。

        :return: The offset of this ListUsersRequest.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListUsersRequest.

        分页查询起始条数。

        :param offset: The offset of this ListUsersRequest.
        :type offset: str
        """
        self._offset = offset

    @property
    def description(self):
        """Gets the description of this ListUsersRequest.

        用户描述查询，模糊匹配。

        :return: The description of this ListUsersRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ListUsersRequest.

        用户描述查询，模糊匹配。

        :param description: The description of this ListUsersRequest.
        :type description: str
        """
        self._description = description

    @property
    def active_type(self):
        """Gets the active_type of this ListUsersRequest.

        激活类型，默认为用户激活。 * USER_ACTIVATE： 用户激活 * ADMIN_ACTIVATE： 管理员激活

        :return: The active_type of this ListUsersRequest.
        :rtype: str
        """
        return self._active_type

    @active_type.setter
    def active_type(self, active_type):
        """Sets the active_type of this ListUsersRequest.

        激活类型，默认为用户激活。 * USER_ACTIVATE： 用户激活 * ADMIN_ACTIVATE： 管理员激活

        :param active_type: The active_type of this ListUsersRequest.
        :type active_type: str
        """
        self._active_type = active_type

    @property
    def group_name(self):
        """Gets the group_name of this ListUsersRequest.

        桌面用户组名，精确匹配。

        :return: The group_name of this ListUsersRequest.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this ListUsersRequest.

        桌面用户组名，精确匹配。

        :param group_name: The group_name of this ListUsersRequest.
        :type group_name: str
        """
        self._group_name = group_name

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
        if not isinstance(other, ListUsersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
