# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDesktopsConnectStatusResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'desktops': 'list[ConnectDesktopsInfo]',
        'total_count': 'int'
    }

    attribute_map = {
        'desktops': 'desktops',
        'total_count': 'total_count'
    }

    def __init__(self, desktops=None, total_count=None):
        """ListDesktopsConnectStatusResponse

        The model defined in huaweicloud sdk

        :param desktops: 桌面登录信息列表。
        :type desktops: list[:class:`huaweicloudsdkworkspace.v2.ConnectDesktopsInfo`]
        :param total_count: 桌面总数。
        :type total_count: int
        """
        
        super(ListDesktopsConnectStatusResponse, self).__init__()

        self._desktops = None
        self._total_count = None
        self.discriminator = None

        if desktops is not None:
            self.desktops = desktops
        if total_count is not None:
            self.total_count = total_count

    @property
    def desktops(self):
        """Gets the desktops of this ListDesktopsConnectStatusResponse.

        桌面登录信息列表。

        :return: The desktops of this ListDesktopsConnectStatusResponse.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.ConnectDesktopsInfo`]
        """
        return self._desktops

    @desktops.setter
    def desktops(self, desktops):
        """Sets the desktops of this ListDesktopsConnectStatusResponse.

        桌面登录信息列表。

        :param desktops: The desktops of this ListDesktopsConnectStatusResponse.
        :type desktops: list[:class:`huaweicloudsdkworkspace.v2.ConnectDesktopsInfo`]
        """
        self._desktops = desktops

    @property
    def total_count(self):
        """Gets the total_count of this ListDesktopsConnectStatusResponse.

        桌面总数。

        :return: The total_count of this ListDesktopsConnectStatusResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ListDesktopsConnectStatusResponse.

        桌面总数。

        :param total_count: The total_count of this ListDesktopsConnectStatusResponse.
        :type total_count: int
        """
        self._total_count = total_count

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
        if not isinstance(other, ListDesktopsConnectStatusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
