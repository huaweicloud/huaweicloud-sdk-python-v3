# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDbCacheMappingsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_count': 'int',
        'dbcache_mappings': 'list[QueryDBCacheMappingResponse]'
    }

    attribute_map = {
        'total_count': 'total_count',
        'dbcache_mappings': 'dbcache_mappings'
    }

    def __init__(self, total_count=None, dbcache_mappings=None):
        r"""ListDbCacheMappingsResponse

        The model defined in huaweicloud sdk

        :param total_count: 总记录数。
        :type total_count: int
        :param dbcache_mappings: 内存加速映射信息。
        :type dbcache_mappings: list[:class:`huaweicloudsdkgaussdbfornosql.v3.QueryDBCacheMappingResponse`]
        """
        
        super(ListDbCacheMappingsResponse, self).__init__()

        self._total_count = None
        self._dbcache_mappings = None
        self.discriminator = None

        if total_count is not None:
            self.total_count = total_count
        if dbcache_mappings is not None:
            self.dbcache_mappings = dbcache_mappings

    @property
    def total_count(self):
        r"""Gets the total_count of this ListDbCacheMappingsResponse.

        总记录数。

        :return: The total_count of this ListDbCacheMappingsResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListDbCacheMappingsResponse.

        总记录数。

        :param total_count: The total_count of this ListDbCacheMappingsResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def dbcache_mappings(self):
        r"""Gets the dbcache_mappings of this ListDbCacheMappingsResponse.

        内存加速映射信息。

        :return: The dbcache_mappings of this ListDbCacheMappingsResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdbfornosql.v3.QueryDBCacheMappingResponse`]
        """
        return self._dbcache_mappings

    @dbcache_mappings.setter
    def dbcache_mappings(self, dbcache_mappings):
        r"""Sets the dbcache_mappings of this ListDbCacheMappingsResponse.

        内存加速映射信息。

        :param dbcache_mappings: The dbcache_mappings of this ListDbCacheMappingsResponse.
        :type dbcache_mappings: list[:class:`huaweicloudsdkgaussdbfornosql.v3.QueryDBCacheMappingResponse`]
        """
        self._dbcache_mappings = dbcache_mappings

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
        if not isinstance(other, ListDbCacheMappingsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
