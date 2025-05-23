# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListStoreRequestBody:

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
        'limit': 'int'
    }

    attribute_map = {
        'cursor_name': 'cursor_name',
        'limit': 'limit'
    }

    def __init__(self, cursor_name=None, limit=None):
        r"""ListStoreRequestBody

        The model defined in huaweicloud sdk

        :param cursor_name: 上次返回的游标位置，本次响应包含该仓名。 - 长度：[16,52] - 取值字符限制：[a-z0-9-]+
        :type cursor_name: str
        :param limit: 响应返回的仓个数。
        :type limit: int
        """
        
        

        self._cursor_name = None
        self._limit = None
        self.discriminator = None

        if cursor_name is not None:
            self.cursor_name = cursor_name
        if limit is not None:
            self.limit = limit

    @property
    def cursor_name(self):
        r"""Gets the cursor_name of this ListStoreRequestBody.

        上次返回的游标位置，本次响应包含该仓名。 - 长度：[16,52] - 取值字符限制：[a-z0-9-]+

        :return: The cursor_name of this ListStoreRequestBody.
        :rtype: str
        """
        return self._cursor_name

    @cursor_name.setter
    def cursor_name(self, cursor_name):
        r"""Sets the cursor_name of this ListStoreRequestBody.

        上次返回的游标位置，本次响应包含该仓名。 - 长度：[16,52] - 取值字符限制：[a-z0-9-]+

        :param cursor_name: The cursor_name of this ListStoreRequestBody.
        :type cursor_name: str
        """
        self._cursor_name = cursor_name

    @property
    def limit(self):
        r"""Gets the limit of this ListStoreRequestBody.

        响应返回的仓个数。

        :return: The limit of this ListStoreRequestBody.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListStoreRequestBody.

        响应返回的仓个数。

        :param limit: The limit of this ListStoreRequestBody.
        :type limit: int
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
        if not isinstance(other, ListStoreRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
