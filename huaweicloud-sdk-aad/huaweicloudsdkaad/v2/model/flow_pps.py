# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FlowPps:

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
        'attack_pps': 'int',
        'normal_pps': 'int'
    }

    attribute_map = {
        'utime': 'utime',
        'attack_pps': 'attack_pps',
        'normal_pps': 'normal_pps'
    }

    def __init__(self, utime=None, attack_pps=None, normal_pps=None):
        r"""FlowPps

        The model defined in huaweicloud sdk

        :param utime: 数据时间
        :type utime: int
        :param attack_pps: 攻击包速率
        :type attack_pps: int
        :param normal_pps: 正常包速率
        :type normal_pps: int
        """
        
        

        self._utime = None
        self._attack_pps = None
        self._normal_pps = None
        self.discriminator = None

        if utime is not None:
            self.utime = utime
        if attack_pps is not None:
            self.attack_pps = attack_pps
        if normal_pps is not None:
            self.normal_pps = normal_pps

    @property
    def utime(self):
        r"""Gets the utime of this FlowPps.

        数据时间

        :return: The utime of this FlowPps.
        :rtype: int
        """
        return self._utime

    @utime.setter
    def utime(self, utime):
        r"""Sets the utime of this FlowPps.

        数据时间

        :param utime: The utime of this FlowPps.
        :type utime: int
        """
        self._utime = utime

    @property
    def attack_pps(self):
        r"""Gets the attack_pps of this FlowPps.

        攻击包速率

        :return: The attack_pps of this FlowPps.
        :rtype: int
        """
        return self._attack_pps

    @attack_pps.setter
    def attack_pps(self, attack_pps):
        r"""Sets the attack_pps of this FlowPps.

        攻击包速率

        :param attack_pps: The attack_pps of this FlowPps.
        :type attack_pps: int
        """
        self._attack_pps = attack_pps

    @property
    def normal_pps(self):
        r"""Gets the normal_pps of this FlowPps.

        正常包速率

        :return: The normal_pps of this FlowPps.
        :rtype: int
        """
        return self._normal_pps

    @normal_pps.setter
    def normal_pps(self, normal_pps):
        r"""Sets the normal_pps of this FlowPps.

        正常包速率

        :param normal_pps: The normal_pps of this FlowPps.
        :type normal_pps: int
        """
        self._normal_pps = normal_pps

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
        if not isinstance(other, FlowPps):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
