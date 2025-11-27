# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInspectionReportRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'start_at': 'int',
        'end_at': 'int',
        'datastore_type': 'str',
        'health_rank': 'str',
        'sort_field': 'str',
        'asc': 'bool',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'start_at': 'start_at',
        'end_at': 'end_at',
        'datastore_type': 'datastore_type',
        'health_rank': 'health_rank',
        'sort_field': 'sort_field',
        'asc': 'asc',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, start_at=None, end_at=None, datastore_type=None, health_rank=None, sort_field=None, asc=None, offset=None, limit=None):
        r"""ListInspectionReportRequest

        The model defined in huaweicloud sdk

        :param start_at: 开始时间（Unix timestamp），单位：毫秒。
        :type start_at: int
        :param end_at: 结束时间（Unix timestamp），单位：毫秒。
        :type end_at: int
        :param datastore_type: 数据库类型。支持MySQL、TaurusDB、GaussDB、MariaDB。
        :type datastore_type: str
        :param health_rank: 健康等级
        :type health_rank: str
        :param sort_field: 排序字段
        :type sort_field: str
        :param asc: 排序顺序（true:正序, false:逆序）
        :type asc: bool
        :param offset: 偏移量
        :type offset: int
        :param limit: 每页记录数
        :type limit: int
        """
        
        

        self._start_at = None
        self._end_at = None
        self._datastore_type = None
        self._health_rank = None
        self._sort_field = None
        self._asc = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.start_at = start_at
        self.end_at = end_at
        self.datastore_type = datastore_type
        if health_rank is not None:
            self.health_rank = health_rank
        if sort_field is not None:
            self.sort_field = sort_field
        if asc is not None:
            self.asc = asc
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def start_at(self):
        r"""Gets the start_at of this ListInspectionReportRequest.

        开始时间（Unix timestamp），单位：毫秒。

        :return: The start_at of this ListInspectionReportRequest.
        :rtype: int
        """
        return self._start_at

    @start_at.setter
    def start_at(self, start_at):
        r"""Sets the start_at of this ListInspectionReportRequest.

        开始时间（Unix timestamp），单位：毫秒。

        :param start_at: The start_at of this ListInspectionReportRequest.
        :type start_at: int
        """
        self._start_at = start_at

    @property
    def end_at(self):
        r"""Gets the end_at of this ListInspectionReportRequest.

        结束时间（Unix timestamp），单位：毫秒。

        :return: The end_at of this ListInspectionReportRequest.
        :rtype: int
        """
        return self._end_at

    @end_at.setter
    def end_at(self, end_at):
        r"""Sets the end_at of this ListInspectionReportRequest.

        结束时间（Unix timestamp），单位：毫秒。

        :param end_at: The end_at of this ListInspectionReportRequest.
        :type end_at: int
        """
        self._end_at = end_at

    @property
    def datastore_type(self):
        r"""Gets the datastore_type of this ListInspectionReportRequest.

        数据库类型。支持MySQL、TaurusDB、GaussDB、MariaDB。

        :return: The datastore_type of this ListInspectionReportRequest.
        :rtype: str
        """
        return self._datastore_type

    @datastore_type.setter
    def datastore_type(self, datastore_type):
        r"""Sets the datastore_type of this ListInspectionReportRequest.

        数据库类型。支持MySQL、TaurusDB、GaussDB、MariaDB。

        :param datastore_type: The datastore_type of this ListInspectionReportRequest.
        :type datastore_type: str
        """
        self._datastore_type = datastore_type

    @property
    def health_rank(self):
        r"""Gets the health_rank of this ListInspectionReportRequest.

        健康等级

        :return: The health_rank of this ListInspectionReportRequest.
        :rtype: str
        """
        return self._health_rank

    @health_rank.setter
    def health_rank(self, health_rank):
        r"""Sets the health_rank of this ListInspectionReportRequest.

        健康等级

        :param health_rank: The health_rank of this ListInspectionReportRequest.
        :type health_rank: str
        """
        self._health_rank = health_rank

    @property
    def sort_field(self):
        r"""Gets the sort_field of this ListInspectionReportRequest.

        排序字段

        :return: The sort_field of this ListInspectionReportRequest.
        :rtype: str
        """
        return self._sort_field

    @sort_field.setter
    def sort_field(self, sort_field):
        r"""Sets the sort_field of this ListInspectionReportRequest.

        排序字段

        :param sort_field: The sort_field of this ListInspectionReportRequest.
        :type sort_field: str
        """
        self._sort_field = sort_field

    @property
    def asc(self):
        r"""Gets the asc of this ListInspectionReportRequest.

        排序顺序（true:正序, false:逆序）

        :return: The asc of this ListInspectionReportRequest.
        :rtype: bool
        """
        return self._asc

    @asc.setter
    def asc(self, asc):
        r"""Sets the asc of this ListInspectionReportRequest.

        排序顺序（true:正序, false:逆序）

        :param asc: The asc of this ListInspectionReportRequest.
        :type asc: bool
        """
        self._asc = asc

    @property
    def offset(self):
        r"""Gets the offset of this ListInspectionReportRequest.

        偏移量

        :return: The offset of this ListInspectionReportRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListInspectionReportRequest.

        偏移量

        :param offset: The offset of this ListInspectionReportRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListInspectionReportRequest.

        每页记录数

        :return: The limit of this ListInspectionReportRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListInspectionReportRequest.

        每页记录数

        :param limit: The limit of this ListInspectionReportRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListInspectionReportRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
