# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowNodeMetricsRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'metric_names': 'list[str]',
        'start_time': 'int',
        'end_time': 'int',
        'node_id': 'str'
    }

    attribute_map = {
        'metric_names': 'metric_names',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'node_id': 'node_id'
    }

    def __init__(self, metric_names=None, start_time=None, end_time=None, node_id=None):
        r"""ShowNodeMetricsRequestBody

        The model defined in huaweicloud sdk

        :param metric_names: CES指标名列表
        :type metric_names: list[str]
        :param start_time: 开始时间，Unix timestamp，单位：毫秒
        :type start_time: int
        :param end_time: 结束时间，Unix timestamp，单位：毫秒
        :type end_time: int
        :param node_id: 节点ID
        :type node_id: str
        """
        
        

        self._metric_names = None
        self._start_time = None
        self._end_time = None
        self._node_id = None
        self.discriminator = None

        self.metric_names = metric_names
        self.start_time = start_time
        self.end_time = end_time
        if node_id is not None:
            self.node_id = node_id

    @property
    def metric_names(self):
        r"""Gets the metric_names of this ShowNodeMetricsRequestBody.

        CES指标名列表

        :return: The metric_names of this ShowNodeMetricsRequestBody.
        :rtype: list[str]
        """
        return self._metric_names

    @metric_names.setter
    def metric_names(self, metric_names):
        r"""Sets the metric_names of this ShowNodeMetricsRequestBody.

        CES指标名列表

        :param metric_names: The metric_names of this ShowNodeMetricsRequestBody.
        :type metric_names: list[str]
        """
        self._metric_names = metric_names

    @property
    def start_time(self):
        r"""Gets the start_time of this ShowNodeMetricsRequestBody.

        开始时间，Unix timestamp，单位：毫秒

        :return: The start_time of this ShowNodeMetricsRequestBody.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ShowNodeMetricsRequestBody.

        开始时间，Unix timestamp，单位：毫秒

        :param start_time: The start_time of this ShowNodeMetricsRequestBody.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ShowNodeMetricsRequestBody.

        结束时间，Unix timestamp，单位：毫秒

        :return: The end_time of this ShowNodeMetricsRequestBody.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ShowNodeMetricsRequestBody.

        结束时间，Unix timestamp，单位：毫秒

        :param end_time: The end_time of this ShowNodeMetricsRequestBody.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def node_id(self):
        r"""Gets the node_id of this ShowNodeMetricsRequestBody.

        节点ID

        :return: The node_id of this ShowNodeMetricsRequestBody.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this ShowNodeMetricsRequestBody.

        节点ID

        :param node_id: The node_id of this ShowNodeMetricsRequestBody.
        :type node_id: str
        """
        self._node_id = node_id

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
        if not isinstance(other, ShowNodeMetricsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
