# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CountSubJobsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'job_type': 'str',
        'job_id': 'str'
    }

    attribute_map = {
        'status': 'status',
        'job_type': 'job_type',
        'job_id': 'job_id'
    }

    def __init__(self, status=None, job_type=None, job_id=None):
        r"""CountSubJobsRequest

        The model defined in huaweicloud sdk

        :param status: job详情的状态： * &#x60;WAITING&#x60; - 等待 * &#x60;RUNNING&#x60; - 运行中 * &#x60;SUCCESS&#x60; - 成功 * &#x60;FAILED&#x60; - 失败 * &#x60;ABNORMAL&#x60; - 异常 * &#x60;ROLLBACK&#x60; - 回滚中 * &#x60;ABORTING&#x60; - 取消
        :type status: str
        :param job_type: 任务类型，传入多个任务类型的时候将任务类型用英文逗号(,)进行分隔。
        :type job_type: str
        :param job_id: 任务ID。
        :type job_id: str
        """
        
        

        self._status = None
        self._job_type = None
        self._job_id = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if job_type is not None:
            self.job_type = job_type
        if job_id is not None:
            self.job_id = job_id

    @property
    def status(self):
        r"""Gets the status of this CountSubJobsRequest.

        job详情的状态： * `WAITING` - 等待 * `RUNNING` - 运行中 * `SUCCESS` - 成功 * `FAILED` - 失败 * `ABNORMAL` - 异常 * `ROLLBACK` - 回滚中 * `ABORTING` - 取消

        :return: The status of this CountSubJobsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CountSubJobsRequest.

        job详情的状态： * `WAITING` - 等待 * `RUNNING` - 运行中 * `SUCCESS` - 成功 * `FAILED` - 失败 * `ABNORMAL` - 异常 * `ROLLBACK` - 回滚中 * `ABORTING` - 取消

        :param status: The status of this CountSubJobsRequest.
        :type status: str
        """
        self._status = status

    @property
    def job_type(self):
        r"""Gets the job_type of this CountSubJobsRequest.

        任务类型，传入多个任务类型的时候将任务类型用英文逗号(,)进行分隔。

        :return: The job_type of this CountSubJobsRequest.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        r"""Sets the job_type of this CountSubJobsRequest.

        任务类型，传入多个任务类型的时候将任务类型用英文逗号(,)进行分隔。

        :param job_type: The job_type of this CountSubJobsRequest.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def job_id(self):
        r"""Gets the job_id of this CountSubJobsRequest.

        任务ID。

        :return: The job_id of this CountSubJobsRequest.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this CountSubJobsRequest.

        任务ID。

        :param job_id: The job_id of this CountSubJobsRequest.
        :type job_id: str
        """
        self._job_id = job_id

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
        if not isinstance(other, CountSubJobsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
