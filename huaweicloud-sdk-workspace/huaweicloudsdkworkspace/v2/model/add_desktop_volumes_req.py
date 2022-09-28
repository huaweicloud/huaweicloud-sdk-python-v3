# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddDesktopVolumesReq:

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
        'volumes': 'list[Volume]'
    }

    attribute_map = {
        'desktop_id': 'desktop_id',
        'volumes': 'volumes'
    }

    def __init__(self, desktop_id=None, volumes=None):
        """AddDesktopVolumesReq

        The model defined in huaweicloud sdk

        :param desktop_id: 桌面Id。
        :type desktop_id: str
        :param volumes: 待新增的磁盘信息，每个桌面的数据盘数量不超过10个。
        :type volumes: list[:class:`huaweicloudsdkworkspace.v2.Volume`]
        """
        
        

        self._desktop_id = None
        self._volumes = None
        self.discriminator = None

        if desktop_id is not None:
            self.desktop_id = desktop_id
        if volumes is not None:
            self.volumes = volumes

    @property
    def desktop_id(self):
        """Gets the desktop_id of this AddDesktopVolumesReq.

        桌面Id。

        :return: The desktop_id of this AddDesktopVolumesReq.
        :rtype: str
        """
        return self._desktop_id

    @desktop_id.setter
    def desktop_id(self, desktop_id):
        """Sets the desktop_id of this AddDesktopVolumesReq.

        桌面Id。

        :param desktop_id: The desktop_id of this AddDesktopVolumesReq.
        :type desktop_id: str
        """
        self._desktop_id = desktop_id

    @property
    def volumes(self):
        """Gets the volumes of this AddDesktopVolumesReq.

        待新增的磁盘信息，每个桌面的数据盘数量不超过10个。

        :return: The volumes of this AddDesktopVolumesReq.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.Volume`]
        """
        return self._volumes

    @volumes.setter
    def volumes(self, volumes):
        """Sets the volumes of this AddDesktopVolumesReq.

        待新增的磁盘信息，每个桌面的数据盘数量不超过10个。

        :param volumes: The volumes of this AddDesktopVolumesReq.
        :type volumes: list[:class:`huaweicloudsdkworkspace.v2.Volume`]
        """
        self._volumes = volumes

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
        if not isinstance(other, AddDesktopVolumesReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
