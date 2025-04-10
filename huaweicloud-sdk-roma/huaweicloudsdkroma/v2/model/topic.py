# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Topic:

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
        'description': 'str',
        'permission': 'int',
        'is_private': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'permission': 'permission',
        'is_private': 'is_private'
    }

    def __init__(self, id=None, name=None, description=None, permission=None, is_private=None):
        r"""Topic

        The model defined in huaweicloud sdk

        :param id: TOPIC的ID
        :type id: int
        :param name: TOPIC的名称
        :type name: str
        :param description: TOPIC描述
        :type description: str
        :param permission: TOPIC权限, 主题权限 0-发布 1-订阅
        :type permission: int
        :param is_private: TOPIC类型 0-基础TOPIC 1-用户自定义TOPIC
        :type is_private: int
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._permission = None
        self._is_private = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if permission is not None:
            self.permission = permission
        if is_private is not None:
            self.is_private = is_private

    @property
    def id(self):
        r"""Gets the id of this Topic.

        TOPIC的ID

        :return: The id of this Topic.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this Topic.

        TOPIC的ID

        :param id: The id of this Topic.
        :type id: int
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this Topic.

        TOPIC的名称

        :return: The name of this Topic.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Topic.

        TOPIC的名称

        :param name: The name of this Topic.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this Topic.

        TOPIC描述

        :return: The description of this Topic.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this Topic.

        TOPIC描述

        :param description: The description of this Topic.
        :type description: str
        """
        self._description = description

    @property
    def permission(self):
        r"""Gets the permission of this Topic.

        TOPIC权限, 主题权限 0-发布 1-订阅

        :return: The permission of this Topic.
        :rtype: int
        """
        return self._permission

    @permission.setter
    def permission(self, permission):
        r"""Sets the permission of this Topic.

        TOPIC权限, 主题权限 0-发布 1-订阅

        :param permission: The permission of this Topic.
        :type permission: int
        """
        self._permission = permission

    @property
    def is_private(self):
        r"""Gets the is_private of this Topic.

        TOPIC类型 0-基础TOPIC 1-用户自定义TOPIC

        :return: The is_private of this Topic.
        :rtype: int
        """
        return self._is_private

    @is_private.setter
    def is_private(self, is_private):
        r"""Sets the is_private of this Topic.

        TOPIC类型 0-基础TOPIC 1-用户自定义TOPIC

        :param is_private: The is_private of this Topic.
        :type is_private: int
        """
        self._is_private = is_private

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
        if not isinstance(other, Topic):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
