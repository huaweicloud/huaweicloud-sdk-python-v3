# coding: utf-8

import pprint
import re

import six





class UserStatusDTO:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'number': 'str',
        'reg_status': 'str',
        'call_status': 'str'
    }

    attribute_map = {
        'number': 'Number',
        'reg_status': 'RegStatus',
        'call_status': 'CallStatus'
    }

    def __init__(self, number=None, reg_status=None, call_status=None):
        """UserStatusDTO - a model defined in huaweicloud sdk"""
        
        

        self._number = None
        self._reg_status = None
        self._call_status = None
        self.discriminator = None

        if number is not None:
            self.number = number
        if reg_status is not None:
            self.reg_status = reg_status
        if call_status is not None:
            self.call_status = call_status

    @property
    def number(self):
        """Gets the number of this UserStatusDTO.

        终端号码

        :return: The number of this UserStatusDTO.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this UserStatusDTO.

        终端号码

        :param number: The number of this UserStatusDTO.
        :type: str
        """
        self._number = number

    @property
    def reg_status(self):
        """Gets the reg_status of this UserStatusDTO.

        注册状态。 * 1是未注册上 * 0是已注册 

        :return: The reg_status of this UserStatusDTO.
        :rtype: str
        """
        return self._reg_status

    @reg_status.setter
    def reg_status(self, reg_status):
        """Sets the reg_status of this UserStatusDTO.

        注册状态。 * 1是未注册上 * 0是已注册 

        :param reg_status: The reg_status of this UserStatusDTO.
        :type: str
        """
        self._reg_status = reg_status

    @property
    def call_status(self):
        """Gets the call_status of this UserStatusDTO.

        呼叫状态。 * 0:未上线 * 1:空闲中 * 2:使用中 * 3:非会议硬终端统一的无效值 

        :return: The call_status of this UserStatusDTO.
        :rtype: str
        """
        return self._call_status

    @call_status.setter
    def call_status(self, call_status):
        """Sets the call_status of this UserStatusDTO.

        呼叫状态。 * 0:未上线 * 1:空闲中 * 2:使用中 * 3:非会议硬终端统一的无效值 

        :param call_status: The call_status of this UserStatusDTO.
        :type: str
        """
        self._call_status = call_status

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
        if not isinstance(other, UserStatusDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
