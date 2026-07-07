# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ParseDeadLockResponse(SdkResponse):

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
        'status': 'str',
        'sql_insight_job_id': 'int'
    }

    attribute_map = {
        'job_id': 'job_id',
        'status': 'status',
        'sql_insight_job_id': 'sql_insight_job_id'
    }

    def __init__(self, job_id=None, status=None, sql_insight_job_id=None):
        r"""ParseDeadLockResponse

        The model defined in huaweicloud sdk

        :param job_id: 一键分析死锁日志任务唯一标识符
        :type job_id: str
        :param status: 任务状态
        :type status: str
        :param sql_insight_job_id: SQL洞察任务唯一标识符
        :type sql_insight_job_id: int
        """
        
        super().__init__()

        self._job_id = None
        self._status = None
        self._sql_insight_job_id = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if status is not None:
            self.status = status
        if sql_insight_job_id is not None:
            self.sql_insight_job_id = sql_insight_job_id

    @property
    def job_id(self):
        r"""Gets the job_id of this ParseDeadLockResponse.

        一键分析死锁日志任务唯一标识符

        :return: The job_id of this ParseDeadLockResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this ParseDeadLockResponse.

        一键分析死锁日志任务唯一标识符

        :param job_id: The job_id of this ParseDeadLockResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def status(self):
        r"""Gets the status of this ParseDeadLockResponse.

        任务状态

        :return: The status of this ParseDeadLockResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ParseDeadLockResponse.

        任务状态

        :param status: The status of this ParseDeadLockResponse.
        :type status: str
        """
        self._status = status

    @property
    def sql_insight_job_id(self):
        r"""Gets the sql_insight_job_id of this ParseDeadLockResponse.

        SQL洞察任务唯一标识符

        :return: The sql_insight_job_id of this ParseDeadLockResponse.
        :rtype: int
        """
        return self._sql_insight_job_id

    @sql_insight_job_id.setter
    def sql_insight_job_id(self, sql_insight_job_id):
        r"""Sets the sql_insight_job_id of this ParseDeadLockResponse.

        SQL洞察任务唯一标识符

        :param sql_insight_job_id: The sql_insight_job_id of this ParseDeadLockResponse.
        :type sql_insight_job_id: int
        """
        self._sql_insight_job_id = sql_insight_job_id

    def to_dict(self):
        import warnings
        warnings.warn("ParseDeadLockResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ParseDeadLockResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
