# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTableResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cursor_name': 'str',
        'table_names': 'list[str]'
    }

    attribute_map = {
        'cursor_name': 'cursor_name',
        'table_names': 'table_names'
    }

    def __init__(self, cursor_name=None, table_names=None):
        r"""ListTableResponse

        The model defined in huaweicloud sdk

        :param cursor_name: 本次响应后的游标位置，下次请求时携带，如果为空，表示后面无更多。 - 长度：[3, 63] - 取值字符限制：[a-z0-9_-]+ &gt; 如果为空，表示后面无更多。
        :type cursor_name: str
        :param table_names: 返回的表名列表。 - 长度：最大100
        :type table_names: list[str]
        """
        
        super(ListTableResponse, self).__init__()

        self._cursor_name = None
        self._table_names = None
        self.discriminator = None

        if cursor_name is not None:
            self.cursor_name = cursor_name
        if table_names is not None:
            self.table_names = table_names

    @property
    def cursor_name(self):
        r"""Gets the cursor_name of this ListTableResponse.

        本次响应后的游标位置，下次请求时携带，如果为空，表示后面无更多。 - 长度：[3, 63] - 取值字符限制：[a-z0-9_-]+ > 如果为空，表示后面无更多。

        :return: The cursor_name of this ListTableResponse.
        :rtype: str
        """
        return self._cursor_name

    @cursor_name.setter
    def cursor_name(self, cursor_name):
        r"""Sets the cursor_name of this ListTableResponse.

        本次响应后的游标位置，下次请求时携带，如果为空，表示后面无更多。 - 长度：[3, 63] - 取值字符限制：[a-z0-9_-]+ > 如果为空，表示后面无更多。

        :param cursor_name: The cursor_name of this ListTableResponse.
        :type cursor_name: str
        """
        self._cursor_name = cursor_name

    @property
    def table_names(self):
        r"""Gets the table_names of this ListTableResponse.

        返回的表名列表。 - 长度：最大100

        :return: The table_names of this ListTableResponse.
        :rtype: list[str]
        """
        return self._table_names

    @table_names.setter
    def table_names(self, table_names):
        r"""Sets the table_names of this ListTableResponse.

        返回的表名列表。 - 长度：最大100

        :param table_names: The table_names of this ListTableResponse.
        :type table_names: list[str]
        """
        self._table_names = table_names

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
        if not isinstance(other, ListTableResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
