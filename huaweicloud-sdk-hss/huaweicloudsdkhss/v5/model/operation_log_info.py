# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OperationLogInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'host_id': 'str',
        'host_name': 'str',
        'backup_name': 'str',
        'process': 'int',
        'status': 'str',
        'started_at': 'str',
        'ended_at': 'str',
        'error_info': 'ErrorInfo'
    }

    attribute_map = {
        'host_id': 'host_id',
        'host_name': 'host_name',
        'backup_name': 'backup_name',
        'process': 'process',
        'status': 'status',
        'started_at': 'started_at',
        'ended_at': 'ended_at',
        'error_info': 'error_info'
    }

    def __init__(self, host_id=None, host_name=None, backup_name=None, process=None, status=None, started_at=None, ended_at=None, error_info=None):
        r"""OperationLogInfo

        The model defined in huaweicloud sdk

        :param host_id: 主机ID
        :type host_id: str
        :param host_name: 主机名称
        :type host_name: str
        :param backup_name: 备份名称
        :type backup_name: str
        :param process: 恢复进度（百分比）
        :type process: int
        :param status: 恢复状态，包含如下：   - success : 成功   - skipped : 跳过   - failed : 失败   - running : 正在运行   - timeout : 超时   - waiting : 等待
        :type status: str
        :param started_at: 任务开始时间
        :type started_at: str
        :param ended_at: 任务结束时间
        :type ended_at: str
        :param error_info: 
        :type error_info: :class:`huaweicloudsdkhss.v5.ErrorInfo`
        """
        
        

        self._host_id = None
        self._host_name = None
        self._backup_name = None
        self._process = None
        self._status = None
        self._started_at = None
        self._ended_at = None
        self._error_info = None
        self.discriminator = None

        if host_id is not None:
            self.host_id = host_id
        if host_name is not None:
            self.host_name = host_name
        if backup_name is not None:
            self.backup_name = backup_name
        if process is not None:
            self.process = process
        if status is not None:
            self.status = status
        if started_at is not None:
            self.started_at = started_at
        if ended_at is not None:
            self.ended_at = ended_at
        if error_info is not None:
            self.error_info = error_info

    @property
    def host_id(self):
        r"""Gets the host_id of this OperationLogInfo.

        主机ID

        :return: The host_id of this OperationLogInfo.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this OperationLogInfo.

        主机ID

        :param host_id: The host_id of this OperationLogInfo.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def host_name(self):
        r"""Gets the host_name of this OperationLogInfo.

        主机名称

        :return: The host_name of this OperationLogInfo.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this OperationLogInfo.

        主机名称

        :param host_name: The host_name of this OperationLogInfo.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def backup_name(self):
        r"""Gets the backup_name of this OperationLogInfo.

        备份名称

        :return: The backup_name of this OperationLogInfo.
        :rtype: str
        """
        return self._backup_name

    @backup_name.setter
    def backup_name(self, backup_name):
        r"""Sets the backup_name of this OperationLogInfo.

        备份名称

        :param backup_name: The backup_name of this OperationLogInfo.
        :type backup_name: str
        """
        self._backup_name = backup_name

    @property
    def process(self):
        r"""Gets the process of this OperationLogInfo.

        恢复进度（百分比）

        :return: The process of this OperationLogInfo.
        :rtype: int
        """
        return self._process

    @process.setter
    def process(self, process):
        r"""Sets the process of this OperationLogInfo.

        恢复进度（百分比）

        :param process: The process of this OperationLogInfo.
        :type process: int
        """
        self._process = process

    @property
    def status(self):
        r"""Gets the status of this OperationLogInfo.

        恢复状态，包含如下：   - success : 成功   - skipped : 跳过   - failed : 失败   - running : 正在运行   - timeout : 超时   - waiting : 等待

        :return: The status of this OperationLogInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this OperationLogInfo.

        恢复状态，包含如下：   - success : 成功   - skipped : 跳过   - failed : 失败   - running : 正在运行   - timeout : 超时   - waiting : 等待

        :param status: The status of this OperationLogInfo.
        :type status: str
        """
        self._status = status

    @property
    def started_at(self):
        r"""Gets the started_at of this OperationLogInfo.

        任务开始时间

        :return: The started_at of this OperationLogInfo.
        :rtype: str
        """
        return self._started_at

    @started_at.setter
    def started_at(self, started_at):
        r"""Sets the started_at of this OperationLogInfo.

        任务开始时间

        :param started_at: The started_at of this OperationLogInfo.
        :type started_at: str
        """
        self._started_at = started_at

    @property
    def ended_at(self):
        r"""Gets the ended_at of this OperationLogInfo.

        任务结束时间

        :return: The ended_at of this OperationLogInfo.
        :rtype: str
        """
        return self._ended_at

    @ended_at.setter
    def ended_at(self, ended_at):
        r"""Sets the ended_at of this OperationLogInfo.

        任务结束时间

        :param ended_at: The ended_at of this OperationLogInfo.
        :type ended_at: str
        """
        self._ended_at = ended_at

    @property
    def error_info(self):
        r"""Gets the error_info of this OperationLogInfo.

        :return: The error_info of this OperationLogInfo.
        :rtype: :class:`huaweicloudsdkhss.v5.ErrorInfo`
        """
        return self._error_info

    @error_info.setter
    def error_info(self, error_info):
        r"""Sets the error_info of this OperationLogInfo.

        :param error_info: The error_info of this OperationLogInfo.
        :type error_info: :class:`huaweicloudsdkhss.v5.ErrorInfo`
        """
        self._error_info = error_info

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
        if not isinstance(other, OperationLogInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
