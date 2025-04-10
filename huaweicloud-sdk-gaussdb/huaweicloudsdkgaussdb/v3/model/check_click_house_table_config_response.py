# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckClickHouseTableConfigResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'source_database_name': 'str',
        'table_config_check_results': 'list[ChDatabaseTableConfigCheckResult]'
    }

    attribute_map = {
        'source_database_name': 'source_database_name',
        'table_config_check_results': 'table_config_check_results'
    }

    def __init__(self, source_database_name=None, table_config_check_results=None):
        r"""CheckClickHouseTableConfigResponse

        The model defined in huaweicloud sdk

        :param source_database_name: 源数据库名。
        :type source_database_name: str
        :param table_config_check_results: 表配置检查结果。
        :type table_config_check_results: list[:class:`huaweicloudsdkgaussdb.v3.ChDatabaseTableConfigCheckResult`]
        """
        
        super(CheckClickHouseTableConfigResponse, self).__init__()

        self._source_database_name = None
        self._table_config_check_results = None
        self.discriminator = None

        if source_database_name is not None:
            self.source_database_name = source_database_name
        if table_config_check_results is not None:
            self.table_config_check_results = table_config_check_results

    @property
    def source_database_name(self):
        r"""Gets the source_database_name of this CheckClickHouseTableConfigResponse.

        源数据库名。

        :return: The source_database_name of this CheckClickHouseTableConfigResponse.
        :rtype: str
        """
        return self._source_database_name

    @source_database_name.setter
    def source_database_name(self, source_database_name):
        r"""Sets the source_database_name of this CheckClickHouseTableConfigResponse.

        源数据库名。

        :param source_database_name: The source_database_name of this CheckClickHouseTableConfigResponse.
        :type source_database_name: str
        """
        self._source_database_name = source_database_name

    @property
    def table_config_check_results(self):
        r"""Gets the table_config_check_results of this CheckClickHouseTableConfigResponse.

        表配置检查结果。

        :return: The table_config_check_results of this CheckClickHouseTableConfigResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdb.v3.ChDatabaseTableConfigCheckResult`]
        """
        return self._table_config_check_results

    @table_config_check_results.setter
    def table_config_check_results(self, table_config_check_results):
        r"""Sets the table_config_check_results of this CheckClickHouseTableConfigResponse.

        表配置检查结果。

        :param table_config_check_results: The table_config_check_results of this CheckClickHouseTableConfigResponse.
        :type table_config_check_results: list[:class:`huaweicloudsdkgaussdb.v3.ChDatabaseTableConfigCheckResult`]
        """
        self._table_config_check_results = table_config_check_results

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
        if not isinstance(other, CheckClickHouseTableConfigResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
