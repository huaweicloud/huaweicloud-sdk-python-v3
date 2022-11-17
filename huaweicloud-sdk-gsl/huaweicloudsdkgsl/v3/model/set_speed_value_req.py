# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SetSpeedValueReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'speed_value': 'int'
    }

    attribute_map = {
        'speed_value': 'speed_value'
    }

    def __init__(self, speed_value=None):
        """SetSpeedValueReq

        The model defined in huaweicloud sdk

        :param speed_value: 限制带宽速率，单位 Kbps，-1表示不限速,1Mbps&#x3D;1024Kbps。正整数表示限制到当前速率，电信支持限制速率:1Kbps,64 Kbps,256 Kbps,512Kbps,1Mbs，3Mbs,5Mbs,7Mbs,10Mbs,20Mbs,30Mbs,40Mbs,50Mbs,60Mbs,70Mbs,80Mbs,90Mbs,100Mbs,110Mbs,120Mbs,130Mbs,140Mbs,150Mbs。联通支持限制速率:256Kbps,512Kbps,1Mbps,2Mbps,7.25Mbps。
        :type speed_value: int
        """
        
        

        self._speed_value = None
        self.discriminator = None

        self.speed_value = speed_value

    @property
    def speed_value(self):
        """Gets the speed_value of this SetSpeedValueReq.

        限制带宽速率，单位 Kbps，-1表示不限速,1Mbps=1024Kbps。正整数表示限制到当前速率，电信支持限制速率:1Kbps,64 Kbps,256 Kbps,512Kbps,1Mbs，3Mbs,5Mbs,7Mbs,10Mbs,20Mbs,30Mbs,40Mbs,50Mbs,60Mbs,70Mbs,80Mbs,90Mbs,100Mbs,110Mbs,120Mbs,130Mbs,140Mbs,150Mbs。联通支持限制速率:256Kbps,512Kbps,1Mbps,2Mbps,7.25Mbps。

        :return: The speed_value of this SetSpeedValueReq.
        :rtype: int
        """
        return self._speed_value

    @speed_value.setter
    def speed_value(self, speed_value):
        """Sets the speed_value of this SetSpeedValueReq.

        限制带宽速率，单位 Kbps，-1表示不限速,1Mbps=1024Kbps。正整数表示限制到当前速率，电信支持限制速率:1Kbps,64 Kbps,256 Kbps,512Kbps,1Mbs，3Mbs,5Mbs,7Mbs,10Mbs,20Mbs,30Mbs,40Mbs,50Mbs,60Mbs,70Mbs,80Mbs,90Mbs,100Mbs,110Mbs,120Mbs,130Mbs,140Mbs,150Mbs。联通支持限制速率:256Kbps,512Kbps,1Mbps,2Mbps,7.25Mbps。

        :param speed_value: The speed_value of this SetSpeedValueReq.
        :type speed_value: int
        """
        self._speed_value = speed_value

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
        if not isinstance(other, SetSpeedValueReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
