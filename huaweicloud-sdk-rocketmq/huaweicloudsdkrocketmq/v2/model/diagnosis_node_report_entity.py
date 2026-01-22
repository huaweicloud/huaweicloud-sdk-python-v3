# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DiagnosisNodeReportEntity:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'node_id': 'str',
        'is_faulted': 'bool',
        'abnormal_item_sum': 'int',
        'message_accumulation': 'int',
        'dead_lock': 'bool',
        'deadlock_thread': 'str',
        'stack_id': 'str',
        'is_pop': 'bool',
        'consume_type': 'str'
    }

    attribute_map = {
        'node_id': 'node_id',
        'is_faulted': 'is_faulted',
        'abnormal_item_sum': 'abnormal_item_sum',
        'message_accumulation': 'message_accumulation',
        'dead_lock': 'dead_lock',
        'deadlock_thread': 'deadlock_thread',
        'stack_id': 'stack_id',
        'is_pop': 'is_pop',
        'consume_type': 'consume_type'
    }

    def __init__(self, node_id=None, is_faulted=None, abnormal_item_sum=None, message_accumulation=None, dead_lock=None, deadlock_thread=None, stack_id=None, is_pop=None, consume_type=None):
        r"""DiagnosisNodeReportEntity

        The model defined in huaweicloud sdk

        :param node_id: **参数解释**： 节点ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type node_id: str
        :param is_faulted: **参数解释**： 是否故障。 **约束限制**： 不涉及。 **取值范围**： - true：故障 - false：没有故障。 **默认取值**： 不涉及。
        :type is_faulted: bool
        :param abnormal_item_sum: **参数解释**： 异常项总数。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type abnormal_item_sum: int
        :param message_accumulation: **参数解释**： 消息堆积数。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type message_accumulation: int
        :param dead_lock: **参数解释**： 是否为死锁。 **约束限制**： 不涉及。 **取值范围**： - true：是死锁。 - false：不是死锁。 **默认取值**： 不涉及。
        :type dead_lock: bool
        :param deadlock_thread: **参数解释**： 死锁线程。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type deadlock_thread: str
        :param stack_id: **参数解释**： 线程ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type stack_id: str
        :param is_pop: **参数解释**： 是否为pop消费模式。 **约束限制**： 不涉及。 **取值范围**： - true：是pop消费模式。 - false：不是pop消费模式。 **默认取值**： 不涉及。
        :type is_pop: bool
        :param consume_type: **参数解释**： 消费类型。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type consume_type: str
        """
        
        

        self._node_id = None
        self._is_faulted = None
        self._abnormal_item_sum = None
        self._message_accumulation = None
        self._dead_lock = None
        self._deadlock_thread = None
        self._stack_id = None
        self._is_pop = None
        self._consume_type = None
        self.discriminator = None

        if node_id is not None:
            self.node_id = node_id
        if is_faulted is not None:
            self.is_faulted = is_faulted
        if abnormal_item_sum is not None:
            self.abnormal_item_sum = abnormal_item_sum
        if message_accumulation is not None:
            self.message_accumulation = message_accumulation
        if dead_lock is not None:
            self.dead_lock = dead_lock
        if deadlock_thread is not None:
            self.deadlock_thread = deadlock_thread
        if stack_id is not None:
            self.stack_id = stack_id
        if is_pop is not None:
            self.is_pop = is_pop
        if consume_type is not None:
            self.consume_type = consume_type

    @property
    def node_id(self):
        r"""Gets the node_id of this DiagnosisNodeReportEntity.

        **参数解释**： 节点ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The node_id of this DiagnosisNodeReportEntity.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this DiagnosisNodeReportEntity.

        **参数解释**： 节点ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param node_id: The node_id of this DiagnosisNodeReportEntity.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def is_faulted(self):
        r"""Gets the is_faulted of this DiagnosisNodeReportEntity.

        **参数解释**： 是否故障。 **约束限制**： 不涉及。 **取值范围**： - true：故障 - false：没有故障。 **默认取值**： 不涉及。

        :return: The is_faulted of this DiagnosisNodeReportEntity.
        :rtype: bool
        """
        return self._is_faulted

    @is_faulted.setter
    def is_faulted(self, is_faulted):
        r"""Sets the is_faulted of this DiagnosisNodeReportEntity.

        **参数解释**： 是否故障。 **约束限制**： 不涉及。 **取值范围**： - true：故障 - false：没有故障。 **默认取值**： 不涉及。

        :param is_faulted: The is_faulted of this DiagnosisNodeReportEntity.
        :type is_faulted: bool
        """
        self._is_faulted = is_faulted

    @property
    def abnormal_item_sum(self):
        r"""Gets the abnormal_item_sum of this DiagnosisNodeReportEntity.

        **参数解释**： 异常项总数。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The abnormal_item_sum of this DiagnosisNodeReportEntity.
        :rtype: int
        """
        return self._abnormal_item_sum

    @abnormal_item_sum.setter
    def abnormal_item_sum(self, abnormal_item_sum):
        r"""Sets the abnormal_item_sum of this DiagnosisNodeReportEntity.

        **参数解释**： 异常项总数。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param abnormal_item_sum: The abnormal_item_sum of this DiagnosisNodeReportEntity.
        :type abnormal_item_sum: int
        """
        self._abnormal_item_sum = abnormal_item_sum

    @property
    def message_accumulation(self):
        r"""Gets the message_accumulation of this DiagnosisNodeReportEntity.

        **参数解释**： 消息堆积数。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The message_accumulation of this DiagnosisNodeReportEntity.
        :rtype: int
        """
        return self._message_accumulation

    @message_accumulation.setter
    def message_accumulation(self, message_accumulation):
        r"""Sets the message_accumulation of this DiagnosisNodeReportEntity.

        **参数解释**： 消息堆积数。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param message_accumulation: The message_accumulation of this DiagnosisNodeReportEntity.
        :type message_accumulation: int
        """
        self._message_accumulation = message_accumulation

    @property
    def dead_lock(self):
        r"""Gets the dead_lock of this DiagnosisNodeReportEntity.

        **参数解释**： 是否为死锁。 **约束限制**： 不涉及。 **取值范围**： - true：是死锁。 - false：不是死锁。 **默认取值**： 不涉及。

        :return: The dead_lock of this DiagnosisNodeReportEntity.
        :rtype: bool
        """
        return self._dead_lock

    @dead_lock.setter
    def dead_lock(self, dead_lock):
        r"""Sets the dead_lock of this DiagnosisNodeReportEntity.

        **参数解释**： 是否为死锁。 **约束限制**： 不涉及。 **取值范围**： - true：是死锁。 - false：不是死锁。 **默认取值**： 不涉及。

        :param dead_lock: The dead_lock of this DiagnosisNodeReportEntity.
        :type dead_lock: bool
        """
        self._dead_lock = dead_lock

    @property
    def deadlock_thread(self):
        r"""Gets the deadlock_thread of this DiagnosisNodeReportEntity.

        **参数解释**： 死锁线程。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The deadlock_thread of this DiagnosisNodeReportEntity.
        :rtype: str
        """
        return self._deadlock_thread

    @deadlock_thread.setter
    def deadlock_thread(self, deadlock_thread):
        r"""Sets the deadlock_thread of this DiagnosisNodeReportEntity.

        **参数解释**： 死锁线程。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param deadlock_thread: The deadlock_thread of this DiagnosisNodeReportEntity.
        :type deadlock_thread: str
        """
        self._deadlock_thread = deadlock_thread

    @property
    def stack_id(self):
        r"""Gets the stack_id of this DiagnosisNodeReportEntity.

        **参数解释**： 线程ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The stack_id of this DiagnosisNodeReportEntity.
        :rtype: str
        """
        return self._stack_id

    @stack_id.setter
    def stack_id(self, stack_id):
        r"""Sets the stack_id of this DiagnosisNodeReportEntity.

        **参数解释**： 线程ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param stack_id: The stack_id of this DiagnosisNodeReportEntity.
        :type stack_id: str
        """
        self._stack_id = stack_id

    @property
    def is_pop(self):
        r"""Gets the is_pop of this DiagnosisNodeReportEntity.

        **参数解释**： 是否为pop消费模式。 **约束限制**： 不涉及。 **取值范围**： - true：是pop消费模式。 - false：不是pop消费模式。 **默认取值**： 不涉及。

        :return: The is_pop of this DiagnosisNodeReportEntity.
        :rtype: bool
        """
        return self._is_pop

    @is_pop.setter
    def is_pop(self, is_pop):
        r"""Sets the is_pop of this DiagnosisNodeReportEntity.

        **参数解释**： 是否为pop消费模式。 **约束限制**： 不涉及。 **取值范围**： - true：是pop消费模式。 - false：不是pop消费模式。 **默认取值**： 不涉及。

        :param is_pop: The is_pop of this DiagnosisNodeReportEntity.
        :type is_pop: bool
        """
        self._is_pop = is_pop

    @property
    def consume_type(self):
        r"""Gets the consume_type of this DiagnosisNodeReportEntity.

        **参数解释**： 消费类型。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The consume_type of this DiagnosisNodeReportEntity.
        :rtype: str
        """
        return self._consume_type

    @consume_type.setter
    def consume_type(self, consume_type):
        r"""Sets the consume_type of this DiagnosisNodeReportEntity.

        **参数解释**： 消费类型。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param consume_type: The consume_type of this DiagnosisNodeReportEntity.
        :type consume_type: str
        """
        self._consume_type = consume_type

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
        if not isinstance(other, DiagnosisNodeReportEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
