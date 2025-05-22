# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LogicalClusterPlanVo:

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
        'logical_cluster_name': 'str',
        'node_num': 'int',
        'plan_type': 'str',
        'status': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'update_time': 'str',
        'user': 'str',
        'actions': 'list[LogicalClusterPlanActions]'
    }

    attribute_map = {
        'id': 'id',
        'logical_cluster_name': 'logical_cluster_name',
        'node_num': 'node_num',
        'plan_type': 'plan_type',
        'status': 'status',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'update_time': 'update_time',
        'user': 'user',
        'actions': 'actions'
    }

    def __init__(self, id=None, logical_cluster_name=None, node_num=None, plan_type=None, status=None, start_time=None, end_time=None, update_time=None, user=None, actions=None):
        r"""LogicalClusterPlanVo

        The model defined in huaweicloud sdk

        :param id: **参数解释**： 增删逻辑集群计划ID。 **取值范围**： 不涉及。
        :type id: str
        :param logical_cluster_name: **参数解释**： 逻辑集群名字。 **取值范围**： 不涉及。
        :type logical_cluster_name: str
        :param node_num: **参数解释**： 逻辑集群节点个数。 **取值范围**： 不涉及。
        :type node_num: int
        :param plan_type: **参数解释**： 逻辑集群增删计划类型，取值范围为 (once|periodicity)，表示单次或周期性。 **取值范围**： 不涉及。
        :type plan_type: str
        :param status: **参数解释**： 逻辑集群增删计划状态。 **取值范围**： running：运行中 waiting：等待中 deleted：已删除 finished：已完成 disabled：已禁用 failed：失败
        :type status: str
        :param start_time: **参数解释**： 逻辑集群增删计划开始时间。 **取值范围**： 不涉及。
        :type start_time: str
        :param end_time: **参数解释**： 逻辑集群增删计划结束时间。 **取值范围**： 不涉及。
        :type end_time: str
        :param update_time: **参数解释**： 逻辑集群增删计划更新时间。 **取值范围**： 不涉及。
        :type update_time: str
        :param user: **参数解释**： 逻辑集群增删计划绑定的用户。 **取值范围**： 不涉及。
        :type user: str
        :param actions: **参数解释**： 任务信息。 **取值范围**： 不涉及。
        :type actions: list[:class:`huaweicloudsdkdws.v2.LogicalClusterPlanActions`]
        """
        
        

        self._id = None
        self._logical_cluster_name = None
        self._node_num = None
        self._plan_type = None
        self._status = None
        self._start_time = None
        self._end_time = None
        self._update_time = None
        self._user = None
        self._actions = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if logical_cluster_name is not None:
            self.logical_cluster_name = logical_cluster_name
        if node_num is not None:
            self.node_num = node_num
        if plan_type is not None:
            self.plan_type = plan_type
        if status is not None:
            self.status = status
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if update_time is not None:
            self.update_time = update_time
        if user is not None:
            self.user = user
        if actions is not None:
            self.actions = actions

    @property
    def id(self):
        r"""Gets the id of this LogicalClusterPlanVo.

        **参数解释**： 增删逻辑集群计划ID。 **取值范围**： 不涉及。

        :return: The id of this LogicalClusterPlanVo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this LogicalClusterPlanVo.

        **参数解释**： 增删逻辑集群计划ID。 **取值范围**： 不涉及。

        :param id: The id of this LogicalClusterPlanVo.
        :type id: str
        """
        self._id = id

    @property
    def logical_cluster_name(self):
        r"""Gets the logical_cluster_name of this LogicalClusterPlanVo.

        **参数解释**： 逻辑集群名字。 **取值范围**： 不涉及。

        :return: The logical_cluster_name of this LogicalClusterPlanVo.
        :rtype: str
        """
        return self._logical_cluster_name

    @logical_cluster_name.setter
    def logical_cluster_name(self, logical_cluster_name):
        r"""Sets the logical_cluster_name of this LogicalClusterPlanVo.

        **参数解释**： 逻辑集群名字。 **取值范围**： 不涉及。

        :param logical_cluster_name: The logical_cluster_name of this LogicalClusterPlanVo.
        :type logical_cluster_name: str
        """
        self._logical_cluster_name = logical_cluster_name

    @property
    def node_num(self):
        r"""Gets the node_num of this LogicalClusterPlanVo.

        **参数解释**： 逻辑集群节点个数。 **取值范围**： 不涉及。

        :return: The node_num of this LogicalClusterPlanVo.
        :rtype: int
        """
        return self._node_num

    @node_num.setter
    def node_num(self, node_num):
        r"""Sets the node_num of this LogicalClusterPlanVo.

        **参数解释**： 逻辑集群节点个数。 **取值范围**： 不涉及。

        :param node_num: The node_num of this LogicalClusterPlanVo.
        :type node_num: int
        """
        self._node_num = node_num

    @property
    def plan_type(self):
        r"""Gets the plan_type of this LogicalClusterPlanVo.

        **参数解释**： 逻辑集群增删计划类型，取值范围为 (once|periodicity)，表示单次或周期性。 **取值范围**： 不涉及。

        :return: The plan_type of this LogicalClusterPlanVo.
        :rtype: str
        """
        return self._plan_type

    @plan_type.setter
    def plan_type(self, plan_type):
        r"""Sets the plan_type of this LogicalClusterPlanVo.

        **参数解释**： 逻辑集群增删计划类型，取值范围为 (once|periodicity)，表示单次或周期性。 **取值范围**： 不涉及。

        :param plan_type: The plan_type of this LogicalClusterPlanVo.
        :type plan_type: str
        """
        self._plan_type = plan_type

    @property
    def status(self):
        r"""Gets the status of this LogicalClusterPlanVo.

        **参数解释**： 逻辑集群增删计划状态。 **取值范围**： running：运行中 waiting：等待中 deleted：已删除 finished：已完成 disabled：已禁用 failed：失败

        :return: The status of this LogicalClusterPlanVo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this LogicalClusterPlanVo.

        **参数解释**： 逻辑集群增删计划状态。 **取值范围**： running：运行中 waiting：等待中 deleted：已删除 finished：已完成 disabled：已禁用 failed：失败

        :param status: The status of this LogicalClusterPlanVo.
        :type status: str
        """
        self._status = status

    @property
    def start_time(self):
        r"""Gets the start_time of this LogicalClusterPlanVo.

        **参数解释**： 逻辑集群增删计划开始时间。 **取值范围**： 不涉及。

        :return: The start_time of this LogicalClusterPlanVo.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this LogicalClusterPlanVo.

        **参数解释**： 逻辑集群增删计划开始时间。 **取值范围**： 不涉及。

        :param start_time: The start_time of this LogicalClusterPlanVo.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this LogicalClusterPlanVo.

        **参数解释**： 逻辑集群增删计划结束时间。 **取值范围**： 不涉及。

        :return: The end_time of this LogicalClusterPlanVo.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this LogicalClusterPlanVo.

        **参数解释**： 逻辑集群增删计划结束时间。 **取值范围**： 不涉及。

        :param end_time: The end_time of this LogicalClusterPlanVo.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def update_time(self):
        r"""Gets the update_time of this LogicalClusterPlanVo.

        **参数解释**： 逻辑集群增删计划更新时间。 **取值范围**： 不涉及。

        :return: The update_time of this LogicalClusterPlanVo.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this LogicalClusterPlanVo.

        **参数解释**： 逻辑集群增删计划更新时间。 **取值范围**： 不涉及。

        :param update_time: The update_time of this LogicalClusterPlanVo.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def user(self):
        r"""Gets the user of this LogicalClusterPlanVo.

        **参数解释**： 逻辑集群增删计划绑定的用户。 **取值范围**： 不涉及。

        :return: The user of this LogicalClusterPlanVo.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        r"""Sets the user of this LogicalClusterPlanVo.

        **参数解释**： 逻辑集群增删计划绑定的用户。 **取值范围**： 不涉及。

        :param user: The user of this LogicalClusterPlanVo.
        :type user: str
        """
        self._user = user

    @property
    def actions(self):
        r"""Gets the actions of this LogicalClusterPlanVo.

        **参数解释**： 任务信息。 **取值范围**： 不涉及。

        :return: The actions of this LogicalClusterPlanVo.
        :rtype: list[:class:`huaweicloudsdkdws.v2.LogicalClusterPlanActions`]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        r"""Sets the actions of this LogicalClusterPlanVo.

        **参数解释**： 任务信息。 **取值范围**： 不涉及。

        :param actions: The actions of this LogicalClusterPlanVo.
        :type actions: list[:class:`huaweicloudsdkdws.v2.LogicalClusterPlanActions`]
        """
        self._actions = actions

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
        if not isinstance(other, LogicalClusterPlanVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
