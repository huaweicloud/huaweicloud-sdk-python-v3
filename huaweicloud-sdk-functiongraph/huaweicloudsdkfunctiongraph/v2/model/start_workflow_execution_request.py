# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StartWorkflowExecutionRequest:

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
        'x_create_time': 'str',
        'x_workflow_run_id': 'str',
        'x_workflow_run_merge_fn_parameters': 'str',
        'body': 'FlowExecuteBody'
    }

    attribute_map = {
        'workflow_id': 'workflow_id',
        'x_create_time': 'X-Create-Time',
        'x_workflow_run_id': 'X-WorkflowRun-ID',
        'x_workflow_run_merge_fn_parameters': 'X-WorkflowRun-MergeFnParameters',
        'body': 'body'
    }

    def __init__(self, workflow_id=None, x_create_time=None, x_workflow_run_id=None, x_workflow_run_merge_fn_parameters=None, body=None):
        """StartWorkflowExecutionRequest

        The model defined in huaweicloud sdk

        :param workflow_id: 函数流定义ID
        :type workflow_id: str
        :param x_create_time: workflowRun task create time
        :type x_create_time: str
        :param x_workflow_run_id: workflowRun id
        :type x_workflow_run_id: str
        :param x_workflow_run_merge_fn_parameters: Combines the output of the previous node with the input of the next node into an input.
        :type x_workflow_run_merge_fn_parameters: str
        :param body: Body of the StartWorkflowExecutionRequest
        :type body: :class:`huaweicloudsdkfunctiongraph.v2.FlowExecuteBody`
        """
        
        

        self._workflow_id = None
        self._x_create_time = None
        self._x_workflow_run_id = None
        self._x_workflow_run_merge_fn_parameters = None
        self._body = None
        self.discriminator = None

        self.workflow_id = workflow_id
        if x_create_time is not None:
            self.x_create_time = x_create_time
        if x_workflow_run_id is not None:
            self.x_workflow_run_id = x_workflow_run_id
        if x_workflow_run_merge_fn_parameters is not None:
            self.x_workflow_run_merge_fn_parameters = x_workflow_run_merge_fn_parameters
        if body is not None:
            self.body = body

    @property
    def workflow_id(self):
        """Gets the workflow_id of this StartWorkflowExecutionRequest.

        函数流定义ID

        :return: The workflow_id of this StartWorkflowExecutionRequest.
        :rtype: str
        """
        return self._workflow_id

    @workflow_id.setter
    def workflow_id(self, workflow_id):
        """Sets the workflow_id of this StartWorkflowExecutionRequest.

        函数流定义ID

        :param workflow_id: The workflow_id of this StartWorkflowExecutionRequest.
        :type workflow_id: str
        """
        self._workflow_id = workflow_id

    @property
    def x_create_time(self):
        """Gets the x_create_time of this StartWorkflowExecutionRequest.

        workflowRun task create time

        :return: The x_create_time of this StartWorkflowExecutionRequest.
        :rtype: str
        """
        return self._x_create_time

    @x_create_time.setter
    def x_create_time(self, x_create_time):
        """Sets the x_create_time of this StartWorkflowExecutionRequest.

        workflowRun task create time

        :param x_create_time: The x_create_time of this StartWorkflowExecutionRequest.
        :type x_create_time: str
        """
        self._x_create_time = x_create_time

    @property
    def x_workflow_run_id(self):
        """Gets the x_workflow_run_id of this StartWorkflowExecutionRequest.

        workflowRun id

        :return: The x_workflow_run_id of this StartWorkflowExecutionRequest.
        :rtype: str
        """
        return self._x_workflow_run_id

    @x_workflow_run_id.setter
    def x_workflow_run_id(self, x_workflow_run_id):
        """Sets the x_workflow_run_id of this StartWorkflowExecutionRequest.

        workflowRun id

        :param x_workflow_run_id: The x_workflow_run_id of this StartWorkflowExecutionRequest.
        :type x_workflow_run_id: str
        """
        self._x_workflow_run_id = x_workflow_run_id

    @property
    def x_workflow_run_merge_fn_parameters(self):
        """Gets the x_workflow_run_merge_fn_parameters of this StartWorkflowExecutionRequest.

        Combines the output of the previous node with the input of the next node into an input.

        :return: The x_workflow_run_merge_fn_parameters of this StartWorkflowExecutionRequest.
        :rtype: str
        """
        return self._x_workflow_run_merge_fn_parameters

    @x_workflow_run_merge_fn_parameters.setter
    def x_workflow_run_merge_fn_parameters(self, x_workflow_run_merge_fn_parameters):
        """Sets the x_workflow_run_merge_fn_parameters of this StartWorkflowExecutionRequest.

        Combines the output of the previous node with the input of the next node into an input.

        :param x_workflow_run_merge_fn_parameters: The x_workflow_run_merge_fn_parameters of this StartWorkflowExecutionRequest.
        :type x_workflow_run_merge_fn_parameters: str
        """
        self._x_workflow_run_merge_fn_parameters = x_workflow_run_merge_fn_parameters

    @property
    def body(self):
        """Gets the body of this StartWorkflowExecutionRequest.


        :return: The body of this StartWorkflowExecutionRequest.
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.FlowExecuteBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this StartWorkflowExecutionRequest.


        :param body: The body of this StartWorkflowExecutionRequest.
        :type body: :class:`huaweicloudsdkfunctiongraph.v2.FlowExecuteBody`
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
        if not isinstance(other, StartWorkflowExecutionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
