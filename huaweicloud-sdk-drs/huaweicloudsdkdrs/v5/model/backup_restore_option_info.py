# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BackupRestoreOptionInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_cover': 'bool',
        'is_default_restore': 'bool',
        'is_last_backup': 'bool',
        'is_precheck': 'bool',
        'recovery_mode': 'str',
        'db_names': 'list[str]',
        'reset_db_name_map': 'dict(str, str)',
        'is_delete_backup_file': 'bool'
    }

    attribute_map = {
        'is_cover': 'is_cover',
        'is_default_restore': 'is_default_restore',
        'is_last_backup': 'is_last_backup',
        'is_precheck': 'is_precheck',
        'recovery_mode': 'recovery_mode',
        'db_names': 'db_names',
        'reset_db_name_map': 'reset_db_name_map',
        'is_delete_backup_file': 'is_delete_backup_file'
    }

    def __init__(self, is_cover=None, is_default_restore=None, is_last_backup=None, is_precheck=None, recovery_mode=None, db_names=None, reset_db_name_map=None, is_delete_backup_file=None):
        r"""BackupRestoreOptionInfo

        The model defined in huaweicloud sdk

        :param is_cover: 是否覆盖目标数据库，不填默认为false。  值为“true”表示覆盖。  值为“false”表示不覆盖。
        :type is_cover: bool
        :param is_default_restore: 是否默认恢复，默认恢复所有数据库。  “true”是代表默认恢复还原备份文件中的全部数据库。  “false”代表需要在db_names这个字段中指定需要恢复的数据库名。
        :type is_default_restore: bool
        :param is_last_backup: 一次典型的增量恢复过程，会涉及多次恢复增量备份。每个增量备份恢复均会使目标数据库保持还原中状态，此时数据库不可读写，直至最后一个增量备份恢复完成后，数据库才能变成可用状态。此后数据库将无法继续进行增量恢复，所以确定为最后一个备份的场景有：  一次性全量迁移，后续将不再进行增量恢复时，设置该字段值为“true”。  增量恢复流程中，确定为最后割接阶段的最后一个增量备份时，设置该字段值为“false”。
        :type is_last_backup: bool
        :param is_precheck: 是否执行预校验。 true：执行。 false：不执行。
        :type is_precheck: bool
        :param recovery_mode: 恢复模式：  “full”表示全量迁移。  “incre”表示增量迁移 。
        :type recovery_mode: str
        :param db_names: 数据库名称。
        :type db_names: list[str]
        :param reset_db_name_map: 该字段为一个map，目前使用格式key是\&quot;\&quot;，value是新数据库名字。 该功能将忽略备份文件中原有的数据库名，通过DRS将其恢复为指定的新数据库名。 使用条件： - 备份文件中只有一个数据库。 - 备份文件是全量备份类型（待恢复备份类型选择：全量备份），且是一次性恢复（最后一个备份选择：是）。
        :type reset_db_name_map: dict(str, str)
        :param is_delete_backup_file: 该参数控制使用OBS桶中备份文件恢复时，当任务结束时是否删除下载到RDS for SQL server磁盘中的OBS备份文件，默认删除。 - true 删除 - false 不删除
        :type is_delete_backup_file: bool
        """
        
        

        self._is_cover = None
        self._is_default_restore = None
        self._is_last_backup = None
        self._is_precheck = None
        self._recovery_mode = None
        self._db_names = None
        self._reset_db_name_map = None
        self._is_delete_backup_file = None
        self.discriminator = None

        if is_cover is not None:
            self.is_cover = is_cover
        if is_default_restore is not None:
            self.is_default_restore = is_default_restore
        self.is_last_backup = is_last_backup
        self.is_precheck = is_precheck
        self.recovery_mode = recovery_mode
        if db_names is not None:
            self.db_names = db_names
        if reset_db_name_map is not None:
            self.reset_db_name_map = reset_db_name_map
        if is_delete_backup_file is not None:
            self.is_delete_backup_file = is_delete_backup_file

    @property
    def is_cover(self):
        r"""Gets the is_cover of this BackupRestoreOptionInfo.

        是否覆盖目标数据库，不填默认为false。  值为“true”表示覆盖。  值为“false”表示不覆盖。

        :return: The is_cover of this BackupRestoreOptionInfo.
        :rtype: bool
        """
        return self._is_cover

    @is_cover.setter
    def is_cover(self, is_cover):
        r"""Sets the is_cover of this BackupRestoreOptionInfo.

        是否覆盖目标数据库，不填默认为false。  值为“true”表示覆盖。  值为“false”表示不覆盖。

        :param is_cover: The is_cover of this BackupRestoreOptionInfo.
        :type is_cover: bool
        """
        self._is_cover = is_cover

    @property
    def is_default_restore(self):
        r"""Gets the is_default_restore of this BackupRestoreOptionInfo.

        是否默认恢复，默认恢复所有数据库。  “true”是代表默认恢复还原备份文件中的全部数据库。  “false”代表需要在db_names这个字段中指定需要恢复的数据库名。

        :return: The is_default_restore of this BackupRestoreOptionInfo.
        :rtype: bool
        """
        return self._is_default_restore

    @is_default_restore.setter
    def is_default_restore(self, is_default_restore):
        r"""Sets the is_default_restore of this BackupRestoreOptionInfo.

        是否默认恢复，默认恢复所有数据库。  “true”是代表默认恢复还原备份文件中的全部数据库。  “false”代表需要在db_names这个字段中指定需要恢复的数据库名。

        :param is_default_restore: The is_default_restore of this BackupRestoreOptionInfo.
        :type is_default_restore: bool
        """
        self._is_default_restore = is_default_restore

    @property
    def is_last_backup(self):
        r"""Gets the is_last_backup of this BackupRestoreOptionInfo.

        一次典型的增量恢复过程，会涉及多次恢复增量备份。每个增量备份恢复均会使目标数据库保持还原中状态，此时数据库不可读写，直至最后一个增量备份恢复完成后，数据库才能变成可用状态。此后数据库将无法继续进行增量恢复，所以确定为最后一个备份的场景有：  一次性全量迁移，后续将不再进行增量恢复时，设置该字段值为“true”。  增量恢复流程中，确定为最后割接阶段的最后一个增量备份时，设置该字段值为“false”。

        :return: The is_last_backup of this BackupRestoreOptionInfo.
        :rtype: bool
        """
        return self._is_last_backup

    @is_last_backup.setter
    def is_last_backup(self, is_last_backup):
        r"""Sets the is_last_backup of this BackupRestoreOptionInfo.

        一次典型的增量恢复过程，会涉及多次恢复增量备份。每个增量备份恢复均会使目标数据库保持还原中状态，此时数据库不可读写，直至最后一个增量备份恢复完成后，数据库才能变成可用状态。此后数据库将无法继续进行增量恢复，所以确定为最后一个备份的场景有：  一次性全量迁移，后续将不再进行增量恢复时，设置该字段值为“true”。  增量恢复流程中，确定为最后割接阶段的最后一个增量备份时，设置该字段值为“false”。

        :param is_last_backup: The is_last_backup of this BackupRestoreOptionInfo.
        :type is_last_backup: bool
        """
        self._is_last_backup = is_last_backup

    @property
    def is_precheck(self):
        r"""Gets the is_precheck of this BackupRestoreOptionInfo.

        是否执行预校验。 true：执行。 false：不执行。

        :return: The is_precheck of this BackupRestoreOptionInfo.
        :rtype: bool
        """
        return self._is_precheck

    @is_precheck.setter
    def is_precheck(self, is_precheck):
        r"""Sets the is_precheck of this BackupRestoreOptionInfo.

        是否执行预校验。 true：执行。 false：不执行。

        :param is_precheck: The is_precheck of this BackupRestoreOptionInfo.
        :type is_precheck: bool
        """
        self._is_precheck = is_precheck

    @property
    def recovery_mode(self):
        r"""Gets the recovery_mode of this BackupRestoreOptionInfo.

        恢复模式：  “full”表示全量迁移。  “incre”表示增量迁移 。

        :return: The recovery_mode of this BackupRestoreOptionInfo.
        :rtype: str
        """
        return self._recovery_mode

    @recovery_mode.setter
    def recovery_mode(self, recovery_mode):
        r"""Sets the recovery_mode of this BackupRestoreOptionInfo.

        恢复模式：  “full”表示全量迁移。  “incre”表示增量迁移 。

        :param recovery_mode: The recovery_mode of this BackupRestoreOptionInfo.
        :type recovery_mode: str
        """
        self._recovery_mode = recovery_mode

    @property
    def db_names(self):
        r"""Gets the db_names of this BackupRestoreOptionInfo.

        数据库名称。

        :return: The db_names of this BackupRestoreOptionInfo.
        :rtype: list[str]
        """
        return self._db_names

    @db_names.setter
    def db_names(self, db_names):
        r"""Sets the db_names of this BackupRestoreOptionInfo.

        数据库名称。

        :param db_names: The db_names of this BackupRestoreOptionInfo.
        :type db_names: list[str]
        """
        self._db_names = db_names

    @property
    def reset_db_name_map(self):
        r"""Gets the reset_db_name_map of this BackupRestoreOptionInfo.

        该字段为一个map，目前使用格式key是\"\"，value是新数据库名字。 该功能将忽略备份文件中原有的数据库名，通过DRS将其恢复为指定的新数据库名。 使用条件： - 备份文件中只有一个数据库。 - 备份文件是全量备份类型（待恢复备份类型选择：全量备份），且是一次性恢复（最后一个备份选择：是）。

        :return: The reset_db_name_map of this BackupRestoreOptionInfo.
        :rtype: dict(str, str)
        """
        return self._reset_db_name_map

    @reset_db_name_map.setter
    def reset_db_name_map(self, reset_db_name_map):
        r"""Sets the reset_db_name_map of this BackupRestoreOptionInfo.

        该字段为一个map，目前使用格式key是\"\"，value是新数据库名字。 该功能将忽略备份文件中原有的数据库名，通过DRS将其恢复为指定的新数据库名。 使用条件： - 备份文件中只有一个数据库。 - 备份文件是全量备份类型（待恢复备份类型选择：全量备份），且是一次性恢复（最后一个备份选择：是）。

        :param reset_db_name_map: The reset_db_name_map of this BackupRestoreOptionInfo.
        :type reset_db_name_map: dict(str, str)
        """
        self._reset_db_name_map = reset_db_name_map

    @property
    def is_delete_backup_file(self):
        r"""Gets the is_delete_backup_file of this BackupRestoreOptionInfo.

        该参数控制使用OBS桶中备份文件恢复时，当任务结束时是否删除下载到RDS for SQL server磁盘中的OBS备份文件，默认删除。 - true 删除 - false 不删除

        :return: The is_delete_backup_file of this BackupRestoreOptionInfo.
        :rtype: bool
        """
        return self._is_delete_backup_file

    @is_delete_backup_file.setter
    def is_delete_backup_file(self, is_delete_backup_file):
        r"""Sets the is_delete_backup_file of this BackupRestoreOptionInfo.

        该参数控制使用OBS桶中备份文件恢复时，当任务结束时是否删除下载到RDS for SQL server磁盘中的OBS备份文件，默认删除。 - true 删除 - false 不删除

        :param is_delete_backup_file: The is_delete_backup_file of this BackupRestoreOptionInfo.
        :type is_delete_backup_file: bool
        """
        self._is_delete_backup_file = is_delete_backup_file

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
        if not isinstance(other, BackupRestoreOptionInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
