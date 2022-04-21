# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSnapshotsResponse(SdkResponse):

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
        'snapshots': 'list[SnapshotList]',
        'snapshots_links': 'list[Link]'
    }

    attribute_map = {
        'count': 'count',
        'snapshots': 'snapshots',
        'snapshots_links': 'snapshots_links'
    }

    def __init__(self, count=None, snapshots=None, snapshots_links=None):
        """ListSnapshotsResponse

        The model defined in huaweicloud sdk

        :param count: 快照的总数量，不受limi参数的影响。
        :type count: int
        :param snapshots: 快照信息。
        :type snapshots: list[:class:`huaweicloudsdkevs.v2.SnapshotList`]
        :param snapshots_links: 云硬盘快照列表查询位置标记。当查询时指定limit时会返回该字段，返回该字段表示本次查询只查出了部分云硬盘快照信息。
        :type snapshots_links: list[:class:`huaweicloudsdkevs.v2.Link`]
        """
        
        super(ListSnapshotsResponse, self).__init__()

        self._count = None
        self._snapshots = None
        self._snapshots_links = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if snapshots is not None:
            self.snapshots = snapshots
        if snapshots_links is not None:
            self.snapshots_links = snapshots_links

    @property
    def count(self):
        """Gets the count of this ListSnapshotsResponse.

        快照的总数量，不受limi参数的影响。

        :return: The count of this ListSnapshotsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListSnapshotsResponse.

        快照的总数量，不受limi参数的影响。

        :param count: The count of this ListSnapshotsResponse.
        :type count: int
        """
        self._count = count

    @property
    def snapshots(self):
        """Gets the snapshots of this ListSnapshotsResponse.

        快照信息。

        :return: The snapshots of this ListSnapshotsResponse.
        :rtype: list[:class:`huaweicloudsdkevs.v2.SnapshotList`]
        """
        return self._snapshots

    @snapshots.setter
    def snapshots(self, snapshots):
        """Sets the snapshots of this ListSnapshotsResponse.

        快照信息。

        :param snapshots: The snapshots of this ListSnapshotsResponse.
        :type snapshots: list[:class:`huaweicloudsdkevs.v2.SnapshotList`]
        """
        self._snapshots = snapshots

    @property
    def snapshots_links(self):
        """Gets the snapshots_links of this ListSnapshotsResponse.

        云硬盘快照列表查询位置标记。当查询时指定limit时会返回该字段，返回该字段表示本次查询只查出了部分云硬盘快照信息。

        :return: The snapshots_links of this ListSnapshotsResponse.
        :rtype: list[:class:`huaweicloudsdkevs.v2.Link`]
        """
        return self._snapshots_links

    @snapshots_links.setter
    def snapshots_links(self, snapshots_links):
        """Sets the snapshots_links of this ListSnapshotsResponse.

        云硬盘快照列表查询位置标记。当查询时指定limit时会返回该字段，返回该字段表示本次查询只查出了部分云硬盘快照信息。

        :param snapshots_links: The snapshots_links of this ListSnapshotsResponse.
        :type snapshots_links: list[:class:`huaweicloudsdkevs.v2.Link`]
        """
        self._snapshots_links = snapshots_links

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
        if not isinstance(other, ListSnapshotsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
