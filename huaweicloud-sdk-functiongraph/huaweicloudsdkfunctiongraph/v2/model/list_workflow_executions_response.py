# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListWorkflowExecutionsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'executions': 'list[FlowExecutionBrief]'
    }

    attribute_map = {
        'executions': 'executions'
    }

    def __init__(self, executions=None):
        """ListWorkflowExecutionsResponse

        The model defined in huaweicloud sdk

        :param executions: 流程执行信息列表
        :type executions: list[:class:`huaweicloudsdkfunctiongraph.v2.FlowExecutionBrief`]
        """
        
        super(ListWorkflowExecutionsResponse, self).__init__()

        self._executions = None
        self.discriminator = None

        if executions is not None:
            self.executions = executions

    @property
    def executions(self):
        """Gets the executions of this ListWorkflowExecutionsResponse.

        流程执行信息列表

        :return: The executions of this ListWorkflowExecutionsResponse.
        :rtype: list[:class:`huaweicloudsdkfunctiongraph.v2.FlowExecutionBrief`]
        """
        return self._executions

    @executions.setter
    def executions(self, executions):
        """Sets the executions of this ListWorkflowExecutionsResponse.

        流程执行信息列表

        :param executions: The executions of this ListWorkflowExecutionsResponse.
        :type executions: list[:class:`huaweicloudsdkfunctiongraph.v2.FlowExecutionBrief`]
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
        if not isinstance(other, ListWorkflowExecutionsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
