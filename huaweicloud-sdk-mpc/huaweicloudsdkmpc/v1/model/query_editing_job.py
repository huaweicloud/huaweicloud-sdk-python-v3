# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryEditingJob:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_id': 'str',
        'status': 'str',
        'error_code': 'str',
        'exec_description': 'str',
        'description': 'str',
        'progress': 'int',
        'create_time': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'user_data': 'str',
        'output': 'ObsObjInfo',
        'editing_output': 'EditingOutputFileInfo'
    }

    attribute_map = {
        'job_id': 'job_id',
        'status': 'status',
        'error_code': 'error_code',
        'exec_description': 'exec_description',
        'description': 'description',
        'progress': 'progress',
        'create_time': 'create_time',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'user_data': 'user_data',
        'output': 'output',
        'editing_output': 'editing_output'
    }

    def __init__(self, job_id=None, status=None, error_code=None, exec_description=None, description=None, progress=None, create_time=None, start_time=None, end_time=None, user_data=None, output=None, editing_output=None):
        """QueryEditingJob

        The model defined in huaweicloud sdk

        :param job_id: 任务ID 
        :type job_id: str
        :param status: 任务执行状态，取值如下。WAITING：等待启动 PROCESSING：处理中 SUCCEEDED：处理成功。FAILED：处理失败。 
        :type status: str
        :param error_code: 任务的返回码。 
        :type error_code: str
        :param exec_description: 处理信息。 
        :type exec_description: str
        :param description: 处理信息。 
        :type description: str
        :param progress: 任务执行进度百分比, 取值范围：[0, 100]。 
        :type progress: int
        :param create_time: 剪切拼接任务创建时间 格式 yyyyMMddHHmmss 必须是与时区无关的UTC时间 
        :type create_time: str
        :param start_time: 剪切拼接任务开始时间 格式 yyyyMMddHHmmss 必须是与时区无关的UTC时间 
        :type start_time: str
        :param end_time: 剪切拼接任务结束时间 格式 yyyyMMddHHmmss 必须是与时区无关的UTC时间 
        :type end_time: str
        :param user_data: 用户自定义数据
        :type user_data: str
        :param output: 
        :type output: :class:`huaweicloudsdkmpc.v1.ObsObjInfo`
        :param editing_output: 
        :type editing_output: :class:`huaweicloudsdkmpc.v1.EditingOutputFileInfo`
        """
        
        

        self._job_id = None
        self._status = None
        self._error_code = None
        self._exec_description = None
        self._description = None
        self._progress = None
        self._create_time = None
        self._start_time = None
        self._end_time = None
        self._user_data = None
        self._output = None
        self._editing_output = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if status is not None:
            self.status = status
        if error_code is not None:
            self.error_code = error_code
        if exec_description is not None:
            self.exec_description = exec_description
        if description is not None:
            self.description = description
        if progress is not None:
            self.progress = progress
        if create_time is not None:
            self.create_time = create_time
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if user_data is not None:
            self.user_data = user_data
        if output is not None:
            self.output = output
        if editing_output is not None:
            self.editing_output = editing_output

    @property
    def job_id(self):
        """Gets the job_id of this QueryEditingJob.

        任务ID 

        :return: The job_id of this QueryEditingJob.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this QueryEditingJob.

        任务ID 

        :param job_id: The job_id of this QueryEditingJob.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def status(self):
        """Gets the status of this QueryEditingJob.

        任务执行状态，取值如下。WAITING：等待启动 PROCESSING：处理中 SUCCEEDED：处理成功。FAILED：处理失败。 

        :return: The status of this QueryEditingJob.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this QueryEditingJob.

        任务执行状态，取值如下。WAITING：等待启动 PROCESSING：处理中 SUCCEEDED：处理成功。FAILED：处理失败。 

        :param status: The status of this QueryEditingJob.
        :type status: str
        """
        self._status = status

    @property
    def error_code(self):
        """Gets the error_code of this QueryEditingJob.

        任务的返回码。 

        :return: The error_code of this QueryEditingJob.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this QueryEditingJob.

        任务的返回码。 

        :param error_code: The error_code of this QueryEditingJob.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def exec_description(self):
        """Gets the exec_description of this QueryEditingJob.

        处理信息。 

        :return: The exec_description of this QueryEditingJob.
        :rtype: str
        """
        return self._exec_description

    @exec_description.setter
    def exec_description(self, exec_description):
        """Sets the exec_description of this QueryEditingJob.

        处理信息。 

        :param exec_description: The exec_description of this QueryEditingJob.
        :type exec_description: str
        """
        self._exec_description = exec_description

    @property
    def description(self):
        """Gets the description of this QueryEditingJob.

        处理信息。 

        :return: The description of this QueryEditingJob.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this QueryEditingJob.

        处理信息。 

        :param description: The description of this QueryEditingJob.
        :type description: str
        """
        self._description = description

    @property
    def progress(self):
        """Gets the progress of this QueryEditingJob.

        任务执行进度百分比, 取值范围：[0, 100]。 

        :return: The progress of this QueryEditingJob.
        :rtype: int
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this QueryEditingJob.

        任务执行进度百分比, 取值范围：[0, 100]。 

        :param progress: The progress of this QueryEditingJob.
        :type progress: int
        """
        self._progress = progress

    @property
    def create_time(self):
        """Gets the create_time of this QueryEditingJob.

        剪切拼接任务创建时间 格式 yyyyMMddHHmmss 必须是与时区无关的UTC时间 

        :return: The create_time of this QueryEditingJob.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this QueryEditingJob.

        剪切拼接任务创建时间 格式 yyyyMMddHHmmss 必须是与时区无关的UTC时间 

        :param create_time: The create_time of this QueryEditingJob.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def start_time(self):
        """Gets the start_time of this QueryEditingJob.

        剪切拼接任务开始时间 格式 yyyyMMddHHmmss 必须是与时区无关的UTC时间 

        :return: The start_time of this QueryEditingJob.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this QueryEditingJob.

        剪切拼接任务开始时间 格式 yyyyMMddHHmmss 必须是与时区无关的UTC时间 

        :param start_time: The start_time of this QueryEditingJob.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this QueryEditingJob.

        剪切拼接任务结束时间 格式 yyyyMMddHHmmss 必须是与时区无关的UTC时间 

        :return: The end_time of this QueryEditingJob.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this QueryEditingJob.

        剪切拼接任务结束时间 格式 yyyyMMddHHmmss 必须是与时区无关的UTC时间 

        :param end_time: The end_time of this QueryEditingJob.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def user_data(self):
        """Gets the user_data of this QueryEditingJob.

        用户自定义数据

        :return: The user_data of this QueryEditingJob.
        :rtype: str
        """
        return self._user_data

    @user_data.setter
    def user_data(self, user_data):
        """Sets the user_data of this QueryEditingJob.

        用户自定义数据

        :param user_data: The user_data of this QueryEditingJob.
        :type user_data: str
        """
        self._user_data = user_data

    @property
    def output(self):
        """Gets the output of this QueryEditingJob.

        :return: The output of this QueryEditingJob.
        :rtype: :class:`huaweicloudsdkmpc.v1.ObsObjInfo`
        """
        return self._output

    @output.setter
    def output(self, output):
        """Sets the output of this QueryEditingJob.

        :param output: The output of this QueryEditingJob.
        :type output: :class:`huaweicloudsdkmpc.v1.ObsObjInfo`
        """
        self._output = output

    @property
    def editing_output(self):
        """Gets the editing_output of this QueryEditingJob.

        :return: The editing_output of this QueryEditingJob.
        :rtype: :class:`huaweicloudsdkmpc.v1.EditingOutputFileInfo`
        """
        return self._editing_output

    @editing_output.setter
    def editing_output(self, editing_output):
        """Sets the editing_output of this QueryEditingJob.

        :param editing_output: The editing_output of this QueryEditingJob.
        :type editing_output: :class:`huaweicloudsdkmpc.v1.EditingOutputFileInfo`
        """
        self._editing_output = editing_output

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
        if not isinstance(other, QueryEditingJob):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
