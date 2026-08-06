# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HealthReportTableSpaceNewStat:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'database_top_resp': 'list[HealthReportTableSpaceQuerySpaceTopResp]',
        'table_top_resp': 'list[HealthReportTableSpaceQuerySpaceTopResp]',
        'rapid_growth_tables_resp': 'list[HealthReportTableSpaceQueryRapidGrowthTablesResp]',
        'no_primary_tables_resp': 'list[HealthReportTableSpaceQuerySpecialTablesResp]',
        'no_index_tables_resp': 'list[HealthReportTableSpaceQuerySpecialTablesResp]'
    }

    attribute_map = {
        'database_top_resp': 'database_top_resp',
        'table_top_resp': 'table_top_resp',
        'rapid_growth_tables_resp': 'rapid_growth_tables_resp',
        'no_primary_tables_resp': 'no_primary_tables_resp',
        'no_index_tables_resp': 'no_index_tables_resp'
    }

    def __init__(self, database_top_resp=None, table_top_resp=None, rapid_growth_tables_resp=None, no_primary_tables_resp=None, no_index_tables_resp=None):
        r"""HealthReportTableSpaceNewStat

        The model defined in huaweicloud sdk

        :param database_top_resp: top库列表。
        :type database_top_resp: list[:class:`huaweicloudsdkdas.v3.HealthReportTableSpaceQuerySpaceTopResp`]
        :param table_top_resp: top表列表。
        :type table_top_resp: list[:class:`huaweicloudsdkdas.v3.HealthReportTableSpaceQuerySpaceTopResp`]
        :param rapid_growth_tables_resp: 异常增长表列表。
        :type rapid_growth_tables_resp: list[:class:`huaweicloudsdkdas.v3.HealthReportTableSpaceQueryRapidGrowthTablesResp`]
        :param no_primary_tables_resp: 无主键表列表。
        :type no_primary_tables_resp: list[:class:`huaweicloudsdkdas.v3.HealthReportTableSpaceQuerySpecialTablesResp`]
        :param no_index_tables_resp: 无索引表列表。
        :type no_index_tables_resp: list[:class:`huaweicloudsdkdas.v3.HealthReportTableSpaceQuerySpecialTablesResp`]
        """
        
        

        self._database_top_resp = None
        self._table_top_resp = None
        self._rapid_growth_tables_resp = None
        self._no_primary_tables_resp = None
        self._no_index_tables_resp = None
        self.discriminator = None

        if database_top_resp is not None:
            self.database_top_resp = database_top_resp
        if table_top_resp is not None:
            self.table_top_resp = table_top_resp
        if rapid_growth_tables_resp is not None:
            self.rapid_growth_tables_resp = rapid_growth_tables_resp
        if no_primary_tables_resp is not None:
            self.no_primary_tables_resp = no_primary_tables_resp
        if no_index_tables_resp is not None:
            self.no_index_tables_resp = no_index_tables_resp

    @property
    def database_top_resp(self):
        r"""Gets the database_top_resp of this HealthReportTableSpaceNewStat.

        top库列表。

        :return: The database_top_resp of this HealthReportTableSpaceNewStat.
        :rtype: list[:class:`huaweicloudsdkdas.v3.HealthReportTableSpaceQuerySpaceTopResp`]
        """
        return self._database_top_resp

    @database_top_resp.setter
    def database_top_resp(self, database_top_resp):
        r"""Sets the database_top_resp of this HealthReportTableSpaceNewStat.

        top库列表。

        :param database_top_resp: The database_top_resp of this HealthReportTableSpaceNewStat.
        :type database_top_resp: list[:class:`huaweicloudsdkdas.v3.HealthReportTableSpaceQuerySpaceTopResp`]
        """
        self._database_top_resp = database_top_resp

    @property
    def table_top_resp(self):
        r"""Gets the table_top_resp of this HealthReportTableSpaceNewStat.

        top表列表。

        :return: The table_top_resp of this HealthReportTableSpaceNewStat.
        :rtype: list[:class:`huaweicloudsdkdas.v3.HealthReportTableSpaceQuerySpaceTopResp`]
        """
        return self._table_top_resp

    @table_top_resp.setter
    def table_top_resp(self, table_top_resp):
        r"""Sets the table_top_resp of this HealthReportTableSpaceNewStat.

        top表列表。

        :param table_top_resp: The table_top_resp of this HealthReportTableSpaceNewStat.
        :type table_top_resp: list[:class:`huaweicloudsdkdas.v3.HealthReportTableSpaceQuerySpaceTopResp`]
        """
        self._table_top_resp = table_top_resp

    @property
    def rapid_growth_tables_resp(self):
        r"""Gets the rapid_growth_tables_resp of this HealthReportTableSpaceNewStat.

        异常增长表列表。

        :return: The rapid_growth_tables_resp of this HealthReportTableSpaceNewStat.
        :rtype: list[:class:`huaweicloudsdkdas.v3.HealthReportTableSpaceQueryRapidGrowthTablesResp`]
        """
        return self._rapid_growth_tables_resp

    @rapid_growth_tables_resp.setter
    def rapid_growth_tables_resp(self, rapid_growth_tables_resp):
        r"""Sets the rapid_growth_tables_resp of this HealthReportTableSpaceNewStat.

        异常增长表列表。

        :param rapid_growth_tables_resp: The rapid_growth_tables_resp of this HealthReportTableSpaceNewStat.
        :type rapid_growth_tables_resp: list[:class:`huaweicloudsdkdas.v3.HealthReportTableSpaceQueryRapidGrowthTablesResp`]
        """
        self._rapid_growth_tables_resp = rapid_growth_tables_resp

    @property
    def no_primary_tables_resp(self):
        r"""Gets the no_primary_tables_resp of this HealthReportTableSpaceNewStat.

        无主键表列表。

        :return: The no_primary_tables_resp of this HealthReportTableSpaceNewStat.
        :rtype: list[:class:`huaweicloudsdkdas.v3.HealthReportTableSpaceQuerySpecialTablesResp`]
        """
        return self._no_primary_tables_resp

    @no_primary_tables_resp.setter
    def no_primary_tables_resp(self, no_primary_tables_resp):
        r"""Sets the no_primary_tables_resp of this HealthReportTableSpaceNewStat.

        无主键表列表。

        :param no_primary_tables_resp: The no_primary_tables_resp of this HealthReportTableSpaceNewStat.
        :type no_primary_tables_resp: list[:class:`huaweicloudsdkdas.v3.HealthReportTableSpaceQuerySpecialTablesResp`]
        """
        self._no_primary_tables_resp = no_primary_tables_resp

    @property
    def no_index_tables_resp(self):
        r"""Gets the no_index_tables_resp of this HealthReportTableSpaceNewStat.

        无索引表列表。

        :return: The no_index_tables_resp of this HealthReportTableSpaceNewStat.
        :rtype: list[:class:`huaweicloudsdkdas.v3.HealthReportTableSpaceQuerySpecialTablesResp`]
        """
        return self._no_index_tables_resp

    @no_index_tables_resp.setter
    def no_index_tables_resp(self, no_index_tables_resp):
        r"""Sets the no_index_tables_resp of this HealthReportTableSpaceNewStat.

        无索引表列表。

        :param no_index_tables_resp: The no_index_tables_resp of this HealthReportTableSpaceNewStat.
        :type no_index_tables_resp: list[:class:`huaweicloudsdkdas.v3.HealthReportTableSpaceQuerySpecialTablesResp`]
        """
        self._no_index_tables_resp = no_index_tables_resp

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
        if not isinstance(other, HealthReportTableSpaceNewStat):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
