# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTaskDetailResponse(SdkResponse):

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
        'task_type': 'str',
        'status': 'str',
        'error_code': 'str',
        'error_msg': 'str',
        'create_time': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'workflow_task': 'WorkflowTask',
        'edit_media_task': 'EditMediaTask',
        'session_context': 'str',
        'callback_url': 'str'
    }

    attribute_map = {
        'task_id': 'task_id',
        'task_type': 'task_type',
        'status': 'status',
        'error_code': 'error_code',
        'error_msg': 'error_msg',
        'create_time': 'create_time',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'workflow_task': 'workflow_task',
        'edit_media_task': 'edit_media_task',
        'session_context': 'session_context',
        'callback_url': 'callback_url'
    }

    def __init__(self, task_id=None, task_type=None, status=None, error_code=None, error_msg=None, create_time=None, start_time=None, end_time=None, workflow_task=None, edit_media_task=None, session_context=None, callback_url=None):
        r"""ShowTaskDetailResponse

        The model defined in huaweicloud sdk

        :param task_id: 任务Id
        :type task_id: str
        :param task_type: 任务类型
        :type task_type: str
        :param status: 任务状态，包含就绪，处理中，成功，失败，已取消
        :type status: str
        :param error_code: 错误码
        :type error_code: str
        :param error_msg: 错误信息
        :type error_msg: str
        :param create_time: 任务开始时间
        :type create_time: str
        :param start_time: 任务开始处理时间，多个任务则是第一个任务的开始时间
        :type start_time: str
        :param end_time: 任务处理结束时间，多个任务则是最后一个任务的结束时间
        :type end_time: str
        :param workflow_task: 
        :type workflow_task: :class:`huaweicloudsdkvod.v1.WorkflowTask`
        :param edit_media_task: 
        :type edit_media_task: :class:`huaweicloudsdkvod.v1.EditMediaTask`
        :param session_context: 用户自定义数据
        :type session_context: str
        :param callback_url: 客户回调地址
        :type callback_url: str
        """
        
        super(ShowTaskDetailResponse, self).__init__()

        self._task_id = None
        self._task_type = None
        self._status = None
        self._error_code = None
        self._error_msg = None
        self._create_time = None
        self._start_time = None
        self._end_time = None
        self._workflow_task = None
        self._edit_media_task = None
        self._session_context = None
        self._callback_url = None
        self.discriminator = None

        if task_id is not None:
            self.task_id = task_id
        if task_type is not None:
            self.task_type = task_type
        if status is not None:
            self.status = status
        if error_code is not None:
            self.error_code = error_code
        if error_msg is not None:
            self.error_msg = error_msg
        if create_time is not None:
            self.create_time = create_time
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if workflow_task is not None:
            self.workflow_task = workflow_task
        if edit_media_task is not None:
            self.edit_media_task = edit_media_task
        if session_context is not None:
            self.session_context = session_context
        if callback_url is not None:
            self.callback_url = callback_url

    @property
    def task_id(self):
        r"""Gets the task_id of this ShowTaskDetailResponse.

        任务Id

        :return: The task_id of this ShowTaskDetailResponse.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this ShowTaskDetailResponse.

        任务Id

        :param task_id: The task_id of this ShowTaskDetailResponse.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def task_type(self):
        r"""Gets the task_type of this ShowTaskDetailResponse.

        任务类型

        :return: The task_type of this ShowTaskDetailResponse.
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        r"""Sets the task_type of this ShowTaskDetailResponse.

        任务类型

        :param task_type: The task_type of this ShowTaskDetailResponse.
        :type task_type: str
        """
        self._task_type = task_type

    @property
    def status(self):
        r"""Gets the status of this ShowTaskDetailResponse.

        任务状态，包含就绪，处理中，成功，失败，已取消

        :return: The status of this ShowTaskDetailResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowTaskDetailResponse.

        任务状态，包含就绪，处理中，成功，失败，已取消

        :param status: The status of this ShowTaskDetailResponse.
        :type status: str
        """
        self._status = status

    @property
    def error_code(self):
        r"""Gets the error_code of this ShowTaskDetailResponse.

        错误码

        :return: The error_code of this ShowTaskDetailResponse.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this ShowTaskDetailResponse.

        错误码

        :param error_code: The error_code of this ShowTaskDetailResponse.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_msg(self):
        r"""Gets the error_msg of this ShowTaskDetailResponse.

        错误信息

        :return: The error_msg of this ShowTaskDetailResponse.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        r"""Sets the error_msg of this ShowTaskDetailResponse.

        错误信息

        :param error_msg: The error_msg of this ShowTaskDetailResponse.
        :type error_msg: str
        """
        self._error_msg = error_msg

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowTaskDetailResponse.

        任务开始时间

        :return: The create_time of this ShowTaskDetailResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowTaskDetailResponse.

        任务开始时间

        :param create_time: The create_time of this ShowTaskDetailResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def start_time(self):
        r"""Gets the start_time of this ShowTaskDetailResponse.

        任务开始处理时间，多个任务则是第一个任务的开始时间

        :return: The start_time of this ShowTaskDetailResponse.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ShowTaskDetailResponse.

        任务开始处理时间，多个任务则是第一个任务的开始时间

        :param start_time: The start_time of this ShowTaskDetailResponse.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ShowTaskDetailResponse.

        任务处理结束时间，多个任务则是最后一个任务的结束时间

        :return: The end_time of this ShowTaskDetailResponse.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ShowTaskDetailResponse.

        任务处理结束时间，多个任务则是最后一个任务的结束时间

        :param end_time: The end_time of this ShowTaskDetailResponse.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def workflow_task(self):
        r"""Gets the workflow_task of this ShowTaskDetailResponse.

        :return: The workflow_task of this ShowTaskDetailResponse.
        :rtype: :class:`huaweicloudsdkvod.v1.WorkflowTask`
        """
        return self._workflow_task

    @workflow_task.setter
    def workflow_task(self, workflow_task):
        r"""Sets the workflow_task of this ShowTaskDetailResponse.

        :param workflow_task: The workflow_task of this ShowTaskDetailResponse.
        :type workflow_task: :class:`huaweicloudsdkvod.v1.WorkflowTask`
        """
        self._workflow_task = workflow_task

    @property
    def edit_media_task(self):
        r"""Gets the edit_media_task of this ShowTaskDetailResponse.

        :return: The edit_media_task of this ShowTaskDetailResponse.
        :rtype: :class:`huaweicloudsdkvod.v1.EditMediaTask`
        """
        return self._edit_media_task

    @edit_media_task.setter
    def edit_media_task(self, edit_media_task):
        r"""Sets the edit_media_task of this ShowTaskDetailResponse.

        :param edit_media_task: The edit_media_task of this ShowTaskDetailResponse.
        :type edit_media_task: :class:`huaweicloudsdkvod.v1.EditMediaTask`
        """
        self._edit_media_task = edit_media_task

    @property
    def session_context(self):
        r"""Gets the session_context of this ShowTaskDetailResponse.

        用户自定义数据

        :return: The session_context of this ShowTaskDetailResponse.
        :rtype: str
        """
        return self._session_context

    @session_context.setter
    def session_context(self, session_context):
        r"""Sets the session_context of this ShowTaskDetailResponse.

        用户自定义数据

        :param session_context: The session_context of this ShowTaskDetailResponse.
        :type session_context: str
        """
        self._session_context = session_context

    @property
    def callback_url(self):
        r"""Gets the callback_url of this ShowTaskDetailResponse.

        客户回调地址

        :return: The callback_url of this ShowTaskDetailResponse.
        :rtype: str
        """
        return self._callback_url

    @callback_url.setter
    def callback_url(self, callback_url):
        r"""Sets the callback_url of this ShowTaskDetailResponse.

        客户回调地址

        :param callback_url: The callback_url of this ShowTaskDetailResponse.
        :type callback_url: str
        """
        self._callback_url = callback_url

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
        if not isinstance(other, ShowTaskDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
