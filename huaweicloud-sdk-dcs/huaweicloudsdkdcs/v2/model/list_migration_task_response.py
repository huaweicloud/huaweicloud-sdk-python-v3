# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListMigrationTaskResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'migration_tasks': 'list[MigrationTaskList]',
        'target_instance_address': 'str',
        'migration_method': 'str',
        'task_name': 'str',
        'target_instance_id': 'str',
        'source_instance_name': 'str',
        'target_instance_name': 'str',
        'migrate_type': 'str',
        'created_at': 'str',
        'source_instance_id': 'str',
        'task_id': 'str',
        'data_source': 'str',
        'status': 'str'
    }

    attribute_map = {
        'count': 'count',
        'migration_tasks': 'migration_tasks',
        'target_instance_address': 'target_instance_address',
        'migration_method': 'migration_method',
        'task_name': 'task_name',
        'target_instance_id': 'target_instance_id',
        'source_instance_name': 'source_instance_name',
        'target_instance_name': 'target_instance_name',
        'migrate_type': 'migrate_type',
        'created_at': 'created_at',
        'source_instance_id': 'source_instance_id',
        'task_id': 'task_id',
        'data_source': 'data_source',
        'status': 'status'
    }

    def __init__(self, count=None, migration_tasks=None, target_instance_address=None, migration_method=None, task_name=None, target_instance_id=None, source_instance_name=None, target_instance_name=None, migrate_type=None, created_at=None, source_instance_id=None, task_id=None, data_source=None, status=None):
        """ListMigrationTaskResponse

        The model defined in huaweicloud sdk

        :param count: 迁移任务数量。
        :type count: int
        :param migration_tasks: 迁移任务列表。
        :type migration_tasks: list[:class:`huaweicloudsdkdcs.v2.MigrationTaskList`]
        :param target_instance_address: 目标实例地址
        :type target_instance_address: str
        :param migration_method: 迁移方式，包括全量迁移和增量迁移两种类型。
        :type migration_method: str
        :param task_name: 迁移任务名称。
        :type task_name: str
        :param target_instance_id: 目标实例ID。
        :type target_instance_id: str
        :param source_instance_name: 源实例名称，若自建redis则为空。
        :type source_instance_name: str
        :param target_instance_name: 目标实例名称。
        :type target_instance_name: str
        :param migrate_type: 迁移任务类型,包括备份文件导入和在线迁移两种类型。
        :type migrate_type: str
        :param created_at: 迁移任务创建时间
        :type created_at: str
        :param source_instance_id: 源实例ID，若自建redis则为空。
        :type source_instance_id: str
        :param task_id: 迁移任务ID。
        :type task_id: str
        :param data_source: 源redis地址，格式为ip:port或者桶名。
        :type data_source: str
        :param status: 迁移任务状态，这个字段的值包括：SUCCESS, FAILED, MIGRATING，TERMINATED
        :type status: str
        """
        
        super(ListMigrationTaskResponse, self).__init__()

        self._count = None
        self._migration_tasks = None
        self._target_instance_address = None
        self._migration_method = None
        self._task_name = None
        self._target_instance_id = None
        self._source_instance_name = None
        self._target_instance_name = None
        self._migrate_type = None
        self._created_at = None
        self._source_instance_id = None
        self._task_id = None
        self._data_source = None
        self._status = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if migration_tasks is not None:
            self.migration_tasks = migration_tasks
        if target_instance_address is not None:
            self.target_instance_address = target_instance_address
        if migration_method is not None:
            self.migration_method = migration_method
        if task_name is not None:
            self.task_name = task_name
        if target_instance_id is not None:
            self.target_instance_id = target_instance_id
        if source_instance_name is not None:
            self.source_instance_name = source_instance_name
        if target_instance_name is not None:
            self.target_instance_name = target_instance_name
        if migrate_type is not None:
            self.migrate_type = migrate_type
        if created_at is not None:
            self.created_at = created_at
        if source_instance_id is not None:
            self.source_instance_id = source_instance_id
        if task_id is not None:
            self.task_id = task_id
        if data_source is not None:
            self.data_source = data_source
        if status is not None:
            self.status = status

    @property
    def count(self):
        """Gets the count of this ListMigrationTaskResponse.

        迁移任务数量。

        :return: The count of this ListMigrationTaskResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListMigrationTaskResponse.

        迁移任务数量。

        :param count: The count of this ListMigrationTaskResponse.
        :type count: int
        """
        self._count = count

    @property
    def migration_tasks(self):
        """Gets the migration_tasks of this ListMigrationTaskResponse.

        迁移任务列表。

        :return: The migration_tasks of this ListMigrationTaskResponse.
        :rtype: list[:class:`huaweicloudsdkdcs.v2.MigrationTaskList`]
        """
        return self._migration_tasks

    @migration_tasks.setter
    def migration_tasks(self, migration_tasks):
        """Sets the migration_tasks of this ListMigrationTaskResponse.

        迁移任务列表。

        :param migration_tasks: The migration_tasks of this ListMigrationTaskResponse.
        :type migration_tasks: list[:class:`huaweicloudsdkdcs.v2.MigrationTaskList`]
        """
        self._migration_tasks = migration_tasks

    @property
    def target_instance_address(self):
        """Gets the target_instance_address of this ListMigrationTaskResponse.

        目标实例地址

        :return: The target_instance_address of this ListMigrationTaskResponse.
        :rtype: str
        """
        return self._target_instance_address

    @target_instance_address.setter
    def target_instance_address(self, target_instance_address):
        """Sets the target_instance_address of this ListMigrationTaskResponse.

        目标实例地址

        :param target_instance_address: The target_instance_address of this ListMigrationTaskResponse.
        :type target_instance_address: str
        """
        self._target_instance_address = target_instance_address

    @property
    def migration_method(self):
        """Gets the migration_method of this ListMigrationTaskResponse.

        迁移方式，包括全量迁移和增量迁移两种类型。

        :return: The migration_method of this ListMigrationTaskResponse.
        :rtype: str
        """
        return self._migration_method

    @migration_method.setter
    def migration_method(self, migration_method):
        """Sets the migration_method of this ListMigrationTaskResponse.

        迁移方式，包括全量迁移和增量迁移两种类型。

        :param migration_method: The migration_method of this ListMigrationTaskResponse.
        :type migration_method: str
        """
        self._migration_method = migration_method

    @property
    def task_name(self):
        """Gets the task_name of this ListMigrationTaskResponse.

        迁移任务名称。

        :return: The task_name of this ListMigrationTaskResponse.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        """Sets the task_name of this ListMigrationTaskResponse.

        迁移任务名称。

        :param task_name: The task_name of this ListMigrationTaskResponse.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def target_instance_id(self):
        """Gets the target_instance_id of this ListMigrationTaskResponse.

        目标实例ID。

        :return: The target_instance_id of this ListMigrationTaskResponse.
        :rtype: str
        """
        return self._target_instance_id

    @target_instance_id.setter
    def target_instance_id(self, target_instance_id):
        """Sets the target_instance_id of this ListMigrationTaskResponse.

        目标实例ID。

        :param target_instance_id: The target_instance_id of this ListMigrationTaskResponse.
        :type target_instance_id: str
        """
        self._target_instance_id = target_instance_id

    @property
    def source_instance_name(self):
        """Gets the source_instance_name of this ListMigrationTaskResponse.

        源实例名称，若自建redis则为空。

        :return: The source_instance_name of this ListMigrationTaskResponse.
        :rtype: str
        """
        return self._source_instance_name

    @source_instance_name.setter
    def source_instance_name(self, source_instance_name):
        """Sets the source_instance_name of this ListMigrationTaskResponse.

        源实例名称，若自建redis则为空。

        :param source_instance_name: The source_instance_name of this ListMigrationTaskResponse.
        :type source_instance_name: str
        """
        self._source_instance_name = source_instance_name

    @property
    def target_instance_name(self):
        """Gets the target_instance_name of this ListMigrationTaskResponse.

        目标实例名称。

        :return: The target_instance_name of this ListMigrationTaskResponse.
        :rtype: str
        """
        return self._target_instance_name

    @target_instance_name.setter
    def target_instance_name(self, target_instance_name):
        """Sets the target_instance_name of this ListMigrationTaskResponse.

        目标实例名称。

        :param target_instance_name: The target_instance_name of this ListMigrationTaskResponse.
        :type target_instance_name: str
        """
        self._target_instance_name = target_instance_name

    @property
    def migrate_type(self):
        """Gets the migrate_type of this ListMigrationTaskResponse.

        迁移任务类型,包括备份文件导入和在线迁移两种类型。

        :return: The migrate_type of this ListMigrationTaskResponse.
        :rtype: str
        """
        return self._migrate_type

    @migrate_type.setter
    def migrate_type(self, migrate_type):
        """Sets the migrate_type of this ListMigrationTaskResponse.

        迁移任务类型,包括备份文件导入和在线迁移两种类型。

        :param migrate_type: The migrate_type of this ListMigrationTaskResponse.
        :type migrate_type: str
        """
        self._migrate_type = migrate_type

    @property
    def created_at(self):
        """Gets the created_at of this ListMigrationTaskResponse.

        迁移任务创建时间

        :return: The created_at of this ListMigrationTaskResponse.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ListMigrationTaskResponse.

        迁移任务创建时间

        :param created_at: The created_at of this ListMigrationTaskResponse.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def source_instance_id(self):
        """Gets the source_instance_id of this ListMigrationTaskResponse.

        源实例ID，若自建redis则为空。

        :return: The source_instance_id of this ListMigrationTaskResponse.
        :rtype: str
        """
        return self._source_instance_id

    @source_instance_id.setter
    def source_instance_id(self, source_instance_id):
        """Sets the source_instance_id of this ListMigrationTaskResponse.

        源实例ID，若自建redis则为空。

        :param source_instance_id: The source_instance_id of this ListMigrationTaskResponse.
        :type source_instance_id: str
        """
        self._source_instance_id = source_instance_id

    @property
    def task_id(self):
        """Gets the task_id of this ListMigrationTaskResponse.

        迁移任务ID。

        :return: The task_id of this ListMigrationTaskResponse.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this ListMigrationTaskResponse.

        迁移任务ID。

        :param task_id: The task_id of this ListMigrationTaskResponse.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def data_source(self):
        """Gets the data_source of this ListMigrationTaskResponse.

        源redis地址，格式为ip:port或者桶名。

        :return: The data_source of this ListMigrationTaskResponse.
        :rtype: str
        """
        return self._data_source

    @data_source.setter
    def data_source(self, data_source):
        """Sets the data_source of this ListMigrationTaskResponse.

        源redis地址，格式为ip:port或者桶名。

        :param data_source: The data_source of this ListMigrationTaskResponse.
        :type data_source: str
        """
        self._data_source = data_source

    @property
    def status(self):
        """Gets the status of this ListMigrationTaskResponse.

        迁移任务状态，这个字段的值包括：SUCCESS, FAILED, MIGRATING，TERMINATED

        :return: The status of this ListMigrationTaskResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListMigrationTaskResponse.

        迁移任务状态，这个字段的值包括：SUCCESS, FAILED, MIGRATING，TERMINATED

        :param status: The status of this ListMigrationTaskResponse.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, ListMigrationTaskResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
