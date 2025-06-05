# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IamRoleDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'display_name': 'str',
        'type': 'str',
        'description': 'str',
        'actions': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'display_name': 'display_name',
        'type': 'type',
        'description': 'description',
        'actions': 'actions'
    }

    def __init__(self, id=None, display_name=None, type=None, description=None, actions=None):
        r"""IamRoleDto

        The model defined in huaweicloud sdk

        :param id: 权限ID。
        :type id: str
        :param display_name: 权限显示名称。
        :type display_name: str
        :param type: 权限类型：AX为全局级角色，XA为项目级角色。
        :type type: str
        :param description: 权限描述。
        :type description: str
        :param actions: 授权项，指对资源的具体操作权限。
        :type actions: list[str]
        """
        
        

        self._id = None
        self._display_name = None
        self._type = None
        self._description = None
        self._actions = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if display_name is not None:
            self.display_name = display_name
        if type is not None:
            self.type = type
        if description is not None:
            self.description = description
        if actions is not None:
            self.actions = actions

    @property
    def id(self):
        r"""Gets the id of this IamRoleDto.

        权限ID。

        :return: The id of this IamRoleDto.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this IamRoleDto.

        权限ID。

        :param id: The id of this IamRoleDto.
        :type id: str
        """
        self._id = id

    @property
    def display_name(self):
        r"""Gets the display_name of this IamRoleDto.

        权限显示名称。

        :return: The display_name of this IamRoleDto.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        r"""Sets the display_name of this IamRoleDto.

        权限显示名称。

        :param display_name: The display_name of this IamRoleDto.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def type(self):
        r"""Gets the type of this IamRoleDto.

        权限类型：AX为全局级角色，XA为项目级角色。

        :return: The type of this IamRoleDto.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this IamRoleDto.

        权限类型：AX为全局级角色，XA为项目级角色。

        :param type: The type of this IamRoleDto.
        :type type: str
        """
        self._type = type

    @property
    def description(self):
        r"""Gets the description of this IamRoleDto.

        权限描述。

        :return: The description of this IamRoleDto.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this IamRoleDto.

        权限描述。

        :param description: The description of this IamRoleDto.
        :type description: str
        """
        self._description = description

    @property
    def actions(self):
        r"""Gets the actions of this IamRoleDto.

        授权项，指对资源的具体操作权限。

        :return: The actions of this IamRoleDto.
        :rtype: list[str]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        r"""Sets the actions of this IamRoleDto.

        授权项，指对资源的具体操作权限。

        :param actions: The actions of this IamRoleDto.
        :type actions: list[str]
        """
        self._actions = actions

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
        if not isinstance(other, IamRoleDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
