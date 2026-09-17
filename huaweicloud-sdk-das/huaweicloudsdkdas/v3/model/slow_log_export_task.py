# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SlowLogExportTask:

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
        'create_at': 'int',
        'start_time': 'int',
        'end_time': 'int',
        'download_url': 'str'
    }

    attribute_map = {
        'task_id': 'task_id',
        'instance_id': 'instance_id',
        'task_status': 'task_status',
        'create_at': 'create_at',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'download_url': 'download_url'
    }

    def __init__(self, task_id=None, instance_id=None, task_status=None, create_at=None, start_time=None, end_time=None, download_url=None):
        r"""SlowLogExportTask

        The model defined in huaweicloud sdk

        :param task_id: 任务ID
        :type task_id: int
        :param instance_id: 实例ID
        :type instance_id: str
        :param task_status: 任务状态
        :type task_status: int
        :param create_at: 任务创建时间（Unix timestamp），单位：毫秒
        :type create_at: int
        :param start_time: 任务开始时间（Unix timestamp），单位：毫秒
        :type start_time: int
        :param end_time: 任务结束时间（Unix timestamp），单位：毫秒
        :type end_time: int
        :param download_url: 下载地址
        :type download_url: str
        """
        
        

        self._task_id = None
        self._instance_id = None
        self._task_status = None
        self._create_at = None
        self._start_time = None
        self._end_time = None
        self._download_url = None
        self.discriminator = None

        if task_id is not None:
            self.task_id = task_id
        if instance_id is not None:
            self.instance_id = instance_id
        if task_status is not None:
            self.task_status = task_status
        if create_at is not None:
            self.create_at = create_at
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if download_url is not None:
            self.download_url = download_url

    @property
    def task_id(self):
        r"""Gets the task_id of this SlowLogExportTask.

        任务ID

        :return: The task_id of this SlowLogExportTask.
        :rtype: int
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this SlowLogExportTask.

        任务ID

        :param task_id: The task_id of this SlowLogExportTask.
        :type task_id: int
        """
        self._task_id = task_id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this SlowLogExportTask.

        实例ID

        :return: The instance_id of this SlowLogExportTask.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this SlowLogExportTask.

        实例ID

        :param instance_id: The instance_id of this SlowLogExportTask.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def task_status(self):
        r"""Gets the task_status of this SlowLogExportTask.

        任务状态

        :return: The task_status of this SlowLogExportTask.
        :rtype: int
        """
        return self._task_status

    @task_status.setter
    def task_status(self, task_status):
        r"""Sets the task_status of this SlowLogExportTask.

        任务状态

        :param task_status: The task_status of this SlowLogExportTask.
        :type task_status: int
        """
        self._task_status = task_status

    @property
    def create_at(self):
        r"""Gets the create_at of this SlowLogExportTask.

        任务创建时间（Unix timestamp），单位：毫秒

        :return: The create_at of this SlowLogExportTask.
        :rtype: int
        """
        return self._create_at

    @create_at.setter
    def create_at(self, create_at):
        r"""Sets the create_at of this SlowLogExportTask.

        任务创建时间（Unix timestamp），单位：毫秒

        :param create_at: The create_at of this SlowLogExportTask.
        :type create_at: int
        """
        self._create_at = create_at

    @property
    def start_time(self):
        r"""Gets the start_time of this SlowLogExportTask.

        任务开始时间（Unix timestamp），单位：毫秒

        :return: The start_time of this SlowLogExportTask.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this SlowLogExportTask.

        任务开始时间（Unix timestamp），单位：毫秒

        :param start_time: The start_time of this SlowLogExportTask.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this SlowLogExportTask.

        任务结束时间（Unix timestamp），单位：毫秒

        :return: The end_time of this SlowLogExportTask.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this SlowLogExportTask.

        任务结束时间（Unix timestamp），单位：毫秒

        :param end_time: The end_time of this SlowLogExportTask.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def download_url(self):
        r"""Gets the download_url of this SlowLogExportTask.

        下载地址

        :return: The download_url of this SlowLogExportTask.
        :rtype: str
        """
        return self._download_url

    @download_url.setter
    def download_url(self, download_url):
        r"""Sets the download_url of this SlowLogExportTask.

        下载地址

        :param download_url: The download_url of this SlowLogExportTask.
        :type download_url: str
        """
        self._download_url = download_url

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
        if not isinstance(other, SlowLogExportTask):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
