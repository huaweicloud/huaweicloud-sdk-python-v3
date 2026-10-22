# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListV2TenantImageSnapshotsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'ImageSnapshotStatus',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'status': 'status',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, status=None, offset=None, limit=None):
        r"""ListV2TenantImageSnapshotsRequest

        The model defined in huaweicloud sdk

        :param status: **参数解释**：镜像快照状态。 **约束限制**：不涉及。 **取值范围**：   - Creating：创建中。   - Available：可用。   - Unavailable：不可用。 **默认取值**：不涉及。 
        :type status: :class:`huaweicloudsdkaidatalake.v2.ImageSnapshotStatus`
        :param offset: **参数解释**：偏移量，表示从此偏移量开始查询。 **约束限制**：不涉及。 **取值范围**：0~1000000000。 **默认取值**：0。
        :type offset: int
        :param limit: **参数解释**：分页大小。 **约束限制**：不涉及。 **取值范围**：1~1000。 **默认取值**：100。 
        :type limit: int
        """
        
        

        self._status = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def status(self):
        r"""Gets the status of this ListV2TenantImageSnapshotsRequest.

        **参数解释**：镜像快照状态。 **约束限制**：不涉及。 **取值范围**：   - Creating：创建中。   - Available：可用。   - Unavailable：不可用。 **默认取值**：不涉及。 

        :return: The status of this ListV2TenantImageSnapshotsRequest.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.ImageSnapshotStatus`
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListV2TenantImageSnapshotsRequest.

        **参数解释**：镜像快照状态。 **约束限制**：不涉及。 **取值范围**：   - Creating：创建中。   - Available：可用。   - Unavailable：不可用。 **默认取值**：不涉及。 

        :param status: The status of this ListV2TenantImageSnapshotsRequest.
        :type status: :class:`huaweicloudsdkaidatalake.v2.ImageSnapshotStatus`
        """
        self._status = status

    @property
    def offset(self):
        r"""Gets the offset of this ListV2TenantImageSnapshotsRequest.

        **参数解释**：偏移量，表示从此偏移量开始查询。 **约束限制**：不涉及。 **取值范围**：0~1000000000。 **默认取值**：0。

        :return: The offset of this ListV2TenantImageSnapshotsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListV2TenantImageSnapshotsRequest.

        **参数解释**：偏移量，表示从此偏移量开始查询。 **约束限制**：不涉及。 **取值范围**：0~1000000000。 **默认取值**：0。

        :param offset: The offset of this ListV2TenantImageSnapshotsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListV2TenantImageSnapshotsRequest.

        **参数解释**：分页大小。 **约束限制**：不涉及。 **取值范围**：1~1000。 **默认取值**：100。 

        :return: The limit of this ListV2TenantImageSnapshotsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListV2TenantImageSnapshotsRequest.

        **参数解释**：分页大小。 **约束限制**：不涉及。 **取值范围**：1~1000。 **默认取值**：100。 

        :param limit: The limit of this ListV2TenantImageSnapshotsRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListV2TenantImageSnapshotsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
