# coding: utf-8

import pprint
import re

import six





class CreateMigrationTaskBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'task_name': 'str',
        'description': 'str',
        'migration_type': 'str',
        'migration_method': 'str',
        'backup_files': 'BackupFilesBody',
        'network_type': 'str',
        'source_instance': 'SourceInstanceBody',
        'target_instance': 'TargetInstanceBody'
    }

    attribute_map = {
        'task_name': 'task_name',
        'description': 'description',
        'migration_type': 'migration_type',
        'migration_method': 'migration_method',
        'backup_files': 'backup_files',
        'network_type': 'network_type',
        'source_instance': 'source_instance',
        'target_instance': 'target_instance'
    }

    def __init__(self, task_name=None, description=None, migration_type=None, migration_method=None, backup_files=None, network_type=None, source_instance=None, target_instance=None):
        """CreateMigrationTaskBody - a model defined in huaweicloud sdk"""
        
        

        self._task_name = None
        self._description = None
        self._migration_type = None
        self._migration_method = None
        self._backup_files = None
        self._network_type = None
        self._source_instance = None
        self._target_instance = None
        self.discriminator = None

        self.task_name = task_name
        if description is not None:
            self.description = description
        self.migration_type = migration_type
        self.migration_method = migration_method
        if backup_files is not None:
            self.backup_files = backup_files
        if network_type is not None:
            self.network_type = network_type
        if source_instance is not None:
            self.source_instance = source_instance
        self.target_instance = target_instance

    @property
    def task_name(self):
        """Gets the task_name of this CreateMigrationTaskBody.

        迁移任务名称。

        :return: The task_name of this CreateMigrationTaskBody.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        """Sets the task_name of this CreateMigrationTaskBody.

        迁移任务名称。

        :param task_name: The task_name of this CreateMigrationTaskBody.
        :type: str
        """
        self._task_name = task_name

    @property
    def description(self):
        """Gets the description of this CreateMigrationTaskBody.

        迁移任务描述。

        :return: The description of this CreateMigrationTaskBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateMigrationTaskBody.

        迁移任务描述。

        :param description: The description of this CreateMigrationTaskBody.
        :type: str
        """
        self._description = description

    @property
    def migration_type(self):
        """Gets the migration_type of this CreateMigrationTaskBody.

        迁移任务类型,包括备份文件导入和在线迁移两种类型。 取值范围： - backupfile_import：表示备份文件导入 - online_migration：表示在线迁移。 

        :return: The migration_type of this CreateMigrationTaskBody.
        :rtype: str
        """
        return self._migration_type

    @migration_type.setter
    def migration_type(self, migration_type):
        """Sets the migration_type of this CreateMigrationTaskBody.

        迁移任务类型,包括备份文件导入和在线迁移两种类型。 取值范围： - backupfile_import：表示备份文件导入 - online_migration：表示在线迁移。 

        :param migration_type: The migration_type of this CreateMigrationTaskBody.
        :type: str
        """
        self._migration_type = migration_type

    @property
    def migration_method(self):
        """Gets the migration_method of this CreateMigrationTaskBody.

        迁移方式，包括全量迁移和增量迁移两种类型。 取值范围： - full_amount_migration：表示全量迁移。 - incremental_migration：表示增量迁移。 

        :return: The migration_method of this CreateMigrationTaskBody.
        :rtype: str
        """
        return self._migration_method

    @migration_method.setter
    def migration_method(self, migration_method):
        """Sets the migration_method of this CreateMigrationTaskBody.

        迁移方式，包括全量迁移和增量迁移两种类型。 取值范围： - full_amount_migration：表示全量迁移。 - incremental_migration：表示增量迁移。 

        :param migration_method: The migration_method of this CreateMigrationTaskBody.
        :type: str
        """
        self._migration_method = migration_method

    @property
    def backup_files(self):
        """Gets the backup_files of this CreateMigrationTaskBody.


        :return: The backup_files of this CreateMigrationTaskBody.
        :rtype: BackupFilesBody
        """
        return self._backup_files

    @backup_files.setter
    def backup_files(self, backup_files):
        """Sets the backup_files of this CreateMigrationTaskBody.


        :param backup_files: The backup_files of this CreateMigrationTaskBody.
        :type: BackupFilesBody
        """
        self._backup_files = backup_files

    @property
    def network_type(self):
        """Gets the network_type of this CreateMigrationTaskBody.

        迁移任务类型为在线迁移时，表示源Redis和目标Redis联通的网络类型，包括vpc和vpn两种类型。 

        :return: The network_type of this CreateMigrationTaskBody.
        :rtype: str
        """
        return self._network_type

    @network_type.setter
    def network_type(self, network_type):
        """Sets the network_type of this CreateMigrationTaskBody.

        迁移任务类型为在线迁移时，表示源Redis和目标Redis联通的网络类型，包括vpc和vpn两种类型。 

        :param network_type: The network_type of this CreateMigrationTaskBody.
        :type: str
        """
        self._network_type = network_type

    @property
    def source_instance(self):
        """Gets the source_instance of this CreateMigrationTaskBody.


        :return: The source_instance of this CreateMigrationTaskBody.
        :rtype: SourceInstanceBody
        """
        return self._source_instance

    @source_instance.setter
    def source_instance(self, source_instance):
        """Sets the source_instance of this CreateMigrationTaskBody.


        :param source_instance: The source_instance of this CreateMigrationTaskBody.
        :type: SourceInstanceBody
        """
        self._source_instance = source_instance

    @property
    def target_instance(self):
        """Gets the target_instance of this CreateMigrationTaskBody.


        :return: The target_instance of this CreateMigrationTaskBody.
        :rtype: TargetInstanceBody
        """
        return self._target_instance

    @target_instance.setter
    def target_instance(self, target_instance):
        """Sets the target_instance of this CreateMigrationTaskBody.


        :param target_instance: The target_instance of this CreateMigrationTaskBody.
        :type: TargetInstanceBody
        """
        self._target_instance = target_instance

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
        if not isinstance(other, CreateMigrationTaskBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
