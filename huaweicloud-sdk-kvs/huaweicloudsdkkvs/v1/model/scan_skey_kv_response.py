# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ScanSkeyKvResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'returned_count': 'int',
        'filtered_count': 'int',
        'cursor_sort_key': 'dict',
        'returned_kv_items': 'list[ReturnedKvItem]'
    }

    attribute_map = {
        'returned_count': 'returned_count',
        'filtered_count': 'filtered_count',
        'cursor_sort_key': 'cursor_sort_key',
        'returned_kv_items': 'returned_kv_items'
    }

    def __init__(self, returned_count=None, filtered_count=None, cursor_sort_key=None, returned_kv_items=None):
        r"""ScanSkeyKvResponse

        The model defined in huaweicloud sdk

        :param returned_count: 返回的文档数量，为0不表示结束。 - 如果filtered_count超过500仍无匹配，则返回0。 -  长度：4
        :type returned_count: int
        :param filtered_count: 被过滤掉的文档数量。 - 长度：4
        :type filtered_count: int
        :param cursor_sort_key: 下次请求时的start_key。 &gt; 该值为空时，表示指定范围或者指定filter条件所有kv已经返回。
        :type cursor_sort_key: dict
        :param returned_kv_items: 返回的kv列表，与scan_kv的kv_array相同。
        :type returned_kv_items: list[:class:`huaweicloudsdkkvs.v1.ReturnedKvItem`]
        """
        
        super(ScanSkeyKvResponse, self).__init__()

        self._returned_count = None
        self._filtered_count = None
        self._cursor_sort_key = None
        self._returned_kv_items = None
        self.discriminator = None

        if returned_count is not None:
            self.returned_count = returned_count
        if filtered_count is not None:
            self.filtered_count = filtered_count
        if cursor_sort_key is not None:
            self.cursor_sort_key = cursor_sort_key
        if returned_kv_items is not None:
            self.returned_kv_items = returned_kv_items

    @property
    def returned_count(self):
        r"""Gets the returned_count of this ScanSkeyKvResponse.

        返回的文档数量，为0不表示结束。 - 如果filtered_count超过500仍无匹配，则返回0。 -  长度：4

        :return: The returned_count of this ScanSkeyKvResponse.
        :rtype: int
        """
        return self._returned_count

    @returned_count.setter
    def returned_count(self, returned_count):
        r"""Sets the returned_count of this ScanSkeyKvResponse.

        返回的文档数量，为0不表示结束。 - 如果filtered_count超过500仍无匹配，则返回0。 -  长度：4

        :param returned_count: The returned_count of this ScanSkeyKvResponse.
        :type returned_count: int
        """
        self._returned_count = returned_count

    @property
    def filtered_count(self):
        r"""Gets the filtered_count of this ScanSkeyKvResponse.

        被过滤掉的文档数量。 - 长度：4

        :return: The filtered_count of this ScanSkeyKvResponse.
        :rtype: int
        """
        return self._filtered_count

    @filtered_count.setter
    def filtered_count(self, filtered_count):
        r"""Sets the filtered_count of this ScanSkeyKvResponse.

        被过滤掉的文档数量。 - 长度：4

        :param filtered_count: The filtered_count of this ScanSkeyKvResponse.
        :type filtered_count: int
        """
        self._filtered_count = filtered_count

    @property
    def cursor_sort_key(self):
        r"""Gets the cursor_sort_key of this ScanSkeyKvResponse.

        下次请求时的start_key。 > 该值为空时，表示指定范围或者指定filter条件所有kv已经返回。

        :return: The cursor_sort_key of this ScanSkeyKvResponse.
        :rtype: dict
        """
        return self._cursor_sort_key

    @cursor_sort_key.setter
    def cursor_sort_key(self, cursor_sort_key):
        r"""Sets the cursor_sort_key of this ScanSkeyKvResponse.

        下次请求时的start_key。 > 该值为空时，表示指定范围或者指定filter条件所有kv已经返回。

        :param cursor_sort_key: The cursor_sort_key of this ScanSkeyKvResponse.
        :type cursor_sort_key: dict
        """
        self._cursor_sort_key = cursor_sort_key

    @property
    def returned_kv_items(self):
        r"""Gets the returned_kv_items of this ScanSkeyKvResponse.

        返回的kv列表，与scan_kv的kv_array相同。

        :return: The returned_kv_items of this ScanSkeyKvResponse.
        :rtype: list[:class:`huaweicloudsdkkvs.v1.ReturnedKvItem`]
        """
        return self._returned_kv_items

    @returned_kv_items.setter
    def returned_kv_items(self, returned_kv_items):
        r"""Sets the returned_kv_items of this ScanSkeyKvResponse.

        返回的kv列表，与scan_kv的kv_array相同。

        :param returned_kv_items: The returned_kv_items of this ScanSkeyKvResponse.
        :type returned_kv_items: list[:class:`huaweicloudsdkkvs.v1.ReturnedKvItem`]
        """
        self._returned_kv_items = returned_kv_items

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
        if not isinstance(other, ScanSkeyKvResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
