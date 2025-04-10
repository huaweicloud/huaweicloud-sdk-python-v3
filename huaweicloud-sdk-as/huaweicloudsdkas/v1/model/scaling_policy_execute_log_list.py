# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ScalingPolicyExecuteLogList:

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
        'failed_reason': 'str',
        'execute_type': 'str',
        'execute_time': 'str',
        'id': 'str',
        'tenant_id': 'str',
        'scaling_policy_id': 'str',
        'scaling_resource_type': 'str',
        'scaling_resource_id': 'str',
        'old_value': 'str',
        'desire_value': 'str',
        'limit_value': 'str',
        'type': 'str',
        'job_records': 'list[JobRecords]',
        'meta_data': 'EipMetaData'
    }

    attribute_map = {
        'status': 'status',
        'failed_reason': 'failed_reason',
        'execute_type': 'execute_type',
        'execute_time': 'execute_time',
        'id': 'id',
        'tenant_id': 'tenant_id',
        'scaling_policy_id': 'scaling_policy_id',
        'scaling_resource_type': 'scaling_resource_type',
        'scaling_resource_id': 'scaling_resource_id',
        'old_value': 'old_value',
        'desire_value': 'desire_value',
        'limit_value': 'limit_value',
        'type': 'type',
        'job_records': 'job_records',
        'meta_data': 'meta_data'
    }

    def __init__(self, status=None, failed_reason=None, execute_type=None, execute_time=None, id=None, tenant_id=None, scaling_policy_id=None, scaling_resource_type=None, scaling_resource_id=None, old_value=None, desire_value=None, limit_value=None, type=None, job_records=None, meta_data=None):
        r"""ScalingPolicyExecuteLogList

        The model defined in huaweicloud sdk

        :param status: 策略执行状态：SUCCESS：成功。FAIL：失败。EXECUTING：执行中
        :type status: str
        :param failed_reason: 策略执行失败原因。
        :type failed_reason: str
        :param execute_type: 策略执行类型：SCHEDULE：自动触发（定时）。RECURRENCE：自动触发（周期）。ALARM：自动警告（告警）。MANUAL：手动触发
        :type execute_type: str
        :param execute_time: 策略执行时间，遵循UTC时间。
        :type execute_time: str
        :param id: 策略执行日志ID。
        :type id: str
        :param tenant_id: 租户id。
        :type tenant_id: str
        :param scaling_policy_id: 伸缩策略ID。
        :type scaling_policy_id: str
        :param scaling_resource_type: 伸缩资源类型：伸缩组：SCALING_GROUP 带宽：BANDWIDTH
        :type scaling_resource_type: str
        :param scaling_resource_id: 伸缩资源ID。
        :type scaling_resource_id: str
        :param old_value: 伸缩原始值。
        :type old_value: str
        :param desire_value: 伸缩目标值。
        :type desire_value: str
        :param limit_value: 操作限制。当scaling_resource_type为BANDWIDTH时，且operation不为SET时，limit_value生效，单位为Mbit/s。此时，当operation为ADD时，limit_value表示最高带宽限制；当operation为REDUCE时，limit_value表示最低带宽限制。
        :type limit_value: str
        :param type: 策略执行任务类型。ADD：添加。REMOVE：减少。SET：设置为
        :type type: str
        :param job_records: 策略执行动作包含的具体任务
        :type job_records: list[:class:`huaweicloudsdkas.v1.JobRecords`]
        :param meta_data: 
        :type meta_data: :class:`huaweicloudsdkas.v1.EipMetaData`
        """
        
        

        self._status = None
        self._failed_reason = None
        self._execute_type = None
        self._execute_time = None
        self._id = None
        self._tenant_id = None
        self._scaling_policy_id = None
        self._scaling_resource_type = None
        self._scaling_resource_id = None
        self._old_value = None
        self._desire_value = None
        self._limit_value = None
        self._type = None
        self._job_records = None
        self._meta_data = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if failed_reason is not None:
            self.failed_reason = failed_reason
        if execute_type is not None:
            self.execute_type = execute_type
        if execute_time is not None:
            self.execute_time = execute_time
        if id is not None:
            self.id = id
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if scaling_policy_id is not None:
            self.scaling_policy_id = scaling_policy_id
        if scaling_resource_type is not None:
            self.scaling_resource_type = scaling_resource_type
        if scaling_resource_id is not None:
            self.scaling_resource_id = scaling_resource_id
        if old_value is not None:
            self.old_value = old_value
        if desire_value is not None:
            self.desire_value = desire_value
        if limit_value is not None:
            self.limit_value = limit_value
        if type is not None:
            self.type = type
        if job_records is not None:
            self.job_records = job_records
        if meta_data is not None:
            self.meta_data = meta_data

    @property
    def status(self):
        r"""Gets the status of this ScalingPolicyExecuteLogList.

        策略执行状态：SUCCESS：成功。FAIL：失败。EXECUTING：执行中

        :return: The status of this ScalingPolicyExecuteLogList.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ScalingPolicyExecuteLogList.

        策略执行状态：SUCCESS：成功。FAIL：失败。EXECUTING：执行中

        :param status: The status of this ScalingPolicyExecuteLogList.
        :type status: str
        """
        self._status = status

    @property
    def failed_reason(self):
        r"""Gets the failed_reason of this ScalingPolicyExecuteLogList.

        策略执行失败原因。

        :return: The failed_reason of this ScalingPolicyExecuteLogList.
        :rtype: str
        """
        return self._failed_reason

    @failed_reason.setter
    def failed_reason(self, failed_reason):
        r"""Sets the failed_reason of this ScalingPolicyExecuteLogList.

        策略执行失败原因。

        :param failed_reason: The failed_reason of this ScalingPolicyExecuteLogList.
        :type failed_reason: str
        """
        self._failed_reason = failed_reason

    @property
    def execute_type(self):
        r"""Gets the execute_type of this ScalingPolicyExecuteLogList.

        策略执行类型：SCHEDULE：自动触发（定时）。RECURRENCE：自动触发（周期）。ALARM：自动警告（告警）。MANUAL：手动触发

        :return: The execute_type of this ScalingPolicyExecuteLogList.
        :rtype: str
        """
        return self._execute_type

    @execute_type.setter
    def execute_type(self, execute_type):
        r"""Sets the execute_type of this ScalingPolicyExecuteLogList.

        策略执行类型：SCHEDULE：自动触发（定时）。RECURRENCE：自动触发（周期）。ALARM：自动警告（告警）。MANUAL：手动触发

        :param execute_type: The execute_type of this ScalingPolicyExecuteLogList.
        :type execute_type: str
        """
        self._execute_type = execute_type

    @property
    def execute_time(self):
        r"""Gets the execute_time of this ScalingPolicyExecuteLogList.

        策略执行时间，遵循UTC时间。

        :return: The execute_time of this ScalingPolicyExecuteLogList.
        :rtype: str
        """
        return self._execute_time

    @execute_time.setter
    def execute_time(self, execute_time):
        r"""Sets the execute_time of this ScalingPolicyExecuteLogList.

        策略执行时间，遵循UTC时间。

        :param execute_time: The execute_time of this ScalingPolicyExecuteLogList.
        :type execute_time: str
        """
        self._execute_time = execute_time

    @property
    def id(self):
        r"""Gets the id of this ScalingPolicyExecuteLogList.

        策略执行日志ID。

        :return: The id of this ScalingPolicyExecuteLogList.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ScalingPolicyExecuteLogList.

        策略执行日志ID。

        :param id: The id of this ScalingPolicyExecuteLogList.
        :type id: str
        """
        self._id = id

    @property
    def tenant_id(self):
        r"""Gets the tenant_id of this ScalingPolicyExecuteLogList.

        租户id。

        :return: The tenant_id of this ScalingPolicyExecuteLogList.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        r"""Sets the tenant_id of this ScalingPolicyExecuteLogList.

        租户id。

        :param tenant_id: The tenant_id of this ScalingPolicyExecuteLogList.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def scaling_policy_id(self):
        r"""Gets the scaling_policy_id of this ScalingPolicyExecuteLogList.

        伸缩策略ID。

        :return: The scaling_policy_id of this ScalingPolicyExecuteLogList.
        :rtype: str
        """
        return self._scaling_policy_id

    @scaling_policy_id.setter
    def scaling_policy_id(self, scaling_policy_id):
        r"""Sets the scaling_policy_id of this ScalingPolicyExecuteLogList.

        伸缩策略ID。

        :param scaling_policy_id: The scaling_policy_id of this ScalingPolicyExecuteLogList.
        :type scaling_policy_id: str
        """
        self._scaling_policy_id = scaling_policy_id

    @property
    def scaling_resource_type(self):
        r"""Gets the scaling_resource_type of this ScalingPolicyExecuteLogList.

        伸缩资源类型：伸缩组：SCALING_GROUP 带宽：BANDWIDTH

        :return: The scaling_resource_type of this ScalingPolicyExecuteLogList.
        :rtype: str
        """
        return self._scaling_resource_type

    @scaling_resource_type.setter
    def scaling_resource_type(self, scaling_resource_type):
        r"""Sets the scaling_resource_type of this ScalingPolicyExecuteLogList.

        伸缩资源类型：伸缩组：SCALING_GROUP 带宽：BANDWIDTH

        :param scaling_resource_type: The scaling_resource_type of this ScalingPolicyExecuteLogList.
        :type scaling_resource_type: str
        """
        self._scaling_resource_type = scaling_resource_type

    @property
    def scaling_resource_id(self):
        r"""Gets the scaling_resource_id of this ScalingPolicyExecuteLogList.

        伸缩资源ID。

        :return: The scaling_resource_id of this ScalingPolicyExecuteLogList.
        :rtype: str
        """
        return self._scaling_resource_id

    @scaling_resource_id.setter
    def scaling_resource_id(self, scaling_resource_id):
        r"""Sets the scaling_resource_id of this ScalingPolicyExecuteLogList.

        伸缩资源ID。

        :param scaling_resource_id: The scaling_resource_id of this ScalingPolicyExecuteLogList.
        :type scaling_resource_id: str
        """
        self._scaling_resource_id = scaling_resource_id

    @property
    def old_value(self):
        r"""Gets the old_value of this ScalingPolicyExecuteLogList.

        伸缩原始值。

        :return: The old_value of this ScalingPolicyExecuteLogList.
        :rtype: str
        """
        return self._old_value

    @old_value.setter
    def old_value(self, old_value):
        r"""Sets the old_value of this ScalingPolicyExecuteLogList.

        伸缩原始值。

        :param old_value: The old_value of this ScalingPolicyExecuteLogList.
        :type old_value: str
        """
        self._old_value = old_value

    @property
    def desire_value(self):
        r"""Gets the desire_value of this ScalingPolicyExecuteLogList.

        伸缩目标值。

        :return: The desire_value of this ScalingPolicyExecuteLogList.
        :rtype: str
        """
        return self._desire_value

    @desire_value.setter
    def desire_value(self, desire_value):
        r"""Sets the desire_value of this ScalingPolicyExecuteLogList.

        伸缩目标值。

        :param desire_value: The desire_value of this ScalingPolicyExecuteLogList.
        :type desire_value: str
        """
        self._desire_value = desire_value

    @property
    def limit_value(self):
        r"""Gets the limit_value of this ScalingPolicyExecuteLogList.

        操作限制。当scaling_resource_type为BANDWIDTH时，且operation不为SET时，limit_value生效，单位为Mbit/s。此时，当operation为ADD时，limit_value表示最高带宽限制；当operation为REDUCE时，limit_value表示最低带宽限制。

        :return: The limit_value of this ScalingPolicyExecuteLogList.
        :rtype: str
        """
        return self._limit_value

    @limit_value.setter
    def limit_value(self, limit_value):
        r"""Sets the limit_value of this ScalingPolicyExecuteLogList.

        操作限制。当scaling_resource_type为BANDWIDTH时，且operation不为SET时，limit_value生效，单位为Mbit/s。此时，当operation为ADD时，limit_value表示最高带宽限制；当operation为REDUCE时，limit_value表示最低带宽限制。

        :param limit_value: The limit_value of this ScalingPolicyExecuteLogList.
        :type limit_value: str
        """
        self._limit_value = limit_value

    @property
    def type(self):
        r"""Gets the type of this ScalingPolicyExecuteLogList.

        策略执行任务类型。ADD：添加。REMOVE：减少。SET：设置为

        :return: The type of this ScalingPolicyExecuteLogList.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ScalingPolicyExecuteLogList.

        策略执行任务类型。ADD：添加。REMOVE：减少。SET：设置为

        :param type: The type of this ScalingPolicyExecuteLogList.
        :type type: str
        """
        self._type = type

    @property
    def job_records(self):
        r"""Gets the job_records of this ScalingPolicyExecuteLogList.

        策略执行动作包含的具体任务

        :return: The job_records of this ScalingPolicyExecuteLogList.
        :rtype: list[:class:`huaweicloudsdkas.v1.JobRecords`]
        """
        return self._job_records

    @job_records.setter
    def job_records(self, job_records):
        r"""Sets the job_records of this ScalingPolicyExecuteLogList.

        策略执行动作包含的具体任务

        :param job_records: The job_records of this ScalingPolicyExecuteLogList.
        :type job_records: list[:class:`huaweicloudsdkas.v1.JobRecords`]
        """
        self._job_records = job_records

    @property
    def meta_data(self):
        r"""Gets the meta_data of this ScalingPolicyExecuteLogList.

        :return: The meta_data of this ScalingPolicyExecuteLogList.
        :rtype: :class:`huaweicloudsdkas.v1.EipMetaData`
        """
        return self._meta_data

    @meta_data.setter
    def meta_data(self, meta_data):
        r"""Sets the meta_data of this ScalingPolicyExecuteLogList.

        :param meta_data: The meta_data of this ScalingPolicyExecuteLogList.
        :type meta_data: :class:`huaweicloudsdkas.v1.EipMetaData`
        """
        self._meta_data = meta_data

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
        if not isinstance(other, ScalingPolicyExecuteLogList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
