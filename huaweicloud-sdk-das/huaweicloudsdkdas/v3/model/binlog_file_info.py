# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BinlogFileInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'file_name': 'str',
        'backup_id': 'str',
        'file_size': 'int',
        'task_info': 'BinlogParseTaskInfo',
        'begin_time': 'str',
        'end_time': 'str'
    }

    attribute_map = {
        'file_name': 'file_name',
        'backup_id': 'backup_id',
        'file_size': 'file_size',
        'task_info': 'task_info',
        'begin_time': 'begin_time',
        'end_time': 'end_time'
    }

    def __init__(self, file_name=None, backup_id=None, file_size=None, task_info=None, begin_time=None, end_time=None):
        r"""BinlogFileInfo

        The model defined in huaweicloud sdk

        :param file_name: 文件名称
        :type file_name: str
        :param backup_id: 备份ID
        :type backup_id: str
        :param file_size: 文件大小
        :type file_size: int
        :param task_info: 
        :type task_info: :class:`huaweicloudsdkdas.v3.BinlogParseTaskInfo`
        :param begin_time: binlog备份开始时间
        :type begin_time: str
        :param end_time: binlog备份结束时间
        :type end_time: str
        """
        
        

        self._file_name = None
        self._backup_id = None
        self._file_size = None
        self._task_info = None
        self._begin_time = None
        self._end_time = None
        self.discriminator = None

        if file_name is not None:
            self.file_name = file_name
        if backup_id is not None:
            self.backup_id = backup_id
        if file_size is not None:
            self.file_size = file_size
        if task_info is not None:
            self.task_info = task_info
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def file_name(self):
        r"""Gets the file_name of this BinlogFileInfo.

        文件名称

        :return: The file_name of this BinlogFileInfo.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        r"""Sets the file_name of this BinlogFileInfo.

        文件名称

        :param file_name: The file_name of this BinlogFileInfo.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def backup_id(self):
        r"""Gets the backup_id of this BinlogFileInfo.

        备份ID

        :return: The backup_id of this BinlogFileInfo.
        :rtype: str
        """
        return self._backup_id

    @backup_id.setter
    def backup_id(self, backup_id):
        r"""Sets the backup_id of this BinlogFileInfo.

        备份ID

        :param backup_id: The backup_id of this BinlogFileInfo.
        :type backup_id: str
        """
        self._backup_id = backup_id

    @property
    def file_size(self):
        r"""Gets the file_size of this BinlogFileInfo.

        文件大小

        :return: The file_size of this BinlogFileInfo.
        :rtype: int
        """
        return self._file_size

    @file_size.setter
    def file_size(self, file_size):
        r"""Sets the file_size of this BinlogFileInfo.

        文件大小

        :param file_size: The file_size of this BinlogFileInfo.
        :type file_size: int
        """
        self._file_size = file_size

    @property
    def task_info(self):
        r"""Gets the task_info of this BinlogFileInfo.

        :return: The task_info of this BinlogFileInfo.
        :rtype: :class:`huaweicloudsdkdas.v3.BinlogParseTaskInfo`
        """
        return self._task_info

    @task_info.setter
    def task_info(self, task_info):
        r"""Sets the task_info of this BinlogFileInfo.

        :param task_info: The task_info of this BinlogFileInfo.
        :type task_info: :class:`huaweicloudsdkdas.v3.BinlogParseTaskInfo`
        """
        self._task_info = task_info

    @property
    def begin_time(self):
        r"""Gets the begin_time of this BinlogFileInfo.

        binlog备份开始时间

        :return: The begin_time of this BinlogFileInfo.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        r"""Sets the begin_time of this BinlogFileInfo.

        binlog备份开始时间

        :param begin_time: The begin_time of this BinlogFileInfo.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        r"""Gets the end_time of this BinlogFileInfo.

        binlog备份结束时间

        :return: The end_time of this BinlogFileInfo.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this BinlogFileInfo.

        binlog备份结束时间

        :param end_time: The end_time of this BinlogFileInfo.
        :type end_time: str
        """
        self._end_time = end_time

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BinlogFileInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
