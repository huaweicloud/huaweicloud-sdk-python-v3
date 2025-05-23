# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDeploymentGroupDetailResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_id': 'str',
        'created_time': 'str',
        'updated_time': 'str',
        'host_count': 'int',
        'project_name': 'str',
        'name': 'str',
        'region_name': 'str',
        'project_id': 'str',
        'os': 'str',
        'auto_connection_test_switch': 'int',
        'slave_cluster_id': 'str',
        'nick_name': 'str',
        'created_by': 'UserInfo',
        'updated_by': 'UserInfo',
        'description': 'str',
        'permission': 'PermissionGroupDetail'
    }

    attribute_map = {
        'group_id': 'group_id',
        'created_time': 'created_time',
        'updated_time': 'updated_time',
        'host_count': 'host_count',
        'project_name': 'project_name',
        'name': 'name',
        'region_name': 'region_name',
        'project_id': 'project_id',
        'os': 'os',
        'auto_connection_test_switch': 'auto_connection_test_switch',
        'slave_cluster_id': 'slave_cluster_id',
        'nick_name': 'nick_name',
        'created_by': 'created_by',
        'updated_by': 'updated_by',
        'description': 'description',
        'permission': 'permission'
    }

    def __init__(self, group_id=None, created_time=None, updated_time=None, host_count=None, project_name=None, name=None, region_name=None, project_id=None, os=None, auto_connection_test_switch=None, slave_cluster_id=None, nick_name=None, created_by=None, updated_by=None, description=None, permission=None):
        r"""ShowDeploymentGroupDetailResponse

        The model defined in huaweicloud sdk

        :param group_id: 主机集群id
        :type group_id: str
        :param created_time: 创建时间
        :type created_time: str
        :param updated_time: 修改时间
        :type updated_time: str
        :param host_count: 集群内主机数量，一个主机集群内最多可添加200台主机
        :type host_count: int
        :param project_name: 项目名称
        :type project_name: str
        :param name: 主机集群名
        :type name: str
        :param region_name: 局点信息
        :type region_name: str
        :param project_id: 项目id
        :type project_id: str
        :param os: 操作系统：windows|linux
        :type os: str
        :param auto_connection_test_switch: 自动测试功能已下架，该字段已失效
        :type auto_connection_test_switch: int
        :param slave_cluster_id: slave集群id，默认为null时使用默认slave集群，用户自定义slave时为slave集群id
        :type slave_cluster_id: str
        :param nick_name: 用户昵称
        :type nick_name: str
        :param created_by: 
        :type created_by: :class:`huaweicloudsdkcodeartsdeploy.v2.UserInfo`
        :param updated_by: 
        :type updated_by: :class:`huaweicloudsdkcodeartsdeploy.v2.UserInfo`
        :param description: 描述
        :type description: str
        :param permission: 
        :type permission: :class:`huaweicloudsdkcodeartsdeploy.v2.PermissionGroupDetail`
        """
        
        super(ShowDeploymentGroupDetailResponse, self).__init__()

        self._group_id = None
        self._created_time = None
        self._updated_time = None
        self._host_count = None
        self._project_name = None
        self._name = None
        self._region_name = None
        self._project_id = None
        self._os = None
        self._auto_connection_test_switch = None
        self._slave_cluster_id = None
        self._nick_name = None
        self._created_by = None
        self._updated_by = None
        self._description = None
        self._permission = None
        self.discriminator = None

        if group_id is not None:
            self.group_id = group_id
        if created_time is not None:
            self.created_time = created_time
        if updated_time is not None:
            self.updated_time = updated_time
        if host_count is not None:
            self.host_count = host_count
        if project_name is not None:
            self.project_name = project_name
        if name is not None:
            self.name = name
        if region_name is not None:
            self.region_name = region_name
        if project_id is not None:
            self.project_id = project_id
        if os is not None:
            self.os = os
        if auto_connection_test_switch is not None:
            self.auto_connection_test_switch = auto_connection_test_switch
        if slave_cluster_id is not None:
            self.slave_cluster_id = slave_cluster_id
        if nick_name is not None:
            self.nick_name = nick_name
        if created_by is not None:
            self.created_by = created_by
        if updated_by is not None:
            self.updated_by = updated_by
        if description is not None:
            self.description = description
        if permission is not None:
            self.permission = permission

    @property
    def group_id(self):
        r"""Gets the group_id of this ShowDeploymentGroupDetailResponse.

        主机集群id

        :return: The group_id of this ShowDeploymentGroupDetailResponse.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this ShowDeploymentGroupDetailResponse.

        主机集群id

        :param group_id: The group_id of this ShowDeploymentGroupDetailResponse.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def created_time(self):
        r"""Gets the created_time of this ShowDeploymentGroupDetailResponse.

        创建时间

        :return: The created_time of this ShowDeploymentGroupDetailResponse.
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        r"""Sets the created_time of this ShowDeploymentGroupDetailResponse.

        创建时间

        :param created_time: The created_time of this ShowDeploymentGroupDetailResponse.
        :type created_time: str
        """
        self._created_time = created_time

    @property
    def updated_time(self):
        r"""Gets the updated_time of this ShowDeploymentGroupDetailResponse.

        修改时间

        :return: The updated_time of this ShowDeploymentGroupDetailResponse.
        :rtype: str
        """
        return self._updated_time

    @updated_time.setter
    def updated_time(self, updated_time):
        r"""Sets the updated_time of this ShowDeploymentGroupDetailResponse.

        修改时间

        :param updated_time: The updated_time of this ShowDeploymentGroupDetailResponse.
        :type updated_time: str
        """
        self._updated_time = updated_time

    @property
    def host_count(self):
        r"""Gets the host_count of this ShowDeploymentGroupDetailResponse.

        集群内主机数量，一个主机集群内最多可添加200台主机

        :return: The host_count of this ShowDeploymentGroupDetailResponse.
        :rtype: int
        """
        return self._host_count

    @host_count.setter
    def host_count(self, host_count):
        r"""Sets the host_count of this ShowDeploymentGroupDetailResponse.

        集群内主机数量，一个主机集群内最多可添加200台主机

        :param host_count: The host_count of this ShowDeploymentGroupDetailResponse.
        :type host_count: int
        """
        self._host_count = host_count

    @property
    def project_name(self):
        r"""Gets the project_name of this ShowDeploymentGroupDetailResponse.

        项目名称

        :return: The project_name of this ShowDeploymentGroupDetailResponse.
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        r"""Sets the project_name of this ShowDeploymentGroupDetailResponse.

        项目名称

        :param project_name: The project_name of this ShowDeploymentGroupDetailResponse.
        :type project_name: str
        """
        self._project_name = project_name

    @property
    def name(self):
        r"""Gets the name of this ShowDeploymentGroupDetailResponse.

        主机集群名

        :return: The name of this ShowDeploymentGroupDetailResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowDeploymentGroupDetailResponse.

        主机集群名

        :param name: The name of this ShowDeploymentGroupDetailResponse.
        :type name: str
        """
        self._name = name

    @property
    def region_name(self):
        r"""Gets the region_name of this ShowDeploymentGroupDetailResponse.

        局点信息

        :return: The region_name of this ShowDeploymentGroupDetailResponse.
        :rtype: str
        """
        return self._region_name

    @region_name.setter
    def region_name(self, region_name):
        r"""Sets the region_name of this ShowDeploymentGroupDetailResponse.

        局点信息

        :param region_name: The region_name of this ShowDeploymentGroupDetailResponse.
        :type region_name: str
        """
        self._region_name = region_name

    @property
    def project_id(self):
        r"""Gets the project_id of this ShowDeploymentGroupDetailResponse.

        项目id

        :return: The project_id of this ShowDeploymentGroupDetailResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ShowDeploymentGroupDetailResponse.

        项目id

        :param project_id: The project_id of this ShowDeploymentGroupDetailResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def os(self):
        r"""Gets the os of this ShowDeploymentGroupDetailResponse.

        操作系统：windows|linux

        :return: The os of this ShowDeploymentGroupDetailResponse.
        :rtype: str
        """
        return self._os

    @os.setter
    def os(self, os):
        r"""Sets the os of this ShowDeploymentGroupDetailResponse.

        操作系统：windows|linux

        :param os: The os of this ShowDeploymentGroupDetailResponse.
        :type os: str
        """
        self._os = os

    @property
    def auto_connection_test_switch(self):
        r"""Gets the auto_connection_test_switch of this ShowDeploymentGroupDetailResponse.

        自动测试功能已下架，该字段已失效

        :return: The auto_connection_test_switch of this ShowDeploymentGroupDetailResponse.
        :rtype: int
        """
        return self._auto_connection_test_switch

    @auto_connection_test_switch.setter
    def auto_connection_test_switch(self, auto_connection_test_switch):
        r"""Sets the auto_connection_test_switch of this ShowDeploymentGroupDetailResponse.

        自动测试功能已下架，该字段已失效

        :param auto_connection_test_switch: The auto_connection_test_switch of this ShowDeploymentGroupDetailResponse.
        :type auto_connection_test_switch: int
        """
        self._auto_connection_test_switch = auto_connection_test_switch

    @property
    def slave_cluster_id(self):
        r"""Gets the slave_cluster_id of this ShowDeploymentGroupDetailResponse.

        slave集群id，默认为null时使用默认slave集群，用户自定义slave时为slave集群id

        :return: The slave_cluster_id of this ShowDeploymentGroupDetailResponse.
        :rtype: str
        """
        return self._slave_cluster_id

    @slave_cluster_id.setter
    def slave_cluster_id(self, slave_cluster_id):
        r"""Sets the slave_cluster_id of this ShowDeploymentGroupDetailResponse.

        slave集群id，默认为null时使用默认slave集群，用户自定义slave时为slave集群id

        :param slave_cluster_id: The slave_cluster_id of this ShowDeploymentGroupDetailResponse.
        :type slave_cluster_id: str
        """
        self._slave_cluster_id = slave_cluster_id

    @property
    def nick_name(self):
        r"""Gets the nick_name of this ShowDeploymentGroupDetailResponse.

        用户昵称

        :return: The nick_name of this ShowDeploymentGroupDetailResponse.
        :rtype: str
        """
        return self._nick_name

    @nick_name.setter
    def nick_name(self, nick_name):
        r"""Sets the nick_name of this ShowDeploymentGroupDetailResponse.

        用户昵称

        :param nick_name: The nick_name of this ShowDeploymentGroupDetailResponse.
        :type nick_name: str
        """
        self._nick_name = nick_name

    @property
    def created_by(self):
        r"""Gets the created_by of this ShowDeploymentGroupDetailResponse.

        :return: The created_by of this ShowDeploymentGroupDetailResponse.
        :rtype: :class:`huaweicloudsdkcodeartsdeploy.v2.UserInfo`
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        r"""Sets the created_by of this ShowDeploymentGroupDetailResponse.

        :param created_by: The created_by of this ShowDeploymentGroupDetailResponse.
        :type created_by: :class:`huaweicloudsdkcodeartsdeploy.v2.UserInfo`
        """
        self._created_by = created_by

    @property
    def updated_by(self):
        r"""Gets the updated_by of this ShowDeploymentGroupDetailResponse.

        :return: The updated_by of this ShowDeploymentGroupDetailResponse.
        :rtype: :class:`huaweicloudsdkcodeartsdeploy.v2.UserInfo`
        """
        return self._updated_by

    @updated_by.setter
    def updated_by(self, updated_by):
        r"""Sets the updated_by of this ShowDeploymentGroupDetailResponse.

        :param updated_by: The updated_by of this ShowDeploymentGroupDetailResponse.
        :type updated_by: :class:`huaweicloudsdkcodeartsdeploy.v2.UserInfo`
        """
        self._updated_by = updated_by

    @property
    def description(self):
        r"""Gets the description of this ShowDeploymentGroupDetailResponse.

        描述

        :return: The description of this ShowDeploymentGroupDetailResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowDeploymentGroupDetailResponse.

        描述

        :param description: The description of this ShowDeploymentGroupDetailResponse.
        :type description: str
        """
        self._description = description

    @property
    def permission(self):
        r"""Gets the permission of this ShowDeploymentGroupDetailResponse.

        :return: The permission of this ShowDeploymentGroupDetailResponse.
        :rtype: :class:`huaweicloudsdkcodeartsdeploy.v2.PermissionGroupDetail`
        """
        return self._permission

    @permission.setter
    def permission(self, permission):
        r"""Sets the permission of this ShowDeploymentGroupDetailResponse.

        :param permission: The permission of this ShowDeploymentGroupDetailResponse.
        :type permission: :class:`huaweicloudsdkcodeartsdeploy.v2.PermissionGroupDetail`
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
        if not isinstance(other, ShowDeploymentGroupDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
