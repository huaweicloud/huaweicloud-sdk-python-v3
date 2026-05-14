# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EditingTaskInfo:

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
        'asset_id': 'str',
        'status': 'str',
        'progress': 'int',
        'create_time': 'str',
        'end_time': 'str'
    }

    attribute_map = {
        'task_id': 'task_id',
        'asset_id': 'asset_id',
        'status': 'status',
        'progress': 'progress',
        'create_time': 'create_time',
        'end_time': 'end_time'
    }

    def __init__(self, task_id=None, asset_id=None, status=None, progress=None, create_time=None, end_time=None):
        r"""EditingTaskInfo

        The model defined in huaweicloud sdk

        :param task_id: 编辑任务ID 
        :type task_id: str
        :param asset_id: 输出的媒资ID 
        :type asset_id: str
        :param status: 任务状态 - WAITING 等待中 - PROCESSING 处理中； - SUCCEED 成功； - FAILED 失败； - CANCEL 已取消； 
        :type status: str
        :param progress: 进度，取值0-100 
        :type progress: int
        :param create_time: 任务创建时间，格式按照RFC3339，UTC时间，如2020-09-01T18:50:20Z 
        :type create_time: str
        :param end_time: 任务结束时间，格式按照RFC3339，UTC时间，如2020-09-01T18:50:20Z，当任务结束时才有值 
        :type end_time: str
        """
        
        

        self._task_id = None
        self._asset_id = None
        self._status = None
        self._progress = None
        self._create_time = None
        self._end_time = None
        self.discriminator = None

        if task_id is not None:
            self.task_id = task_id
        if asset_id is not None:
            self.asset_id = asset_id
        if status is not None:
            self.status = status
        if progress is not None:
            self.progress = progress
        if create_time is not None:
            self.create_time = create_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def task_id(self):
        r"""Gets the task_id of this EditingTaskInfo.

        编辑任务ID 

        :return: The task_id of this EditingTaskInfo.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this EditingTaskInfo.

        编辑任务ID 

        :param task_id: The task_id of this EditingTaskInfo.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def asset_id(self):
        r"""Gets the asset_id of this EditingTaskInfo.

        输出的媒资ID 

        :return: The asset_id of this EditingTaskInfo.
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        r"""Sets the asset_id of this EditingTaskInfo.

        输出的媒资ID 

        :param asset_id: The asset_id of this EditingTaskInfo.
        :type asset_id: str
        """
        self._asset_id = asset_id

    @property
    def status(self):
        r"""Gets the status of this EditingTaskInfo.

        任务状态 - WAITING 等待中 - PROCESSING 处理中； - SUCCEED 成功； - FAILED 失败； - CANCEL 已取消； 

        :return: The status of this EditingTaskInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this EditingTaskInfo.

        任务状态 - WAITING 等待中 - PROCESSING 处理中； - SUCCEED 成功； - FAILED 失败； - CANCEL 已取消； 

        :param status: The status of this EditingTaskInfo.
        :type status: str
        """
        self._status = status

    @property
    def progress(self):
        r"""Gets the progress of this EditingTaskInfo.

        进度，取值0-100 

        :return: The progress of this EditingTaskInfo.
        :rtype: int
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        r"""Sets the progress of this EditingTaskInfo.

        进度，取值0-100 

        :param progress: The progress of this EditingTaskInfo.
        :type progress: int
        """
        self._progress = progress

    @property
    def create_time(self):
        r"""Gets the create_time of this EditingTaskInfo.

        任务创建时间，格式按照RFC3339，UTC时间，如2020-09-01T18:50:20Z 

        :return: The create_time of this EditingTaskInfo.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this EditingTaskInfo.

        任务创建时间，格式按照RFC3339，UTC时间，如2020-09-01T18:50:20Z 

        :param create_time: The create_time of this EditingTaskInfo.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def end_time(self):
        r"""Gets the end_time of this EditingTaskInfo.

        任务结束时间，格式按照RFC3339，UTC时间，如2020-09-01T18:50:20Z，当任务结束时才有值 

        :return: The end_time of this EditingTaskInfo.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this EditingTaskInfo.

        任务结束时间，格式按照RFC3339，UTC时间，如2020-09-01T18:50:20Z，当任务结束时才有值 

        :param end_time: The end_time of this EditingTaskInfo.
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
        if not isinstance(other, EditingTaskInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
