# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListVolumeTypeResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'volume_types': 'list[VolumeTypeInfo]'
    }

    attribute_map = {
        'volume_types': 'volume_types'
    }

    def __init__(self, volume_types=None):
        """ListVolumeTypeResponse

        The model defined in huaweicloud sdk

        :param volume_types: 磁盘列表
        :type volume_types: list[:class:`huaweicloudsdkworkspaceapp.v1.VolumeTypeInfo`]
        """
        
        super(ListVolumeTypeResponse, self).__init__()

        self._volume_types = None
        self.discriminator = None

        if volume_types is not None:
            self.volume_types = volume_types

    @property
    def volume_types(self):
        """Gets the volume_types of this ListVolumeTypeResponse.

        磁盘列表

        :return: The volume_types of this ListVolumeTypeResponse.
        :rtype: list[:class:`huaweicloudsdkworkspaceapp.v1.VolumeTypeInfo`]
        """
        return self._volume_types

    @volume_types.setter
    def volume_types(self, volume_types):
        """Sets the volume_types of this ListVolumeTypeResponse.

        磁盘列表

        :param volume_types: The volume_types of this ListVolumeTypeResponse.
        :type volume_types: list[:class:`huaweicloudsdkworkspaceapp.v1.VolumeTypeInfo`]
        """
        self._volume_types = volume_types

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListVolumeTypeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
