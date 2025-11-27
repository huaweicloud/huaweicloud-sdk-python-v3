# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportTask:

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
        'task_name': 'str',
        'status': 'str',
        'download_link': 'str',
        'create_time': 'int',
        'update_time': 'int'
    }

    attribute_map = {
        'task_id': 'task_id',
        'task_name': 'task_name',
        'status': 'status',
        'download_link': 'download_link',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, task_id=None, task_name=None, status=None, download_link=None, create_time=None, update_time=None):
        r"""ExportTask

        The model defined in huaweicloud sdk

        :param task_id: 导出任务id
        :type task_id: str
        :param task_name: 导出任务名称
        :type task_name: str
        :param status: **参数解释：** 应用模板状态（域名粒度） **约束限制：** 不涉及 **取值范围：** - success: 应用模板成功 - fail: 应用模板失败 **默认取值：** 不涉及
        :type status: str
        :param download_link: 下载链接
        :type download_link: str
        :param create_time: 创建时间
        :type create_time: int
        :param update_time: 最近更新时间
        :type update_time: int
        """
        
        

        self._task_id = None
        self._task_name = None
        self._status = None
        self._download_link = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if task_id is not None:
            self.task_id = task_id
        if task_name is not None:
            self.task_name = task_name
        if status is not None:
            self.status = status
        if download_link is not None:
            self.download_link = download_link
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def task_id(self):
        r"""Gets the task_id of this ExportTask.

        导出任务id

        :return: The task_id of this ExportTask.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this ExportTask.

        导出任务id

        :param task_id: The task_id of this ExportTask.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def task_name(self):
        r"""Gets the task_name of this ExportTask.

        导出任务名称

        :return: The task_name of this ExportTask.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        r"""Sets the task_name of this ExportTask.

        导出任务名称

        :param task_name: The task_name of this ExportTask.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def status(self):
        r"""Gets the status of this ExportTask.

        **参数解释：** 应用模板状态（域名粒度） **约束限制：** 不涉及 **取值范围：** - success: 应用模板成功 - fail: 应用模板失败 **默认取值：** 不涉及

        :return: The status of this ExportTask.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ExportTask.

        **参数解释：** 应用模板状态（域名粒度） **约束限制：** 不涉及 **取值范围：** - success: 应用模板成功 - fail: 应用模板失败 **默认取值：** 不涉及

        :param status: The status of this ExportTask.
        :type status: str
        """
        self._status = status

    @property
    def download_link(self):
        r"""Gets the download_link of this ExportTask.

        下载链接

        :return: The download_link of this ExportTask.
        :rtype: str
        """
        return self._download_link

    @download_link.setter
    def download_link(self, download_link):
        r"""Sets the download_link of this ExportTask.

        下载链接

        :param download_link: The download_link of this ExportTask.
        :type download_link: str
        """
        self._download_link = download_link

    @property
    def create_time(self):
        r"""Gets the create_time of this ExportTask.

        创建时间

        :return: The create_time of this ExportTask.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ExportTask.

        创建时间

        :param create_time: The create_time of this ExportTask.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this ExportTask.

        最近更新时间

        :return: The update_time of this ExportTask.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ExportTask.

        最近更新时间

        :param update_time: The update_time of this ExportTask.
        :type update_time: int
        """
        self._update_time = update_time

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
        if not isinstance(other, ExportTask):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
