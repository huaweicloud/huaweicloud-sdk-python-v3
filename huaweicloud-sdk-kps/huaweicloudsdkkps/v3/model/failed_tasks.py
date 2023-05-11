# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FailedTasks:

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
        'operate_type': 'str',
        'task_time': 'str',
        'task_error_code': 'str',
        'task_error_msg': 'str',
        'server_name': 'str',
        'server_id': 'str',
        'keypair_name': 'str'
    }

    attribute_map = {
        'task_id': 'task_id',
        'operate_type': 'operate_type',
        'task_time': 'task_time',
        'task_error_code': 'task_error_code',
        'task_error_msg': 'task_error_msg',
        'server_name': 'server_name',
        'server_id': 'server_id',
        'keypair_name': 'keypair_name'
    }

    def __init__(self, task_id=None, operate_type=None, task_time=None, task_error_code=None, task_error_msg=None, server_name=None, server_id=None, keypair_name=None):
        """FailedTasks

        The model defined in huaweicloud sdk

        :param task_id: 虚拟机ID
        :type task_id: str
        :param operate_type: 任务的操作类型。 - FAILED_RESET 重置 - FAILED_REPLACE 替换 - FAILED_UNBIND 解绑
        :type operate_type: str
        :param task_time: 任务时间
        :type task_time: str
        :param task_error_code: 任务失败错误码
        :type task_error_code: str
        :param task_error_msg: 任务失败错误码
        :type task_error_msg: str
        :param server_name: 虚拟机名称
        :type server_name: str
        :param server_id: 虚拟机ID
        :type server_id: str
        :param keypair_name: 密钥对名称
        :type keypair_name: str
        """
        
        

        self._task_id = None
        self._operate_type = None
        self._task_time = None
        self._task_error_code = None
        self._task_error_msg = None
        self._server_name = None
        self._server_id = None
        self._keypair_name = None
        self.discriminator = None

        if task_id is not None:
            self.task_id = task_id
        if operate_type is not None:
            self.operate_type = operate_type
        if task_time is not None:
            self.task_time = task_time
        if task_error_code is not None:
            self.task_error_code = task_error_code
        if task_error_msg is not None:
            self.task_error_msg = task_error_msg
        if server_name is not None:
            self.server_name = server_name
        if server_id is not None:
            self.server_id = server_id
        if keypair_name is not None:
            self.keypair_name = keypair_name

    @property
    def task_id(self):
        """Gets the task_id of this FailedTasks.

        虚拟机ID

        :return: The task_id of this FailedTasks.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this FailedTasks.

        虚拟机ID

        :param task_id: The task_id of this FailedTasks.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def operate_type(self):
        """Gets the operate_type of this FailedTasks.

        任务的操作类型。 - FAILED_RESET 重置 - FAILED_REPLACE 替换 - FAILED_UNBIND 解绑

        :return: The operate_type of this FailedTasks.
        :rtype: str
        """
        return self._operate_type

    @operate_type.setter
    def operate_type(self, operate_type):
        """Sets the operate_type of this FailedTasks.

        任务的操作类型。 - FAILED_RESET 重置 - FAILED_REPLACE 替换 - FAILED_UNBIND 解绑

        :param operate_type: The operate_type of this FailedTasks.
        :type operate_type: str
        """
        self._operate_type = operate_type

    @property
    def task_time(self):
        """Gets the task_time of this FailedTasks.

        任务时间

        :return: The task_time of this FailedTasks.
        :rtype: str
        """
        return self._task_time

    @task_time.setter
    def task_time(self, task_time):
        """Sets the task_time of this FailedTasks.

        任务时间

        :param task_time: The task_time of this FailedTasks.
        :type task_time: str
        """
        self._task_time = task_time

    @property
    def task_error_code(self):
        """Gets the task_error_code of this FailedTasks.

        任务失败错误码

        :return: The task_error_code of this FailedTasks.
        :rtype: str
        """
        return self._task_error_code

    @task_error_code.setter
    def task_error_code(self, task_error_code):
        """Sets the task_error_code of this FailedTasks.

        任务失败错误码

        :param task_error_code: The task_error_code of this FailedTasks.
        :type task_error_code: str
        """
        self._task_error_code = task_error_code

    @property
    def task_error_msg(self):
        """Gets the task_error_msg of this FailedTasks.

        任务失败错误码

        :return: The task_error_msg of this FailedTasks.
        :rtype: str
        """
        return self._task_error_msg

    @task_error_msg.setter
    def task_error_msg(self, task_error_msg):
        """Sets the task_error_msg of this FailedTasks.

        任务失败错误码

        :param task_error_msg: The task_error_msg of this FailedTasks.
        :type task_error_msg: str
        """
        self._task_error_msg = task_error_msg

    @property
    def server_name(self):
        """Gets the server_name of this FailedTasks.

        虚拟机名称

        :return: The server_name of this FailedTasks.
        :rtype: str
        """
        return self._server_name

    @server_name.setter
    def server_name(self, server_name):
        """Sets the server_name of this FailedTasks.

        虚拟机名称

        :param server_name: The server_name of this FailedTasks.
        :type server_name: str
        """
        self._server_name = server_name

    @property
    def server_id(self):
        """Gets the server_id of this FailedTasks.

        虚拟机ID

        :return: The server_id of this FailedTasks.
        :rtype: str
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        """Sets the server_id of this FailedTasks.

        虚拟机ID

        :param server_id: The server_id of this FailedTasks.
        :type server_id: str
        """
        self._server_id = server_id

    @property
    def keypair_name(self):
        """Gets the keypair_name of this FailedTasks.

        密钥对名称

        :return: The keypair_name of this FailedTasks.
        :rtype: str
        """
        return self._keypair_name

    @keypair_name.setter
    def keypair_name(self, keypair_name):
        """Sets the keypair_name of this FailedTasks.

        密钥对名称

        :param keypair_name: The keypair_name of this FailedTasks.
        :type keypair_name: str
        """
        self._keypair_name = keypair_name

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
        if not isinstance(other, FailedTasks):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
