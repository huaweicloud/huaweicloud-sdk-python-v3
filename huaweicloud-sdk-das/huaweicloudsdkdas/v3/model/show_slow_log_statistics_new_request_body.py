# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSlowLogStatisticsNewRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'node_ids': 'list[str]',
        'statistics_field': 'str',
        'start_time': 'int',
        'end_time': 'int',
        'sort_field': 'str',
        'sort_asc': 'bool'
    }

    attribute_map = {
        'node_ids': 'node_ids',
        'statistics_field': 'statistics_field',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'sort_field': 'sort_field',
        'sort_asc': 'sort_asc'
    }

    def __init__(self, node_ids=None, statistics_field=None, start_time=None, end_time=None, sort_field=None, sort_asc=None):
        r"""ShowSlowLogStatisticsNewRequestBody

        The model defined in huaweicloud sdk

        :param node_ids: 节点ID列表
        :type node_ids: list[str]
        :param statistics_field: 统计字段，取值范围：nodeId、sqlType、dbName、collection、user、client
        :type statistics_field: str
        :param start_time: 开始时间（Unix timestamp），单位：毫秒
        :type start_time: int
        :param end_time: 结束时间（Unix timestamp），单位：毫秒
        :type end_time: int
        :param sort_field: 排序字段
        :type sort_field: str
        :param sort_asc: 排序顺序（true：正序，false：逆序）
        :type sort_asc: bool
        """
        
        

        self._node_ids = None
        self._statistics_field = None
        self._start_time = None
        self._end_time = None
        self._sort_field = None
        self._sort_asc = None
        self.discriminator = None

        if node_ids is not None:
            self.node_ids = node_ids
        self.statistics_field = statistics_field
        self.start_time = start_time
        self.end_time = end_time
        if sort_field is not None:
            self.sort_field = sort_field
        if sort_asc is not None:
            self.sort_asc = sort_asc

    @property
    def node_ids(self):
        r"""Gets the node_ids of this ShowSlowLogStatisticsNewRequestBody.

        节点ID列表

        :return: The node_ids of this ShowSlowLogStatisticsNewRequestBody.
        :rtype: list[str]
        """
        return self._node_ids

    @node_ids.setter
    def node_ids(self, node_ids):
        r"""Sets the node_ids of this ShowSlowLogStatisticsNewRequestBody.

        节点ID列表

        :param node_ids: The node_ids of this ShowSlowLogStatisticsNewRequestBody.
        :type node_ids: list[str]
        """
        self._node_ids = node_ids

    @property
    def statistics_field(self):
        r"""Gets the statistics_field of this ShowSlowLogStatisticsNewRequestBody.

        统计字段，取值范围：nodeId、sqlType、dbName、collection、user、client

        :return: The statistics_field of this ShowSlowLogStatisticsNewRequestBody.
        :rtype: str
        """
        return self._statistics_field

    @statistics_field.setter
    def statistics_field(self, statistics_field):
        r"""Sets the statistics_field of this ShowSlowLogStatisticsNewRequestBody.

        统计字段，取值范围：nodeId、sqlType、dbName、collection、user、client

        :param statistics_field: The statistics_field of this ShowSlowLogStatisticsNewRequestBody.
        :type statistics_field: str
        """
        self._statistics_field = statistics_field

    @property
    def start_time(self):
        r"""Gets the start_time of this ShowSlowLogStatisticsNewRequestBody.

        开始时间（Unix timestamp），单位：毫秒

        :return: The start_time of this ShowSlowLogStatisticsNewRequestBody.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ShowSlowLogStatisticsNewRequestBody.

        开始时间（Unix timestamp），单位：毫秒

        :param start_time: The start_time of this ShowSlowLogStatisticsNewRequestBody.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ShowSlowLogStatisticsNewRequestBody.

        结束时间（Unix timestamp），单位：毫秒

        :return: The end_time of this ShowSlowLogStatisticsNewRequestBody.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ShowSlowLogStatisticsNewRequestBody.

        结束时间（Unix timestamp），单位：毫秒

        :param end_time: The end_time of this ShowSlowLogStatisticsNewRequestBody.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def sort_field(self):
        r"""Gets the sort_field of this ShowSlowLogStatisticsNewRequestBody.

        排序字段

        :return: The sort_field of this ShowSlowLogStatisticsNewRequestBody.
        :rtype: str
        """
        return self._sort_field

    @sort_field.setter
    def sort_field(self, sort_field):
        r"""Sets the sort_field of this ShowSlowLogStatisticsNewRequestBody.

        排序字段

        :param sort_field: The sort_field of this ShowSlowLogStatisticsNewRequestBody.
        :type sort_field: str
        """
        self._sort_field = sort_field

    @property
    def sort_asc(self):
        r"""Gets the sort_asc of this ShowSlowLogStatisticsNewRequestBody.

        排序顺序（true：正序，false：逆序）

        :return: The sort_asc of this ShowSlowLogStatisticsNewRequestBody.
        :rtype: bool
        """
        return self._sort_asc

    @sort_asc.setter
    def sort_asc(self, sort_asc):
        r"""Sets the sort_asc of this ShowSlowLogStatisticsNewRequestBody.

        排序顺序（true：正序，false：逆序）

        :param sort_asc: The sort_asc of this ShowSlowLogStatisticsNewRequestBody.
        :type sort_asc: bool
        """
        self._sort_asc = sort_asc

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
        if not isinstance(other, ShowSlowLogStatisticsNewRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
