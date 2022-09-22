# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PublicIp:

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
        'bandwidth_size': 'int',
        'bandwidth_share_type': 'str'
    }

    attribute_map = {
        'type': 'type',
        'bandwidth_size': 'bandwidth_size',
        'bandwidth_share_type': 'bandwidth_share_type'
    }

    def __init__(self, type=None, bandwidth_size=None, bandwidth_share_type=None):
        """PublicIp

        The model defined in huaweicloud sdk

        :param type: 弹性公网IP类型，默认为5_bgp
        :type type: str
        :param bandwidth_size: 带宽大小，单位：Mbit/s  调整带宽时的最小单位会根据带宽范围不同存在差异。  小于等于300Mbit/s，默认最小单位为1Mbit/s。300Mbit/s~1000Mbit/s，默认最小单位为50Mbit/s。大于1000Mbit/s：默认最小单位为500Mbit/s。 
        :type bandwidth_size: int
        :param bandwidth_share_type: 带宽共享类型
        :type bandwidth_share_type: str
        """
        
        

        self._type = None
        self._bandwidth_size = None
        self._bandwidth_share_type = None
        self.discriminator = None

        self.type = type
        self.bandwidth_size = bandwidth_size
        if bandwidth_share_type is not None:
            self.bandwidth_share_type = bandwidth_share_type

    @property
    def type(self):
        """Gets the type of this PublicIp.

        弹性公网IP类型，默认为5_bgp

        :return: The type of this PublicIp.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PublicIp.

        弹性公网IP类型，默认为5_bgp

        :param type: The type of this PublicIp.
        :type type: str
        """
        self._type = type

    @property
    def bandwidth_size(self):
        """Gets the bandwidth_size of this PublicIp.

        带宽大小，单位：Mbit/s  调整带宽时的最小单位会根据带宽范围不同存在差异。  小于等于300Mbit/s，默认最小单位为1Mbit/s。300Mbit/s~1000Mbit/s，默认最小单位为50Mbit/s。大于1000Mbit/s：默认最小单位为500Mbit/s。 

        :return: The bandwidth_size of this PublicIp.
        :rtype: int
        """
        return self._bandwidth_size

    @bandwidth_size.setter
    def bandwidth_size(self, bandwidth_size):
        """Sets the bandwidth_size of this PublicIp.

        带宽大小，单位：Mbit/s  调整带宽时的最小单位会根据带宽范围不同存在差异。  小于等于300Mbit/s，默认最小单位为1Mbit/s。300Mbit/s~1000Mbit/s，默认最小单位为50Mbit/s。大于1000Mbit/s：默认最小单位为500Mbit/s。 

        :param bandwidth_size: The bandwidth_size of this PublicIp.
        :type bandwidth_size: int
        """
        self._bandwidth_size = bandwidth_size

    @property
    def bandwidth_share_type(self):
        """Gets the bandwidth_share_type of this PublicIp.

        带宽共享类型

        :return: The bandwidth_share_type of this PublicIp.
        :rtype: str
        """
        return self._bandwidth_share_type

    @bandwidth_share_type.setter
    def bandwidth_share_type(self, bandwidth_share_type):
        """Sets the bandwidth_share_type of this PublicIp.

        带宽共享类型

        :param bandwidth_share_type: The bandwidth_share_type of this PublicIp.
        :type bandwidth_share_type: str
        """
        self._bandwidth_share_type = bandwidth_share_type

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
        if not isinstance(other, PublicIp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
