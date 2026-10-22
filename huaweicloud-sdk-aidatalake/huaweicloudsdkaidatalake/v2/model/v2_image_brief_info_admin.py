# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class V2ImageBriefInfoAdmin:

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
        'version_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'version_id': 'version_id'
    }

    def __init__(self, id=None, version_id=None):
        r"""V2ImageBriefInfoAdmin

        The model defined in huaweicloud sdk

        :param id: **参数解释**：镜像版本ID。可通过[查询自定义镜像版本列表](ListV2TenantImageVersions.xml)获取镜像版本ID。 **约束限制**：不涉及。 **取值范围**：长度为32~36的英文、数字、中划线的组合。 **默认取值**：不涉及。
        :type id: str
        :param version_id: **参数解释**：镜像版本ID。可通过[查询自定义镜像版本列表](ListV2TenantImageVersions.xml)获取镜像版本ID。 **约束限制**：不涉及。 **取值范围**：长度为32~36的英文、数字、中划线的组合。 **默认取值**：不涉及。
        :type version_id: str
        """
        
        

        self._id = None
        self._version_id = None
        self.discriminator = None

        self.id = id
        self.version_id = version_id

    @property
    def id(self):
        r"""Gets the id of this V2ImageBriefInfoAdmin.

        **参数解释**：镜像版本ID。可通过[查询自定义镜像版本列表](ListV2TenantImageVersions.xml)获取镜像版本ID。 **约束限制**：不涉及。 **取值范围**：长度为32~36的英文、数字、中划线的组合。 **默认取值**：不涉及。

        :return: The id of this V2ImageBriefInfoAdmin.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this V2ImageBriefInfoAdmin.

        **参数解释**：镜像版本ID。可通过[查询自定义镜像版本列表](ListV2TenantImageVersions.xml)获取镜像版本ID。 **约束限制**：不涉及。 **取值范围**：长度为32~36的英文、数字、中划线的组合。 **默认取值**：不涉及。

        :param id: The id of this V2ImageBriefInfoAdmin.
        :type id: str
        """
        self._id = id

    @property
    def version_id(self):
        r"""Gets the version_id of this V2ImageBriefInfoAdmin.

        **参数解释**：镜像版本ID。可通过[查询自定义镜像版本列表](ListV2TenantImageVersions.xml)获取镜像版本ID。 **约束限制**：不涉及。 **取值范围**：长度为32~36的英文、数字、中划线的组合。 **默认取值**：不涉及。

        :return: The version_id of this V2ImageBriefInfoAdmin.
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        r"""Sets the version_id of this V2ImageBriefInfoAdmin.

        **参数解释**：镜像版本ID。可通过[查询自定义镜像版本列表](ListV2TenantImageVersions.xml)获取镜像版本ID。 **约束限制**：不涉及。 **取值范围**：长度为32~36的英文、数字、中划线的组合。 **默认取值**：不涉及。

        :param version_id: The version_id of this V2ImageBriefInfoAdmin.
        :type version_id: str
        """
        self._version_id = version_id

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
        if not isinstance(other, V2ImageBriefInfoAdmin):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
