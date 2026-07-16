# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Workload:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'api_version': 'str',
        'kind': 'str',
        'type': 'str',
        'namespace': 'str',
        'name': 'str',
        'job_name': 'str',
        'uid': 'str',
        'job_uuid': 'str',
        'flavor': 'str',
        'status': 'str',
        'resource_requirement': 'WorkloadResourceRequirement',
        'priority': 'str',
        'running_duration': 'int',
        'pending_duration': 'int',
        'pending_position': 'int',
        'create_time': 'int',
        'gvk': 'str',
        'host_ips': 'str',
        'nodes': 'list[WorkloadNodeVO]'
    }

    attribute_map = {
        'api_version': 'apiVersion',
        'kind': 'kind',
        'type': 'type',
        'namespace': 'namespace',
        'name': 'name',
        'job_name': 'jobName',
        'uid': 'uid',
        'job_uuid': 'jobUUID',
        'flavor': 'flavor',
        'status': 'status',
        'resource_requirement': 'resourceRequirement',
        'priority': 'priority',
        'running_duration': 'runningDuration',
        'pending_duration': 'pendingDuration',
        'pending_position': 'pendingPosition',
        'create_time': 'createTime',
        'gvk': 'gvk',
        'host_ips': 'hostIps',
        'nodes': 'nodes'
    }

    def __init__(self, api_version=None, kind=None, type=None, namespace=None, name=None, job_name=None, uid=None, job_uuid=None, flavor=None, status=None, resource_requirement=None, priority=None, running_duration=None, pending_duration=None, pending_position=None, create_time=None, gvk=None, host_ips=None, nodes=None):
        r"""Workload

        The model defined in huaweicloud sdk

        :param api_version: **参数解释**：资源的API版本。 **取值范围**：可选值如下： - v1：当前资源版本为v1
        :type api_version: str
        :param kind: **参数解释**：资源的类型。 **取值范围**：可选值如下： - Workload：资源池作业
        :type kind: str
        :param type: **参数解释**：资源池中作业的业务类型。 **取值范围**：可选值如下： - train：训练作业 - infer：推理服务 - notebook：Notebook作业 - x-infer：新版推理作业
        :type type: str
        :param namespace: **参数解释**：集群中作业所属的命名空间。 **取值范围**：不涉及。
        :type namespace: str
        :param name: **参数解释**：作业的名称。 **取值范围**：不涉及。
        :type name: str
        :param job_name: **参数解释**：作业的归属的上层业务的名称。 **取值范围**：不涉及。
        :type job_name: str
        :param uid: **参数解释**：作业的ID。 **取值范围**：不涉及。
        :type uid: str
        :param job_uuid: **参数解释**：作业的归属的上层业务的ID。 **取值范围**：不涉及。
        :type job_uuid: str
        :param flavor: **参数解释**：作业的资源规格。 **取值范围**：不涉及。
        :type flavor: str
        :param status: **参数解释**：作业状态。 **取值范围**：不涉及。
        :type status: str
        :param resource_requirement: 
        :type resource_requirement: :class:`huaweicloudsdkmodelarts.v1.WorkloadResourceRequirement`
        :param priority: **参数解释**：作业的优先级。 **取值范围**：不涉及。
        :type priority: str
        :param running_duration: **参数解释**：作业的运行时长，以秒为单位。 **取值范围**：不涉及。
        :type running_duration: int
        :param pending_duration: **参数解释**：作业的排队时长，以秒为单位。 **取值范围**：不涉及。
        :type pending_duration: int
        :param pending_position: **参数解释**：作业当前的排队位置。 **取值范围**：不涉及。
        :type pending_position: int
        :param create_time: **参数解释**：作业的Unix创建时间戳，以毫秒为单位。 **取值范围**：不涉及。
        :type create_time: int
        :param gvk: **参数解释**：作业的k8s资源类型、分组和版本。 **取值范围**：不涉及。
        :type gvk: str
        :param host_ips: **参数解释**：作业运行的节点IP列表，以“,”分隔。 **取值范围**：不涉及。
        :type host_ips: str
        :param nodes: **参数解释**：作业运行时占用的节点资源信息。
        :type nodes: list[:class:`huaweicloudsdkmodelarts.v1.WorkloadNodeVO`]
        """
        
        

        self._api_version = None
        self._kind = None
        self._type = None
        self._namespace = None
        self._name = None
        self._job_name = None
        self._uid = None
        self._job_uuid = None
        self._flavor = None
        self._status = None
        self._resource_requirement = None
        self._priority = None
        self._running_duration = None
        self._pending_duration = None
        self._pending_position = None
        self._create_time = None
        self._gvk = None
        self._host_ips = None
        self._nodes = None
        self.discriminator = None

        self.api_version = api_version
        self.kind = kind
        self.type = type
        self.namespace = namespace
        self.name = name
        if job_name is not None:
            self.job_name = job_name
        if uid is not None:
            self.uid = uid
        if job_uuid is not None:
            self.job_uuid = job_uuid
        if flavor is not None:
            self.flavor = flavor
        if status is not None:
            self.status = status
        if resource_requirement is not None:
            self.resource_requirement = resource_requirement
        if priority is not None:
            self.priority = priority
        if running_duration is not None:
            self.running_duration = running_duration
        if pending_duration is not None:
            self.pending_duration = pending_duration
        if pending_position is not None:
            self.pending_position = pending_position
        if create_time is not None:
            self.create_time = create_time
        if gvk is not None:
            self.gvk = gvk
        if host_ips is not None:
            self.host_ips = host_ips
        if nodes is not None:
            self.nodes = nodes

    @property
    def api_version(self):
        r"""Gets the api_version of this Workload.

        **参数解释**：资源的API版本。 **取值范围**：可选值如下： - v1：当前资源版本为v1

        :return: The api_version of this Workload.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        r"""Sets the api_version of this Workload.

        **参数解释**：资源的API版本。 **取值范围**：可选值如下： - v1：当前资源版本为v1

        :param api_version: The api_version of this Workload.
        :type api_version: str
        """
        self._api_version = api_version

    @property
    def kind(self):
        r"""Gets the kind of this Workload.

        **参数解释**：资源的类型。 **取值范围**：可选值如下： - Workload：资源池作业

        :return: The kind of this Workload.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        r"""Sets the kind of this Workload.

        **参数解释**：资源的类型。 **取值范围**：可选值如下： - Workload：资源池作业

        :param kind: The kind of this Workload.
        :type kind: str
        """
        self._kind = kind

    @property
    def type(self):
        r"""Gets the type of this Workload.

        **参数解释**：资源池中作业的业务类型。 **取值范围**：可选值如下： - train：训练作业 - infer：推理服务 - notebook：Notebook作业 - x-infer：新版推理作业

        :return: The type of this Workload.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this Workload.

        **参数解释**：资源池中作业的业务类型。 **取值范围**：可选值如下： - train：训练作业 - infer：推理服务 - notebook：Notebook作业 - x-infer：新版推理作业

        :param type: The type of this Workload.
        :type type: str
        """
        self._type = type

    @property
    def namespace(self):
        r"""Gets the namespace of this Workload.

        **参数解释**：集群中作业所属的命名空间。 **取值范围**：不涉及。

        :return: The namespace of this Workload.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this Workload.

        **参数解释**：集群中作业所属的命名空间。 **取值范围**：不涉及。

        :param namespace: The namespace of this Workload.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def name(self):
        r"""Gets the name of this Workload.

        **参数解释**：作业的名称。 **取值范围**：不涉及。

        :return: The name of this Workload.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Workload.

        **参数解释**：作业的名称。 **取值范围**：不涉及。

        :param name: The name of this Workload.
        :type name: str
        """
        self._name = name

    @property
    def job_name(self):
        r"""Gets the job_name of this Workload.

        **参数解释**：作业的归属的上层业务的名称。 **取值范围**：不涉及。

        :return: The job_name of this Workload.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        r"""Sets the job_name of this Workload.

        **参数解释**：作业的归属的上层业务的名称。 **取值范围**：不涉及。

        :param job_name: The job_name of this Workload.
        :type job_name: str
        """
        self._job_name = job_name

    @property
    def uid(self):
        r"""Gets the uid of this Workload.

        **参数解释**：作业的ID。 **取值范围**：不涉及。

        :return: The uid of this Workload.
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        r"""Sets the uid of this Workload.

        **参数解释**：作业的ID。 **取值范围**：不涉及。

        :param uid: The uid of this Workload.
        :type uid: str
        """
        self._uid = uid

    @property
    def job_uuid(self):
        r"""Gets the job_uuid of this Workload.

        **参数解释**：作业的归属的上层业务的ID。 **取值范围**：不涉及。

        :return: The job_uuid of this Workload.
        :rtype: str
        """
        return self._job_uuid

    @job_uuid.setter
    def job_uuid(self, job_uuid):
        r"""Sets the job_uuid of this Workload.

        **参数解释**：作业的归属的上层业务的ID。 **取值范围**：不涉及。

        :param job_uuid: The job_uuid of this Workload.
        :type job_uuid: str
        """
        self._job_uuid = job_uuid

    @property
    def flavor(self):
        r"""Gets the flavor of this Workload.

        **参数解释**：作业的资源规格。 **取值范围**：不涉及。

        :return: The flavor of this Workload.
        :rtype: str
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        r"""Sets the flavor of this Workload.

        **参数解释**：作业的资源规格。 **取值范围**：不涉及。

        :param flavor: The flavor of this Workload.
        :type flavor: str
        """
        self._flavor = flavor

    @property
    def status(self):
        r"""Gets the status of this Workload.

        **参数解释**：作业状态。 **取值范围**：不涉及。

        :return: The status of this Workload.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this Workload.

        **参数解释**：作业状态。 **取值范围**：不涉及。

        :param status: The status of this Workload.
        :type status: str
        """
        self._status = status

    @property
    def resource_requirement(self):
        r"""Gets the resource_requirement of this Workload.

        :return: The resource_requirement of this Workload.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.WorkloadResourceRequirement`
        """
        return self._resource_requirement

    @resource_requirement.setter
    def resource_requirement(self, resource_requirement):
        r"""Sets the resource_requirement of this Workload.

        :param resource_requirement: The resource_requirement of this Workload.
        :type resource_requirement: :class:`huaweicloudsdkmodelarts.v1.WorkloadResourceRequirement`
        """
        self._resource_requirement = resource_requirement

    @property
    def priority(self):
        r"""Gets the priority of this Workload.

        **参数解释**：作业的优先级。 **取值范围**：不涉及。

        :return: The priority of this Workload.
        :rtype: str
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        r"""Sets the priority of this Workload.

        **参数解释**：作业的优先级。 **取值范围**：不涉及。

        :param priority: The priority of this Workload.
        :type priority: str
        """
        self._priority = priority

    @property
    def running_duration(self):
        r"""Gets the running_duration of this Workload.

        **参数解释**：作业的运行时长，以秒为单位。 **取值范围**：不涉及。

        :return: The running_duration of this Workload.
        :rtype: int
        """
        return self._running_duration

    @running_duration.setter
    def running_duration(self, running_duration):
        r"""Sets the running_duration of this Workload.

        **参数解释**：作业的运行时长，以秒为单位。 **取值范围**：不涉及。

        :param running_duration: The running_duration of this Workload.
        :type running_duration: int
        """
        self._running_duration = running_duration

    @property
    def pending_duration(self):
        r"""Gets the pending_duration of this Workload.

        **参数解释**：作业的排队时长，以秒为单位。 **取值范围**：不涉及。

        :return: The pending_duration of this Workload.
        :rtype: int
        """
        return self._pending_duration

    @pending_duration.setter
    def pending_duration(self, pending_duration):
        r"""Sets the pending_duration of this Workload.

        **参数解释**：作业的排队时长，以秒为单位。 **取值范围**：不涉及。

        :param pending_duration: The pending_duration of this Workload.
        :type pending_duration: int
        """
        self._pending_duration = pending_duration

    @property
    def pending_position(self):
        r"""Gets the pending_position of this Workload.

        **参数解释**：作业当前的排队位置。 **取值范围**：不涉及。

        :return: The pending_position of this Workload.
        :rtype: int
        """
        return self._pending_position

    @pending_position.setter
    def pending_position(self, pending_position):
        r"""Sets the pending_position of this Workload.

        **参数解释**：作业当前的排队位置。 **取值范围**：不涉及。

        :param pending_position: The pending_position of this Workload.
        :type pending_position: int
        """
        self._pending_position = pending_position

    @property
    def create_time(self):
        r"""Gets the create_time of this Workload.

        **参数解释**：作业的Unix创建时间戳，以毫秒为单位。 **取值范围**：不涉及。

        :return: The create_time of this Workload.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this Workload.

        **参数解释**：作业的Unix创建时间戳，以毫秒为单位。 **取值范围**：不涉及。

        :param create_time: The create_time of this Workload.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def gvk(self):
        r"""Gets the gvk of this Workload.

        **参数解释**：作业的k8s资源类型、分组和版本。 **取值范围**：不涉及。

        :return: The gvk of this Workload.
        :rtype: str
        """
        return self._gvk

    @gvk.setter
    def gvk(self, gvk):
        r"""Sets the gvk of this Workload.

        **参数解释**：作业的k8s资源类型、分组和版本。 **取值范围**：不涉及。

        :param gvk: The gvk of this Workload.
        :type gvk: str
        """
        self._gvk = gvk

    @property
    def host_ips(self):
        r"""Gets the host_ips of this Workload.

        **参数解释**：作业运行的节点IP列表，以“,”分隔。 **取值范围**：不涉及。

        :return: The host_ips of this Workload.
        :rtype: str
        """
        return self._host_ips

    @host_ips.setter
    def host_ips(self, host_ips):
        r"""Sets the host_ips of this Workload.

        **参数解释**：作业运行的节点IP列表，以“,”分隔。 **取值范围**：不涉及。

        :param host_ips: The host_ips of this Workload.
        :type host_ips: str
        """
        self._host_ips = host_ips

    @property
    def nodes(self):
        r"""Gets the nodes of this Workload.

        **参数解释**：作业运行时占用的节点资源信息。

        :return: The nodes of this Workload.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.WorkloadNodeVO`]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        r"""Sets the nodes of this Workload.

        **参数解释**：作业运行时占用的节点资源信息。

        :param nodes: The nodes of this Workload.
        :type nodes: list[:class:`huaweicloudsdkmodelarts.v1.WorkloadNodeVO`]
        """
        self._nodes = nodes

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
        if not isinstance(other, Workload):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
