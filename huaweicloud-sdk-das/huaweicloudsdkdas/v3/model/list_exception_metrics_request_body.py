# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListExceptionMetricsRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'start_time': 'int',
        'end_time': 'int',
        'engine_type': 'str',
        'node_id': 'str',
        'metric_names': 'list[str]',
        'interval': 'str',
        'aggregation_mode': 'str'
    }

    attribute_map = {
        'start_time': 'start_time',
        'end_time': 'end_time',
        'engine_type': 'engine_type',
        'node_id': 'node_id',
        'metric_names': 'metric_names',
        'interval': 'interval',
        'aggregation_mode': 'aggregation_mode'
    }

    def __init__(self, start_time=None, end_time=None, engine_type=None, node_id=None, metric_names=None, interval=None, aggregation_mode=None):
        r"""ListExceptionMetricsRequestBody

        The model defined in huaweicloud sdk

        :param start_time: 开始时间（Unix timestamp，毫秒）
        :type start_time: int
        :param end_time: 结束时间（Unix timestamp，毫秒）
        :type end_time: int
        :param engine_type: 数据库引擎类型
        :type engine_type: str
        :param node_id: 节点ID
        :type node_id: str
        :param metric_names: CES指标名列表
        :type metric_names: list[str]
        :param interval: 聚合粒度
        :type interval: str
        :param aggregation_mode: 聚合方式
        :type aggregation_mode: str
        """
        
        

        self._start_time = None
        self._end_time = None
        self._engine_type = None
        self._node_id = None
        self._metric_names = None
        self._interval = None
        self._aggregation_mode = None
        self.discriminator = None

        self.start_time = start_time
        self.end_time = end_time
        if engine_type is not None:
            self.engine_type = engine_type
        if node_id is not None:
            self.node_id = node_id
        self.metric_names = metric_names
        self.interval = interval
        self.aggregation_mode = aggregation_mode

    @property
    def start_time(self):
        r"""Gets the start_time of this ListExceptionMetricsRequestBody.

        开始时间（Unix timestamp，毫秒）

        :return: The start_time of this ListExceptionMetricsRequestBody.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListExceptionMetricsRequestBody.

        开始时间（Unix timestamp，毫秒）

        :param start_time: The start_time of this ListExceptionMetricsRequestBody.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListExceptionMetricsRequestBody.

        结束时间（Unix timestamp，毫秒）

        :return: The end_time of this ListExceptionMetricsRequestBody.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListExceptionMetricsRequestBody.

        结束时间（Unix timestamp，毫秒）

        :param end_time: The end_time of this ListExceptionMetricsRequestBody.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def engine_type(self):
        r"""Gets the engine_type of this ListExceptionMetricsRequestBody.

        数据库引擎类型

        :return: The engine_type of this ListExceptionMetricsRequestBody.
        :rtype: str
        """
        return self._engine_type

    @engine_type.setter
    def engine_type(self, engine_type):
        r"""Sets the engine_type of this ListExceptionMetricsRequestBody.

        数据库引擎类型

        :param engine_type: The engine_type of this ListExceptionMetricsRequestBody.
        :type engine_type: str
        """
        self._engine_type = engine_type

    @property
    def node_id(self):
        r"""Gets the node_id of this ListExceptionMetricsRequestBody.

        节点ID

        :return: The node_id of this ListExceptionMetricsRequestBody.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this ListExceptionMetricsRequestBody.

        节点ID

        :param node_id: The node_id of this ListExceptionMetricsRequestBody.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def metric_names(self):
        r"""Gets the metric_names of this ListExceptionMetricsRequestBody.

        CES指标名列表

        :return: The metric_names of this ListExceptionMetricsRequestBody.
        :rtype: list[str]
        """
        return self._metric_names

    @metric_names.setter
    def metric_names(self, metric_names):
        r"""Sets the metric_names of this ListExceptionMetricsRequestBody.

        CES指标名列表

        :param metric_names: The metric_names of this ListExceptionMetricsRequestBody.
        :type metric_names: list[str]
        """
        self._metric_names = metric_names

    @property
    def interval(self):
        r"""Gets the interval of this ListExceptionMetricsRequestBody.

        聚合粒度

        :return: The interval of this ListExceptionMetricsRequestBody.
        :rtype: str
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        r"""Sets the interval of this ListExceptionMetricsRequestBody.

        聚合粒度

        :param interval: The interval of this ListExceptionMetricsRequestBody.
        :type interval: str
        """
        self._interval = interval

    @property
    def aggregation_mode(self):
        r"""Gets the aggregation_mode of this ListExceptionMetricsRequestBody.

        聚合方式

        :return: The aggregation_mode of this ListExceptionMetricsRequestBody.
        :rtype: str
        """
        return self._aggregation_mode

    @aggregation_mode.setter
    def aggregation_mode(self, aggregation_mode):
        r"""Sets the aggregation_mode of this ListExceptionMetricsRequestBody.

        聚合方式

        :param aggregation_mode: The aggregation_mode of this ListExceptionMetricsRequestBody.
        :type aggregation_mode: str
        """
        self._aggregation_mode = aggregation_mode

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
        if not isinstance(other, ListExceptionMetricsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
