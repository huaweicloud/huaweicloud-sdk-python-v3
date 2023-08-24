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
        'status': 'str',
        'input_json': 'object',
        'input_url': 'str',
        'start_time': 'datetime',
        'end_time': 'datetime',
        'create_time': 'datetime',
        'output_json': 'object',
        'output_url': 'str'
    }

    attribute_map = {
        'task_id': 'task_id',
        'status': 'status',
        'input_json': 'input_json',
        'input_url': 'input_url',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'create_time': 'create_time',
        'output_json': 'output_json',
        'output_url': 'output_url'
    }

    def __init__(self, task_id=None, status=None, input_json=None, input_url=None, start_time=None, end_time=None, create_time=None, output_json=None, output_url=None):
        """ShowTaskResponse

        The model defined in huaweicloud sdk

        :param task_id: 任务编号
        :type task_id: str
        :param status: 任务运行状态，暂考虑取值仅为 Running/Failed/Successed
        :type status: str
        :param input_json: 如果提交任务使用了input_enable参数，并且创建任务使用的是json格式非文件方式，该值为输入的字符串; 对应数据结构参见创建任务时的结构体
        :type input_json: object
        :param input_url: 如果提交任务使用了input_enable参数，并且创建任务使用的是文件方式，该值为OBS对应的文件绝对路径
        :type input_url: str
        :param start_time: 开始时间（UTC）
        :type start_time: datetime
        :param end_time: 结束时间（UTC）
        :type end_time: datetime
        :param create_time: 创建时间（UTC）
        :type create_time: datetime
        :param output_json: 任务处理结果，json格式；每个子服务该对象结构不同，框架层不解析具体key，运行态直接拷贝算法服务返回信息、
        :type output_json: object
        :param output_url: 任务结果文件对应的绝对地址，具体值由租户OBS对应的待存储路径前缀和文件名组成，文件名服务端固定用task_id命名
        :type output_url: str
        """
        
        super(ShowTaskResponse, self).__init__()

        self._task_id = None
        self._status = None
        self._input_json = None
        self._input_url = None
        self._start_time = None
        self._end_time = None
        self._create_time = None
        self._output_json = None
        self._output_url = None
        self.discriminator = None

        if task_id is not None:
            self.task_id = task_id
        if status is not None:
            self.status = status
        if input_json is not None:
            self.input_json = input_json
        if input_url is not None:
            self.input_url = input_url
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if create_time is not None:
            self.create_time = create_time
        if output_json is not None:
            self.output_json = output_json
        if output_url is not None:
            self.output_url = output_url

    @property
    def task_id(self):
        """Gets the task_id of this ShowTaskResponse.

        任务编号

        :return: The task_id of this ShowTaskResponse.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this ShowTaskResponse.

        任务编号

        :param task_id: The task_id of this ShowTaskResponse.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def status(self):
        """Gets the status of this ShowTaskResponse.

        任务运行状态，暂考虑取值仅为 Running/Failed/Successed

        :return: The status of this ShowTaskResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowTaskResponse.

        任务运行状态，暂考虑取值仅为 Running/Failed/Successed

        :param status: The status of this ShowTaskResponse.
        :type status: str
        """
        self._status = status

    @property
    def input_json(self):
        """Gets the input_json of this ShowTaskResponse.

        如果提交任务使用了input_enable参数，并且创建任务使用的是json格式非文件方式，该值为输入的字符串; 对应数据结构参见创建任务时的结构体

        :return: The input_json of this ShowTaskResponse.
        :rtype: object
        """
        return self._input_json

    @input_json.setter
    def input_json(self, input_json):
        """Sets the input_json of this ShowTaskResponse.

        如果提交任务使用了input_enable参数，并且创建任务使用的是json格式非文件方式，该值为输入的字符串; 对应数据结构参见创建任务时的结构体

        :param input_json: The input_json of this ShowTaskResponse.
        :type input_json: object
        """
        self._input_json = input_json

    @property
    def input_url(self):
        """Gets the input_url of this ShowTaskResponse.

        如果提交任务使用了input_enable参数，并且创建任务使用的是文件方式，该值为OBS对应的文件绝对路径

        :return: The input_url of this ShowTaskResponse.
        :rtype: str
        """
        return self._input_url

    @input_url.setter
    def input_url(self, input_url):
        """Sets the input_url of this ShowTaskResponse.

        如果提交任务使用了input_enable参数，并且创建任务使用的是文件方式，该值为OBS对应的文件绝对路径

        :param input_url: The input_url of this ShowTaskResponse.
        :type input_url: str
        """
        self._input_url = input_url

    @property
    def start_time(self):
        """Gets the start_time of this ShowTaskResponse.

        开始时间（UTC）

        :return: The start_time of this ShowTaskResponse.
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ShowTaskResponse.

        开始时间（UTC）

        :param start_time: The start_time of this ShowTaskResponse.
        :type start_time: datetime
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ShowTaskResponse.

        结束时间（UTC）

        :return: The end_time of this ShowTaskResponse.
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ShowTaskResponse.

        结束时间（UTC）

        :param end_time: The end_time of this ShowTaskResponse.
        :type end_time: datetime
        """
        self._end_time = end_time

    @property
    def create_time(self):
        """Gets the create_time of this ShowTaskResponse.

        创建时间（UTC）

        :return: The create_time of this ShowTaskResponse.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ShowTaskResponse.

        创建时间（UTC）

        :param create_time: The create_time of this ShowTaskResponse.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def output_json(self):
        """Gets the output_json of this ShowTaskResponse.

        任务处理结果，json格式；每个子服务该对象结构不同，框架层不解析具体key，运行态直接拷贝算法服务返回信息、

        :return: The output_json of this ShowTaskResponse.
        :rtype: object
        """
        return self._output_json

    @output_json.setter
    def output_json(self, output_json):
        """Sets the output_json of this ShowTaskResponse.

        任务处理结果，json格式；每个子服务该对象结构不同，框架层不解析具体key，运行态直接拷贝算法服务返回信息、

        :param output_json: The output_json of this ShowTaskResponse.
        :type output_json: object
        """
        self._output_json = output_json

    @property
    def output_url(self):
        """Gets the output_url of this ShowTaskResponse.

        任务结果文件对应的绝对地址，具体值由租户OBS对应的待存储路径前缀和文件名组成，文件名服务端固定用task_id命名

        :return: The output_url of this ShowTaskResponse.
        :rtype: str
        """
        return self._output_url

    @output_url.setter
    def output_url(self, output_url):
        """Sets the output_url of this ShowTaskResponse.

        任务结果文件对应的绝对地址，具体值由租户OBS对应的待存储路径前缀和文件名组成，文件名服务端固定用task_id命名

        :param output_url: The output_url of this ShowTaskResponse.
        :type output_url: str
        """
        self._output_url = output_url

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
