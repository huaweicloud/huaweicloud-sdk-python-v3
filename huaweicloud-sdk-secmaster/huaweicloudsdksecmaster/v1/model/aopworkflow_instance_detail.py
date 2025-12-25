# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AopworkflowInstanceDetail:

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
        'workflow': 'AopworkflowInstanceDetailWorkflow',
        'dataclass': 'AopworkflowInstanceDetailDataclass',
        'playbook': 'AopworkflowInstanceDetailPlaybook',
        'trigger_type': 'str',
        'status': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'retry_count': 'int',
        'defense_id': 'str',
        'dataobject_id': 'str',
        'topology': 'WorkflowInstanceTopology'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'workflow': 'workflow',
        'dataclass': 'dataclass',
        'playbook': 'playbook',
        'trigger_type': 'trigger_type',
        'status': 'status',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'retry_count': 'retry_count',
        'defense_id': 'defense_id',
        'dataobject_id': 'dataobject_id',
        'topology': 'topology'
    }

    def __init__(self, id=None, name=None, workflow=None, dataclass=None, playbook=None, trigger_type=None, status=None, start_time=None, end_time=None, retry_count=None, defense_id=None, dataobject_id=None, topology=None):
        r"""AopworkflowInstanceDetail

        The model defined in huaweicloud sdk

        :param id: **参数解释**: 流程实例的ID **约束限制**: 不涉及
        :type id: str
        :param name: **参数解释**: 流程实例的名字 **约束限制**: 不涉及
        :type name: str
        :param workflow: 
        :type workflow: :class:`huaweicloudsdksecmaster.v1.AopworkflowInstanceDetailWorkflow`
        :param dataclass: 
        :type dataclass: :class:`huaweicloudsdksecmaster.v1.AopworkflowInstanceDetailDataclass`
        :param playbook: 
        :type playbook: :class:`huaweicloudsdksecmaster.v1.AopworkflowInstanceDetailPlaybook`
        :param trigger_type: **参数解释**:          触发方式 **取值范围**: - DEBUG   调试触发 - TIMER   定时触发 - EVENT   事件触发 - MANUAL  手动触发
        :type trigger_type: str
        :param status: **参数解释**:          流程实例的状态 **取值范围**: - RUNNING   运行中 - FAILED    运行失败 - FINISHED  运行结束 - RETRYING  重试中 - TERMINATING 终止中 - TERMINATED  已终止
        :type status: str
        :param start_time: **参数解释**: 开始时间 **约束限制**: 不涉及
        :type start_time: str
        :param end_time: **参数解释**: 结束时间 **约束限制**: 不涉及
        :type end_time: str
        :param retry_count: **参数解释**: 流程实例重试次数 **约束限制**: 不涉及
        :type retry_count: int
        :param defense_id: **参数解释**: 防线ID **约束限制**: 不涉及
        :type defense_id: str
        :param dataobject_id: **参数解释**: dataobject的ID **约束限制**: 不涉及
        :type dataobject_id: str
        :param topology: 
        :type topology: :class:`huaweicloudsdksecmaster.v1.WorkflowInstanceTopology`
        """
        
        

        self._id = None
        self._name = None
        self._workflow = None
        self._dataclass = None
        self._playbook = None
        self._trigger_type = None
        self._status = None
        self._start_time = None
        self._end_time = None
        self._retry_count = None
        self._defense_id = None
        self._dataobject_id = None
        self._topology = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if workflow is not None:
            self.workflow = workflow
        if dataclass is not None:
            self.dataclass = dataclass
        if playbook is not None:
            self.playbook = playbook
        if trigger_type is not None:
            self.trigger_type = trigger_type
        if status is not None:
            self.status = status
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if retry_count is not None:
            self.retry_count = retry_count
        if defense_id is not None:
            self.defense_id = defense_id
        if dataobject_id is not None:
            self.dataobject_id = dataobject_id
        if topology is not None:
            self.topology = topology

    @property
    def id(self):
        r"""Gets the id of this AopworkflowInstanceDetail.

        **参数解释**: 流程实例的ID **约束限制**: 不涉及

        :return: The id of this AopworkflowInstanceDetail.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this AopworkflowInstanceDetail.

        **参数解释**: 流程实例的ID **约束限制**: 不涉及

        :param id: The id of this AopworkflowInstanceDetail.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this AopworkflowInstanceDetail.

        **参数解释**: 流程实例的名字 **约束限制**: 不涉及

        :return: The name of this AopworkflowInstanceDetail.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this AopworkflowInstanceDetail.

        **参数解释**: 流程实例的名字 **约束限制**: 不涉及

        :param name: The name of this AopworkflowInstanceDetail.
        :type name: str
        """
        self._name = name

    @property
    def workflow(self):
        r"""Gets the workflow of this AopworkflowInstanceDetail.

        :return: The workflow of this AopworkflowInstanceDetail.
        :rtype: :class:`huaweicloudsdksecmaster.v1.AopworkflowInstanceDetailWorkflow`
        """
        return self._workflow

    @workflow.setter
    def workflow(self, workflow):
        r"""Sets the workflow of this AopworkflowInstanceDetail.

        :param workflow: The workflow of this AopworkflowInstanceDetail.
        :type workflow: :class:`huaweicloudsdksecmaster.v1.AopworkflowInstanceDetailWorkflow`
        """
        self._workflow = workflow

    @property
    def dataclass(self):
        r"""Gets the dataclass of this AopworkflowInstanceDetail.

        :return: The dataclass of this AopworkflowInstanceDetail.
        :rtype: :class:`huaweicloudsdksecmaster.v1.AopworkflowInstanceDetailDataclass`
        """
        return self._dataclass

    @dataclass.setter
    def dataclass(self, dataclass):
        r"""Sets the dataclass of this AopworkflowInstanceDetail.

        :param dataclass: The dataclass of this AopworkflowInstanceDetail.
        :type dataclass: :class:`huaweicloudsdksecmaster.v1.AopworkflowInstanceDetailDataclass`
        """
        self._dataclass = dataclass

    @property
    def playbook(self):
        r"""Gets the playbook of this AopworkflowInstanceDetail.

        :return: The playbook of this AopworkflowInstanceDetail.
        :rtype: :class:`huaweicloudsdksecmaster.v1.AopworkflowInstanceDetailPlaybook`
        """
        return self._playbook

    @playbook.setter
    def playbook(self, playbook):
        r"""Sets the playbook of this AopworkflowInstanceDetail.

        :param playbook: The playbook of this AopworkflowInstanceDetail.
        :type playbook: :class:`huaweicloudsdksecmaster.v1.AopworkflowInstanceDetailPlaybook`
        """
        self._playbook = playbook

    @property
    def trigger_type(self):
        r"""Gets the trigger_type of this AopworkflowInstanceDetail.

        **参数解释**:          触发方式 **取值范围**: - DEBUG   调试触发 - TIMER   定时触发 - EVENT   事件触发 - MANUAL  手动触发

        :return: The trigger_type of this AopworkflowInstanceDetail.
        :rtype: str
        """
        return self._trigger_type

    @trigger_type.setter
    def trigger_type(self, trigger_type):
        r"""Sets the trigger_type of this AopworkflowInstanceDetail.

        **参数解释**:          触发方式 **取值范围**: - DEBUG   调试触发 - TIMER   定时触发 - EVENT   事件触发 - MANUAL  手动触发

        :param trigger_type: The trigger_type of this AopworkflowInstanceDetail.
        :type trigger_type: str
        """
        self._trigger_type = trigger_type

    @property
    def status(self):
        r"""Gets the status of this AopworkflowInstanceDetail.

        **参数解释**:          流程实例的状态 **取值范围**: - RUNNING   运行中 - FAILED    运行失败 - FINISHED  运行结束 - RETRYING  重试中 - TERMINATING 终止中 - TERMINATED  已终止

        :return: The status of this AopworkflowInstanceDetail.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this AopworkflowInstanceDetail.

        **参数解释**:          流程实例的状态 **取值范围**: - RUNNING   运行中 - FAILED    运行失败 - FINISHED  运行结束 - RETRYING  重试中 - TERMINATING 终止中 - TERMINATED  已终止

        :param status: The status of this AopworkflowInstanceDetail.
        :type status: str
        """
        self._status = status

    @property
    def start_time(self):
        r"""Gets the start_time of this AopworkflowInstanceDetail.

        **参数解释**: 开始时间 **约束限制**: 不涉及

        :return: The start_time of this AopworkflowInstanceDetail.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this AopworkflowInstanceDetail.

        **参数解释**: 开始时间 **约束限制**: 不涉及

        :param start_time: The start_time of this AopworkflowInstanceDetail.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this AopworkflowInstanceDetail.

        **参数解释**: 结束时间 **约束限制**: 不涉及

        :return: The end_time of this AopworkflowInstanceDetail.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this AopworkflowInstanceDetail.

        **参数解释**: 结束时间 **约束限制**: 不涉及

        :param end_time: The end_time of this AopworkflowInstanceDetail.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def retry_count(self):
        r"""Gets the retry_count of this AopworkflowInstanceDetail.

        **参数解释**: 流程实例重试次数 **约束限制**: 不涉及

        :return: The retry_count of this AopworkflowInstanceDetail.
        :rtype: int
        """
        return self._retry_count

    @retry_count.setter
    def retry_count(self, retry_count):
        r"""Sets the retry_count of this AopworkflowInstanceDetail.

        **参数解释**: 流程实例重试次数 **约束限制**: 不涉及

        :param retry_count: The retry_count of this AopworkflowInstanceDetail.
        :type retry_count: int
        """
        self._retry_count = retry_count

    @property
    def defense_id(self):
        r"""Gets the defense_id of this AopworkflowInstanceDetail.

        **参数解释**: 防线ID **约束限制**: 不涉及

        :return: The defense_id of this AopworkflowInstanceDetail.
        :rtype: str
        """
        return self._defense_id

    @defense_id.setter
    def defense_id(self, defense_id):
        r"""Sets the defense_id of this AopworkflowInstanceDetail.

        **参数解释**: 防线ID **约束限制**: 不涉及

        :param defense_id: The defense_id of this AopworkflowInstanceDetail.
        :type defense_id: str
        """
        self._defense_id = defense_id

    @property
    def dataobject_id(self):
        r"""Gets the dataobject_id of this AopworkflowInstanceDetail.

        **参数解释**: dataobject的ID **约束限制**: 不涉及

        :return: The dataobject_id of this AopworkflowInstanceDetail.
        :rtype: str
        """
        return self._dataobject_id

    @dataobject_id.setter
    def dataobject_id(self, dataobject_id):
        r"""Sets the dataobject_id of this AopworkflowInstanceDetail.

        **参数解释**: dataobject的ID **约束限制**: 不涉及

        :param dataobject_id: The dataobject_id of this AopworkflowInstanceDetail.
        :type dataobject_id: str
        """
        self._dataobject_id = dataobject_id

    @property
    def topology(self):
        r"""Gets the topology of this AopworkflowInstanceDetail.

        :return: The topology of this AopworkflowInstanceDetail.
        :rtype: :class:`huaweicloudsdksecmaster.v1.WorkflowInstanceTopology`
        """
        return self._topology

    @topology.setter
    def topology(self, topology):
        r"""Sets the topology of this AopworkflowInstanceDetail.

        :param topology: The topology of this AopworkflowInstanceDetail.
        :type topology: :class:`huaweicloudsdksecmaster.v1.WorkflowInstanceTopology`
        """
        self._topology = topology

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
        if not isinstance(other, AopworkflowInstanceDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
