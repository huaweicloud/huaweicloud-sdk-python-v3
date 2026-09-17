# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListOperationalTaskRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_id': 'str',
        'time_zone': 'str',
        'type': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'time_zone': 'time_zone',
        'type': 'type',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, cluster_id=None, time_zone=None, type=None, limit=None, offset=None):
        r"""ListOperationalTaskRequest

        The model defined in huaweicloud sdk

        :param cluster_id: **参数解释**： 集群ID。获取方法请参见[获取集群ID](dws_02_00068.xml)。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type cluster_id: str
        :param time_zone: **参数解释**： 时区偏移量，默认为UTC时间（0偏移），即+0000。 **约束限制**： 不涉及。 **取值范围**： -2359~+2359 **默认取值**： +0000
        :type time_zone: str
        :param type: **参数解释**： 任务类型。 **约束限制**： 仅支持两种值。 **取值范围**： Date：单次型任务； Window：周期型任务； **默认取值**： 无。
        :type type: str
        :param limit: **参数解释**： 分页查询，每页大小。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 100
        :type limit: int
        :param offset: **参数解释**： 分页偏移量，从0开始，页数减1。 **约束限制**： 不涉及。 **取值范围**： 大于等于0 **默认取值**： 0
        :type offset: int
        """
        
        

        self._cluster_id = None
        self._time_zone = None
        self._type = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        self.cluster_id = cluster_id
        if time_zone is not None:
            self.time_zone = time_zone
        if type is not None:
            self.type = type
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this ListOperationalTaskRequest.

        **参数解释**： 集群ID。获取方法请参见[获取集群ID](dws_02_00068.xml)。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The cluster_id of this ListOperationalTaskRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this ListOperationalTaskRequest.

        **参数解释**： 集群ID。获取方法请参见[获取集群ID](dws_02_00068.xml)。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param cluster_id: The cluster_id of this ListOperationalTaskRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def time_zone(self):
        r"""Gets the time_zone of this ListOperationalTaskRequest.

        **参数解释**： 时区偏移量，默认为UTC时间（0偏移），即+0000。 **约束限制**： 不涉及。 **取值范围**： -2359~+2359 **默认取值**： +0000

        :return: The time_zone of this ListOperationalTaskRequest.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        r"""Sets the time_zone of this ListOperationalTaskRequest.

        **参数解释**： 时区偏移量，默认为UTC时间（0偏移），即+0000。 **约束限制**： 不涉及。 **取值范围**： -2359~+2359 **默认取值**： +0000

        :param time_zone: The time_zone of this ListOperationalTaskRequest.
        :type time_zone: str
        """
        self._time_zone = time_zone

    @property
    def type(self):
        r"""Gets the type of this ListOperationalTaskRequest.

        **参数解释**： 任务类型。 **约束限制**： 仅支持两种值。 **取值范围**： Date：单次型任务； Window：周期型任务； **默认取值**： 无。

        :return: The type of this ListOperationalTaskRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListOperationalTaskRequest.

        **参数解释**： 任务类型。 **约束限制**： 仅支持两种值。 **取值范围**： Date：单次型任务； Window：周期型任务； **默认取值**： 无。

        :param type: The type of this ListOperationalTaskRequest.
        :type type: str
        """
        self._type = type

    @property
    def limit(self):
        r"""Gets the limit of this ListOperationalTaskRequest.

        **参数解释**： 分页查询，每页大小。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 100

        :return: The limit of this ListOperationalTaskRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListOperationalTaskRequest.

        **参数解释**： 分页查询，每页大小。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 100

        :param limit: The limit of this ListOperationalTaskRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListOperationalTaskRequest.

        **参数解释**： 分页偏移量，从0开始，页数减1。 **约束限制**： 不涉及。 **取值范围**： 大于等于0 **默认取值**： 0

        :return: The offset of this ListOperationalTaskRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListOperationalTaskRequest.

        **参数解释**： 分页偏移量，从0开始，页数减1。 **约束限制**： 不涉及。 **取值范围**： 大于等于0 **默认取值**： 0

        :param offset: The offset of this ListOperationalTaskRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ListOperationalTaskRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
