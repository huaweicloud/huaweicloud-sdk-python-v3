# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SpaceTrend:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'node_id': 'str',
        'name': 'str',
        'series': 'list[float]',
        'timestamps': 'list[int]'
    }

    attribute_map = {
        'node_id': 'node_id',
        'name': 'name',
        'series': 'series',
        'timestamps': 'timestamps'
    }

    def __init__(self, node_id=None, name=None, series=None, timestamps=None):
        r"""SpaceTrend

        The model defined in huaweicloud sdk

        :param node_id: 节点ID
        :type node_id: str
        :param name: 指标名
        :type name: str
        :param series: 指标值列表
        :type series: list[float]
        :param timestamps: 时间戳列表
        :type timestamps: list[int]
        """
        
        

        self._node_id = None
        self._name = None
        self._series = None
        self._timestamps = None
        self.discriminator = None

        if node_id is not None:
            self.node_id = node_id
        if name is not None:
            self.name = name
        if series is not None:
            self.series = series
        if timestamps is not None:
            self.timestamps = timestamps

    @property
    def node_id(self):
        r"""Gets the node_id of this SpaceTrend.

        节点ID

        :return: The node_id of this SpaceTrend.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this SpaceTrend.

        节点ID

        :param node_id: The node_id of this SpaceTrend.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def name(self):
        r"""Gets the name of this SpaceTrend.

        指标名

        :return: The name of this SpaceTrend.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this SpaceTrend.

        指标名

        :param name: The name of this SpaceTrend.
        :type name: str
        """
        self._name = name

    @property
    def series(self):
        r"""Gets the series of this SpaceTrend.

        指标值列表

        :return: The series of this SpaceTrend.
        :rtype: list[float]
        """
        return self._series

    @series.setter
    def series(self, series):
        r"""Sets the series of this SpaceTrend.

        指标值列表

        :param series: The series of this SpaceTrend.
        :type series: list[float]
        """
        self._series = series

    @property
    def timestamps(self):
        r"""Gets the timestamps of this SpaceTrend.

        时间戳列表

        :return: The timestamps of this SpaceTrend.
        :rtype: list[int]
        """
        return self._timestamps

    @timestamps.setter
    def timestamps(self, timestamps):
        r"""Sets the timestamps of this SpaceTrend.

        时间戳列表

        :param timestamps: The timestamps of this SpaceTrend.
        :type timestamps: list[int]
        """
        self._timestamps = timestamps

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
        if not isinstance(other, SpaceTrend):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
