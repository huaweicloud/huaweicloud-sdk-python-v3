# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpenEngressEipReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'bandwidth_size': 'str',
        'bandwidth_charging_mode': 'str'
    }

    attribute_map = {
        'bandwidth_size': 'bandwidth_size',
        'bandwidth_charging_mode': 'bandwidth_charging_mode'
    }

    def __init__(self, bandwidth_size=None, bandwidth_charging_mode=None):
        """OpenEngressEipReq

        The model defined in huaweicloud sdk

        :param bandwidth_size: 出公网带宽  单位：Mbit/s
        :type bandwidth_size: str
        :param bandwidth_charging_mode: 出公网带宽计费类型： - bandwidth：按带宽计费 - traffic：按流量计费
        :type bandwidth_charging_mode: str
        """
        
        

        self._bandwidth_size = None
        self._bandwidth_charging_mode = None
        self.discriminator = None

        if bandwidth_size is not None:
            self.bandwidth_size = bandwidth_size
        if bandwidth_charging_mode is not None:
            self.bandwidth_charging_mode = bandwidth_charging_mode

    @property
    def bandwidth_size(self):
        """Gets the bandwidth_size of this OpenEngressEipReq.

        出公网带宽  单位：Mbit/s

        :return: The bandwidth_size of this OpenEngressEipReq.
        :rtype: str
        """
        return self._bandwidth_size

    @bandwidth_size.setter
    def bandwidth_size(self, bandwidth_size):
        """Sets the bandwidth_size of this OpenEngressEipReq.

        出公网带宽  单位：Mbit/s

        :param bandwidth_size: The bandwidth_size of this OpenEngressEipReq.
        :type bandwidth_size: str
        """
        self._bandwidth_size = bandwidth_size

    @property
    def bandwidth_charging_mode(self):
        """Gets the bandwidth_charging_mode of this OpenEngressEipReq.

        出公网带宽计费类型： - bandwidth：按带宽计费 - traffic：按流量计费

        :return: The bandwidth_charging_mode of this OpenEngressEipReq.
        :rtype: str
        """
        return self._bandwidth_charging_mode

    @bandwidth_charging_mode.setter
    def bandwidth_charging_mode(self, bandwidth_charging_mode):
        """Sets the bandwidth_charging_mode of this OpenEngressEipReq.

        出公网带宽计费类型： - bandwidth：按带宽计费 - traffic：按流量计费

        :param bandwidth_charging_mode: The bandwidth_charging_mode of this OpenEngressEipReq.
        :type bandwidth_charging_mode: str
        """
        self._bandwidth_charging_mode = bandwidth_charging_mode

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
        if not isinstance(other, OpenEngressEipReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
