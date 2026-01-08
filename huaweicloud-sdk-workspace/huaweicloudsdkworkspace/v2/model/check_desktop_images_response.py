# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckDesktopImagesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'image_infos': 'list[DesktopImageInfo]'
    }

    attribute_map = {
        'image_infos': 'image_infos'
    }

    def __init__(self, image_infos=None):
        r"""CheckDesktopImagesResponse

        The model defined in huaweicloud sdk

        :param image_infos: 桌面镜像信息。
        :type image_infos: list[:class:`huaweicloudsdkworkspace.v2.DesktopImageInfo`]
        """
        
        super().__init__()

        self._image_infos = None
        self.discriminator = None

        if image_infos is not None:
            self.image_infos = image_infos

    @property
    def image_infos(self):
        r"""Gets the image_infos of this CheckDesktopImagesResponse.

        桌面镜像信息。

        :return: The image_infos of this CheckDesktopImagesResponse.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.DesktopImageInfo`]
        """
        return self._image_infos

    @image_infos.setter
    def image_infos(self, image_infos):
        r"""Sets the image_infos of this CheckDesktopImagesResponse.

        桌面镜像信息。

        :param image_infos: The image_infos of this CheckDesktopImagesResponse.
        :type image_infos: list[:class:`huaweicloudsdkworkspace.v2.DesktopImageInfo`]
        """
        self._image_infos = image_infos

    def to_dict(self):
        import warnings
        warnings.warn("CheckDesktopImagesResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, CheckDesktopImagesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
