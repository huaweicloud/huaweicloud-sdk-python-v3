# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Role:

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
        'role_description': 'str',
        'description': 'str',
        'scope': 'str'
    }

    attribute_map = {
        'id': 'id',
        'display_name': 'display_name',
        'role_description': 'role_description',
        'description': 'description',
        'scope': 'scope'
    }

    def __init__(self, id=None, display_name=None, role_description=None, description=None, scope=None):
        r"""Role

        The model defined in huaweicloud sdk

        :param id: 角色id
        :type id: str
        :param display_name: 角色名称
        :type display_name: str
        :param role_description: 角色描述
        :type role_description: str
        :param description: 描述
        :type description: str
        :param scope: 角色范围
        :type scope: str
        """
        
        

        self._id = None
        self._display_name = None
        self._role_description = None
        self._description = None
        self._scope = None
        self.discriminator = None

        self.id = id
        self.display_name = display_name
        self.role_description = role_description
        self.description = description
        self.scope = scope

    @property
    def id(self):
        r"""Gets the id of this Role.

        角色id

        :return: The id of this Role.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this Role.

        角色id

        :param id: The id of this Role.
        :type id: str
        """
        self._id = id

    @property
    def display_name(self):
        r"""Gets the display_name of this Role.

        角色名称

        :return: The display_name of this Role.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        r"""Sets the display_name of this Role.

        角色名称

        :param display_name: The display_name of this Role.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def role_description(self):
        r"""Gets the role_description of this Role.

        角色描述

        :return: The role_description of this Role.
        :rtype: str
        """
        return self._role_description

    @role_description.setter
    def role_description(self, role_description):
        r"""Sets the role_description of this Role.

        角色描述

        :param role_description: The role_description of this Role.
        :type role_description: str
        """
        self._role_description = role_description

    @property
    def description(self):
        r"""Gets the description of this Role.

        描述

        :return: The description of this Role.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this Role.

        描述

        :param description: The description of this Role.
        :type description: str
        """
        self._description = description

    @property
    def scope(self):
        r"""Gets the scope of this Role.

        角色范围

        :return: The scope of this Role.
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        r"""Sets the scope of this Role.

        角色范围

        :param scope: The scope of this Role.
        :type scope: str
        """
        self._scope = scope

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
        if not isinstance(other, Role):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
