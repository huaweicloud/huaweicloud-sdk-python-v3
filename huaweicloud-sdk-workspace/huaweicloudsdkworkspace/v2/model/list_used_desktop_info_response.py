# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListUsedDesktopInfoResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'desktop_used_info_list': 'list[DesktopUsedHoursInfo]',
        'total_count': 'int'
    }

    attribute_map = {
        'desktop_used_info_list': 'desktop_used_info_list',
        'total_count': 'total_count'
    }

    def __init__(self, desktop_used_info_list=None, total_count=None):
        """ListUsedDesktopInfoResponse

        The model defined in huaweicloud sdk

        :param desktop_used_info_list: 桌面使用信息（以桌面Id划分）。
        :type desktop_used_info_list: list[:class:`huaweicloudsdkworkspace.v2.DesktopUsedHoursInfo`]
        :param total_count: 总数。
        :type total_count: int
        """
        
        super(ListUsedDesktopInfoResponse, self).__init__()

        self._desktop_used_info_list = None
        self._total_count = None
        self.discriminator = None

        if desktop_used_info_list is not None:
            self.desktop_used_info_list = desktop_used_info_list
        if total_count is not None:
            self.total_count = total_count

    @property
    def desktop_used_info_list(self):
        """Gets the desktop_used_info_list of this ListUsedDesktopInfoResponse.

        桌面使用信息（以桌面Id划分）。

        :return: The desktop_used_info_list of this ListUsedDesktopInfoResponse.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.DesktopUsedHoursInfo`]
        """
        return self._desktop_used_info_list

    @desktop_used_info_list.setter
    def desktop_used_info_list(self, desktop_used_info_list):
        """Sets the desktop_used_info_list of this ListUsedDesktopInfoResponse.

        桌面使用信息（以桌面Id划分）。

        :param desktop_used_info_list: The desktop_used_info_list of this ListUsedDesktopInfoResponse.
        :type desktop_used_info_list: list[:class:`huaweicloudsdkworkspace.v2.DesktopUsedHoursInfo`]
        """
        self._desktop_used_info_list = desktop_used_info_list

    @property
    def total_count(self):
        """Gets the total_count of this ListUsedDesktopInfoResponse.

        总数。

        :return: The total_count of this ListUsedDesktopInfoResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ListUsedDesktopInfoResponse.

        总数。

        :param total_count: The total_count of this ListUsedDesktopInfoResponse.
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
        if not isinstance(other, ListUsedDesktopInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
