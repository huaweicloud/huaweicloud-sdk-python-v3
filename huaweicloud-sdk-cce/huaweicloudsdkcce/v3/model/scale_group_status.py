# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ScaleGroupStatus:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'uid': 'str',
        'creation_timestamp': 'str',
        'update_timestamp': 'str',
        'phase': 'str',
        'desired_node_count': 'int',
        'unpaid_scale_node_count': 'int',
        'existing_node_count': 'ScaleGroupStatusExistingNodeCount',
        'upcoming_node_count': 'ScaleGroupStatusUpcomingNodeCount',
        'scale_down_disabled_node_count': 'int',
        'conditions': 'list[NodePoolCondition]'
    }

    attribute_map = {
        'name': 'name',
        'uid': 'uid',
        'creation_timestamp': 'creationTimestamp',
        'update_timestamp': 'updateTimestamp',
        'phase': 'phase',
        'desired_node_count': 'desiredNodeCount',
        'unpaid_scale_node_count': 'unpaidScaleNodeCount',
        'existing_node_count': 'existingNodeCount',
        'upcoming_node_count': 'upcomingNodeCount',
        'scale_down_disabled_node_count': 'scaleDownDisabledNodeCount',
        'conditions': 'conditions'
    }

    def __init__(self, name=None, uid=None, creation_timestamp=None, update_timestamp=None, phase=None, desired_node_count=None, unpaid_scale_node_count=None, existing_node_count=None, upcoming_node_count=None, scale_down_disabled_node_count=None, conditions=None):
        r"""ScaleGroupStatus

        The model defined in huaweicloud sdk

        :param name: 伸缩组名称
        :type name: str
        :param uid: 伸缩组uuid
        :type uid: str
        :param creation_timestamp: 伸缩组创建时间
        :type creation_timestamp: str
        :param update_timestamp: 伸缩组更新时间
        :type update_timestamp: str
        :param phase: 伸缩组状态。 - 空值：可用（伸缩组当前节点数已达到预期，且无伸缩中的节点） - Synchronizing：伸缩中（伸缩组当前节点数未达到预期，且无伸缩中的节点） - Synchronized：伸缩等待中（伸缩组当前节点数未达到预期，或者存在伸缩中的节点） - SoldOut：伸缩组当前不可扩容（兼容字段，标记节点池资源售罄、资源配额不足等不可扩容状态） &gt; 上述伸缩组状态已废弃，仅兼容保留，不建议使用，替代感知方式如下： &gt; - 伸缩组扩缩状态：可通过desiredNodeCount/existingNodeCount/upcomingNodeCount节点状态统计信息，精确感知当前伸缩组扩缩状态。 &gt; - 伸缩组可扩容状态：可通过conditions感知伸缩组详细状态，其中\&quot;Scalable\&quot;可替代SoldOut语义。 - Deleting：删除中 - Error：错误 
        :type phase: str
        :param desired_node_count: 伸缩组期望节点数
        :type desired_node_count: int
        :param unpaid_scale_node_count: 订单未支付节点个数
        :type unpaid_scale_node_count: int
        :param existing_node_count: 
        :type existing_node_count: :class:`huaweicloudsdkcce.v3.ScaleGroupStatusExistingNodeCount`
        :param upcoming_node_count: 
        :type upcoming_node_count: :class:`huaweicloudsdkcce.v3.ScaleGroupStatusUpcomingNodeCount`
        :param scale_down_disabled_node_count: 伸缩组禁止缩容的节点数
        :type scale_down_disabled_node_count: int
        :param conditions: 伸缩组当前详细状态列表，详情参见Condition类型定义。
        :type conditions: list[:class:`huaweicloudsdkcce.v3.NodePoolCondition`]
        """
        
        

        self._name = None
        self._uid = None
        self._creation_timestamp = None
        self._update_timestamp = None
        self._phase = None
        self._desired_node_count = None
        self._unpaid_scale_node_count = None
        self._existing_node_count = None
        self._upcoming_node_count = None
        self._scale_down_disabled_node_count = None
        self._conditions = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if uid is not None:
            self.uid = uid
        if creation_timestamp is not None:
            self.creation_timestamp = creation_timestamp
        if update_timestamp is not None:
            self.update_timestamp = update_timestamp
        if phase is not None:
            self.phase = phase
        if desired_node_count is not None:
            self.desired_node_count = desired_node_count
        if unpaid_scale_node_count is not None:
            self.unpaid_scale_node_count = unpaid_scale_node_count
        if existing_node_count is not None:
            self.existing_node_count = existing_node_count
        if upcoming_node_count is not None:
            self.upcoming_node_count = upcoming_node_count
        if scale_down_disabled_node_count is not None:
            self.scale_down_disabled_node_count = scale_down_disabled_node_count
        if conditions is not None:
            self.conditions = conditions

    @property
    def name(self):
        r"""Gets the name of this ScaleGroupStatus.

        伸缩组名称

        :return: The name of this ScaleGroupStatus.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ScaleGroupStatus.

        伸缩组名称

        :param name: The name of this ScaleGroupStatus.
        :type name: str
        """
        self._name = name

    @property
    def uid(self):
        r"""Gets the uid of this ScaleGroupStatus.

        伸缩组uuid

        :return: The uid of this ScaleGroupStatus.
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        r"""Sets the uid of this ScaleGroupStatus.

        伸缩组uuid

        :param uid: The uid of this ScaleGroupStatus.
        :type uid: str
        """
        self._uid = uid

    @property
    def creation_timestamp(self):
        r"""Gets the creation_timestamp of this ScaleGroupStatus.

        伸缩组创建时间

        :return: The creation_timestamp of this ScaleGroupStatus.
        :rtype: str
        """
        return self._creation_timestamp

    @creation_timestamp.setter
    def creation_timestamp(self, creation_timestamp):
        r"""Sets the creation_timestamp of this ScaleGroupStatus.

        伸缩组创建时间

        :param creation_timestamp: The creation_timestamp of this ScaleGroupStatus.
        :type creation_timestamp: str
        """
        self._creation_timestamp = creation_timestamp

    @property
    def update_timestamp(self):
        r"""Gets the update_timestamp of this ScaleGroupStatus.

        伸缩组更新时间

        :return: The update_timestamp of this ScaleGroupStatus.
        :rtype: str
        """
        return self._update_timestamp

    @update_timestamp.setter
    def update_timestamp(self, update_timestamp):
        r"""Sets the update_timestamp of this ScaleGroupStatus.

        伸缩组更新时间

        :param update_timestamp: The update_timestamp of this ScaleGroupStatus.
        :type update_timestamp: str
        """
        self._update_timestamp = update_timestamp

    @property
    def phase(self):
        r"""Gets the phase of this ScaleGroupStatus.

        伸缩组状态。 - 空值：可用（伸缩组当前节点数已达到预期，且无伸缩中的节点） - Synchronizing：伸缩中（伸缩组当前节点数未达到预期，且无伸缩中的节点） - Synchronized：伸缩等待中（伸缩组当前节点数未达到预期，或者存在伸缩中的节点） - SoldOut：伸缩组当前不可扩容（兼容字段，标记节点池资源售罄、资源配额不足等不可扩容状态） > 上述伸缩组状态已废弃，仅兼容保留，不建议使用，替代感知方式如下： > - 伸缩组扩缩状态：可通过desiredNodeCount/existingNodeCount/upcomingNodeCount节点状态统计信息，精确感知当前伸缩组扩缩状态。 > - 伸缩组可扩容状态：可通过conditions感知伸缩组详细状态，其中\"Scalable\"可替代SoldOut语义。 - Deleting：删除中 - Error：错误 

        :return: The phase of this ScaleGroupStatus.
        :rtype: str
        """
        return self._phase

    @phase.setter
    def phase(self, phase):
        r"""Sets the phase of this ScaleGroupStatus.

        伸缩组状态。 - 空值：可用（伸缩组当前节点数已达到预期，且无伸缩中的节点） - Synchronizing：伸缩中（伸缩组当前节点数未达到预期，且无伸缩中的节点） - Synchronized：伸缩等待中（伸缩组当前节点数未达到预期，或者存在伸缩中的节点） - SoldOut：伸缩组当前不可扩容（兼容字段，标记节点池资源售罄、资源配额不足等不可扩容状态） > 上述伸缩组状态已废弃，仅兼容保留，不建议使用，替代感知方式如下： > - 伸缩组扩缩状态：可通过desiredNodeCount/existingNodeCount/upcomingNodeCount节点状态统计信息，精确感知当前伸缩组扩缩状态。 > - 伸缩组可扩容状态：可通过conditions感知伸缩组详细状态，其中\"Scalable\"可替代SoldOut语义。 - Deleting：删除中 - Error：错误 

        :param phase: The phase of this ScaleGroupStatus.
        :type phase: str
        """
        self._phase = phase

    @property
    def desired_node_count(self):
        r"""Gets the desired_node_count of this ScaleGroupStatus.

        伸缩组期望节点数

        :return: The desired_node_count of this ScaleGroupStatus.
        :rtype: int
        """
        return self._desired_node_count

    @desired_node_count.setter
    def desired_node_count(self, desired_node_count):
        r"""Sets the desired_node_count of this ScaleGroupStatus.

        伸缩组期望节点数

        :param desired_node_count: The desired_node_count of this ScaleGroupStatus.
        :type desired_node_count: int
        """
        self._desired_node_count = desired_node_count

    @property
    def unpaid_scale_node_count(self):
        r"""Gets the unpaid_scale_node_count of this ScaleGroupStatus.

        订单未支付节点个数

        :return: The unpaid_scale_node_count of this ScaleGroupStatus.
        :rtype: int
        """
        return self._unpaid_scale_node_count

    @unpaid_scale_node_count.setter
    def unpaid_scale_node_count(self, unpaid_scale_node_count):
        r"""Sets the unpaid_scale_node_count of this ScaleGroupStatus.

        订单未支付节点个数

        :param unpaid_scale_node_count: The unpaid_scale_node_count of this ScaleGroupStatus.
        :type unpaid_scale_node_count: int
        """
        self._unpaid_scale_node_count = unpaid_scale_node_count

    @property
    def existing_node_count(self):
        r"""Gets the existing_node_count of this ScaleGroupStatus.

        :return: The existing_node_count of this ScaleGroupStatus.
        :rtype: :class:`huaweicloudsdkcce.v3.ScaleGroupStatusExistingNodeCount`
        """
        return self._existing_node_count

    @existing_node_count.setter
    def existing_node_count(self, existing_node_count):
        r"""Sets the existing_node_count of this ScaleGroupStatus.

        :param existing_node_count: The existing_node_count of this ScaleGroupStatus.
        :type existing_node_count: :class:`huaweicloudsdkcce.v3.ScaleGroupStatusExistingNodeCount`
        """
        self._existing_node_count = existing_node_count

    @property
    def upcoming_node_count(self):
        r"""Gets the upcoming_node_count of this ScaleGroupStatus.

        :return: The upcoming_node_count of this ScaleGroupStatus.
        :rtype: :class:`huaweicloudsdkcce.v3.ScaleGroupStatusUpcomingNodeCount`
        """
        return self._upcoming_node_count

    @upcoming_node_count.setter
    def upcoming_node_count(self, upcoming_node_count):
        r"""Sets the upcoming_node_count of this ScaleGroupStatus.

        :param upcoming_node_count: The upcoming_node_count of this ScaleGroupStatus.
        :type upcoming_node_count: :class:`huaweicloudsdkcce.v3.ScaleGroupStatusUpcomingNodeCount`
        """
        self._upcoming_node_count = upcoming_node_count

    @property
    def scale_down_disabled_node_count(self):
        r"""Gets the scale_down_disabled_node_count of this ScaleGroupStatus.

        伸缩组禁止缩容的节点数

        :return: The scale_down_disabled_node_count of this ScaleGroupStatus.
        :rtype: int
        """
        return self._scale_down_disabled_node_count

    @scale_down_disabled_node_count.setter
    def scale_down_disabled_node_count(self, scale_down_disabled_node_count):
        r"""Sets the scale_down_disabled_node_count of this ScaleGroupStatus.

        伸缩组禁止缩容的节点数

        :param scale_down_disabled_node_count: The scale_down_disabled_node_count of this ScaleGroupStatus.
        :type scale_down_disabled_node_count: int
        """
        self._scale_down_disabled_node_count = scale_down_disabled_node_count

    @property
    def conditions(self):
        r"""Gets the conditions of this ScaleGroupStatus.

        伸缩组当前详细状态列表，详情参见Condition类型定义。

        :return: The conditions of this ScaleGroupStatus.
        :rtype: list[:class:`huaweicloudsdkcce.v3.NodePoolCondition`]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        r"""Sets the conditions of this ScaleGroupStatus.

        伸缩组当前详细状态列表，详情参见Condition类型定义。

        :param conditions: The conditions of this ScaleGroupStatus.
        :type conditions: list[:class:`huaweicloudsdkcce.v3.NodePoolCondition`]
        """
        self._conditions = conditions

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
        if not isinstance(other, ScaleGroupStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
