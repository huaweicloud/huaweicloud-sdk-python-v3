# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Eip:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'type': 'str',
        'charge_mode': 'str',
        'bandwidth_size': 'int'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'charge_mode': 'charge_mode',
        'bandwidth_size': 'bandwidth_size'
    }

    def __init__(self, id=None, type=None, charge_mode=None, bandwidth_size=None):
        """Eip

        The model defined in huaweicloud sdk

        :param id: 桌面绑定的Eip的id，有值时优先绑定Eip。
        :type id: str
        :param type: EIP的类型，5_bgp（全动态BGP），5_sbgp（静态BGP）
        :type type: str
        :param charge_mode: eip带宽计费模式 - TRAFFIC：按流量计费。 - BANDWIDTH：按带宽计费。
        :type charge_mode: str
        :param bandwidth_size: 带宽大小
        :type bandwidth_size: int
        """
        
        

        self._id = None
        self._type = None
        self._charge_mode = None
        self._bandwidth_size = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if charge_mode is not None:
            self.charge_mode = charge_mode
        if bandwidth_size is not None:
            self.bandwidth_size = bandwidth_size

    @property
    def id(self):
        """Gets the id of this Eip.

        桌面绑定的Eip的id，有值时优先绑定Eip。

        :return: The id of this Eip.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Eip.

        桌面绑定的Eip的id，有值时优先绑定Eip。

        :param id: The id of this Eip.
        :type id: str
        """
        self._id = id

    @property
    def type(self):
        """Gets the type of this Eip.

        EIP的类型，5_bgp（全动态BGP），5_sbgp（静态BGP）

        :return: The type of this Eip.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Eip.

        EIP的类型，5_bgp（全动态BGP），5_sbgp（静态BGP）

        :param type: The type of this Eip.
        :type type: str
        """
        self._type = type

    @property
    def charge_mode(self):
        """Gets the charge_mode of this Eip.

        eip带宽计费模式 - TRAFFIC：按流量计费。 - BANDWIDTH：按带宽计费。

        :return: The charge_mode of this Eip.
        :rtype: str
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        """Sets the charge_mode of this Eip.

        eip带宽计费模式 - TRAFFIC：按流量计费。 - BANDWIDTH：按带宽计费。

        :param charge_mode: The charge_mode of this Eip.
        :type charge_mode: str
        """
        self._charge_mode = charge_mode

    @property
    def bandwidth_size(self):
        """Gets the bandwidth_size of this Eip.

        带宽大小

        :return: The bandwidth_size of this Eip.
        :rtype: int
        """
        return self._bandwidth_size

    @bandwidth_size.setter
    def bandwidth_size(self, bandwidth_size):
        """Sets the bandwidth_size of this Eip.

        带宽大小

        :param bandwidth_size: The bandwidth_size of this Eip.
        :type bandwidth_size: int
        """
        self._bandwidth_size = bandwidth_size

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
        if not isinstance(other, Eip):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
