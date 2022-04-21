# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowMaintainWindowsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'maintain_windows': 'list[MaintainWindowsEntity]'
    }

    attribute_map = {
        'maintain_windows': 'maintain_windows'
    }

    def __init__(self, maintain_windows=None):
        """ShowMaintainWindowsResponse

        The model defined in huaweicloud sdk

        :param maintain_windows: 支持的维护时间窗列表。
        :type maintain_windows: list[:class:`huaweicloudsdkrabbitmq.v2.MaintainWindowsEntity`]
        """
        
        super(ShowMaintainWindowsResponse, self).__init__()

        self._maintain_windows = None
        self.discriminator = None

        if maintain_windows is not None:
            self.maintain_windows = maintain_windows

    @property
    def maintain_windows(self):
        """Gets the maintain_windows of this ShowMaintainWindowsResponse.

        支持的维护时间窗列表。

        :return: The maintain_windows of this ShowMaintainWindowsResponse.
        :rtype: list[:class:`huaweicloudsdkrabbitmq.v2.MaintainWindowsEntity`]
        """
        return self._maintain_windows

    @maintain_windows.setter
    def maintain_windows(self, maintain_windows):
        """Sets the maintain_windows of this ShowMaintainWindowsResponse.

        支持的维护时间窗列表。

        :param maintain_windows: The maintain_windows of this ShowMaintainWindowsResponse.
        :type maintain_windows: list[:class:`huaweicloudsdkrabbitmq.v2.MaintainWindowsEntity`]
        """
        self._maintain_windows = maintain_windows

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
        if not isinstance(other, ShowMaintainWindowsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
