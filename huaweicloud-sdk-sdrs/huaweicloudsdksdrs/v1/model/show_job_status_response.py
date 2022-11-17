# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowJobStatusResponse(SdkResponse):

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
        'entities': 'JobEntities',
        'job_id': 'str',
        'job_type': 'str',
        'begin_time': 'str',
        'end_time': 'str',
        'error_code': 'str',
        'fail_reason': 'str'
    }

    attribute_map = {
        'status': 'status',
        'entities': 'entities',
        'job_id': 'job_id',
        'job_type': 'job_type',
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'error_code': 'error_code',
        'fail_reason': 'fail_reason'
    }

    def __init__(self, status=None, entities=None, job_id=None, job_type=None, begin_time=None, end_time=None, error_code=None, fail_reason=None):
        """ShowJobStatusResponse

        The model defined in huaweicloud sdk

        :param status: Job的状态。 SUCCESS：成功。 RUNNING：运行中。 FAIL：失败。 INIT：正在初始化。
        :type status: str
        :param entities: 
        :type entities: :class:`huaweicloudsdksdrs.v1.JobEntities`
        :param job_id: Job ID。
        :type job_id: str
        :param job_type: Job的类型。createProtectionGroupNoCG：创建保护组。deleteProtectionGroupNoCG：删除保护组。startProtectionGroupNoCG ：保护组开始保护。reprotectProtectionGroupNoCG ：保护组重保护。stopProtectionGroupNoCG ：保护组停止保护。failoverProtectionGroupNoCG  ：保护组故障切换。reverseProtectionGroupNoCG：保护组切换。createProtectedInstanceNoCG：创建保护实例。deleteProtectedInstanceNoCG：删除保护实例。attachReplicationPairNew：保护实例挂载复制对。detachReplicationPairNew：保护实例卸载复制对。addNicNew：保护实例添加网卡。deleteNicNew：保护实例删除网卡。resizeProtectedInstanceNew：保护实例变更规格。createReplicationPairNoCG：创建复制对。deleteReplicationPairNoCG：删除复制对。expandReplicationPairNew：复制对扩容。createDisasterRecoveryDrill：创建容灾演练。deleteDisasterRecoveryDrill：删除容灾演练。
        :type job_type: str
        :param begin_time: 开始时间。默认格式为：\&quot;yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ\&quot;，例：\&quot;2019-04-01T12:00:00.000Z\&quot;。
        :type begin_time: str
        :param end_time: 结束时间。默认格式为：\&quot;yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ\&quot;，例：\&quot;2019-04-01T12:00:00.000Z\&quot;。
        :type end_time: str
        :param error_code: Job执行失败时的错误码。
        :type error_code: str
        :param fail_reason: Job执行失败时的错误原因。
        :type fail_reason: str
        """
        
        super(ShowJobStatusResponse, self).__init__()

        self._status = None
        self._entities = None
        self._job_id = None
        self._job_type = None
        self._begin_time = None
        self._end_time = None
        self._error_code = None
        self._fail_reason = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if entities is not None:
            self.entities = entities
        if job_id is not None:
            self.job_id = job_id
        if job_type is not None:
            self.job_type = job_type
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time
        if error_code is not None:
            self.error_code = error_code
        if fail_reason is not None:
            self.fail_reason = fail_reason

    @property
    def status(self):
        """Gets the status of this ShowJobStatusResponse.

        Job的状态。 SUCCESS：成功。 RUNNING：运行中。 FAIL：失败。 INIT：正在初始化。

        :return: The status of this ShowJobStatusResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowJobStatusResponse.

        Job的状态。 SUCCESS：成功。 RUNNING：运行中。 FAIL：失败。 INIT：正在初始化。

        :param status: The status of this ShowJobStatusResponse.
        :type status: str
        """
        self._status = status

    @property
    def entities(self):
        """Gets the entities of this ShowJobStatusResponse.

        :return: The entities of this ShowJobStatusResponse.
        :rtype: :class:`huaweicloudsdksdrs.v1.JobEntities`
        """
        return self._entities

    @entities.setter
    def entities(self, entities):
        """Sets the entities of this ShowJobStatusResponse.

        :param entities: The entities of this ShowJobStatusResponse.
        :type entities: :class:`huaweicloudsdksdrs.v1.JobEntities`
        """
        self._entities = entities

    @property
    def job_id(self):
        """Gets the job_id of this ShowJobStatusResponse.

        Job ID。

        :return: The job_id of this ShowJobStatusResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this ShowJobStatusResponse.

        Job ID。

        :param job_id: The job_id of this ShowJobStatusResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def job_type(self):
        """Gets the job_type of this ShowJobStatusResponse.

        Job的类型。createProtectionGroupNoCG：创建保护组。deleteProtectionGroupNoCG：删除保护组。startProtectionGroupNoCG ：保护组开始保护。reprotectProtectionGroupNoCG ：保护组重保护。stopProtectionGroupNoCG ：保护组停止保护。failoverProtectionGroupNoCG  ：保护组故障切换。reverseProtectionGroupNoCG：保护组切换。createProtectedInstanceNoCG：创建保护实例。deleteProtectedInstanceNoCG：删除保护实例。attachReplicationPairNew：保护实例挂载复制对。detachReplicationPairNew：保护实例卸载复制对。addNicNew：保护实例添加网卡。deleteNicNew：保护实例删除网卡。resizeProtectedInstanceNew：保护实例变更规格。createReplicationPairNoCG：创建复制对。deleteReplicationPairNoCG：删除复制对。expandReplicationPairNew：复制对扩容。createDisasterRecoveryDrill：创建容灾演练。deleteDisasterRecoveryDrill：删除容灾演练。

        :return: The job_type of this ShowJobStatusResponse.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        """Sets the job_type of this ShowJobStatusResponse.

        Job的类型。createProtectionGroupNoCG：创建保护组。deleteProtectionGroupNoCG：删除保护组。startProtectionGroupNoCG ：保护组开始保护。reprotectProtectionGroupNoCG ：保护组重保护。stopProtectionGroupNoCG ：保护组停止保护。failoverProtectionGroupNoCG  ：保护组故障切换。reverseProtectionGroupNoCG：保护组切换。createProtectedInstanceNoCG：创建保护实例。deleteProtectedInstanceNoCG：删除保护实例。attachReplicationPairNew：保护实例挂载复制对。detachReplicationPairNew：保护实例卸载复制对。addNicNew：保护实例添加网卡。deleteNicNew：保护实例删除网卡。resizeProtectedInstanceNew：保护实例变更规格。createReplicationPairNoCG：创建复制对。deleteReplicationPairNoCG：删除复制对。expandReplicationPairNew：复制对扩容。createDisasterRecoveryDrill：创建容灾演练。deleteDisasterRecoveryDrill：删除容灾演练。

        :param job_type: The job_type of this ShowJobStatusResponse.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def begin_time(self):
        """Gets the begin_time of this ShowJobStatusResponse.

        开始时间。默认格式为：\"yyyy-MM-dd'T'HH:mm:ss.SSSZ\"，例：\"2019-04-01T12:00:00.000Z\"。

        :return: The begin_time of this ShowJobStatusResponse.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        """Sets the begin_time of this ShowJobStatusResponse.

        开始时间。默认格式为：\"yyyy-MM-dd'T'HH:mm:ss.SSSZ\"，例：\"2019-04-01T12:00:00.000Z\"。

        :param begin_time: The begin_time of this ShowJobStatusResponse.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        """Gets the end_time of this ShowJobStatusResponse.

        结束时间。默认格式为：\"yyyy-MM-dd'T'HH:mm:ss.SSSZ\"，例：\"2019-04-01T12:00:00.000Z\"。

        :return: The end_time of this ShowJobStatusResponse.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ShowJobStatusResponse.

        结束时间。默认格式为：\"yyyy-MM-dd'T'HH:mm:ss.SSSZ\"，例：\"2019-04-01T12:00:00.000Z\"。

        :param end_time: The end_time of this ShowJobStatusResponse.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def error_code(self):
        """Gets the error_code of this ShowJobStatusResponse.

        Job执行失败时的错误码。

        :return: The error_code of this ShowJobStatusResponse.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this ShowJobStatusResponse.

        Job执行失败时的错误码。

        :param error_code: The error_code of this ShowJobStatusResponse.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def fail_reason(self):
        """Gets the fail_reason of this ShowJobStatusResponse.

        Job执行失败时的错误原因。

        :return: The fail_reason of this ShowJobStatusResponse.
        :rtype: str
        """
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, fail_reason):
        """Sets the fail_reason of this ShowJobStatusResponse.

        Job执行失败时的错误原因。

        :param fail_reason: The fail_reason of this ShowJobStatusResponse.
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
        if not isinstance(other, ShowJobStatusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
