# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSnapshotGroupResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'snapshot_groups': 'list[SnapshotGroupDetail]'
    }

    attribute_map = {
        'snapshot_groups': 'snapshot_groups'
    }

    def __init__(self, snapshot_groups=None):
        r"""ListSnapshotGroupResponse

        The model defined in huaweicloud sdk

        :param snapshot_groups: **参数解释** 快照一致性组列表信息。 **取值范围** 不涉及。
        :type snapshot_groups: list[:class:`huaweicloudsdkevs.v2.SnapshotGroupDetail`]
        """
        
        super().__init__()

        self._snapshot_groups = None
        self.discriminator = None

        if snapshot_groups is not None:
            self.snapshot_groups = snapshot_groups

    @property
    def snapshot_groups(self):
        r"""Gets the snapshot_groups of this ListSnapshotGroupResponse.

        **参数解释** 快照一致性组列表信息。 **取值范围** 不涉及。

        :return: The snapshot_groups of this ListSnapshotGroupResponse.
        :rtype: list[:class:`huaweicloudsdkevs.v2.SnapshotGroupDetail`]
        """
        return self._snapshot_groups

    @snapshot_groups.setter
    def snapshot_groups(self, snapshot_groups):
        r"""Sets the snapshot_groups of this ListSnapshotGroupResponse.

        **参数解释** 快照一致性组列表信息。 **取值范围** 不涉及。

        :param snapshot_groups: The snapshot_groups of this ListSnapshotGroupResponse.
        :type snapshot_groups: list[:class:`huaweicloudsdkevs.v2.SnapshotGroupDetail`]
        """
        self._snapshot_groups = snapshot_groups

    def to_dict(self):
        import warnings
        warnings.warn("ListSnapshotGroupResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListSnapshotGroupResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
