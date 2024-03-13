# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodeCheckStatus:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'phase': 'str',
        'node_stage_status': 'list[NodeStageStatus]'
    }

    attribute_map = {
        'phase': 'phase',
        'node_stage_status': 'nodeStageStatus'
    }

    def __init__(self, phase=None, node_stage_status=None):
        """NodeCheckStatus

        The model defined in huaweicloud sdk

        :param phase: 状态，取值如下 - Init: 初始化 - Running 运行中 - Success 成功 - Failed 失败
        :type phase: str
        :param node_stage_status: 节点检查状态
        :type node_stage_status: list[:class:`huaweicloudsdkcce.v3.NodeStageStatus`]
        """
        
        

        self._phase = None
        self._node_stage_status = None
        self.discriminator = None

        if phase is not None:
            self.phase = phase
        if node_stage_status is not None:
            self.node_stage_status = node_stage_status

    @property
    def phase(self):
        """Gets the phase of this NodeCheckStatus.

        状态，取值如下 - Init: 初始化 - Running 运行中 - Success 成功 - Failed 失败

        :return: The phase of this NodeCheckStatus.
        :rtype: str
        """
        return self._phase

    @phase.setter
    def phase(self, phase):
        """Sets the phase of this NodeCheckStatus.

        状态，取值如下 - Init: 初始化 - Running 运行中 - Success 成功 - Failed 失败

        :param phase: The phase of this NodeCheckStatus.
        :type phase: str
        """
        self._phase = phase

    @property
    def node_stage_status(self):
        """Gets the node_stage_status of this NodeCheckStatus.

        节点检查状态

        :return: The node_stage_status of this NodeCheckStatus.
        :rtype: list[:class:`huaweicloudsdkcce.v3.NodeStageStatus`]
        """
        return self._node_stage_status

    @node_stage_status.setter
    def node_stage_status(self, node_stage_status):
        """Sets the node_stage_status of this NodeCheckStatus.

        节点检查状态

        :param node_stage_status: The node_stage_status of this NodeCheckStatus.
        :type node_stage_status: list[:class:`huaweicloudsdkcce.v3.NodeStageStatus`]
        """
        self._node_stage_status = node_stage_status

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
        if not isinstance(other, NodeCheckStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
