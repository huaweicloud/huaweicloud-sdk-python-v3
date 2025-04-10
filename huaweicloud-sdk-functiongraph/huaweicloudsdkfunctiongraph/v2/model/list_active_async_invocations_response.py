# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListActiveAsyncInvocationsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'invocations': 'list[ListFunctionAsyncInvocationsResult]',
        'count': 'int',
        'next_marker': 'int'
    }

    attribute_map = {
        'invocations': 'invocations',
        'count': 'count',
        'next_marker': 'next_marker'
    }

    def __init__(self, invocations=None, count=None, next_marker=None):
        r"""ListActiveAsyncInvocationsResponse

        The model defined in huaweicloud sdk

        :param invocations: 异步调用记录列表。
        :type invocations: list[:class:`huaweicloudsdkfunctiongraph.v2.ListFunctionAsyncInvocationsResult`]
        :param count: 查询数据总条数
        :type count: int
        :param next_marker: 查询下一页的起始位置
        :type next_marker: int
        """
        
        super(ListActiveAsyncInvocationsResponse, self).__init__()

        self._invocations = None
        self._count = None
        self._next_marker = None
        self.discriminator = None

        if invocations is not None:
            self.invocations = invocations
        if count is not None:
            self.count = count
        if next_marker is not None:
            self.next_marker = next_marker

    @property
    def invocations(self):
        r"""Gets the invocations of this ListActiveAsyncInvocationsResponse.

        异步调用记录列表。

        :return: The invocations of this ListActiveAsyncInvocationsResponse.
        :rtype: list[:class:`huaweicloudsdkfunctiongraph.v2.ListFunctionAsyncInvocationsResult`]
        """
        return self._invocations

    @invocations.setter
    def invocations(self, invocations):
        r"""Sets the invocations of this ListActiveAsyncInvocationsResponse.

        异步调用记录列表。

        :param invocations: The invocations of this ListActiveAsyncInvocationsResponse.
        :type invocations: list[:class:`huaweicloudsdkfunctiongraph.v2.ListFunctionAsyncInvocationsResult`]
        """
        self._invocations = invocations

    @property
    def count(self):
        r"""Gets the count of this ListActiveAsyncInvocationsResponse.

        查询数据总条数

        :return: The count of this ListActiveAsyncInvocationsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListActiveAsyncInvocationsResponse.

        查询数据总条数

        :param count: The count of this ListActiveAsyncInvocationsResponse.
        :type count: int
        """
        self._count = count

    @property
    def next_marker(self):
        r"""Gets the next_marker of this ListActiveAsyncInvocationsResponse.

        查询下一页的起始位置

        :return: The next_marker of this ListActiveAsyncInvocationsResponse.
        :rtype: int
        """
        return self._next_marker

    @next_marker.setter
    def next_marker(self, next_marker):
        r"""Sets the next_marker of this ListActiveAsyncInvocationsResponse.

        查询下一页的起始位置

        :param next_marker: The next_marker of this ListActiveAsyncInvocationsResponse.
        :type next_marker: int
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
        if not isinstance(other, ListActiveAsyncInvocationsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
