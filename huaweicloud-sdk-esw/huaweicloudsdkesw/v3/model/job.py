# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Job:

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
        'name': 'str',
        'status': 'str',
        'begin_time': 'str',
        'end_time': 'str',
        'process': 'str',
        'fail_reason': 'str',
        'resource_id': 'str',
        'resource_name': 'str',
        'resource_type': 'str',
        'project_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'process': 'process',
        'fail_reason': 'fail_reason',
        'resource_id': 'resource_id',
        'resource_name': 'resource_name',
        'resource_type': 'resource_type',
        'project_id': 'project_id'
    }

    def __init__(self, id=None, name=None, status=None, begin_time=None, end_time=None, process=None, fail_reason=None, resource_id=None, resource_name=None, resource_type=None, project_id=None):
        r"""Job

        The model defined in huaweicloud sdk

        :param id: - 参数解释：任务的唯一标识。 - 约束限制：带“-”的UUID格式。 - 取值范围：不涉及。 - 默认取值：不涉及。
        :type id: str
        :param name: - 参数解释：当前任务的名称。 - 约束限制：不涉及。 - 取值范围：不涉及。 - 默认取值：不涉及。
        :type name: str
        :param status: - 参数解释：任务状态。 - 约束限制：不涉及。 - 取值范围：   - RUNNING：运行中   - FAILED：失败   - COMPLETED：已完成 - 默认取值：不涉及。
        :type status: str
        :param begin_time: - 参数解释：任务开始时间。 - 约束限制：UTC时间，格式为yyyy-MM-ddTHH:mm:ss。 - 取值范围：不涉及。 - 默认取值：不涉及。
        :type begin_time: str
        :param end_time: - 参数解释：任务结束时间。 - 约束限制：   - UTC时间，格式为yyyy-MM-ddTHH:mm:ss。   - 仅在任务状态为FAILED或者COMPLETED时可见 - 取值范围：不涉及。 - 默认取值：不涉及。
        :type end_time: str
        :param process: - 参数解释：任务当前进度，以百分比展示。 - 约束限制：仅在任务状态为RUNNING时可见。 - 取值范围：不涉及。 - 默认取值：不涉及。
        :type process: str
        :param fail_reason: - 参数解释：任务的失败原因。 - 约束限制：仅在任务状态为FAILED时显示。 - 取值范围：不涉及。 - 默认取值：不涉及。
        :type fail_reason: str
        :param resource_id: - 参数解释：任务当前关联的资源ID。 - 约束限制：不涉及。 - 取值范围：不涉及。 - 默认取值：不涉及。
        :type resource_id: str
        :param resource_name: - 参数解释：任务当前关联的资源名称。 - 约束限制：不涉及。 - 取值范围：不涉及。 - 默认取值：不涉及。
        :type resource_name: str
        :param resource_type: - 参数解释：任务当前关联的资源类型。 - 约束限制：不涉及。 - 取值范围：   - instance：ESW实例 - 默认取值：不涉及。
        :type resource_type: str
        :param project_id: - 参数解释：ESW实例所属项目ID。 - 约束限制：不涉及。 - 取值范围：不涉及。 - 默认取值：不涉及。
        :type project_id: str
        """
        
        

        self._id = None
        self._name = None
        self._status = None
        self._begin_time = None
        self._end_time = None
        self._process = None
        self._fail_reason = None
        self._resource_id = None
        self._resource_name = None
        self._resource_type = None
        self._project_id = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.status = status
        self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time
        if process is not None:
            self.process = process
        if fail_reason is not None:
            self.fail_reason = fail_reason
        self.resource_id = resource_id
        self.resource_name = resource_name
        self.resource_type = resource_type
        self.project_id = project_id

    @property
    def id(self):
        r"""Gets the id of this Job.

        - 参数解释：任务的唯一标识。 - 约束限制：带“-”的UUID格式。 - 取值范围：不涉及。 - 默认取值：不涉及。

        :return: The id of this Job.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this Job.

        - 参数解释：任务的唯一标识。 - 约束限制：带“-”的UUID格式。 - 取值范围：不涉及。 - 默认取值：不涉及。

        :param id: The id of this Job.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this Job.

        - 参数解释：当前任务的名称。 - 约束限制：不涉及。 - 取值范围：不涉及。 - 默认取值：不涉及。

        :return: The name of this Job.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Job.

        - 参数解释：当前任务的名称。 - 约束限制：不涉及。 - 取值范围：不涉及。 - 默认取值：不涉及。

        :param name: The name of this Job.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        r"""Gets the status of this Job.

        - 参数解释：任务状态。 - 约束限制：不涉及。 - 取值范围：   - RUNNING：运行中   - FAILED：失败   - COMPLETED：已完成 - 默认取值：不涉及。

        :return: The status of this Job.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this Job.

        - 参数解释：任务状态。 - 约束限制：不涉及。 - 取值范围：   - RUNNING：运行中   - FAILED：失败   - COMPLETED：已完成 - 默认取值：不涉及。

        :param status: The status of this Job.
        :type status: str
        """
        self._status = status

    @property
    def begin_time(self):
        r"""Gets the begin_time of this Job.

        - 参数解释：任务开始时间。 - 约束限制：UTC时间，格式为yyyy-MM-ddTHH:mm:ss。 - 取值范围：不涉及。 - 默认取值：不涉及。

        :return: The begin_time of this Job.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        r"""Sets the begin_time of this Job.

        - 参数解释：任务开始时间。 - 约束限制：UTC时间，格式为yyyy-MM-ddTHH:mm:ss。 - 取值范围：不涉及。 - 默认取值：不涉及。

        :param begin_time: The begin_time of this Job.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        r"""Gets the end_time of this Job.

        - 参数解释：任务结束时间。 - 约束限制：   - UTC时间，格式为yyyy-MM-ddTHH:mm:ss。   - 仅在任务状态为FAILED或者COMPLETED时可见 - 取值范围：不涉及。 - 默认取值：不涉及。

        :return: The end_time of this Job.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this Job.

        - 参数解释：任务结束时间。 - 约束限制：   - UTC时间，格式为yyyy-MM-ddTHH:mm:ss。   - 仅在任务状态为FAILED或者COMPLETED时可见 - 取值范围：不涉及。 - 默认取值：不涉及。

        :param end_time: The end_time of this Job.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def process(self):
        r"""Gets the process of this Job.

        - 参数解释：任务当前进度，以百分比展示。 - 约束限制：仅在任务状态为RUNNING时可见。 - 取值范围：不涉及。 - 默认取值：不涉及。

        :return: The process of this Job.
        :rtype: str
        """
        return self._process

    @process.setter
    def process(self, process):
        r"""Sets the process of this Job.

        - 参数解释：任务当前进度，以百分比展示。 - 约束限制：仅在任务状态为RUNNING时可见。 - 取值范围：不涉及。 - 默认取值：不涉及。

        :param process: The process of this Job.
        :type process: str
        """
        self._process = process

    @property
    def fail_reason(self):
        r"""Gets the fail_reason of this Job.

        - 参数解释：任务的失败原因。 - 约束限制：仅在任务状态为FAILED时显示。 - 取值范围：不涉及。 - 默认取值：不涉及。

        :return: The fail_reason of this Job.
        :rtype: str
        """
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, fail_reason):
        r"""Sets the fail_reason of this Job.

        - 参数解释：任务的失败原因。 - 约束限制：仅在任务状态为FAILED时显示。 - 取值范围：不涉及。 - 默认取值：不涉及。

        :param fail_reason: The fail_reason of this Job.
        :type fail_reason: str
        """
        self._fail_reason = fail_reason

    @property
    def resource_id(self):
        r"""Gets the resource_id of this Job.

        - 参数解释：任务当前关联的资源ID。 - 约束限制：不涉及。 - 取值范围：不涉及。 - 默认取值：不涉及。

        :return: The resource_id of this Job.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this Job.

        - 参数解释：任务当前关联的资源ID。 - 约束限制：不涉及。 - 取值范围：不涉及。 - 默认取值：不涉及。

        :param resource_id: The resource_id of this Job.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_name(self):
        r"""Gets the resource_name of this Job.

        - 参数解释：任务当前关联的资源名称。 - 约束限制：不涉及。 - 取值范围：不涉及。 - 默认取值：不涉及。

        :return: The resource_name of this Job.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        r"""Sets the resource_name of this Job.

        - 参数解释：任务当前关联的资源名称。 - 约束限制：不涉及。 - 取值范围：不涉及。 - 默认取值：不涉及。

        :param resource_name: The resource_name of this Job.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def resource_type(self):
        r"""Gets the resource_type of this Job.

        - 参数解释：任务当前关联的资源类型。 - 约束限制：不涉及。 - 取值范围：   - instance：ESW实例 - 默认取值：不涉及。

        :return: The resource_type of this Job.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this Job.

        - 参数解释：任务当前关联的资源类型。 - 约束限制：不涉及。 - 取值范围：   - instance：ESW实例 - 默认取值：不涉及。

        :param resource_type: The resource_type of this Job.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def project_id(self):
        r"""Gets the project_id of this Job.

        - 参数解释：ESW实例所属项目ID。 - 约束限制：不涉及。 - 取值范围：不涉及。 - 默认取值：不涉及。

        :return: The project_id of this Job.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this Job.

        - 参数解释：ESW实例所属项目ID。 - 约束限制：不涉及。 - 取值范围：不涉及。 - 默认取值：不涉及。

        :param project_id: The project_id of this Job.
        :type project_id: str
        """
        self._project_id = project_id

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Job):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
