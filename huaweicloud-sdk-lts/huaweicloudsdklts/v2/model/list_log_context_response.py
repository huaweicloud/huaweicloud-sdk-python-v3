# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListLogContextResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'logs': 'list[LogContents]',
        'total_count': 'int',
        'backwards_count': 'int',
        'forwards_count': 'int',
        'is_query_complete': 'bool'
    }

    attribute_map = {
        'logs': 'logs',
        'total_count': 'total_count',
        'backwards_count': 'backwards_count',
        'forwards_count': 'forwards_count',
        'is_query_complete': 'isQueryComplete'
    }

    def __init__(self, logs=None, total_count=None, backwards_count=None, forwards_count=None, is_query_complete=None):
        r"""ListLogContextResponse

        The model defined in huaweicloud sdk

        :param logs: 上下文日志信息。
        :type logs: list[:class:`huaweicloudsdklts.v2.LogContents`]
        :param total_count: 返回的总日志条数，包含请求参数中所指定的起始日志。
        :type total_count: int
        :param backwards_count: 向前查询到的日志条数。
        :type backwards_count: int
        :param forwards_count: 向后查询到的日志条数。
        :type forwards_count: int
        :param is_query_complete: 是否查询完成。
        :type is_query_complete: bool
        """
        
        super(ListLogContextResponse, self).__init__()

        self._logs = None
        self._total_count = None
        self._backwards_count = None
        self._forwards_count = None
        self._is_query_complete = None
        self.discriminator = None

        if logs is not None:
            self.logs = logs
        if total_count is not None:
            self.total_count = total_count
        if backwards_count is not None:
            self.backwards_count = backwards_count
        if forwards_count is not None:
            self.forwards_count = forwards_count
        if is_query_complete is not None:
            self.is_query_complete = is_query_complete

    @property
    def logs(self):
        r"""Gets the logs of this ListLogContextResponse.

        上下文日志信息。

        :return: The logs of this ListLogContextResponse.
        :rtype: list[:class:`huaweicloudsdklts.v2.LogContents`]
        """
        return self._logs

    @logs.setter
    def logs(self, logs):
        r"""Sets the logs of this ListLogContextResponse.

        上下文日志信息。

        :param logs: The logs of this ListLogContextResponse.
        :type logs: list[:class:`huaweicloudsdklts.v2.LogContents`]
        """
        self._logs = logs

    @property
    def total_count(self):
        r"""Gets the total_count of this ListLogContextResponse.

        返回的总日志条数，包含请求参数中所指定的起始日志。

        :return: The total_count of this ListLogContextResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListLogContextResponse.

        返回的总日志条数，包含请求参数中所指定的起始日志。

        :param total_count: The total_count of this ListLogContextResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def backwards_count(self):
        r"""Gets the backwards_count of this ListLogContextResponse.

        向前查询到的日志条数。

        :return: The backwards_count of this ListLogContextResponse.
        :rtype: int
        """
        return self._backwards_count

    @backwards_count.setter
    def backwards_count(self, backwards_count):
        r"""Sets the backwards_count of this ListLogContextResponse.

        向前查询到的日志条数。

        :param backwards_count: The backwards_count of this ListLogContextResponse.
        :type backwards_count: int
        """
        self._backwards_count = backwards_count

    @property
    def forwards_count(self):
        r"""Gets the forwards_count of this ListLogContextResponse.

        向后查询到的日志条数。

        :return: The forwards_count of this ListLogContextResponse.
        :rtype: int
        """
        return self._forwards_count

    @forwards_count.setter
    def forwards_count(self, forwards_count):
        r"""Sets the forwards_count of this ListLogContextResponse.

        向后查询到的日志条数。

        :param forwards_count: The forwards_count of this ListLogContextResponse.
        :type forwards_count: int
        """
        self._forwards_count = forwards_count

    @property
    def is_query_complete(self):
        r"""Gets the is_query_complete of this ListLogContextResponse.

        是否查询完成。

        :return: The is_query_complete of this ListLogContextResponse.
        :rtype: bool
        """
        return self._is_query_complete

    @is_query_complete.setter
    def is_query_complete(self, is_query_complete):
        r"""Sets the is_query_complete of this ListLogContextResponse.

        是否查询完成。

        :param is_query_complete: The is_query_complete of this ListLogContextResponse.
        :type is_query_complete: bool
        """
        self._is_query_complete = is_query_complete

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
        if not isinstance(other, ListLogContextResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
