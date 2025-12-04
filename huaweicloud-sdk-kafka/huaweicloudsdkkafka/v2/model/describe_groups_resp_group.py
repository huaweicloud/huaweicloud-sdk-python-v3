# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DescribeGroupsRespGroup:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'state': 'str',
        'created_at': 'object',
        'group_id': 'str',
        'coordinator_id': 'int',
        'assignment_strategy': 'str',
        'group_desc': 'str'
    }

    attribute_map = {
        'state': 'state',
        'created_at': 'createdAt',
        'group_id': 'group_id',
        'coordinator_id': 'coordinator_id',
        'assignment_strategy': 'assignment_strategy',
        'group_desc': 'group_desc'
    }

    def __init__(self, state=None, created_at=None, group_id=None, coordinator_id=None, assignment_strategy=None, group_desc=None):
        r"""DescribeGroupsRespGroup

        The model defined in huaweicloud sdk

        :param state: **参数解释**： 消费组状态。 **取值范围**： - Dead：消费组内没有任何成员，且没有任何元数据。 - Empty：消费组内没有任何成员，存在元数据。 - PreparingRebalance：准备开启rebalance。 - CompletingRebalance：所有成员加入group。 - Stable：消费组内成员可正常消费。
        :type state: str
        :param created_at: **参数解释**： 创建时间。 **取值范围**： 不涉及。
        :type created_at: object
        :param group_id: **参数解释**： 消费组名称。 **取值范围**： 不涉及。
        :type group_id: str
        :param coordinator_id: **参数解释**： 协调器编号。 **取值范围**： 不涉及。
        :type coordinator_id: int
        :param assignment_strategy: **参数解释**： 分区分配策略。 **取值范围**： 不涉及。
        :type assignment_strategy: str
        :param group_desc: **参数解释**： 消费组描述。 **取值范围**： 不涉及。
        :type group_desc: str
        """
        
        

        self._state = None
        self._created_at = None
        self._group_id = None
        self._coordinator_id = None
        self._assignment_strategy = None
        self._group_desc = None
        self.discriminator = None

        if state is not None:
            self.state = state
        if created_at is not None:
            self.created_at = created_at
        if group_id is not None:
            self.group_id = group_id
        if coordinator_id is not None:
            self.coordinator_id = coordinator_id
        if assignment_strategy is not None:
            self.assignment_strategy = assignment_strategy
        if group_desc is not None:
            self.group_desc = group_desc

    @property
    def state(self):
        r"""Gets the state of this DescribeGroupsRespGroup.

        **参数解释**： 消费组状态。 **取值范围**： - Dead：消费组内没有任何成员，且没有任何元数据。 - Empty：消费组内没有任何成员，存在元数据。 - PreparingRebalance：准备开启rebalance。 - CompletingRebalance：所有成员加入group。 - Stable：消费组内成员可正常消费。

        :return: The state of this DescribeGroupsRespGroup.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this DescribeGroupsRespGroup.

        **参数解释**： 消费组状态。 **取值范围**： - Dead：消费组内没有任何成员，且没有任何元数据。 - Empty：消费组内没有任何成员，存在元数据。 - PreparingRebalance：准备开启rebalance。 - CompletingRebalance：所有成员加入group。 - Stable：消费组内成员可正常消费。

        :param state: The state of this DescribeGroupsRespGroup.
        :type state: str
        """
        self._state = state

    @property
    def created_at(self):
        r"""Gets the created_at of this DescribeGroupsRespGroup.

        **参数解释**： 创建时间。 **取值范围**： 不涉及。

        :return: The created_at of this DescribeGroupsRespGroup.
        :rtype: object
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this DescribeGroupsRespGroup.

        **参数解释**： 创建时间。 **取值范围**： 不涉及。

        :param created_at: The created_at of this DescribeGroupsRespGroup.
        :type created_at: object
        """
        self._created_at = created_at

    @property
    def group_id(self):
        r"""Gets the group_id of this DescribeGroupsRespGroup.

        **参数解释**： 消费组名称。 **取值范围**： 不涉及。

        :return: The group_id of this DescribeGroupsRespGroup.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this DescribeGroupsRespGroup.

        **参数解释**： 消费组名称。 **取值范围**： 不涉及。

        :param group_id: The group_id of this DescribeGroupsRespGroup.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def coordinator_id(self):
        r"""Gets the coordinator_id of this DescribeGroupsRespGroup.

        **参数解释**： 协调器编号。 **取值范围**： 不涉及。

        :return: The coordinator_id of this DescribeGroupsRespGroup.
        :rtype: int
        """
        return self._coordinator_id

    @coordinator_id.setter
    def coordinator_id(self, coordinator_id):
        r"""Sets the coordinator_id of this DescribeGroupsRespGroup.

        **参数解释**： 协调器编号。 **取值范围**： 不涉及。

        :param coordinator_id: The coordinator_id of this DescribeGroupsRespGroup.
        :type coordinator_id: int
        """
        self._coordinator_id = coordinator_id

    @property
    def assignment_strategy(self):
        r"""Gets the assignment_strategy of this DescribeGroupsRespGroup.

        **参数解释**： 分区分配策略。 **取值范围**： 不涉及。

        :return: The assignment_strategy of this DescribeGroupsRespGroup.
        :rtype: str
        """
        return self._assignment_strategy

    @assignment_strategy.setter
    def assignment_strategy(self, assignment_strategy):
        r"""Sets the assignment_strategy of this DescribeGroupsRespGroup.

        **参数解释**： 分区分配策略。 **取值范围**： 不涉及。

        :param assignment_strategy: The assignment_strategy of this DescribeGroupsRespGroup.
        :type assignment_strategy: str
        """
        self._assignment_strategy = assignment_strategy

    @property
    def group_desc(self):
        r"""Gets the group_desc of this DescribeGroupsRespGroup.

        **参数解释**： 消费组描述。 **取值范围**： 不涉及。

        :return: The group_desc of this DescribeGroupsRespGroup.
        :rtype: str
        """
        return self._group_desc

    @group_desc.setter
    def group_desc(self, group_desc):
        r"""Sets the group_desc of this DescribeGroupsRespGroup.

        **参数解释**： 消费组描述。 **取值范围**： 不涉及。

        :param group_desc: The group_desc of this DescribeGroupsRespGroup.
        :type group_desc: str
        """
        self._group_desc = group_desc

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
        if not isinstance(other, DescribeGroupsRespGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
