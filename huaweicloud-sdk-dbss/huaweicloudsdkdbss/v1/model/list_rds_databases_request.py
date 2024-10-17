# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRdsDatabasesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'db_type': 'str',
        'offset': 'str',
        'limit': 'str'
    }

    attribute_map = {
        'db_type': 'db_type',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, db_type=None, offset=None, limit=None):
        """ListRdsDatabasesRequest

        The model defined in huaweicloud sdk

        :param db_type: 数据库类型 - MYSQL - ORACLE - POSTGRESQL - SQLSERVER - DAMENG - TAURUS - DWS - KINGBASE - MARIADB - GAUSSDBOPENGAUSS
        :type db_type: str
        :param offset: 偏移量，从第一条数据偏移offset条数据后开始查询，默认为0。
        :type offset: str
        :param limit: 查询记录数，默认为100。
        :type limit: str
        """
        
        

        self._db_type = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.db_type = db_type
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def db_type(self):
        """Gets the db_type of this ListRdsDatabasesRequest.

        数据库类型 - MYSQL - ORACLE - POSTGRESQL - SQLSERVER - DAMENG - TAURUS - DWS - KINGBASE - MARIADB - GAUSSDBOPENGAUSS

        :return: The db_type of this ListRdsDatabasesRequest.
        :rtype: str
        """
        return self._db_type

    @db_type.setter
    def db_type(self, db_type):
        """Sets the db_type of this ListRdsDatabasesRequest.

        数据库类型 - MYSQL - ORACLE - POSTGRESQL - SQLSERVER - DAMENG - TAURUS - DWS - KINGBASE - MARIADB - GAUSSDBOPENGAUSS

        :param db_type: The db_type of this ListRdsDatabasesRequest.
        :type db_type: str
        """
        self._db_type = db_type

    @property
    def offset(self):
        """Gets the offset of this ListRdsDatabasesRequest.

        偏移量，从第一条数据偏移offset条数据后开始查询，默认为0。

        :return: The offset of this ListRdsDatabasesRequest.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListRdsDatabasesRequest.

        偏移量，从第一条数据偏移offset条数据后开始查询，默认为0。

        :param offset: The offset of this ListRdsDatabasesRequest.
        :type offset: str
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListRdsDatabasesRequest.

        查询记录数，默认为100。

        :return: The limit of this ListRdsDatabasesRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListRdsDatabasesRequest.

        查询记录数，默认为100。

        :param limit: The limit of this ListRdsDatabasesRequest.
        :type limit: str
        """
        self._limit = limit

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
        if not isinstance(other, ListRdsDatabasesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
