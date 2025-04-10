# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSecurityPermissionSetResponse(SdkResponse):

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
        'parent_id': 'str',
        'name': 'str',
        'description': 'str',
        'type': 'str',
        'managed_cluster_id': 'str',
        'managed_cluster_name': 'str',
        'project_id': 'str',
        'domain_id': 'str',
        'instance_id': 'str',
        'manager_id': 'str',
        'manager_name': 'str',
        'manager_type': 'str',
        'datasource_type': 'str',
        'sync_status': 'str',
        'sync_msg': 'str',
        'sync_time': 'int',
        'create_time': 'int',
        'create_user': 'str',
        'update_time': 'int',
        'update_user': 'str'
    }

    attribute_map = {
        'id': 'id',
        'parent_id': 'parent_id',
        'name': 'name',
        'description': 'description',
        'type': 'type',
        'managed_cluster_id': 'managed_cluster_id',
        'managed_cluster_name': 'managed_cluster_name',
        'project_id': 'project_id',
        'domain_id': 'domain_id',
        'instance_id': 'instance_id',
        'manager_id': 'manager_id',
        'manager_name': 'manager_name',
        'manager_type': 'manager_type',
        'datasource_type': 'datasource_type',
        'sync_status': 'sync_status',
        'sync_msg': 'sync_msg',
        'sync_time': 'sync_time',
        'create_time': 'create_time',
        'create_user': 'create_user',
        'update_time': 'update_time',
        'update_user': 'update_user'
    }

    def __init__(self, id=None, parent_id=None, name=None, description=None, type=None, managed_cluster_id=None, managed_cluster_name=None, project_id=None, domain_id=None, instance_id=None, manager_id=None, manager_name=None, manager_type=None, datasource_type=None, sync_status=None, sync_msg=None, sync_time=None, create_time=None, create_user=None, update_time=None, update_user=None):
        r"""CreateSecurityPermissionSetResponse

        The model defined in huaweicloud sdk

        :param id: 编号
        :type id: str
        :param parent_id: 父权限集id
        :type parent_id: str
        :param name: 名称
        :type name: str
        :param description: 描述
        :type description: str
        :param type: 权限集类型, COMMON, MRS_MANAGED
        :type type: str
        :param managed_cluster_id: 纳管角色所在集群id（仅纳管类权限集需要）
        :type managed_cluster_id: str
        :param managed_cluster_name: 纳管角色所在集群名称（仅纳管类权限集需要）
        :type managed_cluster_name: str
        :param project_id: 项目id
        :type project_id: str
        :param domain_id: 租户id
        :type domain_id: str
        :param instance_id: 实例id
        :type instance_id: str
        :param manager_id: 管理员id
        :type manager_id: str
        :param manager_name: 管理员名称
        :type manager_name: str
        :param manager_type: 管理员类型
        :type manager_type: str
        :param datasource_type: 数据源类型
        :type datasource_type: str
        :param sync_status: 同步状态,UNKNOWN,NOT_SYNC,SYNCING,SYNC_SUCCESS,SYNC_FAIL
        :type sync_status: str
        :param sync_msg: 同步信息
        :type sync_msg: str
        :param sync_time: 同步时间
        :type sync_time: int
        :param create_time: 创建时间
        :type create_time: int
        :param create_user: 创建者
        :type create_user: str
        :param update_time: 更新时间
        :type update_time: int
        :param update_user: 更新者
        :type update_user: str
        """
        
        super(CreateSecurityPermissionSetResponse, self).__init__()

        self._id = None
        self._parent_id = None
        self._name = None
        self._description = None
        self._type = None
        self._managed_cluster_id = None
        self._managed_cluster_name = None
        self._project_id = None
        self._domain_id = None
        self._instance_id = None
        self._manager_id = None
        self._manager_name = None
        self._manager_type = None
        self._datasource_type = None
        self._sync_status = None
        self._sync_msg = None
        self._sync_time = None
        self._create_time = None
        self._create_user = None
        self._update_time = None
        self._update_user = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if parent_id is not None:
            self.parent_id = parent_id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if type is not None:
            self.type = type
        if managed_cluster_id is not None:
            self.managed_cluster_id = managed_cluster_id
        if managed_cluster_name is not None:
            self.managed_cluster_name = managed_cluster_name
        if project_id is not None:
            self.project_id = project_id
        if domain_id is not None:
            self.domain_id = domain_id
        if instance_id is not None:
            self.instance_id = instance_id
        if manager_id is not None:
            self.manager_id = manager_id
        if manager_name is not None:
            self.manager_name = manager_name
        if manager_type is not None:
            self.manager_type = manager_type
        if datasource_type is not None:
            self.datasource_type = datasource_type
        if sync_status is not None:
            self.sync_status = sync_status
        if sync_msg is not None:
            self.sync_msg = sync_msg
        if sync_time is not None:
            self.sync_time = sync_time
        if create_time is not None:
            self.create_time = create_time
        if create_user is not None:
            self.create_user = create_user
        if update_time is not None:
            self.update_time = update_time
        if update_user is not None:
            self.update_user = update_user

    @property
    def id(self):
        r"""Gets the id of this CreateSecurityPermissionSetResponse.

        编号

        :return: The id of this CreateSecurityPermissionSetResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CreateSecurityPermissionSetResponse.

        编号

        :param id: The id of this CreateSecurityPermissionSetResponse.
        :type id: str
        """
        self._id = id

    @property
    def parent_id(self):
        r"""Gets the parent_id of this CreateSecurityPermissionSetResponse.

        父权限集id

        :return: The parent_id of this CreateSecurityPermissionSetResponse.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        r"""Sets the parent_id of this CreateSecurityPermissionSetResponse.

        父权限集id

        :param parent_id: The parent_id of this CreateSecurityPermissionSetResponse.
        :type parent_id: str
        """
        self._parent_id = parent_id

    @property
    def name(self):
        r"""Gets the name of this CreateSecurityPermissionSetResponse.

        名称

        :return: The name of this CreateSecurityPermissionSetResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateSecurityPermissionSetResponse.

        名称

        :param name: The name of this CreateSecurityPermissionSetResponse.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this CreateSecurityPermissionSetResponse.

        描述

        :return: The description of this CreateSecurityPermissionSetResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateSecurityPermissionSetResponse.

        描述

        :param description: The description of this CreateSecurityPermissionSetResponse.
        :type description: str
        """
        self._description = description

    @property
    def type(self):
        r"""Gets the type of this CreateSecurityPermissionSetResponse.

        权限集类型, COMMON, MRS_MANAGED

        :return: The type of this CreateSecurityPermissionSetResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CreateSecurityPermissionSetResponse.

        权限集类型, COMMON, MRS_MANAGED

        :param type: The type of this CreateSecurityPermissionSetResponse.
        :type type: str
        """
        self._type = type

    @property
    def managed_cluster_id(self):
        r"""Gets the managed_cluster_id of this CreateSecurityPermissionSetResponse.

        纳管角色所在集群id（仅纳管类权限集需要）

        :return: The managed_cluster_id of this CreateSecurityPermissionSetResponse.
        :rtype: str
        """
        return self._managed_cluster_id

    @managed_cluster_id.setter
    def managed_cluster_id(self, managed_cluster_id):
        r"""Sets the managed_cluster_id of this CreateSecurityPermissionSetResponse.

        纳管角色所在集群id（仅纳管类权限集需要）

        :param managed_cluster_id: The managed_cluster_id of this CreateSecurityPermissionSetResponse.
        :type managed_cluster_id: str
        """
        self._managed_cluster_id = managed_cluster_id

    @property
    def managed_cluster_name(self):
        r"""Gets the managed_cluster_name of this CreateSecurityPermissionSetResponse.

        纳管角色所在集群名称（仅纳管类权限集需要）

        :return: The managed_cluster_name of this CreateSecurityPermissionSetResponse.
        :rtype: str
        """
        return self._managed_cluster_name

    @managed_cluster_name.setter
    def managed_cluster_name(self, managed_cluster_name):
        r"""Sets the managed_cluster_name of this CreateSecurityPermissionSetResponse.

        纳管角色所在集群名称（仅纳管类权限集需要）

        :param managed_cluster_name: The managed_cluster_name of this CreateSecurityPermissionSetResponse.
        :type managed_cluster_name: str
        """
        self._managed_cluster_name = managed_cluster_name

    @property
    def project_id(self):
        r"""Gets the project_id of this CreateSecurityPermissionSetResponse.

        项目id

        :return: The project_id of this CreateSecurityPermissionSetResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this CreateSecurityPermissionSetResponse.

        项目id

        :param project_id: The project_id of this CreateSecurityPermissionSetResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def domain_id(self):
        r"""Gets the domain_id of this CreateSecurityPermissionSetResponse.

        租户id

        :return: The domain_id of this CreateSecurityPermissionSetResponse.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this CreateSecurityPermissionSetResponse.

        租户id

        :param domain_id: The domain_id of this CreateSecurityPermissionSetResponse.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this CreateSecurityPermissionSetResponse.

        实例id

        :return: The instance_id of this CreateSecurityPermissionSetResponse.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this CreateSecurityPermissionSetResponse.

        实例id

        :param instance_id: The instance_id of this CreateSecurityPermissionSetResponse.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def manager_id(self):
        r"""Gets the manager_id of this CreateSecurityPermissionSetResponse.

        管理员id

        :return: The manager_id of this CreateSecurityPermissionSetResponse.
        :rtype: str
        """
        return self._manager_id

    @manager_id.setter
    def manager_id(self, manager_id):
        r"""Sets the manager_id of this CreateSecurityPermissionSetResponse.

        管理员id

        :param manager_id: The manager_id of this CreateSecurityPermissionSetResponse.
        :type manager_id: str
        """
        self._manager_id = manager_id

    @property
    def manager_name(self):
        r"""Gets the manager_name of this CreateSecurityPermissionSetResponse.

        管理员名称

        :return: The manager_name of this CreateSecurityPermissionSetResponse.
        :rtype: str
        """
        return self._manager_name

    @manager_name.setter
    def manager_name(self, manager_name):
        r"""Sets the manager_name of this CreateSecurityPermissionSetResponse.

        管理员名称

        :param manager_name: The manager_name of this CreateSecurityPermissionSetResponse.
        :type manager_name: str
        """
        self._manager_name = manager_name

    @property
    def manager_type(self):
        r"""Gets the manager_type of this CreateSecurityPermissionSetResponse.

        管理员类型

        :return: The manager_type of this CreateSecurityPermissionSetResponse.
        :rtype: str
        """
        return self._manager_type

    @manager_type.setter
    def manager_type(self, manager_type):
        r"""Sets the manager_type of this CreateSecurityPermissionSetResponse.

        管理员类型

        :param manager_type: The manager_type of this CreateSecurityPermissionSetResponse.
        :type manager_type: str
        """
        self._manager_type = manager_type

    @property
    def datasource_type(self):
        r"""Gets the datasource_type of this CreateSecurityPermissionSetResponse.

        数据源类型

        :return: The datasource_type of this CreateSecurityPermissionSetResponse.
        :rtype: str
        """
        return self._datasource_type

    @datasource_type.setter
    def datasource_type(self, datasource_type):
        r"""Sets the datasource_type of this CreateSecurityPermissionSetResponse.

        数据源类型

        :param datasource_type: The datasource_type of this CreateSecurityPermissionSetResponse.
        :type datasource_type: str
        """
        self._datasource_type = datasource_type

    @property
    def sync_status(self):
        r"""Gets the sync_status of this CreateSecurityPermissionSetResponse.

        同步状态,UNKNOWN,NOT_SYNC,SYNCING,SYNC_SUCCESS,SYNC_FAIL

        :return: The sync_status of this CreateSecurityPermissionSetResponse.
        :rtype: str
        """
        return self._sync_status

    @sync_status.setter
    def sync_status(self, sync_status):
        r"""Sets the sync_status of this CreateSecurityPermissionSetResponse.

        同步状态,UNKNOWN,NOT_SYNC,SYNCING,SYNC_SUCCESS,SYNC_FAIL

        :param sync_status: The sync_status of this CreateSecurityPermissionSetResponse.
        :type sync_status: str
        """
        self._sync_status = sync_status

    @property
    def sync_msg(self):
        r"""Gets the sync_msg of this CreateSecurityPermissionSetResponse.

        同步信息

        :return: The sync_msg of this CreateSecurityPermissionSetResponse.
        :rtype: str
        """
        return self._sync_msg

    @sync_msg.setter
    def sync_msg(self, sync_msg):
        r"""Sets the sync_msg of this CreateSecurityPermissionSetResponse.

        同步信息

        :param sync_msg: The sync_msg of this CreateSecurityPermissionSetResponse.
        :type sync_msg: str
        """
        self._sync_msg = sync_msg

    @property
    def sync_time(self):
        r"""Gets the sync_time of this CreateSecurityPermissionSetResponse.

        同步时间

        :return: The sync_time of this CreateSecurityPermissionSetResponse.
        :rtype: int
        """
        return self._sync_time

    @sync_time.setter
    def sync_time(self, sync_time):
        r"""Sets the sync_time of this CreateSecurityPermissionSetResponse.

        同步时间

        :param sync_time: The sync_time of this CreateSecurityPermissionSetResponse.
        :type sync_time: int
        """
        self._sync_time = sync_time

    @property
    def create_time(self):
        r"""Gets the create_time of this CreateSecurityPermissionSetResponse.

        创建时间

        :return: The create_time of this CreateSecurityPermissionSetResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this CreateSecurityPermissionSetResponse.

        创建时间

        :param create_time: The create_time of this CreateSecurityPermissionSetResponse.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def create_user(self):
        r"""Gets the create_user of this CreateSecurityPermissionSetResponse.

        创建者

        :return: The create_user of this CreateSecurityPermissionSetResponse.
        :rtype: str
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        r"""Sets the create_user of this CreateSecurityPermissionSetResponse.

        创建者

        :param create_user: The create_user of this CreateSecurityPermissionSetResponse.
        :type create_user: str
        """
        self._create_user = create_user

    @property
    def update_time(self):
        r"""Gets the update_time of this CreateSecurityPermissionSetResponse.

        更新时间

        :return: The update_time of this CreateSecurityPermissionSetResponse.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this CreateSecurityPermissionSetResponse.

        更新时间

        :param update_time: The update_time of this CreateSecurityPermissionSetResponse.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def update_user(self):
        r"""Gets the update_user of this CreateSecurityPermissionSetResponse.

        更新者

        :return: The update_user of this CreateSecurityPermissionSetResponse.
        :rtype: str
        """
        return self._update_user

    @update_user.setter
    def update_user(self, update_user):
        r"""Sets the update_user of this CreateSecurityPermissionSetResponse.

        更新者

        :param update_user: The update_user of this CreateSecurityPermissionSetResponse.
        :type update_user: str
        """
        self._update_user = update_user

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
        if not isinstance(other, CreateSecurityPermissionSetResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
