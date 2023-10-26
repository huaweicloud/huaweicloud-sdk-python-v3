# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowUrlTaskInfoResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'count': 'int',
        'result': 'list[Urls]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'total': 'total',
        'count': 'count',
        'result': 'result',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, total=None, count=None, result=None, x_request_id=None):
        """ShowUrlTaskInfoResponse

        The model defined in huaweicloud sdk

        :param total: 查询结果总数。
        :type total: int
        :param count: 当前查询到的总页数。
        :type count: int
        :param result: url信息。
        :type result: list[:class:`huaweicloudsdkcdn.v2.Urls`]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ShowUrlTaskInfoResponse, self).__init__()

        self._total = None
        self._count = None
        self._result = None
        self._x_request_id = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if count is not None:
            self.count = count
        if result is not None:
            self.result = result
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def total(self):
        """Gets the total of this ShowUrlTaskInfoResponse.

        查询结果总数。

        :return: The total of this ShowUrlTaskInfoResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ShowUrlTaskInfoResponse.

        查询结果总数。

        :param total: The total of this ShowUrlTaskInfoResponse.
        :type total: int
        """
        self._total = total

    @property
    def count(self):
        """Gets the count of this ShowUrlTaskInfoResponse.

        当前查询到的总页数。

        :return: The count of this ShowUrlTaskInfoResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ShowUrlTaskInfoResponse.

        当前查询到的总页数。

        :param count: The count of this ShowUrlTaskInfoResponse.
        :type count: int
        """
        self._count = count

    @property
    def result(self):
        """Gets the result of this ShowUrlTaskInfoResponse.

        url信息。

        :return: The result of this ShowUrlTaskInfoResponse.
        :rtype: list[:class:`huaweicloudsdkcdn.v2.Urls`]
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this ShowUrlTaskInfoResponse.

        url信息。

        :param result: The result of this ShowUrlTaskInfoResponse.
        :type result: list[:class:`huaweicloudsdkcdn.v2.Urls`]
        """
        self._result = result

    @property
    def x_request_id(self):
        """Gets the x_request_id of this ShowUrlTaskInfoResponse.

        :return: The x_request_id of this ShowUrlTaskInfoResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this ShowUrlTaskInfoResponse.

        :param x_request_id: The x_request_id of this ShowUrlTaskInfoResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, ShowUrlTaskInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
