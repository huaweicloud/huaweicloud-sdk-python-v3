# coding: utf-8

import six

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
        'group_id': 'str',
        'state': 'str',
        'coordinator_id': 'int',
        'members': 'list[DescribeGroupsRespGroupMembers]',
        'group_message_offsets': 'list[ShowGroupsRespGroupGroupMessageOffsets]',
        'assignment_strategy': 'str'
    }

    attribute_map = {
        'group_id': 'group_id',
        'state': 'state',
        'coordinator_id': 'coordinator_id',
        'members': 'members',
        'group_message_offsets': 'group_message_offsets',
        'assignment_strategy': 'assignment_strategy'
    }

    def __init__(self, group_id=None, state=None, coordinator_id=None, members=None, group_message_offsets=None, assignment_strategy=None):
        r"""DescribeGroupsRespGroup

        The model defined in huaweicloud sdk

        :param group_id: 消费组名称。
        :type group_id: str
        :param state: 消费组状态。包含以下状态： - Dead：消费组内没有任何成员，且没有任何元数据。 - Empty：消费组内没有任何成员，存在元数据。 - PreparingRebalance：准备开启rebalance。 - CompletingRebalance：所有成员加入group。 - Stable：消费组内成员可正常消费。
        :type state: str
        :param coordinator_id: 协调器编号。
        :type coordinator_id: int
        :param members: 消费者列表。
        :type members: list[:class:`huaweicloudsdkkafka.v2.DescribeGroupsRespGroupMembers`]
        :param group_message_offsets: 消费进度。
        :type group_message_offsets: list[:class:`huaweicloudsdkkafka.v2.ShowGroupsRespGroupGroupMessageOffsets`]
        :param assignment_strategy: 分区分配策略。
        :type assignment_strategy: str
        """
        
        

        self._group_id = None
        self._state = None
        self._coordinator_id = None
        self._members = None
        self._group_message_offsets = None
        self._assignment_strategy = None
        self.discriminator = None

        if group_id is not None:
            self.group_id = group_id
        if state is not None:
            self.state = state
        if coordinator_id is not None:
            self.coordinator_id = coordinator_id
        if members is not None:
            self.members = members
        if group_message_offsets is not None:
            self.group_message_offsets = group_message_offsets
        if assignment_strategy is not None:
            self.assignment_strategy = assignment_strategy

    @property
    def group_id(self):
        r"""Gets the group_id of this DescribeGroupsRespGroup.

        消费组名称。

        :return: The group_id of this DescribeGroupsRespGroup.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this DescribeGroupsRespGroup.

        消费组名称。

        :param group_id: The group_id of this DescribeGroupsRespGroup.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def state(self):
        r"""Gets the state of this DescribeGroupsRespGroup.

        消费组状态。包含以下状态： - Dead：消费组内没有任何成员，且没有任何元数据。 - Empty：消费组内没有任何成员，存在元数据。 - PreparingRebalance：准备开启rebalance。 - CompletingRebalance：所有成员加入group。 - Stable：消费组内成员可正常消费。

        :return: The state of this DescribeGroupsRespGroup.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this DescribeGroupsRespGroup.

        消费组状态。包含以下状态： - Dead：消费组内没有任何成员，且没有任何元数据。 - Empty：消费组内没有任何成员，存在元数据。 - PreparingRebalance：准备开启rebalance。 - CompletingRebalance：所有成员加入group。 - Stable：消费组内成员可正常消费。

        :param state: The state of this DescribeGroupsRespGroup.
        :type state: str
        """
        self._state = state

    @property
    def coordinator_id(self):
        r"""Gets the coordinator_id of this DescribeGroupsRespGroup.

        协调器编号。

        :return: The coordinator_id of this DescribeGroupsRespGroup.
        :rtype: int
        """
        return self._coordinator_id

    @coordinator_id.setter
    def coordinator_id(self, coordinator_id):
        r"""Sets the coordinator_id of this DescribeGroupsRespGroup.

        协调器编号。

        :param coordinator_id: The coordinator_id of this DescribeGroupsRespGroup.
        :type coordinator_id: int
        """
        self._coordinator_id = coordinator_id

    @property
    def members(self):
        r"""Gets the members of this DescribeGroupsRespGroup.

        消费者列表。

        :return: The members of this DescribeGroupsRespGroup.
        :rtype: list[:class:`huaweicloudsdkkafka.v2.DescribeGroupsRespGroupMembers`]
        """
        return self._members

    @members.setter
    def members(self, members):
        r"""Sets the members of this DescribeGroupsRespGroup.

        消费者列表。

        :param members: The members of this DescribeGroupsRespGroup.
        :type members: list[:class:`huaweicloudsdkkafka.v2.DescribeGroupsRespGroupMembers`]
        """
        self._members = members

    @property
    def group_message_offsets(self):
        r"""Gets the group_message_offsets of this DescribeGroupsRespGroup.

        消费进度。

        :return: The group_message_offsets of this DescribeGroupsRespGroup.
        :rtype: list[:class:`huaweicloudsdkkafka.v2.ShowGroupsRespGroupGroupMessageOffsets`]
        """
        return self._group_message_offsets

    @group_message_offsets.setter
    def group_message_offsets(self, group_message_offsets):
        r"""Sets the group_message_offsets of this DescribeGroupsRespGroup.

        消费进度。

        :param group_message_offsets: The group_message_offsets of this DescribeGroupsRespGroup.
        :type group_message_offsets: list[:class:`huaweicloudsdkkafka.v2.ShowGroupsRespGroupGroupMessageOffsets`]
        """
        self._group_message_offsets = group_message_offsets

    @property
    def assignment_strategy(self):
        r"""Gets the assignment_strategy of this DescribeGroupsRespGroup.

        分区分配策略。

        :return: The assignment_strategy of this DescribeGroupsRespGroup.
        :rtype: str
        """
        return self._assignment_strategy

    @assignment_strategy.setter
    def assignment_strategy(self, assignment_strategy):
        r"""Sets the assignment_strategy of this DescribeGroupsRespGroup.

        分区分配策略。

        :param assignment_strategy: The assignment_strategy of this DescribeGroupsRespGroup.
        :type assignment_strategy: str
        """
        self._assignment_strategy = assignment_strategy

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
        if not isinstance(other, DescribeGroupsRespGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
