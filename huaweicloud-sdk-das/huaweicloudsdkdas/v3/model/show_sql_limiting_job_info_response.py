# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSqlLimitingJobInfoResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_id': 'str',
        'job_name': 'str',
        'job_type': 'str',
        'status': 'str',
        'fail_reason': 'str'
    }

    attribute_map = {
        'job_id': 'job_id',
        'job_name': 'job_name',
        'job_type': 'job_type',
        'status': 'status',
        'fail_reason': 'fail_reason'
    }

    def __init__(self, job_id=None, job_name=None, job_type=None, status=None, fail_reason=None):
        r"""ShowSqlLimitingJobInfoResponse

        The model defined in huaweicloud sdk

        :param job_id: 任务ID
        :type job_id: str
        :param job_name: 任务名称
        :type job_name: str
        :param job_type: 任务类型
        :type job_type: str
        :param status: 任务状态
        :type status: str
        :param fail_reason: 失败原因
        :type fail_reason: str
        """
        
        super().__init__()

        self._job_id = None
        self._job_name = None
        self._job_type = None
        self._status = None
        self._fail_reason = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if job_name is not None:
            self.job_name = job_name
        if job_type is not None:
            self.job_type = job_type
        if status is not None:
            self.status = status
        if fail_reason is not None:
            self.fail_reason = fail_reason

    @property
    def job_id(self):
        r"""Gets the job_id of this ShowSqlLimitingJobInfoResponse.

        任务ID

        :return: The job_id of this ShowSqlLimitingJobInfoResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this ShowSqlLimitingJobInfoResponse.

        任务ID

        :param job_id: The job_id of this ShowSqlLimitingJobInfoResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def job_name(self):
        r"""Gets the job_name of this ShowSqlLimitingJobInfoResponse.

        任务名称

        :return: The job_name of this ShowSqlLimitingJobInfoResponse.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        r"""Sets the job_name of this ShowSqlLimitingJobInfoResponse.

        任务名称

        :param job_name: The job_name of this ShowSqlLimitingJobInfoResponse.
        :type job_name: str
        """
        self._job_name = job_name

    @property
    def job_type(self):
        r"""Gets the job_type of this ShowSqlLimitingJobInfoResponse.

        任务类型

        :return: The job_type of this ShowSqlLimitingJobInfoResponse.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        r"""Sets the job_type of this ShowSqlLimitingJobInfoResponse.

        任务类型

        :param job_type: The job_type of this ShowSqlLimitingJobInfoResponse.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def status(self):
        r"""Gets the status of this ShowSqlLimitingJobInfoResponse.

        任务状态

        :return: The status of this ShowSqlLimitingJobInfoResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowSqlLimitingJobInfoResponse.

        任务状态

        :param status: The status of this ShowSqlLimitingJobInfoResponse.
        :type status: str
        """
        self._status = status

    @property
    def fail_reason(self):
        r"""Gets the fail_reason of this ShowSqlLimitingJobInfoResponse.

        失败原因

        :return: The fail_reason of this ShowSqlLimitingJobInfoResponse.
        :rtype: str
        """
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, fail_reason):
        r"""Sets the fail_reason of this ShowSqlLimitingJobInfoResponse.

        失败原因

        :param fail_reason: The fail_reason of this ShowSqlLimitingJobInfoResponse.
        :type fail_reason: str
        """
        self._fail_reason = fail_reason

    def to_dict(self):
        import warnings
        warnings.warn("ShowSqlLimitingJobInfoResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowSqlLimitingJobInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
