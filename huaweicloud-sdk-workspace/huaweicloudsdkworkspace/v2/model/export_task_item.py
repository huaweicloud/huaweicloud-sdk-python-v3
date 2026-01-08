# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportTaskItem:

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
        'file_name': 'str',
        'status': 'str',
        'fail_reason': 'str',
        'error_code': 'str',
        'create_time': 'str',
        'end_time': 'str',
        'is_download': 'bool'
    }

    attribute_map = {
        'task_id': 'task_id',
        'file_name': 'file_name',
        'status': 'status',
        'fail_reason': 'fail_reason',
        'error_code': 'error_code',
        'create_time': 'create_time',
        'end_time': 'end_time',
        'is_download': 'is_download'
    }

    def __init__(self, task_id=None, file_name=None, status=None, fail_reason=None, error_code=None, create_time=None, end_time=None, is_download=None):
        r"""ExportTaskItem

        The model defined in huaweicloud sdk

        :param task_id: 导出任务id。
        :type task_id: str
        :param file_name: 导出文件名。
        :type file_name: str
        :param status: 导出任务的状态，取值为 CREATING, SUCCESS, FAIL, EXPIRED; CREATING为进行中，SUCCESS为成功，FAIL为失败，EXPIRED为过期。
        :type status: str
        :param fail_reason: 任务失败的原因。
        :type fail_reason: str
        :param error_code: 任务失败错误码。
        :type error_code: str
        :param create_time: 创建文件的时间, utc时间：yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ。
        :type create_time: str
        :param end_time: 创建文件的时间, utc时间：yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ。
        :type end_time: str
        :param is_download: 是否已下载。
        :type is_download: bool
        """
        
        

        self._task_id = None
        self._file_name = None
        self._status = None
        self._fail_reason = None
        self._error_code = None
        self._create_time = None
        self._end_time = None
        self._is_download = None
        self.discriminator = None

        if task_id is not None:
            self.task_id = task_id
        if file_name is not None:
            self.file_name = file_name
        if status is not None:
            self.status = status
        if fail_reason is not None:
            self.fail_reason = fail_reason
        if error_code is not None:
            self.error_code = error_code
        if create_time is not None:
            self.create_time = create_time
        if end_time is not None:
            self.end_time = end_time
        if is_download is not None:
            self.is_download = is_download

    @property
    def task_id(self):
        r"""Gets the task_id of this ExportTaskItem.

        导出任务id。

        :return: The task_id of this ExportTaskItem.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this ExportTaskItem.

        导出任务id。

        :param task_id: The task_id of this ExportTaskItem.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def file_name(self):
        r"""Gets the file_name of this ExportTaskItem.

        导出文件名。

        :return: The file_name of this ExportTaskItem.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        r"""Sets the file_name of this ExportTaskItem.

        导出文件名。

        :param file_name: The file_name of this ExportTaskItem.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def status(self):
        r"""Gets the status of this ExportTaskItem.

        导出任务的状态，取值为 CREATING, SUCCESS, FAIL, EXPIRED; CREATING为进行中，SUCCESS为成功，FAIL为失败，EXPIRED为过期。

        :return: The status of this ExportTaskItem.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ExportTaskItem.

        导出任务的状态，取值为 CREATING, SUCCESS, FAIL, EXPIRED; CREATING为进行中，SUCCESS为成功，FAIL为失败，EXPIRED为过期。

        :param status: The status of this ExportTaskItem.
        :type status: str
        """
        self._status = status

    @property
    def fail_reason(self):
        r"""Gets the fail_reason of this ExportTaskItem.

        任务失败的原因。

        :return: The fail_reason of this ExportTaskItem.
        :rtype: str
        """
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, fail_reason):
        r"""Sets the fail_reason of this ExportTaskItem.

        任务失败的原因。

        :param fail_reason: The fail_reason of this ExportTaskItem.
        :type fail_reason: str
        """
        self._fail_reason = fail_reason

    @property
    def error_code(self):
        r"""Gets the error_code of this ExportTaskItem.

        任务失败错误码。

        :return: The error_code of this ExportTaskItem.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this ExportTaskItem.

        任务失败错误码。

        :param error_code: The error_code of this ExportTaskItem.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def create_time(self):
        r"""Gets the create_time of this ExportTaskItem.

        创建文件的时间, utc时间：yyyy-MM-dd'T'HH:mm:ss.SSSZ。

        :return: The create_time of this ExportTaskItem.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ExportTaskItem.

        创建文件的时间, utc时间：yyyy-MM-dd'T'HH:mm:ss.SSSZ。

        :param create_time: The create_time of this ExportTaskItem.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ExportTaskItem.

        创建文件的时间, utc时间：yyyy-MM-dd'T'HH:mm:ss.SSSZ。

        :return: The end_time of this ExportTaskItem.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ExportTaskItem.

        创建文件的时间, utc时间：yyyy-MM-dd'T'HH:mm:ss.SSSZ。

        :param end_time: The end_time of this ExportTaskItem.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def is_download(self):
        r"""Gets the is_download of this ExportTaskItem.

        是否已下载。

        :return: The is_download of this ExportTaskItem.
        :rtype: bool
        """
        return self._is_download

    @is_download.setter
    def is_download(self, is_download):
        r"""Sets the is_download of this ExportTaskItem.

        是否已下载。

        :param is_download: The is_download of this ExportTaskItem.
        :type is_download: bool
        """
        self._is_download = is_download

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
        if not isinstance(other, ExportTaskItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
