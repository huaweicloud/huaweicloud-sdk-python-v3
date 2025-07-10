# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WorkflowTemplateVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'process_nodes': 'list[WorkflowTemplateNodesVO]',
        'process_flows': 'list[WorkflowTemplateFlowsVO]'
    }

    attribute_map = {
        'process_nodes': 'processNodes',
        'process_flows': 'processFlows'
    }

    def __init__(self, process_nodes=None, process_flows=None):
        r"""WorkflowTemplateVO

        The model defined in huaweicloud sdk

        :param process_nodes: 状态流中的状态信息
        :type process_nodes: list[:class:`huaweicloudsdkprojectman.v4.WorkflowTemplateNodesVO`]
        :param process_flows: 状态流中的流转线信息
        :type process_flows: list[:class:`huaweicloudsdkprojectman.v4.WorkflowTemplateFlowsVO`]
        """
        
        

        self._process_nodes = None
        self._process_flows = None
        self.discriminator = None

        if process_nodes is not None:
            self.process_nodes = process_nodes
        if process_flows is not None:
            self.process_flows = process_flows

    @property
    def process_nodes(self):
        r"""Gets the process_nodes of this WorkflowTemplateVO.

        状态流中的状态信息

        :return: The process_nodes of this WorkflowTemplateVO.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.WorkflowTemplateNodesVO`]
        """
        return self._process_nodes

    @process_nodes.setter
    def process_nodes(self, process_nodes):
        r"""Sets the process_nodes of this WorkflowTemplateVO.

        状态流中的状态信息

        :param process_nodes: The process_nodes of this WorkflowTemplateVO.
        :type process_nodes: list[:class:`huaweicloudsdkprojectman.v4.WorkflowTemplateNodesVO`]
        """
        self._process_nodes = process_nodes

    @property
    def process_flows(self):
        r"""Gets the process_flows of this WorkflowTemplateVO.

        状态流中的流转线信息

        :return: The process_flows of this WorkflowTemplateVO.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.WorkflowTemplateFlowsVO`]
        """
        return self._process_flows

    @process_flows.setter
    def process_flows(self, process_flows):
        r"""Sets the process_flows of this WorkflowTemplateVO.

        状态流中的流转线信息

        :param process_flows: The process_flows of this WorkflowTemplateVO.
        :type process_flows: list[:class:`huaweicloudsdkprojectman.v4.WorkflowTemplateFlowsVO`]
        """
        self._process_flows = process_flows

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
        if not isinstance(other, WorkflowTemplateVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
