# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateCallbackWorkflowRequest:

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
        'x_workflow_run_id': 'str',
        'x_workflow_state_id': 'str',
        'body': 'CallbackWorkflowRequestBody'
    }

    attribute_map = {
        'workflow_id': 'workflow_id',
        'x_workflow_run_id': 'X-Workflow-Run-Id',
        'x_workflow_state_id': 'X-Workflow-State-Id',
        'body': 'body'
    }

    def __init__(self, workflow_id=None, x_workflow_run_id=None, x_workflow_state_id=None, body=None):
        """CreateCallbackWorkflowRequest

        The model defined in huaweicloud sdk

        :param workflow_id: 函数工作流ID
        :type workflow_id: str
        :param x_workflow_run_id: workflow run id
        :type x_workflow_run_id: str
        :param x_workflow_state_id: workflow state id
        :type x_workflow_state_id: str
        :param body: Body of the CreateCallbackWorkflowRequest
        :type body: :class:`huaweicloudsdkfunctiongraph.v2.CallbackWorkflowRequestBody`
        """
        
        

        self._workflow_id = None
        self._x_workflow_run_id = None
        self._x_workflow_state_id = None
        self._body = None
        self.discriminator = None

        self.workflow_id = workflow_id
        self.x_workflow_run_id = x_workflow_run_id
        self.x_workflow_state_id = x_workflow_state_id
        if body is not None:
            self.body = body

    @property
    def workflow_id(self):
        """Gets the workflow_id of this CreateCallbackWorkflowRequest.

        函数工作流ID

        :return: The workflow_id of this CreateCallbackWorkflowRequest.
        :rtype: str
        """
        return self._workflow_id

    @workflow_id.setter
    def workflow_id(self, workflow_id):
        """Sets the workflow_id of this CreateCallbackWorkflowRequest.

        函数工作流ID

        :param workflow_id: The workflow_id of this CreateCallbackWorkflowRequest.
        :type workflow_id: str
        """
        self._workflow_id = workflow_id

    @property
    def x_workflow_run_id(self):
        """Gets the x_workflow_run_id of this CreateCallbackWorkflowRequest.

        workflow run id

        :return: The x_workflow_run_id of this CreateCallbackWorkflowRequest.
        :rtype: str
        """
        return self._x_workflow_run_id

    @x_workflow_run_id.setter
    def x_workflow_run_id(self, x_workflow_run_id):
        """Sets the x_workflow_run_id of this CreateCallbackWorkflowRequest.

        workflow run id

        :param x_workflow_run_id: The x_workflow_run_id of this CreateCallbackWorkflowRequest.
        :type x_workflow_run_id: str
        """
        self._x_workflow_run_id = x_workflow_run_id

    @property
    def x_workflow_state_id(self):
        """Gets the x_workflow_state_id of this CreateCallbackWorkflowRequest.

        workflow state id

        :return: The x_workflow_state_id of this CreateCallbackWorkflowRequest.
        :rtype: str
        """
        return self._x_workflow_state_id

    @x_workflow_state_id.setter
    def x_workflow_state_id(self, x_workflow_state_id):
        """Sets the x_workflow_state_id of this CreateCallbackWorkflowRequest.

        workflow state id

        :param x_workflow_state_id: The x_workflow_state_id of this CreateCallbackWorkflowRequest.
        :type x_workflow_state_id: str
        """
        self._x_workflow_state_id = x_workflow_state_id

    @property
    def body(self):
        """Gets the body of this CreateCallbackWorkflowRequest.

        :return: The body of this CreateCallbackWorkflowRequest.
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.CallbackWorkflowRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this CreateCallbackWorkflowRequest.

        :param body: The body of this CreateCallbackWorkflowRequest.
        :type body: :class:`huaweicloudsdkfunctiongraph.v2.CallbackWorkflowRequestBody`
        """
        self._body = body

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
        if not isinstance(other, CreateCallbackWorkflowRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
