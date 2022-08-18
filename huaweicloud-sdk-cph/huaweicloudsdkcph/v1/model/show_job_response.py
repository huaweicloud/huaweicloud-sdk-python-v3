# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowJobResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'request_id': 'str',
        'error_msg': 'str',
        'execute_msg': 'str',
        'job_id': 'str',
        'end_time': 'str',
        'begin_time': 'str',
        'error_code': 'str',
        'status': 'int'
    }

    attribute_map = {
        'request_id': 'request_id',
        'error_msg': 'error_msg',
        'execute_msg': 'execute_msg',
        'job_id': 'job_id',
        'end_time': 'end_time',
        'begin_time': 'begin_time',
        'error_code': 'error_code',
        'status': 'status'
    }

    def __init__(self, request_id=None, error_msg=None, execute_msg=None, job_id=None, end_time=None, begin_time=None, error_code=None, status=None):
        """ShowJobResponse

        The model defined in huaweicloud sdk

        :param request_id: 请求的唯一标识ID
        :type request_id: str
        :param error_msg: 任务错误码说明
        :type error_msg: str
        :param execute_msg: 任务执行返回内容，最长1024个字节
        :type execute_msg: str
        :param job_id: 任务的唯一标识
        :type job_id: str
        :param end_time: 任务处理结束时间 时间格式为UTC，YYYY-MM-DDTHH:MM:SSZ
        :type end_time: str
        :param begin_time: 任务处理开始时间 时间格式为UTC，YYYY-MM-DDTHH:MM:SSZ
        :type begin_time: str
        :param error_code: 任务错误码
        :type error_code: str
        :param status: 任务状态 - 1： 运行中 - 2： 成功 - -1： 失败
        :type status: int
        """
        
        super(ShowJobResponse, self).__init__()

        self._request_id = None
        self._error_msg = None
        self._execute_msg = None
        self._job_id = None
        self._end_time = None
        self._begin_time = None
        self._error_code = None
        self._status = None
        self.discriminator = None

        self.request_id = request_id
        self.error_msg = error_msg
        self.execute_msg = execute_msg
        self.job_id = job_id
        self.end_time = end_time
        self.begin_time = begin_time
        self.error_code = error_code
        self.status = status

    @property
    def request_id(self):
        """Gets the request_id of this ShowJobResponse.

        请求的唯一标识ID

        :return: The request_id of this ShowJobResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ShowJobResponse.

        请求的唯一标识ID

        :param request_id: The request_id of this ShowJobResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def error_msg(self):
        """Gets the error_msg of this ShowJobResponse.

        任务错误码说明

        :return: The error_msg of this ShowJobResponse.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        """Sets the error_msg of this ShowJobResponse.

        任务错误码说明

        :param error_msg: The error_msg of this ShowJobResponse.
        :type error_msg: str
        """
        self._error_msg = error_msg

    @property
    def execute_msg(self):
        """Gets the execute_msg of this ShowJobResponse.

        任务执行返回内容，最长1024个字节

        :return: The execute_msg of this ShowJobResponse.
        :rtype: str
        """
        return self._execute_msg

    @execute_msg.setter
    def execute_msg(self, execute_msg):
        """Sets the execute_msg of this ShowJobResponse.

        任务执行返回内容，最长1024个字节

        :param execute_msg: The execute_msg of this ShowJobResponse.
        :type execute_msg: str
        """
        self._execute_msg = execute_msg

    @property
    def job_id(self):
        """Gets the job_id of this ShowJobResponse.

        任务的唯一标识

        :return: The job_id of this ShowJobResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this ShowJobResponse.

        任务的唯一标识

        :param job_id: The job_id of this ShowJobResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def end_time(self):
        """Gets the end_time of this ShowJobResponse.

        任务处理结束时间 时间格式为UTC，YYYY-MM-DDTHH:MM:SSZ

        :return: The end_time of this ShowJobResponse.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ShowJobResponse.

        任务处理结束时间 时间格式为UTC，YYYY-MM-DDTHH:MM:SSZ

        :param end_time: The end_time of this ShowJobResponse.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def begin_time(self):
        """Gets the begin_time of this ShowJobResponse.

        任务处理开始时间 时间格式为UTC，YYYY-MM-DDTHH:MM:SSZ

        :return: The begin_time of this ShowJobResponse.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        """Sets the begin_time of this ShowJobResponse.

        任务处理开始时间 时间格式为UTC，YYYY-MM-DDTHH:MM:SSZ

        :param begin_time: The begin_time of this ShowJobResponse.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def error_code(self):
        """Gets the error_code of this ShowJobResponse.

        任务错误码

        :return: The error_code of this ShowJobResponse.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this ShowJobResponse.

        任务错误码

        :param error_code: The error_code of this ShowJobResponse.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def status(self):
        """Gets the status of this ShowJobResponse.

        任务状态 - 1： 运行中 - 2： 成功 - -1： 失败

        :return: The status of this ShowJobResponse.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowJobResponse.

        任务状态 - 1： 运行中 - 2： 成功 - -1： 失败

        :param status: The status of this ShowJobResponse.
        :type status: int
        """
        self._status = status

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
        if not isinstance(other, ShowJobResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
