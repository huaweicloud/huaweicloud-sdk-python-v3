# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListClusterActionsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_id': 'str',
        'action_name': 'str'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'action_name': 'action_name'
    }

    def __init__(self, cluster_id=None, action_name=None):
        r"""ListClusterActionsRequest

        The model defined in huaweicloud sdk

        :param cluster_id: **参数解释**： 集群ID。获取方法请参见[获取集群ID](dws_02_00068.xml)。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type cluster_id: str
        :param action_name: **参数解释**： 任务名称。当前仅部分任务在操作中阶段支持查看任务详情。 **约束限制**： 不涉及。 **取值范围**： GROWING、RESIZE_FAILURE、RESTORING、RESTORING_FAILED、SNAPSHOTTING、SNAPSHOTTING_FAILED、FINE_GRAINED_RESTORING、FINE_GRAINED_RESTORING_FAILED **默认取值**： 不涉及。
        :type action_name: str
        """
        
        

        self._cluster_id = None
        self._action_name = None
        self.discriminator = None

        self.cluster_id = cluster_id
        self.action_name = action_name

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this ListClusterActionsRequest.

        **参数解释**： 集群ID。获取方法请参见[获取集群ID](dws_02_00068.xml)。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The cluster_id of this ListClusterActionsRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this ListClusterActionsRequest.

        **参数解释**： 集群ID。获取方法请参见[获取集群ID](dws_02_00068.xml)。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param cluster_id: The cluster_id of this ListClusterActionsRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def action_name(self):
        r"""Gets the action_name of this ListClusterActionsRequest.

        **参数解释**： 任务名称。当前仅部分任务在操作中阶段支持查看任务详情。 **约束限制**： 不涉及。 **取值范围**： GROWING、RESIZE_FAILURE、RESTORING、RESTORING_FAILED、SNAPSHOTTING、SNAPSHOTTING_FAILED、FINE_GRAINED_RESTORING、FINE_GRAINED_RESTORING_FAILED **默认取值**： 不涉及。

        :return: The action_name of this ListClusterActionsRequest.
        :rtype: str
        """
        return self._action_name

    @action_name.setter
    def action_name(self, action_name):
        r"""Sets the action_name of this ListClusterActionsRequest.

        **参数解释**： 任务名称。当前仅部分任务在操作中阶段支持查看任务详情。 **约束限制**： 不涉及。 **取值范围**： GROWING、RESIZE_FAILURE、RESTORING、RESTORING_FAILED、SNAPSHOTTING、SNAPSHOTTING_FAILED、FINE_GRAINED_RESTORING、FINE_GRAINED_RESTORING_FAILED **默认取值**： 不涉及。

        :param action_name: The action_name of this ListClusterActionsRequest.
        :type action_name: str
        """
        self._action_name = action_name

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
        if not isinstance(other, ListClusterActionsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
