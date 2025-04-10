# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPostgresqlListHistoryTablesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_language': 'str',
        'database_name': 'str',
        'body': 'PostgreSQLHistoryTableRequest'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'database_name': 'database_name',
        'body': 'body'
    }

    def __init__(self, x_language=None, database_name=None, body=None):
        r"""ListPostgresqlListHistoryTablesRequest

        The model defined in huaweicloud sdk

        :param x_language: 语言
        :type x_language: str
        :param database_name: 数据库引擎。支持的引擎如下，不区分大小写：postgresql
        :type database_name: str
        :param body: Body of the ListPostgresqlListHistoryTablesRequest
        :type body: :class:`huaweicloudsdkrds.v3.PostgreSQLHistoryTableRequest`
        """
        
        

        self._x_language = None
        self._database_name = None
        self._body = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.database_name = database_name
        if body is not None:
            self.body = body

    @property
    def x_language(self):
        r"""Gets the x_language of this ListPostgresqlListHistoryTablesRequest.

        语言

        :return: The x_language of this ListPostgresqlListHistoryTablesRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ListPostgresqlListHistoryTablesRequest.

        语言

        :param x_language: The x_language of this ListPostgresqlListHistoryTablesRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def database_name(self):
        r"""Gets the database_name of this ListPostgresqlListHistoryTablesRequest.

        数据库引擎。支持的引擎如下，不区分大小写：postgresql

        :return: The database_name of this ListPostgresqlListHistoryTablesRequest.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        r"""Sets the database_name of this ListPostgresqlListHistoryTablesRequest.

        数据库引擎。支持的引擎如下，不区分大小写：postgresql

        :param database_name: The database_name of this ListPostgresqlListHistoryTablesRequest.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def body(self):
        r"""Gets the body of this ListPostgresqlListHistoryTablesRequest.

        :return: The body of this ListPostgresqlListHistoryTablesRequest.
        :rtype: :class:`huaweicloudsdkrds.v3.PostgreSQLHistoryTableRequest`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this ListPostgresqlListHistoryTablesRequest.

        :param body: The body of this ListPostgresqlListHistoryTablesRequest.
        :type body: :class:`huaweicloudsdkrds.v3.PostgreSQLHistoryTableRequest`
        """
        self._body = body

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
        if not isinstance(other, ListPostgresqlListHistoryTablesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
