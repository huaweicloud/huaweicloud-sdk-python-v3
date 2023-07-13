# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowProjectResponse(SdkResponse):

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
        'obs_bucket_name': 'str',
        'swr_namespace': 'str',
        'creator': 'str',
        'role': 'str',
        'roles': 'list[ProjectRoleRsp]',
        'size': 'int',
        'status': 'str',
        'tags': 'list[str]',
        'description': 'str',
        'create_time': 'str',
        'update_time': 'str',
        'delete_time': 'str',
        'is_core': 'bool',
        'storage_quota': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'obs_bucket_name': 'obs_bucket_name',
        'swr_namespace': 'swr_namespace',
        'creator': 'creator',
        'role': 'role',
        'roles': 'roles',
        'size': 'size',
        'status': 'status',
        'tags': 'tags',
        'description': 'description',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'delete_time': 'delete_time',
        'is_core': 'is_core',
        'storage_quota': 'storage_quota'
    }

    def __init__(self, id=None, name=None, obs_bucket_name=None, swr_namespace=None, creator=None, role=None, roles=None, size=None, status=None, tags=None, description=None, create_time=None, update_time=None, delete_time=None, is_core=None, storage_quota=None):
        """ShowProjectResponse

        The model defined in huaweicloud sdk

        :param id: 项目id
        :type id: str
        :param name: 项目名称
        :type name: str
        :param obs_bucket_name: 项目桶名
        :type obs_bucket_name: str
        :param swr_namespace: 项目组织名
        :type swr_namespace: str
        :param creator: 项目所有者
        :type creator: str
        :param role: 当前用户在该项目上的角色
        :type role: str
        :param roles: 项目角色列表
        :type roles: list[:class:`huaweicloudsdkeihealth.v1.ProjectRoleRsp`]
        :param size: 项目桶存储量
        :type size: int
        :param status: 项目状态
        :type status: str
        :param tags: 标签列表
        :type tags: list[str]
        :param description: 项目描述
        :type description: str
        :param create_time: 项目创建时间
        :type create_time: str
        :param update_time: 项目更新时间
        :type update_time: str
        :param delete_time: 请求删除时间
        :type delete_time: str
        :param is_core: 是否为核心项目
        :type is_core: bool
        :param storage_quota: 项目数据容量配额，-1表示无容量限制
        :type storage_quota: int
        """
        
        super(ShowProjectResponse, self).__init__()

        self._id = None
        self._name = None
        self._obs_bucket_name = None
        self._swr_namespace = None
        self._creator = None
        self._role = None
        self._roles = None
        self._size = None
        self._status = None
        self._tags = None
        self._description = None
        self._create_time = None
        self._update_time = None
        self._delete_time = None
        self._is_core = None
        self._storage_quota = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if obs_bucket_name is not None:
            self.obs_bucket_name = obs_bucket_name
        if swr_namespace is not None:
            self.swr_namespace = swr_namespace
        if creator is not None:
            self.creator = creator
        if role is not None:
            self.role = role
        if roles is not None:
            self.roles = roles
        if size is not None:
            self.size = size
        if status is not None:
            self.status = status
        if tags is not None:
            self.tags = tags
        if description is not None:
            self.description = description
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if delete_time is not None:
            self.delete_time = delete_time
        if is_core is not None:
            self.is_core = is_core
        if storage_quota is not None:
            self.storage_quota = storage_quota

    @property
    def id(self):
        """Gets the id of this ShowProjectResponse.

        项目id

        :return: The id of this ShowProjectResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowProjectResponse.

        项目id

        :param id: The id of this ShowProjectResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ShowProjectResponse.

        项目名称

        :return: The name of this ShowProjectResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowProjectResponse.

        项目名称

        :param name: The name of this ShowProjectResponse.
        :type name: str
        """
        self._name = name

    @property
    def obs_bucket_name(self):
        """Gets the obs_bucket_name of this ShowProjectResponse.

        项目桶名

        :return: The obs_bucket_name of this ShowProjectResponse.
        :rtype: str
        """
        return self._obs_bucket_name

    @obs_bucket_name.setter
    def obs_bucket_name(self, obs_bucket_name):
        """Sets the obs_bucket_name of this ShowProjectResponse.

        项目桶名

        :param obs_bucket_name: The obs_bucket_name of this ShowProjectResponse.
        :type obs_bucket_name: str
        """
        self._obs_bucket_name = obs_bucket_name

    @property
    def swr_namespace(self):
        """Gets the swr_namespace of this ShowProjectResponse.

        项目组织名

        :return: The swr_namespace of this ShowProjectResponse.
        :rtype: str
        """
        return self._swr_namespace

    @swr_namespace.setter
    def swr_namespace(self, swr_namespace):
        """Sets the swr_namespace of this ShowProjectResponse.

        项目组织名

        :param swr_namespace: The swr_namespace of this ShowProjectResponse.
        :type swr_namespace: str
        """
        self._swr_namespace = swr_namespace

    @property
    def creator(self):
        """Gets the creator of this ShowProjectResponse.

        项目所有者

        :return: The creator of this ShowProjectResponse.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this ShowProjectResponse.

        项目所有者

        :param creator: The creator of this ShowProjectResponse.
        :type creator: str
        """
        self._creator = creator

    @property
    def role(self):
        """Gets the role of this ShowProjectResponse.

        当前用户在该项目上的角色

        :return: The role of this ShowProjectResponse.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this ShowProjectResponse.

        当前用户在该项目上的角色

        :param role: The role of this ShowProjectResponse.
        :type role: str
        """
        self._role = role

    @property
    def roles(self):
        """Gets the roles of this ShowProjectResponse.

        项目角色列表

        :return: The roles of this ShowProjectResponse.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.ProjectRoleRsp`]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this ShowProjectResponse.

        项目角色列表

        :param roles: The roles of this ShowProjectResponse.
        :type roles: list[:class:`huaweicloudsdkeihealth.v1.ProjectRoleRsp`]
        """
        self._roles = roles

    @property
    def size(self):
        """Gets the size of this ShowProjectResponse.

        项目桶存储量

        :return: The size of this ShowProjectResponse.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ShowProjectResponse.

        项目桶存储量

        :param size: The size of this ShowProjectResponse.
        :type size: int
        """
        self._size = size

    @property
    def status(self):
        """Gets the status of this ShowProjectResponse.

        项目状态

        :return: The status of this ShowProjectResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowProjectResponse.

        项目状态

        :param status: The status of this ShowProjectResponse.
        :type status: str
        """
        self._status = status

    @property
    def tags(self):
        """Gets the tags of this ShowProjectResponse.

        标签列表

        :return: The tags of this ShowProjectResponse.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ShowProjectResponse.

        标签列表

        :param tags: The tags of this ShowProjectResponse.
        :type tags: list[str]
        """
        self._tags = tags

    @property
    def description(self):
        """Gets the description of this ShowProjectResponse.

        项目描述

        :return: The description of this ShowProjectResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ShowProjectResponse.

        项目描述

        :param description: The description of this ShowProjectResponse.
        :type description: str
        """
        self._description = description

    @property
    def create_time(self):
        """Gets the create_time of this ShowProjectResponse.

        项目创建时间

        :return: The create_time of this ShowProjectResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ShowProjectResponse.

        项目创建时间

        :param create_time: The create_time of this ShowProjectResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this ShowProjectResponse.

        项目更新时间

        :return: The update_time of this ShowProjectResponse.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this ShowProjectResponse.

        项目更新时间

        :param update_time: The update_time of this ShowProjectResponse.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def delete_time(self):
        """Gets the delete_time of this ShowProjectResponse.

        请求删除时间

        :return: The delete_time of this ShowProjectResponse.
        :rtype: str
        """
        return self._delete_time

    @delete_time.setter
    def delete_time(self, delete_time):
        """Sets the delete_time of this ShowProjectResponse.

        请求删除时间

        :param delete_time: The delete_time of this ShowProjectResponse.
        :type delete_time: str
        """
        self._delete_time = delete_time

    @property
    def is_core(self):
        """Gets the is_core of this ShowProjectResponse.

        是否为核心项目

        :return: The is_core of this ShowProjectResponse.
        :rtype: bool
        """
        return self._is_core

    @is_core.setter
    def is_core(self, is_core):
        """Sets the is_core of this ShowProjectResponse.

        是否为核心项目

        :param is_core: The is_core of this ShowProjectResponse.
        :type is_core: bool
        """
        self._is_core = is_core

    @property
    def storage_quota(self):
        """Gets the storage_quota of this ShowProjectResponse.

        项目数据容量配额，-1表示无容量限制

        :return: The storage_quota of this ShowProjectResponse.
        :rtype: int
        """
        return self._storage_quota

    @storage_quota.setter
    def storage_quota(self, storage_quota):
        """Sets the storage_quota of this ShowProjectResponse.

        项目数据容量配额，-1表示无容量限制

        :param storage_quota: The storage_quota of this ShowProjectResponse.
        :type storage_quota: int
        """
        self._storage_quota = storage_quota

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
        if not isinstance(other, ShowProjectResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
