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
        'updated_at': 'str'
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
        'updated_at': 'updated_at'
    }

    def __init__(self, task_id=None, task_name=None, description=None, status=None, migration_type=None, migration_method=None, ecs_tenant_private_ip=None, backup_files=None, network_type=None, source_instance=None, target_instance=None, created_at=None, updated_at=None):
        """StopMigrationTaskResponse

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

    @property
    def task_id(self):
        """Gets the task_id of this StopMigrationTaskResponse.

        迁移任务ID。

        :return: The task_id of this StopMigrationTaskResponse.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this StopMigrationTaskResponse.

        迁移任务ID。

        :param task_id: The task_id of this StopMigrationTaskResponse.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def task_name(self):
        """Gets the task_name of this StopMigrationTaskResponse.

        迁移任务名称。

        :return: The task_name of this StopMigrationTaskResponse.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        """Sets the task_name of this StopMigrationTaskResponse.

        迁移任务名称。

        :param task_name: The task_name of this StopMigrationTaskResponse.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def description(self):
        """Gets the description of this StopMigrationTaskResponse.

        迁移任务描述。

        :return: The description of this StopMigrationTaskResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this StopMigrationTaskResponse.

        迁移任务描述。

        :param description: The description of this StopMigrationTaskResponse.
        :type description: str
        """
        self._description = description

    @property
    def status(self):
        """Gets the status of this StopMigrationTaskResponse.

        迁移任务状态，这个字段的值包括：SUCCESS, FAILED, MIGRATING，TERMINATED。

        :return: The status of this StopMigrationTaskResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this StopMigrationTaskResponse.

        迁移任务状态，这个字段的值包括：SUCCESS, FAILED, MIGRATING，TERMINATED。

        :param status: The status of this StopMigrationTaskResponse.
        :type status: str
        """
        self._status = status

    @property
    def migration_type(self):
        """Gets the migration_type of this StopMigrationTaskResponse.

        迁移任务类型,包括备份文件导入和在线迁移两种类型。

        :return: The migration_type of this StopMigrationTaskResponse.
        :rtype: str
        """
        return self._migration_type

    @migration_type.setter
    def migration_type(self, migration_type):
        """Sets the migration_type of this StopMigrationTaskResponse.

        迁移任务类型,包括备份文件导入和在线迁移两种类型。

        :param migration_type: The migration_type of this StopMigrationTaskResponse.
        :type migration_type: str
        """
        self._migration_type = migration_type

    @property
    def migration_method(self):
        """Gets the migration_method of this StopMigrationTaskResponse.

        迁移方式，包括全量迁移和增量迁移两种类型。

        :return: The migration_method of this StopMigrationTaskResponse.
        :rtype: str
        """
        return self._migration_method

    @migration_method.setter
    def migration_method(self, migration_method):
        """Sets the migration_method of this StopMigrationTaskResponse.

        迁移方式，包括全量迁移和增量迁移两种类型。

        :param migration_method: The migration_method of this StopMigrationTaskResponse.
        :type migration_method: str
        """
        self._migration_method = migration_method

    @property
    def ecs_tenant_private_ip(self):
        """Gets the ecs_tenant_private_ip of this StopMigrationTaskResponse.

        迁移机租户侧私有IP，与目的/源redis私有IP处于同VPC，可将此IP加入白名单

        :return: The ecs_tenant_private_ip of this StopMigrationTaskResponse.
        :rtype: str
        """
        return self._ecs_tenant_private_ip

    @ecs_tenant_private_ip.setter
    def ecs_tenant_private_ip(self, ecs_tenant_private_ip):
        """Sets the ecs_tenant_private_ip of this StopMigrationTaskResponse.

        迁移机租户侧私有IP，与目的/源redis私有IP处于同VPC，可将此IP加入白名单

        :param ecs_tenant_private_ip: The ecs_tenant_private_ip of this StopMigrationTaskResponse.
        :type ecs_tenant_private_ip: str
        """
        self._ecs_tenant_private_ip = ecs_tenant_private_ip

    @property
    def backup_files(self):
        """Gets the backup_files of this StopMigrationTaskResponse.

        :return: The backup_files of this StopMigrationTaskResponse.
        :rtype: :class:`huaweicloudsdkdcs.v2.BackupFilesBody`
        """
        return self._backup_files

    @backup_files.setter
    def backup_files(self, backup_files):
        """Sets the backup_files of this StopMigrationTaskResponse.

        :param backup_files: The backup_files of this StopMigrationTaskResponse.
        :type backup_files: :class:`huaweicloudsdkdcs.v2.BackupFilesBody`
        """
        self._backup_files = backup_files

    @property
    def network_type(self):
        """Gets the network_type of this StopMigrationTaskResponse.

        网络类型，包括vpc和vpn两种类型。

        :return: The network_type of this StopMigrationTaskResponse.
        :rtype: str
        """
        return self._network_type

    @network_type.setter
    def network_type(self, network_type):
        """Sets the network_type of this StopMigrationTaskResponse.

        网络类型，包括vpc和vpn两种类型。

        :param network_type: The network_type of this StopMigrationTaskResponse.
        :type network_type: str
        """
        self._network_type = network_type

    @property
    def source_instance(self):
        """Gets the source_instance of this StopMigrationTaskResponse.

        :return: The source_instance of this StopMigrationTaskResponse.
        :rtype: :class:`huaweicloudsdkdcs.v2.SourceInstanceBody`
        """
        return self._source_instance

    @source_instance.setter
    def source_instance(self, source_instance):
        """Sets the source_instance of this StopMigrationTaskResponse.

        :param source_instance: The source_instance of this StopMigrationTaskResponse.
        :type source_instance: :class:`huaweicloudsdkdcs.v2.SourceInstanceBody`
        """
        self._source_instance = source_instance

    @property
    def target_instance(self):
        """Gets the target_instance of this StopMigrationTaskResponse.

        :return: The target_instance of this StopMigrationTaskResponse.
        :rtype: :class:`huaweicloudsdkdcs.v2.TargetInstanceBody`
        """
        return self._target_instance

    @target_instance.setter
    def target_instance(self, target_instance):
        """Sets the target_instance of this StopMigrationTaskResponse.

        :param target_instance: The target_instance of this StopMigrationTaskResponse.
        :type target_instance: :class:`huaweicloudsdkdcs.v2.TargetInstanceBody`
        """
        self._target_instance = target_instance

    @property
    def created_at(self):
        """Gets the created_at of this StopMigrationTaskResponse.

        迁移任务创建时间。

        :return: The created_at of this StopMigrationTaskResponse.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this StopMigrationTaskResponse.

        迁移任务创建时间。

        :param created_at: The created_at of this StopMigrationTaskResponse.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this StopMigrationTaskResponse.

        迁移任务完成时间。

        :return: The updated_at of this StopMigrationTaskResponse.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this StopMigrationTaskResponse.

        迁移任务完成时间。

        :param updated_at: The updated_at of this StopMigrationTaskResponse.
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
        if not isinstance(other, StopMigrationTaskResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
