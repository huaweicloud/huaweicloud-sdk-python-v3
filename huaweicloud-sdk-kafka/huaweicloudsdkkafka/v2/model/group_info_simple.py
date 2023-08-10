# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GroupInfoSimple:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'created_at': 'int',
        'group_id': 'str',
        'state': 'str',
        'coordinator_id': 'int',
        'group_desc': 'str',
        'lag': 'int'
    }

    attribute_map = {
        'created_at': 'createdAt',
        'group_id': 'group_id',
        'state': 'state',
        'coordinator_id': 'coordinator_id',
        'group_desc': 'group_desc',
        'lag': 'lag'
    }

    def __init__(self, created_at=None, group_id=None, state=None, coordinator_id=None, group_desc=None, lag=None):
        """GroupInfoSimple

        The model defined in huaweicloud sdk

        :param created_at: 创建时间。
        :type created_at: int
        :param group_id: 消费组ID。
        :type group_id: str
        :param state: 消费组状态。包含以下状态： - Dead：消费组内没有任何成员，且没有任何元数据。 - Empty：消费组内没有任何成员，存在元数据。 - PreparingRebalance：准备开启rebalance。 - CompletingRebalance：所有成员加入group。 - Stable：消费组内成员可正常消费。
        :type state: str
        :param coordinator_id: 协调器编号。
        :type coordinator_id: int
        :param group_desc: 消费组描述。
        :type group_desc: str
        :param lag: 堆积数。
        :type lag: int
        """
        
        

        self._created_at = None
        self._group_id = None
        self._state = None
        self._coordinator_id = None
        self._group_desc = None
        self._lag = None
        self.discriminator = None

        if created_at is not None:
            self.created_at = created_at
        if group_id is not None:
            self.group_id = group_id
        if state is not None:
            self.state = state
        if coordinator_id is not None:
            self.coordinator_id = coordinator_id
        if group_desc is not None:
            self.group_desc = group_desc
        if lag is not None:
            self.lag = lag

    @property
    def created_at(self):
        """Gets the created_at of this GroupInfoSimple.

        创建时间。

        :return: The created_at of this GroupInfoSimple.
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this GroupInfoSimple.

        创建时间。

        :param created_at: The created_at of this GroupInfoSimple.
        :type created_at: int
        """
        self._created_at = created_at

    @property
    def group_id(self):
        """Gets the group_id of this GroupInfoSimple.

        消费组ID。

        :return: The group_id of this GroupInfoSimple.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this GroupInfoSimple.

        消费组ID。

        :param group_id: The group_id of this GroupInfoSimple.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def state(self):
        """Gets the state of this GroupInfoSimple.

        消费组状态。包含以下状态： - Dead：消费组内没有任何成员，且没有任何元数据。 - Empty：消费组内没有任何成员，存在元数据。 - PreparingRebalance：准备开启rebalance。 - CompletingRebalance：所有成员加入group。 - Stable：消费组内成员可正常消费。

        :return: The state of this GroupInfoSimple.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this GroupInfoSimple.

        消费组状态。包含以下状态： - Dead：消费组内没有任何成员，且没有任何元数据。 - Empty：消费组内没有任何成员，存在元数据。 - PreparingRebalance：准备开启rebalance。 - CompletingRebalance：所有成员加入group。 - Stable：消费组内成员可正常消费。

        :param state: The state of this GroupInfoSimple.
        :type state: str
        """
        self._state = state

    @property
    def coordinator_id(self):
        """Gets the coordinator_id of this GroupInfoSimple.

        协调器编号。

        :return: The coordinator_id of this GroupInfoSimple.
        :rtype: int
        """
        return self._coordinator_id

    @coordinator_id.setter
    def coordinator_id(self, coordinator_id):
        """Sets the coordinator_id of this GroupInfoSimple.

        协调器编号。

        :param coordinator_id: The coordinator_id of this GroupInfoSimple.
        :type coordinator_id: int
        """
        self._coordinator_id = coordinator_id

    @property
    def group_desc(self):
        """Gets the group_desc of this GroupInfoSimple.

        消费组描述。

        :return: The group_desc of this GroupInfoSimple.
        :rtype: str
        """
        return self._group_desc

    @group_desc.setter
    def group_desc(self, group_desc):
        """Sets the group_desc of this GroupInfoSimple.

        消费组描述。

        :param group_desc: The group_desc of this GroupInfoSimple.
        :type group_desc: str
        """
        self._group_desc = group_desc

    @property
    def lag(self):
        """Gets the lag of this GroupInfoSimple.

        堆积数。

        :return: The lag of this GroupInfoSimple.
        :rtype: int
        """
        return self._lag

    @lag.setter
    def lag(self, lag):
        """Sets the lag of this GroupInfoSimple.

        堆积数。

        :param lag: The lag of this GroupInfoSimple.
        :type lag: int
        """
        self._lag = lag

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
        if not isinstance(other, GroupInfoSimple):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
