# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExpandVolumesReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'desktop_id': 'str',
        'volume_id': 'str',
        'new_size': 'int'
    }

    attribute_map = {
        'desktop_id': 'desktop_id',
        'volume_id': 'volume_id',
        'new_size': 'new_size'
    }

    def __init__(self, desktop_id=None, volume_id=None, new_size=None):
        """ExpandVolumesReq

        The model defined in huaweicloud sdk

        :param desktop_id: 桌面ID。
        :type desktop_id: str
        :param volume_id: 磁盘ID。
        :type volume_id: str
        :param new_size: 扩容后的磁盘大小，单位为GB。
        :type new_size: int
        """
        
        

        self._desktop_id = None
        self._volume_id = None
        self._new_size = None
        self.discriminator = None

        if desktop_id is not None:
            self.desktop_id = desktop_id
        if volume_id is not None:
            self.volume_id = volume_id
        if new_size is not None:
            self.new_size = new_size

    @property
    def desktop_id(self):
        """Gets the desktop_id of this ExpandVolumesReq.

        桌面ID。

        :return: The desktop_id of this ExpandVolumesReq.
        :rtype: str
        """
        return self._desktop_id

    @desktop_id.setter
    def desktop_id(self, desktop_id):
        """Sets the desktop_id of this ExpandVolumesReq.

        桌面ID。

        :param desktop_id: The desktop_id of this ExpandVolumesReq.
        :type desktop_id: str
        """
        self._desktop_id = desktop_id

    @property
    def volume_id(self):
        """Gets the volume_id of this ExpandVolumesReq.

        磁盘ID。

        :return: The volume_id of this ExpandVolumesReq.
        :rtype: str
        """
        return self._volume_id

    @volume_id.setter
    def volume_id(self, volume_id):
        """Sets the volume_id of this ExpandVolumesReq.

        磁盘ID。

        :param volume_id: The volume_id of this ExpandVolumesReq.
        :type volume_id: str
        """
        self._volume_id = volume_id

    @property
    def new_size(self):
        """Gets the new_size of this ExpandVolumesReq.

        扩容后的磁盘大小，单位为GB。

        :return: The new_size of this ExpandVolumesReq.
        :rtype: int
        """
        return self._new_size

    @new_size.setter
    def new_size(self, new_size):
        """Sets the new_size of this ExpandVolumesReq.

        扩容后的磁盘大小，单位为GB。

        :param new_size: The new_size of this ExpandVolumesReq.
        :type new_size: int
        """
        self._new_size = new_size

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
        if not isinstance(other, ExpandVolumesReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
