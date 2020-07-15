# coding: utf-8

import pprint
import re

import six





class PartAttendee:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'phone': 'str',
        'phone2': 'str',
        'phone3': 'str',
        'type': 'str'
    }

    attribute_map = {
        'name': 'name',
        'phone': 'phone',
        'phone2': 'phone2',
        'phone3': 'phone3',
        'type': 'type'
    }

    def __init__(self, name=None, phone=None, phone2=None, phone3=None, type=None):
        """PartAttendee - a model defined in huaweicloud sdk"""
        
        

        self._name = None
        self._phone = None
        self._phone2 = None
        self._phone3 = None
        self._type = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if phone is not None:
            self.phone = phone
        if phone2 is not None:
            self.phone2 = phone2
        if phone3 is not None:
            self.phone3 = phone3
        if type is not None:
            self.type = type

    @property
    def name(self):
        """Gets the name of this PartAttendee.

        与会者名称或昵称。长度限制为96个字符。

        :return: The name of this PartAttendee.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PartAttendee.

        与会者名称或昵称。长度限制为96个字符。

        :param name: The name of this PartAttendee.
        :type: str
        """
        self._name = name

    @property
    def phone(self):
        """Gets the phone of this PartAttendee.

        电话号码(可支持SIP、TEL号码格式)。最大不超过127个字符。 当type为telepresence时，且设备为三屏智真，则该字段填写中屏号码。

        :return: The phone of this PartAttendee.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this PartAttendee.

        电话号码(可支持SIP、TEL号码格式)。最大不超过127个字符。 当type为telepresence时，且设备为三屏智真，则该字段填写中屏号码。

        :param phone: The phone of this PartAttendee.
        :type: str
        """
        self._phone = phone

    @property
    def phone2(self):
        """Gets the phone2 of this PartAttendee.

        取值类型同参数phone。（预留字段） 当type为telepresence时，且设备为三屏智真，则该字段填写左屏号码。

        :return: The phone2 of this PartAttendee.
        :rtype: str
        """
        return self._phone2

    @phone2.setter
    def phone2(self, phone2):
        """Sets the phone2 of this PartAttendee.

        取值类型同参数phone。（预留字段） 当type为telepresence时，且设备为三屏智真，则该字段填写左屏号码。

        :param phone2: The phone2 of this PartAttendee.
        :type: str
        """
        self._phone2 = phone2

    @property
    def phone3(self):
        """Gets the phone3 of this PartAttendee.

        取值类型同参数phone。（预留字段） 当type为telepresence时，且设备为三屏智真，则该字段填写右屏号码。

        :return: The phone3 of this PartAttendee.
        :rtype: str
        """
        return self._phone3

    @phone3.setter
    def phone3(self, phone3):
        """Sets the phone3 of this PartAttendee.

        取值类型同参数phone。（预留字段） 当type为telepresence时，且设备为三屏智真，则该字段填写右屏号码。

        :param phone3: The phone3 of this PartAttendee.
        :type: str
        """
        self._phone3 = phone3

    @property
    def type(self):
        """Gets the type of this PartAttendee.

        默认值由会议AS定义，号码类型枚举如下： - normal: 软终端。 - telepresence: 智真。单屏、三屏智真均属此类。（预留字段） - terminal: 会议室或硬终端。 - outside: 外部与会人。 - mobile: 用户手机号码。 - telephone: 用户固定电话。（预留字段）

        :return: The type of this PartAttendee.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PartAttendee.

        默认值由会议AS定义，号码类型枚举如下： - normal: 软终端。 - telepresence: 智真。单屏、三屏智真均属此类。（预留字段） - terminal: 会议室或硬终端。 - outside: 外部与会人。 - mobile: 用户手机号码。 - telephone: 用户固定电话。（预留字段）

        :param type: The type of this PartAttendee.
        :type: str
        """
        self._type = type

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
        if not isinstance(other, PartAttendee):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
