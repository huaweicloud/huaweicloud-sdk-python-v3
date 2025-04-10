# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Job:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'phone_id': 'str',
        'server_id': 'str',
        'node_id': 'str',
        'job_id': 'str',
        'begin_time': 'str',
        'end_time': 'str',
        'status': 'int',
        'error_code': 'str',
        'error_msg': 'str',
        'execute_msg': 'str'
    }

    attribute_map = {
        'phone_id': 'phone_id',
        'server_id': 'server_id',
        'node_id': 'node_id',
        'job_id': 'job_id',
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'status': 'status',
        'error_code': 'error_code',
        'error_msg': 'error_msg',
        'execute_msg': 'execute_msg'
    }

    def __init__(self, phone_id=None, server_id=None, node_id=None, job_id=None, begin_time=None, end_time=None, status=None, error_code=None, error_msg=None, execute_msg=None):
        r"""Job

        The model defined in huaweicloud sdk

        :param phone_id: 云手机的唯一标识，云手机相关任务包含此字段。
        :type phone_id: str
        :param server_id: 云手机服务器的唯一标识ID，云手机服务器相关任务包含此字段。
        :type server_id: str
        :param node_id: （已废弃）云手机服务器的唯一标识ID，云手机服务含此字段。
        :type node_id: str
        :param job_id: 任务的唯一标识。
        :type job_id: str
        :param begin_time: 任务处理开始时间， 时间格式为UTC，YYYY-MM-DDTHH:MM:SSZ。
        :type begin_time: str
        :param end_time: 任务处理结束时间， 时间格式为UTC，YYYY-MM-DDTHH:MM:SSZ。
        :type end_time: str
        :param status: 任务状态。 - 1 ：运行中 - 2 ： 成功 - -1 ：失败
        :type status: int
        :param error_code: 任务错误码。
        :type error_code: str
        :param error_msg: 任务错误码说明。
        :type error_msg: str
        :param execute_msg: 任务执行返回内容，最长1024个字节。
        :type execute_msg: str
        """
        
        

        self._phone_id = None
        self._server_id = None
        self._node_id = None
        self._job_id = None
        self._begin_time = None
        self._end_time = None
        self._status = None
        self._error_code = None
        self._error_msg = None
        self._execute_msg = None
        self.discriminator = None

        if phone_id is not None:
            self.phone_id = phone_id
        if server_id is not None:
            self.server_id = server_id
        if node_id is not None:
            self.node_id = node_id
        if job_id is not None:
            self.job_id = job_id
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time
        if status is not None:
            self.status = status
        if error_code is not None:
            self.error_code = error_code
        if error_msg is not None:
            self.error_msg = error_msg
        if execute_msg is not None:
            self.execute_msg = execute_msg

    @property
    def phone_id(self):
        r"""Gets the phone_id of this Job.

        云手机的唯一标识，云手机相关任务包含此字段。

        :return: The phone_id of this Job.
        :rtype: str
        """
        return self._phone_id

    @phone_id.setter
    def phone_id(self, phone_id):
        r"""Sets the phone_id of this Job.

        云手机的唯一标识，云手机相关任务包含此字段。

        :param phone_id: The phone_id of this Job.
        :type phone_id: str
        """
        self._phone_id = phone_id

    @property
    def server_id(self):
        r"""Gets the server_id of this Job.

        云手机服务器的唯一标识ID，云手机服务器相关任务包含此字段。

        :return: The server_id of this Job.
        :rtype: str
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        r"""Sets the server_id of this Job.

        云手机服务器的唯一标识ID，云手机服务器相关任务包含此字段。

        :param server_id: The server_id of this Job.
        :type server_id: str
        """
        self._server_id = server_id

    @property
    def node_id(self):
        r"""Gets the node_id of this Job.

        （已废弃）云手机服务器的唯一标识ID，云手机服务含此字段。

        :return: The node_id of this Job.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this Job.

        （已废弃）云手机服务器的唯一标识ID，云手机服务含此字段。

        :param node_id: The node_id of this Job.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def job_id(self):
        r"""Gets the job_id of this Job.

        任务的唯一标识。

        :return: The job_id of this Job.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this Job.

        任务的唯一标识。

        :param job_id: The job_id of this Job.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def begin_time(self):
        r"""Gets the begin_time of this Job.

        任务处理开始时间， 时间格式为UTC，YYYY-MM-DDTHH:MM:SSZ。

        :return: The begin_time of this Job.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        r"""Sets the begin_time of this Job.

        任务处理开始时间， 时间格式为UTC，YYYY-MM-DDTHH:MM:SSZ。

        :param begin_time: The begin_time of this Job.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        r"""Gets the end_time of this Job.

        任务处理结束时间， 时间格式为UTC，YYYY-MM-DDTHH:MM:SSZ。

        :return: The end_time of this Job.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this Job.

        任务处理结束时间， 时间格式为UTC，YYYY-MM-DDTHH:MM:SSZ。

        :param end_time: The end_time of this Job.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def status(self):
        r"""Gets the status of this Job.

        任务状态。 - 1 ：运行中 - 2 ： 成功 - -1 ：失败

        :return: The status of this Job.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this Job.

        任务状态。 - 1 ：运行中 - 2 ： 成功 - -1 ：失败

        :param status: The status of this Job.
        :type status: int
        """
        self._status = status

    @property
    def error_code(self):
        r"""Gets the error_code of this Job.

        任务错误码。

        :return: The error_code of this Job.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this Job.

        任务错误码。

        :param error_code: The error_code of this Job.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_msg(self):
        r"""Gets the error_msg of this Job.

        任务错误码说明。

        :return: The error_msg of this Job.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        r"""Sets the error_msg of this Job.

        任务错误码说明。

        :param error_msg: The error_msg of this Job.
        :type error_msg: str
        """
        self._error_msg = error_msg

    @property
    def execute_msg(self):
        r"""Gets the execute_msg of this Job.

        任务执行返回内容，最长1024个字节。

        :return: The execute_msg of this Job.
        :rtype: str
        """
        return self._execute_msg

    @execute_msg.setter
    def execute_msg(self, execute_msg):
        r"""Sets the execute_msg of this Job.

        任务执行返回内容，最长1024个字节。

        :param execute_msg: The execute_msg of this Job.
        :type execute_msg: str
        """
        self._execute_msg = execute_msg

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
        if not isinstance(other, Job):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
