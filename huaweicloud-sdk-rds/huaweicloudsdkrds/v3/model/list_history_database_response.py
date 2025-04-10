# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListHistoryDatabaseResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'database_limit': 'int',
        'table_limit': 'int',
        'instances': 'list[HistoryDatabaseInstance]'
    }

    attribute_map = {
        'database_limit': 'database_limit',
        'table_limit': 'table_limit',
        'instances': 'instances'
    }

    def __init__(self, database_limit=None, table_limit=None, instances=None):
        r"""ListHistoryDatabaseResponse

        The model defined in huaweicloud sdk

        :param database_limit: 恢复库数量限制个数
        :type database_limit: int
        :param table_limit: 恢复表数量限制个数
        :type table_limit: int
        :param instances: 实例信息
        :type instances: list[:class:`huaweicloudsdkrds.v3.HistoryDatabaseInstance`]
        """
        
        super(ListHistoryDatabaseResponse, self).__init__()

        self._database_limit = None
        self._table_limit = None
        self._instances = None
        self.discriminator = None

        if database_limit is not None:
            self.database_limit = database_limit
        if table_limit is not None:
            self.table_limit = table_limit
        if instances is not None:
            self.instances = instances

    @property
    def database_limit(self):
        r"""Gets the database_limit of this ListHistoryDatabaseResponse.

        恢复库数量限制个数

        :return: The database_limit of this ListHistoryDatabaseResponse.
        :rtype: int
        """
        return self._database_limit

    @database_limit.setter
    def database_limit(self, database_limit):
        r"""Sets the database_limit of this ListHistoryDatabaseResponse.

        恢复库数量限制个数

        :param database_limit: The database_limit of this ListHistoryDatabaseResponse.
        :type database_limit: int
        """
        self._database_limit = database_limit

    @property
    def table_limit(self):
        r"""Gets the table_limit of this ListHistoryDatabaseResponse.

        恢复表数量限制个数

        :return: The table_limit of this ListHistoryDatabaseResponse.
        :rtype: int
        """
        return self._table_limit

    @table_limit.setter
    def table_limit(self, table_limit):
        r"""Sets the table_limit of this ListHistoryDatabaseResponse.

        恢复表数量限制个数

        :param table_limit: The table_limit of this ListHistoryDatabaseResponse.
        :type table_limit: int
        """
        self._table_limit = table_limit

    @property
    def instances(self):
        r"""Gets the instances of this ListHistoryDatabaseResponse.

        实例信息

        :return: The instances of this ListHistoryDatabaseResponse.
        :rtype: list[:class:`huaweicloudsdkrds.v3.HistoryDatabaseInstance`]
        """
        return self._instances

    @instances.setter
    def instances(self, instances):
        r"""Sets the instances of this ListHistoryDatabaseResponse.

        实例信息

        :param instances: The instances of this ListHistoryDatabaseResponse.
        :type instances: list[:class:`huaweicloudsdkrds.v3.HistoryDatabaseInstance`]
        """
        self._instances = instances

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
        if not isinstance(other, ListHistoryDatabaseResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
