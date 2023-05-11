# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Permission:

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
        'name': 'str',
        'resource_type': 'str',
        'content': 'str',
        'is_resource_type_default': 'bool',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'resource_type': 'resource_type',
        'content': 'content',
        'is_resource_type_default': 'is_resource_type_default',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, name=None, resource_type=None, content=None, is_resource_type_default=None, created_at=None, updated_at=None):
        """Permission

        The model defined in huaweicloud sdk

        :param id: 权限ID。
        :type id: str
        :param name: 权限名称。
        :type name: str
        :param resource_type: 资源类型。
        :type resource_type: str
        :param content: 权限的影响和行为。
        :type content: str
        :param is_resource_type_default: 该权限是否是此资源类型的默认权限。
        :type is_resource_type_default: bool
        :param created_at: 权限的创建时间。
        :type created_at: datetime
        :param updated_at: 最后一次更新权限的时间。
        :type updated_at: datetime
        """
        
        

        self._id = None
        self._name = None
        self._resource_type = None
        self._content = None
        self._is_resource_type_default = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.resource_type = resource_type
        self.content = content
        self.is_resource_type_default = is_resource_type_default
        self.created_at = created_at
        self.updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this Permission.

        权限ID。

        :return: The id of this Permission.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Permission.

        权限ID。

        :param id: The id of this Permission.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this Permission.

        权限名称。

        :return: The name of this Permission.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Permission.

        权限名称。

        :param name: The name of this Permission.
        :type name: str
        """
        self._name = name

    @property
    def resource_type(self):
        """Gets the resource_type of this Permission.

        资源类型。

        :return: The resource_type of this Permission.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this Permission.

        资源类型。

        :param resource_type: The resource_type of this Permission.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def content(self):
        """Gets the content of this Permission.

        权限的影响和行为。

        :return: The content of this Permission.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this Permission.

        权限的影响和行为。

        :param content: The content of this Permission.
        :type content: str
        """
        self._content = content

    @property
    def is_resource_type_default(self):
        """Gets the is_resource_type_default of this Permission.

        该权限是否是此资源类型的默认权限。

        :return: The is_resource_type_default of this Permission.
        :rtype: bool
        """
        return self._is_resource_type_default

    @is_resource_type_default.setter
    def is_resource_type_default(self, is_resource_type_default):
        """Sets the is_resource_type_default of this Permission.

        该权限是否是此资源类型的默认权限。

        :param is_resource_type_default: The is_resource_type_default of this Permission.
        :type is_resource_type_default: bool
        """
        self._is_resource_type_default = is_resource_type_default

    @property
    def created_at(self):
        """Gets the created_at of this Permission.

        权限的创建时间。

        :return: The created_at of this Permission.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Permission.

        权限的创建时间。

        :param created_at: The created_at of this Permission.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this Permission.

        最后一次更新权限的时间。

        :return: The updated_at of this Permission.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Permission.

        最后一次更新权限的时间。

        :param updated_at: The updated_at of this Permission.
        :type updated_at: datetime
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
        if not isinstance(other, Permission):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
