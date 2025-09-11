# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BackupInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'backup_task_fail_reason': 'str',
        'backup_time': 'datetime',
        'deleted': 'bool',
        'end_time': 'datetime',
        'file_size': 'int',
        'file_size_unit': 'str',
        'id': 'str',
        'mode': 'str',
        'name': 'str',
        'percentage': 'int',
        'progress': 'str',
        'restore_task_fail_reason': 'str',
        'sha256': 'str',
        'start_time': 'datetime'
    }

    attribute_map = {
        'backup_task_fail_reason': 'backup_task_fail_reason',
        'backup_time': 'backup_time',
        'deleted': 'deleted',
        'end_time': 'end_time',
        'file_size': 'file_size',
        'file_size_unit': 'file_size_unit',
        'id': 'id',
        'mode': 'mode',
        'name': 'name',
        'percentage': 'percentage',
        'progress': 'progress',
        'restore_task_fail_reason': 'restore_task_fail_reason',
        'sha256': 'sha256',
        'start_time': 'start_time'
    }

    def __init__(self, backup_task_fail_reason=None, backup_time=None, deleted=None, end_time=None, file_size=None, file_size_unit=None, id=None, mode=None, name=None, percentage=None, progress=None, restore_task_fail_reason=None, sha256=None, start_time=None):
        r"""BackupInfo

        The model defined in huaweicloud sdk

        :param backup_task_fail_reason: 备份失败原因
        :type backup_task_fail_reason: str
        :param backup_time: 备份时间,yyyy-MM-dd HH:mm:ss
        :type backup_time: datetime
        :param deleted: 标记删除
        :type deleted: bool
        :param end_time: 备份结束时间,yyyy-MM-dd HH:mm:ss
        :type end_time: datetime
        :param file_size: 文件大小
        :type file_size: int
        :param file_size_unit: 文件大小单位 - Byte - KB - MB - GB
        :type file_size_unit: str
        :param id: 备份ID
        :type id: str
        :param mode: 备份方式 - AUTO：自动备份
        :type mode: str
        :param name: 备份名称
        :type name: str
        :param percentage: 备份进度
        :type percentage: int
        :param progress: 进度 - CLEAN_AFTER_FAILED: 清理失败 - DELETING：删除中 - DELETED：已删除 - DELETE_FAIL：删除失败 - RESTORING_WAITING：恢复等待中 - RESTORING：恢复中 - RESTORED：已恢复 - RESTORE_FAIL：恢复失败 - BACKUP_WAITING：等待备份 - FILE_UPLOAD_WAITING：等待上传备份文件 - FILE_UPLOADING：上传中 - AUTO_BACKUPING：自动备份中 - AUTO_BACKUPED：自动备份结束 - AUTO_BACKUP_FAIL：自动备份失败 - MANUAL_BACKUPING：手动备份中 - MANUAL_BACKUPED：手动备份结束 - MANUAL_BACKUP_FAIL：手动备份失败 - ISAP_WAITING：ISAP等待备份 - ISAP_BACKUPING：ISAP备份中 - ISAP_BACKUPED：ISAP备份成功 - ISAP_BACKUP_FAIL：ISAP备份失败 - ISAP_FILE_UPLOAD_WAITING：ISAP等待上传备份文件 - ISAP_FILE_UPLOADING：ISAP上传中
        :type progress: str
        :param restore_task_fail_reason: 还原失败原因
        :type restore_task_fail_reason: str
        :param sha256: 文件SHA256
        :type sha256: str
        :param start_time: 备份开始时间,yyyy-MM-dd HH:mm:ss
        :type start_time: datetime
        """
        
        

        self._backup_task_fail_reason = None
        self._backup_time = None
        self._deleted = None
        self._end_time = None
        self._file_size = None
        self._file_size_unit = None
        self._id = None
        self._mode = None
        self._name = None
        self._percentage = None
        self._progress = None
        self._restore_task_fail_reason = None
        self._sha256 = None
        self._start_time = None
        self.discriminator = None

        if backup_task_fail_reason is not None:
            self.backup_task_fail_reason = backup_task_fail_reason
        if backup_time is not None:
            self.backup_time = backup_time
        if deleted is not None:
            self.deleted = deleted
        if end_time is not None:
            self.end_time = end_time
        if file_size is not None:
            self.file_size = file_size
        if file_size_unit is not None:
            self.file_size_unit = file_size_unit
        if id is not None:
            self.id = id
        if mode is not None:
            self.mode = mode
        if name is not None:
            self.name = name
        if percentage is not None:
            self.percentage = percentage
        if progress is not None:
            self.progress = progress
        if restore_task_fail_reason is not None:
            self.restore_task_fail_reason = restore_task_fail_reason
        if sha256 is not None:
            self.sha256 = sha256
        if start_time is not None:
            self.start_time = start_time

    @property
    def backup_task_fail_reason(self):
        r"""Gets the backup_task_fail_reason of this BackupInfo.

        备份失败原因

        :return: The backup_task_fail_reason of this BackupInfo.
        :rtype: str
        """
        return self._backup_task_fail_reason

    @backup_task_fail_reason.setter
    def backup_task_fail_reason(self, backup_task_fail_reason):
        r"""Sets the backup_task_fail_reason of this BackupInfo.

        备份失败原因

        :param backup_task_fail_reason: The backup_task_fail_reason of this BackupInfo.
        :type backup_task_fail_reason: str
        """
        self._backup_task_fail_reason = backup_task_fail_reason

    @property
    def backup_time(self):
        r"""Gets the backup_time of this BackupInfo.

        备份时间,yyyy-MM-dd HH:mm:ss

        :return: The backup_time of this BackupInfo.
        :rtype: datetime
        """
        return self._backup_time

    @backup_time.setter
    def backup_time(self, backup_time):
        r"""Sets the backup_time of this BackupInfo.

        备份时间,yyyy-MM-dd HH:mm:ss

        :param backup_time: The backup_time of this BackupInfo.
        :type backup_time: datetime
        """
        self._backup_time = backup_time

    @property
    def deleted(self):
        r"""Gets the deleted of this BackupInfo.

        标记删除

        :return: The deleted of this BackupInfo.
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        r"""Sets the deleted of this BackupInfo.

        标记删除

        :param deleted: The deleted of this BackupInfo.
        :type deleted: bool
        """
        self._deleted = deleted

    @property
    def end_time(self):
        r"""Gets the end_time of this BackupInfo.

        备份结束时间,yyyy-MM-dd HH:mm:ss

        :return: The end_time of this BackupInfo.
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this BackupInfo.

        备份结束时间,yyyy-MM-dd HH:mm:ss

        :param end_time: The end_time of this BackupInfo.
        :type end_time: datetime
        """
        self._end_time = end_time

    @property
    def file_size(self):
        r"""Gets the file_size of this BackupInfo.

        文件大小

        :return: The file_size of this BackupInfo.
        :rtype: int
        """
        return self._file_size

    @file_size.setter
    def file_size(self, file_size):
        r"""Sets the file_size of this BackupInfo.

        文件大小

        :param file_size: The file_size of this BackupInfo.
        :type file_size: int
        """
        self._file_size = file_size

    @property
    def file_size_unit(self):
        r"""Gets the file_size_unit of this BackupInfo.

        文件大小单位 - Byte - KB - MB - GB

        :return: The file_size_unit of this BackupInfo.
        :rtype: str
        """
        return self._file_size_unit

    @file_size_unit.setter
    def file_size_unit(self, file_size_unit):
        r"""Sets the file_size_unit of this BackupInfo.

        文件大小单位 - Byte - KB - MB - GB

        :param file_size_unit: The file_size_unit of this BackupInfo.
        :type file_size_unit: str
        """
        self._file_size_unit = file_size_unit

    @property
    def id(self):
        r"""Gets the id of this BackupInfo.

        备份ID

        :return: The id of this BackupInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this BackupInfo.

        备份ID

        :param id: The id of this BackupInfo.
        :type id: str
        """
        self._id = id

    @property
    def mode(self):
        r"""Gets the mode of this BackupInfo.

        备份方式 - AUTO：自动备份

        :return: The mode of this BackupInfo.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        r"""Sets the mode of this BackupInfo.

        备份方式 - AUTO：自动备份

        :param mode: The mode of this BackupInfo.
        :type mode: str
        """
        self._mode = mode

    @property
    def name(self):
        r"""Gets the name of this BackupInfo.

        备份名称

        :return: The name of this BackupInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this BackupInfo.

        备份名称

        :param name: The name of this BackupInfo.
        :type name: str
        """
        self._name = name

    @property
    def percentage(self):
        r"""Gets the percentage of this BackupInfo.

        备份进度

        :return: The percentage of this BackupInfo.
        :rtype: int
        """
        return self._percentage

    @percentage.setter
    def percentage(self, percentage):
        r"""Sets the percentage of this BackupInfo.

        备份进度

        :param percentage: The percentage of this BackupInfo.
        :type percentage: int
        """
        self._percentage = percentage

    @property
    def progress(self):
        r"""Gets the progress of this BackupInfo.

        进度 - CLEAN_AFTER_FAILED: 清理失败 - DELETING：删除中 - DELETED：已删除 - DELETE_FAIL：删除失败 - RESTORING_WAITING：恢复等待中 - RESTORING：恢复中 - RESTORED：已恢复 - RESTORE_FAIL：恢复失败 - BACKUP_WAITING：等待备份 - FILE_UPLOAD_WAITING：等待上传备份文件 - FILE_UPLOADING：上传中 - AUTO_BACKUPING：自动备份中 - AUTO_BACKUPED：自动备份结束 - AUTO_BACKUP_FAIL：自动备份失败 - MANUAL_BACKUPING：手动备份中 - MANUAL_BACKUPED：手动备份结束 - MANUAL_BACKUP_FAIL：手动备份失败 - ISAP_WAITING：ISAP等待备份 - ISAP_BACKUPING：ISAP备份中 - ISAP_BACKUPED：ISAP备份成功 - ISAP_BACKUP_FAIL：ISAP备份失败 - ISAP_FILE_UPLOAD_WAITING：ISAP等待上传备份文件 - ISAP_FILE_UPLOADING：ISAP上传中

        :return: The progress of this BackupInfo.
        :rtype: str
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        r"""Sets the progress of this BackupInfo.

        进度 - CLEAN_AFTER_FAILED: 清理失败 - DELETING：删除中 - DELETED：已删除 - DELETE_FAIL：删除失败 - RESTORING_WAITING：恢复等待中 - RESTORING：恢复中 - RESTORED：已恢复 - RESTORE_FAIL：恢复失败 - BACKUP_WAITING：等待备份 - FILE_UPLOAD_WAITING：等待上传备份文件 - FILE_UPLOADING：上传中 - AUTO_BACKUPING：自动备份中 - AUTO_BACKUPED：自动备份结束 - AUTO_BACKUP_FAIL：自动备份失败 - MANUAL_BACKUPING：手动备份中 - MANUAL_BACKUPED：手动备份结束 - MANUAL_BACKUP_FAIL：手动备份失败 - ISAP_WAITING：ISAP等待备份 - ISAP_BACKUPING：ISAP备份中 - ISAP_BACKUPED：ISAP备份成功 - ISAP_BACKUP_FAIL：ISAP备份失败 - ISAP_FILE_UPLOAD_WAITING：ISAP等待上传备份文件 - ISAP_FILE_UPLOADING：ISAP上传中

        :param progress: The progress of this BackupInfo.
        :type progress: str
        """
        self._progress = progress

    @property
    def restore_task_fail_reason(self):
        r"""Gets the restore_task_fail_reason of this BackupInfo.

        还原失败原因

        :return: The restore_task_fail_reason of this BackupInfo.
        :rtype: str
        """
        return self._restore_task_fail_reason

    @restore_task_fail_reason.setter
    def restore_task_fail_reason(self, restore_task_fail_reason):
        r"""Sets the restore_task_fail_reason of this BackupInfo.

        还原失败原因

        :param restore_task_fail_reason: The restore_task_fail_reason of this BackupInfo.
        :type restore_task_fail_reason: str
        """
        self._restore_task_fail_reason = restore_task_fail_reason

    @property
    def sha256(self):
        r"""Gets the sha256 of this BackupInfo.

        文件SHA256

        :return: The sha256 of this BackupInfo.
        :rtype: str
        """
        return self._sha256

    @sha256.setter
    def sha256(self, sha256):
        r"""Sets the sha256 of this BackupInfo.

        文件SHA256

        :param sha256: The sha256 of this BackupInfo.
        :type sha256: str
        """
        self._sha256 = sha256

    @property
    def start_time(self):
        r"""Gets the start_time of this BackupInfo.

        备份开始时间,yyyy-MM-dd HH:mm:ss

        :return: The start_time of this BackupInfo.
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this BackupInfo.

        备份开始时间,yyyy-MM-dd HH:mm:ss

        :param start_time: The start_time of this BackupInfo.
        :type start_time: datetime
        """
        self._start_time = start_time

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
        if not isinstance(other, BackupInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
