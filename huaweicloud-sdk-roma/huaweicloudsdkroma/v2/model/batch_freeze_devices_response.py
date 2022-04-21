# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchFreezeDevicesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'success': 'list[DeviceInfoSimple]',
        'failed': 'list[DeviceInfoSimple]'
    }

    attribute_map = {
        'success': 'success',
        'failed': 'failed'
    }

    def __init__(self, success=None, failed=None):
        """BatchFreezeDevicesResponse

        The model defined in huaweicloud sdk

        :param success: 下线成功设备列表
        :type success: list[:class:`huaweicloudsdkroma.v2.DeviceInfoSimple`]
        :param failed: 下线失败设备列表
        :type failed: list[:class:`huaweicloudsdkroma.v2.DeviceInfoSimple`]
        """
        
        super(BatchFreezeDevicesResponse, self).__init__()

        self._success = None
        self._failed = None
        self.discriminator = None

        if success is not None:
            self.success = success
        if failed is not None:
            self.failed = failed

    @property
    def success(self):
        """Gets the success of this BatchFreezeDevicesResponse.

        下线成功设备列表

        :return: The success of this BatchFreezeDevicesResponse.
        :rtype: list[:class:`huaweicloudsdkroma.v2.DeviceInfoSimple`]
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this BatchFreezeDevicesResponse.

        下线成功设备列表

        :param success: The success of this BatchFreezeDevicesResponse.
        :type success: list[:class:`huaweicloudsdkroma.v2.DeviceInfoSimple`]
        """
        self._success = success

    @property
    def failed(self):
        """Gets the failed of this BatchFreezeDevicesResponse.

        下线失败设备列表

        :return: The failed of this BatchFreezeDevicesResponse.
        :rtype: list[:class:`huaweicloudsdkroma.v2.DeviceInfoSimple`]
        """
        return self._failed

    @failed.setter
    def failed(self, failed):
        """Sets the failed of this BatchFreezeDevicesResponse.

        下线失败设备列表

        :param failed: The failed of this BatchFreezeDevicesResponse.
        :type failed: list[:class:`huaweicloudsdkroma.v2.DeviceInfoSimple`]
        """
        self._failed = failed

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
        if not isinstance(other, BatchFreezeDevicesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
