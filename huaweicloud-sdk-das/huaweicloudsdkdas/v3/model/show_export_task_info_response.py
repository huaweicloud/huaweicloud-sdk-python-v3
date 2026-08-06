# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowExportTaskInfoResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'create_at': 'float',
        'download_url': 'str',
        'end_time': 'float',
        'export_line_num': 'float',
        'instance_id': 'str',
        'last_record_time': 'float',
        'start_time': 'float',
        'task_id': 'float',
        'task_status': 'int'
    }

    attribute_map = {
        'create_at': 'create_at',
        'download_url': 'download_url',
        'end_time': 'end_time',
        'export_line_num': 'export_line_num',
        'instance_id': 'instance_id',
        'last_record_time': 'last_record_time',
        'start_time': 'start_time',
        'task_id': 'task_id',
        'task_status': 'task_status'
    }

    def __init__(self, create_at=None, download_url=None, end_time=None, export_line_num=None, instance_id=None, last_record_time=None, start_time=None, task_id=None, task_status=None):
        r"""ShowExportTaskInfoResponse

        The model defined in huaweicloud sdk

        :param create_at: 创建时间
        :type create_at: float
        :param download_url: 下载链接
        :type download_url: str
        :param end_time: 结束时间
        :type end_time: float
        :param export_line_num: 导出条数
        :type export_line_num: float
        :param instance_id: 实例ID
        :type instance_id: str
        :param last_record_time: 最新SQL执行时间
        :type last_record_time: float
        :param start_time: 开始时间
        :type start_time: float
        :param task_id: 任务ID
        :type task_id: float
        :param task_status: 任务状态
        :type task_status: int
        """
        
        super().__init__()

        self._create_at = None
        self._download_url = None
        self._end_time = None
        self._export_line_num = None
        self._instance_id = None
        self._last_record_time = None
        self._start_time = None
        self._task_id = None
        self._task_status = None
        self.discriminator = None

        if create_at is not None:
            self.create_at = create_at
        if download_url is not None:
            self.download_url = download_url
        if end_time is not None:
            self.end_time = end_time
        if export_line_num is not None:
            self.export_line_num = export_line_num
        if instance_id is not None:
            self.instance_id = instance_id
        if last_record_time is not None:
            self.last_record_time = last_record_time
        if start_time is not None:
            self.start_time = start_time
        if task_id is not None:
            self.task_id = task_id
        if task_status is not None:
            self.task_status = task_status

    @property
    def create_at(self):
        r"""Gets the create_at of this ShowExportTaskInfoResponse.

        创建时间

        :return: The create_at of this ShowExportTaskInfoResponse.
        :rtype: float
        """
        return self._create_at

    @create_at.setter
    def create_at(self, create_at):
        r"""Sets the create_at of this ShowExportTaskInfoResponse.

        创建时间

        :param create_at: The create_at of this ShowExportTaskInfoResponse.
        :type create_at: float
        """
        self._create_at = create_at

    @property
    def download_url(self):
        r"""Gets the download_url of this ShowExportTaskInfoResponse.

        下载链接

        :return: The download_url of this ShowExportTaskInfoResponse.
        :rtype: str
        """
        return self._download_url

    @download_url.setter
    def download_url(self, download_url):
        r"""Sets the download_url of this ShowExportTaskInfoResponse.

        下载链接

        :param download_url: The download_url of this ShowExportTaskInfoResponse.
        :type download_url: str
        """
        self._download_url = download_url

    @property
    def end_time(self):
        r"""Gets the end_time of this ShowExportTaskInfoResponse.

        结束时间

        :return: The end_time of this ShowExportTaskInfoResponse.
        :rtype: float
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ShowExportTaskInfoResponse.

        结束时间

        :param end_time: The end_time of this ShowExportTaskInfoResponse.
        :type end_time: float
        """
        self._end_time = end_time

    @property
    def export_line_num(self):
        r"""Gets the export_line_num of this ShowExportTaskInfoResponse.

        导出条数

        :return: The export_line_num of this ShowExportTaskInfoResponse.
        :rtype: float
        """
        return self._export_line_num

    @export_line_num.setter
    def export_line_num(self, export_line_num):
        r"""Sets the export_line_num of this ShowExportTaskInfoResponse.

        导出条数

        :param export_line_num: The export_line_num of this ShowExportTaskInfoResponse.
        :type export_line_num: float
        """
        self._export_line_num = export_line_num

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ShowExportTaskInfoResponse.

        实例ID

        :return: The instance_id of this ShowExportTaskInfoResponse.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ShowExportTaskInfoResponse.

        实例ID

        :param instance_id: The instance_id of this ShowExportTaskInfoResponse.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def last_record_time(self):
        r"""Gets the last_record_time of this ShowExportTaskInfoResponse.

        最新SQL执行时间

        :return: The last_record_time of this ShowExportTaskInfoResponse.
        :rtype: float
        """
        return self._last_record_time

    @last_record_time.setter
    def last_record_time(self, last_record_time):
        r"""Sets the last_record_time of this ShowExportTaskInfoResponse.

        最新SQL执行时间

        :param last_record_time: The last_record_time of this ShowExportTaskInfoResponse.
        :type last_record_time: float
        """
        self._last_record_time = last_record_time

    @property
    def start_time(self):
        r"""Gets the start_time of this ShowExportTaskInfoResponse.

        开始时间

        :return: The start_time of this ShowExportTaskInfoResponse.
        :rtype: float
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ShowExportTaskInfoResponse.

        开始时间

        :param start_time: The start_time of this ShowExportTaskInfoResponse.
        :type start_time: float
        """
        self._start_time = start_time

    @property
    def task_id(self):
        r"""Gets the task_id of this ShowExportTaskInfoResponse.

        任务ID

        :return: The task_id of this ShowExportTaskInfoResponse.
        :rtype: float
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this ShowExportTaskInfoResponse.

        任务ID

        :param task_id: The task_id of this ShowExportTaskInfoResponse.
        :type task_id: float
        """
        self._task_id = task_id

    @property
    def task_status(self):
        r"""Gets the task_status of this ShowExportTaskInfoResponse.

        任务状态

        :return: The task_status of this ShowExportTaskInfoResponse.
        :rtype: int
        """
        return self._task_status

    @task_status.setter
    def task_status(self, task_status):
        r"""Sets the task_status of this ShowExportTaskInfoResponse.

        任务状态

        :param task_status: The task_status of this ShowExportTaskInfoResponse.
        :type task_status: int
        """
        self._task_status = task_status

    def to_dict(self):
        import warnings
        warnings.warn("ShowExportTaskInfoResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ShowExportTaskInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
