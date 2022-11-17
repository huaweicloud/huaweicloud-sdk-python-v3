# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


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
        'type': 'str',
        'role': 'int',
        'is_mute': 'int'
    }

    attribute_map = {
        'name': 'name',
        'phone': 'phone',
        'phone2': 'phone2',
        'phone3': 'phone3',
        'type': 'type',
        'role': 'role',
        'is_mute': 'isMute'
    }

    def __init__(self, name=None, phone=None, phone2=None, phone3=None, type=None, role=None, is_mute=None):
        """PartAttendee

        The model defined in huaweicloud sdk

        :param name: 与会者名称。
        :type name: str
        :param phone: 号码。SIP号码或者手机号码。
        :type phone: str
        :param phone2: 预留字段，取值类型同参数“phone”。
        :type phone2: str
        :param phone3: 预留字段，取值类型同参数“phone”。
        :type phone3: str
        :param type: 终端类型，类型枚举如下： * normal：软终端 * terminal：硬终端 * outside：外部与会人 * mobile：用户手机号码 * ideahub：ideahub * board: 电子白板（SmartRooms）。含Maxhub、海信大屏、IdeaHub B2hwvision：华为智慧屏TV
        :type type: str
        :param role: 用户入会时是否需要自动静音 。默认不静音。 * 0： 不需要静音 * 1： 需要静音
        :type role: int
        :param is_mute: 用户入会时是否需要自动静音。默认不静音。 * 0: 不需要静音。 * 1: 需要静音。
        :type is_mute: int
        """
        
        

        self._name = None
        self._phone = None
        self._phone2 = None
        self._phone3 = None
        self._type = None
        self._role = None
        self._is_mute = None
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
        if role is not None:
            self.role = role
        if is_mute is not None:
            self.is_mute = is_mute

    @property
    def name(self):
        """Gets the name of this PartAttendee.

        与会者名称。

        :return: The name of this PartAttendee.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PartAttendee.

        与会者名称。

        :param name: The name of this PartAttendee.
        :type name: str
        """
        self._name = name

    @property
    def phone(self):
        """Gets the phone of this PartAttendee.

        号码。SIP号码或者手机号码。

        :return: The phone of this PartAttendee.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this PartAttendee.

        号码。SIP号码或者手机号码。

        :param phone: The phone of this PartAttendee.
        :type phone: str
        """
        self._phone = phone

    @property
    def phone2(self):
        """Gets the phone2 of this PartAttendee.

        预留字段，取值类型同参数“phone”。

        :return: The phone2 of this PartAttendee.
        :rtype: str
        """
        return self._phone2

    @phone2.setter
    def phone2(self, phone2):
        """Sets the phone2 of this PartAttendee.

        预留字段，取值类型同参数“phone”。

        :param phone2: The phone2 of this PartAttendee.
        :type phone2: str
        """
        self._phone2 = phone2

    @property
    def phone3(self):
        """Gets the phone3 of this PartAttendee.

        预留字段，取值类型同参数“phone”。

        :return: The phone3 of this PartAttendee.
        :rtype: str
        """
        return self._phone3

    @phone3.setter
    def phone3(self, phone3):
        """Sets the phone3 of this PartAttendee.

        预留字段，取值类型同参数“phone”。

        :param phone3: The phone3 of this PartAttendee.
        :type phone3: str
        """
        self._phone3 = phone3

    @property
    def type(self):
        """Gets the type of this PartAttendee.

        终端类型，类型枚举如下： * normal：软终端 * terminal：硬终端 * outside：外部与会人 * mobile：用户手机号码 * ideahub：ideahub * board: 电子白板（SmartRooms）。含Maxhub、海信大屏、IdeaHub B2hwvision：华为智慧屏TV

        :return: The type of this PartAttendee.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PartAttendee.

        终端类型，类型枚举如下： * normal：软终端 * terminal：硬终端 * outside：外部与会人 * mobile：用户手机号码 * ideahub：ideahub * board: 电子白板（SmartRooms）。含Maxhub、海信大屏、IdeaHub B2hwvision：华为智慧屏TV

        :param type: The type of this PartAttendee.
        :type type: str
        """
        self._type = type

    @property
    def role(self):
        """Gets the role of this PartAttendee.

        用户入会时是否需要自动静音 。默认不静音。 * 0： 不需要静音 * 1： 需要静音

        :return: The role of this PartAttendee.
        :rtype: int
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this PartAttendee.

        用户入会时是否需要自动静音 。默认不静音。 * 0： 不需要静音 * 1： 需要静音

        :param role: The role of this PartAttendee.
        :type role: int
        """
        self._role = role

    @property
    def is_mute(self):
        """Gets the is_mute of this PartAttendee.

        用户入会时是否需要自动静音。默认不静音。 * 0: 不需要静音。 * 1: 需要静音。

        :return: The is_mute of this PartAttendee.
        :rtype: int
        """
        return self._is_mute

    @is_mute.setter
    def is_mute(self, is_mute):
        """Sets the is_mute of this PartAttendee.

        用户入会时是否需要自动静音。默认不静音。 * 0: 不需要静音。 * 1: 需要静音。

        :param is_mute: The is_mute of this PartAttendee.
        :type is_mute: int
        """
        self._is_mute = is_mute

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
        if not isinstance(other, PartAttendee):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
