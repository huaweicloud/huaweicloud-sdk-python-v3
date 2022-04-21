# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobRecords:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'job_name': 'str',
        'record_type': 'str',
        'record_time': 'str',
        'request': 'str',
        'response': 'str',
        'code': 'str',
        'message': 'str',
        'job_status': 'str'
    }

    attribute_map = {
        'job_name': 'job_name',
        'record_type': 'record_type',
        'record_time': 'record_time',
        'request': 'request',
        'response': 'response',
        'code': 'code',
        'message': 'message',
        'job_status': 'job_status'
    }

    def __init__(self, job_name=None, record_type=None, record_time=None, request=None, response=None, code=None, message=None, job_status=None):
        """JobRecords

        The model defined in huaweicloud sdk

        :param job_name: 任务名称
        :type job_name: str
        :param record_type: 记录类型。API：接口调用类型。MEG：消息类型。
        :type record_type: str
        :param record_time: 记录时间。
        :type record_time: str
        :param request: 请求体，仅当record_type为API时有效
        :type request: str
        :param response: 返回体，仅当record_type为API时有效
        :type response: str
        :param code: 返回码，仅当record_type为API时有效
        :type code: str
        :param message: 消息，仅当record_type为MEG时有效
        :type message: str
        :param job_status: job执行状态：SUCCESS：成功。FAIL：失败。
        :type job_status: str
        """
        
        

        self._job_name = None
        self._record_type = None
        self._record_time = None
        self._request = None
        self._response = None
        self._code = None
        self._message = None
        self._job_status = None
        self.discriminator = None

        if job_name is not None:
            self.job_name = job_name
        if record_type is not None:
            self.record_type = record_type
        if record_time is not None:
            self.record_time = record_time
        if request is not None:
            self.request = request
        if response is not None:
            self.response = response
        if code is not None:
            self.code = code
        if message is not None:
            self.message = message
        if job_status is not None:
            self.job_status = job_status

    @property
    def job_name(self):
        """Gets the job_name of this JobRecords.

        任务名称

        :return: The job_name of this JobRecords.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        """Sets the job_name of this JobRecords.

        任务名称

        :param job_name: The job_name of this JobRecords.
        :type job_name: str
        """
        self._job_name = job_name

    @property
    def record_type(self):
        """Gets the record_type of this JobRecords.

        记录类型。API：接口调用类型。MEG：消息类型。

        :return: The record_type of this JobRecords.
        :rtype: str
        """
        return self._record_type

    @record_type.setter
    def record_type(self, record_type):
        """Sets the record_type of this JobRecords.

        记录类型。API：接口调用类型。MEG：消息类型。

        :param record_type: The record_type of this JobRecords.
        :type record_type: str
        """
        self._record_type = record_type

    @property
    def record_time(self):
        """Gets the record_time of this JobRecords.

        记录时间。

        :return: The record_time of this JobRecords.
        :rtype: str
        """
        return self._record_time

    @record_time.setter
    def record_time(self, record_time):
        """Sets the record_time of this JobRecords.

        记录时间。

        :param record_time: The record_time of this JobRecords.
        :type record_time: str
        """
        self._record_time = record_time

    @property
    def request(self):
        """Gets the request of this JobRecords.

        请求体，仅当record_type为API时有效

        :return: The request of this JobRecords.
        :rtype: str
        """
        return self._request

    @request.setter
    def request(self, request):
        """Sets the request of this JobRecords.

        请求体，仅当record_type为API时有效

        :param request: The request of this JobRecords.
        :type request: str
        """
        self._request = request

    @property
    def response(self):
        """Gets the response of this JobRecords.

        返回体，仅当record_type为API时有效

        :return: The response of this JobRecords.
        :rtype: str
        """
        return self._response

    @response.setter
    def response(self, response):
        """Sets the response of this JobRecords.

        返回体，仅当record_type为API时有效

        :param response: The response of this JobRecords.
        :type response: str
        """
        self._response = response

    @property
    def code(self):
        """Gets the code of this JobRecords.

        返回码，仅当record_type为API时有效

        :return: The code of this JobRecords.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this JobRecords.

        返回码，仅当record_type为API时有效

        :param code: The code of this JobRecords.
        :type code: str
        """
        self._code = code

    @property
    def message(self):
        """Gets the message of this JobRecords.

        消息，仅当record_type为MEG时有效

        :return: The message of this JobRecords.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this JobRecords.

        消息，仅当record_type为MEG时有效

        :param message: The message of this JobRecords.
        :type message: str
        """
        self._message = message

    @property
    def job_status(self):
        """Gets the job_status of this JobRecords.

        job执行状态：SUCCESS：成功。FAIL：失败。

        :return: The job_status of this JobRecords.
        :rtype: str
        """
        return self._job_status

    @job_status.setter
    def job_status(self, job_status):
        """Sets the job_status of this JobRecords.

        job执行状态：SUCCESS：成功。FAIL：失败。

        :param job_status: The job_status of this JobRecords.
        :type job_status: str
        """
        self._job_status = job_status

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
        if not isinstance(other, JobRecords):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
