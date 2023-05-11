# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateServerBlockDeviceReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'block_device': 'UpdateServerBlockDeviceOption'
    }

    attribute_map = {
        'block_device': 'block_device'
    }

    def __init__(self, block_device=None):
        """UpdateServerBlockDeviceReq

        The model defined in huaweicloud sdk

        :param block_device: 
        :type block_device: :class:`huaweicloudsdkecs.v2.UpdateServerBlockDeviceOption`
        """
        
        

        self._block_device = None
        self.discriminator = None

        self.block_device = block_device

    @property
    def block_device(self):
        """Gets the block_device of this UpdateServerBlockDeviceReq.

        :return: The block_device of this UpdateServerBlockDeviceReq.
        :rtype: :class:`huaweicloudsdkecs.v2.UpdateServerBlockDeviceOption`
        """
        return self._block_device

    @block_device.setter
    def block_device(self, block_device):
        """Sets the block_device of this UpdateServerBlockDeviceReq.

        :param block_device: The block_device of this UpdateServerBlockDeviceReq.
        :type block_device: :class:`huaweicloudsdkecs.v2.UpdateServerBlockDeviceOption`
        """
        self._block_device = block_device

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
        if not isinstance(other, UpdateServerBlockDeviceReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
