# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MigrationTaskList:

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
        'status': 'str',
        'migration_type': 'str',
        'migration_method': 'str',
        'ecs_tenant_private_ip': 'str',
        'data_source': 'str',
        'source_instance_name': 'str',
        'source_instance_id': 'str',
        'target_instance_addrs': 'str',
        'target_instance_name': 'str',
        'target_instance_id': 'str',
        'created_at': 'str'
    }

    attribute_map = {
        'task_id': 'task_id',
        'task_name': 'task_name',
        'status': 'status',
        'migration_type': 'migration_type',
        'migration_method': 'migration_method',
        'ecs_tenant_private_ip': 'ecs_tenant_private_ip',
        'data_source': 'data_source',
        'source_instance_name': 'source_instance_name',
        'source_instance_id': 'source_instance_id',
        'target_instance_addrs': 'target_instance_addrs',
        'target_instance_name': 'target_instance_name',
        'target_instance_id': 'target_instance_id',
        'created_at': 'created_at'
    }

    def __init__(self, task_id=None, task_name=None, status=None, migration_type=None, migration_method=None, ecs_tenant_private_ip=None, data_source=None, source_instance_name=None, source_instance_id=None, target_instance_addrs=None, target_instance_name=None, target_instance_id=None, created_at=None):
        """MigrationTaskList

        The model defined in huaweicloud sdk

        :param task_id: 迁移任务ID。
        :type task_id: str
        :param task_name: 迁移任务名称。
        :type task_name: str
        :param status: 迁移任务状态，这个字段的值包括：SUCCESS, FAILED, MIGRATING，TERMINATED
        :type status: str
        :param migration_type: 迁移任务类型,包括备份文件导入和在线迁移两种类型。
        :type migration_type: str
        :param migration_method: 迁移方式，包括全量迁移和增量迁移两种类型。
        :type migration_method: str
        :param ecs_tenant_private_ip: 迁移机租户侧私有IP，与目的/源redis私有IP处于同VPC，可将此IP加入白名单
        :type ecs_tenant_private_ip: str
        :param data_source: 数据源，格式为ip:port或者桶名。
        :type data_source: str
        :param source_instance_name: 源实例名称，若自建redis则为空。
        :type source_instance_name: str
        :param source_instance_id: 源实例ID，若自建redis则为空。
        :type source_instance_id: str
        :param target_instance_addrs: 目标redis地址，格式为ip:port。
        :type target_instance_addrs: str
        :param target_instance_name: 目标实例名称。
        :type target_instance_name: str
        :param target_instance_id: 目标实例ID。
        :type target_instance_id: str
        :param created_at: 迁移任务创建时间
        :type created_at: str
        """
        
        

        self._task_id = None
        self._task_name = None
        self._status = None
        self._migration_type = None
        self._migration_method = None
        self._ecs_tenant_private_ip = None
        self._data_source = None
        self._source_instance_name = None
        self._source_instance_id = None
        self._target_instance_addrs = None
        self._target_instance_name = None
        self._target_instance_id = None
        self._created_at = None
        self.discriminator = None

        if task_id is not None:
            self.task_id = task_id
        if task_name is not None:
            self.task_name = task_name
        if status is not None:
            self.status = status
        if migration_type is not None:
            self.migration_type = migration_type
        if migration_method is not None:
            self.migration_method = migration_method
        if ecs_tenant_private_ip is not None:
            self.ecs_tenant_private_ip = ecs_tenant_private_ip
        if data_source is not None:
            self.data_source = data_source
        if source_instance_name is not None:
            self.source_instance_name = source_instance_name
        if source_instance_id is not None:
            self.source_instance_id = source_instance_id
        if target_instance_addrs is not None:
            self.target_instance_addrs = target_instance_addrs
        if target_instance_name is not None:
            self.target_instance_name = target_instance_name
        if target_instance_id is not None:
            self.target_instance_id = target_instance_id
        if created_at is not None:
            self.created_at = created_at

    @property
    def task_id(self):
        """Gets the task_id of this MigrationTaskList.

        迁移任务ID。

        :return: The task_id of this MigrationTaskList.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this MigrationTaskList.

        迁移任务ID。

        :param task_id: The task_id of this MigrationTaskList.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def task_name(self):
        """Gets the task_name of this MigrationTaskList.

        迁移任务名称。

        :return: The task_name of this MigrationTaskList.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        """Sets the task_name of this MigrationTaskList.

        迁移任务名称。

        :param task_name: The task_name of this MigrationTaskList.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def status(self):
        """Gets the status of this MigrationTaskList.

        迁移任务状态，这个字段的值包括：SUCCESS, FAILED, MIGRATING，TERMINATED

        :return: The status of this MigrationTaskList.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this MigrationTaskList.

        迁移任务状态，这个字段的值包括：SUCCESS, FAILED, MIGRATING，TERMINATED

        :param status: The status of this MigrationTaskList.
        :type status: str
        """
        self._status = status

    @property
    def migration_type(self):
        """Gets the migration_type of this MigrationTaskList.

        迁移任务类型,包括备份文件导入和在线迁移两种类型。

        :return: The migration_type of this MigrationTaskList.
        :rtype: str
        """
        return self._migration_type

    @migration_type.setter
    def migration_type(self, migration_type):
        """Sets the migration_type of this MigrationTaskList.

        迁移任务类型,包括备份文件导入和在线迁移两种类型。

        :param migration_type: The migration_type of this MigrationTaskList.
        :type migration_type: str
        """
        self._migration_type = migration_type

    @property
    def migration_method(self):
        """Gets the migration_method of this MigrationTaskList.

        迁移方式，包括全量迁移和增量迁移两种类型。

        :return: The migration_method of this MigrationTaskList.
        :rtype: str
        """
        return self._migration_method

    @migration_method.setter
    def migration_method(self, migration_method):
        """Sets the migration_method of this MigrationTaskList.

        迁移方式，包括全量迁移和增量迁移两种类型。

        :param migration_method: The migration_method of this MigrationTaskList.
        :type migration_method: str
        """
        self._migration_method = migration_method

    @property
    def ecs_tenant_private_ip(self):
        """Gets the ecs_tenant_private_ip of this MigrationTaskList.

        迁移机租户侧私有IP，与目的/源redis私有IP处于同VPC，可将此IP加入白名单

        :return: The ecs_tenant_private_ip of this MigrationTaskList.
        :rtype: str
        """
        return self._ecs_tenant_private_ip

    @ecs_tenant_private_ip.setter
    def ecs_tenant_private_ip(self, ecs_tenant_private_ip):
        """Sets the ecs_tenant_private_ip of this MigrationTaskList.

        迁移机租户侧私有IP，与目的/源redis私有IP处于同VPC，可将此IP加入白名单

        :param ecs_tenant_private_ip: The ecs_tenant_private_ip of this MigrationTaskList.
        :type ecs_tenant_private_ip: str
        """
        self._ecs_tenant_private_ip = ecs_tenant_private_ip

    @property
    def data_source(self):
        """Gets the data_source of this MigrationTaskList.

        数据源，格式为ip:port或者桶名。

        :return: The data_source of this MigrationTaskList.
        :rtype: str
        """
        return self._data_source

    @data_source.setter
    def data_source(self, data_source):
        """Sets the data_source of this MigrationTaskList.

        数据源，格式为ip:port或者桶名。

        :param data_source: The data_source of this MigrationTaskList.
        :type data_source: str
        """
        self._data_source = data_source

    @property
    def source_instance_name(self):
        """Gets the source_instance_name of this MigrationTaskList.

        源实例名称，若自建redis则为空。

        :return: The source_instance_name of this MigrationTaskList.
        :rtype: str
        """
        return self._source_instance_name

    @source_instance_name.setter
    def source_instance_name(self, source_instance_name):
        """Sets the source_instance_name of this MigrationTaskList.

        源实例名称，若自建redis则为空。

        :param source_instance_name: The source_instance_name of this MigrationTaskList.
        :type source_instance_name: str
        """
        self._source_instance_name = source_instance_name

    @property
    def source_instance_id(self):
        """Gets the source_instance_id of this MigrationTaskList.

        源实例ID，若自建redis则为空。

        :return: The source_instance_id of this MigrationTaskList.
        :rtype: str
        """
        return self._source_instance_id

    @source_instance_id.setter
    def source_instance_id(self, source_instance_id):
        """Sets the source_instance_id of this MigrationTaskList.

        源实例ID，若自建redis则为空。

        :param source_instance_id: The source_instance_id of this MigrationTaskList.
        :type source_instance_id: str
        """
        self._source_instance_id = source_instance_id

    @property
    def target_instance_addrs(self):
        """Gets the target_instance_addrs of this MigrationTaskList.

        目标redis地址，格式为ip:port。

        :return: The target_instance_addrs of this MigrationTaskList.
        :rtype: str
        """
        return self._target_instance_addrs

    @target_instance_addrs.setter
    def target_instance_addrs(self, target_instance_addrs):
        """Sets the target_instance_addrs of this MigrationTaskList.

        目标redis地址，格式为ip:port。

        :param target_instance_addrs: The target_instance_addrs of this MigrationTaskList.
        :type target_instance_addrs: str
        """
        self._target_instance_addrs = target_instance_addrs

    @property
    def target_instance_name(self):
        """Gets the target_instance_name of this MigrationTaskList.

        目标实例名称。

        :return: The target_instance_name of this MigrationTaskList.
        :rtype: str
        """
        return self._target_instance_name

    @target_instance_name.setter
    def target_instance_name(self, target_instance_name):
        """Sets the target_instance_name of this MigrationTaskList.

        目标实例名称。

        :param target_instance_name: The target_instance_name of this MigrationTaskList.
        :type target_instance_name: str
        """
        self._target_instance_name = target_instance_name

    @property
    def target_instance_id(self):
        """Gets the target_instance_id of this MigrationTaskList.

        目标实例ID。

        :return: The target_instance_id of this MigrationTaskList.
        :rtype: str
        """
        return self._target_instance_id

    @target_instance_id.setter
    def target_instance_id(self, target_instance_id):
        """Sets the target_instance_id of this MigrationTaskList.

        目标实例ID。

        :param target_instance_id: The target_instance_id of this MigrationTaskList.
        :type target_instance_id: str
        """
        self._target_instance_id = target_instance_id

    @property
    def created_at(self):
        """Gets the created_at of this MigrationTaskList.

        迁移任务创建时间

        :return: The created_at of this MigrationTaskList.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this MigrationTaskList.

        迁移任务创建时间

        :param created_at: The created_at of this MigrationTaskList.
        :type created_at: str
        """
        self._created_at = created_at

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
        if not isinstance(other, MigrationTaskList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
