# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TopologyNodeInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_type': 'str',
        'action_id': 'str',
        'action_name': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'error_msg': 'str',
        'input': 'str',
        'output': 'str',
        'parent_instance_id': 'str',
        'status': 'str',
        'succeed': 'bool'
    }

    attribute_map = {
        'instance_type': 'instance_type',
        'action_id': 'action_id',
        'action_name': 'action_name',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'error_msg': 'error_msg',
        'input': 'input',
        'output': 'output',
        'parent_instance_id': 'parent_instance_id',
        'status': 'status',
        'succeed': 'succeed'
    }

    def __init__(self, instance_type=None, action_id=None, action_name=None, start_time=None, end_time=None, error_msg=None, input=None, output=None, parent_instance_id=None, status=None, succeed=None):
        r"""TopologyNodeInfo

        The model defined in huaweicloud sdk

        :param instance_type: **参数解释**: 流程图拓扑图的节点实例类型 **取值范围**: - TASK
        :type instance_type: str
        :param action_id: **参数解释**: 流程拓扑图的节点ID **取值范围**: 不涉及
        :type action_id: str
        :param action_name: **参数解释**:     流程拓扑图的节点名称 **取值范围**: 不涉及
        :type action_name: str
        :param start_time: **参数解释**:          流程图拓扑图的节点开始时间 **取值范围**: - 不涉及
        :type start_time: str
        :param end_time: **参数解释**:          流程图拓扑图的节点结束时间 **取值范围**: - 不涉及
        :type end_time: str
        :param error_msg: **参数解释**:          流程图拓扑图的节点错误信息 **取值范围**: - 不涉及
        :type error_msg: str
        :param input: **参数解释**:          流程图拓扑图的节点输入信息 **取值范围**: - 不涉及
        :type input: str
        :param output: **参数解释**:          流程图拓扑图的节点输出信息 **取值范围**: - 不涉及
        :type output: str
        :param parent_instance_id: **参数解释**:          流程图拓扑图的父实例ID **取值范围**: - 不涉及
        :type parent_instance_id: str
        :param status: **参数解释**:          流程图拓扑图的节点的状态 **取值范围**: - RUNNING 运行中 - FAILED  运行失败 - FINISHED 运行结束
        :type status: str
        :param succeed: **参数解释**:          流程图拓扑图的节点是否成功 **取值范围**: - true  成功 - false 失败
        :type succeed: bool
        """
        
        

        self._instance_type = None
        self._action_id = None
        self._action_name = None
        self._start_time = None
        self._end_time = None
        self._error_msg = None
        self._input = None
        self._output = None
        self._parent_instance_id = None
        self._status = None
        self._succeed = None
        self.discriminator = None

        if instance_type is not None:
            self.instance_type = instance_type
        if action_id is not None:
            self.action_id = action_id
        if action_name is not None:
            self.action_name = action_name
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if error_msg is not None:
            self.error_msg = error_msg
        if input is not None:
            self.input = input
        if output is not None:
            self.output = output
        if parent_instance_id is not None:
            self.parent_instance_id = parent_instance_id
        if status is not None:
            self.status = status
        if succeed is not None:
            self.succeed = succeed

    @property
    def instance_type(self):
        r"""Gets the instance_type of this TopologyNodeInfo.

        **参数解释**: 流程图拓扑图的节点实例类型 **取值范围**: - TASK

        :return: The instance_type of this TopologyNodeInfo.
        :rtype: str
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        r"""Sets the instance_type of this TopologyNodeInfo.

        **参数解释**: 流程图拓扑图的节点实例类型 **取值范围**: - TASK

        :param instance_type: The instance_type of this TopologyNodeInfo.
        :type instance_type: str
        """
        self._instance_type = instance_type

    @property
    def action_id(self):
        r"""Gets the action_id of this TopologyNodeInfo.

        **参数解释**: 流程拓扑图的节点ID **取值范围**: 不涉及

        :return: The action_id of this TopologyNodeInfo.
        :rtype: str
        """
        return self._action_id

    @action_id.setter
    def action_id(self, action_id):
        r"""Sets the action_id of this TopologyNodeInfo.

        **参数解释**: 流程拓扑图的节点ID **取值范围**: 不涉及

        :param action_id: The action_id of this TopologyNodeInfo.
        :type action_id: str
        """
        self._action_id = action_id

    @property
    def action_name(self):
        r"""Gets the action_name of this TopologyNodeInfo.

        **参数解释**:     流程拓扑图的节点名称 **取值范围**: 不涉及

        :return: The action_name of this TopologyNodeInfo.
        :rtype: str
        """
        return self._action_name

    @action_name.setter
    def action_name(self, action_name):
        r"""Sets the action_name of this TopologyNodeInfo.

        **参数解释**:     流程拓扑图的节点名称 **取值范围**: 不涉及

        :param action_name: The action_name of this TopologyNodeInfo.
        :type action_name: str
        """
        self._action_name = action_name

    @property
    def start_time(self):
        r"""Gets the start_time of this TopologyNodeInfo.

        **参数解释**:          流程图拓扑图的节点开始时间 **取值范围**: - 不涉及

        :return: The start_time of this TopologyNodeInfo.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this TopologyNodeInfo.

        **参数解释**:          流程图拓扑图的节点开始时间 **取值范围**: - 不涉及

        :param start_time: The start_time of this TopologyNodeInfo.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this TopologyNodeInfo.

        **参数解释**:          流程图拓扑图的节点结束时间 **取值范围**: - 不涉及

        :return: The end_time of this TopologyNodeInfo.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this TopologyNodeInfo.

        **参数解释**:          流程图拓扑图的节点结束时间 **取值范围**: - 不涉及

        :param end_time: The end_time of this TopologyNodeInfo.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def error_msg(self):
        r"""Gets the error_msg of this TopologyNodeInfo.

        **参数解释**:          流程图拓扑图的节点错误信息 **取值范围**: - 不涉及

        :return: The error_msg of this TopologyNodeInfo.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        r"""Sets the error_msg of this TopologyNodeInfo.

        **参数解释**:          流程图拓扑图的节点错误信息 **取值范围**: - 不涉及

        :param error_msg: The error_msg of this TopologyNodeInfo.
        :type error_msg: str
        """
        self._error_msg = error_msg

    @property
    def input(self):
        r"""Gets the input of this TopologyNodeInfo.

        **参数解释**:          流程图拓扑图的节点输入信息 **取值范围**: - 不涉及

        :return: The input of this TopologyNodeInfo.
        :rtype: str
        """
        return self._input

    @input.setter
    def input(self, input):
        r"""Sets the input of this TopologyNodeInfo.

        **参数解释**:          流程图拓扑图的节点输入信息 **取值范围**: - 不涉及

        :param input: The input of this TopologyNodeInfo.
        :type input: str
        """
        self._input = input

    @property
    def output(self):
        r"""Gets the output of this TopologyNodeInfo.

        **参数解释**:          流程图拓扑图的节点输出信息 **取值范围**: - 不涉及

        :return: The output of this TopologyNodeInfo.
        :rtype: str
        """
        return self._output

    @output.setter
    def output(self, output):
        r"""Sets the output of this TopologyNodeInfo.

        **参数解释**:          流程图拓扑图的节点输出信息 **取值范围**: - 不涉及

        :param output: The output of this TopologyNodeInfo.
        :type output: str
        """
        self._output = output

    @property
    def parent_instance_id(self):
        r"""Gets the parent_instance_id of this TopologyNodeInfo.

        **参数解释**:          流程图拓扑图的父实例ID **取值范围**: - 不涉及

        :return: The parent_instance_id of this TopologyNodeInfo.
        :rtype: str
        """
        return self._parent_instance_id

    @parent_instance_id.setter
    def parent_instance_id(self, parent_instance_id):
        r"""Sets the parent_instance_id of this TopologyNodeInfo.

        **参数解释**:          流程图拓扑图的父实例ID **取值范围**: - 不涉及

        :param parent_instance_id: The parent_instance_id of this TopologyNodeInfo.
        :type parent_instance_id: str
        """
        self._parent_instance_id = parent_instance_id

    @property
    def status(self):
        r"""Gets the status of this TopologyNodeInfo.

        **参数解释**:          流程图拓扑图的节点的状态 **取值范围**: - RUNNING 运行中 - FAILED  运行失败 - FINISHED 运行结束

        :return: The status of this TopologyNodeInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this TopologyNodeInfo.

        **参数解释**:          流程图拓扑图的节点的状态 **取值范围**: - RUNNING 运行中 - FAILED  运行失败 - FINISHED 运行结束

        :param status: The status of this TopologyNodeInfo.
        :type status: str
        """
        self._status = status

    @property
    def succeed(self):
        r"""Gets the succeed of this TopologyNodeInfo.

        **参数解释**:          流程图拓扑图的节点是否成功 **取值范围**: - true  成功 - false 失败

        :return: The succeed of this TopologyNodeInfo.
        :rtype: bool
        """
        return self._succeed

    @succeed.setter
    def succeed(self, succeed):
        r"""Sets the succeed of this TopologyNodeInfo.

        **参数解释**:          流程图拓扑图的节点是否成功 **取值范围**: - true  成功 - false 失败

        :param succeed: The succeed of this TopologyNodeInfo.
        :type succeed: bool
        """
        self._succeed = succeed

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
        if not isinstance(other, TopologyNodeInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
