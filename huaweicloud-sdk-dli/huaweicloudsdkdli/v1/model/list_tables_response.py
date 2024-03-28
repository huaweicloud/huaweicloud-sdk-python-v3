# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTablesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_success': 'bool',
        'message': 'str',
        'table_count': 'int',
        'tables': 'list[Table]'
    }

    attribute_map = {
        'is_success': 'is_success',
        'message': 'message',
        'table_count': 'table_count',
        'tables': 'tables'
    }

    def __init__(self, is_success=None, message=None, table_count=None, tables=None):
        """ListTablesResponse

        The model defined in huaweicloud sdk

        :param is_success: 执行请求是否成功。“true”表示请求执行成功。
        :type is_success: bool
        :param message: 系统提示信息，执行成功时，信息可能为空。
        :type message: str
        :param table_count: 表的总个数。
        :type table_count: int
        :param tables: 表的信息。
        :type tables: list[:class:`huaweicloudsdkdli.v1.Table`]
        """
        
        super(ListTablesResponse, self).__init__()

        self._is_success = None
        self._message = None
        self._table_count = None
        self._tables = None
        self.discriminator = None

        if is_success is not None:
            self.is_success = is_success
        if message is not None:
            self.message = message
        if table_count is not None:
            self.table_count = table_count
        if tables is not None:
            self.tables = tables

    @property
    def is_success(self):
        """Gets the is_success of this ListTablesResponse.

        执行请求是否成功。“true”表示请求执行成功。

        :return: The is_success of this ListTablesResponse.
        :rtype: bool
        """
        return self._is_success

    @is_success.setter
    def is_success(self, is_success):
        """Sets the is_success of this ListTablesResponse.

        执行请求是否成功。“true”表示请求执行成功。

        :param is_success: The is_success of this ListTablesResponse.
        :type is_success: bool
        """
        self._is_success = is_success

    @property
    def message(self):
        """Gets the message of this ListTablesResponse.

        系统提示信息，执行成功时，信息可能为空。

        :return: The message of this ListTablesResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ListTablesResponse.

        系统提示信息，执行成功时，信息可能为空。

        :param message: The message of this ListTablesResponse.
        :type message: str
        """
        self._message = message

    @property
    def table_count(self):
        """Gets the table_count of this ListTablesResponse.

        表的总个数。

        :return: The table_count of this ListTablesResponse.
        :rtype: int
        """
        return self._table_count

    @table_count.setter
    def table_count(self, table_count):
        """Sets the table_count of this ListTablesResponse.

        表的总个数。

        :param table_count: The table_count of this ListTablesResponse.
        :type table_count: int
        """
        self._table_count = table_count

    @property
    def tables(self):
        """Gets the tables of this ListTablesResponse.

        表的信息。

        :return: The tables of this ListTablesResponse.
        :rtype: list[:class:`huaweicloudsdkdli.v1.Table`]
        """
        return self._tables

    @tables.setter
    def tables(self, tables):
        """Sets the tables of this ListTablesResponse.

        表的信息。

        :param tables: The tables of this ListTablesResponse.
        :type tables: list[:class:`huaweicloudsdkdli.v1.Table`]
        """
        self._tables = tables

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
        if not isinstance(other, ListTablesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
