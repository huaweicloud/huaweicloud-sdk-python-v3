# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteWorkflowRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'graph_name': 'str'
    }

    attribute_map = {
        'graph_name': 'graph_name'
    }

    def __init__(self, graph_name=None):
        r"""DeleteWorkflowRequest

        The model defined in huaweicloud sdk

        :param graph_name: 工作流名称。名称必须以字母或数字开头，只能由字母、数字、下划线和中划线组成，长度小于等于64个字符，且不能重名。
        :type graph_name: str
        """
        
        

        self._graph_name = None
        self.discriminator = None

        self.graph_name = graph_name

    @property
    def graph_name(self):
        r"""Gets the graph_name of this DeleteWorkflowRequest.

        工作流名称。名称必须以字母或数字开头，只能由字母、数字、下划线和中划线组成，长度小于等于64个字符，且不能重名。

        :return: The graph_name of this DeleteWorkflowRequest.
        :rtype: str
        """
        return self._graph_name

    @graph_name.setter
    def graph_name(self, graph_name):
        r"""Sets the graph_name of this DeleteWorkflowRequest.

        工作流名称。名称必须以字母或数字开头，只能由字母、数字、下划线和中划线组成，长度小于等于64个字符，且不能重名。

        :param graph_name: The graph_name of this DeleteWorkflowRequest.
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
        if not isinstance(other, DeleteWorkflowRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
