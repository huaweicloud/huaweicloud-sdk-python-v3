# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDatasetResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'run_id': 'str',
        'job_type': 'str',
        'sql_job': 'SqlJobQueryDataset'
    }

    attribute_map = {
        'count': 'count',
        'run_id': 'run_id',
        'job_type': 'job_type',
        'sql_job': 'sql_job'
    }

    def __init__(self, count=None, run_id=None, job_type=None, sql_job=None):
        r"""ShowDatasetResponse

        The model defined in huaweicloud sdk

        :param count: 作业结果总个数。
        :type count: int
        :param run_id: 作业运行ID。
        :type run_id: str
        :param job_type: 作业类型。
        :type job_type: str
        :param sql_job: 
        :type sql_job: :class:`huaweicloudsdkiotanalytics.v1.SqlJobQueryDataset`
        """
        
        super(ShowDatasetResponse, self).__init__()

        self._count = None
        self._run_id = None
        self._job_type = None
        self._sql_job = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if run_id is not None:
            self.run_id = run_id
        if job_type is not None:
            self.job_type = job_type
        if sql_job is not None:
            self.sql_job = sql_job

    @property
    def count(self):
        r"""Gets the count of this ShowDatasetResponse.

        作业结果总个数。

        :return: The count of this ShowDatasetResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ShowDatasetResponse.

        作业结果总个数。

        :param count: The count of this ShowDatasetResponse.
        :type count: int
        """
        self._count = count

    @property
    def run_id(self):
        r"""Gets the run_id of this ShowDatasetResponse.

        作业运行ID。

        :return: The run_id of this ShowDatasetResponse.
        :rtype: str
        """
        return self._run_id

    @run_id.setter
    def run_id(self, run_id):
        r"""Sets the run_id of this ShowDatasetResponse.

        作业运行ID。

        :param run_id: The run_id of this ShowDatasetResponse.
        :type run_id: str
        """
        self._run_id = run_id

    @property
    def job_type(self):
        r"""Gets the job_type of this ShowDatasetResponse.

        作业类型。

        :return: The job_type of this ShowDatasetResponse.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        r"""Sets the job_type of this ShowDatasetResponse.

        作业类型。

        :param job_type: The job_type of this ShowDatasetResponse.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def sql_job(self):
        r"""Gets the sql_job of this ShowDatasetResponse.

        :return: The sql_job of this ShowDatasetResponse.
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.SqlJobQueryDataset`
        """
        return self._sql_job

    @sql_job.setter
    def sql_job(self, sql_job):
        r"""Sets the sql_job of this ShowDatasetResponse.

        :param sql_job: The sql_job of this ShowDatasetResponse.
        :type sql_job: :class:`huaweicloudsdkiotanalytics.v1.SqlJobQueryDataset`
        """
        self._sql_job = sql_job

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
        if not isinstance(other, ShowDatasetResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
