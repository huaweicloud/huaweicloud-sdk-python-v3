# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HealthReportTableSpaceQuerySpecialTablesResp:

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
        'last_diagnose_timestamp': 'int',
        'tables': 'list[HealthReportTableSpaceTablesDto]'
    }

    attribute_map = {
        'total_count': 'total_count',
        'last_diagnose_timestamp': 'last_diagnose_timestamp',
        'tables': 'tables'
    }

    def __init__(self, total_count=None, last_diagnose_timestamp=None, tables=None):
        r"""HealthReportTableSpaceQuerySpecialTablesResp

        The model defined in huaweicloud sdk

        :param total_count: 总数。
        :type total_count: int
        :param last_diagnose_timestamp: 最近诊断时间。
        :type last_diagnose_timestamp: int
        :param tables: 库表信息列表。
        :type tables: list[:class:`huaweicloudsdkdas.v3.HealthReportTableSpaceTablesDto`]
        """
        
        

        self._total_count = None
        self._last_diagnose_timestamp = None
        self._tables = None
        self.discriminator = None

        if total_count is not None:
            self.total_count = total_count
        if last_diagnose_timestamp is not None:
            self.last_diagnose_timestamp = last_diagnose_timestamp
        if tables is not None:
            self.tables = tables

    @property
    def total_count(self):
        r"""Gets the total_count of this HealthReportTableSpaceQuerySpecialTablesResp.

        总数。

        :return: The total_count of this HealthReportTableSpaceQuerySpecialTablesResp.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this HealthReportTableSpaceQuerySpecialTablesResp.

        总数。

        :param total_count: The total_count of this HealthReportTableSpaceQuerySpecialTablesResp.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def last_diagnose_timestamp(self):
        r"""Gets the last_diagnose_timestamp of this HealthReportTableSpaceQuerySpecialTablesResp.

        最近诊断时间。

        :return: The last_diagnose_timestamp of this HealthReportTableSpaceQuerySpecialTablesResp.
        :rtype: int
        """
        return self._last_diagnose_timestamp

    @last_diagnose_timestamp.setter
    def last_diagnose_timestamp(self, last_diagnose_timestamp):
        r"""Sets the last_diagnose_timestamp of this HealthReportTableSpaceQuerySpecialTablesResp.

        最近诊断时间。

        :param last_diagnose_timestamp: The last_diagnose_timestamp of this HealthReportTableSpaceQuerySpecialTablesResp.
        :type last_diagnose_timestamp: int
        """
        self._last_diagnose_timestamp = last_diagnose_timestamp

    @property
    def tables(self):
        r"""Gets the tables of this HealthReportTableSpaceQuerySpecialTablesResp.

        库表信息列表。

        :return: The tables of this HealthReportTableSpaceQuerySpecialTablesResp.
        :rtype: list[:class:`huaweicloudsdkdas.v3.HealthReportTableSpaceTablesDto`]
        """
        return self._tables

    @tables.setter
    def tables(self, tables):
        r"""Sets the tables of this HealthReportTableSpaceQuerySpecialTablesResp.

        库表信息列表。

        :param tables: The tables of this HealthReportTableSpaceQuerySpecialTablesResp.
        :type tables: list[:class:`huaweicloudsdkdas.v3.HealthReportTableSpaceTablesDto`]
        """
        self._tables = tables

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
        if not isinstance(other, HealthReportTableSpaceQuerySpecialTablesResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
