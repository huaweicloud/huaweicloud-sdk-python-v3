# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteV2TenantImageSnapshotRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'image_id': 'str',
        'version_id': 'str',
        'image_snapshot_id': 'str'
    }

    attribute_map = {
        'image_id': 'image_id',
        'version_id': 'version_id',
        'image_snapshot_id': 'image_snapshot_id'
    }

    def __init__(self, image_id=None, version_id=None, image_snapshot_id=None):
        r"""DeleteV2TenantImageSnapshotRequest

        The model defined in huaweicloud sdk

        :param image_id: **参数解释**：镜像ID。可通过[查询自定义镜像列表]获取镜像ID(ListV2TenantImages.xml)。 **约束限制**：不涉及。 **取值范围**：长度为32~36的英文字符、数字和中划线的组合。 **默认取值**：不涉及。
        :type image_id: str
        :param version_id: **参数解释**：镜像版本ID。可通过[查询自定义镜像版本列表](ListV2TenantImageVersions.xml)获取镜像版本ID。 **约束限制**：不涉及。 **取值范围**：长度为32~36的英文字符、数字和中划线的组合。 **默认取值**：不涉及。
        :type version_id: str
        :param image_snapshot_id: **参数解释**：镜像快照ID。可通过[查询镜像快照列表]获取镜像ID(ListV2TenantImageSnapshots.xml)。 **约束限制**：不涉及。 **取值范围**：长度为32~36的英文字符、数字和中划线的组合。 **默认取值**：不涉及。 
        :type image_snapshot_id: str
        """
        
        

        self._image_id = None
        self._version_id = None
        self._image_snapshot_id = None
        self.discriminator = None

        self.image_id = image_id
        self.version_id = version_id
        self.image_snapshot_id = image_snapshot_id

    @property
    def image_id(self):
        r"""Gets the image_id of this DeleteV2TenantImageSnapshotRequest.

        **参数解释**：镜像ID。可通过[查询自定义镜像列表]获取镜像ID(ListV2TenantImages.xml)。 **约束限制**：不涉及。 **取值范围**：长度为32~36的英文字符、数字和中划线的组合。 **默认取值**：不涉及。

        :return: The image_id of this DeleteV2TenantImageSnapshotRequest.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this DeleteV2TenantImageSnapshotRequest.

        **参数解释**：镜像ID。可通过[查询自定义镜像列表]获取镜像ID(ListV2TenantImages.xml)。 **约束限制**：不涉及。 **取值范围**：长度为32~36的英文字符、数字和中划线的组合。 **默认取值**：不涉及。

        :param image_id: The image_id of this DeleteV2TenantImageSnapshotRequest.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def version_id(self):
        r"""Gets the version_id of this DeleteV2TenantImageSnapshotRequest.

        **参数解释**：镜像版本ID。可通过[查询自定义镜像版本列表](ListV2TenantImageVersions.xml)获取镜像版本ID。 **约束限制**：不涉及。 **取值范围**：长度为32~36的英文字符、数字和中划线的组合。 **默认取值**：不涉及。

        :return: The version_id of this DeleteV2TenantImageSnapshotRequest.
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        r"""Sets the version_id of this DeleteV2TenantImageSnapshotRequest.

        **参数解释**：镜像版本ID。可通过[查询自定义镜像版本列表](ListV2TenantImageVersions.xml)获取镜像版本ID。 **约束限制**：不涉及。 **取值范围**：长度为32~36的英文字符、数字和中划线的组合。 **默认取值**：不涉及。

        :param version_id: The version_id of this DeleteV2TenantImageSnapshotRequest.
        :type version_id: str
        """
        self._version_id = version_id

    @property
    def image_snapshot_id(self):
        r"""Gets the image_snapshot_id of this DeleteV2TenantImageSnapshotRequest.

        **参数解释**：镜像快照ID。可通过[查询镜像快照列表]获取镜像ID(ListV2TenantImageSnapshots.xml)。 **约束限制**：不涉及。 **取值范围**：长度为32~36的英文字符、数字和中划线的组合。 **默认取值**：不涉及。 

        :return: The image_snapshot_id of this DeleteV2TenantImageSnapshotRequest.
        :rtype: str
        """
        return self._image_snapshot_id

    @image_snapshot_id.setter
    def image_snapshot_id(self, image_snapshot_id):
        r"""Sets the image_snapshot_id of this DeleteV2TenantImageSnapshotRequest.

        **参数解释**：镜像快照ID。可通过[查询镜像快照列表]获取镜像ID(ListV2TenantImageSnapshots.xml)。 **约束限制**：不涉及。 **取值范围**：长度为32~36的英文字符、数字和中划线的组合。 **默认取值**：不涉及。 

        :param image_snapshot_id: The image_snapshot_id of this DeleteV2TenantImageSnapshotRequest.
        :type image_snapshot_id: str
        """
        self._image_snapshot_id = image_snapshot_id

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
        if not isinstance(other, DeleteV2TenantImageSnapshotRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
