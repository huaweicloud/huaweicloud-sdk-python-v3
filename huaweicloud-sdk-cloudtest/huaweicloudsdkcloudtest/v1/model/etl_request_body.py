# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EtlRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'offset': 'int',
        'limit': 'int',
        'table_name': 'str',
        'is_bak': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'filter_time_field': 'str',
        'sort_field': 'str',
        'schema_no': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'table_name': 'table_name',
        'is_bak': 'is_bak',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'filter_time_field': 'filter_time_field',
        'sort_field': 'sort_field',
        'schema_no': 'schema_no'
    }

    def __init__(self, offset=None, limit=None, table_name=None, is_bak=None, start_time=None, end_time=None, filter_time_field=None, sort_field=None, schema_no=None):
        r"""EtlRequestBody

        The model defined in huaweicloud sdk

        :param offset: 分页偏移量
        :type offset: int
        :param limit: 分页大小，最大值1000
        :type limit: int
        :param table_name: 需要同步的表名称
        :type table_name: str
        :param is_bak: 是否是bak表数据
        :type is_bak: str
        :param start_time: 查询时间段起始时间
        :type start_time: str
        :param end_time: 查询时间段截止时间
        :type end_time: str
        :param filter_time_field: 用于时间段过滤的字段
        :type filter_time_field: str
        :param sort_field: 用于时间排序的字段，不传默认按照更新时间排序
        :type sort_field: str
        :param schema_no: 分库编号（数字类型）
        :type schema_no: str
        """
        
        

        self._offset = None
        self._limit = None
        self._table_name = None
        self._is_bak = None
        self._start_time = None
        self._end_time = None
        self._filter_time_field = None
        self._sort_field = None
        self._schema_no = None
        self.discriminator = None

        self.offset = offset
        self.limit = limit
        self.table_name = table_name
        if is_bak is not None:
            self.is_bak = is_bak
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if filter_time_field is not None:
            self.filter_time_field = filter_time_field
        if sort_field is not None:
            self.sort_field = sort_field
        self.schema_no = schema_no

    @property
    def offset(self):
        r"""Gets the offset of this EtlRequestBody.

        分页偏移量

        :return: The offset of this EtlRequestBody.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this EtlRequestBody.

        分页偏移量

        :param offset: The offset of this EtlRequestBody.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this EtlRequestBody.

        分页大小，最大值1000

        :return: The limit of this EtlRequestBody.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this EtlRequestBody.

        分页大小，最大值1000

        :param limit: The limit of this EtlRequestBody.
        :type limit: int
        """
        self._limit = limit

    @property
    def table_name(self):
        r"""Gets the table_name of this EtlRequestBody.

        需要同步的表名称

        :return: The table_name of this EtlRequestBody.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        r"""Sets the table_name of this EtlRequestBody.

        需要同步的表名称

        :param table_name: The table_name of this EtlRequestBody.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def is_bak(self):
        r"""Gets the is_bak of this EtlRequestBody.

        是否是bak表数据

        :return: The is_bak of this EtlRequestBody.
        :rtype: str
        """
        return self._is_bak

    @is_bak.setter
    def is_bak(self, is_bak):
        r"""Sets the is_bak of this EtlRequestBody.

        是否是bak表数据

        :param is_bak: The is_bak of this EtlRequestBody.
        :type is_bak: str
        """
        self._is_bak = is_bak

    @property
    def start_time(self):
        r"""Gets the start_time of this EtlRequestBody.

        查询时间段起始时间

        :return: The start_time of this EtlRequestBody.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this EtlRequestBody.

        查询时间段起始时间

        :param start_time: The start_time of this EtlRequestBody.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this EtlRequestBody.

        查询时间段截止时间

        :return: The end_time of this EtlRequestBody.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this EtlRequestBody.

        查询时间段截止时间

        :param end_time: The end_time of this EtlRequestBody.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def filter_time_field(self):
        r"""Gets the filter_time_field of this EtlRequestBody.

        用于时间段过滤的字段

        :return: The filter_time_field of this EtlRequestBody.
        :rtype: str
        """
        return self._filter_time_field

    @filter_time_field.setter
    def filter_time_field(self, filter_time_field):
        r"""Sets the filter_time_field of this EtlRequestBody.

        用于时间段过滤的字段

        :param filter_time_field: The filter_time_field of this EtlRequestBody.
        :type filter_time_field: str
        """
        self._filter_time_field = filter_time_field

    @property
    def sort_field(self):
        r"""Gets the sort_field of this EtlRequestBody.

        用于时间排序的字段，不传默认按照更新时间排序

        :return: The sort_field of this EtlRequestBody.
        :rtype: str
        """
        return self._sort_field

    @sort_field.setter
    def sort_field(self, sort_field):
        r"""Sets the sort_field of this EtlRequestBody.

        用于时间排序的字段，不传默认按照更新时间排序

        :param sort_field: The sort_field of this EtlRequestBody.
        :type sort_field: str
        """
        self._sort_field = sort_field

    @property
    def schema_no(self):
        r"""Gets the schema_no of this EtlRequestBody.

        分库编号（数字类型）

        :return: The schema_no of this EtlRequestBody.
        :rtype: str
        """
        return self._schema_no

    @schema_no.setter
    def schema_no(self, schema_no):
        r"""Sets the schema_no of this EtlRequestBody.

        分库编号（数字类型）

        :param schema_no: The schema_no of this EtlRequestBody.
        :type schema_no: str
        """
        self._schema_no = schema_no

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
        if not isinstance(other, EtlRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
