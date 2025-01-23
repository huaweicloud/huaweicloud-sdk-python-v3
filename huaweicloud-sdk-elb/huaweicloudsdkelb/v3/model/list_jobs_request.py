# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListJobsRequest:

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
        'job_type': 'str',
        'status': 'str',
        'error_code': 'str',
        'resource_id': 'str',
        'begin_time': 'str'
    }

    attribute_map = {
        'job_id': 'job_id',
        'job_type': 'job_type',
        'status': 'status',
        'error_code': 'error_code',
        'resource_id': 'resource_id',
        'begin_time': 'begin_time'
    }

    def __init__(self, job_id=None, job_type=None, status=None, error_code=None, resource_id=None, begin_time=None):
        """ListJobsRequest

        The model defined in huaweicloud sdk

        :param job_id: 参数解释：任务ID。
        :type job_id: str
        :param job_type: 参数解释：任务类型。
        :type job_type: str
        :param status: 参数解释：任务状态。  取值范围：INIT,RUNNING,FAIL,SUCCESS,ROLLBACKING,COMPLETE,ROLLBACK_FAIL,CANCEL
        :type status: str
        :param error_code: 参数解释： 任务的错误码。
        :type error_code: str
        :param resource_id: 参数解释：资源ID。
        :type resource_id: str
        :param begin_time: 参数解释：查询任务的开始时间大于等于传入时间的任务。格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss
        :type begin_time: str
        """
        
        

        self._job_id = None
        self._job_type = None
        self._status = None
        self._error_code = None
        self._resource_id = None
        self._begin_time = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if job_type is not None:
            self.job_type = job_type
        if status is not None:
            self.status = status
        if error_code is not None:
            self.error_code = error_code
        if resource_id is not None:
            self.resource_id = resource_id
        if begin_time is not None:
            self.begin_time = begin_time

    @property
    def job_id(self):
        """Gets the job_id of this ListJobsRequest.

        参数解释：任务ID。

        :return: The job_id of this ListJobsRequest.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this ListJobsRequest.

        参数解释：任务ID。

        :param job_id: The job_id of this ListJobsRequest.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def job_type(self):
        """Gets the job_type of this ListJobsRequest.

        参数解释：任务类型。

        :return: The job_type of this ListJobsRequest.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        """Sets the job_type of this ListJobsRequest.

        参数解释：任务类型。

        :param job_type: The job_type of this ListJobsRequest.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def status(self):
        """Gets the status of this ListJobsRequest.

        参数解释：任务状态。  取值范围：INIT,RUNNING,FAIL,SUCCESS,ROLLBACKING,COMPLETE,ROLLBACK_FAIL,CANCEL

        :return: The status of this ListJobsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListJobsRequest.

        参数解释：任务状态。  取值范围：INIT,RUNNING,FAIL,SUCCESS,ROLLBACKING,COMPLETE,ROLLBACK_FAIL,CANCEL

        :param status: The status of this ListJobsRequest.
        :type status: str
        """
        self._status = status

    @property
    def error_code(self):
        """Gets the error_code of this ListJobsRequest.

        参数解释： 任务的错误码。

        :return: The error_code of this ListJobsRequest.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this ListJobsRequest.

        参数解释： 任务的错误码。

        :param error_code: The error_code of this ListJobsRequest.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def resource_id(self):
        """Gets the resource_id of this ListJobsRequest.

        参数解释：资源ID。

        :return: The resource_id of this ListJobsRequest.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this ListJobsRequest.

        参数解释：资源ID。

        :param resource_id: The resource_id of this ListJobsRequest.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def begin_time(self):
        """Gets the begin_time of this ListJobsRequest.

        参数解释：查询任务的开始时间大于等于传入时间的任务。格式：yyyy-MM-dd'T'HH:mm:ss

        :return: The begin_time of this ListJobsRequest.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        """Sets the begin_time of this ListJobsRequest.

        参数解释：查询任务的开始时间大于等于传入时间的任务。格式：yyyy-MM-dd'T'HH:mm:ss

        :param begin_time: The begin_time of this ListJobsRequest.
        :type begin_time: str
        """
        self._begin_time = begin_time

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
        if not isinstance(other, ListJobsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
