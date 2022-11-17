# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExtractTask:

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
        'create_time': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'error_code': 'str',
        'description': 'str',
        'user_data': 'str',
        'input': 'ObsObjInfo',
        'output': 'ObsObjInfo',
        'metadata': 'MetaData'
    }

    attribute_map = {
        'task_id': 'task_id',
        'status': 'status',
        'create_time': 'create_time',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'error_code': 'error_code',
        'description': 'description',
        'user_data': 'user_data',
        'input': 'input',
        'output': 'output',
        'metadata': 'metadata'
    }

    def __init__(self, task_id=None, status=None, create_time=None, start_time=None, end_time=None, error_code=None, description=None, user_data=None, input=None, output=None, metadata=None):
        """ExtractTask

        The model defined in huaweicloud sdk

        :param task_id: 任务ID 
        :type task_id: str
        :param status: 任务状态。  取值如下： - INIT：初始状态。 - WAITING：等待启动。 - PROCESSING：处理中。 - SUCCEED：处理成功。 - FAILED：处理失败。 - CANCELED：已取消。 
        :type status: str
        :param create_time: 任务创建时间 
        :type create_time: str
        :param start_time: 任务启动时间 
        :type start_time: str
        :param end_time: 任务结束时间 
        :type end_time: str
        :param error_code: 任务的返回码。 
        :type error_code: str
        :param description: 错误描述 
        :type description: str
        :param user_data: 用户数据。 
        :type user_data: str
        :param input: 
        :type input: :class:`huaweicloudsdkmpc.v1.ObsObjInfo`
        :param output: 
        :type output: :class:`huaweicloudsdkmpc.v1.ObsObjInfo`
        :param metadata: 
        :type metadata: :class:`huaweicloudsdkmpc.v1.MetaData`
        """
        
        

        self._task_id = None
        self._status = None
        self._create_time = None
        self._start_time = None
        self._end_time = None
        self._error_code = None
        self._description = None
        self._user_data = None
        self._input = None
        self._output = None
        self._metadata = None
        self.discriminator = None

        if task_id is not None:
            self.task_id = task_id
        if status is not None:
            self.status = status
        if create_time is not None:
            self.create_time = create_time
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if error_code is not None:
            self.error_code = error_code
        if description is not None:
            self.description = description
        if user_data is not None:
            self.user_data = user_data
        if input is not None:
            self.input = input
        if output is not None:
            self.output = output
        if metadata is not None:
            self.metadata = metadata

    @property
    def task_id(self):
        """Gets the task_id of this ExtractTask.

        任务ID 

        :return: The task_id of this ExtractTask.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this ExtractTask.

        任务ID 

        :param task_id: The task_id of this ExtractTask.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def status(self):
        """Gets the status of this ExtractTask.

        任务状态。  取值如下： - INIT：初始状态。 - WAITING：等待启动。 - PROCESSING：处理中。 - SUCCEED：处理成功。 - FAILED：处理失败。 - CANCELED：已取消。 

        :return: The status of this ExtractTask.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ExtractTask.

        任务状态。  取值如下： - INIT：初始状态。 - WAITING：等待启动。 - PROCESSING：处理中。 - SUCCEED：处理成功。 - FAILED：处理失败。 - CANCELED：已取消。 

        :param status: The status of this ExtractTask.
        :type status: str
        """
        self._status = status

    @property
    def create_time(self):
        """Gets the create_time of this ExtractTask.

        任务创建时间 

        :return: The create_time of this ExtractTask.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ExtractTask.

        任务创建时间 

        :param create_time: The create_time of this ExtractTask.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def start_time(self):
        """Gets the start_time of this ExtractTask.

        任务启动时间 

        :return: The start_time of this ExtractTask.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ExtractTask.

        任务启动时间 

        :param start_time: The start_time of this ExtractTask.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ExtractTask.

        任务结束时间 

        :return: The end_time of this ExtractTask.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ExtractTask.

        任务结束时间 

        :param end_time: The end_time of this ExtractTask.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def error_code(self):
        """Gets the error_code of this ExtractTask.

        任务的返回码。 

        :return: The error_code of this ExtractTask.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this ExtractTask.

        任务的返回码。 

        :param error_code: The error_code of this ExtractTask.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def description(self):
        """Gets the description of this ExtractTask.

        错误描述 

        :return: The description of this ExtractTask.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ExtractTask.

        错误描述 

        :param description: The description of this ExtractTask.
        :type description: str
        """
        self._description = description

    @property
    def user_data(self):
        """Gets the user_data of this ExtractTask.

        用户数据。 

        :return: The user_data of this ExtractTask.
        :rtype: str
        """
        return self._user_data

    @user_data.setter
    def user_data(self, user_data):
        """Sets the user_data of this ExtractTask.

        用户数据。 

        :param user_data: The user_data of this ExtractTask.
        :type user_data: str
        """
        self._user_data = user_data

    @property
    def input(self):
        """Gets the input of this ExtractTask.

        :return: The input of this ExtractTask.
        :rtype: :class:`huaweicloudsdkmpc.v1.ObsObjInfo`
        """
        return self._input

    @input.setter
    def input(self, input):
        """Sets the input of this ExtractTask.

        :param input: The input of this ExtractTask.
        :type input: :class:`huaweicloudsdkmpc.v1.ObsObjInfo`
        """
        self._input = input

    @property
    def output(self):
        """Gets the output of this ExtractTask.

        :return: The output of this ExtractTask.
        :rtype: :class:`huaweicloudsdkmpc.v1.ObsObjInfo`
        """
        return self._output

    @output.setter
    def output(self, output):
        """Sets the output of this ExtractTask.

        :param output: The output of this ExtractTask.
        :type output: :class:`huaweicloudsdkmpc.v1.ObsObjInfo`
        """
        self._output = output

    @property
    def metadata(self):
        """Gets the metadata of this ExtractTask.

        :return: The metadata of this ExtractTask.
        :rtype: :class:`huaweicloudsdkmpc.v1.MetaData`
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this ExtractTask.

        :param metadata: The metadata of this ExtractTask.
        :type metadata: :class:`huaweicloudsdkmpc.v1.MetaData`
        """
        self._metadata = metadata

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
        if not isinstance(other, ExtractTask):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
