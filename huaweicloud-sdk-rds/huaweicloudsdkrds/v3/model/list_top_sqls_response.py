# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTopSqlsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_count': 'int',
        'list': 'list[QueryTopSqlsResult]',
        'avg_cpu_time_top_values': 'list[TopSqlsTimeResult]',
        'avg_duration_time_top_values': 'list[TopSqlsTimeResult]',
        'avg_rows_top_values': 'list[TopSqlsRowResult]',
        'avg_logical_top_values': 'list[TopSqlsLogicalReadResult]',
        'total_cpu_time_top_values': 'list[TopSqlsTimeResult]',
        'total_duration_time_top_values': 'list[TopSqlsTimeResult]',
        'total_rows_top_values': 'list[TopSqlsRowResult]',
        'total_logical_reads_top_values': 'list[TopSqlsLogicalReadResult]'
    }

    attribute_map = {
        'total_count': 'total_count',
        'list': 'list',
        'avg_cpu_time_top_values': 'avg_cpu_time_top_values',
        'avg_duration_time_top_values': 'avg_duration_time_top_values',
        'avg_rows_top_values': 'avg_rows_top_values',
        'avg_logical_top_values': 'avg_logical_top_values',
        'total_cpu_time_top_values': 'total_cpu_time_top_values',
        'total_duration_time_top_values': 'total_duration_time_top_values',
        'total_rows_top_values': 'total_rows_top_values',
        'total_logical_reads_top_values': 'total_logical_reads_top_values'
    }

    def __init__(self, total_count=None, list=None, avg_cpu_time_top_values=None, avg_duration_time_top_values=None, avg_rows_top_values=None, avg_logical_top_values=None, total_cpu_time_top_values=None, total_duration_time_top_values=None, total_rows_top_values=None, total_logical_reads_top_values=None):
        r"""ListTopSqlsResponse

        The model defined in huaweicloud sdk

        :param total_count: 总数。
        :type total_count: int
        :param list: TOP SQL 信息列表。
        :type list: list[:class:`huaweicloudsdkrds.v3.QueryTopSqlsResult`]
        :param avg_cpu_time_top_values: 平均CPU开销表TOP SQL列表。
        :type avg_cpu_time_top_values: list[:class:`huaweicloudsdkrds.v3.TopSqlsTimeResult`]
        :param avg_duration_time_top_values: 平均执行耗时TOP SQL列表。
        :type avg_duration_time_top_values: list[:class:`huaweicloudsdkrds.v3.TopSqlsTimeResult`]
        :param avg_rows_top_values: 平均返回行TOP SQL列表。
        :type avg_rows_top_values: list[:class:`huaweicloudsdkrds.v3.TopSqlsRowResult`]
        :param avg_logical_top_values: 平均逻辑读TOP SQL列表。
        :type avg_logical_top_values: list[:class:`huaweicloudsdkrds.v3.TopSqlsLogicalReadResult`]
        :param total_cpu_time_top_values: 总CPU开销表TOP SQL列表。
        :type total_cpu_time_top_values: list[:class:`huaweicloudsdkrds.v3.TopSqlsTimeResult`]
        :param total_duration_time_top_values: 总执行耗时TOP SQL列表。
        :type total_duration_time_top_values: list[:class:`huaweicloudsdkrds.v3.TopSqlsTimeResult`]
        :param total_rows_top_values: 总返回行TOP SQL列表。
        :type total_rows_top_values: list[:class:`huaweicloudsdkrds.v3.TopSqlsRowResult`]
        :param total_logical_reads_top_values: 总逻辑读TOP SQL列表。
        :type total_logical_reads_top_values: list[:class:`huaweicloudsdkrds.v3.TopSqlsLogicalReadResult`]
        """
        
        super().__init__()

        self._total_count = None
        self._list = None
        self._avg_cpu_time_top_values = None
        self._avg_duration_time_top_values = None
        self._avg_rows_top_values = None
        self._avg_logical_top_values = None
        self._total_cpu_time_top_values = None
        self._total_duration_time_top_values = None
        self._total_rows_top_values = None
        self._total_logical_reads_top_values = None
        self.discriminator = None

        if total_count is not None:
            self.total_count = total_count
        if list is not None:
            self.list = list
        if avg_cpu_time_top_values is not None:
            self.avg_cpu_time_top_values = avg_cpu_time_top_values
        if avg_duration_time_top_values is not None:
            self.avg_duration_time_top_values = avg_duration_time_top_values
        if avg_rows_top_values is not None:
            self.avg_rows_top_values = avg_rows_top_values
        if avg_logical_top_values is not None:
            self.avg_logical_top_values = avg_logical_top_values
        if total_cpu_time_top_values is not None:
            self.total_cpu_time_top_values = total_cpu_time_top_values
        if total_duration_time_top_values is not None:
            self.total_duration_time_top_values = total_duration_time_top_values
        if total_rows_top_values is not None:
            self.total_rows_top_values = total_rows_top_values
        if total_logical_reads_top_values is not None:
            self.total_logical_reads_top_values = total_logical_reads_top_values

    @property
    def total_count(self):
        r"""Gets the total_count of this ListTopSqlsResponse.

        总数。

        :return: The total_count of this ListTopSqlsResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListTopSqlsResponse.

        总数。

        :param total_count: The total_count of this ListTopSqlsResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def list(self):
        r"""Gets the list of this ListTopSqlsResponse.

        TOP SQL 信息列表。

        :return: The list of this ListTopSqlsResponse.
        :rtype: list[:class:`huaweicloudsdkrds.v3.QueryTopSqlsResult`]
        """
        return self._list

    @list.setter
    def list(self, list):
        r"""Sets the list of this ListTopSqlsResponse.

        TOP SQL 信息列表。

        :param list: The list of this ListTopSqlsResponse.
        :type list: list[:class:`huaweicloudsdkrds.v3.QueryTopSqlsResult`]
        """
        self._list = list

    @property
    def avg_cpu_time_top_values(self):
        r"""Gets the avg_cpu_time_top_values of this ListTopSqlsResponse.

        平均CPU开销表TOP SQL列表。

        :return: The avg_cpu_time_top_values of this ListTopSqlsResponse.
        :rtype: list[:class:`huaweicloudsdkrds.v3.TopSqlsTimeResult`]
        """
        return self._avg_cpu_time_top_values

    @avg_cpu_time_top_values.setter
    def avg_cpu_time_top_values(self, avg_cpu_time_top_values):
        r"""Sets the avg_cpu_time_top_values of this ListTopSqlsResponse.

        平均CPU开销表TOP SQL列表。

        :param avg_cpu_time_top_values: The avg_cpu_time_top_values of this ListTopSqlsResponse.
        :type avg_cpu_time_top_values: list[:class:`huaweicloudsdkrds.v3.TopSqlsTimeResult`]
        """
        self._avg_cpu_time_top_values = avg_cpu_time_top_values

    @property
    def avg_duration_time_top_values(self):
        r"""Gets the avg_duration_time_top_values of this ListTopSqlsResponse.

        平均执行耗时TOP SQL列表。

        :return: The avg_duration_time_top_values of this ListTopSqlsResponse.
        :rtype: list[:class:`huaweicloudsdkrds.v3.TopSqlsTimeResult`]
        """
        return self._avg_duration_time_top_values

    @avg_duration_time_top_values.setter
    def avg_duration_time_top_values(self, avg_duration_time_top_values):
        r"""Sets the avg_duration_time_top_values of this ListTopSqlsResponse.

        平均执行耗时TOP SQL列表。

        :param avg_duration_time_top_values: The avg_duration_time_top_values of this ListTopSqlsResponse.
        :type avg_duration_time_top_values: list[:class:`huaweicloudsdkrds.v3.TopSqlsTimeResult`]
        """
        self._avg_duration_time_top_values = avg_duration_time_top_values

    @property
    def avg_rows_top_values(self):
        r"""Gets the avg_rows_top_values of this ListTopSqlsResponse.

        平均返回行TOP SQL列表。

        :return: The avg_rows_top_values of this ListTopSqlsResponse.
        :rtype: list[:class:`huaweicloudsdkrds.v3.TopSqlsRowResult`]
        """
        return self._avg_rows_top_values

    @avg_rows_top_values.setter
    def avg_rows_top_values(self, avg_rows_top_values):
        r"""Sets the avg_rows_top_values of this ListTopSqlsResponse.

        平均返回行TOP SQL列表。

        :param avg_rows_top_values: The avg_rows_top_values of this ListTopSqlsResponse.
        :type avg_rows_top_values: list[:class:`huaweicloudsdkrds.v3.TopSqlsRowResult`]
        """
        self._avg_rows_top_values = avg_rows_top_values

    @property
    def avg_logical_top_values(self):
        r"""Gets the avg_logical_top_values of this ListTopSqlsResponse.

        平均逻辑读TOP SQL列表。

        :return: The avg_logical_top_values of this ListTopSqlsResponse.
        :rtype: list[:class:`huaweicloudsdkrds.v3.TopSqlsLogicalReadResult`]
        """
        return self._avg_logical_top_values

    @avg_logical_top_values.setter
    def avg_logical_top_values(self, avg_logical_top_values):
        r"""Sets the avg_logical_top_values of this ListTopSqlsResponse.

        平均逻辑读TOP SQL列表。

        :param avg_logical_top_values: The avg_logical_top_values of this ListTopSqlsResponse.
        :type avg_logical_top_values: list[:class:`huaweicloudsdkrds.v3.TopSqlsLogicalReadResult`]
        """
        self._avg_logical_top_values = avg_logical_top_values

    @property
    def total_cpu_time_top_values(self):
        r"""Gets the total_cpu_time_top_values of this ListTopSqlsResponse.

        总CPU开销表TOP SQL列表。

        :return: The total_cpu_time_top_values of this ListTopSqlsResponse.
        :rtype: list[:class:`huaweicloudsdkrds.v3.TopSqlsTimeResult`]
        """
        return self._total_cpu_time_top_values

    @total_cpu_time_top_values.setter
    def total_cpu_time_top_values(self, total_cpu_time_top_values):
        r"""Sets the total_cpu_time_top_values of this ListTopSqlsResponse.

        总CPU开销表TOP SQL列表。

        :param total_cpu_time_top_values: The total_cpu_time_top_values of this ListTopSqlsResponse.
        :type total_cpu_time_top_values: list[:class:`huaweicloudsdkrds.v3.TopSqlsTimeResult`]
        """
        self._total_cpu_time_top_values = total_cpu_time_top_values

    @property
    def total_duration_time_top_values(self):
        r"""Gets the total_duration_time_top_values of this ListTopSqlsResponse.

        总执行耗时TOP SQL列表。

        :return: The total_duration_time_top_values of this ListTopSqlsResponse.
        :rtype: list[:class:`huaweicloudsdkrds.v3.TopSqlsTimeResult`]
        """
        return self._total_duration_time_top_values

    @total_duration_time_top_values.setter
    def total_duration_time_top_values(self, total_duration_time_top_values):
        r"""Sets the total_duration_time_top_values of this ListTopSqlsResponse.

        总执行耗时TOP SQL列表。

        :param total_duration_time_top_values: The total_duration_time_top_values of this ListTopSqlsResponse.
        :type total_duration_time_top_values: list[:class:`huaweicloudsdkrds.v3.TopSqlsTimeResult`]
        """
        self._total_duration_time_top_values = total_duration_time_top_values

    @property
    def total_rows_top_values(self):
        r"""Gets the total_rows_top_values of this ListTopSqlsResponse.

        总返回行TOP SQL列表。

        :return: The total_rows_top_values of this ListTopSqlsResponse.
        :rtype: list[:class:`huaweicloudsdkrds.v3.TopSqlsRowResult`]
        """
        return self._total_rows_top_values

    @total_rows_top_values.setter
    def total_rows_top_values(self, total_rows_top_values):
        r"""Sets the total_rows_top_values of this ListTopSqlsResponse.

        总返回行TOP SQL列表。

        :param total_rows_top_values: The total_rows_top_values of this ListTopSqlsResponse.
        :type total_rows_top_values: list[:class:`huaweicloudsdkrds.v3.TopSqlsRowResult`]
        """
        self._total_rows_top_values = total_rows_top_values

    @property
    def total_logical_reads_top_values(self):
        r"""Gets the total_logical_reads_top_values of this ListTopSqlsResponse.

        总逻辑读TOP SQL列表。

        :return: The total_logical_reads_top_values of this ListTopSqlsResponse.
        :rtype: list[:class:`huaweicloudsdkrds.v3.TopSqlsLogicalReadResult`]
        """
        return self._total_logical_reads_top_values

    @total_logical_reads_top_values.setter
    def total_logical_reads_top_values(self, total_logical_reads_top_values):
        r"""Sets the total_logical_reads_top_values of this ListTopSqlsResponse.

        总逻辑读TOP SQL列表。

        :param total_logical_reads_top_values: The total_logical_reads_top_values of this ListTopSqlsResponse.
        :type total_logical_reads_top_values: list[:class:`huaweicloudsdkrds.v3.TopSqlsLogicalReadResult`]
        """
        self._total_logical_reads_top_values = total_logical_reads_top_values

    def to_dict(self):
        import warnings
        warnings.warn("ListTopSqlsResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ListTopSqlsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
