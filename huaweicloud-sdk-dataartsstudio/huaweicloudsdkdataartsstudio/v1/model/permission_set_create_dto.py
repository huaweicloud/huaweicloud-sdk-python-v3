# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PermissionSetCreateDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'parent_id': 'str',
        'description': 'str',
        'type': 'str',
        'managed_cluster_id': 'str',
        'managed_cluster_name': 'str',
        'managed_role_name': 'str',
        'manager_id': 'str',
        'manager_name': 'str',
        'manager_type': 'str'
    }

    attribute_map = {
        'name': 'name',
        'parent_id': 'parent_id',
        'description': 'description',
        'type': 'type',
        'managed_cluster_id': 'managed_cluster_id',
        'managed_cluster_name': 'managed_cluster_name',
        'managed_role_name': 'managed_role_name',
        'manager_id': 'manager_id',
        'manager_name': 'manager_name',
        'manager_type': 'manager_type'
    }

    def __init__(self, name=None, parent_id=None, description=None, type=None, managed_cluster_id=None, managed_cluster_name=None, managed_role_name=None, manager_id=None, manager_name=None, manager_type=None):
        """PermissionSetCreateDTO

        The model defined in huaweicloud sdk

        :param name: 名称
        :type name: str
        :param parent_id: 父权限集id
        :type parent_id: str
        :param description: 描述
        :type description: str
        :param type: 权限集类型, COMMON, MRS_MANAGED
        :type type: str
        :param managed_cluster_id: 纳管角色所在集群id（仅纳管类权限集需要）
        :type managed_cluster_id: str
        :param managed_cluster_name: 纳管角色所在集群名称（仅纳管类权限集需要）
        :type managed_cluster_name: str
        :param managed_role_name: 纳管角色名称（仅纳管类权限集需要）
        :type managed_role_name: str
        :param manager_id: 管理员id
        :type manager_id: str
        :param manager_name: 管理员名称
        :type manager_name: str
        :param manager_type: 管理员类型, 用户/用户组, USER, USER_GROUP
        :type manager_type: str
        """
        
        

        self._name = None
        self._parent_id = None
        self._description = None
        self._type = None
        self._managed_cluster_id = None
        self._managed_cluster_name = None
        self._managed_role_name = None
        self._manager_id = None
        self._manager_name = None
        self._manager_type = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if parent_id is not None:
            self.parent_id = parent_id
        if description is not None:
            self.description = description
        if type is not None:
            self.type = type
        if managed_cluster_id is not None:
            self.managed_cluster_id = managed_cluster_id
        if managed_cluster_name is not None:
            self.managed_cluster_name = managed_cluster_name
        if managed_role_name is not None:
            self.managed_role_name = managed_role_name
        if manager_id is not None:
            self.manager_id = manager_id
        if manager_name is not None:
            self.manager_name = manager_name
        if manager_type is not None:
            self.manager_type = manager_type

    @property
    def name(self):
        """Gets the name of this PermissionSetCreateDTO.

        名称

        :return: The name of this PermissionSetCreateDTO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PermissionSetCreateDTO.

        名称

        :param name: The name of this PermissionSetCreateDTO.
        :type name: str
        """
        self._name = name

    @property
    def parent_id(self):
        """Gets the parent_id of this PermissionSetCreateDTO.

        父权限集id

        :return: The parent_id of this PermissionSetCreateDTO.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this PermissionSetCreateDTO.

        父权限集id

        :param parent_id: The parent_id of this PermissionSetCreateDTO.
        :type parent_id: str
        """
        self._parent_id = parent_id

    @property
    def description(self):
        """Gets the description of this PermissionSetCreateDTO.

        描述

        :return: The description of this PermissionSetCreateDTO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PermissionSetCreateDTO.

        描述

        :param description: The description of this PermissionSetCreateDTO.
        :type description: str
        """
        self._description = description

    @property
    def type(self):
        """Gets the type of this PermissionSetCreateDTO.

        权限集类型, COMMON, MRS_MANAGED

        :return: The type of this PermissionSetCreateDTO.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PermissionSetCreateDTO.

        权限集类型, COMMON, MRS_MANAGED

        :param type: The type of this PermissionSetCreateDTO.
        :type type: str
        """
        self._type = type

    @property
    def managed_cluster_id(self):
        """Gets the managed_cluster_id of this PermissionSetCreateDTO.

        纳管角色所在集群id（仅纳管类权限集需要）

        :return: The managed_cluster_id of this PermissionSetCreateDTO.
        :rtype: str
        """
        return self._managed_cluster_id

    @managed_cluster_id.setter
    def managed_cluster_id(self, managed_cluster_id):
        """Sets the managed_cluster_id of this PermissionSetCreateDTO.

        纳管角色所在集群id（仅纳管类权限集需要）

        :param managed_cluster_id: The managed_cluster_id of this PermissionSetCreateDTO.
        :type managed_cluster_id: str
        """
        self._managed_cluster_id = managed_cluster_id

    @property
    def managed_cluster_name(self):
        """Gets the managed_cluster_name of this PermissionSetCreateDTO.

        纳管角色所在集群名称（仅纳管类权限集需要）

        :return: The managed_cluster_name of this PermissionSetCreateDTO.
        :rtype: str
        """
        return self._managed_cluster_name

    @managed_cluster_name.setter
    def managed_cluster_name(self, managed_cluster_name):
        """Sets the managed_cluster_name of this PermissionSetCreateDTO.

        纳管角色所在集群名称（仅纳管类权限集需要）

        :param managed_cluster_name: The managed_cluster_name of this PermissionSetCreateDTO.
        :type managed_cluster_name: str
        """
        self._managed_cluster_name = managed_cluster_name

    @property
    def managed_role_name(self):
        """Gets the managed_role_name of this PermissionSetCreateDTO.

        纳管角色名称（仅纳管类权限集需要）

        :return: The managed_role_name of this PermissionSetCreateDTO.
        :rtype: str
        """
        return self._managed_role_name

    @managed_role_name.setter
    def managed_role_name(self, managed_role_name):
        """Sets the managed_role_name of this PermissionSetCreateDTO.

        纳管角色名称（仅纳管类权限集需要）

        :param managed_role_name: The managed_role_name of this PermissionSetCreateDTO.
        :type managed_role_name: str
        """
        self._managed_role_name = managed_role_name

    @property
    def manager_id(self):
        """Gets the manager_id of this PermissionSetCreateDTO.

        管理员id

        :return: The manager_id of this PermissionSetCreateDTO.
        :rtype: str
        """
        return self._manager_id

    @manager_id.setter
    def manager_id(self, manager_id):
        """Sets the manager_id of this PermissionSetCreateDTO.

        管理员id

        :param manager_id: The manager_id of this PermissionSetCreateDTO.
        :type manager_id: str
        """
        self._manager_id = manager_id

    @property
    def manager_name(self):
        """Gets the manager_name of this PermissionSetCreateDTO.

        管理员名称

        :return: The manager_name of this PermissionSetCreateDTO.
        :rtype: str
        """
        return self._manager_name

    @manager_name.setter
    def manager_name(self, manager_name):
        """Sets the manager_name of this PermissionSetCreateDTO.

        管理员名称

        :param manager_name: The manager_name of this PermissionSetCreateDTO.
        :type manager_name: str
        """
        self._manager_name = manager_name

    @property
    def manager_type(self):
        """Gets the manager_type of this PermissionSetCreateDTO.

        管理员类型, 用户/用户组, USER, USER_GROUP

        :return: The manager_type of this PermissionSetCreateDTO.
        :rtype: str
        """
        return self._manager_type

    @manager_type.setter
    def manager_type(self, manager_type):
        """Sets the manager_type of this PermissionSetCreateDTO.

        管理员类型, 用户/用户组, USER, USER_GROUP

        :param manager_type: The manager_type of this PermissionSetCreateDTO.
        :type manager_type: str
        """
        self._manager_type = manager_type

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
        if not isinstance(other, PermissionSetCreateDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
