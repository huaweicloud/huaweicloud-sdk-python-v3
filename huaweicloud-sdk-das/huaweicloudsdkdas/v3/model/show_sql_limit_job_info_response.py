# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSqlLimitJobInfoResponse(SdkResponse):

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
        'job_status': 'str',
        'fail_reason': 'str'
    }

    attribute_map = {
        'job_id': 'job_id',
        'job_status': 'job_status',
        'fail_reason': 'fail_reason'
    }

    def __init__(self, job_id=None, job_status=None, fail_reason=None):
        """ShowSqlLimitJobInfoResponse

        The model defined in huaweicloud sdk

        :param job_id: 任务ID
        :type job_id: str
        :param job_status: 任务状态
        :type job_status: str
        :param fail_reason: 失败原因
        :type fail_reason: str
        """
        
        super(ShowSqlLimitJobInfoResponse, self).__init__()

        self._job_id = None
        self._job_status = None
        self._fail_reason = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if job_status is not None:
            self.job_status = job_status
        if fail_reason is not None:
            self.fail_reason = fail_reason

    @property
    def job_id(self):
        """Gets the job_id of this ShowSqlLimitJobInfoResponse.

        任务ID

        :return: The job_id of this ShowSqlLimitJobInfoResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this ShowSqlLimitJobInfoResponse.

        任务ID

        :param job_id: The job_id of this ShowSqlLimitJobInfoResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def job_status(self):
        """Gets the job_status of this ShowSqlLimitJobInfoResponse.

        任务状态

        :return: The job_status of this ShowSqlLimitJobInfoResponse.
        :rtype: str
        """
        return self._job_status

    @job_status.setter
    def job_status(self, job_status):
        """Sets the job_status of this ShowSqlLimitJobInfoResponse.

        任务状态

        :param job_status: The job_status of this ShowSqlLimitJobInfoResponse.
        :type job_status: str
        """
        self._job_status = job_status

    @property
    def fail_reason(self):
        """Gets the fail_reason of this ShowSqlLimitJobInfoResponse.

        失败原因

        :return: The fail_reason of this ShowSqlLimitJobInfoResponse.
        :rtype: str
        """
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, fail_reason):
        """Sets the fail_reason of this ShowSqlLimitJobInfoResponse.

        失败原因

        :param fail_reason: The fail_reason of this ShowSqlLimitJobInfoResponse.
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
        if not isinstance(other, ShowSqlLimitJobInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
