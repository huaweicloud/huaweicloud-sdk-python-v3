# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IndexUsageExportTaskInfo:

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
        'download_url': 'str'
    }

    attribute_map = {
        'task_id': 'task_id',
        'instance_id': 'instance_id',
        'task_status': 'task_status',
        'create_at': 'create_at',
        'download_url': 'download_url'
    }

    def __init__(self, task_id=None, instance_id=None, task_status=None, create_at=None, download_url=None):
        r"""IndexUsageExportTaskInfo

        The model defined in huaweicloud sdk

        :param task_id: 任务ID
        :type task_id: int
        :param instance_id: 实例ID
        :type instance_id: str
        :param task_status: 任务状态
        :type task_status: int
        :param create_at: 创建时间
        :type create_at: int
        :param download_url: 下载地址
        :type download_url: str
        """
        
        

        self._task_id = None
        self._instance_id = None
        self._task_status = None
        self._create_at = None
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
        if download_url is not None:
            self.download_url = download_url

    @property
    def task_id(self):
        r"""Gets the task_id of this IndexUsageExportTaskInfo.

        任务ID

        :return: The task_id of this IndexUsageExportTaskInfo.
        :rtype: int
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this IndexUsageExportTaskInfo.

        任务ID

        :param task_id: The task_id of this IndexUsageExportTaskInfo.
        :type task_id: int
        """
        self._task_id = task_id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this IndexUsageExportTaskInfo.

        实例ID

        :return: The instance_id of this IndexUsageExportTaskInfo.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this IndexUsageExportTaskInfo.

        实例ID

        :param instance_id: The instance_id of this IndexUsageExportTaskInfo.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def task_status(self):
        r"""Gets the task_status of this IndexUsageExportTaskInfo.

        任务状态

        :return: The task_status of this IndexUsageExportTaskInfo.
        :rtype: int
        """
        return self._task_status

    @task_status.setter
    def task_status(self, task_status):
        r"""Sets the task_status of this IndexUsageExportTaskInfo.

        任务状态

        :param task_status: The task_status of this IndexUsageExportTaskInfo.
        :type task_status: int
        """
        self._task_status = task_status

    @property
    def create_at(self):
        r"""Gets the create_at of this IndexUsageExportTaskInfo.

        创建时间

        :return: The create_at of this IndexUsageExportTaskInfo.
        :rtype: int
        """
        return self._create_at

    @create_at.setter
    def create_at(self, create_at):
        r"""Sets the create_at of this IndexUsageExportTaskInfo.

        创建时间

        :param create_at: The create_at of this IndexUsageExportTaskInfo.
        :type create_at: int
        """
        self._create_at = create_at

    @property
    def download_url(self):
        r"""Gets the download_url of this IndexUsageExportTaskInfo.

        下载地址

        :return: The download_url of this IndexUsageExportTaskInfo.
        :rtype: str
        """
        return self._download_url

    @download_url.setter
    def download_url(self, download_url):
        r"""Sets the download_url of this IndexUsageExportTaskInfo.

        下载地址

        :param download_url: The download_url of this IndexUsageExportTaskInfo.
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
        if not isinstance(other, IndexUsageExportTaskInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
