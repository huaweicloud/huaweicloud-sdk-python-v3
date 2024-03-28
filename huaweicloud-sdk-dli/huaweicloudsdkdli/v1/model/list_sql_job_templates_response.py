# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSqlJobTemplatesResponse(SdkResponse):

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
        'sql_count': 'int',
        'sqls': 'list[SqlJobTemplate]'
    }

    attribute_map = {
        'is_success': 'is_success',
        'message': 'message',
        'sql_count': 'sql_count',
        'sqls': 'sqls'
    }

    def __init__(self, is_success=None, message=None, sql_count=None, sqls=None):
        """ListSqlJobTemplatesResponse

        The model defined in huaweicloud sdk

        :param is_success: 是否成功。
        :type is_success: bool
        :param message: 系统提示信息，执行成功时，信息可能为空。执行失败时，用于显示执行失败的原因。
        :type message: str
        :param sql_count: SQL模板总数。
        :type sql_count: int
        :param sqls: 
        :type sqls: list[:class:`huaweicloudsdkdli.v1.SqlJobTemplate`]
        """
        
        super(ListSqlJobTemplatesResponse, self).__init__()

        self._is_success = None
        self._message = None
        self._sql_count = None
        self._sqls = None
        self.discriminator = None

        if is_success is not None:
            self.is_success = is_success
        if message is not None:
            self.message = message
        if sql_count is not None:
            self.sql_count = sql_count
        if sqls is not None:
            self.sqls = sqls

    @property
    def is_success(self):
        """Gets the is_success of this ListSqlJobTemplatesResponse.

        是否成功。

        :return: The is_success of this ListSqlJobTemplatesResponse.
        :rtype: bool
        """
        return self._is_success

    @is_success.setter
    def is_success(self, is_success):
        """Sets the is_success of this ListSqlJobTemplatesResponse.

        是否成功。

        :param is_success: The is_success of this ListSqlJobTemplatesResponse.
        :type is_success: bool
        """
        self._is_success = is_success

    @property
    def message(self):
        """Gets the message of this ListSqlJobTemplatesResponse.

        系统提示信息，执行成功时，信息可能为空。执行失败时，用于显示执行失败的原因。

        :return: The message of this ListSqlJobTemplatesResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ListSqlJobTemplatesResponse.

        系统提示信息，执行成功时，信息可能为空。执行失败时，用于显示执行失败的原因。

        :param message: The message of this ListSqlJobTemplatesResponse.
        :type message: str
        """
        self._message = message

    @property
    def sql_count(self):
        """Gets the sql_count of this ListSqlJobTemplatesResponse.

        SQL模板总数。

        :return: The sql_count of this ListSqlJobTemplatesResponse.
        :rtype: int
        """
        return self._sql_count

    @sql_count.setter
    def sql_count(self, sql_count):
        """Sets the sql_count of this ListSqlJobTemplatesResponse.

        SQL模板总数。

        :param sql_count: The sql_count of this ListSqlJobTemplatesResponse.
        :type sql_count: int
        """
        self._sql_count = sql_count

    @property
    def sqls(self):
        """Gets the sqls of this ListSqlJobTemplatesResponse.

        :return: The sqls of this ListSqlJobTemplatesResponse.
        :rtype: list[:class:`huaweicloudsdkdli.v1.SqlJobTemplate`]
        """
        return self._sqls

    @sqls.setter
    def sqls(self, sqls):
        """Sets the sqls of this ListSqlJobTemplatesResponse.

        :param sqls: The sqls of this ListSqlJobTemplatesResponse.
        :type sqls: list[:class:`huaweicloudsdkdli.v1.SqlJobTemplate`]
        """
        self._sqls = sqls

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
        if not isinstance(other, ListSqlJobTemplatesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
