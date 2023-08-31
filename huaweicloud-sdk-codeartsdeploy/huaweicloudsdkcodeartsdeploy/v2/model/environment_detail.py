# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EnvironmentDetail:

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
        'description': 'str',
        'os': 'str',
        'nick_name': 'str',
        'deploy_type': 'int',
        'created_time': 'str',
        'instance_count': 'int',
        'created_by': 'UserInfo',
        'permission': 'EnvironmentPermissionDetail'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'os': 'os',
        'nick_name': 'nick_name',
        'deploy_type': 'deploy_type',
        'created_time': 'created_time',
        'instance_count': 'instance_count',
        'created_by': 'created_by',
        'permission': 'permission'
    }

    def __init__(self, id=None, name=None, description=None, os=None, nick_name=None, deploy_type=None, created_time=None, instance_count=None, created_by=None, permission=None):
        """EnvironmentDetail

        The model defined in huaweicloud sdk

        :param id: 环境id
        :type id: str
        :param name: 环境名称
        :type name: str
        :param description: 环境描述
        :type description: str
        :param os: 操作系统
        :type os: str
        :param nick_name: 用户昵称
        :type nick_name: str
        :param deploy_type: 部署类型：0表示主机, 1表示kubernetes
        :type deploy_type: int
        :param created_time: 创建时间
        :type created_time: str
        :param instance_count: 环境下主机实例数量
        :type instance_count: int
        :param created_by: 
        :type created_by: :class:`huaweicloudsdkcodeartsdeploy.v2.UserInfo`
        :param permission: 
        :type permission: :class:`huaweicloudsdkcodeartsdeploy.v2.EnvironmentPermissionDetail`
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._os = None
        self._nick_name = None
        self._deploy_type = None
        self._created_time = None
        self._instance_count = None
        self._created_by = None
        self._permission = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if os is not None:
            self.os = os
        if nick_name is not None:
            self.nick_name = nick_name
        if deploy_type is not None:
            self.deploy_type = deploy_type
        if created_time is not None:
            self.created_time = created_time
        if instance_count is not None:
            self.instance_count = instance_count
        if created_by is not None:
            self.created_by = created_by
        if permission is not None:
            self.permission = permission

    @property
    def id(self):
        """Gets the id of this EnvironmentDetail.

        环境id

        :return: The id of this EnvironmentDetail.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EnvironmentDetail.

        环境id

        :param id: The id of this EnvironmentDetail.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this EnvironmentDetail.

        环境名称

        :return: The name of this EnvironmentDetail.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EnvironmentDetail.

        环境名称

        :param name: The name of this EnvironmentDetail.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this EnvironmentDetail.

        环境描述

        :return: The description of this EnvironmentDetail.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this EnvironmentDetail.

        环境描述

        :param description: The description of this EnvironmentDetail.
        :type description: str
        """
        self._description = description

    @property
    def os(self):
        """Gets the os of this EnvironmentDetail.

        操作系统

        :return: The os of this EnvironmentDetail.
        :rtype: str
        """
        return self._os

    @os.setter
    def os(self, os):
        """Sets the os of this EnvironmentDetail.

        操作系统

        :param os: The os of this EnvironmentDetail.
        :type os: str
        """
        self._os = os

    @property
    def nick_name(self):
        """Gets the nick_name of this EnvironmentDetail.

        用户昵称

        :return: The nick_name of this EnvironmentDetail.
        :rtype: str
        """
        return self._nick_name

    @nick_name.setter
    def nick_name(self, nick_name):
        """Sets the nick_name of this EnvironmentDetail.

        用户昵称

        :param nick_name: The nick_name of this EnvironmentDetail.
        :type nick_name: str
        """
        self._nick_name = nick_name

    @property
    def deploy_type(self):
        """Gets the deploy_type of this EnvironmentDetail.

        部署类型：0表示主机, 1表示kubernetes

        :return: The deploy_type of this EnvironmentDetail.
        :rtype: int
        """
        return self._deploy_type

    @deploy_type.setter
    def deploy_type(self, deploy_type):
        """Sets the deploy_type of this EnvironmentDetail.

        部署类型：0表示主机, 1表示kubernetes

        :param deploy_type: The deploy_type of this EnvironmentDetail.
        :type deploy_type: int
        """
        self._deploy_type = deploy_type

    @property
    def created_time(self):
        """Gets the created_time of this EnvironmentDetail.

        创建时间

        :return: The created_time of this EnvironmentDetail.
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this EnvironmentDetail.

        创建时间

        :param created_time: The created_time of this EnvironmentDetail.
        :type created_time: str
        """
        self._created_time = created_time

    @property
    def instance_count(self):
        """Gets the instance_count of this EnvironmentDetail.

        环境下主机实例数量

        :return: The instance_count of this EnvironmentDetail.
        :rtype: int
        """
        return self._instance_count

    @instance_count.setter
    def instance_count(self, instance_count):
        """Sets the instance_count of this EnvironmentDetail.

        环境下主机实例数量

        :param instance_count: The instance_count of this EnvironmentDetail.
        :type instance_count: int
        """
        self._instance_count = instance_count

    @property
    def created_by(self):
        """Gets the created_by of this EnvironmentDetail.

        :return: The created_by of this EnvironmentDetail.
        :rtype: :class:`huaweicloudsdkcodeartsdeploy.v2.UserInfo`
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this EnvironmentDetail.

        :param created_by: The created_by of this EnvironmentDetail.
        :type created_by: :class:`huaweicloudsdkcodeartsdeploy.v2.UserInfo`
        """
        self._created_by = created_by

    @property
    def permission(self):
        """Gets the permission of this EnvironmentDetail.

        :return: The permission of this EnvironmentDetail.
        :rtype: :class:`huaweicloudsdkcodeartsdeploy.v2.EnvironmentPermissionDetail`
        """
        return self._permission

    @permission.setter
    def permission(self, permission):
        """Sets the permission of this EnvironmentDetail.

        :param permission: The permission of this EnvironmentDetail.
        :type permission: :class:`huaweicloudsdkcodeartsdeploy.v2.EnvironmentPermissionDetail`
        """
        self._permission = permission

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
        if not isinstance(other, EnvironmentDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
