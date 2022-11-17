# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SyncJob:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'created_at': 'str',
        'domain_id': 'str',
        'domain_name': 'str',
        'id': 'int',
        'namespace': 'str',
        'override': 'bool',
        'remote_namespace': 'str',
        'remote_region_id': 'str',
        'repo_name': 'str',
        'status': 'str',
        'sync_operator_id': 'str',
        'sync_operator_name': 'str',
        'tag': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'created_at': 'createdAt',
        'domain_id': 'domainID',
        'domain_name': 'domainName',
        'id': 'id',
        'namespace': 'namespace',
        'override': 'override',
        'remote_namespace': 'remoteNamespace',
        'remote_region_id': 'remoteRegionId',
        'repo_name': 'repoName',
        'status': 'status',
        'sync_operator_id': 'syncOperatorId',
        'sync_operator_name': 'syncOperatorName',
        'tag': 'tag',
        'updated_at': 'updatedAt'
    }

    def __init__(self, created_at=None, domain_id=None, domain_name=None, id=None, namespace=None, override=None, remote_namespace=None, remote_region_id=None, repo_name=None, status=None, sync_operator_id=None, sync_operator_name=None, tag=None, updated_at=None):
        """SyncJob

        The model defined in huaweicloud sdk

        :param created_at: 创建时间，UTC日期格式，时间为UTC标准时间，用户需要根据本地时间计算偏移量；如东8区需要+8:00
        :type created_at: str
        :param domain_id: 租户ID
        :type domain_id: str
        :param domain_name: 租户名
        :type domain_name: str
        :param id: ID
        :type id: int
        :param namespace: 组织名
        :type namespace: str
        :param override: 是否覆盖
        :type override: bool
        :param remote_namespace: 目的组织
        :type remote_namespace: str
        :param remote_region_id: 目的region
        :type remote_region_id: str
        :param repo_name: 仓库名
        :type repo_name: str
        :param status: 同步状态,waiting、running、success、failed、timeout、cancel、existed
        :type status: str
        :param sync_operator_id: 操作用户ID
        :type sync_operator_id: str
        :param sync_operator_name: 操作用户名
        :type sync_operator_name: str
        :param tag: 镜像版本
        :type tag: str
        :param updated_at: updatedAt
        :type updated_at: str
        """
        
        

        self._created_at = None
        self._domain_id = None
        self._domain_name = None
        self._id = None
        self._namespace = None
        self._override = None
        self._remote_namespace = None
        self._remote_region_id = None
        self._repo_name = None
        self._status = None
        self._sync_operator_id = None
        self._sync_operator_name = None
        self._tag = None
        self._updated_at = None
        self.discriminator = None

        self.created_at = created_at
        self.domain_id = domain_id
        self.domain_name = domain_name
        self.id = id
        self.namespace = namespace
        self.override = override
        self.remote_namespace = remote_namespace
        self.remote_region_id = remote_region_id
        self.repo_name = repo_name
        self.status = status
        self.sync_operator_id = sync_operator_id
        self.sync_operator_name = sync_operator_name
        self.tag = tag
        self.updated_at = updated_at

    @property
    def created_at(self):
        """Gets the created_at of this SyncJob.

        创建时间，UTC日期格式，时间为UTC标准时间，用户需要根据本地时间计算偏移量；如东8区需要+8:00

        :return: The created_at of this SyncJob.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this SyncJob.

        创建时间，UTC日期格式，时间为UTC标准时间，用户需要根据本地时间计算偏移量；如东8区需要+8:00

        :param created_at: The created_at of this SyncJob.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def domain_id(self):
        """Gets the domain_id of this SyncJob.

        租户ID

        :return: The domain_id of this SyncJob.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this SyncJob.

        租户ID

        :param domain_id: The domain_id of this SyncJob.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def domain_name(self):
        """Gets the domain_name of this SyncJob.

        租户名

        :return: The domain_name of this SyncJob.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this SyncJob.

        租户名

        :param domain_name: The domain_name of this SyncJob.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def id(self):
        """Gets the id of this SyncJob.

        ID

        :return: The id of this SyncJob.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SyncJob.

        ID

        :param id: The id of this SyncJob.
        :type id: int
        """
        self._id = id

    @property
    def namespace(self):
        """Gets the namespace of this SyncJob.

        组织名

        :return: The namespace of this SyncJob.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this SyncJob.

        组织名

        :param namespace: The namespace of this SyncJob.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def override(self):
        """Gets the override of this SyncJob.

        是否覆盖

        :return: The override of this SyncJob.
        :rtype: bool
        """
        return self._override

    @override.setter
    def override(self, override):
        """Sets the override of this SyncJob.

        是否覆盖

        :param override: The override of this SyncJob.
        :type override: bool
        """
        self._override = override

    @property
    def remote_namespace(self):
        """Gets the remote_namespace of this SyncJob.

        目的组织

        :return: The remote_namespace of this SyncJob.
        :rtype: str
        """
        return self._remote_namespace

    @remote_namespace.setter
    def remote_namespace(self, remote_namespace):
        """Sets the remote_namespace of this SyncJob.

        目的组织

        :param remote_namespace: The remote_namespace of this SyncJob.
        :type remote_namespace: str
        """
        self._remote_namespace = remote_namespace

    @property
    def remote_region_id(self):
        """Gets the remote_region_id of this SyncJob.

        目的region

        :return: The remote_region_id of this SyncJob.
        :rtype: str
        """
        return self._remote_region_id

    @remote_region_id.setter
    def remote_region_id(self, remote_region_id):
        """Sets the remote_region_id of this SyncJob.

        目的region

        :param remote_region_id: The remote_region_id of this SyncJob.
        :type remote_region_id: str
        """
        self._remote_region_id = remote_region_id

    @property
    def repo_name(self):
        """Gets the repo_name of this SyncJob.

        仓库名

        :return: The repo_name of this SyncJob.
        :rtype: str
        """
        return self._repo_name

    @repo_name.setter
    def repo_name(self, repo_name):
        """Sets the repo_name of this SyncJob.

        仓库名

        :param repo_name: The repo_name of this SyncJob.
        :type repo_name: str
        """
        self._repo_name = repo_name

    @property
    def status(self):
        """Gets the status of this SyncJob.

        同步状态,waiting、running、success、failed、timeout、cancel、existed

        :return: The status of this SyncJob.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SyncJob.

        同步状态,waiting、running、success、failed、timeout、cancel、existed

        :param status: The status of this SyncJob.
        :type status: str
        """
        self._status = status

    @property
    def sync_operator_id(self):
        """Gets the sync_operator_id of this SyncJob.

        操作用户ID

        :return: The sync_operator_id of this SyncJob.
        :rtype: str
        """
        return self._sync_operator_id

    @sync_operator_id.setter
    def sync_operator_id(self, sync_operator_id):
        """Sets the sync_operator_id of this SyncJob.

        操作用户ID

        :param sync_operator_id: The sync_operator_id of this SyncJob.
        :type sync_operator_id: str
        """
        self._sync_operator_id = sync_operator_id

    @property
    def sync_operator_name(self):
        """Gets the sync_operator_name of this SyncJob.

        操作用户名

        :return: The sync_operator_name of this SyncJob.
        :rtype: str
        """
        return self._sync_operator_name

    @sync_operator_name.setter
    def sync_operator_name(self, sync_operator_name):
        """Sets the sync_operator_name of this SyncJob.

        操作用户名

        :param sync_operator_name: The sync_operator_name of this SyncJob.
        :type sync_operator_name: str
        """
        self._sync_operator_name = sync_operator_name

    @property
    def tag(self):
        """Gets the tag of this SyncJob.

        镜像版本

        :return: The tag of this SyncJob.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this SyncJob.

        镜像版本

        :param tag: The tag of this SyncJob.
        :type tag: str
        """
        self._tag = tag

    @property
    def updated_at(self):
        """Gets the updated_at of this SyncJob.

        updatedAt

        :return: The updated_at of this SyncJob.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this SyncJob.

        updatedAt

        :param updated_at: The updated_at of this SyncJob.
        :type updated_at: str
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
        if not isinstance(other, SyncJob):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
