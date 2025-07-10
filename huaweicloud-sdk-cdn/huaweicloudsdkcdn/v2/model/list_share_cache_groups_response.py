# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListShareCacheGroupsResponse(SdkResponse):

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
        'share_cache_groups': 'list[ListShareCacheGroupsConfig]'
    }

    attribute_map = {
        'total': 'total',
        'share_cache_groups': 'share_cache_groups'
    }

    def __init__(self, total=None, share_cache_groups=None):
        r"""ListShareCacheGroupsResponse

        The model defined in huaweicloud sdk

        :param total: 共享缓存配置总数量
        :type total: int
        :param share_cache_groups: 共享缓存配置
        :type share_cache_groups: list[:class:`huaweicloudsdkcdn.v2.ListShareCacheGroupsConfig`]
        """
        
        super(ListShareCacheGroupsResponse, self).__init__()

        self._total = None
        self._share_cache_groups = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if share_cache_groups is not None:
            self.share_cache_groups = share_cache_groups

    @property
    def total(self):
        r"""Gets the total of this ListShareCacheGroupsResponse.

        共享缓存配置总数量

        :return: The total of this ListShareCacheGroupsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListShareCacheGroupsResponse.

        共享缓存配置总数量

        :param total: The total of this ListShareCacheGroupsResponse.
        :type total: int
        """
        self._total = total

    @property
    def share_cache_groups(self):
        r"""Gets the share_cache_groups of this ListShareCacheGroupsResponse.

        共享缓存配置

        :return: The share_cache_groups of this ListShareCacheGroupsResponse.
        :rtype: list[:class:`huaweicloudsdkcdn.v2.ListShareCacheGroupsConfig`]
        """
        return self._share_cache_groups

    @share_cache_groups.setter
    def share_cache_groups(self, share_cache_groups):
        r"""Sets the share_cache_groups of this ListShareCacheGroupsResponse.

        共享缓存配置

        :param share_cache_groups: The share_cache_groups of this ListShareCacheGroupsResponse.
        :type share_cache_groups: list[:class:`huaweicloudsdkcdn.v2.ListShareCacheGroupsConfig`]
        """
        self._share_cache_groups = share_cache_groups

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
        if not isinstance(other, ListShareCacheGroupsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
