# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDatabasesResponse(SdkResponse):

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
        'database_count': 'int',
        'databases': 'list[ListDatabasesRespDatabase]'
    }

    attribute_map = {
        'is_success': 'is_success',
        'message': 'message',
        'database_count': 'database_count',
        'databases': 'databases'
    }

    def __init__(self, is_success=None, message=None, database_count=None, databases=None):
        """ListDatabasesResponse

        The model defined in huaweicloud sdk

        :param is_success: 执行请求是否成功。“true”表示请求执行成功。
        :type is_success: bool
        :param message: 系统提示信息，执行成功时，信息可能为空。
        :type message: str
        :param database_count: 数据库的总数。
        :type database_count: int
        :param databases: 查询所有数据库的响应参数。
        :type databases: list[:class:`huaweicloudsdkdli.v1.ListDatabasesRespDatabase`]
        """
        
        super(ListDatabasesResponse, self).__init__()

        self._is_success = None
        self._message = None
        self._database_count = None
        self._databases = None
        self.discriminator = None

        if is_success is not None:
            self.is_success = is_success
        if message is not None:
            self.message = message
        if database_count is not None:
            self.database_count = database_count
        if databases is not None:
            self.databases = databases

    @property
    def is_success(self):
        """Gets the is_success of this ListDatabasesResponse.

        执行请求是否成功。“true”表示请求执行成功。

        :return: The is_success of this ListDatabasesResponse.
        :rtype: bool
        """
        return self._is_success

    @is_success.setter
    def is_success(self, is_success):
        """Sets the is_success of this ListDatabasesResponse.

        执行请求是否成功。“true”表示请求执行成功。

        :param is_success: The is_success of this ListDatabasesResponse.
        :type is_success: bool
        """
        self._is_success = is_success

    @property
    def message(self):
        """Gets the message of this ListDatabasesResponse.

        系统提示信息，执行成功时，信息可能为空。

        :return: The message of this ListDatabasesResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ListDatabasesResponse.

        系统提示信息，执行成功时，信息可能为空。

        :param message: The message of this ListDatabasesResponse.
        :type message: str
        """
        self._message = message

    @property
    def database_count(self):
        """Gets the database_count of this ListDatabasesResponse.

        数据库的总数。

        :return: The database_count of this ListDatabasesResponse.
        :rtype: int
        """
        return self._database_count

    @database_count.setter
    def database_count(self, database_count):
        """Sets the database_count of this ListDatabasesResponse.

        数据库的总数。

        :param database_count: The database_count of this ListDatabasesResponse.
        :type database_count: int
        """
        self._database_count = database_count

    @property
    def databases(self):
        """Gets the databases of this ListDatabasesResponse.

        查询所有数据库的响应参数。

        :return: The databases of this ListDatabasesResponse.
        :rtype: list[:class:`huaweicloudsdkdli.v1.ListDatabasesRespDatabase`]
        """
        return self._databases

    @databases.setter
    def databases(self, databases):
        """Sets the databases of this ListDatabasesResponse.

        查询所有数据库的响应参数。

        :param databases: The databases of this ListDatabasesResponse.
        :type databases: list[:class:`huaweicloudsdkdli.v1.ListDatabasesRespDatabase`]
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
        if not isinstance(other, ListDatabasesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
