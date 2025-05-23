# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchFreezeDevicesRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'device_ids': 'list[int]'
    }

    attribute_map = {
        'device_ids': 'device_ids'
    }

    def __init__(self, device_ids=None):
        r"""BatchFreezeDevicesRequestBody

        The model defined in huaweicloud sdk

        :param device_ids: 设备ID列表，自动向下取整
        :type device_ids: list[int]
        """
        
        

        self._device_ids = None
        self.discriminator = None

        self.device_ids = device_ids

    @property
    def device_ids(self):
        r"""Gets the device_ids of this BatchFreezeDevicesRequestBody.

        设备ID列表，自动向下取整

        :return: The device_ids of this BatchFreezeDevicesRequestBody.
        :rtype: list[int]
        """
        return self._device_ids

    @device_ids.setter
    def device_ids(self, device_ids):
        r"""Sets the device_ids of this BatchFreezeDevicesRequestBody.

        设备ID列表，自动向下取整

        :param device_ids: The device_ids of this BatchFreezeDevicesRequestBody.
        :type device_ids: list[int]
        """
        self._device_ids = device_ids

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
        if not isinstance(other, BatchFreezeDevicesRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
