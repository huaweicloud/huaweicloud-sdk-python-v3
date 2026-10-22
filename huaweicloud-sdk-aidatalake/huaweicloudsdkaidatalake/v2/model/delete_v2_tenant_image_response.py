# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteV2TenantImageResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'image_id': 'str'
    }

    attribute_map = {
        'image_id': 'image_id'
    }

    def __init__(self, image_id=None):
        r"""DeleteV2TenantImageResponse

        The model defined in huaweicloud sdk

        :param image_id: **参数解释**：镜像ID。 **取值范围**：长度为32~36的英文字符、数字和中划线的组合。 
        :type image_id: str
        """
        
        super().__init__()

        self._image_id = None
        self.discriminator = None

        if image_id is not None:
            self.image_id = image_id

    @property
    def image_id(self):
        r"""Gets the image_id of this DeleteV2TenantImageResponse.

        **参数解释**：镜像ID。 **取值范围**：长度为32~36的英文字符、数字和中划线的组合。 

        :return: The image_id of this DeleteV2TenantImageResponse.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this DeleteV2TenantImageResponse.

        **参数解释**：镜像ID。 **取值范围**：长度为32~36的英文字符、数字和中划线的组合。 

        :param image_id: The image_id of this DeleteV2TenantImageResponse.
        :type image_id: str
        """
        self._image_id = image_id

    def to_dict(self):
        import warnings
        warnings.warn("DeleteV2TenantImageResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, DeleteV2TenantImageResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
