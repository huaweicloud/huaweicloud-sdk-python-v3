# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFunctionVersionsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'versions': 'list[ListFunctionVersionResult]',
        'next_marker': 'int',
        'count': 'int'
    }

    attribute_map = {
        'versions': 'versions',
        'next_marker': 'next_marker',
        'count': 'count'
    }

    def __init__(self, versions=None, next_marker=None, count=None):
        """ListFunctionVersionsResponse

        The model defined in huaweicloud sdk

        :param versions: 版本列表
        :type versions: list[:class:`huaweicloudsdkfunctiongraph.v2.ListFunctionVersionResult`]
        :param next_marker: 下一次记录位置
        :type next_marker: int
        :param count: 版本总数
        :type count: int
        """
        
        super(ListFunctionVersionsResponse, self).__init__()

        self._versions = None
        self._next_marker = None
        self._count = None
        self.discriminator = None

        if versions is not None:
            self.versions = versions
        if next_marker is not None:
            self.next_marker = next_marker
        if count is not None:
            self.count = count

    @property
    def versions(self):
        """Gets the versions of this ListFunctionVersionsResponse.

        版本列表

        :return: The versions of this ListFunctionVersionsResponse.
        :rtype: list[:class:`huaweicloudsdkfunctiongraph.v2.ListFunctionVersionResult`]
        """
        return self._versions

    @versions.setter
    def versions(self, versions):
        """Sets the versions of this ListFunctionVersionsResponse.

        版本列表

        :param versions: The versions of this ListFunctionVersionsResponse.
        :type versions: list[:class:`huaweicloudsdkfunctiongraph.v2.ListFunctionVersionResult`]
        """
        self._versions = versions

    @property
    def next_marker(self):
        """Gets the next_marker of this ListFunctionVersionsResponse.

        下一次记录位置

        :return: The next_marker of this ListFunctionVersionsResponse.
        :rtype: int
        """
        return self._next_marker

    @next_marker.setter
    def next_marker(self, next_marker):
        """Sets the next_marker of this ListFunctionVersionsResponse.

        下一次记录位置

        :param next_marker: The next_marker of this ListFunctionVersionsResponse.
        :type next_marker: int
        """
        self._next_marker = next_marker

    @property
    def count(self):
        """Gets the count of this ListFunctionVersionsResponse.

        版本总数

        :return: The count of this ListFunctionVersionsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListFunctionVersionsResponse.

        版本总数

        :param count: The count of this ListFunctionVersionsResponse.
        :type count: int
        """
        self._count = count

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
        if not isinstance(other, ListFunctionVersionsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
