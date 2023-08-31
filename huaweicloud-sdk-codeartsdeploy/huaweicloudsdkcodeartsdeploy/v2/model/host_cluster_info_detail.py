# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HostClusterInfoDetail:

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
        'os': 'str',
        'slave_cluster_id': 'str',
        'created_by': 'UserInfo',
        'description': 'str',
        'permission': 'PermissionClusterDetail',
        'nick_name': 'str',
        'is_proxy_mode': 'int',
        'created_time': 'str',
        'updated_time': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'os': 'os',
        'slave_cluster_id': 'slave_cluster_id',
        'created_by': 'created_by',
        'description': 'description',
        'permission': 'permission',
        'nick_name': 'nick_name',
        'is_proxy_mode': 'is_proxy_mode',
        'created_time': 'created_time',
        'updated_time': 'updated_time'
    }

    def __init__(self, id=None, name=None, os=None, slave_cluster_id=None, created_by=None, description=None, permission=None, nick_name=None, is_proxy_mode=None, created_time=None, updated_time=None):
        """HostClusterInfoDetail

        The model defined in huaweicloud sdk

        :param id: 主机集群id
        :type id: str
        :param name: 主机集群名
        :type name: str
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
        :param is_proxy_mode: 是否是代理模式
        :type is_proxy_mode: int
        :param created_time: 创建时间
        :type created_time: str
        :param updated_time: 更新时间
        :type updated_time: str
        """
        
        

        self._id = None
        self._name = None
        self._os = None
        self._slave_cluster_id = None
        self._created_by = None
        self._description = None
        self._permission = None
        self._nick_name = None
        self._is_proxy_mode = None
        self._created_time = None
        self._updated_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
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
        if is_proxy_mode is not None:
            self.is_proxy_mode = is_proxy_mode
        if created_time is not None:
            self.created_time = created_time
        if updated_time is not None:
            self.updated_time = updated_time

    @property
    def id(self):
        """Gets the id of this HostClusterInfoDetail.

        主机集群id

        :return: The id of this HostClusterInfoDetail.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this HostClusterInfoDetail.

        主机集群id

        :param id: The id of this HostClusterInfoDetail.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this HostClusterInfoDetail.

        主机集群名

        :return: The name of this HostClusterInfoDetail.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this HostClusterInfoDetail.

        主机集群名

        :param name: The name of this HostClusterInfoDetail.
        :type name: str
        """
        self._name = name

    @property
    def os(self):
        """Gets the os of this HostClusterInfoDetail.

        操作系统：windows|linux

        :return: The os of this HostClusterInfoDetail.
        :rtype: str
        """
        return self._os

    @os.setter
    def os(self, os):
        """Sets the os of this HostClusterInfoDetail.

        操作系统：windows|linux

        :param os: The os of this HostClusterInfoDetail.
        :type os: str
        """
        self._os = os

    @property
    def slave_cluster_id(self):
        """Gets the slave_cluster_id of this HostClusterInfoDetail.

        slave集群id，默认为null时使用默认slave集群，用户自定义slave时为slave集群id

        :return: The slave_cluster_id of this HostClusterInfoDetail.
        :rtype: str
        """
        return self._slave_cluster_id

    @slave_cluster_id.setter
    def slave_cluster_id(self, slave_cluster_id):
        """Sets the slave_cluster_id of this HostClusterInfoDetail.

        slave集群id，默认为null时使用默认slave集群，用户自定义slave时为slave集群id

        :param slave_cluster_id: The slave_cluster_id of this HostClusterInfoDetail.
        :type slave_cluster_id: str
        """
        self._slave_cluster_id = slave_cluster_id

    @property
    def created_by(self):
        """Gets the created_by of this HostClusterInfoDetail.

        :return: The created_by of this HostClusterInfoDetail.
        :rtype: :class:`huaweicloudsdkcodeartsdeploy.v2.UserInfo`
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this HostClusterInfoDetail.

        :param created_by: The created_by of this HostClusterInfoDetail.
        :type created_by: :class:`huaweicloudsdkcodeartsdeploy.v2.UserInfo`
        """
        self._created_by = created_by

    @property
    def description(self):
        """Gets the description of this HostClusterInfoDetail.

        描述

        :return: The description of this HostClusterInfoDetail.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this HostClusterInfoDetail.

        描述

        :param description: The description of this HostClusterInfoDetail.
        :type description: str
        """
        self._description = description

    @property
    def permission(self):
        """Gets the permission of this HostClusterInfoDetail.

        :return: The permission of this HostClusterInfoDetail.
        :rtype: :class:`huaweicloudsdkcodeartsdeploy.v2.PermissionClusterDetail`
        """
        return self._permission

    @permission.setter
    def permission(self, permission):
        """Sets the permission of this HostClusterInfoDetail.

        :param permission: The permission of this HostClusterInfoDetail.
        :type permission: :class:`huaweicloudsdkcodeartsdeploy.v2.PermissionClusterDetail`
        """
        self._permission = permission

    @property
    def nick_name(self):
        """Gets the nick_name of this HostClusterInfoDetail.

        创建人名称

        :return: The nick_name of this HostClusterInfoDetail.
        :rtype: str
        """
        return self._nick_name

    @nick_name.setter
    def nick_name(self, nick_name):
        """Sets the nick_name of this HostClusterInfoDetail.

        创建人名称

        :param nick_name: The nick_name of this HostClusterInfoDetail.
        :type nick_name: str
        """
        self._nick_name = nick_name

    @property
    def is_proxy_mode(self):
        """Gets the is_proxy_mode of this HostClusterInfoDetail.

        是否是代理模式

        :return: The is_proxy_mode of this HostClusterInfoDetail.
        :rtype: int
        """
        return self._is_proxy_mode

    @is_proxy_mode.setter
    def is_proxy_mode(self, is_proxy_mode):
        """Sets the is_proxy_mode of this HostClusterInfoDetail.

        是否是代理模式

        :param is_proxy_mode: The is_proxy_mode of this HostClusterInfoDetail.
        :type is_proxy_mode: int
        """
        self._is_proxy_mode = is_proxy_mode

    @property
    def created_time(self):
        """Gets the created_time of this HostClusterInfoDetail.

        创建时间

        :return: The created_time of this HostClusterInfoDetail.
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this HostClusterInfoDetail.

        创建时间

        :param created_time: The created_time of this HostClusterInfoDetail.
        :type created_time: str
        """
        self._created_time = created_time

    @property
    def updated_time(self):
        """Gets the updated_time of this HostClusterInfoDetail.

        更新时间

        :return: The updated_time of this HostClusterInfoDetail.
        :rtype: str
        """
        return self._updated_time

    @updated_time.setter
    def updated_time(self, updated_time):
        """Sets the updated_time of this HostClusterInfoDetail.

        更新时间

        :param updated_time: The updated_time of this HostClusterInfoDetail.
        :type updated_time: str
        """
        self._updated_time = updated_time

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
        if not isinstance(other, HostClusterInfoDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
