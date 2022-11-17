# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSimPoolsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'offset': 'int',
        'count': 'int',
        'pools': 'list[SimPoolVO]'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'count': 'count',
        'pools': 'pools'
    }

    def __init__(self, limit=None, offset=None, count=None, pools=None):
        """ListSimPoolsResponse

        The model defined in huaweicloud sdk

        :param limit: 每页记录数
        :type limit: int
        :param offset: 页码
        :type offset: int
        :param count: 当前查询条件的流量池总数
        :type count: int
        :param pools: 当前页的流量池记录列表
        :type pools: list[:class:`huaweicloudsdkgsl.v3.SimPoolVO`]
        """
        
        super(ListSimPoolsResponse, self).__init__()

        self._limit = None
        self._offset = None
        self._count = None
        self._pools = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if count is not None:
            self.count = count
        if pools is not None:
            self.pools = pools

    @property
    def limit(self):
        """Gets the limit of this ListSimPoolsResponse.

        每页记录数

        :return: The limit of this ListSimPoolsResponse.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListSimPoolsResponse.

        每页记录数

        :param limit: The limit of this ListSimPoolsResponse.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListSimPoolsResponse.

        页码

        :return: The offset of this ListSimPoolsResponse.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListSimPoolsResponse.

        页码

        :param offset: The offset of this ListSimPoolsResponse.
        :type offset: int
        """
        self._offset = offset

    @property
    def count(self):
        """Gets the count of this ListSimPoolsResponse.

        当前查询条件的流量池总数

        :return: The count of this ListSimPoolsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListSimPoolsResponse.

        当前查询条件的流量池总数

        :param count: The count of this ListSimPoolsResponse.
        :type count: int
        """
        self._count = count

    @property
    def pools(self):
        """Gets the pools of this ListSimPoolsResponse.

        当前页的流量池记录列表

        :return: The pools of this ListSimPoolsResponse.
        :rtype: list[:class:`huaweicloudsdkgsl.v3.SimPoolVO`]
        """
        return self._pools

    @pools.setter
    def pools(self, pools):
        """Sets the pools of this ListSimPoolsResponse.

        当前页的流量池记录列表

        :param pools: The pools of this ListSimPoolsResponse.
        :type pools: list[:class:`huaweicloudsdkgsl.v3.SimPoolVO`]
        """
        self._pools = pools

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
        if not isinstance(other, ListSimPoolsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
