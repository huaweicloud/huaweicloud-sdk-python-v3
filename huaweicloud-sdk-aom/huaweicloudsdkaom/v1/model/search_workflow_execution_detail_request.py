# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchWorkflowExecutionDetailRequest:

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
        'execution_id': 'str'
    }

    attribute_map = {
        'workflow_id': 'workflow_id',
        'execution_id': 'execution_id'
    }

    def __init__(self, workflow_id=None, execution_id=None):
        """SearchWorkflowExecutionDetailRequest

        The model defined in huaweicloud sdk

        :param workflow_id: 工作流ID，唯一标识，根据project_id和workflow_name生成。
        :type workflow_id: str
        :param execution_id: 工作流执行ID，xxxxx。
        :type execution_id: str
        """
        
        

        self._workflow_id = None
        self._execution_id = None
        self.discriminator = None

        self.workflow_id = workflow_id
        self.execution_id = execution_id

    @property
    def workflow_id(self):
        """Gets the workflow_id of this SearchWorkflowExecutionDetailRequest.

        工作流ID，唯一标识，根据project_id和workflow_name生成。

        :return: The workflow_id of this SearchWorkflowExecutionDetailRequest.
        :rtype: str
        """
        return self._workflow_id

    @workflow_id.setter
    def workflow_id(self, workflow_id):
        """Sets the workflow_id of this SearchWorkflowExecutionDetailRequest.

        工作流ID，唯一标识，根据project_id和workflow_name生成。

        :param workflow_id: The workflow_id of this SearchWorkflowExecutionDetailRequest.
        :type workflow_id: str
        """
        self._workflow_id = workflow_id

    @property
    def execution_id(self):
        """Gets the execution_id of this SearchWorkflowExecutionDetailRequest.

        工作流执行ID，xxxxx。

        :return: The execution_id of this SearchWorkflowExecutionDetailRequest.
        :rtype: str
        """
        return self._execution_id

    @execution_id.setter
    def execution_id(self, execution_id):
        """Sets the execution_id of this SearchWorkflowExecutionDetailRequest.

        工作流执行ID，xxxxx。

        :param execution_id: The execution_id of this SearchWorkflowExecutionDetailRequest.
        :type execution_id: str
        """
        self._execution_id = execution_id

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
        if not isinstance(other, SearchWorkflowExecutionDetailRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
