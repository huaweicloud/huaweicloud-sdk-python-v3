# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowVolumeInRecycleResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'volume': 'RecycleBinVolume'
    }

    attribute_map = {
        'volume': 'volume'
    }

    def __init__(self, volume=None):
        r"""ShowVolumeInRecycleResponse

        The model defined in huaweicloud sdk

        :param volume: 
        :type volume: :class:`huaweicloudsdkevs.v2.RecycleBinVolume`
        """
        
        super().__init__()

        self._volume = None
        self.discriminator = None

        if volume is not None:
            self.volume = volume

    @property
    def volume(self):
        r"""Gets the volume of this ShowVolumeInRecycleResponse.

        :return: The volume of this ShowVolumeInRecycleResponse.
        :rtype: :class:`huaweicloudsdkevs.v2.RecycleBinVolume`
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        r"""Sets the volume of this ShowVolumeInRecycleResponse.

        :param volume: The volume of this ShowVolumeInRecycleResponse.
        :type volume: :class:`huaweicloudsdkevs.v2.RecycleBinVolume`
        """
        self._volume = volume

    def to_dict(self):
        import warnings
        warnings.warn("ShowVolumeInRecycleResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowVolumeInRecycleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
