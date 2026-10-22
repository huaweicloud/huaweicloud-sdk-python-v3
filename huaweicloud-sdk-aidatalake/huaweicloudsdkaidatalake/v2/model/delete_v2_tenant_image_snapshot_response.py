# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteV2TenantImageSnapshotResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'image_snapshot_id': 'str'
    }

    attribute_map = {
        'image_snapshot_id': 'image_snapshot_id'
    }

    def __init__(self, image_snapshot_id=None):
        r"""DeleteV2TenantImageSnapshotResponse

        The model defined in huaweicloud sdk

        :param image_snapshot_id: **参数解释**：被删除的镜像快照ID。 **取值范围**：长度为32~36的英文字符、数字和中划线的组合。 
        :type image_snapshot_id: str
        """
        
        super().__init__()

        self._image_snapshot_id = None
        self.discriminator = None

        if image_snapshot_id is not None:
            self.image_snapshot_id = image_snapshot_id

    @property
    def image_snapshot_id(self):
        r"""Gets the image_snapshot_id of this DeleteV2TenantImageSnapshotResponse.

        **参数解释**：被删除的镜像快照ID。 **取值范围**：长度为32~36的英文字符、数字和中划线的组合。 

        :return: The image_snapshot_id of this DeleteV2TenantImageSnapshotResponse.
        :rtype: str
        """
        return self._image_snapshot_id

    @image_snapshot_id.setter
    def image_snapshot_id(self, image_snapshot_id):
        r"""Sets the image_snapshot_id of this DeleteV2TenantImageSnapshotResponse.

        **参数解释**：被删除的镜像快照ID。 **取值范围**：长度为32~36的英文字符、数字和中划线的组合。 

        :param image_snapshot_id: The image_snapshot_id of this DeleteV2TenantImageSnapshotResponse.
        :type image_snapshot_id: str
        """
        self._image_snapshot_id = image_snapshot_id

    def to_dict(self):
        import warnings
        warnings.warn("DeleteV2TenantImageSnapshotResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, DeleteV2TenantImageSnapshotResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
