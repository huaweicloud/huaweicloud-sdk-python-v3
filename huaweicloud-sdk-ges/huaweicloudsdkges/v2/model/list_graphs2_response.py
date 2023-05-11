# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListGraphs2Response(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'graph_count': 'int',
        'graphs': 'list[ListGraphsRespGraphs]'
    }

    attribute_map = {
        'graph_count': 'graph_count',
        'graphs': 'graphs'
    }

    def __init__(self, graph_count=None, graphs=None):
        """ListGraphs2Response

        The model defined in huaweicloud sdk

        :param graph_count: 图总个数。请求失败时为空。
        :type graph_count: int
        :param graphs: 图列表。请求失败时为空。
        :type graphs: list[:class:`huaweicloudsdkges.v2.ListGraphsRespGraphs`]
        """
        
        super(ListGraphs2Response, self).__init__()

        self._graph_count = None
        self._graphs = None
        self.discriminator = None

        if graph_count is not None:
            self.graph_count = graph_count
        if graphs is not None:
            self.graphs = graphs

    @property
    def graph_count(self):
        """Gets the graph_count of this ListGraphs2Response.

        图总个数。请求失败时为空。

        :return: The graph_count of this ListGraphs2Response.
        :rtype: int
        """
        return self._graph_count

    @graph_count.setter
    def graph_count(self, graph_count):
        """Sets the graph_count of this ListGraphs2Response.

        图总个数。请求失败时为空。

        :param graph_count: The graph_count of this ListGraphs2Response.
        :type graph_count: int
        """
        self._graph_count = graph_count

    @property
    def graphs(self):
        """Gets the graphs of this ListGraphs2Response.

        图列表。请求失败时为空。

        :return: The graphs of this ListGraphs2Response.
        :rtype: list[:class:`huaweicloudsdkges.v2.ListGraphsRespGraphs`]
        """
        return self._graphs

    @graphs.setter
    def graphs(self, graphs):
        """Sets the graphs of this ListGraphs2Response.

        图列表。请求失败时为空。

        :param graphs: The graphs of this ListGraphs2Response.
        :type graphs: list[:class:`huaweicloudsdkges.v2.ListGraphsRespGraphs`]
        """
        self._graphs = graphs

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
        if not isinstance(other, ListGraphs2Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
