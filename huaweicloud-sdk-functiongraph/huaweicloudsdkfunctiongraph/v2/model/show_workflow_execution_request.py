# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowWorkflowExecutionRequest:

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
        'x_get_workflow_full_history_data': 'bool'
    }

    attribute_map = {
        'workflow_id': 'workflow_id',
        'execution_id': 'execution_id',
        'x_get_workflow_full_history_data': 'X-Get-Workflow-Full-History-Data'
    }

    def __init__(self, workflow_id=None, execution_id=None, x_get_workflow_full_history_data=None):
        r"""ShowWorkflowExecutionRequest

        The model defined in huaweicloud sdk

        :param workflow_id: 函数工作流ID
        :type workflow_id: str
        :param execution_id: 函数流执行实例ID
        :type execution_id: str
        :param x_get_workflow_full_history_data: 获取函数流执行详情完整输出值
        :type x_get_workflow_full_history_data: bool
        """
        
        

        self._workflow_id = None
        self._execution_id = None
        self._x_get_workflow_full_history_data = None
        self.discriminator = None

        self.workflow_id = workflow_id
        self.execution_id = execution_id
        if x_get_workflow_full_history_data is not None:
            self.x_get_workflow_full_history_data = x_get_workflow_full_history_data

    @property
    def workflow_id(self):
        r"""Gets the workflow_id of this ShowWorkflowExecutionRequest.

        函数工作流ID

        :return: The workflow_id of this ShowWorkflowExecutionRequest.
        :rtype: str
        """
        return self._workflow_id

    @workflow_id.setter
    def workflow_id(self, workflow_id):
        r"""Sets the workflow_id of this ShowWorkflowExecutionRequest.

        函数工作流ID

        :param workflow_id: The workflow_id of this ShowWorkflowExecutionRequest.
        :type workflow_id: str
        """
        self._workflow_id = workflow_id

    @property
    def execution_id(self):
        r"""Gets the execution_id of this ShowWorkflowExecutionRequest.

        函数流执行实例ID

        :return: The execution_id of this ShowWorkflowExecutionRequest.
        :rtype: str
        """
        return self._execution_id

    @execution_id.setter
    def execution_id(self, execution_id):
        r"""Sets the execution_id of this ShowWorkflowExecutionRequest.

        函数流执行实例ID

        :param execution_id: The execution_id of this ShowWorkflowExecutionRequest.
        :type execution_id: str
        """
        self._execution_id = execution_id

    @property
    def x_get_workflow_full_history_data(self):
        r"""Gets the x_get_workflow_full_history_data of this ShowWorkflowExecutionRequest.

        获取函数流执行详情完整输出值

        :return: The x_get_workflow_full_history_data of this ShowWorkflowExecutionRequest.
        :rtype: bool
        """
        return self._x_get_workflow_full_history_data

    @x_get_workflow_full_history_data.setter
    def x_get_workflow_full_history_data(self, x_get_workflow_full_history_data):
        r"""Sets the x_get_workflow_full_history_data of this ShowWorkflowExecutionRequest.

        获取函数流执行详情完整输出值

        :param x_get_workflow_full_history_data: The x_get_workflow_full_history_data of this ShowWorkflowExecutionRequest.
        :type x_get_workflow_full_history_data: bool
        """
        self._x_get_workflow_full_history_data = x_get_workflow_full_history_data

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
        if not isinstance(other, ShowWorkflowExecutionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
