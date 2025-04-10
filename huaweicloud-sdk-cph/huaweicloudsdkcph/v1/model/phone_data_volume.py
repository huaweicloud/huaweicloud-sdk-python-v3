# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PhoneDataVolume:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'volume_type': 'str',
        'volume_size': 'int'
    }

    attribute_map = {
        'volume_type': 'volume_type',
        'volume_size': 'volume_size'
    }

    def __init__(self, volume_type=None, volume_size=None):
        r"""PhoneDataVolume

        The model defined in huaweicloud sdk

        :param volume_type: 云手机数据盘类型。
        :type volume_type: str
        :param volume_size: 云手机数据盘大小。
        :type volume_size: int
        """
        
        

        self._volume_type = None
        self._volume_size = None
        self.discriminator = None

        if volume_type is not None:
            self.volume_type = volume_type
        if volume_size is not None:
            self.volume_size = volume_size

    @property
    def volume_type(self):
        r"""Gets the volume_type of this PhoneDataVolume.

        云手机数据盘类型。

        :return: The volume_type of this PhoneDataVolume.
        :rtype: str
        """
        return self._volume_type

    @volume_type.setter
    def volume_type(self, volume_type):
        r"""Sets the volume_type of this PhoneDataVolume.

        云手机数据盘类型。

        :param volume_type: The volume_type of this PhoneDataVolume.
        :type volume_type: str
        """
        self._volume_type = volume_type

    @property
    def volume_size(self):
        r"""Gets the volume_size of this PhoneDataVolume.

        云手机数据盘大小。

        :return: The volume_size of this PhoneDataVolume.
        :rtype: int
        """
        return self._volume_size

    @volume_size.setter
    def volume_size(self, volume_size):
        r"""Sets the volume_size of this PhoneDataVolume.

        云手机数据盘大小。

        :param volume_size: The volume_size of this PhoneDataVolume.
        :type volume_size: int
        """
        self._volume_size = volume_size

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
        if not isinstance(other, PhoneDataVolume):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
