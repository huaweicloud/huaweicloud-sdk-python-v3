# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowJobDetailResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'job_type': 'JobType',
        'begin_time': 'datetime',
        'end_time': 'datetime',
        'status': 'JobStatus',
        'sub_jobs_total': 'int',
        'sub_jobs': 'list[JobDetailInfo]'
    }

    attribute_map = {
        'id': 'id',
        'job_type': 'job_type',
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'status': 'status',
        'sub_jobs_total': 'sub_jobs_total',
        'sub_jobs': 'sub_jobs'
    }

    def __init__(self, id=None, job_type=None, begin_time=None, end_time=None, status=None, sub_jobs_total=None, sub_jobs=None):
        r"""ShowJobDetailResponse

        The model defined in huaweicloud sdk

        :param id: 任务ID。
        :type id: str
        :param job_type: 
        :type job_type: :class:`huaweicloudsdkworkspaceapp.v1.JobType`
        :param begin_time: 任务创建时间。
        :type begin_time: datetime
        :param end_time: 任务结束时间。
        :type end_time: datetime
        :param status: 
        :type status: :class:`huaweicloudsdkworkspaceapp.v1.JobStatus`
        :param sub_jobs_total: 子任务总数。
        :type sub_jobs_total: int
        :param sub_jobs: 子任务列表。
        :type sub_jobs: list[:class:`huaweicloudsdkworkspaceapp.v1.JobDetailInfo`]
        """
        
        super(ShowJobDetailResponse, self).__init__()

        self._id = None
        self._job_type = None
        self._begin_time = None
        self._end_time = None
        self._status = None
        self._sub_jobs_total = None
        self._sub_jobs = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if job_type is not None:
            self.job_type = job_type
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time
        if status is not None:
            self.status = status
        if sub_jobs_total is not None:
            self.sub_jobs_total = sub_jobs_total
        if sub_jobs is not None:
            self.sub_jobs = sub_jobs

    @property
    def id(self):
        r"""Gets the id of this ShowJobDetailResponse.

        任务ID。

        :return: The id of this ShowJobDetailResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowJobDetailResponse.

        任务ID。

        :param id: The id of this ShowJobDetailResponse.
        :type id: str
        """
        self._id = id

    @property
    def job_type(self):
        r"""Gets the job_type of this ShowJobDetailResponse.

        :return: The job_type of this ShowJobDetailResponse.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.JobType`
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        r"""Sets the job_type of this ShowJobDetailResponse.

        :param job_type: The job_type of this ShowJobDetailResponse.
        :type job_type: :class:`huaweicloudsdkworkspaceapp.v1.JobType`
        """
        self._job_type = job_type

    @property
    def begin_time(self):
        r"""Gets the begin_time of this ShowJobDetailResponse.

        任务创建时间。

        :return: The begin_time of this ShowJobDetailResponse.
        :rtype: datetime
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        r"""Sets the begin_time of this ShowJobDetailResponse.

        任务创建时间。

        :param begin_time: The begin_time of this ShowJobDetailResponse.
        :type begin_time: datetime
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ShowJobDetailResponse.

        任务结束时间。

        :return: The end_time of this ShowJobDetailResponse.
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ShowJobDetailResponse.

        任务结束时间。

        :param end_time: The end_time of this ShowJobDetailResponse.
        :type end_time: datetime
        """
        self._end_time = end_time

    @property
    def status(self):
        r"""Gets the status of this ShowJobDetailResponse.

        :return: The status of this ShowJobDetailResponse.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.JobStatus`
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowJobDetailResponse.

        :param status: The status of this ShowJobDetailResponse.
        :type status: :class:`huaweicloudsdkworkspaceapp.v1.JobStatus`
        """
        self._status = status

    @property
    def sub_jobs_total(self):
        r"""Gets the sub_jobs_total of this ShowJobDetailResponse.

        子任务总数。

        :return: The sub_jobs_total of this ShowJobDetailResponse.
        :rtype: int
        """
        return self._sub_jobs_total

    @sub_jobs_total.setter
    def sub_jobs_total(self, sub_jobs_total):
        r"""Sets the sub_jobs_total of this ShowJobDetailResponse.

        子任务总数。

        :param sub_jobs_total: The sub_jobs_total of this ShowJobDetailResponse.
        :type sub_jobs_total: int
        """
        self._sub_jobs_total = sub_jobs_total

    @property
    def sub_jobs(self):
        r"""Gets the sub_jobs of this ShowJobDetailResponse.

        子任务列表。

        :return: The sub_jobs of this ShowJobDetailResponse.
        :rtype: list[:class:`huaweicloudsdkworkspaceapp.v1.JobDetailInfo`]
        """
        return self._sub_jobs

    @sub_jobs.setter
    def sub_jobs(self, sub_jobs):
        r"""Sets the sub_jobs of this ShowJobDetailResponse.

        子任务列表。

        :param sub_jobs: The sub_jobs of this ShowJobDetailResponse.
        :type sub_jobs: list[:class:`huaweicloudsdkworkspaceapp.v1.JobDetailInfo`]
        """
        self._sub_jobs = sub_jobs

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
        if not isinstance(other, ShowJobDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
