# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowServerBlockDeviceResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'volume_attachment': 'ServerBlockDevice'
    }

    attribute_map = {
        'volume_attachment': 'volumeAttachment'
    }

    def __init__(self, volume_attachment=None):
        """ShowServerBlockDeviceResponse

        The model defined in huaweicloud sdk

        :param volume_attachment: 
        :type volume_attachment: :class:`huaweicloudsdkecs.v2.ServerBlockDevice`
        """
        
        super(ShowServerBlockDeviceResponse, self).__init__()

        self._volume_attachment = None
        self.discriminator = None

        if volume_attachment is not None:
            self.volume_attachment = volume_attachment

    @property
    def volume_attachment(self):
        """Gets the volume_attachment of this ShowServerBlockDeviceResponse.

        :return: The volume_attachment of this ShowServerBlockDeviceResponse.
        :rtype: :class:`huaweicloudsdkecs.v2.ServerBlockDevice`
        """
        return self._volume_attachment

    @volume_attachment.setter
    def volume_attachment(self, volume_attachment):
        """Sets the volume_attachment of this ShowServerBlockDeviceResponse.

        :param volume_attachment: The volume_attachment of this ShowServerBlockDeviceResponse.
        :type volume_attachment: :class:`huaweicloudsdkecs.v2.ServerBlockDevice`
        """
        self._volume_attachment = volume_attachment

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
        if not isinstance(other, ShowServerBlockDeviceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
