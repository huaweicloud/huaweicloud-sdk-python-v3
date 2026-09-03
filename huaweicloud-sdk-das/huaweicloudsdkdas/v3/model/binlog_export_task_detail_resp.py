# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BinlogExportTaskDetailResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_id': 'int',
        'instance_id': 'str',
        'task_status': 'int',
        'start_time': 'int',
        'end_time': 'int',
        'last_record_time': 'int',
        'create_at': 'int',
        'export_line_num': 'int',
        'download_url': 'str',
        'source_file_name': 'str',
        'parse_task_id': 'int'
    }

    attribute_map = {
        'task_id': 'task_id',
        'instance_id': 'instance_id',
        'task_status': 'task_status',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'last_record_time': 'last_record_time',
        'create_at': 'create_at',
        'export_line_num': 'export_line_num',
        'download_url': 'download_url',
        'source_file_name': 'source_file_name',
        'parse_task_id': 'parse_task_id'
    }

    def __init__(self, task_id=None, instance_id=None, task_status=None, start_time=None, end_time=None, last_record_time=None, create_at=None, export_line_num=None, download_url=None, source_file_name=None, parse_task_id=None):
        r"""BinlogExportTaskDetailResp

        The model defined in huaweicloud sdk

        :param task_id: 任务ID
        :type task_id: int
        :param instance_id: 实例ID
        :type instance_id: str
        :param task_status: 任务状态。取值范围：0（初始化）、1（运行中）、2（部分成功）、3（成功）、4（失败）、-1（已删除）
        :type task_status: int
        :param start_time: 开始时间
        :type start_time: int
        :param end_time: 结束时间
        :type end_time: int
        :param last_record_time: 最后记录时间
        :type last_record_time: int
        :param create_at: 任务创建时间
        :type create_at: int
        :param export_line_num: 导出行数
        :type export_line_num: int
        :param download_url: 文件下载地址
        :type download_url: str
        :param source_file_name: binlog源文件名
        :type source_file_name: str
        :param parse_task_id: 解析任务ID
        :type parse_task_id: int
        """
        
        

        self._task_id = None
        self._instance_id = None
        self._task_status = None
        self._start_time = None
        self._end_time = None
        self._last_record_time = None
        self._create_at = None
        self._export_line_num = None
        self._download_url = None
        self._source_file_name = None
        self._parse_task_id = None
        self.discriminator = None

        if task_id is not None:
            self.task_id = task_id
        if instance_id is not None:
            self.instance_id = instance_id
        if task_status is not None:
            self.task_status = task_status
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if last_record_time is not None:
            self.last_record_time = last_record_time
        if create_at is not None:
            self.create_at = create_at
        if export_line_num is not None:
            self.export_line_num = export_line_num
        if download_url is not None:
            self.download_url = download_url
        if source_file_name is not None:
            self.source_file_name = source_file_name
        if parse_task_id is not None:
            self.parse_task_id = parse_task_id

    @property
    def task_id(self):
        r"""Gets the task_id of this BinlogExportTaskDetailResp.

        任务ID

        :return: The task_id of this BinlogExportTaskDetailResp.
        :rtype: int
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this BinlogExportTaskDetailResp.

        任务ID

        :param task_id: The task_id of this BinlogExportTaskDetailResp.
        :type task_id: int
        """
        self._task_id = task_id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this BinlogExportTaskDetailResp.

        实例ID

        :return: The instance_id of this BinlogExportTaskDetailResp.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this BinlogExportTaskDetailResp.

        实例ID

        :param instance_id: The instance_id of this BinlogExportTaskDetailResp.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def task_status(self):
        r"""Gets the task_status of this BinlogExportTaskDetailResp.

        任务状态。取值范围：0（初始化）、1（运行中）、2（部分成功）、3（成功）、4（失败）、-1（已删除）

        :return: The task_status of this BinlogExportTaskDetailResp.
        :rtype: int
        """
        return self._task_status

    @task_status.setter
    def task_status(self, task_status):
        r"""Sets the task_status of this BinlogExportTaskDetailResp.

        任务状态。取值范围：0（初始化）、1（运行中）、2（部分成功）、3（成功）、4（失败）、-1（已删除）

        :param task_status: The task_status of this BinlogExportTaskDetailResp.
        :type task_status: int
        """
        self._task_status = task_status

    @property
    def start_time(self):
        r"""Gets the start_time of this BinlogExportTaskDetailResp.

        开始时间

        :return: The start_time of this BinlogExportTaskDetailResp.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this BinlogExportTaskDetailResp.

        开始时间

        :param start_time: The start_time of this BinlogExportTaskDetailResp.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this BinlogExportTaskDetailResp.

        结束时间

        :return: The end_time of this BinlogExportTaskDetailResp.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this BinlogExportTaskDetailResp.

        结束时间

        :param end_time: The end_time of this BinlogExportTaskDetailResp.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def last_record_time(self):
        r"""Gets the last_record_time of this BinlogExportTaskDetailResp.

        最后记录时间

        :return: The last_record_time of this BinlogExportTaskDetailResp.
        :rtype: int
        """
        return self._last_record_time

    @last_record_time.setter
    def last_record_time(self, last_record_time):
        r"""Sets the last_record_time of this BinlogExportTaskDetailResp.

        最后记录时间

        :param last_record_time: The last_record_time of this BinlogExportTaskDetailResp.
        :type last_record_time: int
        """
        self._last_record_time = last_record_time

    @property
    def create_at(self):
        r"""Gets the create_at of this BinlogExportTaskDetailResp.

        任务创建时间

        :return: The create_at of this BinlogExportTaskDetailResp.
        :rtype: int
        """
        return self._create_at

    @create_at.setter
    def create_at(self, create_at):
        r"""Sets the create_at of this BinlogExportTaskDetailResp.

        任务创建时间

        :param create_at: The create_at of this BinlogExportTaskDetailResp.
        :type create_at: int
        """
        self._create_at = create_at

    @property
    def export_line_num(self):
        r"""Gets the export_line_num of this BinlogExportTaskDetailResp.

        导出行数

        :return: The export_line_num of this BinlogExportTaskDetailResp.
        :rtype: int
        """
        return self._export_line_num

    @export_line_num.setter
    def export_line_num(self, export_line_num):
        r"""Sets the export_line_num of this BinlogExportTaskDetailResp.

        导出行数

        :param export_line_num: The export_line_num of this BinlogExportTaskDetailResp.
        :type export_line_num: int
        """
        self._export_line_num = export_line_num

    @property
    def download_url(self):
        r"""Gets the download_url of this BinlogExportTaskDetailResp.

        文件下载地址

        :return: The download_url of this BinlogExportTaskDetailResp.
        :rtype: str
        """
        return self._download_url

    @download_url.setter
    def download_url(self, download_url):
        r"""Sets the download_url of this BinlogExportTaskDetailResp.

        文件下载地址

        :param download_url: The download_url of this BinlogExportTaskDetailResp.
        :type download_url: str
        """
        self._download_url = download_url

    @property
    def source_file_name(self):
        r"""Gets the source_file_name of this BinlogExportTaskDetailResp.

        binlog源文件名

        :return: The source_file_name of this BinlogExportTaskDetailResp.
        :rtype: str
        """
        return self._source_file_name

    @source_file_name.setter
    def source_file_name(self, source_file_name):
        r"""Sets the source_file_name of this BinlogExportTaskDetailResp.

        binlog源文件名

        :param source_file_name: The source_file_name of this BinlogExportTaskDetailResp.
        :type source_file_name: str
        """
        self._source_file_name = source_file_name

    @property
    def parse_task_id(self):
        r"""Gets the parse_task_id of this BinlogExportTaskDetailResp.

        解析任务ID

        :return: The parse_task_id of this BinlogExportTaskDetailResp.
        :rtype: int
        """
        return self._parse_task_id

    @parse_task_id.setter
    def parse_task_id(self, parse_task_id):
        r"""Sets the parse_task_id of this BinlogExportTaskDetailResp.

        解析任务ID

        :param parse_task_id: The parse_task_id of this BinlogExportTaskDetailResp.
        :type parse_task_id: int
        """
        self._parse_task_id = parse_task_id

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
        if not isinstance(other, BinlogExportTaskDetailResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
