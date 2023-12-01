# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSqlJobProgressResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_success': 'bool',
        'message': 'str',
        'job_id': 'str',
        'status': 'str',
        'sub_job_id': 'int',
        'progress': 'float',
        'sub_jobs': 'list[SubJobDatas]'
    }

    attribute_map = {
        'is_success': 'is_success',
        'message': 'message',
        'job_id': 'job_id',
        'status': 'status',
        'sub_job_id': 'sub_job_id',
        'progress': 'progress',
        'sub_jobs': 'sub_jobs'
    }

    def __init__(self, is_success=None, message=None, job_id=None, status=None, sub_job_id=None, progress=None, sub_jobs=None):
        """ShowSqlJobProgressResponse

        The model defined in huaweicloud sdk

        :param is_success: 执行请求是否成功。“true”表示请求执行成功。
        :type is_success: bool
        :param message: 系统提示信息，执行成功时，信息可能为空。
        :type message: str
        :param job_id: 作业ID。
        :type job_id: str
        :param status: 作业状态。
        :type status: str
        :param sub_job_id: 正在运行的子作业ID，如果作业还没开始运行或者运行结束，则子作业ID可能为空。
        :type sub_job_id: int
        :param progress: 正在运行的子作业的进度或者整个作业进度，该值只能粗略的估算子作业进度，不表示作业的详细进度。有两方面的含义： （1）如果整个作业刚开始运行或者在提交中，则进度展示为0；如果作业运行结束，则进度展示为1。此时progress表示整个作业的运行进度，因为没有子作业在运行，sub_job_id不展示。 （2）如果有子作业在运行中，则展示该子作业的运行进度，progress的计算方法为：子作业已经完成的task数除以子作业总的task数。此时progress表示子作业的运行进度，sub_job_id展示。
        :type progress: float
        :param sub_jobs: 正在运行作业的子作业的详细信息，一个作业可能包含多个子作业。
        :type sub_jobs: list[:class:`huaweicloudsdkdli.v1.SubJobDatas`]
        """
        
        super(ShowSqlJobProgressResponse, self).__init__()

        self._is_success = None
        self._message = None
        self._job_id = None
        self._status = None
        self._sub_job_id = None
        self._progress = None
        self._sub_jobs = None
        self.discriminator = None

        if is_success is not None:
            self.is_success = is_success
        if message is not None:
            self.message = message
        if job_id is not None:
            self.job_id = job_id
        if status is not None:
            self.status = status
        if sub_job_id is not None:
            self.sub_job_id = sub_job_id
        if progress is not None:
            self.progress = progress
        if sub_jobs is not None:
            self.sub_jobs = sub_jobs

    @property
    def is_success(self):
        """Gets the is_success of this ShowSqlJobProgressResponse.

        执行请求是否成功。“true”表示请求执行成功。

        :return: The is_success of this ShowSqlJobProgressResponse.
        :rtype: bool
        """
        return self._is_success

    @is_success.setter
    def is_success(self, is_success):
        """Sets the is_success of this ShowSqlJobProgressResponse.

        执行请求是否成功。“true”表示请求执行成功。

        :param is_success: The is_success of this ShowSqlJobProgressResponse.
        :type is_success: bool
        """
        self._is_success = is_success

    @property
    def message(self):
        """Gets the message of this ShowSqlJobProgressResponse.

        系统提示信息，执行成功时，信息可能为空。

        :return: The message of this ShowSqlJobProgressResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ShowSqlJobProgressResponse.

        系统提示信息，执行成功时，信息可能为空。

        :param message: The message of this ShowSqlJobProgressResponse.
        :type message: str
        """
        self._message = message

    @property
    def job_id(self):
        """Gets the job_id of this ShowSqlJobProgressResponse.

        作业ID。

        :return: The job_id of this ShowSqlJobProgressResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this ShowSqlJobProgressResponse.

        作业ID。

        :param job_id: The job_id of this ShowSqlJobProgressResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def status(self):
        """Gets the status of this ShowSqlJobProgressResponse.

        作业状态。

        :return: The status of this ShowSqlJobProgressResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowSqlJobProgressResponse.

        作业状态。

        :param status: The status of this ShowSqlJobProgressResponse.
        :type status: str
        """
        self._status = status

    @property
    def sub_job_id(self):
        """Gets the sub_job_id of this ShowSqlJobProgressResponse.

        正在运行的子作业ID，如果作业还没开始运行或者运行结束，则子作业ID可能为空。

        :return: The sub_job_id of this ShowSqlJobProgressResponse.
        :rtype: int
        """
        return self._sub_job_id

    @sub_job_id.setter
    def sub_job_id(self, sub_job_id):
        """Sets the sub_job_id of this ShowSqlJobProgressResponse.

        正在运行的子作业ID，如果作业还没开始运行或者运行结束，则子作业ID可能为空。

        :param sub_job_id: The sub_job_id of this ShowSqlJobProgressResponse.
        :type sub_job_id: int
        """
        self._sub_job_id = sub_job_id

    @property
    def progress(self):
        """Gets the progress of this ShowSqlJobProgressResponse.

        正在运行的子作业的进度或者整个作业进度，该值只能粗略的估算子作业进度，不表示作业的详细进度。有两方面的含义： （1）如果整个作业刚开始运行或者在提交中，则进度展示为0；如果作业运行结束，则进度展示为1。此时progress表示整个作业的运行进度，因为没有子作业在运行，sub_job_id不展示。 （2）如果有子作业在运行中，则展示该子作业的运行进度，progress的计算方法为：子作业已经完成的task数除以子作业总的task数。此时progress表示子作业的运行进度，sub_job_id展示。

        :return: The progress of this ShowSqlJobProgressResponse.
        :rtype: float
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this ShowSqlJobProgressResponse.

        正在运行的子作业的进度或者整个作业进度，该值只能粗略的估算子作业进度，不表示作业的详细进度。有两方面的含义： （1）如果整个作业刚开始运行或者在提交中，则进度展示为0；如果作业运行结束，则进度展示为1。此时progress表示整个作业的运行进度，因为没有子作业在运行，sub_job_id不展示。 （2）如果有子作业在运行中，则展示该子作业的运行进度，progress的计算方法为：子作业已经完成的task数除以子作业总的task数。此时progress表示子作业的运行进度，sub_job_id展示。

        :param progress: The progress of this ShowSqlJobProgressResponse.
        :type progress: float
        """
        self._progress = progress

    @property
    def sub_jobs(self):
        """Gets the sub_jobs of this ShowSqlJobProgressResponse.

        正在运行作业的子作业的详细信息，一个作业可能包含多个子作业。

        :return: The sub_jobs of this ShowSqlJobProgressResponse.
        :rtype: list[:class:`huaweicloudsdkdli.v1.SubJobDatas`]
        """
        return self._sub_jobs

    @sub_jobs.setter
    def sub_jobs(self, sub_jobs):
        """Sets the sub_jobs of this ShowSqlJobProgressResponse.

        正在运行作业的子作业的详细信息，一个作业可能包含多个子作业。

        :param sub_jobs: The sub_jobs of this ShowSqlJobProgressResponse.
        :type sub_jobs: list[:class:`huaweicloudsdkdli.v1.SubJobDatas`]
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
        if not isinstance(other, ShowSqlJobProgressResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
