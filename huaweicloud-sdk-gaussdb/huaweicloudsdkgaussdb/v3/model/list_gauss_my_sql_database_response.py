# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListGaussMySqlDatabaseResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'databases': 'list[ListGaussMysqlDatabaseInfo]',
        'total_count': 'int'
    }

    attribute_map = {
        'databases': 'databases',
        'total_count': 'total_count'
    }

    def __init__(self, databases=None, total_count=None):
        r"""ListGaussMySqlDatabaseResponse

        The model defined in huaweicloud sdk

        :param databases: 数据库信息列表。
        :type databases: list[:class:`huaweicloudsdkgaussdb.v3.ListGaussMysqlDatabaseInfo`]
        :param total_count: 数据库总数。
        :type total_count: int
        """
        
        super(ListGaussMySqlDatabaseResponse, self).__init__()

        self._databases = None
        self._total_count = None
        self.discriminator = None

        if databases is not None:
            self.databases = databases
        if total_count is not None:
            self.total_count = total_count

    @property
    def databases(self):
        r"""Gets the databases of this ListGaussMySqlDatabaseResponse.

        数据库信息列表。

        :return: The databases of this ListGaussMySqlDatabaseResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdb.v3.ListGaussMysqlDatabaseInfo`]
        """
        return self._databases

    @databases.setter
    def databases(self, databases):
        r"""Sets the databases of this ListGaussMySqlDatabaseResponse.

        数据库信息列表。

        :param databases: The databases of this ListGaussMySqlDatabaseResponse.
        :type databases: list[:class:`huaweicloudsdkgaussdb.v3.ListGaussMysqlDatabaseInfo`]
        """
        self._databases = databases

    @property
    def total_count(self):
        r"""Gets the total_count of this ListGaussMySqlDatabaseResponse.

        数据库总数。

        :return: The total_count of this ListGaussMySqlDatabaseResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListGaussMySqlDatabaseResponse.

        数据库总数。

        :param total_count: The total_count of this ListGaussMySqlDatabaseResponse.
        :type total_count: int
        """
        self._total_count = total_count

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
        if not isinstance(other, ListGaussMySqlDatabaseResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
