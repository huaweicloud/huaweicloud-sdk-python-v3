# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListExecuteJobResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_record': 'int',
        'job_executions': 'list[JobExeResult]'
    }

    attribute_map = {
        'total_record': 'totalRecord',
        'job_executions': 'job_executions'
    }

    def __init__(self, total_record=None, job_executions=None):
        r"""ListExecuteJobResponse

        The model defined in huaweicloud sdk

        :param total_record: 作业列表总数。
        :type total_record: int
        :param job_executions: 作业列表。
        :type job_executions: list[:class:`huaweicloudsdkmrs.v1.JobExeResult`]
        """
        
        super(ListExecuteJobResponse, self).__init__()

        self._total_record = None
        self._job_executions = None
        self.discriminator = None

        if total_record is not None:
            self.total_record = total_record
        if job_executions is not None:
            self.job_executions = job_executions

    @property
    def total_record(self):
        r"""Gets the total_record of this ListExecuteJobResponse.

        作业列表总数。

        :return: The total_record of this ListExecuteJobResponse.
        :rtype: int
        """
        return self._total_record

    @total_record.setter
    def total_record(self, total_record):
        r"""Sets the total_record of this ListExecuteJobResponse.

        作业列表总数。

        :param total_record: The total_record of this ListExecuteJobResponse.
        :type total_record: int
        """
        self._total_record = total_record

    @property
    def job_executions(self):
        r"""Gets the job_executions of this ListExecuteJobResponse.

        作业列表。

        :return: The job_executions of this ListExecuteJobResponse.
        :rtype: list[:class:`huaweicloudsdkmrs.v1.JobExeResult`]
        """
        return self._job_executions

    @job_executions.setter
    def job_executions(self, job_executions):
        r"""Sets the job_executions of this ListExecuteJobResponse.

        作业列表。

        :param job_executions: The job_executions of this ListExecuteJobResponse.
        :type job_executions: list[:class:`huaweicloudsdkmrs.v1.JobExeResult`]
        """
        self._job_executions = job_executions

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
        if not isinstance(other, ListExecuteJobResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
