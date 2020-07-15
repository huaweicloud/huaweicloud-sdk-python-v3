# coding: utf-8

import pprint
import re

import six





class ActionDeviceCommand:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'device_id': 'str',
        'cmd': 'Cmd'
    }

    attribute_map = {
        'device_id': 'device_id',
        'cmd': 'cmd'
    }

    def __init__(self, device_id=None, cmd=None):
        """ActionDeviceCommand - a model defined in huaweicloud sdk"""
        
        

        self._device_id = None
        self._cmd = None
        self.discriminator = None

        if device_id is not None:
            self.device_id = device_id
        self.cmd = cmd

    @property
    def device_id(self):
        """Gets the device_id of this ActionDeviceCommand.

        下发命令的设备ID。 - 当创建设备数据规则时，若device_id为空，则命令下发给触发条件的设备。 - 当创建定时规则时，不允许为空。 

        :return: The device_id of this ActionDeviceCommand.
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this ActionDeviceCommand.

        下发命令的设备ID。 - 当创建设备数据规则时，若device_id为空，则命令下发给触发条件的设备。 - 当创建定时规则时，不允许为空。 

        :param device_id: The device_id of this ActionDeviceCommand.
        :type: str
        """
        self._device_id = device_id

    @property
    def cmd(self):
        """Gets the cmd of this ActionDeviceCommand.


        :return: The cmd of this ActionDeviceCommand.
        :rtype: Cmd
        """
        return self._cmd

    @cmd.setter
    def cmd(self, cmd):
        """Sets the cmd of this ActionDeviceCommand.


        :param cmd: The cmd of this ActionDeviceCommand.
        :type: Cmd
        """
        self._cmd = cmd

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ActionDeviceCommand):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
