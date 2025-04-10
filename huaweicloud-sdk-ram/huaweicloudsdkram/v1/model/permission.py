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
        'updated_at': 'datetime',
        'permission_urn': 'str',
        'permission_type': 'str',
        'default_version': 'bool',
        'version': 'int',
        'status': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'resource_type': 'resource_type',
        'content': 'content',
        'is_resource_type_default': 'is_resource_type_default',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'permission_urn': 'permission_urn',
        'permission_type': 'permission_type',
        'default_version': 'default_version',
        'version': 'version',
        'status': 'status'
    }

    def __init__(self, id=None, name=None, resource_type=None, content=None, is_resource_type_default=None, created_at=None, updated_at=None, permission_urn=None, permission_type=None, default_version=None, version=None, status=None):
        r"""Permission

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
        :param permission_urn: 权限URN。
        :type permission_urn: str
        :param permission_type: 权限类型。
        :type permission_type: str
        :param default_version: 此权限是否为默认版本。
        :type default_version: bool
        :param version: 权限版本。
        :type version: int
        :param status: 权限的状态
        :type status: str
        """
        
        

        self._id = None
        self._name = None
        self._resource_type = None
        self._content = None
        self._is_resource_type_default = None
        self._created_at = None
        self._updated_at = None
        self._permission_urn = None
        self._permission_type = None
        self._default_version = None
        self._version = None
        self._status = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.resource_type = resource_type
        self.content = content
        self.is_resource_type_default = is_resource_type_default
        self.created_at = created_at
        self.updated_at = updated_at
        if permission_urn is not None:
            self.permission_urn = permission_urn
        if permission_type is not None:
            self.permission_type = permission_type
        if default_version is not None:
            self.default_version = default_version
        if version is not None:
            self.version = version
        if status is not None:
            self.status = status

    @property
    def id(self):
        r"""Gets the id of this Permission.

        权限ID。

        :return: The id of this Permission.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this Permission.

        权限ID。

        :param id: The id of this Permission.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this Permission.

        权限名称。

        :return: The name of this Permission.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Permission.

        权限名称。

        :param name: The name of this Permission.
        :type name: str
        """
        self._name = name

    @property
    def resource_type(self):
        r"""Gets the resource_type of this Permission.

        资源类型。

        :return: The resource_type of this Permission.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this Permission.

        资源类型。

        :param resource_type: The resource_type of this Permission.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def content(self):
        r"""Gets the content of this Permission.

        权限的影响和行为。

        :return: The content of this Permission.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        r"""Sets the content of this Permission.

        权限的影响和行为。

        :param content: The content of this Permission.
        :type content: str
        """
        self._content = content

    @property
    def is_resource_type_default(self):
        r"""Gets the is_resource_type_default of this Permission.

        该权限是否是此资源类型的默认权限。

        :return: The is_resource_type_default of this Permission.
        :rtype: bool
        """
        return self._is_resource_type_default

    @is_resource_type_default.setter
    def is_resource_type_default(self, is_resource_type_default):
        r"""Sets the is_resource_type_default of this Permission.

        该权限是否是此资源类型的默认权限。

        :param is_resource_type_default: The is_resource_type_default of this Permission.
        :type is_resource_type_default: bool
        """
        self._is_resource_type_default = is_resource_type_default

    @property
    def created_at(self):
        r"""Gets the created_at of this Permission.

        权限的创建时间。

        :return: The created_at of this Permission.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this Permission.

        权限的创建时间。

        :param created_at: The created_at of this Permission.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this Permission.

        最后一次更新权限的时间。

        :return: The updated_at of this Permission.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this Permission.

        最后一次更新权限的时间。

        :param updated_at: The updated_at of this Permission.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

    @property
    def permission_urn(self):
        r"""Gets the permission_urn of this Permission.

        权限URN。

        :return: The permission_urn of this Permission.
        :rtype: str
        """
        return self._permission_urn

    @permission_urn.setter
    def permission_urn(self, permission_urn):
        r"""Sets the permission_urn of this Permission.

        权限URN。

        :param permission_urn: The permission_urn of this Permission.
        :type permission_urn: str
        """
        self._permission_urn = permission_urn

    @property
    def permission_type(self):
        r"""Gets the permission_type of this Permission.

        权限类型。

        :return: The permission_type of this Permission.
        :rtype: str
        """
        return self._permission_type

    @permission_type.setter
    def permission_type(self, permission_type):
        r"""Sets the permission_type of this Permission.

        权限类型。

        :param permission_type: The permission_type of this Permission.
        :type permission_type: str
        """
        self._permission_type = permission_type

    @property
    def default_version(self):
        r"""Gets the default_version of this Permission.

        此权限是否为默认版本。

        :return: The default_version of this Permission.
        :rtype: bool
        """
        return self._default_version

    @default_version.setter
    def default_version(self, default_version):
        r"""Sets the default_version of this Permission.

        此权限是否为默认版本。

        :param default_version: The default_version of this Permission.
        :type default_version: bool
        """
        self._default_version = default_version

    @property
    def version(self):
        r"""Gets the version of this Permission.

        权限版本。

        :return: The version of this Permission.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this Permission.

        权限版本。

        :param version: The version of this Permission.
        :type version: int
        """
        self._version = version

    @property
    def status(self):
        r"""Gets the status of this Permission.

        权限的状态

        :return: The status of this Permission.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this Permission.

        权限的状态

        :param status: The status of this Permission.
        :type status: str
        """
        self._status = status

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
