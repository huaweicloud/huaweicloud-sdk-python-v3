# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListV2TenantImageVersionsResponse(SdkResponse):

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
        'image_versions': 'list[V2ImageVersionInfo]'
    }

    attribute_map = {
        'total': 'total',
        'image_versions': 'image_versions'
    }

    def __init__(self, total=None, image_versions=None):
        r"""ListV2TenantImageVersionsResponse

        The model defined in huaweicloud sdk

        :param total: **参数解释**：自定义镜像版本总记录数。 **取值范围**：最小值为0，最大值为100000。 
        :type total: int
        :param image_versions: **参数解释**：镜像版本列表，每个元素为一个V2ImageVersionInfo对象，包含镜像版本ID、镜像版本、镜像分类、镜像架构、状态等信息。 
        :type image_versions: list[:class:`huaweicloudsdkaidatalake.v2.V2ImageVersionInfo`]
        """
        
        super().__init__()

        self._total = None
        self._image_versions = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if image_versions is not None:
            self.image_versions = image_versions

    @property
    def total(self):
        r"""Gets the total of this ListV2TenantImageVersionsResponse.

        **参数解释**：自定义镜像版本总记录数。 **取值范围**：最小值为0，最大值为100000。 

        :return: The total of this ListV2TenantImageVersionsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListV2TenantImageVersionsResponse.

        **参数解释**：自定义镜像版本总记录数。 **取值范围**：最小值为0，最大值为100000。 

        :param total: The total of this ListV2TenantImageVersionsResponse.
        :type total: int
        """
        self._total = total

    @property
    def image_versions(self):
        r"""Gets the image_versions of this ListV2TenantImageVersionsResponse.

        **参数解释**：镜像版本列表，每个元素为一个V2ImageVersionInfo对象，包含镜像版本ID、镜像版本、镜像分类、镜像架构、状态等信息。 

        :return: The image_versions of this ListV2TenantImageVersionsResponse.
        :rtype: list[:class:`huaweicloudsdkaidatalake.v2.V2ImageVersionInfo`]
        """
        return self._image_versions

    @image_versions.setter
    def image_versions(self, image_versions):
        r"""Sets the image_versions of this ListV2TenantImageVersionsResponse.

        **参数解释**：镜像版本列表，每个元素为一个V2ImageVersionInfo对象，包含镜像版本ID、镜像版本、镜像分类、镜像架构、状态等信息。 

        :param image_versions: The image_versions of this ListV2TenantImageVersionsResponse.
        :type image_versions: list[:class:`huaweicloudsdkaidatalake.v2.V2ImageVersionInfo`]
        """
        self._image_versions = image_versions

    def to_dict(self):
        import warnings
        warnings.warn("ListV2TenantImageVersionsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListV2TenantImageVersionsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
