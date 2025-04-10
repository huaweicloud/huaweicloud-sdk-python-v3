# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StopMigrationTaskResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_id': 'str',
        'task_name': 'str',
        'description': 'str',
        'status': 'str',
        'migration_type': 'str',
        'migration_method': 'str',
        'ecs_tenant_private_ip': 'str',
        'backup_files': 'BackupFilesBody',
        'network_type': 'str',
        'source_instance': 'SourceInstanceBody',
        'target_instance': 'TargetInstanceBody',
        'created_at': 'str',
        'updated_at': 'str',
        'released_at': 'str',
        'version': 'str',
        'resume_mode': 'str',
        'supported_features': 'list[str]',
        'tenant_vpc_id': 'str',
        'tenant_subnet_id': 'str',
        'tenant_security_group_id': 'str',
        'bandwidth_limit_mb': 'str',
        'task_status': 'str'
    }

    attribute_map = {
        'task_id': 'task_id',
        'task_name': 'task_name',
        'description': 'description',
        'status': 'status',
        'migration_type': 'migration_type',
        'migration_method': 'migration_method',
        'ecs_tenant_private_ip': 'ecs_tenant_private_ip',
        'backup_files': 'backup_files',
        'network_type': 'network_type',
        'source_instance': 'source_instance',
        'target_instance': 'target_instance',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'released_at': 'released_at',
        'version': 'version',
        'resume_mode': 'resume_mode',
        'supported_features': 'supported_features',
        'tenant_vpc_id': 'tenant_vpc_id',
        'tenant_subnet_id': 'tenant_subnet_id',
        'tenant_security_group_id': 'tenant_security_group_id',
        'bandwidth_limit_mb': 'bandwidth_limit_mb',
        'task_status': 'task_status'
    }

    def __init__(self, task_id=None, task_name=None, description=None, status=None, migration_type=None, migration_method=None, ecs_tenant_private_ip=None, backup_files=None, network_type=None, source_instance=None, target_instance=None, created_at=None, updated_at=None, released_at=None, version=None, resume_mode=None, supported_features=None, tenant_vpc_id=None, tenant_subnet_id=None, tenant_security_group_id=None, bandwidth_limit_mb=None, task_status=None):
        r"""StopMigrationTaskResponse

        The model defined in huaweicloud sdk

        :param task_id: 迁移任务ID。
        :type task_id: str
        :param task_name: 迁移任务名称。
        :type task_name: str
        :param description: 迁移任务描述。
        :type description: str
        :param status: 迁移任务状态，这个字段的值包括：SUCCESS, FAILED, MIGRATING，TERMINATED。
        :type status: str
        :param migration_type: 迁移任务类型,包括备份文件导入和在线迁移两种类型。
        :type migration_type: str
        :param migration_method: 迁移方式，包括全量迁移和增量迁移两种类型。
        :type migration_method: str
        :param ecs_tenant_private_ip: 迁移机租户侧私有IP，与目的/源redis私有IP处于同VPC，可将此IP加入白名单
        :type ecs_tenant_private_ip: str
        :param backup_files: 
        :type backup_files: :class:`huaweicloudsdkdcs.v2.BackupFilesBody`
        :param network_type: 网络类型，包括vpc和vpn两种类型。
        :type network_type: str
        :param source_instance: 
        :type source_instance: :class:`huaweicloudsdkdcs.v2.SourceInstanceBody`
        :param target_instance: 
        :type target_instance: :class:`huaweicloudsdkdcs.v2.TargetInstanceBody`
        :param created_at: 迁移任务创建时间。
        :type created_at: str
        :param updated_at: 迁移任务完成时间。
        :type updated_at: str
        :param released_at: 迁移机释放时间。
        :type released_at: str
        :param version: 版本。
        :type version: str
        :param resume_mode: 操作模式，分为auto和manual。
        :type resume_mode: str
        :param supported_features: 支持的特性。
        :type supported_features: list[str]
        :param tenant_vpc_id: 租户VPC ID。
        :type tenant_vpc_id: str
        :param tenant_subnet_id: 租户子网ID。
        :type tenant_subnet_id: str
        :param tenant_security_group_id: 租户安全组ID。
        :type tenant_security_group_id: str
        :param bandwidth_limit_mb: 带宽限制速度。
        :type bandwidth_limit_mb: str
        :param task_status: 任务状态。
        :type task_status: str
        """
        
        super(StopMigrationTaskResponse, self).__init__()

        self._task_id = None
        self._task_name = None
        self._description = None
        self._status = None
        self._migration_type = None
        self._migration_method = None
        self._ecs_tenant_private_ip = None
        self._backup_files = None
        self._network_type = None
        self._source_instance = None
        self._target_instance = None
        self._created_at = None
        self._updated_at = None
        self._released_at = None
        self._version = None
        self._resume_mode = None
        self._supported_features = None
        self._tenant_vpc_id = None
        self._tenant_subnet_id = None
        self._tenant_security_group_id = None
        self._bandwidth_limit_mb = None
        self._task_status = None
        self.discriminator = None

        if task_id is not None:
            self.task_id = task_id
        if task_name is not None:
            self.task_name = task_name
        if description is not None:
            self.description = description
        if status is not None:
            self.status = status
        if migration_type is not None:
            self.migration_type = migration_type
        if migration_method is not None:
            self.migration_method = migration_method
        if ecs_tenant_private_ip is not None:
            self.ecs_tenant_private_ip = ecs_tenant_private_ip
        if backup_files is not None:
            self.backup_files = backup_files
        if network_type is not None:
            self.network_type = network_type
        if source_instance is not None:
            self.source_instance = source_instance
        if target_instance is not None:
            self.target_instance = target_instance
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if released_at is not None:
            self.released_at = released_at
        if version is not None:
            self.version = version
        if resume_mode is not None:
            self.resume_mode = resume_mode
        if supported_features is not None:
            self.supported_features = supported_features
        if tenant_vpc_id is not None:
            self.tenant_vpc_id = tenant_vpc_id
        if tenant_subnet_id is not None:
            self.tenant_subnet_id = tenant_subnet_id
        if tenant_security_group_id is not None:
            self.tenant_security_group_id = tenant_security_group_id
        if bandwidth_limit_mb is not None:
            self.bandwidth_limit_mb = bandwidth_limit_mb
        if task_status is not None:
            self.task_status = task_status

    @property
    def task_id(self):
        r"""Gets the task_id of this StopMigrationTaskResponse.

        迁移任务ID。

        :return: The task_id of this StopMigrationTaskResponse.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this StopMigrationTaskResponse.

        迁移任务ID。

        :param task_id: The task_id of this StopMigrationTaskResponse.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def task_name(self):
        r"""Gets the task_name of this StopMigrationTaskResponse.

        迁移任务名称。

        :return: The task_name of this StopMigrationTaskResponse.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        r"""Sets the task_name of this StopMigrationTaskResponse.

        迁移任务名称。

        :param task_name: The task_name of this StopMigrationTaskResponse.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def description(self):
        r"""Gets the description of this StopMigrationTaskResponse.

        迁移任务描述。

        :return: The description of this StopMigrationTaskResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this StopMigrationTaskResponse.

        迁移任务描述。

        :param description: The description of this StopMigrationTaskResponse.
        :type description: str
        """
        self._description = description

    @property
    def status(self):
        r"""Gets the status of this StopMigrationTaskResponse.

        迁移任务状态，这个字段的值包括：SUCCESS, FAILED, MIGRATING，TERMINATED。

        :return: The status of this StopMigrationTaskResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this StopMigrationTaskResponse.

        迁移任务状态，这个字段的值包括：SUCCESS, FAILED, MIGRATING，TERMINATED。

        :param status: The status of this StopMigrationTaskResponse.
        :type status: str
        """
        self._status = status

    @property
    def migration_type(self):
        r"""Gets the migration_type of this StopMigrationTaskResponse.

        迁移任务类型,包括备份文件导入和在线迁移两种类型。

        :return: The migration_type of this StopMigrationTaskResponse.
        :rtype: str
        """
        return self._migration_type

    @migration_type.setter
    def migration_type(self, migration_type):
        r"""Sets the migration_type of this StopMigrationTaskResponse.

        迁移任务类型,包括备份文件导入和在线迁移两种类型。

        :param migration_type: The migration_type of this StopMigrationTaskResponse.
        :type migration_type: str
        """
        self._migration_type = migration_type

    @property
    def migration_method(self):
        r"""Gets the migration_method of this StopMigrationTaskResponse.

        迁移方式，包括全量迁移和增量迁移两种类型。

        :return: The migration_method of this StopMigrationTaskResponse.
        :rtype: str
        """
        return self._migration_method

    @migration_method.setter
    def migration_method(self, migration_method):
        r"""Sets the migration_method of this StopMigrationTaskResponse.

        迁移方式，包括全量迁移和增量迁移两种类型。

        :param migration_method: The migration_method of this StopMigrationTaskResponse.
        :type migration_method: str
        """
        self._migration_method = migration_method

    @property
    def ecs_tenant_private_ip(self):
        r"""Gets the ecs_tenant_private_ip of this StopMigrationTaskResponse.

        迁移机租户侧私有IP，与目的/源redis私有IP处于同VPC，可将此IP加入白名单

        :return: The ecs_tenant_private_ip of this StopMigrationTaskResponse.
        :rtype: str
        """
        return self._ecs_tenant_private_ip

    @ecs_tenant_private_ip.setter
    def ecs_tenant_private_ip(self, ecs_tenant_private_ip):
        r"""Sets the ecs_tenant_private_ip of this StopMigrationTaskResponse.

        迁移机租户侧私有IP，与目的/源redis私有IP处于同VPC，可将此IP加入白名单

        :param ecs_tenant_private_ip: The ecs_tenant_private_ip of this StopMigrationTaskResponse.
        :type ecs_tenant_private_ip: str
        """
        self._ecs_tenant_private_ip = ecs_tenant_private_ip

    @property
    def backup_files(self):
        r"""Gets the backup_files of this StopMigrationTaskResponse.

        :return: The backup_files of this StopMigrationTaskResponse.
        :rtype: :class:`huaweicloudsdkdcs.v2.BackupFilesBody`
        """
        return self._backup_files

    @backup_files.setter
    def backup_files(self, backup_files):
        r"""Sets the backup_files of this StopMigrationTaskResponse.

        :param backup_files: The backup_files of this StopMigrationTaskResponse.
        :type backup_files: :class:`huaweicloudsdkdcs.v2.BackupFilesBody`
        """
        self._backup_files = backup_files

    @property
    def network_type(self):
        r"""Gets the network_type of this StopMigrationTaskResponse.

        网络类型，包括vpc和vpn两种类型。

        :return: The network_type of this StopMigrationTaskResponse.
        :rtype: str
        """
        return self._network_type

    @network_type.setter
    def network_type(self, network_type):
        r"""Sets the network_type of this StopMigrationTaskResponse.

        网络类型，包括vpc和vpn两种类型。

        :param network_type: The network_type of this StopMigrationTaskResponse.
        :type network_type: str
        """
        self._network_type = network_type

    @property
    def source_instance(self):
        r"""Gets the source_instance of this StopMigrationTaskResponse.

        :return: The source_instance of this StopMigrationTaskResponse.
        :rtype: :class:`huaweicloudsdkdcs.v2.SourceInstanceBody`
        """
        return self._source_instance

    @source_instance.setter
    def source_instance(self, source_instance):
        r"""Sets the source_instance of this StopMigrationTaskResponse.

        :param source_instance: The source_instance of this StopMigrationTaskResponse.
        :type source_instance: :class:`huaweicloudsdkdcs.v2.SourceInstanceBody`
        """
        self._source_instance = source_instance

    @property
    def target_instance(self):
        r"""Gets the target_instance of this StopMigrationTaskResponse.

        :return: The target_instance of this StopMigrationTaskResponse.
        :rtype: :class:`huaweicloudsdkdcs.v2.TargetInstanceBody`
        """
        return self._target_instance

    @target_instance.setter
    def target_instance(self, target_instance):
        r"""Sets the target_instance of this StopMigrationTaskResponse.

        :param target_instance: The target_instance of this StopMigrationTaskResponse.
        :type target_instance: :class:`huaweicloudsdkdcs.v2.TargetInstanceBody`
        """
        self._target_instance = target_instance

    @property
    def created_at(self):
        r"""Gets the created_at of this StopMigrationTaskResponse.

        迁移任务创建时间。

        :return: The created_at of this StopMigrationTaskResponse.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this StopMigrationTaskResponse.

        迁移任务创建时间。

        :param created_at: The created_at of this StopMigrationTaskResponse.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this StopMigrationTaskResponse.

        迁移任务完成时间。

        :return: The updated_at of this StopMigrationTaskResponse.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this StopMigrationTaskResponse.

        迁移任务完成时间。

        :param updated_at: The updated_at of this StopMigrationTaskResponse.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def released_at(self):
        r"""Gets the released_at of this StopMigrationTaskResponse.

        迁移机释放时间。

        :return: The released_at of this StopMigrationTaskResponse.
        :rtype: str
        """
        return self._released_at

    @released_at.setter
    def released_at(self, released_at):
        r"""Sets the released_at of this StopMigrationTaskResponse.

        迁移机释放时间。

        :param released_at: The released_at of this StopMigrationTaskResponse.
        :type released_at: str
        """
        self._released_at = released_at

    @property
    def version(self):
        r"""Gets the version of this StopMigrationTaskResponse.

        版本。

        :return: The version of this StopMigrationTaskResponse.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this StopMigrationTaskResponse.

        版本。

        :param version: The version of this StopMigrationTaskResponse.
        :type version: str
        """
        self._version = version

    @property
    def resume_mode(self):
        r"""Gets the resume_mode of this StopMigrationTaskResponse.

        操作模式，分为auto和manual。

        :return: The resume_mode of this StopMigrationTaskResponse.
        :rtype: str
        """
        return self._resume_mode

    @resume_mode.setter
    def resume_mode(self, resume_mode):
        r"""Sets the resume_mode of this StopMigrationTaskResponse.

        操作模式，分为auto和manual。

        :param resume_mode: The resume_mode of this StopMigrationTaskResponse.
        :type resume_mode: str
        """
        self._resume_mode = resume_mode

    @property
    def supported_features(self):
        r"""Gets the supported_features of this StopMigrationTaskResponse.

        支持的特性。

        :return: The supported_features of this StopMigrationTaskResponse.
        :rtype: list[str]
        """
        return self._supported_features

    @supported_features.setter
    def supported_features(self, supported_features):
        r"""Sets the supported_features of this StopMigrationTaskResponse.

        支持的特性。

        :param supported_features: The supported_features of this StopMigrationTaskResponse.
        :type supported_features: list[str]
        """
        self._supported_features = supported_features

    @property
    def tenant_vpc_id(self):
        r"""Gets the tenant_vpc_id of this StopMigrationTaskResponse.

        租户VPC ID。

        :return: The tenant_vpc_id of this StopMigrationTaskResponse.
        :rtype: str
        """
        return self._tenant_vpc_id

    @tenant_vpc_id.setter
    def tenant_vpc_id(self, tenant_vpc_id):
        r"""Sets the tenant_vpc_id of this StopMigrationTaskResponse.

        租户VPC ID。

        :param tenant_vpc_id: The tenant_vpc_id of this StopMigrationTaskResponse.
        :type tenant_vpc_id: str
        """
        self._tenant_vpc_id = tenant_vpc_id

    @property
    def tenant_subnet_id(self):
        r"""Gets the tenant_subnet_id of this StopMigrationTaskResponse.

        租户子网ID。

        :return: The tenant_subnet_id of this StopMigrationTaskResponse.
        :rtype: str
        """
        return self._tenant_subnet_id

    @tenant_subnet_id.setter
    def tenant_subnet_id(self, tenant_subnet_id):
        r"""Sets the tenant_subnet_id of this StopMigrationTaskResponse.

        租户子网ID。

        :param tenant_subnet_id: The tenant_subnet_id of this StopMigrationTaskResponse.
        :type tenant_subnet_id: str
        """
        self._tenant_subnet_id = tenant_subnet_id

    @property
    def tenant_security_group_id(self):
        r"""Gets the tenant_security_group_id of this StopMigrationTaskResponse.

        租户安全组ID。

        :return: The tenant_security_group_id of this StopMigrationTaskResponse.
        :rtype: str
        """
        return self._tenant_security_group_id

    @tenant_security_group_id.setter
    def tenant_security_group_id(self, tenant_security_group_id):
        r"""Sets the tenant_security_group_id of this StopMigrationTaskResponse.

        租户安全组ID。

        :param tenant_security_group_id: The tenant_security_group_id of this StopMigrationTaskResponse.
        :type tenant_security_group_id: str
        """
        self._tenant_security_group_id = tenant_security_group_id

    @property
    def bandwidth_limit_mb(self):
        r"""Gets the bandwidth_limit_mb of this StopMigrationTaskResponse.

        带宽限制速度。

        :return: The bandwidth_limit_mb of this StopMigrationTaskResponse.
        :rtype: str
        """
        return self._bandwidth_limit_mb

    @bandwidth_limit_mb.setter
    def bandwidth_limit_mb(self, bandwidth_limit_mb):
        r"""Sets the bandwidth_limit_mb of this StopMigrationTaskResponse.

        带宽限制速度。

        :param bandwidth_limit_mb: The bandwidth_limit_mb of this StopMigrationTaskResponse.
        :type bandwidth_limit_mb: str
        """
        self._bandwidth_limit_mb = bandwidth_limit_mb

    @property
    def task_status(self):
        r"""Gets the task_status of this StopMigrationTaskResponse.

        任务状态。

        :return: The task_status of this StopMigrationTaskResponse.
        :rtype: str
        """
        return self._task_status

    @task_status.setter
    def task_status(self, task_status):
        r"""Sets the task_status of this StopMigrationTaskResponse.

        任务状态。

        :param task_status: The task_status of this StopMigrationTaskResponse.
        :type task_status: str
        """
        self._task_status = task_status

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
        if not isinstance(other, StopMigrationTaskResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
