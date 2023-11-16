# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FlowGraphResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'edges': 'list[FlowGraphResultEdges]',
        'vertices': 'list[Vertices]'
    }

    attribute_map = {
        'edges': 'edges',
        'vertices': 'vertices'
    }

    def __init__(self, edges=None, vertices=None):
        """FlowGraphResult

        The model defined in huaweicloud sdk

        :param edges: edges
        :type edges: list[:class:`huaweicloudsdkcodeartsbuild.v3.FlowGraphResultEdges`]
        :param vertices: record信息
        :type vertices: list[:class:`huaweicloudsdkcodeartsbuild.v3.Vertices`]
        """
        
        

        self._edges = None
        self._vertices = None
        self.discriminator = None

        if edges is not None:
            self.edges = edges
        if vertices is not None:
            self.vertices = vertices

    @property
    def edges(self):
        """Gets the edges of this FlowGraphResult.

        edges

        :return: The edges of this FlowGraphResult.
        :rtype: list[:class:`huaweicloudsdkcodeartsbuild.v3.FlowGraphResultEdges`]
        """
        return self._edges

    @edges.setter
    def edges(self, edges):
        """Sets the edges of this FlowGraphResult.

        edges

        :param edges: The edges of this FlowGraphResult.
        :type edges: list[:class:`huaweicloudsdkcodeartsbuild.v3.FlowGraphResultEdges`]
        """
        self._edges = edges

    @property
    def vertices(self):
        """Gets the vertices of this FlowGraphResult.

        record信息

        :return: The vertices of this FlowGraphResult.
        :rtype: list[:class:`huaweicloudsdkcodeartsbuild.v3.Vertices`]
        """
        return self._vertices

    @vertices.setter
    def vertices(self, vertices):
        """Sets the vertices of this FlowGraphResult.

        record信息

        :param vertices: The vertices of this FlowGraphResult.
        :type vertices: list[:class:`huaweicloudsdkcodeartsbuild.v3.Vertices`]
        """
        self._vertices = vertices

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
        if not isinstance(other, FlowGraphResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
