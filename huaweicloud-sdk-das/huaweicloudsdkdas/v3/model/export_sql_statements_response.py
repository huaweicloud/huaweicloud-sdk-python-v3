# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportSqlStatementsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'statements': 'list[FullSql]',
        'next_marker': 'str'
    }

    attribute_map = {
        'statements': 'statements',
        'next_marker': 'next_marker'
    }

    def __init__(self, statements=None, next_marker=None):
        r"""ExportSqlStatementsResponse

        The model defined in huaweicloud sdk

        :param statements: 全量SQL集合。当集合为空时，说明SQL已全部导出。
        :type statements: list[:class:`huaweicloudsdkdas.v3.FullSql`]
        :param next_marker: 获取下一页所需的标识符。marker仅在3分钟内有效。
        :type next_marker: str
        """
        
        super(ExportSqlStatementsResponse, self).__init__()

        self._statements = None
        self._next_marker = None
        self.discriminator = None

        if statements is not None:
            self.statements = statements
        if next_marker is not None:
            self.next_marker = next_marker

    @property
    def statements(self):
        r"""Gets the statements of this ExportSqlStatementsResponse.

        全量SQL集合。当集合为空时，说明SQL已全部导出。

        :return: The statements of this ExportSqlStatementsResponse.
        :rtype: list[:class:`huaweicloudsdkdas.v3.FullSql`]
        """
        return self._statements

    @statements.setter
    def statements(self, statements):
        r"""Sets the statements of this ExportSqlStatementsResponse.

        全量SQL集合。当集合为空时，说明SQL已全部导出。

        :param statements: The statements of this ExportSqlStatementsResponse.
        :type statements: list[:class:`huaweicloudsdkdas.v3.FullSql`]
        """
        self._statements = statements

    @property
    def next_marker(self):
        r"""Gets the next_marker of this ExportSqlStatementsResponse.

        获取下一页所需的标识符。marker仅在3分钟内有效。

        :return: The next_marker of this ExportSqlStatementsResponse.
        :rtype: str
        """
        return self._next_marker

    @next_marker.setter
    def next_marker(self, next_marker):
        r"""Sets the next_marker of this ExportSqlStatementsResponse.

        获取下一页所需的标识符。marker仅在3分钟内有效。

        :param next_marker: The next_marker of this ExportSqlStatementsResponse.
        :type next_marker: str
        """
        self._next_marker = next_marker

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
        if not isinstance(other, ExportSqlStatementsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
