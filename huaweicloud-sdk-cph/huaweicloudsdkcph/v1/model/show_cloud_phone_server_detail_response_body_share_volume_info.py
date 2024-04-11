# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowCloudPhoneServerDetailResponseBodyShareVolumeInfo:

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
        'size': 'int',
        'version': 'int'
    }

    attribute_map = {
        'volume_type': 'volume_type',
        'size': 'size',
        'version': 'version'
    }

    def __init__(self, volume_type=None, size=None, version=None):
        """ShowCloudPhoneServerDetailResponseBodyShareVolumeInfo

        The model defined in huaweicloud sdk

        :param volume_type: 共享存储磁盘类型。
        :type volume_type: str
        :param size: 共享存储大小，单位G。
        :type size: int
        :param version: 共享存储版本： - 0：共享存储1.0 - 1：共享存储2.0
        :type version: int
        """
        
        

        self._volume_type = None
        self._size = None
        self._version = None
        self.discriminator = None

        if volume_type is not None:
            self.volume_type = volume_type
        if size is not None:
            self.size = size
        if version is not None:
            self.version = version

    @property
    def volume_type(self):
        """Gets the volume_type of this ShowCloudPhoneServerDetailResponseBodyShareVolumeInfo.

        共享存储磁盘类型。

        :return: The volume_type of this ShowCloudPhoneServerDetailResponseBodyShareVolumeInfo.
        :rtype: str
        """
        return self._volume_type

    @volume_type.setter
    def volume_type(self, volume_type):
        """Sets the volume_type of this ShowCloudPhoneServerDetailResponseBodyShareVolumeInfo.

        共享存储磁盘类型。

        :param volume_type: The volume_type of this ShowCloudPhoneServerDetailResponseBodyShareVolumeInfo.
        :type volume_type: str
        """
        self._volume_type = volume_type

    @property
    def size(self):
        """Gets the size of this ShowCloudPhoneServerDetailResponseBodyShareVolumeInfo.

        共享存储大小，单位G。

        :return: The size of this ShowCloudPhoneServerDetailResponseBodyShareVolumeInfo.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ShowCloudPhoneServerDetailResponseBodyShareVolumeInfo.

        共享存储大小，单位G。

        :param size: The size of this ShowCloudPhoneServerDetailResponseBodyShareVolumeInfo.
        :type size: int
        """
        self._size = size

    @property
    def version(self):
        """Gets the version of this ShowCloudPhoneServerDetailResponseBodyShareVolumeInfo.

        共享存储版本： - 0：共享存储1.0 - 1：共享存储2.0

        :return: The version of this ShowCloudPhoneServerDetailResponseBodyShareVolumeInfo.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ShowCloudPhoneServerDetailResponseBodyShareVolumeInfo.

        共享存储版本： - 0：共享存储1.0 - 1：共享存储2.0

        :param version: The version of this ShowCloudPhoneServerDetailResponseBodyShareVolumeInfo.
        :type version: int
        """
        self._version = version

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
        if not isinstance(other, ShowCloudPhoneServerDetailResponseBodyShareVolumeInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
