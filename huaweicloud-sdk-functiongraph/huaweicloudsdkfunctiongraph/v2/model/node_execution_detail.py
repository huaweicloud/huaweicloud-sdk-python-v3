# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodeExecutionDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'node_id': 'str',
        'node_name': 'str',
        'execution_id': 'str',
        'executions': 'list[NodeExecution]'
    }

    attribute_map = {
        'node_id': 'node_id',
        'node_name': 'node_name',
        'execution_id': 'execution_id',
        'executions': 'executions'
    }

    def __init__(self, node_id=None, node_name=None, execution_id=None, executions=None):
        r"""NodeExecutionDetail

        The model defined in huaweicloud sdk

        :param node_id: 流程节点ID
        :type node_id: str
        :param node_name: 流程节点名称
        :type node_name: str
        :param execution_id: 流程节点执行ID
        :type execution_id: str
        :param executions: 节点执行记录
        :type executions: list[:class:`huaweicloudsdkfunctiongraph.v2.NodeExecution`]
        """
        
        

        self._node_id = None
        self._node_name = None
        self._execution_id = None
        self._executions = None
        self.discriminator = None

        if node_id is not None:
            self.node_id = node_id
        if node_name is not None:
            self.node_name = node_name
        if execution_id is not None:
            self.execution_id = execution_id
        if executions is not None:
            self.executions = executions

    @property
    def node_id(self):
        r"""Gets the node_id of this NodeExecutionDetail.

        流程节点ID

        :return: The node_id of this NodeExecutionDetail.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this NodeExecutionDetail.

        流程节点ID

        :param node_id: The node_id of this NodeExecutionDetail.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def node_name(self):
        r"""Gets the node_name of this NodeExecutionDetail.

        流程节点名称

        :return: The node_name of this NodeExecutionDetail.
        :rtype: str
        """
        return self._node_name

    @node_name.setter
    def node_name(self, node_name):
        r"""Sets the node_name of this NodeExecutionDetail.

        流程节点名称

        :param node_name: The node_name of this NodeExecutionDetail.
        :type node_name: str
        """
        self._node_name = node_name

    @property
    def execution_id(self):
        r"""Gets the execution_id of this NodeExecutionDetail.

        流程节点执行ID

        :return: The execution_id of this NodeExecutionDetail.
        :rtype: str
        """
        return self._execution_id

    @execution_id.setter
    def execution_id(self, execution_id):
        r"""Sets the execution_id of this NodeExecutionDetail.

        流程节点执行ID

        :param execution_id: The execution_id of this NodeExecutionDetail.
        :type execution_id: str
        """
        self._execution_id = execution_id

    @property
    def executions(self):
        r"""Gets the executions of this NodeExecutionDetail.

        节点执行记录

        :return: The executions of this NodeExecutionDetail.
        :rtype: list[:class:`huaweicloudsdkfunctiongraph.v2.NodeExecution`]
        """
        return self._executions

    @executions.setter
    def executions(self, executions):
        r"""Sets the executions of this NodeExecutionDetail.

        节点执行记录

        :param executions: The executions of this NodeExecutionDetail.
        :type executions: list[:class:`huaweicloudsdkfunctiongraph.v2.NodeExecution`]
        """
        self._executions = executions

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
        if not isinstance(other, NodeExecutionDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
