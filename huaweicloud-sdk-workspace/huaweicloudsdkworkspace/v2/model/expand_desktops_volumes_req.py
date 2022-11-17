# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExpandDesktopsVolumesReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'desktop_volumes_expansion': 'list[ExpandVolumesReq]'
    }

    attribute_map = {
        'desktop_volumes_expansion': 'desktop_volumes_expansion'
    }

    def __init__(self, desktop_volumes_expansion=None):
        """ExpandDesktopsVolumesReq

        The model defined in huaweicloud sdk

        :param desktop_volumes_expansion: 扩容磁盘参数。
        :type desktop_volumes_expansion: list[:class:`huaweicloudsdkworkspace.v2.ExpandVolumesReq`]
        """
        
        

        self._desktop_volumes_expansion = None
        self.discriminator = None

        if desktop_volumes_expansion is not None:
            self.desktop_volumes_expansion = desktop_volumes_expansion

    @property
    def desktop_volumes_expansion(self):
        """Gets the desktop_volumes_expansion of this ExpandDesktopsVolumesReq.

        扩容磁盘参数。

        :return: The desktop_volumes_expansion of this ExpandDesktopsVolumesReq.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.ExpandVolumesReq`]
        """
        return self._desktop_volumes_expansion

    @desktop_volumes_expansion.setter
    def desktop_volumes_expansion(self, desktop_volumes_expansion):
        """Sets the desktop_volumes_expansion of this ExpandDesktopsVolumesReq.

        扩容磁盘参数。

        :param desktop_volumes_expansion: The desktop_volumes_expansion of this ExpandDesktopsVolumesReq.
        :type desktop_volumes_expansion: list[:class:`huaweicloudsdkworkspace.v2.ExpandVolumesReq`]
        """
        self._desktop_volumes_expansion = desktop_volumes_expansion

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
        if not isinstance(other, ExpandDesktopsVolumesReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
