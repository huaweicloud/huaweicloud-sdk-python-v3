# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OperationObject:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'room_code': 'str',
        'rack_code': 'str',
        'u_position': 'str',
        'sn': 'str',
        'port_or_slot': 'str'
    }

    attribute_map = {
        'type': 'type',
        'room_code': 'room_code',
        'rack_code': 'rack_code',
        'u_position': 'u_position',
        'sn': 'sn',
        'port_or_slot': 'port_or_slot'
    }

    def __init__(self, type=None, room_code=None, rack_code=None, u_position=None, sn=None, port_or_slot=None):
        r"""OperationObject

        The model defined in huaweicloud sdk

        :param type: 对象类型
        :type type: str
        :param room_code: 机房编码
        :type room_code: str
        :param rack_code: 机柜编码
        :type rack_code: str
        :param u_position: u位
        :type u_position: str
        :param sn: sn
        :type sn: str
        :param port_or_slot: 端口号或槽口号
        :type port_or_slot: str
        """
        
        

        self._type = None
        self._room_code = None
        self._rack_code = None
        self._u_position = None
        self._sn = None
        self._port_or_slot = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if room_code is not None:
            self.room_code = room_code
        if rack_code is not None:
            self.rack_code = rack_code
        if u_position is not None:
            self.u_position = u_position
        if sn is not None:
            self.sn = sn
        if port_or_slot is not None:
            self.port_or_slot = port_or_slot

    @property
    def type(self):
        r"""Gets the type of this OperationObject.

        对象类型

        :return: The type of this OperationObject.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this OperationObject.

        对象类型

        :param type: The type of this OperationObject.
        :type type: str
        """
        self._type = type

    @property
    def room_code(self):
        r"""Gets the room_code of this OperationObject.

        机房编码

        :return: The room_code of this OperationObject.
        :rtype: str
        """
        return self._room_code

    @room_code.setter
    def room_code(self, room_code):
        r"""Sets the room_code of this OperationObject.

        机房编码

        :param room_code: The room_code of this OperationObject.
        :type room_code: str
        """
        self._room_code = room_code

    @property
    def rack_code(self):
        r"""Gets the rack_code of this OperationObject.

        机柜编码

        :return: The rack_code of this OperationObject.
        :rtype: str
        """
        return self._rack_code

    @rack_code.setter
    def rack_code(self, rack_code):
        r"""Sets the rack_code of this OperationObject.

        机柜编码

        :param rack_code: The rack_code of this OperationObject.
        :type rack_code: str
        """
        self._rack_code = rack_code

    @property
    def u_position(self):
        r"""Gets the u_position of this OperationObject.

        u位

        :return: The u_position of this OperationObject.
        :rtype: str
        """
        return self._u_position

    @u_position.setter
    def u_position(self, u_position):
        r"""Sets the u_position of this OperationObject.

        u位

        :param u_position: The u_position of this OperationObject.
        :type u_position: str
        """
        self._u_position = u_position

    @property
    def sn(self):
        r"""Gets the sn of this OperationObject.

        sn

        :return: The sn of this OperationObject.
        :rtype: str
        """
        return self._sn

    @sn.setter
    def sn(self, sn):
        r"""Sets the sn of this OperationObject.

        sn

        :param sn: The sn of this OperationObject.
        :type sn: str
        """
        self._sn = sn

    @property
    def port_or_slot(self):
        r"""Gets the port_or_slot of this OperationObject.

        端口号或槽口号

        :return: The port_or_slot of this OperationObject.
        :rtype: str
        """
        return self._port_or_slot

    @port_or_slot.setter
    def port_or_slot(self, port_or_slot):
        r"""Sets the port_or_slot of this OperationObject.

        端口号或槽口号

        :param port_or_slot: The port_or_slot of this OperationObject.
        :type port_or_slot: str
        """
        self._port_or_slot = port_or_slot

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
        if not isinstance(other, OperationObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
