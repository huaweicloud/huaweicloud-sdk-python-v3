# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSnapshotGroupRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'snapshot_group_id': 'str'
    }

    attribute_map = {
        'snapshot_group_id': 'snapshot_group_id'
    }

    def __init__(self, snapshot_group_id=None):
        r"""ShowSnapshotGroupRequest

        The model defined in huaweicloud sdk

        :param snapshot_group_id: **参数解释** 快照一致性组ID。 可通过[查询快照一致性组列表](ListSnapshotGroup.xml)接口获取快照一致性组ID。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。
        :type snapshot_group_id: str
        """
        
        

        self._snapshot_group_id = None
        self.discriminator = None

        self.snapshot_group_id = snapshot_group_id

    @property
    def snapshot_group_id(self):
        r"""Gets the snapshot_group_id of this ShowSnapshotGroupRequest.

        **参数解释** 快照一致性组ID。 可通过[查询快照一致性组列表](ListSnapshotGroup.xml)接口获取快照一致性组ID。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :return: The snapshot_group_id of this ShowSnapshotGroupRequest.
        :rtype: str
        """
        return self._snapshot_group_id

    @snapshot_group_id.setter
    def snapshot_group_id(self, snapshot_group_id):
        r"""Sets the snapshot_group_id of this ShowSnapshotGroupRequest.

        **参数解释** 快照一致性组ID。 可通过[查询快照一致性组列表](ListSnapshotGroup.xml)接口获取快照一致性组ID。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :param snapshot_group_id: The snapshot_group_id of this ShowSnapshotGroupRequest.
        :type snapshot_group_id: str
        """
        self._snapshot_group_id = snapshot_group_id

    def to_dict(self):
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
        if not isinstance(other, ShowSnapshotGroupRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
