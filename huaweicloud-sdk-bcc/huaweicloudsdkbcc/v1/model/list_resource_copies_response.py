# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListResourceCopiesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'copies': 'list[ResourceCopyItem]',
        'next_marker': 'str'
    }

    attribute_map = {
        'count': 'count',
        'copies': 'copies',
        'next_marker': 'next_marker'
    }

    def __init__(self, count=None, copies=None, next_marker=None):
        r"""ListResourceCopiesResponse

        The model defined in huaweicloud sdk

        :param count: 副本总数
        :type count: int
        :param copies: 副本列表
        :type copies: list[:class:`huaweicloudsdkbcc.v1.ResourceCopyItem`]
        :param next_marker: 下一页的marker
        :type next_marker: str
        """
        
        super(ListResourceCopiesResponse, self).__init__()

        self._count = None
        self._copies = None
        self._next_marker = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if copies is not None:
            self.copies = copies
        if next_marker is not None:
            self.next_marker = next_marker

    @property
    def count(self):
        r"""Gets the count of this ListResourceCopiesResponse.

        副本总数

        :return: The count of this ListResourceCopiesResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListResourceCopiesResponse.

        副本总数

        :param count: The count of this ListResourceCopiesResponse.
        :type count: int
        """
        self._count = count

    @property
    def copies(self):
        r"""Gets the copies of this ListResourceCopiesResponse.

        副本列表

        :return: The copies of this ListResourceCopiesResponse.
        :rtype: list[:class:`huaweicloudsdkbcc.v1.ResourceCopyItem`]
        """
        return self._copies

    @copies.setter
    def copies(self, copies):
        r"""Sets the copies of this ListResourceCopiesResponse.

        副本列表

        :param copies: The copies of this ListResourceCopiesResponse.
        :type copies: list[:class:`huaweicloudsdkbcc.v1.ResourceCopyItem`]
        """
        self._copies = copies

    @property
    def next_marker(self):
        r"""Gets the next_marker of this ListResourceCopiesResponse.

        下一页的marker

        :return: The next_marker of this ListResourceCopiesResponse.
        :rtype: str
        """
        return self._next_marker

    @next_marker.setter
    def next_marker(self, next_marker):
        r"""Sets the next_marker of this ListResourceCopiesResponse.

        下一页的marker

        :param next_marker: The next_marker of this ListResourceCopiesResponse.
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
        if not isinstance(other, ListResourceCopiesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
