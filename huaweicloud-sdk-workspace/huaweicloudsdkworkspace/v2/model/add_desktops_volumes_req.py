# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddDesktopsVolumesReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'add_desktop_volumes_req': 'list[AddDesktopVolumesReq]'
    }

    attribute_map = {
        'add_desktop_volumes_req': 'addDesktopVolumesReq'
    }

    def __init__(self, add_desktop_volumes_req=None):
        """AddDesktopsVolumesReq

        The model defined in huaweicloud sdk

        :param add_desktop_volumes_req: 新增磁盘参数。
        :type add_desktop_volumes_req: list[:class:`huaweicloudsdkworkspace.v2.AddDesktopVolumesReq`]
        """
        
        

        self._add_desktop_volumes_req = None
        self.discriminator = None

        if add_desktop_volumes_req is not None:
            self.add_desktop_volumes_req = add_desktop_volumes_req

    @property
    def add_desktop_volumes_req(self):
        """Gets the add_desktop_volumes_req of this AddDesktopsVolumesReq.

        新增磁盘参数。

        :return: The add_desktop_volumes_req of this AddDesktopsVolumesReq.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.AddDesktopVolumesReq`]
        """
        return self._add_desktop_volumes_req

    @add_desktop_volumes_req.setter
    def add_desktop_volumes_req(self, add_desktop_volumes_req):
        """Sets the add_desktop_volumes_req of this AddDesktopsVolumesReq.

        新增磁盘参数。

        :param add_desktop_volumes_req: The add_desktop_volumes_req of this AddDesktopsVolumesReq.
        :type add_desktop_volumes_req: list[:class:`huaweicloudsdkworkspace.v2.AddDesktopVolumesReq`]
        """
        self._add_desktop_volumes_req = add_desktop_volumes_req

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
        if not isinstance(other, AddDesktopsVolumesReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
