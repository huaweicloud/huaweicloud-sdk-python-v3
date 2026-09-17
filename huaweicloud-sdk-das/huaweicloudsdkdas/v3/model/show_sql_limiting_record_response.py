# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSqlLimitingRecordResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sql_limiting_record_list': 'list[SqlLimitingRecordInfo]',
        'total': 'int',
        'can_show_limit_count': 'bool'
    }

    attribute_map = {
        'sql_limiting_record_list': 'sql_limiting_record_list',
        'total': 'total',
        'can_show_limit_count': 'can_show_limit_count'
    }

    def __init__(self, sql_limiting_record_list=None, total=None, can_show_limit_count=None):
        r"""ShowSqlLimitingRecordResponse

        The model defined in huaweicloud sdk

        :param sql_limiting_record_list: SQL限流规则列表
        :type sql_limiting_record_list: list[:class:`huaweicloudsdkdas.v3.SqlLimitingRecordInfo`]
        :param total: SQL限流规则总数
        :type total: int
        :param can_show_limit_count: 实例是否支持展示显示限流触发次数
        :type can_show_limit_count: bool
        """
        
        super().__init__()

        self._sql_limiting_record_list = None
        self._total = None
        self._can_show_limit_count = None
        self.discriminator = None

        if sql_limiting_record_list is not None:
            self.sql_limiting_record_list = sql_limiting_record_list
        if total is not None:
            self.total = total
        if can_show_limit_count is not None:
            self.can_show_limit_count = can_show_limit_count

    @property
    def sql_limiting_record_list(self):
        r"""Gets the sql_limiting_record_list of this ShowSqlLimitingRecordResponse.

        SQL限流规则列表

        :return: The sql_limiting_record_list of this ShowSqlLimitingRecordResponse.
        :rtype: list[:class:`huaweicloudsdkdas.v3.SqlLimitingRecordInfo`]
        """
        return self._sql_limiting_record_list

    @sql_limiting_record_list.setter
    def sql_limiting_record_list(self, sql_limiting_record_list):
        r"""Sets the sql_limiting_record_list of this ShowSqlLimitingRecordResponse.

        SQL限流规则列表

        :param sql_limiting_record_list: The sql_limiting_record_list of this ShowSqlLimitingRecordResponse.
        :type sql_limiting_record_list: list[:class:`huaweicloudsdkdas.v3.SqlLimitingRecordInfo`]
        """
        self._sql_limiting_record_list = sql_limiting_record_list

    @property
    def total(self):
        r"""Gets the total of this ShowSqlLimitingRecordResponse.

        SQL限流规则总数

        :return: The total of this ShowSqlLimitingRecordResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ShowSqlLimitingRecordResponse.

        SQL限流规则总数

        :param total: The total of this ShowSqlLimitingRecordResponse.
        :type total: int
        """
        self._total = total

    @property
    def can_show_limit_count(self):
        r"""Gets the can_show_limit_count of this ShowSqlLimitingRecordResponse.

        实例是否支持展示显示限流触发次数

        :return: The can_show_limit_count of this ShowSqlLimitingRecordResponse.
        :rtype: bool
        """
        return self._can_show_limit_count

    @can_show_limit_count.setter
    def can_show_limit_count(self, can_show_limit_count):
        r"""Sets the can_show_limit_count of this ShowSqlLimitingRecordResponse.

        实例是否支持展示显示限流触发次数

        :param can_show_limit_count: The can_show_limit_count of this ShowSqlLimitingRecordResponse.
        :type can_show_limit_count: bool
        """
        self._can_show_limit_count = can_show_limit_count

    def to_dict(self):
        import warnings
        warnings.warn("ShowSqlLimitingRecordResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowSqlLimitingRecordResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
