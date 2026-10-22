# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CountSnapshotChainsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'volume_id': 'str',
        'availability_zone': 'str',
        'category': 'str',
        'id': 'str'
    }

    attribute_map = {
        'volume_id': 'volume_id',
        'availability_zone': 'availability_zone',
        'category': 'category',
        'id': 'id'
    }

    def __init__(self, volume_id=None, availability_zone=None, category=None, id=None):
        r"""CountSnapshotChainsRequest

        The model defined in huaweicloud sdk

        :param volume_id: **参数解释** 快照链所属的云硬盘ID。 可通过[查询所有云硬盘详情](evs_04_2006.xml)获取云硬盘ID。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。
        :type volume_id: str
        :param availability_zone: **参数解释** 快照链对应的云硬盘所在的可用区。  **约束限制** 不涉及。 **取值范围** 不涉及。         **默认取值** 不涉及。
        :type availability_zone: str
        :param category: **参数解释** 快照链的类型。 **约束限制** 不涉及。 **取值范围** 当前快照链支持\&quot;standard\&quot;、\&quot;standard_copy\&quot;两种类型。  **默认取值** 不涉及。
        :type category: str
        :param id: **参数解释** 快照链ID。 可通过[查询快照链列表](ListSnapshotChains.xml)接口获取快照链ID。 **约束限制** 不涉及。 **取值范围** 不涉及。  **默认取值** 不涉及。
        :type id: str
        """
        
        

        self._volume_id = None
        self._availability_zone = None
        self._category = None
        self._id = None
        self.discriminator = None

        if volume_id is not None:
            self.volume_id = volume_id
        if availability_zone is not None:
            self.availability_zone = availability_zone
        if category is not None:
            self.category = category
        if id is not None:
            self.id = id

    @property
    def volume_id(self):
        r"""Gets the volume_id of this CountSnapshotChainsRequest.

        **参数解释** 快照链所属的云硬盘ID。 可通过[查询所有云硬盘详情](evs_04_2006.xml)获取云硬盘ID。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :return: The volume_id of this CountSnapshotChainsRequest.
        :rtype: str
        """
        return self._volume_id

    @volume_id.setter
    def volume_id(self, volume_id):
        r"""Sets the volume_id of this CountSnapshotChainsRequest.

        **参数解释** 快照链所属的云硬盘ID。 可通过[查询所有云硬盘详情](evs_04_2006.xml)获取云硬盘ID。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :param volume_id: The volume_id of this CountSnapshotChainsRequest.
        :type volume_id: str
        """
        self._volume_id = volume_id

    @property
    def availability_zone(self):
        r"""Gets the availability_zone of this CountSnapshotChainsRequest.

        **参数解释** 快照链对应的云硬盘所在的可用区。  **约束限制** 不涉及。 **取值范围** 不涉及。         **默认取值** 不涉及。

        :return: The availability_zone of this CountSnapshotChainsRequest.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        r"""Sets the availability_zone of this CountSnapshotChainsRequest.

        **参数解释** 快照链对应的云硬盘所在的可用区。  **约束限制** 不涉及。 **取值范围** 不涉及。         **默认取值** 不涉及。

        :param availability_zone: The availability_zone of this CountSnapshotChainsRequest.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def category(self):
        r"""Gets the category of this CountSnapshotChainsRequest.

        **参数解释** 快照链的类型。 **约束限制** 不涉及。 **取值范围** 当前快照链支持\"standard\"、\"standard_copy\"两种类型。  **默认取值** 不涉及。

        :return: The category of this CountSnapshotChainsRequest.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this CountSnapshotChainsRequest.

        **参数解释** 快照链的类型。 **约束限制** 不涉及。 **取值范围** 当前快照链支持\"standard\"、\"standard_copy\"两种类型。  **默认取值** 不涉及。

        :param category: The category of this CountSnapshotChainsRequest.
        :type category: str
        """
        self._category = category

    @property
    def id(self):
        r"""Gets the id of this CountSnapshotChainsRequest.

        **参数解释** 快照链ID。 可通过[查询快照链列表](ListSnapshotChains.xml)接口获取快照链ID。 **约束限制** 不涉及。 **取值范围** 不涉及。  **默认取值** 不涉及。

        :return: The id of this CountSnapshotChainsRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CountSnapshotChainsRequest.

        **参数解释** 快照链ID。 可通过[查询快照链列表](ListSnapshotChains.xml)接口获取快照链ID。 **约束限制** 不涉及。 **取值范围** 不涉及。  **默认取值** 不涉及。

        :param id: The id of this CountSnapshotChainsRequest.
        :type id: str
        """
        self._id = id

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
        if not isinstance(other, CountSnapshotChainsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
