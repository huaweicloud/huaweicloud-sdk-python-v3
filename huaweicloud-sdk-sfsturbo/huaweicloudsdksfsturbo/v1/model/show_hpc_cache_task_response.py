# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowHpcCacheTaskResponse(SdkResponse):

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
        'type': 'str',
        'status': 'str',
        'src_target': 'str',
        'src_prefix': 'str',
        'dest_target': 'str',
        'dest_prefix': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'message': 'str',
        'x_request_id': 'str'
    }

    attribute_map = {
        'task_id': 'task_id',
        'type': 'type',
        'status': 'status',
        'src_target': 'src_target',
        'src_prefix': 'src_prefix',
        'dest_target': 'dest_target',
        'dest_prefix': 'dest_prefix',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'message': 'message',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, task_id=None, type=None, status=None, src_target=None, src_prefix=None, dest_target=None, dest_prefix=None, start_time=None, end_time=None, message=None, x_request_id=None):
        """ShowHpcCacheTaskResponse

        The model defined in huaweicloud sdk

        :param task_id: 任务id
        :type task_id: str
        :param type: 任务类型
        :type type: str
        :param status: 任务状态
        :type status: str
        :param src_target: 源端对象
        :type src_target: str
        :param src_prefix: 源端路径
        :type src_prefix: str
        :param dest_target: 目的端对象
        :type dest_target: str
        :param dest_prefix: 目的端路径
        :type dest_prefix: str
        :param start_time: 任务开始时间
        :type start_time: str
        :param end_time: 任务结束时间
        :type end_time: str
        :param message: 任务执行结果信息
        :type message: str
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ShowHpcCacheTaskResponse, self).__init__()

        self._task_id = None
        self._type = None
        self._status = None
        self._src_target = None
        self._src_prefix = None
        self._dest_target = None
        self._dest_prefix = None
        self._start_time = None
        self._end_time = None
        self._message = None
        self._x_request_id = None
        self.discriminator = None

        if task_id is not None:
            self.task_id = task_id
        if type is not None:
            self.type = type
        if status is not None:
            self.status = status
        if src_target is not None:
            self.src_target = src_target
        if src_prefix is not None:
            self.src_prefix = src_prefix
        if dest_target is not None:
            self.dest_target = dest_target
        if dest_prefix is not None:
            self.dest_prefix = dest_prefix
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if message is not None:
            self.message = message
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def task_id(self):
        """Gets the task_id of this ShowHpcCacheTaskResponse.

        任务id

        :return: The task_id of this ShowHpcCacheTaskResponse.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this ShowHpcCacheTaskResponse.

        任务id

        :param task_id: The task_id of this ShowHpcCacheTaskResponse.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def type(self):
        """Gets the type of this ShowHpcCacheTaskResponse.

        任务类型

        :return: The type of this ShowHpcCacheTaskResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ShowHpcCacheTaskResponse.

        任务类型

        :param type: The type of this ShowHpcCacheTaskResponse.
        :type type: str
        """
        self._type = type

    @property
    def status(self):
        """Gets the status of this ShowHpcCacheTaskResponse.

        任务状态

        :return: The status of this ShowHpcCacheTaskResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowHpcCacheTaskResponse.

        任务状态

        :param status: The status of this ShowHpcCacheTaskResponse.
        :type status: str
        """
        self._status = status

    @property
    def src_target(self):
        """Gets the src_target of this ShowHpcCacheTaskResponse.

        源端对象

        :return: The src_target of this ShowHpcCacheTaskResponse.
        :rtype: str
        """
        return self._src_target

    @src_target.setter
    def src_target(self, src_target):
        """Sets the src_target of this ShowHpcCacheTaskResponse.

        源端对象

        :param src_target: The src_target of this ShowHpcCacheTaskResponse.
        :type src_target: str
        """
        self._src_target = src_target

    @property
    def src_prefix(self):
        """Gets the src_prefix of this ShowHpcCacheTaskResponse.

        源端路径

        :return: The src_prefix of this ShowHpcCacheTaskResponse.
        :rtype: str
        """
        return self._src_prefix

    @src_prefix.setter
    def src_prefix(self, src_prefix):
        """Sets the src_prefix of this ShowHpcCacheTaskResponse.

        源端路径

        :param src_prefix: The src_prefix of this ShowHpcCacheTaskResponse.
        :type src_prefix: str
        """
        self._src_prefix = src_prefix

    @property
    def dest_target(self):
        """Gets the dest_target of this ShowHpcCacheTaskResponse.

        目的端对象

        :return: The dest_target of this ShowHpcCacheTaskResponse.
        :rtype: str
        """
        return self._dest_target

    @dest_target.setter
    def dest_target(self, dest_target):
        """Sets the dest_target of this ShowHpcCacheTaskResponse.

        目的端对象

        :param dest_target: The dest_target of this ShowHpcCacheTaskResponse.
        :type dest_target: str
        """
        self._dest_target = dest_target

    @property
    def dest_prefix(self):
        """Gets the dest_prefix of this ShowHpcCacheTaskResponse.

        目的端路径

        :return: The dest_prefix of this ShowHpcCacheTaskResponse.
        :rtype: str
        """
        return self._dest_prefix

    @dest_prefix.setter
    def dest_prefix(self, dest_prefix):
        """Sets the dest_prefix of this ShowHpcCacheTaskResponse.

        目的端路径

        :param dest_prefix: The dest_prefix of this ShowHpcCacheTaskResponse.
        :type dest_prefix: str
        """
        self._dest_prefix = dest_prefix

    @property
    def start_time(self):
        """Gets the start_time of this ShowHpcCacheTaskResponse.

        任务开始时间

        :return: The start_time of this ShowHpcCacheTaskResponse.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ShowHpcCacheTaskResponse.

        任务开始时间

        :param start_time: The start_time of this ShowHpcCacheTaskResponse.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ShowHpcCacheTaskResponse.

        任务结束时间

        :return: The end_time of this ShowHpcCacheTaskResponse.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ShowHpcCacheTaskResponse.

        任务结束时间

        :param end_time: The end_time of this ShowHpcCacheTaskResponse.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def message(self):
        """Gets the message of this ShowHpcCacheTaskResponse.

        任务执行结果信息

        :return: The message of this ShowHpcCacheTaskResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ShowHpcCacheTaskResponse.

        任务执行结果信息

        :param message: The message of this ShowHpcCacheTaskResponse.
        :type message: str
        """
        self._message = message

    @property
    def x_request_id(self):
        """Gets the x_request_id of this ShowHpcCacheTaskResponse.

        :return: The x_request_id of this ShowHpcCacheTaskResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this ShowHpcCacheTaskResponse.

        :param x_request_id: The x_request_id of this ShowHpcCacheTaskResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, ShowHpcCacheTaskResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
