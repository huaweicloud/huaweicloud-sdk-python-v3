# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AuthorizedObjects:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'object_type': 'str',
        'object_id': 'str',
        'object_name': 'str',
        'user_group': 'str',
        'created_at': 'str'
    }

    attribute_map = {
        'object_type': 'object_type',
        'object_id': 'object_id',
        'object_name': 'object_name',
        'user_group': 'user_group',
        'created_at': 'created_at'
    }

    def __init__(self, object_type=None, object_id=None, object_name=None, user_group=None, created_at=None):
        r"""AuthorizedObjects

        The model defined in huaweicloud sdk

        :param object_type: 绑定对象类型枚举。  - USER：用户 - USER_GROUP：用户组
        :type object_type: str
        :param object_id: 用户/用户组id。
        :type object_id: str
        :param object_name: 用户/用户组名称。
        :type object_name: str
        :param user_group: 桌面用户所属的用户权限组。  - sudo：Linux管理员组。 - default：Linux默认用户组。 - administrators：Windows管理员组。管理员拥有对该桌面的完全访问权，可以做任何需要的更改（禁用操作除外）。 - users：Windows标准用户组。标准用户可以使用大多数软件，并可以更改不影响其他用户的系统设置。
        :type user_group: str
        :param created_at: 创建时间。格式为：UTC格式，例如“2022-05-11T11:45:42.000Z”。
        :type created_at: str
        """
        
        

        self._object_type = None
        self._object_id = None
        self._object_name = None
        self._user_group = None
        self._created_at = None
        self.discriminator = None

        self.object_type = object_type
        self.object_id = object_id
        self.object_name = object_name
        self.user_group = user_group
        if created_at is not None:
            self.created_at = created_at

    @property
    def object_type(self):
        r"""Gets the object_type of this AuthorizedObjects.

        绑定对象类型枚举。  - USER：用户 - USER_GROUP：用户组

        :return: The object_type of this AuthorizedObjects.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        r"""Sets the object_type of this AuthorizedObjects.

        绑定对象类型枚举。  - USER：用户 - USER_GROUP：用户组

        :param object_type: The object_type of this AuthorizedObjects.
        :type object_type: str
        """
        self._object_type = object_type

    @property
    def object_id(self):
        r"""Gets the object_id of this AuthorizedObjects.

        用户/用户组id。

        :return: The object_id of this AuthorizedObjects.
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        r"""Sets the object_id of this AuthorizedObjects.

        用户/用户组id。

        :param object_id: The object_id of this AuthorizedObjects.
        :type object_id: str
        """
        self._object_id = object_id

    @property
    def object_name(self):
        r"""Gets the object_name of this AuthorizedObjects.

        用户/用户组名称。

        :return: The object_name of this AuthorizedObjects.
        :rtype: str
        """
        return self._object_name

    @object_name.setter
    def object_name(self, object_name):
        r"""Sets the object_name of this AuthorizedObjects.

        用户/用户组名称。

        :param object_name: The object_name of this AuthorizedObjects.
        :type object_name: str
        """
        self._object_name = object_name

    @property
    def user_group(self):
        r"""Gets the user_group of this AuthorizedObjects.

        桌面用户所属的用户权限组。  - sudo：Linux管理员组。 - default：Linux默认用户组。 - administrators：Windows管理员组。管理员拥有对该桌面的完全访问权，可以做任何需要的更改（禁用操作除外）。 - users：Windows标准用户组。标准用户可以使用大多数软件，并可以更改不影响其他用户的系统设置。

        :return: The user_group of this AuthorizedObjects.
        :rtype: str
        """
        return self._user_group

    @user_group.setter
    def user_group(self, user_group):
        r"""Sets the user_group of this AuthorizedObjects.

        桌面用户所属的用户权限组。  - sudo：Linux管理员组。 - default：Linux默认用户组。 - administrators：Windows管理员组。管理员拥有对该桌面的完全访问权，可以做任何需要的更改（禁用操作除外）。 - users：Windows标准用户组。标准用户可以使用大多数软件，并可以更改不影响其他用户的系统设置。

        :param user_group: The user_group of this AuthorizedObjects.
        :type user_group: str
        """
        self._user_group = user_group

    @property
    def created_at(self):
        r"""Gets the created_at of this AuthorizedObjects.

        创建时间。格式为：UTC格式，例如“2022-05-11T11:45:42.000Z”。

        :return: The created_at of this AuthorizedObjects.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this AuthorizedObjects.

        创建时间。格式为：UTC格式，例如“2022-05-11T11:45:42.000Z”。

        :param created_at: The created_at of this AuthorizedObjects.
        :type created_at: str
        """
        self._created_at = created_at

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
        if not isinstance(other, AuthorizedObjects):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
