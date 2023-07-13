# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTopologyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'global_trace_id': 'str',
        'line_list': 'list[TraceTopologyLine]',
        'node_list': 'list[TraceTopologyNode]'
    }

    attribute_map = {
        'global_trace_id': 'global_trace_id',
        'line_list': 'line_list',
        'node_list': 'node_list'
    }

    def __init__(self, global_trace_id=None, line_list=None, node_list=None):
        """ShowTopologyResponse

        The model defined in huaweicloud sdk

        :param global_trace_id: 全局traceId。
        :type global_trace_id: str
        :param line_list: 组件之间调用指向线列表。
        :type line_list: list[:class:`huaweicloudsdkapm.v1.TraceTopologyLine`]
        :param node_list: 组件节点列表。
        :type node_list: list[:class:`huaweicloudsdkapm.v1.TraceTopologyNode`]
        """
        
        super(ShowTopologyResponse, self).__init__()

        self._global_trace_id = None
        self._line_list = None
        self._node_list = None
        self.discriminator = None

        if global_trace_id is not None:
            self.global_trace_id = global_trace_id
        if line_list is not None:
            self.line_list = line_list
        if node_list is not None:
            self.node_list = node_list

    @property
    def global_trace_id(self):
        """Gets the global_trace_id of this ShowTopologyResponse.

        全局traceId。

        :return: The global_trace_id of this ShowTopologyResponse.
        :rtype: str
        """
        return self._global_trace_id

    @global_trace_id.setter
    def global_trace_id(self, global_trace_id):
        """Sets the global_trace_id of this ShowTopologyResponse.

        全局traceId。

        :param global_trace_id: The global_trace_id of this ShowTopologyResponse.
        :type global_trace_id: str
        """
        self._global_trace_id = global_trace_id

    @property
    def line_list(self):
        """Gets the line_list of this ShowTopologyResponse.

        组件之间调用指向线列表。

        :return: The line_list of this ShowTopologyResponse.
        :rtype: list[:class:`huaweicloudsdkapm.v1.TraceTopologyLine`]
        """
        return self._line_list

    @line_list.setter
    def line_list(self, line_list):
        """Sets the line_list of this ShowTopologyResponse.

        组件之间调用指向线列表。

        :param line_list: The line_list of this ShowTopologyResponse.
        :type line_list: list[:class:`huaweicloudsdkapm.v1.TraceTopologyLine`]
        """
        self._line_list = line_list

    @property
    def node_list(self):
        """Gets the node_list of this ShowTopologyResponse.

        组件节点列表。

        :return: The node_list of this ShowTopologyResponse.
        :rtype: list[:class:`huaweicloudsdkapm.v1.TraceTopologyNode`]
        """
        return self._node_list

    @node_list.setter
    def node_list(self, node_list):
        """Sets the node_list of this ShowTopologyResponse.

        组件节点列表。

        :param node_list: The node_list of this ShowTopologyResponse.
        :type node_list: list[:class:`huaweicloudsdkapm.v1.TraceTopologyNode`]
        """
        self._node_list = node_list

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
        if not isinstance(other, ShowTopologyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
