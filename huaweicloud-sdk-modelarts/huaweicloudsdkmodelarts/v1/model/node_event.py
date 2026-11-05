# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodeEvent:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'event_id': 'str',
        'is_fault_node': 'bool',
        'node_name': 'str',
        'instance_id': 'str',
        'instance_type': 'str',
        'under_lying_instance_id': 'str',
        'flavor_support_redeploy': 'bool',
        'pool_name': 'str',
        'pool_display_name': 'str',
        'state': 'str',
        'publish_time': 'str',
        'start_time': 'str',
        'finish_time': 'str',
        'job_progress': 'str'
    }

    attribute_map = {
        'event_id': 'eventId',
        'is_fault_node': 'isFaultNode',
        'node_name': 'nodeName',
        'instance_id': 'instanceId',
        'instance_type': 'instanceType',
        'under_lying_instance_id': 'underLyingInstanceId',
        'flavor_support_redeploy': 'flavorSupportRedeploy',
        'pool_name': 'poolName',
        'pool_display_name': 'poolDisplayName',
        'state': 'state',
        'publish_time': 'publishTime',
        'start_time': 'startTime',
        'finish_time': 'finishTime',
        'job_progress': 'jobProgress'
    }

    def __init__(self, event_id=None, is_fault_node=None, node_name=None, instance_id=None, instance_type=None, under_lying_instance_id=None, flavor_support_redeploy=None, pool_name=None, pool_display_name=None, state=None, publish_time=None, start_time=None, finish_time=None, job_progress=None):
        r"""NodeEvent

        The model defined in huaweicloud sdk

        :param event_id: **参数解释**：Iaas计划事件Id。 **取值范围**：不涉及。
        :type event_id: str
        :param is_fault_node: **参数解释**：是否故障节点。 **取值范围**：不涉及。
        :type is_fault_node: bool
        :param node_name: **参数解释**：节点名称。 **取值范围**：不涉及。
        :type node_name: str
        :param instance_id: **参数解释**：节点ID。 **取值范围**：不涉及。
        :type instance_id: str
        :param instance_type: **参数解释**：实例类型。 **取值范围**：不涉及。
        :type instance_type: str
        :param under_lying_instance_id: **参数解释**：底层实例Id。 **取值范围**：不涉及。
        :type under_lying_instance_id: str
        :param flavor_support_redeploy: **参数解释**：节点规格是否支持重部署。 **取值范围**：不涉及。
        :type flavor_support_redeploy: bool
        :param pool_name: **参数解释**：资源池名称。 **取值范围**：不涉及。
        :type pool_name: str
        :param pool_display_name: **参数解释**：资源池显示名称。 **取值范围**：不涉及。
        :type pool_display_name: str
        :param state: **参数解释**：Iaas计划事件状态。 **取值范围**：不涉及。
        :type state: str
        :param publish_time: **参数解释**：Iaas事件发布时间。 **取值范围**：不涉及。
        :type publish_time: str
        :param start_time: **参数解释**：Iaas事件开始时间。 **取值范围**：不涉及。
        :type start_time: str
        :param finish_time: **参数解释**：Iaas事件完成时间。 **取值范围**：不涉及。
        :type finish_time: str
        :param job_progress: **参数解释**：重部署进度。 **取值范围**：不涉及。
        :type job_progress: str
        """
        
        

        self._event_id = None
        self._is_fault_node = None
        self._node_name = None
        self._instance_id = None
        self._instance_type = None
        self._under_lying_instance_id = None
        self._flavor_support_redeploy = None
        self._pool_name = None
        self._pool_display_name = None
        self._state = None
        self._publish_time = None
        self._start_time = None
        self._finish_time = None
        self._job_progress = None
        self.discriminator = None

        if event_id is not None:
            self.event_id = event_id
        if is_fault_node is not None:
            self.is_fault_node = is_fault_node
        if node_name is not None:
            self.node_name = node_name
        if instance_id is not None:
            self.instance_id = instance_id
        if instance_type is not None:
            self.instance_type = instance_type
        if under_lying_instance_id is not None:
            self.under_lying_instance_id = under_lying_instance_id
        if flavor_support_redeploy is not None:
            self.flavor_support_redeploy = flavor_support_redeploy
        if pool_name is not None:
            self.pool_name = pool_name
        if pool_display_name is not None:
            self.pool_display_name = pool_display_name
        if state is not None:
            self.state = state
        if publish_time is not None:
            self.publish_time = publish_time
        if start_time is not None:
            self.start_time = start_time
        if finish_time is not None:
            self.finish_time = finish_time
        if job_progress is not None:
            self.job_progress = job_progress

    @property
    def event_id(self):
        r"""Gets the event_id of this NodeEvent.

        **参数解释**：Iaas计划事件Id。 **取值范围**：不涉及。

        :return: The event_id of this NodeEvent.
        :rtype: str
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        r"""Sets the event_id of this NodeEvent.

        **参数解释**：Iaas计划事件Id。 **取值范围**：不涉及。

        :param event_id: The event_id of this NodeEvent.
        :type event_id: str
        """
        self._event_id = event_id

    @property
    def is_fault_node(self):
        r"""Gets the is_fault_node of this NodeEvent.

        **参数解释**：是否故障节点。 **取值范围**：不涉及。

        :return: The is_fault_node of this NodeEvent.
        :rtype: bool
        """
        return self._is_fault_node

    @is_fault_node.setter
    def is_fault_node(self, is_fault_node):
        r"""Sets the is_fault_node of this NodeEvent.

        **参数解释**：是否故障节点。 **取值范围**：不涉及。

        :param is_fault_node: The is_fault_node of this NodeEvent.
        :type is_fault_node: bool
        """
        self._is_fault_node = is_fault_node

    @property
    def node_name(self):
        r"""Gets the node_name of this NodeEvent.

        **参数解释**：节点名称。 **取值范围**：不涉及。

        :return: The node_name of this NodeEvent.
        :rtype: str
        """
        return self._node_name

    @node_name.setter
    def node_name(self, node_name):
        r"""Sets the node_name of this NodeEvent.

        **参数解释**：节点名称。 **取值范围**：不涉及。

        :param node_name: The node_name of this NodeEvent.
        :type node_name: str
        """
        self._node_name = node_name

    @property
    def instance_id(self):
        r"""Gets the instance_id of this NodeEvent.

        **参数解释**：节点ID。 **取值范围**：不涉及。

        :return: The instance_id of this NodeEvent.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this NodeEvent.

        **参数解释**：节点ID。 **取值范围**：不涉及。

        :param instance_id: The instance_id of this NodeEvent.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def instance_type(self):
        r"""Gets the instance_type of this NodeEvent.

        **参数解释**：实例类型。 **取值范围**：不涉及。

        :return: The instance_type of this NodeEvent.
        :rtype: str
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        r"""Sets the instance_type of this NodeEvent.

        **参数解释**：实例类型。 **取值范围**：不涉及。

        :param instance_type: The instance_type of this NodeEvent.
        :type instance_type: str
        """
        self._instance_type = instance_type

    @property
    def under_lying_instance_id(self):
        r"""Gets the under_lying_instance_id of this NodeEvent.

        **参数解释**：底层实例Id。 **取值范围**：不涉及。

        :return: The under_lying_instance_id of this NodeEvent.
        :rtype: str
        """
        return self._under_lying_instance_id

    @under_lying_instance_id.setter
    def under_lying_instance_id(self, under_lying_instance_id):
        r"""Sets the under_lying_instance_id of this NodeEvent.

        **参数解释**：底层实例Id。 **取值范围**：不涉及。

        :param under_lying_instance_id: The under_lying_instance_id of this NodeEvent.
        :type under_lying_instance_id: str
        """
        self._under_lying_instance_id = under_lying_instance_id

    @property
    def flavor_support_redeploy(self):
        r"""Gets the flavor_support_redeploy of this NodeEvent.

        **参数解释**：节点规格是否支持重部署。 **取值范围**：不涉及。

        :return: The flavor_support_redeploy of this NodeEvent.
        :rtype: bool
        """
        return self._flavor_support_redeploy

    @flavor_support_redeploy.setter
    def flavor_support_redeploy(self, flavor_support_redeploy):
        r"""Sets the flavor_support_redeploy of this NodeEvent.

        **参数解释**：节点规格是否支持重部署。 **取值范围**：不涉及。

        :param flavor_support_redeploy: The flavor_support_redeploy of this NodeEvent.
        :type flavor_support_redeploy: bool
        """
        self._flavor_support_redeploy = flavor_support_redeploy

    @property
    def pool_name(self):
        r"""Gets the pool_name of this NodeEvent.

        **参数解释**：资源池名称。 **取值范围**：不涉及。

        :return: The pool_name of this NodeEvent.
        :rtype: str
        """
        return self._pool_name

    @pool_name.setter
    def pool_name(self, pool_name):
        r"""Sets the pool_name of this NodeEvent.

        **参数解释**：资源池名称。 **取值范围**：不涉及。

        :param pool_name: The pool_name of this NodeEvent.
        :type pool_name: str
        """
        self._pool_name = pool_name

    @property
    def pool_display_name(self):
        r"""Gets the pool_display_name of this NodeEvent.

        **参数解释**：资源池显示名称。 **取值范围**：不涉及。

        :return: The pool_display_name of this NodeEvent.
        :rtype: str
        """
        return self._pool_display_name

    @pool_display_name.setter
    def pool_display_name(self, pool_display_name):
        r"""Sets the pool_display_name of this NodeEvent.

        **参数解释**：资源池显示名称。 **取值范围**：不涉及。

        :param pool_display_name: The pool_display_name of this NodeEvent.
        :type pool_display_name: str
        """
        self._pool_display_name = pool_display_name

    @property
    def state(self):
        r"""Gets the state of this NodeEvent.

        **参数解释**：Iaas计划事件状态。 **取值范围**：不涉及。

        :return: The state of this NodeEvent.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this NodeEvent.

        **参数解释**：Iaas计划事件状态。 **取值范围**：不涉及。

        :param state: The state of this NodeEvent.
        :type state: str
        """
        self._state = state

    @property
    def publish_time(self):
        r"""Gets the publish_time of this NodeEvent.

        **参数解释**：Iaas事件发布时间。 **取值范围**：不涉及。

        :return: The publish_time of this NodeEvent.
        :rtype: str
        """
        return self._publish_time

    @publish_time.setter
    def publish_time(self, publish_time):
        r"""Sets the publish_time of this NodeEvent.

        **参数解释**：Iaas事件发布时间。 **取值范围**：不涉及。

        :param publish_time: The publish_time of this NodeEvent.
        :type publish_time: str
        """
        self._publish_time = publish_time

    @property
    def start_time(self):
        r"""Gets the start_time of this NodeEvent.

        **参数解释**：Iaas事件开始时间。 **取值范围**：不涉及。

        :return: The start_time of this NodeEvent.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this NodeEvent.

        **参数解释**：Iaas事件开始时间。 **取值范围**：不涉及。

        :param start_time: The start_time of this NodeEvent.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def finish_time(self):
        r"""Gets the finish_time of this NodeEvent.

        **参数解释**：Iaas事件完成时间。 **取值范围**：不涉及。

        :return: The finish_time of this NodeEvent.
        :rtype: str
        """
        return self._finish_time

    @finish_time.setter
    def finish_time(self, finish_time):
        r"""Sets the finish_time of this NodeEvent.

        **参数解释**：Iaas事件完成时间。 **取值范围**：不涉及。

        :param finish_time: The finish_time of this NodeEvent.
        :type finish_time: str
        """
        self._finish_time = finish_time

    @property
    def job_progress(self):
        r"""Gets the job_progress of this NodeEvent.

        **参数解释**：重部署进度。 **取值范围**：不涉及。

        :return: The job_progress of this NodeEvent.
        :rtype: str
        """
        return self._job_progress

    @job_progress.setter
    def job_progress(self, job_progress):
        r"""Sets the job_progress of this NodeEvent.

        **参数解释**：重部署进度。 **取值范围**：不涉及。

        :param job_progress: The job_progress of this NodeEvent.
        :type job_progress: str
        """
        self._job_progress = job_progress

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
        if not isinstance(other, NodeEvent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
