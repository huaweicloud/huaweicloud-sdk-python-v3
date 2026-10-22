# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSnapshotChainsResponseBodySnapshotChains:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'availability_zone': 'str',
        'snapshot_count': 'int',
        'capacity': 'float',
        'project_id': 'str',
        'volume_id': 'str',
        'category': 'str',
        'created_at': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'id': 'id',
        'availability_zone': 'availability_zone',
        'snapshot_count': 'snapshot_count',
        'capacity': 'capacity',
        'project_id': 'project_id',
        'volume_id': 'volume_id',
        'category': 'category',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, availability_zone=None, snapshot_count=None, capacity=None, project_id=None, volume_id=None, category=None, created_at=None, updated_at=None):
        r"""ListSnapshotChainsResponseBodySnapshotChains

        The model defined in huaweicloud sdk

        :param id: **参数解释** 快照链ID。 **取值范围** 不涉及。
        :type id: str
        :param availability_zone: **参数解释** 快照链所属云硬盘的可用区。 **取值范围** 不涉及。
        :type availability_zone: str
        :param snapshot_count: **参数解释** 快照链上的快照个数。 **取值范围** 大于等于0。
        :type snapshot_count: int
        :param capacity: **参数解释** 快照链的大小。 **取值范围** 大于等于0。
        :type capacity: float
        :param project_id: **参数解释** 项目ID。 **取值范围** 不涉及。
        :type project_id: str
        :param volume_id: **参数解释** 快照链所属的云硬盘ID。 **取值范围** 不涉及。
        :type volume_id: str
        :param category: **参数解释** 快照链的类型。 **取值范围** 当前快照链支持\&quot;standard\&quot;、\&quot;standard_copy\&quot;两种类型。
        :type category: str
        :param created_at: **参数解释** 创建时间。 **取值范围** 不涉及。
        :type created_at: str
        :param updated_at: **参数解释** 更新时间。 **取值范围** 不涉及。
        :type updated_at: str
        """
        
        

        self._id = None
        self._availability_zone = None
        self._snapshot_count = None
        self._capacity = None
        self._project_id = None
        self._volume_id = None
        self._category = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if availability_zone is not None:
            self.availability_zone = availability_zone
        if snapshot_count is not None:
            self.snapshot_count = snapshot_count
        if capacity is not None:
            self.capacity = capacity
        if project_id is not None:
            self.project_id = project_id
        if volume_id is not None:
            self.volume_id = volume_id
        if category is not None:
            self.category = category
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def id(self):
        r"""Gets the id of this ListSnapshotChainsResponseBodySnapshotChains.

        **参数解释** 快照链ID。 **取值范围** 不涉及。

        :return: The id of this ListSnapshotChainsResponseBodySnapshotChains.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListSnapshotChainsResponseBodySnapshotChains.

        **参数解释** 快照链ID。 **取值范围** 不涉及。

        :param id: The id of this ListSnapshotChainsResponseBodySnapshotChains.
        :type id: str
        """
        self._id = id

    @property
    def availability_zone(self):
        r"""Gets the availability_zone of this ListSnapshotChainsResponseBodySnapshotChains.

        **参数解释** 快照链所属云硬盘的可用区。 **取值范围** 不涉及。

        :return: The availability_zone of this ListSnapshotChainsResponseBodySnapshotChains.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        r"""Sets the availability_zone of this ListSnapshotChainsResponseBodySnapshotChains.

        **参数解释** 快照链所属云硬盘的可用区。 **取值范围** 不涉及。

        :param availability_zone: The availability_zone of this ListSnapshotChainsResponseBodySnapshotChains.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def snapshot_count(self):
        r"""Gets the snapshot_count of this ListSnapshotChainsResponseBodySnapshotChains.

        **参数解释** 快照链上的快照个数。 **取值范围** 大于等于0。

        :return: The snapshot_count of this ListSnapshotChainsResponseBodySnapshotChains.
        :rtype: int
        """
        return self._snapshot_count

    @snapshot_count.setter
    def snapshot_count(self, snapshot_count):
        r"""Sets the snapshot_count of this ListSnapshotChainsResponseBodySnapshotChains.

        **参数解释** 快照链上的快照个数。 **取值范围** 大于等于0。

        :param snapshot_count: The snapshot_count of this ListSnapshotChainsResponseBodySnapshotChains.
        :type snapshot_count: int
        """
        self._snapshot_count = snapshot_count

    @property
    def capacity(self):
        r"""Gets the capacity of this ListSnapshotChainsResponseBodySnapshotChains.

        **参数解释** 快照链的大小。 **取值范围** 大于等于0。

        :return: The capacity of this ListSnapshotChainsResponseBodySnapshotChains.
        :rtype: float
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        r"""Sets the capacity of this ListSnapshotChainsResponseBodySnapshotChains.

        **参数解释** 快照链的大小。 **取值范围** 大于等于0。

        :param capacity: The capacity of this ListSnapshotChainsResponseBodySnapshotChains.
        :type capacity: float
        """
        self._capacity = capacity

    @property
    def project_id(self):
        r"""Gets the project_id of this ListSnapshotChainsResponseBodySnapshotChains.

        **参数解释** 项目ID。 **取值范围** 不涉及。

        :return: The project_id of this ListSnapshotChainsResponseBodySnapshotChains.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ListSnapshotChainsResponseBodySnapshotChains.

        **参数解释** 项目ID。 **取值范围** 不涉及。

        :param project_id: The project_id of this ListSnapshotChainsResponseBodySnapshotChains.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def volume_id(self):
        r"""Gets the volume_id of this ListSnapshotChainsResponseBodySnapshotChains.

        **参数解释** 快照链所属的云硬盘ID。 **取值范围** 不涉及。

        :return: The volume_id of this ListSnapshotChainsResponseBodySnapshotChains.
        :rtype: str
        """
        return self._volume_id

    @volume_id.setter
    def volume_id(self, volume_id):
        r"""Sets the volume_id of this ListSnapshotChainsResponseBodySnapshotChains.

        **参数解释** 快照链所属的云硬盘ID。 **取值范围** 不涉及。

        :param volume_id: The volume_id of this ListSnapshotChainsResponseBodySnapshotChains.
        :type volume_id: str
        """
        self._volume_id = volume_id

    @property
    def category(self):
        r"""Gets the category of this ListSnapshotChainsResponseBodySnapshotChains.

        **参数解释** 快照链的类型。 **取值范围** 当前快照链支持\"standard\"、\"standard_copy\"两种类型。

        :return: The category of this ListSnapshotChainsResponseBodySnapshotChains.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this ListSnapshotChainsResponseBodySnapshotChains.

        **参数解释** 快照链的类型。 **取值范围** 当前快照链支持\"standard\"、\"standard_copy\"两种类型。

        :param category: The category of this ListSnapshotChainsResponseBodySnapshotChains.
        :type category: str
        """
        self._category = category

    @property
    def created_at(self):
        r"""Gets the created_at of this ListSnapshotChainsResponseBodySnapshotChains.

        **参数解释** 创建时间。 **取值范围** 不涉及。

        :return: The created_at of this ListSnapshotChainsResponseBodySnapshotChains.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this ListSnapshotChainsResponseBodySnapshotChains.

        **参数解释** 创建时间。 **取值范围** 不涉及。

        :param created_at: The created_at of this ListSnapshotChainsResponseBodySnapshotChains.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this ListSnapshotChainsResponseBodySnapshotChains.

        **参数解释** 更新时间。 **取值范围** 不涉及。

        :return: The updated_at of this ListSnapshotChainsResponseBodySnapshotChains.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this ListSnapshotChainsResponseBodySnapshotChains.

        **参数解释** 更新时间。 **取值范围** 不涉及。

        :param updated_at: The updated_at of this ListSnapshotChainsResponseBodySnapshotChains.
        :type updated_at: str
        """
        self._updated_at = updated_at

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
        if not isinstance(other, ListSnapshotChainsResponseBodySnapshotChains):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
