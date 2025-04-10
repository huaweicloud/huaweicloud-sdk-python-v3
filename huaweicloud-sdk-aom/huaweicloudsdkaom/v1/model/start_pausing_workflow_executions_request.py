# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StartPausingWorkflowExecutionsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workflow_id': 'str',
        'execution_id': 'str',
        'action': 'str',
        'node_id': 'str'
    }

    attribute_map = {
        'workflow_id': 'workflow_id',
        'execution_id': 'execution_id',
        'action': 'action',
        'node_id': 'node_id'
    }

    def __init__(self, workflow_id=None, execution_id=None, action=None, node_id=None):
        r"""StartPausingWorkflowExecutionsRequest

        The model defined in huaweicloud sdk

        :param workflow_id: 工作流ID，唯一标识，根据project_id和workflow_name生成。
        :type workflow_id: str
        :param execution_id: 工作流执行ID。
        :type execution_id: str
        :param action: 对当前节点的操作：失败重试，失败跳过，暂停继续。 restart可重新执行失败的节点，skip可跳过失败的节点进入下个节点的执行，continue可通过暂停节点进入下一个节点。
        :type action: str
        :param node_id: 当前节点的id。
        :type node_id: str
        """
        
        

        self._workflow_id = None
        self._execution_id = None
        self._action = None
        self._node_id = None
        self.discriminator = None

        self.workflow_id = workflow_id
        self.execution_id = execution_id
        self.action = action
        self.node_id = node_id

    @property
    def workflow_id(self):
        r"""Gets the workflow_id of this StartPausingWorkflowExecutionsRequest.

        工作流ID，唯一标识，根据project_id和workflow_name生成。

        :return: The workflow_id of this StartPausingWorkflowExecutionsRequest.
        :rtype: str
        """
        return self._workflow_id

    @workflow_id.setter
    def workflow_id(self, workflow_id):
        r"""Sets the workflow_id of this StartPausingWorkflowExecutionsRequest.

        工作流ID，唯一标识，根据project_id和workflow_name生成。

        :param workflow_id: The workflow_id of this StartPausingWorkflowExecutionsRequest.
        :type workflow_id: str
        """
        self._workflow_id = workflow_id

    @property
    def execution_id(self):
        r"""Gets the execution_id of this StartPausingWorkflowExecutionsRequest.

        工作流执行ID。

        :return: The execution_id of this StartPausingWorkflowExecutionsRequest.
        :rtype: str
        """
        return self._execution_id

    @execution_id.setter
    def execution_id(self, execution_id):
        r"""Sets the execution_id of this StartPausingWorkflowExecutionsRequest.

        工作流执行ID。

        :param execution_id: The execution_id of this StartPausingWorkflowExecutionsRequest.
        :type execution_id: str
        """
        self._execution_id = execution_id

    @property
    def action(self):
        r"""Gets the action of this StartPausingWorkflowExecutionsRequest.

        对当前节点的操作：失败重试，失败跳过，暂停继续。 restart可重新执行失败的节点，skip可跳过失败的节点进入下个节点的执行，continue可通过暂停节点进入下一个节点。

        :return: The action of this StartPausingWorkflowExecutionsRequest.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this StartPausingWorkflowExecutionsRequest.

        对当前节点的操作：失败重试，失败跳过，暂停继续。 restart可重新执行失败的节点，skip可跳过失败的节点进入下个节点的执行，continue可通过暂停节点进入下一个节点。

        :param action: The action of this StartPausingWorkflowExecutionsRequest.
        :type action: str
        """
        self._action = action

    @property
    def node_id(self):
        r"""Gets the node_id of this StartPausingWorkflowExecutionsRequest.

        当前节点的id。

        :return: The node_id of this StartPausingWorkflowExecutionsRequest.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this StartPausingWorkflowExecutionsRequest.

        当前节点的id。

        :param node_id: The node_id of this StartPausingWorkflowExecutionsRequest.
        :type node_id: str
        """
        self._node_id = node_id

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
        if not isinstance(other, StartPausingWorkflowExecutionsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
