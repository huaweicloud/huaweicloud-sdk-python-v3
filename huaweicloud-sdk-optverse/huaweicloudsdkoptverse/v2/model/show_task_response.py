# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTaskResponse(SdkResponse):

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
        'input_json': 'object',
        'status': 'str',
        'progress': 'object',
        'output_json': 'object',
        'start_time': 'datetime',
        'end_time': 'datetime',
        'create_time': 'datetime'
    }

    attribute_map = {
        'task_id': 'task_id',
        'input_json': 'input_json',
        'status': 'status',
        'progress': 'progress',
        'output_json': 'output_json',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'create_time': 'create_time'
    }

    def __init__(self, task_id=None, input_json=None, status=None, progress=None, output_json=None, start_time=None, end_time=None, create_time=None):
        r"""ShowTaskResponse

        The model defined in huaweicloud sdk

        :param task_id: 任务ID
        :type task_id: str
        :param input_json: 用户输入
        :type input_json: object
        :param status: 状态
        :type status: str
        :param progress: 任务进度
        :type progress: object
        :param output_json: 输出
        :type output_json: object
        :param start_time: 开始时间
        :type start_time: datetime
        :param end_time: 结束时间
        :type end_time: datetime
        :param create_time: 创建时间
        :type create_time: datetime
        """
        
        super(ShowTaskResponse, self).__init__()

        self._task_id = None
        self._input_json = None
        self._status = None
        self._progress = None
        self._output_json = None
        self._start_time = None
        self._end_time = None
        self._create_time = None
        self.discriminator = None

        if task_id is not None:
            self.task_id = task_id
        if input_json is not None:
            self.input_json = input_json
        if status is not None:
            self.status = status
        if progress is not None:
            self.progress = progress
        if output_json is not None:
            self.output_json = output_json
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if create_time is not None:
            self.create_time = create_time

    @property
    def task_id(self):
        r"""Gets the task_id of this ShowTaskResponse.

        任务ID

        :return: The task_id of this ShowTaskResponse.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this ShowTaskResponse.

        任务ID

        :param task_id: The task_id of this ShowTaskResponse.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def input_json(self):
        r"""Gets the input_json of this ShowTaskResponse.

        用户输入

        :return: The input_json of this ShowTaskResponse.
        :rtype: object
        """
        return self._input_json

    @input_json.setter
    def input_json(self, input_json):
        r"""Sets the input_json of this ShowTaskResponse.

        用户输入

        :param input_json: The input_json of this ShowTaskResponse.
        :type input_json: object
        """
        self._input_json = input_json

    @property
    def status(self):
        r"""Gets the status of this ShowTaskResponse.

        状态

        :return: The status of this ShowTaskResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowTaskResponse.

        状态

        :param status: The status of this ShowTaskResponse.
        :type status: str
        """
        self._status = status

    @property
    def progress(self):
        r"""Gets the progress of this ShowTaskResponse.

        任务进度

        :return: The progress of this ShowTaskResponse.
        :rtype: object
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        r"""Sets the progress of this ShowTaskResponse.

        任务进度

        :param progress: The progress of this ShowTaskResponse.
        :type progress: object
        """
        self._progress = progress

    @property
    def output_json(self):
        r"""Gets the output_json of this ShowTaskResponse.

        输出

        :return: The output_json of this ShowTaskResponse.
        :rtype: object
        """
        return self._output_json

    @output_json.setter
    def output_json(self, output_json):
        r"""Sets the output_json of this ShowTaskResponse.

        输出

        :param output_json: The output_json of this ShowTaskResponse.
        :type output_json: object
        """
        self._output_json = output_json

    @property
    def start_time(self):
        r"""Gets the start_time of this ShowTaskResponse.

        开始时间

        :return: The start_time of this ShowTaskResponse.
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ShowTaskResponse.

        开始时间

        :param start_time: The start_time of this ShowTaskResponse.
        :type start_time: datetime
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ShowTaskResponse.

        结束时间

        :return: The end_time of this ShowTaskResponse.
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ShowTaskResponse.

        结束时间

        :param end_time: The end_time of this ShowTaskResponse.
        :type end_time: datetime
        """
        self._end_time = end_time

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowTaskResponse.

        创建时间

        :return: The create_time of this ShowTaskResponse.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowTaskResponse.

        创建时间

        :param create_time: The create_time of this ShowTaskResponse.
        :type create_time: datetime
        """
        self._create_time = create_time

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
        if not isinstance(other, ShowTaskResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
