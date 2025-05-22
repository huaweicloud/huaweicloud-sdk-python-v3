# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LogicalClusterPlanBo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'logical_cluster_name': 'str',
        'user': 'str',
        'node_num': 'int',
        'main_logical_cluster': 'str',
        'plan_type': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'actions': 'list[LogicalClusterPlanActionsParam]'
    }

    attribute_map = {
        'logical_cluster_name': 'logical_cluster_name',
        'user': 'user',
        'node_num': 'node_num',
        'main_logical_cluster': 'main_logical_cluster',
        'plan_type': 'plan_type',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'actions': 'actions'
    }

    def __init__(self, logical_cluster_name=None, user=None, node_num=None, main_logical_cluster=None, plan_type=None, start_time=None, end_time=None, actions=None):
        r"""LogicalClusterPlanBo

        The model defined in huaweicloud sdk

        :param logical_cluster_name: **参数解释**： 逻辑集群名字。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type logical_cluster_name: str
        :param user: **参数解释**： 逻辑集群绑定的用户，若绑定了主逻辑集群，不能绑定用户。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type user: str
        :param node_num: **参数解释**： 逻辑集群节点的个数。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type node_num: int
        :param main_logical_cluster: **参数解释**： 逻辑集群的绑定的主逻辑集群，若绑定了用户，不能绑定主逻辑集群。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type main_logical_cluster: str
        :param plan_type: **参数解释**： 计划类型，取值范围为(once|periodicity)。 **约束限制**： 不涉及。 **取值范围**： once：一次性计划 periodicity：周期性计划 **默认取值**： 不涉及。
        :type plan_type: str
        :param start_time: **参数解释**： 逻辑集群定时增删计划起始时间。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type start_time: str
        :param end_time: **参数解释**： 逻辑集群定时增删计划终止时间。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type end_time: str
        :param actions: **参数解释**： 逻辑集群定时增删计划细节。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type actions: list[:class:`huaweicloudsdkdws.v2.LogicalClusterPlanActionsParam`]
        """
        
        

        self._logical_cluster_name = None
        self._user = None
        self._node_num = None
        self._main_logical_cluster = None
        self._plan_type = None
        self._start_time = None
        self._end_time = None
        self._actions = None
        self.discriminator = None

        if logical_cluster_name is not None:
            self.logical_cluster_name = logical_cluster_name
        if user is not None:
            self.user = user
        if node_num is not None:
            self.node_num = node_num
        if main_logical_cluster is not None:
            self.main_logical_cluster = main_logical_cluster
        self.plan_type = plan_type
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        self.actions = actions

    @property
    def logical_cluster_name(self):
        r"""Gets the logical_cluster_name of this LogicalClusterPlanBo.

        **参数解释**： 逻辑集群名字。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The logical_cluster_name of this LogicalClusterPlanBo.
        :rtype: str
        """
        return self._logical_cluster_name

    @logical_cluster_name.setter
    def logical_cluster_name(self, logical_cluster_name):
        r"""Sets the logical_cluster_name of this LogicalClusterPlanBo.

        **参数解释**： 逻辑集群名字。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param logical_cluster_name: The logical_cluster_name of this LogicalClusterPlanBo.
        :type logical_cluster_name: str
        """
        self._logical_cluster_name = logical_cluster_name

    @property
    def user(self):
        r"""Gets the user of this LogicalClusterPlanBo.

        **参数解释**： 逻辑集群绑定的用户，若绑定了主逻辑集群，不能绑定用户。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The user of this LogicalClusterPlanBo.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        r"""Sets the user of this LogicalClusterPlanBo.

        **参数解释**： 逻辑集群绑定的用户，若绑定了主逻辑集群，不能绑定用户。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param user: The user of this LogicalClusterPlanBo.
        :type user: str
        """
        self._user = user

    @property
    def node_num(self):
        r"""Gets the node_num of this LogicalClusterPlanBo.

        **参数解释**： 逻辑集群节点的个数。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The node_num of this LogicalClusterPlanBo.
        :rtype: int
        """
        return self._node_num

    @node_num.setter
    def node_num(self, node_num):
        r"""Sets the node_num of this LogicalClusterPlanBo.

        **参数解释**： 逻辑集群节点的个数。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param node_num: The node_num of this LogicalClusterPlanBo.
        :type node_num: int
        """
        self._node_num = node_num

    @property
    def main_logical_cluster(self):
        r"""Gets the main_logical_cluster of this LogicalClusterPlanBo.

        **参数解释**： 逻辑集群的绑定的主逻辑集群，若绑定了用户，不能绑定主逻辑集群。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The main_logical_cluster of this LogicalClusterPlanBo.
        :rtype: str
        """
        return self._main_logical_cluster

    @main_logical_cluster.setter
    def main_logical_cluster(self, main_logical_cluster):
        r"""Sets the main_logical_cluster of this LogicalClusterPlanBo.

        **参数解释**： 逻辑集群的绑定的主逻辑集群，若绑定了用户，不能绑定主逻辑集群。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param main_logical_cluster: The main_logical_cluster of this LogicalClusterPlanBo.
        :type main_logical_cluster: str
        """
        self._main_logical_cluster = main_logical_cluster

    @property
    def plan_type(self):
        r"""Gets the plan_type of this LogicalClusterPlanBo.

        **参数解释**： 计划类型，取值范围为(once|periodicity)。 **约束限制**： 不涉及。 **取值范围**： once：一次性计划 periodicity：周期性计划 **默认取值**： 不涉及。

        :return: The plan_type of this LogicalClusterPlanBo.
        :rtype: str
        """
        return self._plan_type

    @plan_type.setter
    def plan_type(self, plan_type):
        r"""Sets the plan_type of this LogicalClusterPlanBo.

        **参数解释**： 计划类型，取值范围为(once|periodicity)。 **约束限制**： 不涉及。 **取值范围**： once：一次性计划 periodicity：周期性计划 **默认取值**： 不涉及。

        :param plan_type: The plan_type of this LogicalClusterPlanBo.
        :type plan_type: str
        """
        self._plan_type = plan_type

    @property
    def start_time(self):
        r"""Gets the start_time of this LogicalClusterPlanBo.

        **参数解释**： 逻辑集群定时增删计划起始时间。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The start_time of this LogicalClusterPlanBo.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this LogicalClusterPlanBo.

        **参数解释**： 逻辑集群定时增删计划起始时间。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param start_time: The start_time of this LogicalClusterPlanBo.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this LogicalClusterPlanBo.

        **参数解释**： 逻辑集群定时增删计划终止时间。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The end_time of this LogicalClusterPlanBo.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this LogicalClusterPlanBo.

        **参数解释**： 逻辑集群定时增删计划终止时间。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param end_time: The end_time of this LogicalClusterPlanBo.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def actions(self):
        r"""Gets the actions of this LogicalClusterPlanBo.

        **参数解释**： 逻辑集群定时增删计划细节。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The actions of this LogicalClusterPlanBo.
        :rtype: list[:class:`huaweicloudsdkdws.v2.LogicalClusterPlanActionsParam`]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        r"""Sets the actions of this LogicalClusterPlanBo.

        **参数解释**： 逻辑集群定时增删计划细节。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param actions: The actions of this LogicalClusterPlanBo.
        :type actions: list[:class:`huaweicloudsdkdws.v2.LogicalClusterPlanActionsParam`]
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
        if not isinstance(other, LogicalClusterPlanBo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
