# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDesktopsResponse(SdkResponse):

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
        'desktops': 'list[SimpleDesktopInfo]',
        'desktop_infos': 'list[SimpleDesktopInfoDetail]'
    }

    attribute_map = {
        'total_count': 'total_count',
        'desktops': 'desktops',
        'desktop_infos': 'desktop_infos'
    }

    def __init__(self, total_count=None, desktops=None, desktop_infos=None):
        r"""ListDesktopsResponse

        The model defined in huaweicloud sdk

        :param total_count: 总数。
        :type total_count: int
        :param desktops: 桌面信息。
        :type desktops: list[:class:`huaweicloudsdkworkspace.v2.SimpleDesktopInfo`]
        :param desktop_infos: Workspace桌面列表。
        :type desktop_infos: list[:class:`huaweicloudsdkworkspace.v2.SimpleDesktopInfoDetail`]
        """
        
        super(ListDesktopsResponse, self).__init__()

        self._total_count = None
        self._desktops = None
        self._desktop_infos = None
        self.discriminator = None

        if total_count is not None:
            self.total_count = total_count
        if desktops is not None:
            self.desktops = desktops
        if desktop_infos is not None:
            self.desktop_infos = desktop_infos

    @property
    def total_count(self):
        r"""Gets the total_count of this ListDesktopsResponse.

        总数。

        :return: The total_count of this ListDesktopsResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListDesktopsResponse.

        总数。

        :param total_count: The total_count of this ListDesktopsResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def desktops(self):
        r"""Gets the desktops of this ListDesktopsResponse.

        桌面信息。

        :return: The desktops of this ListDesktopsResponse.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.SimpleDesktopInfo`]
        """
        return self._desktops

    @desktops.setter
    def desktops(self, desktops):
        r"""Sets the desktops of this ListDesktopsResponse.

        桌面信息。

        :param desktops: The desktops of this ListDesktopsResponse.
        :type desktops: list[:class:`huaweicloudsdkworkspace.v2.SimpleDesktopInfo`]
        """
        self._desktops = desktops

    @property
    def desktop_infos(self):
        r"""Gets the desktop_infos of this ListDesktopsResponse.

        Workspace桌面列表。

        :return: The desktop_infos of this ListDesktopsResponse.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.SimpleDesktopInfoDetail`]
        """
        return self._desktop_infos

    @desktop_infos.setter
    def desktop_infos(self, desktop_infos):
        r"""Sets the desktop_infos of this ListDesktopsResponse.

        Workspace桌面列表。

        :param desktop_infos: The desktop_infos of this ListDesktopsResponse.
        :type desktop_infos: list[:class:`huaweicloudsdkworkspace.v2.SimpleDesktopInfoDetail`]
        """
        self._desktop_infos = desktop_infos

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
        if not isinstance(other, ListDesktopsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
