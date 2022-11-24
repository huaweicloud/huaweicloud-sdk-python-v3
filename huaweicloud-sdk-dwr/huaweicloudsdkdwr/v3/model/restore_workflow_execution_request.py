# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RestoreWorkflowExecutionRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'execution_name': 'str',
        'graph_name': 'str'
    }

    attribute_map = {
        'execution_name': 'execution_name',
        'graph_name': 'graph_name'
    }

    def __init__(self, execution_name=None, graph_name=None):
        """RestoreWorkflowExecutionRequest

        The model defined in huaweicloud sdk

        :param execution_name: 工作流实例名。
        :type execution_name: str
        :param graph_name: 工作流名。
        :type graph_name: str
        """
        
        

        self._execution_name = None
        self._graph_name = None
        self.discriminator = None

        self.execution_name = execution_name
        self.graph_name = graph_name

    @property
    def execution_name(self):
        """Gets the execution_name of this RestoreWorkflowExecutionRequest.

        工作流实例名。

        :return: The execution_name of this RestoreWorkflowExecutionRequest.
        :rtype: str
        """
        return self._execution_name

    @execution_name.setter
    def execution_name(self, execution_name):
        """Sets the execution_name of this RestoreWorkflowExecutionRequest.

        工作流实例名。

        :param execution_name: The execution_name of this RestoreWorkflowExecutionRequest.
        :type execution_name: str
        """
        self._execution_name = execution_name

    @property
    def graph_name(self):
        """Gets the graph_name of this RestoreWorkflowExecutionRequest.

        工作流名。

        :return: The graph_name of this RestoreWorkflowExecutionRequest.
        :rtype: str
        """
        return self._graph_name

    @graph_name.setter
    def graph_name(self, graph_name):
        """Sets the graph_name of this RestoreWorkflowExecutionRequest.

        工作流名。

        :param graph_name: The graph_name of this RestoreWorkflowExecutionRequest.
        :type graph_name: str
        """
        self._graph_name = graph_name

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
        if not isinstance(other, RestoreWorkflowExecutionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
