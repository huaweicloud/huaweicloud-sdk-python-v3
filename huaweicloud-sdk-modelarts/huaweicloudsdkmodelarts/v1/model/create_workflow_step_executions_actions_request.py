# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateWorkflowStepExecutionsActionsRequest:

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
        'step_execution_id': 'str',
        'body': 'StepExecutionAction'
    }

    attribute_map = {
        'workflow_id': 'workflow_id',
        'execution_id': 'execution_id',
        'step_execution_id': 'step_execution_id',
        'body': 'body'
    }

    def __init__(self, workflow_id=None, execution_id=None, step_execution_id=None, body=None):
        r"""CreateWorkflowStepExecutionsActionsRequest

        The model defined in huaweicloud sdk

        :param workflow_id: 工作流的ID。
        :type workflow_id: str
        :param execution_id: 工作流执行ID。
        :type execution_id: str
        :param step_execution_id: 工作流的一次执行中一个节点的执行ID。
        :type step_execution_id: str
        :param body: Body of the CreateWorkflowStepExecutionsActionsRequest
        :type body: :class:`huaweicloudsdkmodelarts.v1.StepExecutionAction`
        """
        
        

        self._workflow_id = None
        self._execution_id = None
        self._step_execution_id = None
        self._body = None
        self.discriminator = None

        self.workflow_id = workflow_id
        self.execution_id = execution_id
        self.step_execution_id = step_execution_id
        if body is not None:
            self.body = body

    @property
    def workflow_id(self):
        r"""Gets the workflow_id of this CreateWorkflowStepExecutionsActionsRequest.

        工作流的ID。

        :return: The workflow_id of this CreateWorkflowStepExecutionsActionsRequest.
        :rtype: str
        """
        return self._workflow_id

    @workflow_id.setter
    def workflow_id(self, workflow_id):
        r"""Sets the workflow_id of this CreateWorkflowStepExecutionsActionsRequest.

        工作流的ID。

        :param workflow_id: The workflow_id of this CreateWorkflowStepExecutionsActionsRequest.
        :type workflow_id: str
        """
        self._workflow_id = workflow_id

    @property
    def execution_id(self):
        r"""Gets the execution_id of this CreateWorkflowStepExecutionsActionsRequest.

        工作流执行ID。

        :return: The execution_id of this CreateWorkflowStepExecutionsActionsRequest.
        :rtype: str
        """
        return self._execution_id

    @execution_id.setter
    def execution_id(self, execution_id):
        r"""Sets the execution_id of this CreateWorkflowStepExecutionsActionsRequest.

        工作流执行ID。

        :param execution_id: The execution_id of this CreateWorkflowStepExecutionsActionsRequest.
        :type execution_id: str
        """
        self._execution_id = execution_id

    @property
    def step_execution_id(self):
        r"""Gets the step_execution_id of this CreateWorkflowStepExecutionsActionsRequest.

        工作流的一次执行中一个节点的执行ID。

        :return: The step_execution_id of this CreateWorkflowStepExecutionsActionsRequest.
        :rtype: str
        """
        return self._step_execution_id

    @step_execution_id.setter
    def step_execution_id(self, step_execution_id):
        r"""Sets the step_execution_id of this CreateWorkflowStepExecutionsActionsRequest.

        工作流的一次执行中一个节点的执行ID。

        :param step_execution_id: The step_execution_id of this CreateWorkflowStepExecutionsActionsRequest.
        :type step_execution_id: str
        """
        self._step_execution_id = step_execution_id

    @property
    def body(self):
        r"""Gets the body of this CreateWorkflowStepExecutionsActionsRequest.

        :return: The body of this CreateWorkflowStepExecutionsActionsRequest.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.StepExecutionAction`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this CreateWorkflowStepExecutionsActionsRequest.

        :param body: The body of this CreateWorkflowStepExecutionsActionsRequest.
        :type body: :class:`huaweicloudsdkmodelarts.v1.StepExecutionAction`
        """
        self._body = body

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
        if not isinstance(other, CreateWorkflowStepExecutionsActionsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
