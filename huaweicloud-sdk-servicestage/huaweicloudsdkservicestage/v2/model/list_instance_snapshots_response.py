# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstanceSnapshotsResponse(SdkResponse):

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
        'snapshots': 'list[InstanceSnapshotView]'
    }

    attribute_map = {
        'count': 'count',
        'snapshots': 'snapshots'
    }

    def __init__(self, count=None, snapshots=None):
        r"""ListInstanceSnapshotsResponse

        The model defined in huaweicloud sdk

        :param count: 快照总数。
        :type count: int
        :param snapshots: 快照列表。
        :type snapshots: list[:class:`huaweicloudsdkservicestage.v2.InstanceSnapshotView`]
        """
        
        super(ListInstanceSnapshotsResponse, self).__init__()

        self._count = None
        self._snapshots = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if snapshots is not None:
            self.snapshots = snapshots

    @property
    def count(self):
        r"""Gets the count of this ListInstanceSnapshotsResponse.

        快照总数。

        :return: The count of this ListInstanceSnapshotsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListInstanceSnapshotsResponse.

        快照总数。

        :param count: The count of this ListInstanceSnapshotsResponse.
        :type count: int
        """
        self._count = count

    @property
    def snapshots(self):
        r"""Gets the snapshots of this ListInstanceSnapshotsResponse.

        快照列表。

        :return: The snapshots of this ListInstanceSnapshotsResponse.
        :rtype: list[:class:`huaweicloudsdkservicestage.v2.InstanceSnapshotView`]
        """
        return self._snapshots

    @snapshots.setter
    def snapshots(self, snapshots):
        r"""Sets the snapshots of this ListInstanceSnapshotsResponse.

        快照列表。

        :param snapshots: The snapshots of this ListInstanceSnapshotsResponse.
        :type snapshots: list[:class:`huaweicloudsdkservicestage.v2.InstanceSnapshotView`]
        """
        self._snapshots = snapshots

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
        if not isinstance(other, ListInstanceSnapshotsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
