# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListJobDetailsResponse(SdkResponse):

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
        'begin_time': 'str',
        'end_time': 'str',
        'status': 'str',
        'failed_code': 'str',
        'failed_detail': 'str',
        'progress': 'str'
    }

    attribute_map = {
        'job_id': 'job_id',
        'job_name': 'job_name',
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'status': 'status',
        'failed_code': 'failed_code',
        'failed_detail': 'failed_detail',
        'progress': 'progress'
    }

    def __init__(self, job_id=None, job_name=None, begin_time=None, end_time=None, status=None, failed_code=None, failed_detail=None, progress=None):
        """ListJobDetailsResponse

        The model defined in huaweicloud sdk

        :param job_id: 任务ID
        :type job_id: str
        :param job_name: 任务名称
        :type job_name: str
        :param begin_time: 任务开始时间
        :type begin_time: str
        :param end_time: 任务结束时间
        :type end_time: str
        :param status: 任务当前状态
        :type status: str
        :param failed_code: 任务失败错误码
        :type failed_code: str
        :param failed_detail: 任务失败错误详情
        :type failed_detail: str
        :param progress: 任务进度
        :type progress: str
        """
        
        super(ListJobDetailsResponse, self).__init__()

        self._job_id = None
        self._job_name = None
        self._begin_time = None
        self._end_time = None
        self._status = None
        self._failed_code = None
        self._failed_detail = None
        self._progress = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if job_name is not None:
            self.job_name = job_name
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time
        if status is not None:
            self.status = status
        if failed_code is not None:
            self.failed_code = failed_code
        if failed_detail is not None:
            self.failed_detail = failed_detail
        if progress is not None:
            self.progress = progress

    @property
    def job_id(self):
        """Gets the job_id of this ListJobDetailsResponse.

        任务ID

        :return: The job_id of this ListJobDetailsResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this ListJobDetailsResponse.

        任务ID

        :param job_id: The job_id of this ListJobDetailsResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def job_name(self):
        """Gets the job_name of this ListJobDetailsResponse.

        任务名称

        :return: The job_name of this ListJobDetailsResponse.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        """Sets the job_name of this ListJobDetailsResponse.

        任务名称

        :param job_name: The job_name of this ListJobDetailsResponse.
        :type job_name: str
        """
        self._job_name = job_name

    @property
    def begin_time(self):
        """Gets the begin_time of this ListJobDetailsResponse.

        任务开始时间

        :return: The begin_time of this ListJobDetailsResponse.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        """Sets the begin_time of this ListJobDetailsResponse.

        任务开始时间

        :param begin_time: The begin_time of this ListJobDetailsResponse.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        """Gets the end_time of this ListJobDetailsResponse.

        任务结束时间

        :return: The end_time of this ListJobDetailsResponse.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ListJobDetailsResponse.

        任务结束时间

        :param end_time: The end_time of this ListJobDetailsResponse.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def status(self):
        """Gets the status of this ListJobDetailsResponse.

        任务当前状态

        :return: The status of this ListJobDetailsResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListJobDetailsResponse.

        任务当前状态

        :param status: The status of this ListJobDetailsResponse.
        :type status: str
        """
        self._status = status

    @property
    def failed_code(self):
        """Gets the failed_code of this ListJobDetailsResponse.

        任务失败错误码

        :return: The failed_code of this ListJobDetailsResponse.
        :rtype: str
        """
        return self._failed_code

    @failed_code.setter
    def failed_code(self, failed_code):
        """Sets the failed_code of this ListJobDetailsResponse.

        任务失败错误码

        :param failed_code: The failed_code of this ListJobDetailsResponse.
        :type failed_code: str
        """
        self._failed_code = failed_code

    @property
    def failed_detail(self):
        """Gets the failed_detail of this ListJobDetailsResponse.

        任务失败错误详情

        :return: The failed_detail of this ListJobDetailsResponse.
        :rtype: str
        """
        return self._failed_detail

    @failed_detail.setter
    def failed_detail(self, failed_detail):
        """Sets the failed_detail of this ListJobDetailsResponse.

        任务失败错误详情

        :param failed_detail: The failed_detail of this ListJobDetailsResponse.
        :type failed_detail: str
        """
        self._failed_detail = failed_detail

    @property
    def progress(self):
        """Gets the progress of this ListJobDetailsResponse.

        任务进度

        :return: The progress of this ListJobDetailsResponse.
        :rtype: str
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this ListJobDetailsResponse.

        任务进度

        :param progress: The progress of this ListJobDetailsResponse.
        :type progress: str
        """
        self._progress = progress

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
        if not isinstance(other, ListJobDetailsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
