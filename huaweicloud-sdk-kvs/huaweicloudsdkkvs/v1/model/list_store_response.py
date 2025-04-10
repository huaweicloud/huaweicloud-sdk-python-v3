# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListStoreResponse(SdkResponse):

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
        'stores': 'list[str]'
    }

    attribute_map = {
        'cursor_name': 'cursor_name',
        'stores': 'stores'
    }

    def __init__(self, cursor_name=None, stores=None):
        r"""ListStoreResponse

        The model defined in huaweicloud sdk

        :param cursor_name: 本次响应后的游标位置，下次请求时携带。 - 长度：[16,52] - 取值字符限制：[a-z0-9-]+ &gt; 如果为空，表示后面无更多仓名。
        :type cursor_name: str
        :param stores: 返回的仓名列表。
        :type stores: list[str]
        """
        
        super(ListStoreResponse, self).__init__()

        self._cursor_name = None
        self._stores = None
        self.discriminator = None

        if cursor_name is not None:
            self.cursor_name = cursor_name
        if stores is not None:
            self.stores = stores

    @property
    def cursor_name(self):
        r"""Gets the cursor_name of this ListStoreResponse.

        本次响应后的游标位置，下次请求时携带。 - 长度：[16,52] - 取值字符限制：[a-z0-9-]+ > 如果为空，表示后面无更多仓名。

        :return: The cursor_name of this ListStoreResponse.
        :rtype: str
        """
        return self._cursor_name

    @cursor_name.setter
    def cursor_name(self, cursor_name):
        r"""Sets the cursor_name of this ListStoreResponse.

        本次响应后的游标位置，下次请求时携带。 - 长度：[16,52] - 取值字符限制：[a-z0-9-]+ > 如果为空，表示后面无更多仓名。

        :param cursor_name: The cursor_name of this ListStoreResponse.
        :type cursor_name: str
        """
        self._cursor_name = cursor_name

    @property
    def stores(self):
        r"""Gets the stores of this ListStoreResponse.

        返回的仓名列表。

        :return: The stores of this ListStoreResponse.
        :rtype: list[str]
        """
        return self._stores

    @stores.setter
    def stores(self, stores):
        r"""Sets the stores of this ListStoreResponse.

        返回的仓名列表。

        :param stores: The stores of this ListStoreResponse.
        :type stores: list[str]
        """
        self._stores = stores

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
        if not isinstance(other, ListStoreResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
