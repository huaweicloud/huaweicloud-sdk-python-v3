# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SetSqlLimitingSwitchNewResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'switch_on': 'str',
        'retry': 'bool',
        'error_msg': 'str',
        'status': 'bool',
        'detail_status': 'str',
        'fail_reason': 'str',
        'job_id': 'str',
        'job_status': 'str'
    }

    attribute_map = {
        'switch_on': 'switch_on',
        'retry': 'retry',
        'error_msg': 'error_msg',
        'status': 'status',
        'detail_status': 'detail_status',
        'fail_reason': 'fail_reason',
        'job_id': 'job_id',
        'job_status': 'job_status'
    }

    def __init__(self, switch_on=None, retry=None, error_msg=None, status=None, detail_status=None, fail_reason=None, job_id=None, job_status=None):
        r"""SetSqlLimitingSwitchNewResponse

        The model defined in huaweicloud sdk

        :param switch_on: 开关状态
        :type switch_on: str
        :param retry: 是否需要重试
        :type retry: bool
        :param error_msg: 错误信息
        :type error_msg: str
        :param status: 状态
        :type status: bool
        :param detail_status: 详细状态
        :type detail_status: str
        :param fail_reason: 失败原因
        :type fail_reason: str
        :param job_id: 工作流ID
        :type job_id: str
        :param job_status: 工作流状态
        :type job_status: str
        """
        
        super().__init__()

        self._switch_on = None
        self._retry = None
        self._error_msg = None
        self._status = None
        self._detail_status = None
        self._fail_reason = None
        self._job_id = None
        self._job_status = None
        self.discriminator = None

        if switch_on is not None:
            self.switch_on = switch_on
        if retry is not None:
            self.retry = retry
        if error_msg is not None:
            self.error_msg = error_msg
        if status is not None:
            self.status = status
        if detail_status is not None:
            self.detail_status = detail_status
        if fail_reason is not None:
            self.fail_reason = fail_reason
        if job_id is not None:
            self.job_id = job_id
        if job_status is not None:
            self.job_status = job_status

    @property
    def switch_on(self):
        r"""Gets the switch_on of this SetSqlLimitingSwitchNewResponse.

        开关状态

        :return: The switch_on of this SetSqlLimitingSwitchNewResponse.
        :rtype: str
        """
        return self._switch_on

    @switch_on.setter
    def switch_on(self, switch_on):
        r"""Sets the switch_on of this SetSqlLimitingSwitchNewResponse.

        开关状态

        :param switch_on: The switch_on of this SetSqlLimitingSwitchNewResponse.
        :type switch_on: str
        """
        self._switch_on = switch_on

    @property
    def retry(self):
        r"""Gets the retry of this SetSqlLimitingSwitchNewResponse.

        是否需要重试

        :return: The retry of this SetSqlLimitingSwitchNewResponse.
        :rtype: bool
        """
        return self._retry

    @retry.setter
    def retry(self, retry):
        r"""Sets the retry of this SetSqlLimitingSwitchNewResponse.

        是否需要重试

        :param retry: The retry of this SetSqlLimitingSwitchNewResponse.
        :type retry: bool
        """
        self._retry = retry

    @property
    def error_msg(self):
        r"""Gets the error_msg of this SetSqlLimitingSwitchNewResponse.

        错误信息

        :return: The error_msg of this SetSqlLimitingSwitchNewResponse.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        r"""Sets the error_msg of this SetSqlLimitingSwitchNewResponse.

        错误信息

        :param error_msg: The error_msg of this SetSqlLimitingSwitchNewResponse.
        :type error_msg: str
        """
        self._error_msg = error_msg

    @property
    def status(self):
        r"""Gets the status of this SetSqlLimitingSwitchNewResponse.

        状态

        :return: The status of this SetSqlLimitingSwitchNewResponse.
        :rtype: bool
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this SetSqlLimitingSwitchNewResponse.

        状态

        :param status: The status of this SetSqlLimitingSwitchNewResponse.
        :type status: bool
        """
        self._status = status

    @property
    def detail_status(self):
        r"""Gets the detail_status of this SetSqlLimitingSwitchNewResponse.

        详细状态

        :return: The detail_status of this SetSqlLimitingSwitchNewResponse.
        :rtype: str
        """
        return self._detail_status

    @detail_status.setter
    def detail_status(self, detail_status):
        r"""Sets the detail_status of this SetSqlLimitingSwitchNewResponse.

        详细状态

        :param detail_status: The detail_status of this SetSqlLimitingSwitchNewResponse.
        :type detail_status: str
        """
        self._detail_status = detail_status

    @property
    def fail_reason(self):
        r"""Gets the fail_reason of this SetSqlLimitingSwitchNewResponse.

        失败原因

        :return: The fail_reason of this SetSqlLimitingSwitchNewResponse.
        :rtype: str
        """
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, fail_reason):
        r"""Sets the fail_reason of this SetSqlLimitingSwitchNewResponse.

        失败原因

        :param fail_reason: The fail_reason of this SetSqlLimitingSwitchNewResponse.
        :type fail_reason: str
        """
        self._fail_reason = fail_reason

    @property
    def job_id(self):
        r"""Gets the job_id of this SetSqlLimitingSwitchNewResponse.

        工作流ID

        :return: The job_id of this SetSqlLimitingSwitchNewResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this SetSqlLimitingSwitchNewResponse.

        工作流ID

        :param job_id: The job_id of this SetSqlLimitingSwitchNewResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def job_status(self):
        r"""Gets the job_status of this SetSqlLimitingSwitchNewResponse.

        工作流状态

        :return: The job_status of this SetSqlLimitingSwitchNewResponse.
        :rtype: str
        """
        return self._job_status

    @job_status.setter
    def job_status(self, job_status):
        r"""Sets the job_status of this SetSqlLimitingSwitchNewResponse.

        工作流状态

        :param job_status: The job_status of this SetSqlLimitingSwitchNewResponse.
        :type job_status: str
        """
        self._job_status = job_status

    def to_dict(self):
        import warnings
        warnings.warn("SetSqlLimitingSwitchNewResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SetSqlLimitingSwitchNewResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
