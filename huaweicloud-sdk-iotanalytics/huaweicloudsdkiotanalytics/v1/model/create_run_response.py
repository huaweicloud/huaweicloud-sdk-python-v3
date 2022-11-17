# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateRunResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'run_id': 'str',
        'job_id': 'str',
        'job_type': 'str',
        'created_time': 'str',
        'sql_job': 'SqlJobRunResponseBody'
    }

    attribute_map = {
        'run_id': 'run_id',
        'job_id': 'job_id',
        'job_type': 'job_type',
        'created_time': 'created_time',
        'sql_job': 'sql_job'
    }

    def __init__(self, run_id=None, job_id=None, job_type=None, created_time=None, sql_job=None):
        """CreateRunResponse

        The model defined in huaweicloud sdk

        :param run_id: 作业运行ID。
        :type run_id: str
        :param job_id: 作业ID。
        :type job_id: str
        :param job_type: 作业类型。
        :type job_type: str
        :param created_time: 创建运行时间。
        :type created_time: str
        :param sql_job: 
        :type sql_job: :class:`huaweicloudsdkiotanalytics.v1.SqlJobRunResponseBody`
        """
        
        super(CreateRunResponse, self).__init__()

        self._run_id = None
        self._job_id = None
        self._job_type = None
        self._created_time = None
        self._sql_job = None
        self.discriminator = None

        if run_id is not None:
            self.run_id = run_id
        if job_id is not None:
            self.job_id = job_id
        if job_type is not None:
            self.job_type = job_type
        if created_time is not None:
            self.created_time = created_time
        if sql_job is not None:
            self.sql_job = sql_job

    @property
    def run_id(self):
        """Gets the run_id of this CreateRunResponse.

        作业运行ID。

        :return: The run_id of this CreateRunResponse.
        :rtype: str
        """
        return self._run_id

    @run_id.setter
    def run_id(self, run_id):
        """Sets the run_id of this CreateRunResponse.

        作业运行ID。

        :param run_id: The run_id of this CreateRunResponse.
        :type run_id: str
        """
        self._run_id = run_id

    @property
    def job_id(self):
        """Gets the job_id of this CreateRunResponse.

        作业ID。

        :return: The job_id of this CreateRunResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this CreateRunResponse.

        作业ID。

        :param job_id: The job_id of this CreateRunResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def job_type(self):
        """Gets the job_type of this CreateRunResponse.

        作业类型。

        :return: The job_type of this CreateRunResponse.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        """Sets the job_type of this CreateRunResponse.

        作业类型。

        :param job_type: The job_type of this CreateRunResponse.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def created_time(self):
        """Gets the created_time of this CreateRunResponse.

        创建运行时间。

        :return: The created_time of this CreateRunResponse.
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this CreateRunResponse.

        创建运行时间。

        :param created_time: The created_time of this CreateRunResponse.
        :type created_time: str
        """
        self._created_time = created_time

    @property
    def sql_job(self):
        """Gets the sql_job of this CreateRunResponse.

        :return: The sql_job of this CreateRunResponse.
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.SqlJobRunResponseBody`
        """
        return self._sql_job

    @sql_job.setter
    def sql_job(self, sql_job):
        """Sets the sql_job of this CreateRunResponse.

        :param sql_job: The sql_job of this CreateRunResponse.
        :type sql_job: :class:`huaweicloudsdkiotanalytics.v1.SqlJobRunResponseBody`
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
        if not isinstance(other, CreateRunResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
