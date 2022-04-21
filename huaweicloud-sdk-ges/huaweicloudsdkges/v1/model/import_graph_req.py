# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImportGraphReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'edgeset_path': 'str',
        'edgeset_format': 'str',
        'vertexset_path': 'str',
        'vertexset_format': 'str',
        'schema_path': 'str',
        'log_dir': 'str',
        'parallel_edge': 'object',
        'action': 'str',
        'ignore_label': 'bool',
        'delimiter': 'str',
        'trim_quote': 'str',
        'offline': 'bool'
    }

    attribute_map = {
        'edgeset_path': 'edgesetPath',
        'edgeset_format': 'edgesetFormat',
        'vertexset_path': 'vertexsetPath',
        'vertexset_format': 'vertexsetFormat',
        'schema_path': 'schemaPath',
        'log_dir': 'logDir',
        'parallel_edge': 'parallelEdge',
        'action': 'action',
        'ignore_label': 'ignoreLabel',
        'delimiter': 'delimiter',
        'trim_quote': 'trimQuote',
        'offline': 'offline'
    }

    def __init__(self, edgeset_path=None, edgeset_format=None, vertexset_path=None, vertexset_format=None, schema_path=None, log_dir=None, parallel_edge=None, action=None, ignore_label=None, delimiter=None, trim_quote=None, offline=None):
        """ImportGraphReq

        The model defined in huaweicloud sdk

        :param edgeset_path: 边文件目录或边文件名。
        :type edgeset_path: str
        :param edgeset_format: 边数据集格式。当前仅支持csv。  默认为csv。
        :type edgeset_format: str
        :param vertexset_path: 点文件目录或点文件名。
        :type vertexset_path: str
        :param vertexset_format: 点数据集格式。当前仅支持csv。  默认为csv。
        :type vertexset_format: str
        :param schema_path: 新增数据的元数据文件路径。
        :type schema_path: str
        :param log_dir: 导入图日志存放目录，用于存储导入失败的数据和详细错入原因。
        :type log_dir: str
        :param parallel_edge: 重复边处理
        :type parallel_edge: object
        :param action: 处理方式，取值为allow，ignore和override，默认为allow。 - allow表示允许重复边。 - ignore表示忽略之后的重复边。 - override表示覆盖之前的重复边。
        :type action: str
        :param ignore_label: 重复边的定义，是否忽略Label。取值为true或者false，默认取true。 - true 表示重复边定义不包含Label，即用&lt;源点，终点&gt;标记一条边，不包含Label。 - false 表示重复边定义包含Label，即用&lt;源点，终点，Label&gt;标记一条边。
        :type ignore_label: bool
        :param delimiter: csv格式文件字段分隔符，默认值为逗号（,）。list/set类型的字段内元素分隔符默认为分号（;）。
        :type delimiter: str
        :param trim_quote: csv格式文件字段包围符，默认值为双引号（\&quot;）。用来包围一个字段，如字段中含有分隔符或者换行等。
        :type trim_quote: str
        :param offline: 是否离线导入，取值为true或者false，默认取false。 - true 表示离线导入，导入速度较快，但导入过程中图处于锁定状态，不可读不可写。 - false 表示在线导入，相对离线导入，在线导入速度略慢，但导入过程中图并未锁定，可读不可写。
        :type offline: bool
        """
        
        

        self._edgeset_path = None
        self._edgeset_format = None
        self._vertexset_path = None
        self._vertexset_format = None
        self._schema_path = None
        self._log_dir = None
        self._parallel_edge = None
        self._action = None
        self._ignore_label = None
        self._delimiter = None
        self._trim_quote = None
        self._offline = None
        self.discriminator = None

        if edgeset_path is not None:
            self.edgeset_path = edgeset_path
        if edgeset_format is not None:
            self.edgeset_format = edgeset_format
        if vertexset_path is not None:
            self.vertexset_path = vertexset_path
        if vertexset_format is not None:
            self.vertexset_format = vertexset_format
        if schema_path is not None:
            self.schema_path = schema_path
        if log_dir is not None:
            self.log_dir = log_dir
        if parallel_edge is not None:
            self.parallel_edge = parallel_edge
        if action is not None:
            self.action = action
        if ignore_label is not None:
            self.ignore_label = ignore_label
        if delimiter is not None:
            self.delimiter = delimiter
        if trim_quote is not None:
            self.trim_quote = trim_quote
        if offline is not None:
            self.offline = offline

    @property
    def edgeset_path(self):
        """Gets the edgeset_path of this ImportGraphReq.

        边文件目录或边文件名。

        :return: The edgeset_path of this ImportGraphReq.
        :rtype: str
        """
        return self._edgeset_path

    @edgeset_path.setter
    def edgeset_path(self, edgeset_path):
        """Sets the edgeset_path of this ImportGraphReq.

        边文件目录或边文件名。

        :param edgeset_path: The edgeset_path of this ImportGraphReq.
        :type edgeset_path: str
        """
        self._edgeset_path = edgeset_path

    @property
    def edgeset_format(self):
        """Gets the edgeset_format of this ImportGraphReq.

        边数据集格式。当前仅支持csv。  默认为csv。

        :return: The edgeset_format of this ImportGraphReq.
        :rtype: str
        """
        return self._edgeset_format

    @edgeset_format.setter
    def edgeset_format(self, edgeset_format):
        """Sets the edgeset_format of this ImportGraphReq.

        边数据集格式。当前仅支持csv。  默认为csv。

        :param edgeset_format: The edgeset_format of this ImportGraphReq.
        :type edgeset_format: str
        """
        self._edgeset_format = edgeset_format

    @property
    def vertexset_path(self):
        """Gets the vertexset_path of this ImportGraphReq.

        点文件目录或点文件名。

        :return: The vertexset_path of this ImportGraphReq.
        :rtype: str
        """
        return self._vertexset_path

    @vertexset_path.setter
    def vertexset_path(self, vertexset_path):
        """Sets the vertexset_path of this ImportGraphReq.

        点文件目录或点文件名。

        :param vertexset_path: The vertexset_path of this ImportGraphReq.
        :type vertexset_path: str
        """
        self._vertexset_path = vertexset_path

    @property
    def vertexset_format(self):
        """Gets the vertexset_format of this ImportGraphReq.

        点数据集格式。当前仅支持csv。  默认为csv。

        :return: The vertexset_format of this ImportGraphReq.
        :rtype: str
        """
        return self._vertexset_format

    @vertexset_format.setter
    def vertexset_format(self, vertexset_format):
        """Sets the vertexset_format of this ImportGraphReq.

        点数据集格式。当前仅支持csv。  默认为csv。

        :param vertexset_format: The vertexset_format of this ImportGraphReq.
        :type vertexset_format: str
        """
        self._vertexset_format = vertexset_format

    @property
    def schema_path(self):
        """Gets the schema_path of this ImportGraphReq.

        新增数据的元数据文件路径。

        :return: The schema_path of this ImportGraphReq.
        :rtype: str
        """
        return self._schema_path

    @schema_path.setter
    def schema_path(self, schema_path):
        """Sets the schema_path of this ImportGraphReq.

        新增数据的元数据文件路径。

        :param schema_path: The schema_path of this ImportGraphReq.
        :type schema_path: str
        """
        self._schema_path = schema_path

    @property
    def log_dir(self):
        """Gets the log_dir of this ImportGraphReq.

        导入图日志存放目录，用于存储导入失败的数据和详细错入原因。

        :return: The log_dir of this ImportGraphReq.
        :rtype: str
        """
        return self._log_dir

    @log_dir.setter
    def log_dir(self, log_dir):
        """Sets the log_dir of this ImportGraphReq.

        导入图日志存放目录，用于存储导入失败的数据和详细错入原因。

        :param log_dir: The log_dir of this ImportGraphReq.
        :type log_dir: str
        """
        self._log_dir = log_dir

    @property
    def parallel_edge(self):
        """Gets the parallel_edge of this ImportGraphReq.

        重复边处理

        :return: The parallel_edge of this ImportGraphReq.
        :rtype: object
        """
        return self._parallel_edge

    @parallel_edge.setter
    def parallel_edge(self, parallel_edge):
        """Sets the parallel_edge of this ImportGraphReq.

        重复边处理

        :param parallel_edge: The parallel_edge of this ImportGraphReq.
        :type parallel_edge: object
        """
        self._parallel_edge = parallel_edge

    @property
    def action(self):
        """Gets the action of this ImportGraphReq.

        处理方式，取值为allow，ignore和override，默认为allow。 - allow表示允许重复边。 - ignore表示忽略之后的重复边。 - override表示覆盖之前的重复边。

        :return: The action of this ImportGraphReq.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this ImportGraphReq.

        处理方式，取值为allow，ignore和override，默认为allow。 - allow表示允许重复边。 - ignore表示忽略之后的重复边。 - override表示覆盖之前的重复边。

        :param action: The action of this ImportGraphReq.
        :type action: str
        """
        self._action = action

    @property
    def ignore_label(self):
        """Gets the ignore_label of this ImportGraphReq.

        重复边的定义，是否忽略Label。取值为true或者false，默认取true。 - true 表示重复边定义不包含Label，即用<源点，终点>标记一条边，不包含Label。 - false 表示重复边定义包含Label，即用<源点，终点，Label>标记一条边。

        :return: The ignore_label of this ImportGraphReq.
        :rtype: bool
        """
        return self._ignore_label

    @ignore_label.setter
    def ignore_label(self, ignore_label):
        """Sets the ignore_label of this ImportGraphReq.

        重复边的定义，是否忽略Label。取值为true或者false，默认取true。 - true 表示重复边定义不包含Label，即用<源点，终点>标记一条边，不包含Label。 - false 表示重复边定义包含Label，即用<源点，终点，Label>标记一条边。

        :param ignore_label: The ignore_label of this ImportGraphReq.
        :type ignore_label: bool
        """
        self._ignore_label = ignore_label

    @property
    def delimiter(self):
        """Gets the delimiter of this ImportGraphReq.

        csv格式文件字段分隔符，默认值为逗号（,）。list/set类型的字段内元素分隔符默认为分号（;）。

        :return: The delimiter of this ImportGraphReq.
        :rtype: str
        """
        return self._delimiter

    @delimiter.setter
    def delimiter(self, delimiter):
        """Sets the delimiter of this ImportGraphReq.

        csv格式文件字段分隔符，默认值为逗号（,）。list/set类型的字段内元素分隔符默认为分号（;）。

        :param delimiter: The delimiter of this ImportGraphReq.
        :type delimiter: str
        """
        self._delimiter = delimiter

    @property
    def trim_quote(self):
        """Gets the trim_quote of this ImportGraphReq.

        csv格式文件字段包围符，默认值为双引号（\"）。用来包围一个字段，如字段中含有分隔符或者换行等。

        :return: The trim_quote of this ImportGraphReq.
        :rtype: str
        """
        return self._trim_quote

    @trim_quote.setter
    def trim_quote(self, trim_quote):
        """Sets the trim_quote of this ImportGraphReq.

        csv格式文件字段包围符，默认值为双引号（\"）。用来包围一个字段，如字段中含有分隔符或者换行等。

        :param trim_quote: The trim_quote of this ImportGraphReq.
        :type trim_quote: str
        """
        self._trim_quote = trim_quote

    @property
    def offline(self):
        """Gets the offline of this ImportGraphReq.

        是否离线导入，取值为true或者false，默认取false。 - true 表示离线导入，导入速度较快，但导入过程中图处于锁定状态，不可读不可写。 - false 表示在线导入，相对离线导入，在线导入速度略慢，但导入过程中图并未锁定，可读不可写。

        :return: The offline of this ImportGraphReq.
        :rtype: bool
        """
        return self._offline

    @offline.setter
    def offline(self, offline):
        """Sets the offline of this ImportGraphReq.

        是否离线导入，取值为true或者false，默认取false。 - true 表示离线导入，导入速度较快，但导入过程中图处于锁定状态，不可读不可写。 - false 表示在线导入，相对离线导入，在线导入速度略慢，但导入过程中图并未锁定，可读不可写。

        :param offline: The offline of this ImportGraphReq.
        :type offline: bool
        """
        self._offline = offline

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
        if not isinstance(other, ImportGraphReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
