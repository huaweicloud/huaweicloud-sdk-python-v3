# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskDetailInfo:

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
        'input': 'ObsObjInfo',
        'output': 'ObsObjInfo',
        'user_data': 'str',
        'error_code': 'str',
        'description': 'str',
        'media_detail': 'MediaDetail',
        'xcode_error': 'ErrorResponse'
    }

    attribute_map = {
        'task_id': 'task_id',
        'status': 'status',
        'create_time': 'create_time',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'input': 'input',
        'output': 'output',
        'user_data': 'user_data',
        'error_code': 'error_code',
        'description': 'description',
        'media_detail': 'media_detail',
        'xcode_error': 'xcode_error'
    }

    def __init__(self, task_id=None, status=None, create_time=None, start_time=None, end_time=None, input=None, output=None, user_data=None, error_code=None, description=None, media_detail=None, xcode_error=None):
        """TaskDetailInfo

        The model defined in huaweicloud sdk

        :param task_id: 任务ID。
        :type task_id: str
        :param status: 任务执行状态，取值如下。 
        :type status: str
        :param create_time: 转码任务启动时间 
        :type create_time: str
        :param start_time: 下发xcode任务成功时间 
        :type start_time: str
        :param end_time: 转码任务结束时间 
        :type end_time: str
        :param input: 
        :type input: :class:`huaweicloudsdkmpc.v1.ObsObjInfo`
        :param output: 
        :type output: :class:`huaweicloudsdkmpc.v1.ObsObjInfo`
        :param user_data: 用户数据。 
        :type user_data: str
        :param error_code: 转码任务错误码。 
        :type error_code: str
        :param description: 转码任务描述，当转码出现异常时，此字段为异常的原因。 
        :type description: str
        :param media_detail: 
        :type media_detail: :class:`huaweicloudsdkmpc.v1.MediaDetail`
        :param xcode_error: 
        :type xcode_error: :class:`huaweicloudsdkmpc.v1.ErrorResponse`
        """
        
        

        self._task_id = None
        self._status = None
        self._create_time = None
        self._start_time = None
        self._end_time = None
        self._input = None
        self._output = None
        self._user_data = None
        self._error_code = None
        self._description = None
        self._media_detail = None
        self._xcode_error = None
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
        if input is not None:
            self.input = input
        if output is not None:
            self.output = output
        if user_data is not None:
            self.user_data = user_data
        if error_code is not None:
            self.error_code = error_code
        if description is not None:
            self.description = description
        if media_detail is not None:
            self.media_detail = media_detail
        if xcode_error is not None:
            self.xcode_error = xcode_error

    @property
    def task_id(self):
        """Gets the task_id of this TaskDetailInfo.

        任务ID。

        :return: The task_id of this TaskDetailInfo.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this TaskDetailInfo.

        任务ID。

        :param task_id: The task_id of this TaskDetailInfo.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def status(self):
        """Gets the status of this TaskDetailInfo.

        任务执行状态，取值如下。 

        :return: The status of this TaskDetailInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TaskDetailInfo.

        任务执行状态，取值如下。 

        :param status: The status of this TaskDetailInfo.
        :type status: str
        """
        self._status = status

    @property
    def create_time(self):
        """Gets the create_time of this TaskDetailInfo.

        转码任务启动时间 

        :return: The create_time of this TaskDetailInfo.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this TaskDetailInfo.

        转码任务启动时间 

        :param create_time: The create_time of this TaskDetailInfo.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def start_time(self):
        """Gets the start_time of this TaskDetailInfo.

        下发xcode任务成功时间 

        :return: The start_time of this TaskDetailInfo.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this TaskDetailInfo.

        下发xcode任务成功时间 

        :param start_time: The start_time of this TaskDetailInfo.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this TaskDetailInfo.

        转码任务结束时间 

        :return: The end_time of this TaskDetailInfo.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this TaskDetailInfo.

        转码任务结束时间 

        :param end_time: The end_time of this TaskDetailInfo.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def input(self):
        """Gets the input of this TaskDetailInfo.

        :return: The input of this TaskDetailInfo.
        :rtype: :class:`huaweicloudsdkmpc.v1.ObsObjInfo`
        """
        return self._input

    @input.setter
    def input(self, input):
        """Sets the input of this TaskDetailInfo.

        :param input: The input of this TaskDetailInfo.
        :type input: :class:`huaweicloudsdkmpc.v1.ObsObjInfo`
        """
        self._input = input

    @property
    def output(self):
        """Gets the output of this TaskDetailInfo.

        :return: The output of this TaskDetailInfo.
        :rtype: :class:`huaweicloudsdkmpc.v1.ObsObjInfo`
        """
        return self._output

    @output.setter
    def output(self, output):
        """Sets the output of this TaskDetailInfo.

        :param output: The output of this TaskDetailInfo.
        :type output: :class:`huaweicloudsdkmpc.v1.ObsObjInfo`
        """
        self._output = output

    @property
    def user_data(self):
        """Gets the user_data of this TaskDetailInfo.

        用户数据。 

        :return: The user_data of this TaskDetailInfo.
        :rtype: str
        """
        return self._user_data

    @user_data.setter
    def user_data(self, user_data):
        """Sets the user_data of this TaskDetailInfo.

        用户数据。 

        :param user_data: The user_data of this TaskDetailInfo.
        :type user_data: str
        """
        self._user_data = user_data

    @property
    def error_code(self):
        """Gets the error_code of this TaskDetailInfo.

        转码任务错误码。 

        :return: The error_code of this TaskDetailInfo.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this TaskDetailInfo.

        转码任务错误码。 

        :param error_code: The error_code of this TaskDetailInfo.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def description(self):
        """Gets the description of this TaskDetailInfo.

        转码任务描述，当转码出现异常时，此字段为异常的原因。 

        :return: The description of this TaskDetailInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TaskDetailInfo.

        转码任务描述，当转码出现异常时，此字段为异常的原因。 

        :param description: The description of this TaskDetailInfo.
        :type description: str
        """
        self._description = description

    @property
    def media_detail(self):
        """Gets the media_detail of this TaskDetailInfo.

        :return: The media_detail of this TaskDetailInfo.
        :rtype: :class:`huaweicloudsdkmpc.v1.MediaDetail`
        """
        return self._media_detail

    @media_detail.setter
    def media_detail(self, media_detail):
        """Sets the media_detail of this TaskDetailInfo.

        :param media_detail: The media_detail of this TaskDetailInfo.
        :type media_detail: :class:`huaweicloudsdkmpc.v1.MediaDetail`
        """
        self._media_detail = media_detail

    @property
    def xcode_error(self):
        """Gets the xcode_error of this TaskDetailInfo.

        :return: The xcode_error of this TaskDetailInfo.
        :rtype: :class:`huaweicloudsdkmpc.v1.ErrorResponse`
        """
        return self._xcode_error

    @xcode_error.setter
    def xcode_error(self, xcode_error):
        """Sets the xcode_error of this TaskDetailInfo.

        :param xcode_error: The xcode_error of this TaskDetailInfo.
        :type xcode_error: :class:`huaweicloudsdkmpc.v1.ErrorResponse`
        """
        self._xcode_error = xcode_error

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
        if not isinstance(other, TaskDetailInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
