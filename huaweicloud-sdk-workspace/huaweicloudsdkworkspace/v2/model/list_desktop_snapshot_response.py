# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDesktopSnapshotResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'desktop_snapshots': 'list[DesktopSnapshotDetailInfo]',
        'total_count': 'int'
    }

    attribute_map = {
        'desktop_snapshots': 'desktop_snapshots',
        'total_count': 'total_count'
    }

    def __init__(self, desktop_snapshots=None, total_count=None):
        r"""ListDesktopSnapshotResponse

        The model defined in huaweicloud sdk

        :param desktop_snapshots: 桌面快照详情列表。
        :type desktop_snapshots: list[:class:`huaweicloudsdkworkspace.v2.DesktopSnapshotDetailInfo`]
        :param total_count: 桌面快照总数。
        :type total_count: int
        """
        
        super(ListDesktopSnapshotResponse, self).__init__()

        self._desktop_snapshots = None
        self._total_count = None
        self.discriminator = None

        if desktop_snapshots is not None:
            self.desktop_snapshots = desktop_snapshots
        if total_count is not None:
            self.total_count = total_count

    @property
    def desktop_snapshots(self):
        r"""Gets the desktop_snapshots of this ListDesktopSnapshotResponse.

        桌面快照详情列表。

        :return: The desktop_snapshots of this ListDesktopSnapshotResponse.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.DesktopSnapshotDetailInfo`]
        """
        return self._desktop_snapshots

    @desktop_snapshots.setter
    def desktop_snapshots(self, desktop_snapshots):
        r"""Sets the desktop_snapshots of this ListDesktopSnapshotResponse.

        桌面快照详情列表。

        :param desktop_snapshots: The desktop_snapshots of this ListDesktopSnapshotResponse.
        :type desktop_snapshots: list[:class:`huaweicloudsdkworkspace.v2.DesktopSnapshotDetailInfo`]
        """
        self._desktop_snapshots = desktop_snapshots

    @property
    def total_count(self):
        r"""Gets the total_count of this ListDesktopSnapshotResponse.

        桌面快照总数。

        :return: The total_count of this ListDesktopSnapshotResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListDesktopSnapshotResponse.

        桌面快照总数。

        :param total_count: The total_count of this ListDesktopSnapshotResponse.
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
        if not isinstance(other, ListDesktopSnapshotResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
