# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSqlSampleTemplatesResponse(SdkResponse):

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
        'sqls': 'list[SqlSampleTemplate]',
        'sql_count': 'int'
    }

    attribute_map = {
        'is_success': 'is_success',
        'message': 'message',
        'sqls': 'sqls',
        'sql_count': 'sqlCount'
    }

    def __init__(self, is_success=None, message=None, sqls=None, sql_count=None):
        r"""ListSqlSampleTemplatesResponse

        The model defined in huaweicloud sdk

        :param is_success: 请求执行是否成功。“true”表示请求执行成功。
        :type is_success: bool
        :param message: 系统提示信息，执行成功时，信息可能为空。
        :type message: str
        :param sqls: 样例模板信息。
        :type sqls: list[:class:`huaweicloudsdkdli.v1.SqlSampleTemplate`]
        :param sql_count: 样例模板个数。
        :type sql_count: int
        """
        
        super(ListSqlSampleTemplatesResponse, self).__init__()

        self._is_success = None
        self._message = None
        self._sqls = None
        self._sql_count = None
        self.discriminator = None

        if is_success is not None:
            self.is_success = is_success
        if message is not None:
            self.message = message
        if sqls is not None:
            self.sqls = sqls
        if sql_count is not None:
            self.sql_count = sql_count

    @property
    def is_success(self):
        r"""Gets the is_success of this ListSqlSampleTemplatesResponse.

        请求执行是否成功。“true”表示请求执行成功。

        :return: The is_success of this ListSqlSampleTemplatesResponse.
        :rtype: bool
        """
        return self._is_success

    @is_success.setter
    def is_success(self, is_success):
        r"""Sets the is_success of this ListSqlSampleTemplatesResponse.

        请求执行是否成功。“true”表示请求执行成功。

        :param is_success: The is_success of this ListSqlSampleTemplatesResponse.
        :type is_success: bool
        """
        self._is_success = is_success

    @property
    def message(self):
        r"""Gets the message of this ListSqlSampleTemplatesResponse.

        系统提示信息，执行成功时，信息可能为空。

        :return: The message of this ListSqlSampleTemplatesResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this ListSqlSampleTemplatesResponse.

        系统提示信息，执行成功时，信息可能为空。

        :param message: The message of this ListSqlSampleTemplatesResponse.
        :type message: str
        """
        self._message = message

    @property
    def sqls(self):
        r"""Gets the sqls of this ListSqlSampleTemplatesResponse.

        样例模板信息。

        :return: The sqls of this ListSqlSampleTemplatesResponse.
        :rtype: list[:class:`huaweicloudsdkdli.v1.SqlSampleTemplate`]
        """
        return self._sqls

    @sqls.setter
    def sqls(self, sqls):
        r"""Sets the sqls of this ListSqlSampleTemplatesResponse.

        样例模板信息。

        :param sqls: The sqls of this ListSqlSampleTemplatesResponse.
        :type sqls: list[:class:`huaweicloudsdkdli.v1.SqlSampleTemplate`]
        """
        self._sqls = sqls

    @property
    def sql_count(self):
        r"""Gets the sql_count of this ListSqlSampleTemplatesResponse.

        样例模板个数。

        :return: The sql_count of this ListSqlSampleTemplatesResponse.
        :rtype: int
        """
        return self._sql_count

    @sql_count.setter
    def sql_count(self, sql_count):
        r"""Sets the sql_count of this ListSqlSampleTemplatesResponse.

        样例模板个数。

        :param sql_count: The sql_count of this ListSqlSampleTemplatesResponse.
        :type sql_count: int
        """
        self._sql_count = sql_count

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
        if not isinstance(other, ListSqlSampleTemplatesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
