# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WorkflowInstanceTopology:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'audit_logs': 'list[TopologyNodeInfo]'
    }

    attribute_map = {
        'audit_logs': 'audit_logs'
    }

    def __init__(self, audit_logs=None):
        r"""WorkflowInstanceTopology

        The model defined in huaweicloud sdk

        :param audit_logs: **参数解释**: 拓扑图节点信息 **约束限制**: 不涉及
        :type audit_logs: list[:class:`huaweicloudsdksecmaster.v1.TopologyNodeInfo`]
        """
        
        

        self._audit_logs = None
        self.discriminator = None

        if audit_logs is not None:
            self.audit_logs = audit_logs

    @property
    def audit_logs(self):
        r"""Gets the audit_logs of this WorkflowInstanceTopology.

        **参数解释**: 拓扑图节点信息 **约束限制**: 不涉及

        :return: The audit_logs of this WorkflowInstanceTopology.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.TopologyNodeInfo`]
        """
        return self._audit_logs

    @audit_logs.setter
    def audit_logs(self, audit_logs):
        r"""Sets the audit_logs of this WorkflowInstanceTopology.

        **参数解释**: 拓扑图节点信息 **约束限制**: 不涉及

        :param audit_logs: The audit_logs of this WorkflowInstanceTopology.
        :type audit_logs: list[:class:`huaweicloudsdksecmaster.v1.TopologyNodeInfo`]
        """
        self._audit_logs = audit_logs

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
        if not isinstance(other, WorkflowInstanceTopology):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
