# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDiskTypeResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'disk_types': 'list[DiskType]'
    }

    attribute_map = {
        'disk_types': 'diskTypes'
    }

    def __init__(self, disk_types=None):
        r"""ListDiskTypeResponse

        The model defined in huaweicloud sdk

        :param disk_types: **参数解释**： 磁盘类型列表。 **取值范围**： 不涉及
        :type disk_types: list[:class:`huaweicloudsdkcss.v1.DiskType`]
        """
        
        super().__init__()

        self._disk_types = None
        self.discriminator = None

        if disk_types is not None:
            self.disk_types = disk_types

    @property
    def disk_types(self):
        r"""Gets the disk_types of this ListDiskTypeResponse.

        **参数解释**： 磁盘类型列表。 **取值范围**： 不涉及

        :return: The disk_types of this ListDiskTypeResponse.
        :rtype: list[:class:`huaweicloudsdkcss.v1.DiskType`]
        """
        return self._disk_types

    @disk_types.setter
    def disk_types(self, disk_types):
        r"""Sets the disk_types of this ListDiskTypeResponse.

        **参数解释**： 磁盘类型列表。 **取值范围**： 不涉及

        :param disk_types: The disk_types of this ListDiskTypeResponse.
        :type disk_types: list[:class:`huaweicloudsdkcss.v1.DiskType`]
        """
        self._disk_types = disk_types

    def to_dict(self):
        import warnings
        warnings.warn("ListDiskTypeResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListDiskTypeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
