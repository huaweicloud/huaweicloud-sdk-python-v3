# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FlowBps:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'utime': 'int',
        'attack_bps': 'int',
        'normal_bps': 'int'
    }

    attribute_map = {
        'utime': 'utime',
        'attack_bps': 'attack_bps',
        'normal_bps': 'normal_bps'
    }

    def __init__(self, utime=None, attack_bps=None, normal_bps=None):
        r"""FlowBps

        The model defined in huaweicloud sdk

        :param utime: 数据时间
        :type utime: int
        :param attack_bps: 攻击流量
        :type attack_bps: int
        :param normal_bps: 正常流量
        :type normal_bps: int
        """
        
        

        self._utime = None
        self._attack_bps = None
        self._normal_bps = None
        self.discriminator = None

        if utime is not None:
            self.utime = utime
        if attack_bps is not None:
            self.attack_bps = attack_bps
        if normal_bps is not None:
            self.normal_bps = normal_bps

    @property
    def utime(self):
        r"""Gets the utime of this FlowBps.

        数据时间

        :return: The utime of this FlowBps.
        :rtype: int
        """
        return self._utime

    @utime.setter
    def utime(self, utime):
        r"""Sets the utime of this FlowBps.

        数据时间

        :param utime: The utime of this FlowBps.
        :type utime: int
        """
        self._utime = utime

    @property
    def attack_bps(self):
        r"""Gets the attack_bps of this FlowBps.

        攻击流量

        :return: The attack_bps of this FlowBps.
        :rtype: int
        """
        return self._attack_bps

    @attack_bps.setter
    def attack_bps(self, attack_bps):
        r"""Sets the attack_bps of this FlowBps.

        攻击流量

        :param attack_bps: The attack_bps of this FlowBps.
        :type attack_bps: int
        """
        self._attack_bps = attack_bps

    @property
    def normal_bps(self):
        r"""Gets the normal_bps of this FlowBps.

        正常流量

        :return: The normal_bps of this FlowBps.
        :rtype: int
        """
        return self._normal_bps

    @normal_bps.setter
    def normal_bps(self, normal_bps):
        r"""Sets the normal_bps of this FlowBps.

        正常流量

        :param normal_bps: The normal_bps of this FlowBps.
        :type normal_bps: int
        """
        self._normal_bps = normal_bps

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
        if not isinstance(other, FlowBps):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
