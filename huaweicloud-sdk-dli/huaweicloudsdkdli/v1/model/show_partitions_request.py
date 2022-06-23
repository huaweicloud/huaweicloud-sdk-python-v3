# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowPartitionsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'database_name': 'str',
        'table_name': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'database_name': 'database_name',
        'table_name': 'table_name',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, database_name=None, table_name=None, limit=None, offset=None):
        """ShowPartitionsRequest

        The model defined in huaweicloud sdk

        :param database_name: 数据库名
        :type database_name: str
        :param table_name: 表名
        :type table_name: str
        :param limit: 显示个数，默认值为100
        :type limit: int
        :param offset: 偏移量
        :type offset: int
        """
        
        

        self._database_name = None
        self._table_name = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        self.database_name = database_name
        self.table_name = table_name
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def database_name(self):
        """Gets the database_name of this ShowPartitionsRequest.

        数据库名

        :return: The database_name of this ShowPartitionsRequest.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        """Sets the database_name of this ShowPartitionsRequest.

        数据库名

        :param database_name: The database_name of this ShowPartitionsRequest.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def table_name(self):
        """Gets the table_name of this ShowPartitionsRequest.

        表名

        :return: The table_name of this ShowPartitionsRequest.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        """Sets the table_name of this ShowPartitionsRequest.

        表名

        :param table_name: The table_name of this ShowPartitionsRequest.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def limit(self):
        """Gets the limit of this ShowPartitionsRequest.

        显示个数，默认值为100

        :return: The limit of this ShowPartitionsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ShowPartitionsRequest.

        显示个数，默认值为100

        :param limit: The limit of this ShowPartitionsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ShowPartitionsRequest.

        偏移量

        :return: The offset of this ShowPartitionsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ShowPartitionsRequest.

        偏移量

        :param offset: The offset of this ShowPartitionsRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ShowPartitionsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
