# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RunningTasks:

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
        'server_name': 'str',
        'server_id': 'str',
        'keypair_name': 'str'
    }

    attribute_map = {
        'task_id': 'task_id',
        'operate_type': 'operate_type',
        'task_time': 'task_time',
        'server_name': 'server_name',
        'server_id': 'server_id',
        'keypair_name': 'keypair_name'
    }

    def __init__(self, task_id=None, operate_type=None, task_time=None, server_name=None, server_id=None, keypair_name=None):
        r"""RunningTasks

        The model defined in huaweicloud sdk

        :param task_id: 虚拟机ID
        :type task_id: str
        :param operate_type: 操作类型。 - FAILED_RESET 重置 - FAILED_REPLACE 替换 - FAILED_UNBIND 解绑
        :type operate_type: str
        :param task_time: 任务时间
        :type task_time: str
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
        if server_name is not None:
            self.server_name = server_name
        if server_id is not None:
            self.server_id = server_id
        if keypair_name is not None:
            self.keypair_name = keypair_name

    @property
    def task_id(self):
        r"""Gets the task_id of this RunningTasks.

        虚拟机ID

        :return: The task_id of this RunningTasks.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this RunningTasks.

        虚拟机ID

        :param task_id: The task_id of this RunningTasks.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def operate_type(self):
        r"""Gets the operate_type of this RunningTasks.

        操作类型。 - FAILED_RESET 重置 - FAILED_REPLACE 替换 - FAILED_UNBIND 解绑

        :return: The operate_type of this RunningTasks.
        :rtype: str
        """
        return self._operate_type

    @operate_type.setter
    def operate_type(self, operate_type):
        r"""Sets the operate_type of this RunningTasks.

        操作类型。 - FAILED_RESET 重置 - FAILED_REPLACE 替换 - FAILED_UNBIND 解绑

        :param operate_type: The operate_type of this RunningTasks.
        :type operate_type: str
        """
        self._operate_type = operate_type

    @property
    def task_time(self):
        r"""Gets the task_time of this RunningTasks.

        任务时间

        :return: The task_time of this RunningTasks.
        :rtype: str
        """
        return self._task_time

    @task_time.setter
    def task_time(self, task_time):
        r"""Sets the task_time of this RunningTasks.

        任务时间

        :param task_time: The task_time of this RunningTasks.
        :type task_time: str
        """
        self._task_time = task_time

    @property
    def server_name(self):
        r"""Gets the server_name of this RunningTasks.

        虚拟机名称

        :return: The server_name of this RunningTasks.
        :rtype: str
        """
        return self._server_name

    @server_name.setter
    def server_name(self, server_name):
        r"""Sets the server_name of this RunningTasks.

        虚拟机名称

        :param server_name: The server_name of this RunningTasks.
        :type server_name: str
        """
        self._server_name = server_name

    @property
    def server_id(self):
        r"""Gets the server_id of this RunningTasks.

        虚拟机ID

        :return: The server_id of this RunningTasks.
        :rtype: str
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        r"""Sets the server_id of this RunningTasks.

        虚拟机ID

        :param server_id: The server_id of this RunningTasks.
        :type server_id: str
        """
        self._server_id = server_id

    @property
    def keypair_name(self):
        r"""Gets the keypair_name of this RunningTasks.

        密钥对名称

        :return: The keypair_name of this RunningTasks.
        :rtype: str
        """
        return self._keypair_name

    @keypair_name.setter
    def keypair_name(self, keypair_name):
        r"""Sets the keypair_name of this RunningTasks.

        密钥对名称

        :param keypair_name: The keypair_name of this RunningTasks.
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
        if not isinstance(other, RunningTasks):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
