# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDesktopPoolsResponse(SdkResponse):

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
        'desktop_pools': 'list[SimpleDesktopPoolInfo]'
    }

    attribute_map = {
        'total_count': 'total_count',
        'desktop_pools': 'desktop_pools'
    }

    def __init__(self, total_count=None, desktop_pools=None):
        r"""ListDesktopPoolsResponse

        The model defined in huaweicloud sdk

        :param total_count: 总数。
        :type total_count: int
        :param desktop_pools: 桌面池信息。
        :type desktop_pools: list[:class:`huaweicloudsdkworkspace.v2.SimpleDesktopPoolInfo`]
        """
        
        super(ListDesktopPoolsResponse, self).__init__()

        self._total_count = None
        self._desktop_pools = None
        self.discriminator = None

        if total_count is not None:
            self.total_count = total_count
        if desktop_pools is not None:
            self.desktop_pools = desktop_pools

    @property
    def total_count(self):
        r"""Gets the total_count of this ListDesktopPoolsResponse.

        总数。

        :return: The total_count of this ListDesktopPoolsResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListDesktopPoolsResponse.

        总数。

        :param total_count: The total_count of this ListDesktopPoolsResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def desktop_pools(self):
        r"""Gets the desktop_pools of this ListDesktopPoolsResponse.

        桌面池信息。

        :return: The desktop_pools of this ListDesktopPoolsResponse.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.SimpleDesktopPoolInfo`]
        """
        return self._desktop_pools

    @desktop_pools.setter
    def desktop_pools(self, desktop_pools):
        r"""Sets the desktop_pools of this ListDesktopPoolsResponse.

        桌面池信息。

        :param desktop_pools: The desktop_pools of this ListDesktopPoolsResponse.
        :type desktop_pools: list[:class:`huaweicloudsdkworkspace.v2.SimpleDesktopPoolInfo`]
        """
        self._desktop_pools = desktop_pools

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
        if not isinstance(other, ListDesktopPoolsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
