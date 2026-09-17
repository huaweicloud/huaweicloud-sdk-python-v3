# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryAnalysisResultBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'datastore_type': 'str',
        'node_id': 'str',
        'start_time': 'int',
        'end_time': 'int',
        'metrics': 'list[str]',
        'action': 'str'
    }

    attribute_map = {
        'datastore_type': 'datastore_type',
        'node_id': 'node_id',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'metrics': 'metrics',
        'action': 'action'
    }

    def __init__(self, datastore_type=None, node_id=None, start_time=None, end_time=None, metrics=None, action=None):
        r"""QueryAnalysisResultBody

        The model defined in huaweicloud sdk

        :param datastore_type: 数据库引擎类型
        :type datastore_type: str
        :param node_id: 节点ID
        :type node_id: str
        :param start_time: 开始时间（Unix timestamp），单位：毫秒
        :type start_time: int
        :param end_time: 结束时间（Unix timestamp），单位：毫秒
        :type end_time: int
        :param metrics: CES指标
        :type metrics: list[str]
        :param action: 动作（relatedSqlAnalysis/slowSqlAnalysis）
        :type action: str
        """
        
        

        self._datastore_type = None
        self._node_id = None
        self._start_time = None
        self._end_time = None
        self._metrics = None
        self._action = None
        self.discriminator = None

        self.datastore_type = datastore_type
        if node_id is not None:
            self.node_id = node_id
        self.start_time = start_time
        self.end_time = end_time
        if metrics is not None:
            self.metrics = metrics
        self.action = action

    @property
    def datastore_type(self):
        r"""Gets the datastore_type of this QueryAnalysisResultBody.

        数据库引擎类型

        :return: The datastore_type of this QueryAnalysisResultBody.
        :rtype: str
        """
        return self._datastore_type

    @datastore_type.setter
    def datastore_type(self, datastore_type):
        r"""Sets the datastore_type of this QueryAnalysisResultBody.

        数据库引擎类型

        :param datastore_type: The datastore_type of this QueryAnalysisResultBody.
        :type datastore_type: str
        """
        self._datastore_type = datastore_type

    @property
    def node_id(self):
        r"""Gets the node_id of this QueryAnalysisResultBody.

        节点ID

        :return: The node_id of this QueryAnalysisResultBody.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this QueryAnalysisResultBody.

        节点ID

        :param node_id: The node_id of this QueryAnalysisResultBody.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def start_time(self):
        r"""Gets the start_time of this QueryAnalysisResultBody.

        开始时间（Unix timestamp），单位：毫秒

        :return: The start_time of this QueryAnalysisResultBody.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this QueryAnalysisResultBody.

        开始时间（Unix timestamp），单位：毫秒

        :param start_time: The start_time of this QueryAnalysisResultBody.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this QueryAnalysisResultBody.

        结束时间（Unix timestamp），单位：毫秒

        :return: The end_time of this QueryAnalysisResultBody.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this QueryAnalysisResultBody.

        结束时间（Unix timestamp），单位：毫秒

        :param end_time: The end_time of this QueryAnalysisResultBody.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def metrics(self):
        r"""Gets the metrics of this QueryAnalysisResultBody.

        CES指标

        :return: The metrics of this QueryAnalysisResultBody.
        :rtype: list[str]
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        r"""Sets the metrics of this QueryAnalysisResultBody.

        CES指标

        :param metrics: The metrics of this QueryAnalysisResultBody.
        :type metrics: list[str]
        """
        self._metrics = metrics

    @property
    def action(self):
        r"""Gets the action of this QueryAnalysisResultBody.

        动作（relatedSqlAnalysis/slowSqlAnalysis）

        :return: The action of this QueryAnalysisResultBody.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this QueryAnalysisResultBody.

        动作（relatedSqlAnalysis/slowSqlAnalysis）

        :param action: The action of this QueryAnalysisResultBody.
        :type action: str
        """
        self._action = action

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, QueryAnalysisResultBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
