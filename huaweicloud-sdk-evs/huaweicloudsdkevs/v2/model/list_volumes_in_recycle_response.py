# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListVolumesInRecycleResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'volumes': 'list[RecycleBinVolume]'
    }

    attribute_map = {
        'count': 'count',
        'volumes': 'volumes'
    }

    def __init__(self, count=None, volumes=None):
        r"""ListVolumesInRecycleResponse

        The model defined in huaweicloud sdk

        :param count: **参数解释** 云硬盘总数。 **取值范围** 不涉及。
        :type count: int
        :param volumes: **参数解释** 云硬盘列表。 **取值范围** 不涉及。
        :type volumes: list[:class:`huaweicloudsdkevs.v2.RecycleBinVolume`]
        """
        
        super().__init__()

        self._count = None
        self._volumes = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if volumes is not None:
            self.volumes = volumes

    @property
    def count(self):
        r"""Gets the count of this ListVolumesInRecycleResponse.

        **参数解释** 云硬盘总数。 **取值范围** 不涉及。

        :return: The count of this ListVolumesInRecycleResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListVolumesInRecycleResponse.

        **参数解释** 云硬盘总数。 **取值范围** 不涉及。

        :param count: The count of this ListVolumesInRecycleResponse.
        :type count: int
        """
        self._count = count

    @property
    def volumes(self):
        r"""Gets the volumes of this ListVolumesInRecycleResponse.

        **参数解释** 云硬盘列表。 **取值范围** 不涉及。

        :return: The volumes of this ListVolumesInRecycleResponse.
        :rtype: list[:class:`huaweicloudsdkevs.v2.RecycleBinVolume`]
        """
        return self._volumes

    @volumes.setter
    def volumes(self, volumes):
        r"""Sets the volumes of this ListVolumesInRecycleResponse.

        **参数解释** 云硬盘列表。 **取值范围** 不涉及。

        :param volumes: The volumes of this ListVolumesInRecycleResponse.
        :type volumes: list[:class:`huaweicloudsdkevs.v2.RecycleBinVolume`]
        """
        self._volumes = volumes

    def to_dict(self):
        import warnings
        warnings.warn("ListVolumesInRecycleResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListVolumesInRecycleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
