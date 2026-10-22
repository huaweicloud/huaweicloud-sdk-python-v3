# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListV2TenantImageSnapshotsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'image_snapshots': 'list[V2ImageSnapshotInfo]'
    }

    attribute_map = {
        'total': 'total',
        'image_snapshots': 'image_snapshots'
    }

    def __init__(self, total=None, image_snapshots=None):
        r"""ListV2TenantImageSnapshotsResponse

        The model defined in huaweicloud sdk

        :param total: **参数解释**：快照总数。 **约束限制**：不涉及。 **取值范围**：0~10000。 **默认取值**：不涉及。 
        :type total: int
        :param image_snapshots: **参数解释**：镜像快照列表。 
        :type image_snapshots: list[:class:`huaweicloudsdkaidatalake.v2.V2ImageSnapshotInfo`]
        """
        
        super().__init__()

        self._total = None
        self._image_snapshots = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if image_snapshots is not None:
            self.image_snapshots = image_snapshots

    @property
    def total(self):
        r"""Gets the total of this ListV2TenantImageSnapshotsResponse.

        **参数解释**：快照总数。 **约束限制**：不涉及。 **取值范围**：0~10000。 **默认取值**：不涉及。 

        :return: The total of this ListV2TenantImageSnapshotsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListV2TenantImageSnapshotsResponse.

        **参数解释**：快照总数。 **约束限制**：不涉及。 **取值范围**：0~10000。 **默认取值**：不涉及。 

        :param total: The total of this ListV2TenantImageSnapshotsResponse.
        :type total: int
        """
        self._total = total

    @property
    def image_snapshots(self):
        r"""Gets the image_snapshots of this ListV2TenantImageSnapshotsResponse.

        **参数解释**：镜像快照列表。 

        :return: The image_snapshots of this ListV2TenantImageSnapshotsResponse.
        :rtype: list[:class:`huaweicloudsdkaidatalake.v2.V2ImageSnapshotInfo`]
        """
        return self._image_snapshots

    @image_snapshots.setter
    def image_snapshots(self, image_snapshots):
        r"""Sets the image_snapshots of this ListV2TenantImageSnapshotsResponse.

        **参数解释**：镜像快照列表。 

        :param image_snapshots: The image_snapshots of this ListV2TenantImageSnapshotsResponse.
        :type image_snapshots: list[:class:`huaweicloudsdkaidatalake.v2.V2ImageSnapshotInfo`]
        """
        self._image_snapshots = image_snapshots

    def to_dict(self):
        import warnings
        warnings.warn("ListV2TenantImageSnapshotsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListV2TenantImageSnapshotsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
