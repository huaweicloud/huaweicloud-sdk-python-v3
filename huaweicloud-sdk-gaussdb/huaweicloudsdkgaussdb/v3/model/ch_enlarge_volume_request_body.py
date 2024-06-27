# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChEnlargeVolumeRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'size_in_gb': 'int'
    }

    attribute_map = {
        'size_in_gb': 'size_in_gb'
    }

    def __init__(self, size_in_gb=None):
        """ChEnlargeVolumeRequestBody

        The model defined in huaweicloud sdk

        :param size_in_gb: 磁盘容量。取值范围：50GB~32000GB。
        :type size_in_gb: int
        """
        
        

        self._size_in_gb = None
        self.discriminator = None

        self.size_in_gb = size_in_gb

    @property
    def size_in_gb(self):
        """Gets the size_in_gb of this ChEnlargeVolumeRequestBody.

        磁盘容量。取值范围：50GB~32000GB。

        :return: The size_in_gb of this ChEnlargeVolumeRequestBody.
        :rtype: int
        """
        return self._size_in_gb

    @size_in_gb.setter
    def size_in_gb(self, size_in_gb):
        """Sets the size_in_gb of this ChEnlargeVolumeRequestBody.

        磁盘容量。取值范围：50GB~32000GB。

        :param size_in_gb: The size_in_gb of this ChEnlargeVolumeRequestBody.
        :type size_in_gb: int
        """
        self._size_in_gb = size_in_gb

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
        if not isinstance(other, ChEnlargeVolumeRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
