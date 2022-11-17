# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowGroupsRespGroup:

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
        'members': 'list[ShowGroupsRespGroupMembers]',
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
        """ShowGroupsRespGroup

        The model defined in huaweicloud sdk

        :param group_id: 消费组名称。
        :type group_id: str
        :param state: 消费组状态。包含以下状态： - Dead：消费组内没有任何成员，且没有任何元数据。 - Empty：消费组内没有任何成员，存在元数据。 - PreparingRebalance：准备开启rebalance。 - CompletingRebalance：所有成员加入group。 - Stable：消费组内成员可正常消费。
        :type state: str
        :param coordinator_id: 协调器编号。
        :type coordinator_id: int
        :param members: 消费者列表。
        :type members: list[:class:`huaweicloudsdkkafka.v2.ShowGroupsRespGroupMembers`]
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
        """Gets the group_id of this ShowGroupsRespGroup.

        消费组名称。

        :return: The group_id of this ShowGroupsRespGroup.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this ShowGroupsRespGroup.

        消费组名称。

        :param group_id: The group_id of this ShowGroupsRespGroup.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def state(self):
        """Gets the state of this ShowGroupsRespGroup.

        消费组状态。包含以下状态： - Dead：消费组内没有任何成员，且没有任何元数据。 - Empty：消费组内没有任何成员，存在元数据。 - PreparingRebalance：准备开启rebalance。 - CompletingRebalance：所有成员加入group。 - Stable：消费组内成员可正常消费。

        :return: The state of this ShowGroupsRespGroup.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ShowGroupsRespGroup.

        消费组状态。包含以下状态： - Dead：消费组内没有任何成员，且没有任何元数据。 - Empty：消费组内没有任何成员，存在元数据。 - PreparingRebalance：准备开启rebalance。 - CompletingRebalance：所有成员加入group。 - Stable：消费组内成员可正常消费。

        :param state: The state of this ShowGroupsRespGroup.
        :type state: str
        """
        self._state = state

    @property
    def coordinator_id(self):
        """Gets the coordinator_id of this ShowGroupsRespGroup.

        协调器编号。

        :return: The coordinator_id of this ShowGroupsRespGroup.
        :rtype: int
        """
        return self._coordinator_id

    @coordinator_id.setter
    def coordinator_id(self, coordinator_id):
        """Sets the coordinator_id of this ShowGroupsRespGroup.

        协调器编号。

        :param coordinator_id: The coordinator_id of this ShowGroupsRespGroup.
        :type coordinator_id: int
        """
        self._coordinator_id = coordinator_id

    @property
    def members(self):
        """Gets the members of this ShowGroupsRespGroup.

        消费者列表。

        :return: The members of this ShowGroupsRespGroup.
        :rtype: list[:class:`huaweicloudsdkkafka.v2.ShowGroupsRespGroupMembers`]
        """
        return self._members

    @members.setter
    def members(self, members):
        """Sets the members of this ShowGroupsRespGroup.

        消费者列表。

        :param members: The members of this ShowGroupsRespGroup.
        :type members: list[:class:`huaweicloudsdkkafka.v2.ShowGroupsRespGroupMembers`]
        """
        self._members = members

    @property
    def group_message_offsets(self):
        """Gets the group_message_offsets of this ShowGroupsRespGroup.

        消费进度。

        :return: The group_message_offsets of this ShowGroupsRespGroup.
        :rtype: list[:class:`huaweicloudsdkkafka.v2.ShowGroupsRespGroupGroupMessageOffsets`]
        """
        return self._group_message_offsets

    @group_message_offsets.setter
    def group_message_offsets(self, group_message_offsets):
        """Sets the group_message_offsets of this ShowGroupsRespGroup.

        消费进度。

        :param group_message_offsets: The group_message_offsets of this ShowGroupsRespGroup.
        :type group_message_offsets: list[:class:`huaweicloudsdkkafka.v2.ShowGroupsRespGroupGroupMessageOffsets`]
        """
        self._group_message_offsets = group_message_offsets

    @property
    def assignment_strategy(self):
        """Gets the assignment_strategy of this ShowGroupsRespGroup.

        分区分配策略。

        :return: The assignment_strategy of this ShowGroupsRespGroup.
        :rtype: str
        """
        return self._assignment_strategy

    @assignment_strategy.setter
    def assignment_strategy(self, assignment_strategy):
        """Sets the assignment_strategy of this ShowGroupsRespGroup.

        分区分配策略。

        :param assignment_strategy: The assignment_strategy of this ShowGroupsRespGroup.
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
        if not isinstance(other, ShowGroupsRespGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
