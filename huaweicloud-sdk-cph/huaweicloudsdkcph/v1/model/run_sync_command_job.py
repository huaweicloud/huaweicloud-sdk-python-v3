# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RunSyncCommandJob:

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
        'job_id': 'str',
        'status': 'int',
        'error_code': 'str',
        'error_msg': 'str',
        'execute_msg': 'str'
    }

    attribute_map = {
        'phone_id': 'phone_id',
        'job_id': 'job_id',
        'status': 'status',
        'error_code': 'error_code',
        'error_msg': 'error_msg',
        'execute_msg': 'execute_msg'
    }

    def __init__(self, phone_id=None, job_id=None, status=None, error_code=None, error_msg=None, execute_msg=None):
        r"""RunSyncCommandJob

        The model defined in huaweicloud sdk

        :param phone_id: 云手机的唯一标识，云手机相关任务包含此字段。
        :type phone_id: str
        :param job_id: 任务的唯一标识。
        :type job_id: str
        :param status: 任务状态 - 2：成功 - 1：运行中 - -1：失败
        :type status: int
        :param error_code: 任务错误码。
        :type error_code: str
        :param error_msg: 任务错误码说明。
        :type error_msg: str
        :param execute_msg: 任务执行返回内容，最长1024字节。
        :type execute_msg: str
        """
        
        

        self._phone_id = None
        self._job_id = None
        self._status = None
        self._error_code = None
        self._error_msg = None
        self._execute_msg = None
        self.discriminator = None

        if phone_id is not None:
            self.phone_id = phone_id
        if job_id is not None:
            self.job_id = job_id
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
        r"""Gets the phone_id of this RunSyncCommandJob.

        云手机的唯一标识，云手机相关任务包含此字段。

        :return: The phone_id of this RunSyncCommandJob.
        :rtype: str
        """
        return self._phone_id

    @phone_id.setter
    def phone_id(self, phone_id):
        r"""Sets the phone_id of this RunSyncCommandJob.

        云手机的唯一标识，云手机相关任务包含此字段。

        :param phone_id: The phone_id of this RunSyncCommandJob.
        :type phone_id: str
        """
        self._phone_id = phone_id

    @property
    def job_id(self):
        r"""Gets the job_id of this RunSyncCommandJob.

        任务的唯一标识。

        :return: The job_id of this RunSyncCommandJob.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this RunSyncCommandJob.

        任务的唯一标识。

        :param job_id: The job_id of this RunSyncCommandJob.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def status(self):
        r"""Gets the status of this RunSyncCommandJob.

        任务状态 - 2：成功 - 1：运行中 - -1：失败

        :return: The status of this RunSyncCommandJob.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this RunSyncCommandJob.

        任务状态 - 2：成功 - 1：运行中 - -1：失败

        :param status: The status of this RunSyncCommandJob.
        :type status: int
        """
        self._status = status

    @property
    def error_code(self):
        r"""Gets the error_code of this RunSyncCommandJob.

        任务错误码。

        :return: The error_code of this RunSyncCommandJob.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this RunSyncCommandJob.

        任务错误码。

        :param error_code: The error_code of this RunSyncCommandJob.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_msg(self):
        r"""Gets the error_msg of this RunSyncCommandJob.

        任务错误码说明。

        :return: The error_msg of this RunSyncCommandJob.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        r"""Sets the error_msg of this RunSyncCommandJob.

        任务错误码说明。

        :param error_msg: The error_msg of this RunSyncCommandJob.
        :type error_msg: str
        """
        self._error_msg = error_msg

    @property
    def execute_msg(self):
        r"""Gets the execute_msg of this RunSyncCommandJob.

        任务执行返回内容，最长1024字节。

        :return: The execute_msg of this RunSyncCommandJob.
        :rtype: str
        """
        return self._execute_msg

    @execute_msg.setter
    def execute_msg(self, execute_msg):
        r"""Sets the execute_msg of this RunSyncCommandJob.

        任务执行返回内容，最长1024字节。

        :param execute_msg: The execute_msg of this RunSyncCommandJob.
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
        if not isinstance(other, RunSyncCommandJob):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
