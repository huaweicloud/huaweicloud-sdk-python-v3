# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSpaceTrendRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'engine_type': 'str',
        'start_time': 'int',
        'end_time': 'int',
        'metric_name': 'str',
        'node_id': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'engine_type': 'engine_type',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'metric_name': 'metric_name',
        'node_id': 'node_id'
    }

    def __init__(self, instance_id=None, engine_type=None, start_time=None, end_time=None, metric_name=None, node_id=None):
        r"""ShowSpaceTrendRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param engine_type: 数据库引擎类型
        :type engine_type: str
        :param start_time: 开始时间（Unix timestamp），单位：毫秒
        :type start_time: int
        :param end_time: 结束时间（Unix timestamp），单位：毫秒
        :type end_time: int
        :param metric_name: 指标名称
        :type metric_name: str
        :param node_id: 节点ID
        :type node_id: str
        """
        
        

        self._instance_id = None
        self._engine_type = None
        self._start_time = None
        self._end_time = None
        self._metric_name = None
        self._node_id = None
        self.discriminator = None

        self.instance_id = instance_id
        self.engine_type = engine_type
        self.start_time = start_time
        self.end_time = end_time
        self.metric_name = metric_name
        if node_id is not None:
            self.node_id = node_id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ShowSpaceTrendRequest.

        实例ID

        :return: The instance_id of this ShowSpaceTrendRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ShowSpaceTrendRequest.

        实例ID

        :param instance_id: The instance_id of this ShowSpaceTrendRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def engine_type(self):
        r"""Gets the engine_type of this ShowSpaceTrendRequest.

        数据库引擎类型

        :return: The engine_type of this ShowSpaceTrendRequest.
        :rtype: str
        """
        return self._engine_type

    @engine_type.setter
    def engine_type(self, engine_type):
        r"""Sets the engine_type of this ShowSpaceTrendRequest.

        数据库引擎类型

        :param engine_type: The engine_type of this ShowSpaceTrendRequest.
        :type engine_type: str
        """
        self._engine_type = engine_type

    @property
    def start_time(self):
        r"""Gets the start_time of this ShowSpaceTrendRequest.

        开始时间（Unix timestamp），单位：毫秒

        :return: The start_time of this ShowSpaceTrendRequest.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ShowSpaceTrendRequest.

        开始时间（Unix timestamp），单位：毫秒

        :param start_time: The start_time of this ShowSpaceTrendRequest.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ShowSpaceTrendRequest.

        结束时间（Unix timestamp），单位：毫秒

        :return: The end_time of this ShowSpaceTrendRequest.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ShowSpaceTrendRequest.

        结束时间（Unix timestamp），单位：毫秒

        :param end_time: The end_time of this ShowSpaceTrendRequest.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def metric_name(self):
        r"""Gets the metric_name of this ShowSpaceTrendRequest.

        指标名称

        :return: The metric_name of this ShowSpaceTrendRequest.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        r"""Sets the metric_name of this ShowSpaceTrendRequest.

        指标名称

        :param metric_name: The metric_name of this ShowSpaceTrendRequest.
        :type metric_name: str
        """
        self._metric_name = metric_name

    @property
    def node_id(self):
        r"""Gets the node_id of this ShowSpaceTrendRequest.

        节点ID

        :return: The node_id of this ShowSpaceTrendRequest.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this ShowSpaceTrendRequest.

        节点ID

        :param node_id: The node_id of this ShowSpaceTrendRequest.
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
        if not isinstance(other, ShowSpaceTrendRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
