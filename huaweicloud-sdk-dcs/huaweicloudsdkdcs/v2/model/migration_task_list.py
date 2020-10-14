# coding: utf-8

import pprint
import re

import six





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
        'target_instance_name': 'str',
        'data_source': 'str',
        'created_at': 'str'
    }

    attribute_map = {
        'task_id': 'task_id',
        'task_name': 'task_name',
        'status': 'status',
        'migration_type': 'migration_type',
        'migration_method': 'migration_method',
        'target_instance_name': 'target_instance_name',
        'data_source': 'data_source',
        'created_at': 'created_at'
    }

    def __init__(self, task_id=None, task_name=None, status=None, migration_type=None, migration_method=None, target_instance_name=None, data_source=None, created_at=None):
        """MigrationTaskList - a model defined in huaweicloud sdk"""
        
        

        self._task_id = None
        self._task_name = None
        self._status = None
        self._migration_type = None
        self._migration_method = None
        self._target_instance_name = None
        self._data_source = None
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
        if target_instance_name is not None:
            self.target_instance_name = target_instance_name
        if data_source is not None:
            self.data_source = data_source
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
        :type: str
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
        :type: str
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
        :type: str
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
        :type: str
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
        :type: str
        """
        self._migration_method = migration_method

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
        :type: str
        """
        self._target_instance_name = target_instance_name

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
        :type: str
        """
        self._data_source = data_source

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
        :type: str
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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MigrationTaskList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
