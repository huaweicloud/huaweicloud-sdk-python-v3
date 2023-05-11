# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StartSyncWorkflowExecutionRequest:

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
        'body': 'FlowExecuteBody'
    }

    attribute_map = {
        'workflow_id': 'workflow_id',
        'body': 'body'
    }

    def __init__(self, workflow_id=None, body=None):
        """StartSyncWorkflowExecutionRequest

        The model defined in huaweicloud sdk

        :param workflow_id: 函数流定义ID
        :type workflow_id: str
        :param body: Body of the StartSyncWorkflowExecutionRequest
        :type body: :class:`huaweicloudsdkfunctiongraph.v2.FlowExecuteBody`
        """
        
        

        self._workflow_id = None
        self._body = None
        self.discriminator = None

        self.workflow_id = workflow_id
        if body is not None:
            self.body = body

    @property
    def workflow_id(self):
        """Gets the workflow_id of this StartSyncWorkflowExecutionRequest.

        函数流定义ID

        :return: The workflow_id of this StartSyncWorkflowExecutionRequest.
        :rtype: str
        """
        return self._workflow_id

    @workflow_id.setter
    def workflow_id(self, workflow_id):
        """Sets the workflow_id of this StartSyncWorkflowExecutionRequest.

        函数流定义ID

        :param workflow_id: The workflow_id of this StartSyncWorkflowExecutionRequest.
        :type workflow_id: str
        """
        self._workflow_id = workflow_id

    @property
    def body(self):
        """Gets the body of this StartSyncWorkflowExecutionRequest.

        :return: The body of this StartSyncWorkflowExecutionRequest.
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.FlowExecuteBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this StartSyncWorkflowExecutionRequest.

        :param body: The body of this StartSyncWorkflowExecutionRequest.
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
        if not isinstance(other, StartSyncWorkflowExecutionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
