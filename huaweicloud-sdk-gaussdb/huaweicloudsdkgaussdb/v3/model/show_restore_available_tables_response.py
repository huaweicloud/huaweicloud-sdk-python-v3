# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowRestoreAvailableTablesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_tables': 'int',
        'databases': 'list[RestoreDatabaseInfos]'
    }

    attribute_map = {
        'total_tables': 'total_tables',
        'databases': 'databases'
    }

    def __init__(self, total_tables=None, databases=None):
        r"""ShowRestoreAvailableTablesResponse

        The model defined in huaweicloud sdk

        :param total_tables: **参数解释**:  实例总表数。  **取值范围**：  不涉及。
        :type total_tables: int
        :param databases: **参数解释**：  数据库信息。
        :type databases: list[:class:`huaweicloudsdkgaussdb.v3.RestoreDatabaseInfos`]
        """
        
        super(ShowRestoreAvailableTablesResponse, self).__init__()

        self._total_tables = None
        self._databases = None
        self.discriminator = None

        if total_tables is not None:
            self.total_tables = total_tables
        if databases is not None:
            self.databases = databases

    @property
    def total_tables(self):
        r"""Gets the total_tables of this ShowRestoreAvailableTablesResponse.

        **参数解释**:  实例总表数。  **取值范围**：  不涉及。

        :return: The total_tables of this ShowRestoreAvailableTablesResponse.
        :rtype: int
        """
        return self._total_tables

    @total_tables.setter
    def total_tables(self, total_tables):
        r"""Sets the total_tables of this ShowRestoreAvailableTablesResponse.

        **参数解释**:  实例总表数。  **取值范围**：  不涉及。

        :param total_tables: The total_tables of this ShowRestoreAvailableTablesResponse.
        :type total_tables: int
        """
        self._total_tables = total_tables

    @property
    def databases(self):
        r"""Gets the databases of this ShowRestoreAvailableTablesResponse.

        **参数解释**：  数据库信息。

        :return: The databases of this ShowRestoreAvailableTablesResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdb.v3.RestoreDatabaseInfos`]
        """
        return self._databases

    @databases.setter
    def databases(self, databases):
        r"""Sets the databases of this ShowRestoreAvailableTablesResponse.

        **参数解释**：  数据库信息。

        :param databases: The databases of this ShowRestoreAvailableTablesResponse.
        :type databases: list[:class:`huaweicloudsdkgaussdb.v3.RestoreDatabaseInfos`]
        """
        self._databases = databases

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
        if not isinstance(other, ShowRestoreAvailableTablesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
