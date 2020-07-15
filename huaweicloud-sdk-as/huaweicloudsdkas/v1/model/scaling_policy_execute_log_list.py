# coding: utf-8

import pprint
import re

import six





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
        'execute_time': 'datetime',
        'id': 'str',
        'project_id': 'str',
        'scaling_policy_id': 'str',
        'scaling_resource_type': 'str',
        'scaling_resource_id': 'str',
        'old_value': 'str',
        'desire_value': 'str',
        'limit_value': 'int',
        'type': 'str',
        'job_records': 'list[JobRecords]',
        'meta_data': 'MetaData'
    }

    attribute_map = {
        'status': 'status',
        'failed_reason': 'failed_reason',
        'execute_type': 'execute_type',
        'execute_time': 'execute_time',
        'id': 'id',
        'project_id': 'project_id',
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

    def __init__(self, status=None, failed_reason=None, execute_type=None, execute_time=None, id=None, project_id=None, scaling_policy_id=None, scaling_resource_type=None, scaling_resource_id=None, old_value=None, desire_value=None, limit_value=None, type=None, job_records=None, meta_data=None):
        """ScalingPolicyExecuteLogList - a model defined in huaweicloud sdk"""
        
        

        self._status = None
        self._failed_reason = None
        self._execute_type = None
        self._execute_time = None
        self._id = None
        self._project_id = None
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
        if project_id is not None:
            self.project_id = project_id
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
        """Gets the status of this ScalingPolicyExecuteLogList.

        策略执行状态：SUCCESS：成功。FAIL：失败。EXECUTING：执行中

        :return: The status of this ScalingPolicyExecuteLogList.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ScalingPolicyExecuteLogList.

        策略执行状态：SUCCESS：成功。FAIL：失败。EXECUTING：执行中

        :param status: The status of this ScalingPolicyExecuteLogList.
        :type: str
        """
        self._status = status

    @property
    def failed_reason(self):
        """Gets the failed_reason of this ScalingPolicyExecuteLogList.

        策略执行失败原因。

        :return: The failed_reason of this ScalingPolicyExecuteLogList.
        :rtype: str
        """
        return self._failed_reason

    @failed_reason.setter
    def failed_reason(self, failed_reason):
        """Sets the failed_reason of this ScalingPolicyExecuteLogList.

        策略执行失败原因。

        :param failed_reason: The failed_reason of this ScalingPolicyExecuteLogList.
        :type: str
        """
        self._failed_reason = failed_reason

    @property
    def execute_type(self):
        """Gets the execute_type of this ScalingPolicyExecuteLogList.

        策略执行类型：SCHEDULE：自动触发（定时）。RECURRENCE：自动触发（周期）。ALARM：自动警告（告警）。MANUAL：手动触发

        :return: The execute_type of this ScalingPolicyExecuteLogList.
        :rtype: str
        """
        return self._execute_type

    @execute_type.setter
    def execute_type(self, execute_type):
        """Sets the execute_type of this ScalingPolicyExecuteLogList.

        策略执行类型：SCHEDULE：自动触发（定时）。RECURRENCE：自动触发（周期）。ALARM：自动警告（告警）。MANUAL：手动触发

        :param execute_type: The execute_type of this ScalingPolicyExecuteLogList.
        :type: str
        """
        self._execute_type = execute_type

    @property
    def execute_time(self):
        """Gets the execute_time of this ScalingPolicyExecuteLogList.

        策略执行时间，遵循UTC时间。

        :return: The execute_time of this ScalingPolicyExecuteLogList.
        :rtype: datetime
        """
        return self._execute_time

    @execute_time.setter
    def execute_time(self, execute_time):
        """Sets the execute_time of this ScalingPolicyExecuteLogList.

        策略执行时间，遵循UTC时间。

        :param execute_time: The execute_time of this ScalingPolicyExecuteLogList.
        :type: datetime
        """
        self._execute_time = execute_time

    @property
    def id(self):
        """Gets the id of this ScalingPolicyExecuteLogList.

        策略执行日志ID。

        :return: The id of this ScalingPolicyExecuteLogList.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ScalingPolicyExecuteLogList.

        策略执行日志ID。

        :param id: The id of this ScalingPolicyExecuteLogList.
        :type: str
        """
        self._id = id

    @property
    def project_id(self):
        """Gets the project_id of this ScalingPolicyExecuteLogList.

        租户id。

        :return: The project_id of this ScalingPolicyExecuteLogList.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ScalingPolicyExecuteLogList.

        租户id。

        :param project_id: The project_id of this ScalingPolicyExecuteLogList.
        :type: str
        """
        self._project_id = project_id

    @property
    def scaling_policy_id(self):
        """Gets the scaling_policy_id of this ScalingPolicyExecuteLogList.

        伸缩策略ID。

        :return: The scaling_policy_id of this ScalingPolicyExecuteLogList.
        :rtype: str
        """
        return self._scaling_policy_id

    @scaling_policy_id.setter
    def scaling_policy_id(self, scaling_policy_id):
        """Sets the scaling_policy_id of this ScalingPolicyExecuteLogList.

        伸缩策略ID。

        :param scaling_policy_id: The scaling_policy_id of this ScalingPolicyExecuteLogList.
        :type: str
        """
        self._scaling_policy_id = scaling_policy_id

    @property
    def scaling_resource_type(self):
        """Gets the scaling_resource_type of this ScalingPolicyExecuteLogList.

        伸缩资源类型：伸缩组：SCALING_GROUP 带宽：BANDWIDTH

        :return: The scaling_resource_type of this ScalingPolicyExecuteLogList.
        :rtype: str
        """
        return self._scaling_resource_type

    @scaling_resource_type.setter
    def scaling_resource_type(self, scaling_resource_type):
        """Sets the scaling_resource_type of this ScalingPolicyExecuteLogList.

        伸缩资源类型：伸缩组：SCALING_GROUP 带宽：BANDWIDTH

        :param scaling_resource_type: The scaling_resource_type of this ScalingPolicyExecuteLogList.
        :type: str
        """
        self._scaling_resource_type = scaling_resource_type

    @property
    def scaling_resource_id(self):
        """Gets the scaling_resource_id of this ScalingPolicyExecuteLogList.

        伸缩资源ID。

        :return: The scaling_resource_id of this ScalingPolicyExecuteLogList.
        :rtype: str
        """
        return self._scaling_resource_id

    @scaling_resource_id.setter
    def scaling_resource_id(self, scaling_resource_id):
        """Sets the scaling_resource_id of this ScalingPolicyExecuteLogList.

        伸缩资源ID。

        :param scaling_resource_id: The scaling_resource_id of this ScalingPolicyExecuteLogList.
        :type: str
        """
        self._scaling_resource_id = scaling_resource_id

    @property
    def old_value(self):
        """Gets the old_value of this ScalingPolicyExecuteLogList.

        伸缩原始值。

        :return: The old_value of this ScalingPolicyExecuteLogList.
        :rtype: str
        """
        return self._old_value

    @old_value.setter
    def old_value(self, old_value):
        """Sets the old_value of this ScalingPolicyExecuteLogList.

        伸缩原始值。

        :param old_value: The old_value of this ScalingPolicyExecuteLogList.
        :type: str
        """
        self._old_value = old_value

    @property
    def desire_value(self):
        """Gets the desire_value of this ScalingPolicyExecuteLogList.

        伸缩目标值。

        :return: The desire_value of this ScalingPolicyExecuteLogList.
        :rtype: str
        """
        return self._desire_value

    @desire_value.setter
    def desire_value(self, desire_value):
        """Sets the desire_value of this ScalingPolicyExecuteLogList.

        伸缩目标值。

        :param desire_value: The desire_value of this ScalingPolicyExecuteLogList.
        :type: str
        """
        self._desire_value = desire_value

    @property
    def limit_value(self):
        """Gets the limit_value of this ScalingPolicyExecuteLogList.

        操作限制。当scaling_resource_type为BANDWIDTH时，且operation不为SET时，limit_value生效，单位为Mbit/s。此时，当operation为ADD时，limit_value表示最高带宽限制；当operation为REDUCE时，limit_value表示最低带宽限制。

        :return: The limit_value of this ScalingPolicyExecuteLogList.
        :rtype: int
        """
        return self._limit_value

    @limit_value.setter
    def limit_value(self, limit_value):
        """Sets the limit_value of this ScalingPolicyExecuteLogList.

        操作限制。当scaling_resource_type为BANDWIDTH时，且operation不为SET时，limit_value生效，单位为Mbit/s。此时，当operation为ADD时，limit_value表示最高带宽限制；当operation为REDUCE时，limit_value表示最低带宽限制。

        :param limit_value: The limit_value of this ScalingPolicyExecuteLogList.
        :type: int
        """
        self._limit_value = limit_value

    @property
    def type(self):
        """Gets the type of this ScalingPolicyExecuteLogList.

        策略执行任务类型。ADD：添加。REMOVE：减少。SET：设置为

        :return: The type of this ScalingPolicyExecuteLogList.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ScalingPolicyExecuteLogList.

        策略执行任务类型。ADD：添加。REMOVE：减少。SET：设置为

        :param type: The type of this ScalingPolicyExecuteLogList.
        :type: str
        """
        self._type = type

    @property
    def job_records(self):
        """Gets the job_records of this ScalingPolicyExecuteLogList.

        策略执行动作包含的具体任务

        :return: The job_records of this ScalingPolicyExecuteLogList.
        :rtype: list[JobRecords]
        """
        return self._job_records

    @job_records.setter
    def job_records(self, job_records):
        """Sets the job_records of this ScalingPolicyExecuteLogList.

        策略执行动作包含的具体任务

        :param job_records: The job_records of this ScalingPolicyExecuteLogList.
        :type: list[JobRecords]
        """
        self._job_records = job_records

    @property
    def meta_data(self):
        """Gets the meta_data of this ScalingPolicyExecuteLogList.


        :return: The meta_data of this ScalingPolicyExecuteLogList.
        :rtype: MetaData
        """
        return self._meta_data

    @meta_data.setter
    def meta_data(self, meta_data):
        """Sets the meta_data of this ScalingPolicyExecuteLogList.


        :param meta_data: The meta_data of this ScalingPolicyExecuteLogList.
        :type: MetaData
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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ScalingPolicyExecuteLogList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
