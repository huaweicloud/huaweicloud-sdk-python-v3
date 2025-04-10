# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowRunResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'run_id': 'str',
        'job_id': 'str',
        'job_type': 'str',
        'status': 'str',
        'created_time': 'str',
        'message': 'str',
        'details': 'list[RunDetail]'
    }

    attribute_map = {
        'run_id': 'run_id',
        'job_id': 'job_id',
        'job_type': 'job_type',
        'status': 'status',
        'created_time': 'created_time',
        'message': 'message',
        'details': 'details'
    }

    def __init__(self, run_id=None, job_id=None, job_type=None, status=None, created_time=None, message=None, details=None):
        r"""ShowRunResponse

        The model defined in huaweicloud sdk

        :param run_id: 作业运行ID。
        :type run_id: str
        :param job_id: 作业ID。
        :type job_id: str
        :param job_type: 作业类型。
        :type job_type: str
        :param status: 此作业的当前状态，包含提交（LAUNCHING）、运行中（RUNNING）、完成（FINISHED）、失败（FAILED）、取消（CANCELLED）。
        :type status: str
        :param created_time: 创建运行时间。
        :type created_time: str
        :param message: 系统提示信息。运行失败时，失败原因。
        :type message: str
        :param details: 作业运行详情。
        :type details: list[:class:`huaweicloudsdkiotanalytics.v1.RunDetail`]
        """
        
        super(ShowRunResponse, self).__init__()

        self._run_id = None
        self._job_id = None
        self._job_type = None
        self._status = None
        self._created_time = None
        self._message = None
        self._details = None
        self.discriminator = None

        if run_id is not None:
            self.run_id = run_id
        if job_id is not None:
            self.job_id = job_id
        if job_type is not None:
            self.job_type = job_type
        if status is not None:
            self.status = status
        if created_time is not None:
            self.created_time = created_time
        if message is not None:
            self.message = message
        if details is not None:
            self.details = details

    @property
    def run_id(self):
        r"""Gets the run_id of this ShowRunResponse.

        作业运行ID。

        :return: The run_id of this ShowRunResponse.
        :rtype: str
        """
        return self._run_id

    @run_id.setter
    def run_id(self, run_id):
        r"""Sets the run_id of this ShowRunResponse.

        作业运行ID。

        :param run_id: The run_id of this ShowRunResponse.
        :type run_id: str
        """
        self._run_id = run_id

    @property
    def job_id(self):
        r"""Gets the job_id of this ShowRunResponse.

        作业ID。

        :return: The job_id of this ShowRunResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this ShowRunResponse.

        作业ID。

        :param job_id: The job_id of this ShowRunResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def job_type(self):
        r"""Gets the job_type of this ShowRunResponse.

        作业类型。

        :return: The job_type of this ShowRunResponse.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        r"""Sets the job_type of this ShowRunResponse.

        作业类型。

        :param job_type: The job_type of this ShowRunResponse.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def status(self):
        r"""Gets the status of this ShowRunResponse.

        此作业的当前状态，包含提交（LAUNCHING）、运行中（RUNNING）、完成（FINISHED）、失败（FAILED）、取消（CANCELLED）。

        :return: The status of this ShowRunResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowRunResponse.

        此作业的当前状态，包含提交（LAUNCHING）、运行中（RUNNING）、完成（FINISHED）、失败（FAILED）、取消（CANCELLED）。

        :param status: The status of this ShowRunResponse.
        :type status: str
        """
        self._status = status

    @property
    def created_time(self):
        r"""Gets the created_time of this ShowRunResponse.

        创建运行时间。

        :return: The created_time of this ShowRunResponse.
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        r"""Sets the created_time of this ShowRunResponse.

        创建运行时间。

        :param created_time: The created_time of this ShowRunResponse.
        :type created_time: str
        """
        self._created_time = created_time

    @property
    def message(self):
        r"""Gets the message of this ShowRunResponse.

        系统提示信息。运行失败时，失败原因。

        :return: The message of this ShowRunResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this ShowRunResponse.

        系统提示信息。运行失败时，失败原因。

        :param message: The message of this ShowRunResponse.
        :type message: str
        """
        self._message = message

    @property
    def details(self):
        r"""Gets the details of this ShowRunResponse.

        作业运行详情。

        :return: The details of this ShowRunResponse.
        :rtype: list[:class:`huaweicloudsdkiotanalytics.v1.RunDetail`]
        """
        return self._details

    @details.setter
    def details(self, details):
        r"""Sets the details of this ShowRunResponse.

        作业运行详情。

        :param details: The details of this ShowRunResponse.
        :type details: list[:class:`huaweicloudsdkiotanalytics.v1.RunDetail`]
        """
        self._details = details

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
        if not isinstance(other, ShowRunResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
