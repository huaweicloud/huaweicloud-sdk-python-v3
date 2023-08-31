# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HostClusterInfo:

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
        'host_count': 'int',
        'name': 'str',
        'project_id': 'str',
        'os': 'str',
        'slave_cluster_id': 'str',
        'created_by': 'UserInfo',
        'description': 'str',
        'permission': 'PermissionClusterDetail',
        'nick_name': 'str',
        'env_count': 'int'
    }

    attribute_map = {
        'id': 'id',
        'host_count': 'host_count',
        'name': 'name',
        'project_id': 'project_id',
        'os': 'os',
        'slave_cluster_id': 'slave_cluster_id',
        'created_by': 'created_by',
        'description': 'description',
        'permission': 'permission',
        'nick_name': 'nick_name',
        'env_count': 'env_count'
    }

    def __init__(self, id=None, host_count=None, name=None, project_id=None, os=None, slave_cluster_id=None, created_by=None, description=None, permission=None, nick_name=None, env_count=None):
        """HostClusterInfo

        The model defined in huaweicloud sdk

        :param id: 主机集群id
        :type id: str
        :param host_count: 集群内主机数量，一个主机集群内最多可添加200台主机
        :type host_count: int
        :param name: 主机集群名
        :type name: str
        :param project_id: 项目ID
        :type project_id: str
        :param os: 操作系统：windows|linux
        :type os: str
        :param slave_cluster_id: slave集群id，默认为null时使用默认slave集群，用户自定义slave时为slave集群id
        :type slave_cluster_id: str
        :param created_by: 
        :type created_by: :class:`huaweicloudsdkcodeartsdeploy.v2.UserInfo`
        :param description: 描述
        :type description: str
        :param permission: 
        :type permission: :class:`huaweicloudsdkcodeartsdeploy.v2.PermissionClusterDetail`
        :param nick_name: 创建人名称
        :type nick_name: str
        :param env_count: 环境数量
        :type env_count: int
        """
        
        

        self._id = None
        self._host_count = None
        self._name = None
        self._project_id = None
        self._os = None
        self._slave_cluster_id = None
        self._created_by = None
        self._description = None
        self._permission = None
        self._nick_name = None
        self._env_count = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if host_count is not None:
            self.host_count = host_count
        if name is not None:
            self.name = name
        if project_id is not None:
            self.project_id = project_id
        if os is not None:
            self.os = os
        if slave_cluster_id is not None:
            self.slave_cluster_id = slave_cluster_id
        if created_by is not None:
            self.created_by = created_by
        if description is not None:
            self.description = description
        if permission is not None:
            self.permission = permission
        if nick_name is not None:
            self.nick_name = nick_name
        if env_count is not None:
            self.env_count = env_count

    @property
    def id(self):
        """Gets the id of this HostClusterInfo.

        主机集群id

        :return: The id of this HostClusterInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this HostClusterInfo.

        主机集群id

        :param id: The id of this HostClusterInfo.
        :type id: str
        """
        self._id = id

    @property
    def host_count(self):
        """Gets the host_count of this HostClusterInfo.

        集群内主机数量，一个主机集群内最多可添加200台主机

        :return: The host_count of this HostClusterInfo.
        :rtype: int
        """
        return self._host_count

    @host_count.setter
    def host_count(self, host_count):
        """Sets the host_count of this HostClusterInfo.

        集群内主机数量，一个主机集群内最多可添加200台主机

        :param host_count: The host_count of this HostClusterInfo.
        :type host_count: int
        """
        self._host_count = host_count

    @property
    def name(self):
        """Gets the name of this HostClusterInfo.

        主机集群名

        :return: The name of this HostClusterInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this HostClusterInfo.

        主机集群名

        :param name: The name of this HostClusterInfo.
        :type name: str
        """
        self._name = name

    @property
    def project_id(self):
        """Gets the project_id of this HostClusterInfo.

        项目ID

        :return: The project_id of this HostClusterInfo.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this HostClusterInfo.

        项目ID

        :param project_id: The project_id of this HostClusterInfo.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def os(self):
        """Gets the os of this HostClusterInfo.

        操作系统：windows|linux

        :return: The os of this HostClusterInfo.
        :rtype: str
        """
        return self._os

    @os.setter
    def os(self, os):
        """Sets the os of this HostClusterInfo.

        操作系统：windows|linux

        :param os: The os of this HostClusterInfo.
        :type os: str
        """
        self._os = os

    @property
    def slave_cluster_id(self):
        """Gets the slave_cluster_id of this HostClusterInfo.

        slave集群id，默认为null时使用默认slave集群，用户自定义slave时为slave集群id

        :return: The slave_cluster_id of this HostClusterInfo.
        :rtype: str
        """
        return self._slave_cluster_id

    @slave_cluster_id.setter
    def slave_cluster_id(self, slave_cluster_id):
        """Sets the slave_cluster_id of this HostClusterInfo.

        slave集群id，默认为null时使用默认slave集群，用户自定义slave时为slave集群id

        :param slave_cluster_id: The slave_cluster_id of this HostClusterInfo.
        :type slave_cluster_id: str
        """
        self._slave_cluster_id = slave_cluster_id

    @property
    def created_by(self):
        """Gets the created_by of this HostClusterInfo.

        :return: The created_by of this HostClusterInfo.
        :rtype: :class:`huaweicloudsdkcodeartsdeploy.v2.UserInfo`
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this HostClusterInfo.

        :param created_by: The created_by of this HostClusterInfo.
        :type created_by: :class:`huaweicloudsdkcodeartsdeploy.v2.UserInfo`
        """
        self._created_by = created_by

    @property
    def description(self):
        """Gets the description of this HostClusterInfo.

        描述

        :return: The description of this HostClusterInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this HostClusterInfo.

        描述

        :param description: The description of this HostClusterInfo.
        :type description: str
        """
        self._description = description

    @property
    def permission(self):
        """Gets the permission of this HostClusterInfo.

        :return: The permission of this HostClusterInfo.
        :rtype: :class:`huaweicloudsdkcodeartsdeploy.v2.PermissionClusterDetail`
        """
        return self._permission

    @permission.setter
    def permission(self, permission):
        """Sets the permission of this HostClusterInfo.

        :param permission: The permission of this HostClusterInfo.
        :type permission: :class:`huaweicloudsdkcodeartsdeploy.v2.PermissionClusterDetail`
        """
        self._permission = permission

    @property
    def nick_name(self):
        """Gets the nick_name of this HostClusterInfo.

        创建人名称

        :return: The nick_name of this HostClusterInfo.
        :rtype: str
        """
        return self._nick_name

    @nick_name.setter
    def nick_name(self, nick_name):
        """Sets the nick_name of this HostClusterInfo.

        创建人名称

        :param nick_name: The nick_name of this HostClusterInfo.
        :type nick_name: str
        """
        self._nick_name = nick_name

    @property
    def env_count(self):
        """Gets the env_count of this HostClusterInfo.

        环境数量

        :return: The env_count of this HostClusterInfo.
        :rtype: int
        """
        return self._env_count

    @env_count.setter
    def env_count(self, env_count):
        """Sets the env_count of this HostClusterInfo.

        环境数量

        :param env_count: The env_count of this HostClusterInfo.
        :type env_count: int
        """
        self._env_count = env_count

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
        if not isinstance(other, HostClusterInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
