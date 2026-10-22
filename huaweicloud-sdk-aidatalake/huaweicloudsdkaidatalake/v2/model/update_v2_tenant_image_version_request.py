# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateV2TenantImageVersionRequest:

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
        'body': 'UpdateV2ImageVersionInput'
    }

    attribute_map = {
        'image_id': 'image_id',
        'version_id': 'version_id',
        'body': 'body'
    }

    def __init__(self, image_id=None, version_id=None, body=None):
        r"""UpdateV2TenantImageVersionRequest

        The model defined in huaweicloud sdk

        :param image_id: **参数解释**：镜像ID。可通过[查询自定义镜像列表]获取镜像ID(ListV2TenantImages.xml)。 **约束限制**：不涉及。 **取值范围**：长度为32~36的英文字符、数字和中划线的组合。 **默认取值**：不涉及。
        :type image_id: str
        :param version_id: **参数解释**：镜像版本ID。可通过[查询自定义镜像版本列表](ListV2TenantImageVersions.xml)获取镜像版本ID。 **约束限制**：不涉及。 **取值范围**：长度为32~36的英文字符、数字和中划线的组合。 **默认取值**：不涉及。
        :type version_id: str
        :param body: Body of the UpdateV2TenantImageVersionRequest
        :type body: :class:`huaweicloudsdkaidatalake.v2.UpdateV2ImageVersionInput`
        """
        
        

        self._image_id = None
        self._version_id = None
        self._body = None
        self.discriminator = None

        self.image_id = image_id
        self.version_id = version_id
        if body is not None:
            self.body = body

    @property
    def image_id(self):
        r"""Gets the image_id of this UpdateV2TenantImageVersionRequest.

        **参数解释**：镜像ID。可通过[查询自定义镜像列表]获取镜像ID(ListV2TenantImages.xml)。 **约束限制**：不涉及。 **取值范围**：长度为32~36的英文字符、数字和中划线的组合。 **默认取值**：不涉及。

        :return: The image_id of this UpdateV2TenantImageVersionRequest.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this UpdateV2TenantImageVersionRequest.

        **参数解释**：镜像ID。可通过[查询自定义镜像列表]获取镜像ID(ListV2TenantImages.xml)。 **约束限制**：不涉及。 **取值范围**：长度为32~36的英文字符、数字和中划线的组合。 **默认取值**：不涉及。

        :param image_id: The image_id of this UpdateV2TenantImageVersionRequest.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def version_id(self):
        r"""Gets the version_id of this UpdateV2TenantImageVersionRequest.

        **参数解释**：镜像版本ID。可通过[查询自定义镜像版本列表](ListV2TenantImageVersions.xml)获取镜像版本ID。 **约束限制**：不涉及。 **取值范围**：长度为32~36的英文字符、数字和中划线的组合。 **默认取值**：不涉及。

        :return: The version_id of this UpdateV2TenantImageVersionRequest.
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        r"""Sets the version_id of this UpdateV2TenantImageVersionRequest.

        **参数解释**：镜像版本ID。可通过[查询自定义镜像版本列表](ListV2TenantImageVersions.xml)获取镜像版本ID。 **约束限制**：不涉及。 **取值范围**：长度为32~36的英文字符、数字和中划线的组合。 **默认取值**：不涉及。

        :param version_id: The version_id of this UpdateV2TenantImageVersionRequest.
        :type version_id: str
        """
        self._version_id = version_id

    @property
    def body(self):
        r"""Gets the body of this UpdateV2TenantImageVersionRequest.

        :return: The body of this UpdateV2TenantImageVersionRequest.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.UpdateV2ImageVersionInput`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateV2TenantImageVersionRequest.

        :param body: The body of this UpdateV2TenantImageVersionRequest.
        :type body: :class:`huaweicloudsdkaidatalake.v2.UpdateV2ImageVersionInput`
        """
        self._body = body

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
        if not isinstance(other, UpdateV2TenantImageVersionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
