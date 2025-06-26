# coding: utf-8

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
        'snapshots': 'list[Snapshots]',
        'count': 'int'
    }

    attribute_map = {
        'snapshots': 'snapshots',
        'count': 'count'
    }

    def __init__(self, snapshots=None, count=None):
        r"""ListSnapshotsResponse

        The model defined in huaweicloud sdk

        :param snapshots: **参数解释**： 快照对象列表。 **取值范围**： 不涉及。
        :type snapshots: list[:class:`huaweicloudsdkdws.v2.Snapshots`]
        :param count: **参数解释**： 列表总数。 **取值范围**： 不涉及。
        :type count: int
        """
        
        super(ListSnapshotsResponse, self).__init__()

        self._snapshots = None
        self._count = None
        self.discriminator = None

        if snapshots is not None:
            self.snapshots = snapshots
        if count is not None:
            self.count = count

    @property
    def snapshots(self):
        r"""Gets the snapshots of this ListSnapshotsResponse.

        **参数解释**： 快照对象列表。 **取值范围**： 不涉及。

        :return: The snapshots of this ListSnapshotsResponse.
        :rtype: list[:class:`huaweicloudsdkdws.v2.Snapshots`]
        """
        return self._snapshots

    @snapshots.setter
    def snapshots(self, snapshots):
        r"""Sets the snapshots of this ListSnapshotsResponse.

        **参数解释**： 快照对象列表。 **取值范围**： 不涉及。

        :param snapshots: The snapshots of this ListSnapshotsResponse.
        :type snapshots: list[:class:`huaweicloudsdkdws.v2.Snapshots`]
        """
        self._snapshots = snapshots

    @property
    def count(self):
        r"""Gets the count of this ListSnapshotsResponse.

        **参数解释**： 列表总数。 **取值范围**： 不涉及。

        :return: The count of this ListSnapshotsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListSnapshotsResponse.

        **参数解释**： 列表总数。 **取值范围**： 不涉及。

        :param count: The count of this ListSnapshotsResponse.
        :type count: int
        """
        self._count = count

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
