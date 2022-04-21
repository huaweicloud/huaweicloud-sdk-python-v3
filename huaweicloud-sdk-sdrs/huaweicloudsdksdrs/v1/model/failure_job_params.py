# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FailureJobParams:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'job_type': 'str',
        'job_status': 'str',
        'begin_time': 'str',
        'job_id': 'str',
        'failure_status': 'str',
        'resource_id': 'str',
        'resource_name': 'str',
        'error_code': 'str',
        'fail_reason': 'str',
        'resource_type': 'str'
    }

    attribute_map = {
        'job_type': 'job_type',
        'job_status': 'job_status',
        'begin_time': 'begin_time',
        'job_id': 'job_id',
        'failure_status': 'failure_status',
        'resource_id': 'resource_id',
        'resource_name': 'resource_name',
        'error_code': 'error_code',
        'fail_reason': 'fail_reason',
        'resource_type': 'resource_type'
    }

    def __init__(self, job_type=None, job_status=None, begin_time=None, job_id=None, failure_status=None, resource_id=None, resource_name=None, error_code=None, fail_reason=None, resource_type=None):
        """FailureJobParams

        The model defined in huaweicloud sdk

        :param job_type: 任务名称。
        :type job_type: str
        :param job_status: 任务状态。当前仅支持“FAIL”。FAIL：表示任务失败。
        :type job_status: str
        :param begin_time: 任务操作时间。默认格式为：\&quot;yyyy-MM-ddTHH:mm:ss.SSSZ\&quot;，例：\&quot;2019-04-01T12:00:00.000Z\&quot;。
        :type begin_time: str
        :param job_id: 任务id。执行异步API命令下发成功的返回参数。
        :type job_id: str
        :param failure_status: 失败任务状态。createFail：表示创建失败。deleteFail：表示删除失败。attachFail：表示挂载失败。detachFail：表示卸载失败。expandFail：表示扩容失败。resizeFail：表示变更规格失败。startFail：表示开启保护失败。stopFail：表示停止保护失败。reverseFail：表示切换失败。failoverFail：表示故障切换失败。reprotectFail : 表示重保护失败。
        :type failure_status: str
        :param resource_id: 资源ID。
        :type resource_id: str
        :param resource_name: 资源名称。
        :type resource_name: str
        :param error_code: 任务失败错误码。
        :type error_code: str
        :param fail_reason: 任务失败原因。
        :type fail_reason: str
        :param resource_type: 资源类型。 server_groups：表示保护组。 protected_instances：表示保护实例。 replications：表示复制对。 disaster_recovery_drills：表示容灾演练。
        :type resource_type: str
        """
        
        

        self._job_type = None
        self._job_status = None
        self._begin_time = None
        self._job_id = None
        self._failure_status = None
        self._resource_id = None
        self._resource_name = None
        self._error_code = None
        self._fail_reason = None
        self._resource_type = None
        self.discriminator = None

        self.job_type = job_type
        self.job_status = job_status
        self.begin_time = begin_time
        self.job_id = job_id
        self.failure_status = failure_status
        self.resource_id = resource_id
        self.resource_name = resource_name
        self.error_code = error_code
        self.fail_reason = fail_reason
        self.resource_type = resource_type

    @property
    def job_type(self):
        """Gets the job_type of this FailureJobParams.

        任务名称。

        :return: The job_type of this FailureJobParams.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        """Sets the job_type of this FailureJobParams.

        任务名称。

        :param job_type: The job_type of this FailureJobParams.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def job_status(self):
        """Gets the job_status of this FailureJobParams.

        任务状态。当前仅支持“FAIL”。FAIL：表示任务失败。

        :return: The job_status of this FailureJobParams.
        :rtype: str
        """
        return self._job_status

    @job_status.setter
    def job_status(self, job_status):
        """Sets the job_status of this FailureJobParams.

        任务状态。当前仅支持“FAIL”。FAIL：表示任务失败。

        :param job_status: The job_status of this FailureJobParams.
        :type job_status: str
        """
        self._job_status = job_status

    @property
    def begin_time(self):
        """Gets the begin_time of this FailureJobParams.

        任务操作时间。默认格式为：\"yyyy-MM-ddTHH:mm:ss.SSSZ\"，例：\"2019-04-01T12:00:00.000Z\"。

        :return: The begin_time of this FailureJobParams.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        """Sets the begin_time of this FailureJobParams.

        任务操作时间。默认格式为：\"yyyy-MM-ddTHH:mm:ss.SSSZ\"，例：\"2019-04-01T12:00:00.000Z\"。

        :param begin_time: The begin_time of this FailureJobParams.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def job_id(self):
        """Gets the job_id of this FailureJobParams.

        任务id。执行异步API命令下发成功的返回参数。

        :return: The job_id of this FailureJobParams.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this FailureJobParams.

        任务id。执行异步API命令下发成功的返回参数。

        :param job_id: The job_id of this FailureJobParams.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def failure_status(self):
        """Gets the failure_status of this FailureJobParams.

        失败任务状态。createFail：表示创建失败。deleteFail：表示删除失败。attachFail：表示挂载失败。detachFail：表示卸载失败。expandFail：表示扩容失败。resizeFail：表示变更规格失败。startFail：表示开启保护失败。stopFail：表示停止保护失败。reverseFail：表示切换失败。failoverFail：表示故障切换失败。reprotectFail : 表示重保护失败。

        :return: The failure_status of this FailureJobParams.
        :rtype: str
        """
        return self._failure_status

    @failure_status.setter
    def failure_status(self, failure_status):
        """Sets the failure_status of this FailureJobParams.

        失败任务状态。createFail：表示创建失败。deleteFail：表示删除失败。attachFail：表示挂载失败。detachFail：表示卸载失败。expandFail：表示扩容失败。resizeFail：表示变更规格失败。startFail：表示开启保护失败。stopFail：表示停止保护失败。reverseFail：表示切换失败。failoverFail：表示故障切换失败。reprotectFail : 表示重保护失败。

        :param failure_status: The failure_status of this FailureJobParams.
        :type failure_status: str
        """
        self._failure_status = failure_status

    @property
    def resource_id(self):
        """Gets the resource_id of this FailureJobParams.

        资源ID。

        :return: The resource_id of this FailureJobParams.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this FailureJobParams.

        资源ID。

        :param resource_id: The resource_id of this FailureJobParams.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_name(self):
        """Gets the resource_name of this FailureJobParams.

        资源名称。

        :return: The resource_name of this FailureJobParams.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """Sets the resource_name of this FailureJobParams.

        资源名称。

        :param resource_name: The resource_name of this FailureJobParams.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def error_code(self):
        """Gets the error_code of this FailureJobParams.

        任务失败错误码。

        :return: The error_code of this FailureJobParams.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this FailureJobParams.

        任务失败错误码。

        :param error_code: The error_code of this FailureJobParams.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def fail_reason(self):
        """Gets the fail_reason of this FailureJobParams.

        任务失败原因。

        :return: The fail_reason of this FailureJobParams.
        :rtype: str
        """
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, fail_reason):
        """Sets the fail_reason of this FailureJobParams.

        任务失败原因。

        :param fail_reason: The fail_reason of this FailureJobParams.
        :type fail_reason: str
        """
        self._fail_reason = fail_reason

    @property
    def resource_type(self):
        """Gets the resource_type of this FailureJobParams.

        资源类型。 server_groups：表示保护组。 protected_instances：表示保护实例。 replications：表示复制对。 disaster_recovery_drills：表示容灾演练。

        :return: The resource_type of this FailureJobParams.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this FailureJobParams.

        资源类型。 server_groups：表示保护组。 protected_instances：表示保护实例。 replications：表示复制对。 disaster_recovery_drills：表示容灾演练。

        :param resource_type: The resource_type of this FailureJobParams.
        :type resource_type: str
        """
        self._resource_type = resource_type

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
        if not isinstance(other, FailureJobParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
