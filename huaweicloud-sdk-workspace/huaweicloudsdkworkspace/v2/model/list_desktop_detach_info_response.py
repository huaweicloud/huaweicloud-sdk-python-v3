# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDesktopDetachInfoResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'desktop_detach_infos': 'list[DesktopDetachInfo]'
    }

    attribute_map = {
        'desktop_detach_infos': 'desktop_detach_infos'
    }

    def __init__(self, desktop_detach_infos=None):
        """ListDesktopDetachInfoResponse

        The model defined in huaweicloud sdk

        :param desktop_detach_infos: 桌面解绑信息
        :type desktop_detach_infos: list[:class:`huaweicloudsdkworkspace.v2.DesktopDetachInfo`]
        """
        
        super(ListDesktopDetachInfoResponse, self).__init__()

        self._desktop_detach_infos = None
        self.discriminator = None

        if desktop_detach_infos is not None:
            self.desktop_detach_infos = desktop_detach_infos

    @property
    def desktop_detach_infos(self):
        """Gets the desktop_detach_infos of this ListDesktopDetachInfoResponse.

        桌面解绑信息

        :return: The desktop_detach_infos of this ListDesktopDetachInfoResponse.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.DesktopDetachInfo`]
        """
        return self._desktop_detach_infos

    @desktop_detach_infos.setter
    def desktop_detach_infos(self, desktop_detach_infos):
        """Sets the desktop_detach_infos of this ListDesktopDetachInfoResponse.

        桌面解绑信息

        :param desktop_detach_infos: The desktop_detach_infos of this ListDesktopDetachInfoResponse.
        :type desktop_detach_infos: list[:class:`huaweicloudsdkworkspace.v2.DesktopDetachInfo`]
        """
        self._desktop_detach_infos = desktop_detach_infos

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
        if not isinstance(other, ListDesktopDetachInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
