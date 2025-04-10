# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SubJobResult:

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
        'fail_reason': 'str',
        'entities': 'SubJobEntities'
    }

    attribute_map = {
        'status': 'status',
        'job_id': 'job_id',
        'job_type': 'job_type',
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'error_code': 'error_code',
        'fail_reason': 'fail_reason',
        'entities': 'entities'
    }

    def __init__(self, status=None, job_id=None, job_type=None, begin_time=None, end_time=None, error_code=None, fail_reason=None, entities=None):
        r"""SubJobResult

        The model defined in huaweicloud sdk

        :param status: 任务状态，目前取值如下： SUCCESS：表示该任务执行已经结束，任务执行成功。 FAIL：表示该任务执行已经结束，任务执行失败。 RUNNING：表示该任务正在执行。 INIT：表给任务还未执行，正在初始化。
        :type status: str
        :param job_id: 子任务ID。
        :type job_id: str
        :param job_type: 子任务类型。
        :type job_type: str
        :param begin_time: 子任务开始执行时间。格式为UTC时间。
        :type begin_time: str
        :param end_time: 子任务结束时间。格式为UTC时间。
        :type end_time: str
        :param error_code: 错误码。
        :type error_code: str
        :param fail_reason: 失败原因。
        :type fail_reason: str
        :param entities: 
        :type entities: :class:`huaweicloudsdkims.v2.SubJobEntities`
        """
        
        

        self._status = None
        self._job_id = None
        self._job_type = None
        self._begin_time = None
        self._end_time = None
        self._error_code = None
        self._fail_reason = None
        self._entities = None
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
        if entities is not None:
            self.entities = entities

    @property
    def status(self):
        r"""Gets the status of this SubJobResult.

        任务状态，目前取值如下： SUCCESS：表示该任务执行已经结束，任务执行成功。 FAIL：表示该任务执行已经结束，任务执行失败。 RUNNING：表示该任务正在执行。 INIT：表给任务还未执行，正在初始化。

        :return: The status of this SubJobResult.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this SubJobResult.

        任务状态，目前取值如下： SUCCESS：表示该任务执行已经结束，任务执行成功。 FAIL：表示该任务执行已经结束，任务执行失败。 RUNNING：表示该任务正在执行。 INIT：表给任务还未执行，正在初始化。

        :param status: The status of this SubJobResult.
        :type status: str
        """
        self._status = status

    @property
    def job_id(self):
        r"""Gets the job_id of this SubJobResult.

        子任务ID。

        :return: The job_id of this SubJobResult.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this SubJobResult.

        子任务ID。

        :param job_id: The job_id of this SubJobResult.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def job_type(self):
        r"""Gets the job_type of this SubJobResult.

        子任务类型。

        :return: The job_type of this SubJobResult.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        r"""Sets the job_type of this SubJobResult.

        子任务类型。

        :param job_type: The job_type of this SubJobResult.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def begin_time(self):
        r"""Gets the begin_time of this SubJobResult.

        子任务开始执行时间。格式为UTC时间。

        :return: The begin_time of this SubJobResult.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        r"""Sets the begin_time of this SubJobResult.

        子任务开始执行时间。格式为UTC时间。

        :param begin_time: The begin_time of this SubJobResult.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        r"""Gets the end_time of this SubJobResult.

        子任务结束时间。格式为UTC时间。

        :return: The end_time of this SubJobResult.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this SubJobResult.

        子任务结束时间。格式为UTC时间。

        :param end_time: The end_time of this SubJobResult.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def error_code(self):
        r"""Gets the error_code of this SubJobResult.

        错误码。

        :return: The error_code of this SubJobResult.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this SubJobResult.

        错误码。

        :param error_code: The error_code of this SubJobResult.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def fail_reason(self):
        r"""Gets the fail_reason of this SubJobResult.

        失败原因。

        :return: The fail_reason of this SubJobResult.
        :rtype: str
        """
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, fail_reason):
        r"""Sets the fail_reason of this SubJobResult.

        失败原因。

        :param fail_reason: The fail_reason of this SubJobResult.
        :type fail_reason: str
        """
        self._fail_reason = fail_reason

    @property
    def entities(self):
        r"""Gets the entities of this SubJobResult.

        :return: The entities of this SubJobResult.
        :rtype: :class:`huaweicloudsdkims.v2.SubJobEntities`
        """
        return self._entities

    @entities.setter
    def entities(self, entities):
        r"""Sets the entities of this SubJobResult.

        :param entities: The entities of this SubJobResult.
        :type entities: :class:`huaweicloudsdkims.v2.SubJobEntities`
        """
        self._entities = entities

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
        if not isinstance(other, SubJobResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
