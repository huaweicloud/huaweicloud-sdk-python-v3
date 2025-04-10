# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Parameters:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'schema_path': 'str',
        'edgeset_path': 'str',
        'edgeset_format': 'str',
        'edgeset_default_label': 'str',
        'vertexset_path': 'str',
        'vertexset_format': 'str',
        'vertexset_default_label': 'str',
        'log_dir': 'str',
        'parallel_edge': 'ParallelEdge'
    }

    attribute_map = {
        'schema_path': 'schemaPath',
        'edgeset_path': 'edgesetPath',
        'edgeset_format': 'edgesetFormat',
        'edgeset_default_label': 'edgesetDefaultLabel',
        'vertexset_path': 'vertexsetPath',
        'vertexset_format': 'vertexsetFormat',
        'vertexset_default_label': 'vertexsetDefaultLabel',
        'log_dir': 'logDir',
        'parallel_edge': 'parallelEdge'
    }

    def __init__(self, schema_path=None, edgeset_path=None, edgeset_format=None, edgeset_default_label=None, vertexset_path=None, vertexset_format=None, vertexset_default_label=None, log_dir=None, parallel_edge=None):
        r"""Parameters

        The model defined in huaweicloud sdk

        :param schema_path: 元数据文件OBS路径，只支持文件。
        :type schema_path: str
        :param edgeset_path: 边数据集文件OBS路径，只支持文件。
        :type edgeset_path: str
        :param edgeset_format: 边数据集格式。当前仅支持csv。  默认为csv。
        :type edgeset_format: str
        :param edgeset_default_label: 边数据集默认标签，当前默认为空，可以不填。
        :type edgeset_default_label: str
        :param vertexset_path: 点数据集OBS路径，只支持文件。
        :type vertexset_path: str
        :param vertexset_format: 点数据集格式。当前仅支持csv。  默认为csv。
        :type vertexset_format: str
        :param vertexset_default_label: 点数据集默认标签，当前默认为空，可以不填。
        :type vertexset_default_label: str
        :param log_dir: OBS日志存储目录，用于存储建图过程导入失败的数据和详细日志。
        :type log_dir: str
        :param parallel_edge: 
        :type parallel_edge: :class:`huaweicloudsdkges.v1.ParallelEdge`
        """
        
        

        self._schema_path = None
        self._edgeset_path = None
        self._edgeset_format = None
        self._edgeset_default_label = None
        self._vertexset_path = None
        self._vertexset_format = None
        self._vertexset_default_label = None
        self._log_dir = None
        self._parallel_edge = None
        self.discriminator = None

        self.schema_path = schema_path
        self.edgeset_path = edgeset_path
        if edgeset_format is not None:
            self.edgeset_format = edgeset_format
        if edgeset_default_label is not None:
            self.edgeset_default_label = edgeset_default_label
        if vertexset_path is not None:
            self.vertexset_path = vertexset_path
        if vertexset_format is not None:
            self.vertexset_format = vertexset_format
        if vertexset_default_label is not None:
            self.vertexset_default_label = vertexset_default_label
        if log_dir is not None:
            self.log_dir = log_dir
        if parallel_edge is not None:
            self.parallel_edge = parallel_edge

    @property
    def schema_path(self):
        r"""Gets the schema_path of this Parameters.

        元数据文件OBS路径，只支持文件。

        :return: The schema_path of this Parameters.
        :rtype: str
        """
        return self._schema_path

    @schema_path.setter
    def schema_path(self, schema_path):
        r"""Sets the schema_path of this Parameters.

        元数据文件OBS路径，只支持文件。

        :param schema_path: The schema_path of this Parameters.
        :type schema_path: str
        """
        self._schema_path = schema_path

    @property
    def edgeset_path(self):
        r"""Gets the edgeset_path of this Parameters.

        边数据集文件OBS路径，只支持文件。

        :return: The edgeset_path of this Parameters.
        :rtype: str
        """
        return self._edgeset_path

    @edgeset_path.setter
    def edgeset_path(self, edgeset_path):
        r"""Sets the edgeset_path of this Parameters.

        边数据集文件OBS路径，只支持文件。

        :param edgeset_path: The edgeset_path of this Parameters.
        :type edgeset_path: str
        """
        self._edgeset_path = edgeset_path

    @property
    def edgeset_format(self):
        r"""Gets the edgeset_format of this Parameters.

        边数据集格式。当前仅支持csv。  默认为csv。

        :return: The edgeset_format of this Parameters.
        :rtype: str
        """
        return self._edgeset_format

    @edgeset_format.setter
    def edgeset_format(self, edgeset_format):
        r"""Sets the edgeset_format of this Parameters.

        边数据集格式。当前仅支持csv。  默认为csv。

        :param edgeset_format: The edgeset_format of this Parameters.
        :type edgeset_format: str
        """
        self._edgeset_format = edgeset_format

    @property
    def edgeset_default_label(self):
        r"""Gets the edgeset_default_label of this Parameters.

        边数据集默认标签，当前默认为空，可以不填。

        :return: The edgeset_default_label of this Parameters.
        :rtype: str
        """
        return self._edgeset_default_label

    @edgeset_default_label.setter
    def edgeset_default_label(self, edgeset_default_label):
        r"""Sets the edgeset_default_label of this Parameters.

        边数据集默认标签，当前默认为空，可以不填。

        :param edgeset_default_label: The edgeset_default_label of this Parameters.
        :type edgeset_default_label: str
        """
        self._edgeset_default_label = edgeset_default_label

    @property
    def vertexset_path(self):
        r"""Gets the vertexset_path of this Parameters.

        点数据集OBS路径，只支持文件。

        :return: The vertexset_path of this Parameters.
        :rtype: str
        """
        return self._vertexset_path

    @vertexset_path.setter
    def vertexset_path(self, vertexset_path):
        r"""Sets the vertexset_path of this Parameters.

        点数据集OBS路径，只支持文件。

        :param vertexset_path: The vertexset_path of this Parameters.
        :type vertexset_path: str
        """
        self._vertexset_path = vertexset_path

    @property
    def vertexset_format(self):
        r"""Gets the vertexset_format of this Parameters.

        点数据集格式。当前仅支持csv。  默认为csv。

        :return: The vertexset_format of this Parameters.
        :rtype: str
        """
        return self._vertexset_format

    @vertexset_format.setter
    def vertexset_format(self, vertexset_format):
        r"""Sets the vertexset_format of this Parameters.

        点数据集格式。当前仅支持csv。  默认为csv。

        :param vertexset_format: The vertexset_format of this Parameters.
        :type vertexset_format: str
        """
        self._vertexset_format = vertexset_format

    @property
    def vertexset_default_label(self):
        r"""Gets the vertexset_default_label of this Parameters.

        点数据集默认标签，当前默认为空，可以不填。

        :return: The vertexset_default_label of this Parameters.
        :rtype: str
        """
        return self._vertexset_default_label

    @vertexset_default_label.setter
    def vertexset_default_label(self, vertexset_default_label):
        r"""Sets the vertexset_default_label of this Parameters.

        点数据集默认标签，当前默认为空，可以不填。

        :param vertexset_default_label: The vertexset_default_label of this Parameters.
        :type vertexset_default_label: str
        """
        self._vertexset_default_label = vertexset_default_label

    @property
    def log_dir(self):
        r"""Gets the log_dir of this Parameters.

        OBS日志存储目录，用于存储建图过程导入失败的数据和详细日志。

        :return: The log_dir of this Parameters.
        :rtype: str
        """
        return self._log_dir

    @log_dir.setter
    def log_dir(self, log_dir):
        r"""Sets the log_dir of this Parameters.

        OBS日志存储目录，用于存储建图过程导入失败的数据和详细日志。

        :param log_dir: The log_dir of this Parameters.
        :type log_dir: str
        """
        self._log_dir = log_dir

    @property
    def parallel_edge(self):
        r"""Gets the parallel_edge of this Parameters.

        :return: The parallel_edge of this Parameters.
        :rtype: :class:`huaweicloudsdkges.v1.ParallelEdge`
        """
        return self._parallel_edge

    @parallel_edge.setter
    def parallel_edge(self, parallel_edge):
        r"""Sets the parallel_edge of this Parameters.

        :param parallel_edge: The parallel_edge of this Parameters.
        :type parallel_edge: :class:`huaweicloudsdkges.v1.ParallelEdge`
        """
        self._parallel_edge = parallel_edge

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
        if not isinstance(other, Parameters):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
