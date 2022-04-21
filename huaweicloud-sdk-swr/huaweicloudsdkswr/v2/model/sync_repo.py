# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SyncRepo:

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
        'sync_auto': 'bool',
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
        'sync_auto': 'syncAuto',
        'updated_at': 'updatedAt'
    }

    def __init__(self, created_at=None, domain_id=None, domain_name=None, id=None, namespace=None, override=None, remote_namespace=None, remote_region_id=None, repo_name=None, sync_auto=None, updated_at=None):
        """SyncRepo

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
        :param sync_auto: 自动同步
        :type sync_auto: bool
        :param updated_at: 更新时间，UTC日期格式，时间为UTC标准时间，用户需要根据本地时间计算偏移量；如东8区需要+8:00
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
        self._sync_auto = None
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
        self.sync_auto = sync_auto
        self.updated_at = updated_at

    @property
    def created_at(self):
        """Gets the created_at of this SyncRepo.

        创建时间，UTC日期格式，时间为UTC标准时间，用户需要根据本地时间计算偏移量；如东8区需要+8:00

        :return: The created_at of this SyncRepo.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this SyncRepo.

        创建时间，UTC日期格式，时间为UTC标准时间，用户需要根据本地时间计算偏移量；如东8区需要+8:00

        :param created_at: The created_at of this SyncRepo.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def domain_id(self):
        """Gets the domain_id of this SyncRepo.

        租户ID

        :return: The domain_id of this SyncRepo.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this SyncRepo.

        租户ID

        :param domain_id: The domain_id of this SyncRepo.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def domain_name(self):
        """Gets the domain_name of this SyncRepo.

        租户名

        :return: The domain_name of this SyncRepo.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this SyncRepo.

        租户名

        :param domain_name: The domain_name of this SyncRepo.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def id(self):
        """Gets the id of this SyncRepo.

        ID

        :return: The id of this SyncRepo.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SyncRepo.

        ID

        :param id: The id of this SyncRepo.
        :type id: int
        """
        self._id = id

    @property
    def namespace(self):
        """Gets the namespace of this SyncRepo.

        组织名

        :return: The namespace of this SyncRepo.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this SyncRepo.

        组织名

        :param namespace: The namespace of this SyncRepo.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def override(self):
        """Gets the override of this SyncRepo.

        是否覆盖

        :return: The override of this SyncRepo.
        :rtype: bool
        """
        return self._override

    @override.setter
    def override(self, override):
        """Sets the override of this SyncRepo.

        是否覆盖

        :param override: The override of this SyncRepo.
        :type override: bool
        """
        self._override = override

    @property
    def remote_namespace(self):
        """Gets the remote_namespace of this SyncRepo.

        目的组织

        :return: The remote_namespace of this SyncRepo.
        :rtype: str
        """
        return self._remote_namespace

    @remote_namespace.setter
    def remote_namespace(self, remote_namespace):
        """Sets the remote_namespace of this SyncRepo.

        目的组织

        :param remote_namespace: The remote_namespace of this SyncRepo.
        :type remote_namespace: str
        """
        self._remote_namespace = remote_namespace

    @property
    def remote_region_id(self):
        """Gets the remote_region_id of this SyncRepo.

        目的region

        :return: The remote_region_id of this SyncRepo.
        :rtype: str
        """
        return self._remote_region_id

    @remote_region_id.setter
    def remote_region_id(self, remote_region_id):
        """Sets the remote_region_id of this SyncRepo.

        目的region

        :param remote_region_id: The remote_region_id of this SyncRepo.
        :type remote_region_id: str
        """
        self._remote_region_id = remote_region_id

    @property
    def repo_name(self):
        """Gets the repo_name of this SyncRepo.

        仓库名

        :return: The repo_name of this SyncRepo.
        :rtype: str
        """
        return self._repo_name

    @repo_name.setter
    def repo_name(self, repo_name):
        """Sets the repo_name of this SyncRepo.

        仓库名

        :param repo_name: The repo_name of this SyncRepo.
        :type repo_name: str
        """
        self._repo_name = repo_name

    @property
    def sync_auto(self):
        """Gets the sync_auto of this SyncRepo.

        自动同步

        :return: The sync_auto of this SyncRepo.
        :rtype: bool
        """
        return self._sync_auto

    @sync_auto.setter
    def sync_auto(self, sync_auto):
        """Sets the sync_auto of this SyncRepo.

        自动同步

        :param sync_auto: The sync_auto of this SyncRepo.
        :type sync_auto: bool
        """
        self._sync_auto = sync_auto

    @property
    def updated_at(self):
        """Gets the updated_at of this SyncRepo.

        更新时间，UTC日期格式，时间为UTC标准时间，用户需要根据本地时间计算偏移量；如东8区需要+8:00

        :return: The updated_at of this SyncRepo.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this SyncRepo.

        更新时间，UTC日期格式，时间为UTC标准时间，用户需要根据本地时间计算偏移量；如东8区需要+8:00

        :param updated_at: The updated_at of this SyncRepo.
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
        if not isinstance(other, SyncRepo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
