# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobData:

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
        'name': 'str',
        'create_time': 'str',
        'end_time': 'str',
        'progress': 'str',
        'store_name': 'str',
        'fail_reason': 'str'
    }

    attribute_map = {
        'job_id': 'job_id',
        'status': 'status',
        'name': 'name',
        'create_time': 'create_time',
        'end_time': 'end_time',
        'progress': 'progress',
        'store_name': 'store_name',
        'fail_reason': 'fail_reason'
    }

    def __init__(self, job_id=None, status=None, name=None, create_time=None, end_time=None, progress=None, store_name=None, fail_reason=None):
        r"""JobData

        The model defined in huaweicloud sdk

        :param job_id: 任务ID。
        :type job_id: str
        :param status: 任务执行状态。取值：  值为“Running”，表示任务正在执行。 值为“Completed”，表示任务执行成功。 值为“Failed”，表示任务执行失败。
        :type status: str
        :param name: 任务名称
        :type name: str
        :param create_time: 创建时间，格式为“yyyy-mm-ddThh:mm:ssZ”。
        :type create_time: str
        :param end_time: 结束时间，格式为“yyyy-mm-ddThh:mm:ssZ”。
        :type end_time: str
        :param progress: 任务执行进度。运行中状态返回执行进度，例如“60%”，表示任务执行进度为60%。
        :type progress: str
        :param store_name: 知识仓实例名称
        :type store_name: str
        :param fail_reason: 任务执行失败时的错误信息。
        :type fail_reason: str
        """
        
        

        self._job_id = None
        self._status = None
        self._name = None
        self._create_time = None
        self._end_time = None
        self._progress = None
        self._store_name = None
        self._fail_reason = None
        self.discriminator = None

        self.job_id = job_id
        self.status = status
        if name is not None:
            self.name = name
        if create_time is not None:
            self.create_time = create_time
        if end_time is not None:
            self.end_time = end_time
        if progress is not None:
            self.progress = progress
        if store_name is not None:
            self.store_name = store_name
        if fail_reason is not None:
            self.fail_reason = fail_reason

    @property
    def job_id(self):
        r"""Gets the job_id of this JobData.

        任务ID。

        :return: The job_id of this JobData.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this JobData.

        任务ID。

        :param job_id: The job_id of this JobData.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def status(self):
        r"""Gets the status of this JobData.

        任务执行状态。取值：  值为“Running”，表示任务正在执行。 值为“Completed”，表示任务执行成功。 值为“Failed”，表示任务执行失败。

        :return: The status of this JobData.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this JobData.

        任务执行状态。取值：  值为“Running”，表示任务正在执行。 值为“Completed”，表示任务执行成功。 值为“Failed”，表示任务执行失败。

        :param status: The status of this JobData.
        :type status: str
        """
        self._status = status

    @property
    def name(self):
        r"""Gets the name of this JobData.

        任务名称

        :return: The name of this JobData.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this JobData.

        任务名称

        :param name: The name of this JobData.
        :type name: str
        """
        self._name = name

    @property
    def create_time(self):
        r"""Gets the create_time of this JobData.

        创建时间，格式为“yyyy-mm-ddThh:mm:ssZ”。

        :return: The create_time of this JobData.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this JobData.

        创建时间，格式为“yyyy-mm-ddThh:mm:ssZ”。

        :param create_time: The create_time of this JobData.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def end_time(self):
        r"""Gets the end_time of this JobData.

        结束时间，格式为“yyyy-mm-ddThh:mm:ssZ”。

        :return: The end_time of this JobData.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this JobData.

        结束时间，格式为“yyyy-mm-ddThh:mm:ssZ”。

        :param end_time: The end_time of this JobData.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def progress(self):
        r"""Gets the progress of this JobData.

        任务执行进度。运行中状态返回执行进度，例如“60%”，表示任务执行进度为60%。

        :return: The progress of this JobData.
        :rtype: str
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        r"""Sets the progress of this JobData.

        任务执行进度。运行中状态返回执行进度，例如“60%”，表示任务执行进度为60%。

        :param progress: The progress of this JobData.
        :type progress: str
        """
        self._progress = progress

    @property
    def store_name(self):
        r"""Gets the store_name of this JobData.

        知识仓实例名称

        :return: The store_name of this JobData.
        :rtype: str
        """
        return self._store_name

    @store_name.setter
    def store_name(self, store_name):
        r"""Sets the store_name of this JobData.

        知识仓实例名称

        :param store_name: The store_name of this JobData.
        :type store_name: str
        """
        self._store_name = store_name

    @property
    def fail_reason(self):
        r"""Gets the fail_reason of this JobData.

        任务执行失败时的错误信息。

        :return: The fail_reason of this JobData.
        :rtype: str
        """
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, fail_reason):
        r"""Sets the fail_reason of this JobData.

        任务执行失败时的错误信息。

        :param fail_reason: The fail_reason of this JobData.
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
        if not isinstance(other, JobData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
