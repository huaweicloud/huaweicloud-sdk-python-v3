# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListImChannelsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'im_channels': 'list[ImChannelItem]'
    }

    attribute_map = {
        'im_channels': 'im_channels'
    }

    def __init__(self, im_channels=None):
        r"""ListImChannelsResponse

        The model defined in huaweicloud sdk

        :param im_channels: IM 通道配置列表
        :type im_channels: list[:class:`huaweicloudsdkworkspace.v2.ImChannelItem`]
        """
        
        super().__init__()

        self._im_channels = None
        self.discriminator = None

        if im_channels is not None:
            self.im_channels = im_channels

    @property
    def im_channels(self):
        r"""Gets the im_channels of this ListImChannelsResponse.

        IM 通道配置列表

        :return: The im_channels of this ListImChannelsResponse.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.ImChannelItem`]
        """
        return self._im_channels

    @im_channels.setter
    def im_channels(self, im_channels):
        r"""Sets the im_channels of this ListImChannelsResponse.

        IM 通道配置列表

        :param im_channels: The im_channels of this ListImChannelsResponse.
        :type im_channels: list[:class:`huaweicloudsdkworkspace.v2.ImChannelItem`]
        """
        self._im_channels = im_channels

    def to_dict(self):
        import warnings
        warnings.warn("ListImChannelsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListImChannelsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
