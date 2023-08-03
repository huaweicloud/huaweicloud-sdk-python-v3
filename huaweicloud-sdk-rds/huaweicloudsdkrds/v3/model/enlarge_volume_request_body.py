# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EnlargeVolumeRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enlarge_volume': 'EnlargeVolumeObject'
    }

    attribute_map = {
        'enlarge_volume': 'enlarge_volume'
    }

    def __init__(self, enlarge_volume=None):
        """EnlargeVolumeRequestBody

        The model defined in huaweicloud sdk

        :param enlarge_volume: 
        :type enlarge_volume: :class:`huaweicloudsdkrds.v3.EnlargeVolumeObject`
        """
        
        

        self._enlarge_volume = None
        self.discriminator = None

        self.enlarge_volume = enlarge_volume

    @property
    def enlarge_volume(self):
        """Gets the enlarge_volume of this EnlargeVolumeRequestBody.

        :return: The enlarge_volume of this EnlargeVolumeRequestBody.
        :rtype: :class:`huaweicloudsdkrds.v3.EnlargeVolumeObject`
        """
        return self._enlarge_volume

    @enlarge_volume.setter
    def enlarge_volume(self, enlarge_volume):
        """Sets the enlarge_volume of this EnlargeVolumeRequestBody.

        :param enlarge_volume: The enlarge_volume of this EnlargeVolumeRequestBody.
        :type enlarge_volume: :class:`huaweicloudsdkrds.v3.EnlargeVolumeObject`
        """
        self._enlarge_volume = enlarge_volume

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
        if not isinstance(other, EnlargeVolumeRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
