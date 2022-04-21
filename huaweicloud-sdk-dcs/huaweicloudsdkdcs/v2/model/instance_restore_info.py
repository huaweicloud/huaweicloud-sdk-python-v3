# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstanceRestoreInfo:

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
        'restore_id': 'str',
        'backup_name': 'str',
        'updated_at': 'str',
        'restore_remark': 'str',
        'created_at': 'str',
        'progress': 'str',
        'error_code': 'str',
        'restore_name': 'str',
        'backup_remark': 'str',
        'status': 'str'
    }

    attribute_map = {
        'backup_id': 'backup_id',
        'restore_id': 'restore_id',
        'backup_name': 'backup_name',
        'updated_at': 'updated_at',
        'restore_remark': 'restore_remark',
        'created_at': 'created_at',
        'progress': 'progress',
        'error_code': 'error_code',
        'restore_name': 'restore_name',
        'backup_remark': 'backup_remark',
        'status': 'status'
    }

    def __init__(self, backup_id=None, restore_id=None, backup_name=None, updated_at=None, restore_remark=None, created_at=None, progress=None, error_code=None, restore_name=None, backup_remark=None, status=None):
        """InstanceRestoreInfo

        The model defined in huaweicloud sdk

        :param backup_id: 备份记录ID。
        :type backup_id: str
        :param restore_id: 恢复记录ID。
        :type restore_id: str
        :param backup_name: 备份记录名称。
        :type backup_name: str
        :param updated_at: 恢复完成时间。
        :type updated_at: str
        :param restore_remark: 恢复备注信息。
        :type restore_remark: str
        :param created_at: 恢复任务创建时间。
        :type created_at: str
        :param progress: 恢复进度。
        :type progress: str
        :param error_code: 恢复失败后错误码 * &#x60;dcs.08.0001&#x60; - 启动备份恢复工具失败。 * &#x60;dcs.08.0002&#x60; - 执行超时。 * &#x60;dcs.08.0003&#x60; - 删除桶失败。 * &#x60;dcs.08.0004&#x60; - 获取ak/sk 失败。 * &#x60;dcs.08.0005&#x60; - 创建桶失败。 * &#x60;dcs.08.0006&#x60; - 查询备份数据大小失败。 * &#x60;dcs.08.0007&#x60; - 恢复时同步数据失败。 * &#x60;dcs.08.0008&#x60; - 自动备份任务未运行，实例正在运行其他任务。 
        :type error_code: str
        :param restore_name: 恢复记录名称。
        :type restore_name: str
        :param backup_remark: 备份备注信息。
        :type backup_remark: str
        :param status: 恢复状态。 - waiting：等待中 - restoring：恢复中 - succeed：恢复成功 - failed：恢复失败 
        :type status: str
        """
        
        

        self._backup_id = None
        self._restore_id = None
        self._backup_name = None
        self._updated_at = None
        self._restore_remark = None
        self._created_at = None
        self._progress = None
        self._error_code = None
        self._restore_name = None
        self._backup_remark = None
        self._status = None
        self.discriminator = None

        if backup_id is not None:
            self.backup_id = backup_id
        if restore_id is not None:
            self.restore_id = restore_id
        if backup_name is not None:
            self.backup_name = backup_name
        if updated_at is not None:
            self.updated_at = updated_at
        if restore_remark is not None:
            self.restore_remark = restore_remark
        if created_at is not None:
            self.created_at = created_at
        if progress is not None:
            self.progress = progress
        if error_code is not None:
            self.error_code = error_code
        if restore_name is not None:
            self.restore_name = restore_name
        if backup_remark is not None:
            self.backup_remark = backup_remark
        if status is not None:
            self.status = status

    @property
    def backup_id(self):
        """Gets the backup_id of this InstanceRestoreInfo.

        备份记录ID。

        :return: The backup_id of this InstanceRestoreInfo.
        :rtype: str
        """
        return self._backup_id

    @backup_id.setter
    def backup_id(self, backup_id):
        """Sets the backup_id of this InstanceRestoreInfo.

        备份记录ID。

        :param backup_id: The backup_id of this InstanceRestoreInfo.
        :type backup_id: str
        """
        self._backup_id = backup_id

    @property
    def restore_id(self):
        """Gets the restore_id of this InstanceRestoreInfo.

        恢复记录ID。

        :return: The restore_id of this InstanceRestoreInfo.
        :rtype: str
        """
        return self._restore_id

    @restore_id.setter
    def restore_id(self, restore_id):
        """Sets the restore_id of this InstanceRestoreInfo.

        恢复记录ID。

        :param restore_id: The restore_id of this InstanceRestoreInfo.
        :type restore_id: str
        """
        self._restore_id = restore_id

    @property
    def backup_name(self):
        """Gets the backup_name of this InstanceRestoreInfo.

        备份记录名称。

        :return: The backup_name of this InstanceRestoreInfo.
        :rtype: str
        """
        return self._backup_name

    @backup_name.setter
    def backup_name(self, backup_name):
        """Sets the backup_name of this InstanceRestoreInfo.

        备份记录名称。

        :param backup_name: The backup_name of this InstanceRestoreInfo.
        :type backup_name: str
        """
        self._backup_name = backup_name

    @property
    def updated_at(self):
        """Gets the updated_at of this InstanceRestoreInfo.

        恢复完成时间。

        :return: The updated_at of this InstanceRestoreInfo.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this InstanceRestoreInfo.

        恢复完成时间。

        :param updated_at: The updated_at of this InstanceRestoreInfo.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def restore_remark(self):
        """Gets the restore_remark of this InstanceRestoreInfo.

        恢复备注信息。

        :return: The restore_remark of this InstanceRestoreInfo.
        :rtype: str
        """
        return self._restore_remark

    @restore_remark.setter
    def restore_remark(self, restore_remark):
        """Sets the restore_remark of this InstanceRestoreInfo.

        恢复备注信息。

        :param restore_remark: The restore_remark of this InstanceRestoreInfo.
        :type restore_remark: str
        """
        self._restore_remark = restore_remark

    @property
    def created_at(self):
        """Gets the created_at of this InstanceRestoreInfo.

        恢复任务创建时间。

        :return: The created_at of this InstanceRestoreInfo.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this InstanceRestoreInfo.

        恢复任务创建时间。

        :param created_at: The created_at of this InstanceRestoreInfo.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def progress(self):
        """Gets the progress of this InstanceRestoreInfo.

        恢复进度。

        :return: The progress of this InstanceRestoreInfo.
        :rtype: str
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this InstanceRestoreInfo.

        恢复进度。

        :param progress: The progress of this InstanceRestoreInfo.
        :type progress: str
        """
        self._progress = progress

    @property
    def error_code(self):
        """Gets the error_code of this InstanceRestoreInfo.

        恢复失败后错误码 * `dcs.08.0001` - 启动备份恢复工具失败。 * `dcs.08.0002` - 执行超时。 * `dcs.08.0003` - 删除桶失败。 * `dcs.08.0004` - 获取ak/sk 失败。 * `dcs.08.0005` - 创建桶失败。 * `dcs.08.0006` - 查询备份数据大小失败。 * `dcs.08.0007` - 恢复时同步数据失败。 * `dcs.08.0008` - 自动备份任务未运行，实例正在运行其他任务。 

        :return: The error_code of this InstanceRestoreInfo.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this InstanceRestoreInfo.

        恢复失败后错误码 * `dcs.08.0001` - 启动备份恢复工具失败。 * `dcs.08.0002` - 执行超时。 * `dcs.08.0003` - 删除桶失败。 * `dcs.08.0004` - 获取ak/sk 失败。 * `dcs.08.0005` - 创建桶失败。 * `dcs.08.0006` - 查询备份数据大小失败。 * `dcs.08.0007` - 恢复时同步数据失败。 * `dcs.08.0008` - 自动备份任务未运行，实例正在运行其他任务。 

        :param error_code: The error_code of this InstanceRestoreInfo.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def restore_name(self):
        """Gets the restore_name of this InstanceRestoreInfo.

        恢复记录名称。

        :return: The restore_name of this InstanceRestoreInfo.
        :rtype: str
        """
        return self._restore_name

    @restore_name.setter
    def restore_name(self, restore_name):
        """Sets the restore_name of this InstanceRestoreInfo.

        恢复记录名称。

        :param restore_name: The restore_name of this InstanceRestoreInfo.
        :type restore_name: str
        """
        self._restore_name = restore_name

    @property
    def backup_remark(self):
        """Gets the backup_remark of this InstanceRestoreInfo.

        备份备注信息。

        :return: The backup_remark of this InstanceRestoreInfo.
        :rtype: str
        """
        return self._backup_remark

    @backup_remark.setter
    def backup_remark(self, backup_remark):
        """Sets the backup_remark of this InstanceRestoreInfo.

        备份备注信息。

        :param backup_remark: The backup_remark of this InstanceRestoreInfo.
        :type backup_remark: str
        """
        self._backup_remark = backup_remark

    @property
    def status(self):
        """Gets the status of this InstanceRestoreInfo.

        恢复状态。 - waiting：等待中 - restoring：恢复中 - succeed：恢复成功 - failed：恢复失败 

        :return: The status of this InstanceRestoreInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InstanceRestoreInfo.

        恢复状态。 - waiting：等待中 - restoring：恢复中 - succeed：恢复成功 - failed：恢复失败 

        :param status: The status of this InstanceRestoreInfo.
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
        if not isinstance(other, InstanceRestoreInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
