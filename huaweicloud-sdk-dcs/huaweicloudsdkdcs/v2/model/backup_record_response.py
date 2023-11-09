# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BackupRecordResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'backup_id': 'str',
        'period': 'str',
        'backup_name': 'str',
        'instance_id': 'str',
        'size': 'int',
        'backup_type': 'str',
        'created_at': 'str',
        'updated_at': 'str',
        'progress': 'str',
        'error_code': 'str',
        'remark': 'str',
        'status': 'str',
        'is_support_restore': 'str',
        'backup_format': 'str',
        'execution_at': 'str'
    }

    attribute_map = {
        'backup_id': 'backup_id',
        'period': 'period',
        'backup_name': 'backup_name',
        'instance_id': 'instance_id',
        'size': 'size',
        'backup_type': 'backup_type',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'progress': 'progress',
        'error_code': 'error_code',
        'remark': 'remark',
        'status': 'status',
        'is_support_restore': 'is_support_restore',
        'backup_format': 'backup_format',
        'execution_at': 'execution_at'
    }

    def __init__(self, backup_id=None, period=None, backup_name=None, instance_id=None, size=None, backup_type=None, created_at=None, updated_at=None, progress=None, error_code=None, remark=None, status=None, is_support_restore=None, backup_format=None, execution_at=None):
        """BackupRecordResponse

        The model defined in huaweicloud sdk

        :param backup_id: 备份记录ID。
        :type backup_id: str
        :param period: 备份执行时间段。
        :type period: str
        :param backup_name: 备份记录名称。
        :type backup_name: str
        :param instance_id: 实例ID。
        :type instance_id: str
        :param size: 备份文件大小（Byte）。
        :type size: int
        :param backup_type: 备份类型。 - manual：表示备份类型为手动备份 - auto：表示备份类型为自动备份 
        :type backup_type: str
        :param created_at: 备份任务创建时间。
        :type created_at: str
        :param updated_at: 备份完成时间。
        :type updated_at: str
        :param progress: 备份进度。
        :type progress: str
        :param error_code: 备份失败后错误码 * &#x60;dcs.08.0001&#x60; - 启动备份恢复工具失败。 * &#x60;dcs.08.0002&#x60; - 执行超时。 * &#x60;dcs.08.0003&#x60; - 删除桶失败。 * &#x60;dcs.08.0004&#x60; - 获取ak/sk 失败。 * &#x60;dcs.08.0005&#x60; - 创建桶失败。 * &#x60;dcs.08.0006&#x60; - 查询备份数据大小失败。 * &#x60;dcs.08.0007&#x60; - 恢复时同步数据失败。 * &#x60;dcs.08.0008&#x60; - 自动备份任务未运行，实例正在运行其他任务。 
        :type error_code: str
        :param remark: 备份缓存实例的备注信息。
        :type remark: str
        :param status: 备份状态。 - waiting：等待中。 - backuping：备份中。 - succeed：备份成功。 - failed：备份失败。 - expired：备份文件过期。 - deleted：已手动删除备份文件。 
        :type status: str
        :param is_support_restore: 是否可以进行恢复操作，取值为TRUE或FALSE。
        :type is_support_restore: str
        :param backup_format: 备份类型。
        :type backup_format: str
        :param execution_at: 执行时间.
        :type execution_at: str
        """
        
        

        self._backup_id = None
        self._period = None
        self._backup_name = None
        self._instance_id = None
        self._size = None
        self._backup_type = None
        self._created_at = None
        self._updated_at = None
        self._progress = None
        self._error_code = None
        self._remark = None
        self._status = None
        self._is_support_restore = None
        self._backup_format = None
        self._execution_at = None
        self.discriminator = None

        if backup_id is not None:
            self.backup_id = backup_id
        if period is not None:
            self.period = period
        if backup_name is not None:
            self.backup_name = backup_name
        if instance_id is not None:
            self.instance_id = instance_id
        if size is not None:
            self.size = size
        if backup_type is not None:
            self.backup_type = backup_type
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if progress is not None:
            self.progress = progress
        if error_code is not None:
            self.error_code = error_code
        if remark is not None:
            self.remark = remark
        if status is not None:
            self.status = status
        if is_support_restore is not None:
            self.is_support_restore = is_support_restore
        if backup_format is not None:
            self.backup_format = backup_format
        if execution_at is not None:
            self.execution_at = execution_at

    @property
    def backup_id(self):
        """Gets the backup_id of this BackupRecordResponse.

        备份记录ID。

        :return: The backup_id of this BackupRecordResponse.
        :rtype: str
        """
        return self._backup_id

    @backup_id.setter
    def backup_id(self, backup_id):
        """Sets the backup_id of this BackupRecordResponse.

        备份记录ID。

        :param backup_id: The backup_id of this BackupRecordResponse.
        :type backup_id: str
        """
        self._backup_id = backup_id

    @property
    def period(self):
        """Gets the period of this BackupRecordResponse.

        备份执行时间段。

        :return: The period of this BackupRecordResponse.
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this BackupRecordResponse.

        备份执行时间段。

        :param period: The period of this BackupRecordResponse.
        :type period: str
        """
        self._period = period

    @property
    def backup_name(self):
        """Gets the backup_name of this BackupRecordResponse.

        备份记录名称。

        :return: The backup_name of this BackupRecordResponse.
        :rtype: str
        """
        return self._backup_name

    @backup_name.setter
    def backup_name(self, backup_name):
        """Sets the backup_name of this BackupRecordResponse.

        备份记录名称。

        :param backup_name: The backup_name of this BackupRecordResponse.
        :type backup_name: str
        """
        self._backup_name = backup_name

    @property
    def instance_id(self):
        """Gets the instance_id of this BackupRecordResponse.

        实例ID。

        :return: The instance_id of this BackupRecordResponse.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this BackupRecordResponse.

        实例ID。

        :param instance_id: The instance_id of this BackupRecordResponse.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def size(self):
        """Gets the size of this BackupRecordResponse.

        备份文件大小（Byte）。

        :return: The size of this BackupRecordResponse.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this BackupRecordResponse.

        备份文件大小（Byte）。

        :param size: The size of this BackupRecordResponse.
        :type size: int
        """
        self._size = size

    @property
    def backup_type(self):
        """Gets the backup_type of this BackupRecordResponse.

        备份类型。 - manual：表示备份类型为手动备份 - auto：表示备份类型为自动备份 

        :return: The backup_type of this BackupRecordResponse.
        :rtype: str
        """
        return self._backup_type

    @backup_type.setter
    def backup_type(self, backup_type):
        """Sets the backup_type of this BackupRecordResponse.

        备份类型。 - manual：表示备份类型为手动备份 - auto：表示备份类型为自动备份 

        :param backup_type: The backup_type of this BackupRecordResponse.
        :type backup_type: str
        """
        self._backup_type = backup_type

    @property
    def created_at(self):
        """Gets the created_at of this BackupRecordResponse.

        备份任务创建时间。

        :return: The created_at of this BackupRecordResponse.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this BackupRecordResponse.

        备份任务创建时间。

        :param created_at: The created_at of this BackupRecordResponse.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this BackupRecordResponse.

        备份完成时间。

        :return: The updated_at of this BackupRecordResponse.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this BackupRecordResponse.

        备份完成时间。

        :param updated_at: The updated_at of this BackupRecordResponse.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def progress(self):
        """Gets the progress of this BackupRecordResponse.

        备份进度。

        :return: The progress of this BackupRecordResponse.
        :rtype: str
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this BackupRecordResponse.

        备份进度。

        :param progress: The progress of this BackupRecordResponse.
        :type progress: str
        """
        self._progress = progress

    @property
    def error_code(self):
        """Gets the error_code of this BackupRecordResponse.

        备份失败后错误码 * `dcs.08.0001` - 启动备份恢复工具失败。 * `dcs.08.0002` - 执行超时。 * `dcs.08.0003` - 删除桶失败。 * `dcs.08.0004` - 获取ak/sk 失败。 * `dcs.08.0005` - 创建桶失败。 * `dcs.08.0006` - 查询备份数据大小失败。 * `dcs.08.0007` - 恢复时同步数据失败。 * `dcs.08.0008` - 自动备份任务未运行，实例正在运行其他任务。 

        :return: The error_code of this BackupRecordResponse.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this BackupRecordResponse.

        备份失败后错误码 * `dcs.08.0001` - 启动备份恢复工具失败。 * `dcs.08.0002` - 执行超时。 * `dcs.08.0003` - 删除桶失败。 * `dcs.08.0004` - 获取ak/sk 失败。 * `dcs.08.0005` - 创建桶失败。 * `dcs.08.0006` - 查询备份数据大小失败。 * `dcs.08.0007` - 恢复时同步数据失败。 * `dcs.08.0008` - 自动备份任务未运行，实例正在运行其他任务。 

        :param error_code: The error_code of this BackupRecordResponse.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def remark(self):
        """Gets the remark of this BackupRecordResponse.

        备份缓存实例的备注信息。

        :return: The remark of this BackupRecordResponse.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this BackupRecordResponse.

        备份缓存实例的备注信息。

        :param remark: The remark of this BackupRecordResponse.
        :type remark: str
        """
        self._remark = remark

    @property
    def status(self):
        """Gets the status of this BackupRecordResponse.

        备份状态。 - waiting：等待中。 - backuping：备份中。 - succeed：备份成功。 - failed：备份失败。 - expired：备份文件过期。 - deleted：已手动删除备份文件。 

        :return: The status of this BackupRecordResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this BackupRecordResponse.

        备份状态。 - waiting：等待中。 - backuping：备份中。 - succeed：备份成功。 - failed：备份失败。 - expired：备份文件过期。 - deleted：已手动删除备份文件。 

        :param status: The status of this BackupRecordResponse.
        :type status: str
        """
        self._status = status

    @property
    def is_support_restore(self):
        """Gets the is_support_restore of this BackupRecordResponse.

        是否可以进行恢复操作，取值为TRUE或FALSE。

        :return: The is_support_restore of this BackupRecordResponse.
        :rtype: str
        """
        return self._is_support_restore

    @is_support_restore.setter
    def is_support_restore(self, is_support_restore):
        """Sets the is_support_restore of this BackupRecordResponse.

        是否可以进行恢复操作，取值为TRUE或FALSE。

        :param is_support_restore: The is_support_restore of this BackupRecordResponse.
        :type is_support_restore: str
        """
        self._is_support_restore = is_support_restore

    @property
    def backup_format(self):
        """Gets the backup_format of this BackupRecordResponse.

        备份类型。

        :return: The backup_format of this BackupRecordResponse.
        :rtype: str
        """
        return self._backup_format

    @backup_format.setter
    def backup_format(self, backup_format):
        """Sets the backup_format of this BackupRecordResponse.

        备份类型。

        :param backup_format: The backup_format of this BackupRecordResponse.
        :type backup_format: str
        """
        self._backup_format = backup_format

    @property
    def execution_at(self):
        """Gets the execution_at of this BackupRecordResponse.

        执行时间.

        :return: The execution_at of this BackupRecordResponse.
        :rtype: str
        """
        return self._execution_at

    @execution_at.setter
    def execution_at(self, execution_at):
        """Sets the execution_at of this BackupRecordResponse.

        执行时间.

        :param execution_at: The execution_at of this BackupRecordResponse.
        :type execution_at: str
        """
        self._execution_at = execution_at

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
        if not isinstance(other, BackupRecordResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
