# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDesktopNetworksRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'desktop_ids': 'list[str]'
    }

    attribute_map = {
        'desktop_ids': 'desktop_ids'
    }

    def __init__(self, desktop_ids=None):
        r"""ShowDesktopNetworksRequest

        The model defined in huaweicloud sdk

        :param desktop_ids: 桌面id列表，最小为1，最大为100。
        :type desktop_ids: list[str]
        """
        
        

        self._desktop_ids = None
        self.discriminator = None

        if desktop_ids is not None:
            self.desktop_ids = desktop_ids

    @property
    def desktop_ids(self):
        r"""Gets the desktop_ids of this ShowDesktopNetworksRequest.

        桌面id列表，最小为1，最大为100。

        :return: The desktop_ids of this ShowDesktopNetworksRequest.
        :rtype: list[str]
        """
        return self._desktop_ids

    @desktop_ids.setter
    def desktop_ids(self, desktop_ids):
        r"""Sets the desktop_ids of this ShowDesktopNetworksRequest.

        桌面id列表，最小为1，最大为100。

        :param desktop_ids: The desktop_ids of this ShowDesktopNetworksRequest.
        :type desktop_ids: list[str]
        """
        self._desktop_ids = desktop_ids

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
        if not isinstance(other, ShowDesktopNetworksRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
