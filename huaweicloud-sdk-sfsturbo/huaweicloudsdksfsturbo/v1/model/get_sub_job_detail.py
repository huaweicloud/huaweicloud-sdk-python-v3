# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetSubJobDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'job_id': 'str',
        'job_type': 'str',
        'begin_time': 'str',
        'end_time': 'str',
        'error_code': 'str',
        'fail_reason': 'str'
    }

    attribute_map = {
        'status': 'status',
        'job_id': 'job_id',
        'job_type': 'job_type',
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'error_code': 'error_code',
        'fail_reason': 'fail_reason'
    }

    def __init__(self, status=None, job_id=None, job_type=None, begin_time=None, end_time=None, error_code=None, fail_reason=None):
        r"""GetSubJobDetail

        The model defined in huaweicloud sdk

        :param status: 子任务的状态。success：成功。running：运行中。failed：失败。waiting：等待执行。
        :type status: str
        :param job_id: 子任务的ID。
        :type job_id: str
        :param job_type: 子任务的类型。
        :type job_type: str
        :param begin_time: 子任务开始时间。UTC时间，格式：&#39;2016-01-02 15:04:05&#39;
        :type begin_time: str
        :param end_time: 子任务结束时间。UTC时间，格式：&#39;2016-01-02 15:04:05&#39;
        :type end_time: str
        :param error_code: 子任务执行失败时的错误码
        :type error_code: str
        :param fail_reason: 子任务执行失败时的错误原因
        :type fail_reason: str
        """
        
        

        self._status = None
        self._job_id = None
        self._job_type = None
        self._begin_time = None
        self._end_time = None
        self._error_code = None
        self._fail_reason = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if job_id is not None:
            self.job_id = job_id
        if job_type is not None:
            self.job_type = job_type
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time
        if error_code is not None:
            self.error_code = error_code
        if fail_reason is not None:
            self.fail_reason = fail_reason

    @property
    def status(self):
        r"""Gets the status of this GetSubJobDetail.

        子任务的状态。success：成功。running：运行中。failed：失败。waiting：等待执行。

        :return: The status of this GetSubJobDetail.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this GetSubJobDetail.

        子任务的状态。success：成功。running：运行中。failed：失败。waiting：等待执行。

        :param status: The status of this GetSubJobDetail.
        :type status: str
        """
        self._status = status

    @property
    def job_id(self):
        r"""Gets the job_id of this GetSubJobDetail.

        子任务的ID。

        :return: The job_id of this GetSubJobDetail.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this GetSubJobDetail.

        子任务的ID。

        :param job_id: The job_id of this GetSubJobDetail.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def job_type(self):
        r"""Gets the job_type of this GetSubJobDetail.

        子任务的类型。

        :return: The job_type of this GetSubJobDetail.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        r"""Sets the job_type of this GetSubJobDetail.

        子任务的类型。

        :param job_type: The job_type of this GetSubJobDetail.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def begin_time(self):
        r"""Gets the begin_time of this GetSubJobDetail.

        子任务开始时间。UTC时间，格式：'2016-01-02 15:04:05'

        :return: The begin_time of this GetSubJobDetail.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        r"""Sets the begin_time of this GetSubJobDetail.

        子任务开始时间。UTC时间，格式：'2016-01-02 15:04:05'

        :param begin_time: The begin_time of this GetSubJobDetail.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        r"""Gets the end_time of this GetSubJobDetail.

        子任务结束时间。UTC时间，格式：'2016-01-02 15:04:05'

        :return: The end_time of this GetSubJobDetail.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this GetSubJobDetail.

        子任务结束时间。UTC时间，格式：'2016-01-02 15:04:05'

        :param end_time: The end_time of this GetSubJobDetail.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def error_code(self):
        r"""Gets the error_code of this GetSubJobDetail.

        子任务执行失败时的错误码

        :return: The error_code of this GetSubJobDetail.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this GetSubJobDetail.

        子任务执行失败时的错误码

        :param error_code: The error_code of this GetSubJobDetail.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def fail_reason(self):
        r"""Gets the fail_reason of this GetSubJobDetail.

        子任务执行失败时的错误原因

        :return: The fail_reason of this GetSubJobDetail.
        :rtype: str
        """
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, fail_reason):
        r"""Sets the fail_reason of this GetSubJobDetail.

        子任务执行失败时的错误原因

        :param fail_reason: The fail_reason of this GetSubJobDetail.
        :type fail_reason: str
        """
        self._fail_reason = fail_reason

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
        if not isinstance(other, GetSubJobDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
