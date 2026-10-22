# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSnapshotChainsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'marker': 'str',
        'limit': 'int',
        'id': 'str',
        'volume_id': 'str',
        'category': 'str'
    }

    attribute_map = {
        'marker': 'marker',
        'limit': 'limit',
        'id': 'id',
        'volume_id': 'volume_id',
        'category': 'category'
    }

    def __init__(self, marker=None, limit=None, id=None, volume_id=None, category=None):
        r"""ListSnapshotChainsRequest

        The model defined in huaweicloud sdk

        :param marker: **参数解释** 分页查询的起始资源ID，取值为上一页最后一条查询记录的资源ID。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。
        :type marker: str
        :param limit: **参数解释** 返回结果个数限制。 **约束限制** 不涉及。 **取值范围** 最小值1，最大值1000，默认为1000。返回的结果中记录数不超过limit值。 **默认取值** 不涉及。
        :type limit: int
        :param id: **参数解释** 快照链ID。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。
        :type id: str
        :param volume_id: **参数解释** 快照链所属的云硬盘ID。 可通过[查询所有云硬盘详情](evs_04_2006.xml)获取云硬盘ID。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。
        :type volume_id: str
        :param category: **参数解释** 快照链的类型。 **约束限制** 不涉及。 **取值范围** 当前快照链支持\&quot;standard\&quot;、\&quot;backup\&quot;和\&quot;server_backup\&quot;三种类型。 **默认取值** 不涉及。
        :type category: str
        """
        
        

        self._marker = None
        self._limit = None
        self._id = None
        self._volume_id = None
        self._category = None
        self.discriminator = None

        if marker is not None:
            self.marker = marker
        if limit is not None:
            self.limit = limit
        if id is not None:
            self.id = id
        if volume_id is not None:
            self.volume_id = volume_id
        if category is not None:
            self.category = category

    @property
    def marker(self):
        r"""Gets the marker of this ListSnapshotChainsRequest.

        **参数解释** 分页查询的起始资源ID，取值为上一页最后一条查询记录的资源ID。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :return: The marker of this ListSnapshotChainsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListSnapshotChainsRequest.

        **参数解释** 分页查询的起始资源ID，取值为上一页最后一条查询记录的资源ID。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :param marker: The marker of this ListSnapshotChainsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def limit(self):
        r"""Gets the limit of this ListSnapshotChainsRequest.

        **参数解释** 返回结果个数限制。 **约束限制** 不涉及。 **取值范围** 最小值1，最大值1000，默认为1000。返回的结果中记录数不超过limit值。 **默认取值** 不涉及。

        :return: The limit of this ListSnapshotChainsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListSnapshotChainsRequest.

        **参数解释** 返回结果个数限制。 **约束限制** 不涉及。 **取值范围** 最小值1，最大值1000，默认为1000。返回的结果中记录数不超过limit值。 **默认取值** 不涉及。

        :param limit: The limit of this ListSnapshotChainsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def id(self):
        r"""Gets the id of this ListSnapshotChainsRequest.

        **参数解释** 快照链ID。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :return: The id of this ListSnapshotChainsRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListSnapshotChainsRequest.

        **参数解释** 快照链ID。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :param id: The id of this ListSnapshotChainsRequest.
        :type id: str
        """
        self._id = id

    @property
    def volume_id(self):
        r"""Gets the volume_id of this ListSnapshotChainsRequest.

        **参数解释** 快照链所属的云硬盘ID。 可通过[查询所有云硬盘详情](evs_04_2006.xml)获取云硬盘ID。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :return: The volume_id of this ListSnapshotChainsRequest.
        :rtype: str
        """
        return self._volume_id

    @volume_id.setter
    def volume_id(self, volume_id):
        r"""Sets the volume_id of this ListSnapshotChainsRequest.

        **参数解释** 快照链所属的云硬盘ID。 可通过[查询所有云硬盘详情](evs_04_2006.xml)获取云硬盘ID。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :param volume_id: The volume_id of this ListSnapshotChainsRequest.
        :type volume_id: str
        """
        self._volume_id = volume_id

    @property
    def category(self):
        r"""Gets the category of this ListSnapshotChainsRequest.

        **参数解释** 快照链的类型。 **约束限制** 不涉及。 **取值范围** 当前快照链支持\"standard\"、\"backup\"和\"server_backup\"三种类型。 **默认取值** 不涉及。

        :return: The category of this ListSnapshotChainsRequest.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this ListSnapshotChainsRequest.

        **参数解释** 快照链的类型。 **约束限制** 不涉及。 **取值范围** 当前快照链支持\"standard\"、\"backup\"和\"server_backup\"三种类型。 **默认取值** 不涉及。

        :param category: The category of this ListSnapshotChainsRequest.
        :type category: str
        """
        self._category = category

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
        if not isinstance(other, ListSnapshotChainsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
