# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportGraphReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'graph_export_path': 'str',
        'edge_set_name': 'str',
        'vertex_set_name': 'str',
        'schema_name': 'str',
        'paginate': 'ExportGraphReqPaginate'
    }

    attribute_map = {
        'graph_export_path': 'graph_export_path',
        'edge_set_name': 'edge_set_name',
        'vertex_set_name': 'vertex_set_name',
        'schema_name': 'schema_name',
        'paginate': 'paginate'
    }

    def __init__(self, graph_export_path=None, edge_set_name=None, vertex_set_name=None, schema_name=None, paginate=None):
        r"""ExportGraphReq

        The model defined in huaweicloud sdk

        :param graph_export_path: 图的导出OBS路径。
        :type graph_export_path: str
        :param edge_set_name: 导出边文件名。
        :type edge_set_name: str
        :param vertex_set_name: 导出点文件名。
        :type vertex_set_name: str
        :param schema_name: 导出元数据文件名。
        :type schema_name: str
        :param paginate: 
        :type paginate: :class:`huaweicloudsdkges.v2.ExportGraphReqPaginate`
        """
        
        

        self._graph_export_path = None
        self._edge_set_name = None
        self._vertex_set_name = None
        self._schema_name = None
        self._paginate = None
        self.discriminator = None

        self.graph_export_path = graph_export_path
        self.edge_set_name = edge_set_name
        self.vertex_set_name = vertex_set_name
        self.schema_name = schema_name
        if paginate is not None:
            self.paginate = paginate

    @property
    def graph_export_path(self):
        r"""Gets the graph_export_path of this ExportGraphReq.

        图的导出OBS路径。

        :return: The graph_export_path of this ExportGraphReq.
        :rtype: str
        """
        return self._graph_export_path

    @graph_export_path.setter
    def graph_export_path(self, graph_export_path):
        r"""Sets the graph_export_path of this ExportGraphReq.

        图的导出OBS路径。

        :param graph_export_path: The graph_export_path of this ExportGraphReq.
        :type graph_export_path: str
        """
        self._graph_export_path = graph_export_path

    @property
    def edge_set_name(self):
        r"""Gets the edge_set_name of this ExportGraphReq.

        导出边文件名。

        :return: The edge_set_name of this ExportGraphReq.
        :rtype: str
        """
        return self._edge_set_name

    @edge_set_name.setter
    def edge_set_name(self, edge_set_name):
        r"""Sets the edge_set_name of this ExportGraphReq.

        导出边文件名。

        :param edge_set_name: The edge_set_name of this ExportGraphReq.
        :type edge_set_name: str
        """
        self._edge_set_name = edge_set_name

    @property
    def vertex_set_name(self):
        r"""Gets the vertex_set_name of this ExportGraphReq.

        导出点文件名。

        :return: The vertex_set_name of this ExportGraphReq.
        :rtype: str
        """
        return self._vertex_set_name

    @vertex_set_name.setter
    def vertex_set_name(self, vertex_set_name):
        r"""Sets the vertex_set_name of this ExportGraphReq.

        导出点文件名。

        :param vertex_set_name: The vertex_set_name of this ExportGraphReq.
        :type vertex_set_name: str
        """
        self._vertex_set_name = vertex_set_name

    @property
    def schema_name(self):
        r"""Gets the schema_name of this ExportGraphReq.

        导出元数据文件名。

        :return: The schema_name of this ExportGraphReq.
        :rtype: str
        """
        return self._schema_name

    @schema_name.setter
    def schema_name(self, schema_name):
        r"""Sets the schema_name of this ExportGraphReq.

        导出元数据文件名。

        :param schema_name: The schema_name of this ExportGraphReq.
        :type schema_name: str
        """
        self._schema_name = schema_name

    @property
    def paginate(self):
        r"""Gets the paginate of this ExportGraphReq.

        :return: The paginate of this ExportGraphReq.
        :rtype: :class:`huaweicloudsdkges.v2.ExportGraphReqPaginate`
        """
        return self._paginate

    @paginate.setter
    def paginate(self, paginate):
        r"""Sets the paginate of this ExportGraphReq.

        :param paginate: The paginate of this ExportGraphReq.
        :type paginate: :class:`huaweicloudsdkges.v2.ExportGraphReqPaginate`
        """
        self._paginate = paginate

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
        if not isinstance(other, ExportGraphReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
