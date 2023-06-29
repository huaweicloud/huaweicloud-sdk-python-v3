# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListUnusedDesktopsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'unused_desktops': 'list[UnusedDesktopInfo]',
        'total_count': 'int'
    }

    attribute_map = {
        'unused_desktops': 'unused_desktops',
        'total_count': 'total_count'
    }

    def __init__(self, unused_desktops=None, total_count=None):
        """ListUnusedDesktopsResponse

        The model defined in huaweicloud sdk

        :param unused_desktops: 指定时间段内未使用桌面列表。
        :type unused_desktops: list[:class:`huaweicloudsdkworkspace.v2.UnusedDesktopInfo`]
        :param total_count: 总数。
        :type total_count: int
        """
        
        super(ListUnusedDesktopsResponse, self).__init__()

        self._unused_desktops = None
        self._total_count = None
        self.discriminator = None

        if unused_desktops is not None:
            self.unused_desktops = unused_desktops
        if total_count is not None:
            self.total_count = total_count

    @property
    def unused_desktops(self):
        """Gets the unused_desktops of this ListUnusedDesktopsResponse.

        指定时间段内未使用桌面列表。

        :return: The unused_desktops of this ListUnusedDesktopsResponse.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.UnusedDesktopInfo`]
        """
        return self._unused_desktops

    @unused_desktops.setter
    def unused_desktops(self, unused_desktops):
        """Sets the unused_desktops of this ListUnusedDesktopsResponse.

        指定时间段内未使用桌面列表。

        :param unused_desktops: The unused_desktops of this ListUnusedDesktopsResponse.
        :type unused_desktops: list[:class:`huaweicloudsdkworkspace.v2.UnusedDesktopInfo`]
        """
        self._unused_desktops = unused_desktops

    @property
    def total_count(self):
        """Gets the total_count of this ListUnusedDesktopsResponse.

        总数。

        :return: The total_count of this ListUnusedDesktopsResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ListUnusedDesktopsResponse.

        总数。

        :param total_count: The total_count of this ListUnusedDesktopsResponse.
        :type total_count: int
        """
        self._total_count = total_count

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
        if not isinstance(other, ListUnusedDesktopsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
