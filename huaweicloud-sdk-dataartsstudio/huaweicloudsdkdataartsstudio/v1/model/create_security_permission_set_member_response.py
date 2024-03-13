# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSecurityPermissionSetMemberResponse(SdkResponse):

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
        'permission_set_id': 'str',
        'project_id': 'str',
        'instance_id': 'str',
        'member_type': 'str',
        'member_id': 'str',
        'member_name': 'str',
        'member_status': 'str',
        'workspace': 'str',
        'cluster_type': 'str',
        'cluster_id': 'str',
        'cluster_name': 'str',
        'create_time': 'int',
        'create_user': 'str',
        'deadline': 'int'
    }

    attribute_map = {
        'id': 'id',
        'permission_set_id': 'permission_set_id',
        'project_id': 'project_id',
        'instance_id': 'instance_id',
        'member_type': 'member_type',
        'member_id': 'member_id',
        'member_name': 'member_name',
        'member_status': 'member_status',
        'workspace': 'workspace',
        'cluster_type': 'cluster_type',
        'cluster_id': 'cluster_id',
        'cluster_name': 'cluster_name',
        'create_time': 'create_time',
        'create_user': 'create_user',
        'deadline': 'deadline'
    }

    def __init__(self, id=None, permission_set_id=None, project_id=None, instance_id=None, member_type=None, member_id=None, member_name=None, member_status=None, workspace=None, cluster_type=None, cluster_id=None, cluster_name=None, create_time=None, create_user=None, deadline=None):
        """CreateSecurityPermissionSetMemberResponse

        The model defined in huaweicloud sdk

        :param id: id
        :type id: str
        :param permission_set_id: 权限集id
        :type permission_set_id: str
        :param project_id: 项目id
        :type project_id: str
        :param instance_id: 实例id
        :type instance_id: str
        :param member_type: 成员类型, 用户/用户组/工作空间角色(废弃)/集群角色, USER, USER_GROUP, WORKSPACE_ROLE, CLUSTER_ROLE
        :type member_type: str
        :param member_id: 成员id
        :type member_id: str
        :param member_name: 成员名称
        :type member_name: str
        :param member_status: 成员状态, NORMAL, UNFINISHED
        :type member_status: str
        :param workspace: 工作空间(仅工作空间角色需要)
        :type workspace: str
        :param cluster_type: 集群类型(仅集群角色需要), MRS, DWS, DLI
        :type cluster_type: str
        :param cluster_id: 集群id(仅集群角色需要)
        :type cluster_id: str
        :param cluster_name: 集群名称(仅集群角色需要)
        :type cluster_name: str
        :param create_time: 创建时间
        :type create_time: int
        :param create_user: 创建者
        :type create_user: str
        :param deadline: 到期时间
        :type deadline: int
        """
        
        super(CreateSecurityPermissionSetMemberResponse, self).__init__()

        self._id = None
        self._permission_set_id = None
        self._project_id = None
        self._instance_id = None
        self._member_type = None
        self._member_id = None
        self._member_name = None
        self._member_status = None
        self._workspace = None
        self._cluster_type = None
        self._cluster_id = None
        self._cluster_name = None
        self._create_time = None
        self._create_user = None
        self._deadline = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if permission_set_id is not None:
            self.permission_set_id = permission_set_id
        if project_id is not None:
            self.project_id = project_id
        if instance_id is not None:
            self.instance_id = instance_id
        if member_type is not None:
            self.member_type = member_type
        if member_id is not None:
            self.member_id = member_id
        if member_name is not None:
            self.member_name = member_name
        if member_status is not None:
            self.member_status = member_status
        if workspace is not None:
            self.workspace = workspace
        if cluster_type is not None:
            self.cluster_type = cluster_type
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if cluster_name is not None:
            self.cluster_name = cluster_name
        if create_time is not None:
            self.create_time = create_time
        if create_user is not None:
            self.create_user = create_user
        if deadline is not None:
            self.deadline = deadline

    @property
    def id(self):
        """Gets the id of this CreateSecurityPermissionSetMemberResponse.

        id

        :return: The id of this CreateSecurityPermissionSetMemberResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreateSecurityPermissionSetMemberResponse.

        id

        :param id: The id of this CreateSecurityPermissionSetMemberResponse.
        :type id: str
        """
        self._id = id

    @property
    def permission_set_id(self):
        """Gets the permission_set_id of this CreateSecurityPermissionSetMemberResponse.

        权限集id

        :return: The permission_set_id of this CreateSecurityPermissionSetMemberResponse.
        :rtype: str
        """
        return self._permission_set_id

    @permission_set_id.setter
    def permission_set_id(self, permission_set_id):
        """Sets the permission_set_id of this CreateSecurityPermissionSetMemberResponse.

        权限集id

        :param permission_set_id: The permission_set_id of this CreateSecurityPermissionSetMemberResponse.
        :type permission_set_id: str
        """
        self._permission_set_id = permission_set_id

    @property
    def project_id(self):
        """Gets the project_id of this CreateSecurityPermissionSetMemberResponse.

        项目id

        :return: The project_id of this CreateSecurityPermissionSetMemberResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this CreateSecurityPermissionSetMemberResponse.

        项目id

        :param project_id: The project_id of this CreateSecurityPermissionSetMemberResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def instance_id(self):
        """Gets the instance_id of this CreateSecurityPermissionSetMemberResponse.

        实例id

        :return: The instance_id of this CreateSecurityPermissionSetMemberResponse.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this CreateSecurityPermissionSetMemberResponse.

        实例id

        :param instance_id: The instance_id of this CreateSecurityPermissionSetMemberResponse.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def member_type(self):
        """Gets the member_type of this CreateSecurityPermissionSetMemberResponse.

        成员类型, 用户/用户组/工作空间角色(废弃)/集群角色, USER, USER_GROUP, WORKSPACE_ROLE, CLUSTER_ROLE

        :return: The member_type of this CreateSecurityPermissionSetMemberResponse.
        :rtype: str
        """
        return self._member_type

    @member_type.setter
    def member_type(self, member_type):
        """Sets the member_type of this CreateSecurityPermissionSetMemberResponse.

        成员类型, 用户/用户组/工作空间角色(废弃)/集群角色, USER, USER_GROUP, WORKSPACE_ROLE, CLUSTER_ROLE

        :param member_type: The member_type of this CreateSecurityPermissionSetMemberResponse.
        :type member_type: str
        """
        self._member_type = member_type

    @property
    def member_id(self):
        """Gets the member_id of this CreateSecurityPermissionSetMemberResponse.

        成员id

        :return: The member_id of this CreateSecurityPermissionSetMemberResponse.
        :rtype: str
        """
        return self._member_id

    @member_id.setter
    def member_id(self, member_id):
        """Sets the member_id of this CreateSecurityPermissionSetMemberResponse.

        成员id

        :param member_id: The member_id of this CreateSecurityPermissionSetMemberResponse.
        :type member_id: str
        """
        self._member_id = member_id

    @property
    def member_name(self):
        """Gets the member_name of this CreateSecurityPermissionSetMemberResponse.

        成员名称

        :return: The member_name of this CreateSecurityPermissionSetMemberResponse.
        :rtype: str
        """
        return self._member_name

    @member_name.setter
    def member_name(self, member_name):
        """Sets the member_name of this CreateSecurityPermissionSetMemberResponse.

        成员名称

        :param member_name: The member_name of this CreateSecurityPermissionSetMemberResponse.
        :type member_name: str
        """
        self._member_name = member_name

    @property
    def member_status(self):
        """Gets the member_status of this CreateSecurityPermissionSetMemberResponse.

        成员状态, NORMAL, UNFINISHED

        :return: The member_status of this CreateSecurityPermissionSetMemberResponse.
        :rtype: str
        """
        return self._member_status

    @member_status.setter
    def member_status(self, member_status):
        """Sets the member_status of this CreateSecurityPermissionSetMemberResponse.

        成员状态, NORMAL, UNFINISHED

        :param member_status: The member_status of this CreateSecurityPermissionSetMemberResponse.
        :type member_status: str
        """
        self._member_status = member_status

    @property
    def workspace(self):
        """Gets the workspace of this CreateSecurityPermissionSetMemberResponse.

        工作空间(仅工作空间角色需要)

        :return: The workspace of this CreateSecurityPermissionSetMemberResponse.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        """Sets the workspace of this CreateSecurityPermissionSetMemberResponse.

        工作空间(仅工作空间角色需要)

        :param workspace: The workspace of this CreateSecurityPermissionSetMemberResponse.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def cluster_type(self):
        """Gets the cluster_type of this CreateSecurityPermissionSetMemberResponse.

        集群类型(仅集群角色需要), MRS, DWS, DLI

        :return: The cluster_type of this CreateSecurityPermissionSetMemberResponse.
        :rtype: str
        """
        return self._cluster_type

    @cluster_type.setter
    def cluster_type(self, cluster_type):
        """Sets the cluster_type of this CreateSecurityPermissionSetMemberResponse.

        集群类型(仅集群角色需要), MRS, DWS, DLI

        :param cluster_type: The cluster_type of this CreateSecurityPermissionSetMemberResponse.
        :type cluster_type: str
        """
        self._cluster_type = cluster_type

    @property
    def cluster_id(self):
        """Gets the cluster_id of this CreateSecurityPermissionSetMemberResponse.

        集群id(仅集群角色需要)

        :return: The cluster_id of this CreateSecurityPermissionSetMemberResponse.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this CreateSecurityPermissionSetMemberResponse.

        集群id(仅集群角色需要)

        :param cluster_id: The cluster_id of this CreateSecurityPermissionSetMemberResponse.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def cluster_name(self):
        """Gets the cluster_name of this CreateSecurityPermissionSetMemberResponse.

        集群名称(仅集群角色需要)

        :return: The cluster_name of this CreateSecurityPermissionSetMemberResponse.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        """Sets the cluster_name of this CreateSecurityPermissionSetMemberResponse.

        集群名称(仅集群角色需要)

        :param cluster_name: The cluster_name of this CreateSecurityPermissionSetMemberResponse.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def create_time(self):
        """Gets the create_time of this CreateSecurityPermissionSetMemberResponse.

        创建时间

        :return: The create_time of this CreateSecurityPermissionSetMemberResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this CreateSecurityPermissionSetMemberResponse.

        创建时间

        :param create_time: The create_time of this CreateSecurityPermissionSetMemberResponse.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def create_user(self):
        """Gets the create_user of this CreateSecurityPermissionSetMemberResponse.

        创建者

        :return: The create_user of this CreateSecurityPermissionSetMemberResponse.
        :rtype: str
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        """Sets the create_user of this CreateSecurityPermissionSetMemberResponse.

        创建者

        :param create_user: The create_user of this CreateSecurityPermissionSetMemberResponse.
        :type create_user: str
        """
        self._create_user = create_user

    @property
    def deadline(self):
        """Gets the deadline of this CreateSecurityPermissionSetMemberResponse.

        到期时间

        :return: The deadline of this CreateSecurityPermissionSetMemberResponse.
        :rtype: int
        """
        return self._deadline

    @deadline.setter
    def deadline(self, deadline):
        """Sets the deadline of this CreateSecurityPermissionSetMemberResponse.

        到期时间

        :param deadline: The deadline of this CreateSecurityPermissionSetMemberResponse.
        :type deadline: int
        """
        self._deadline = deadline

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
        if not isinstance(other, CreateSecurityPermissionSetMemberResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
