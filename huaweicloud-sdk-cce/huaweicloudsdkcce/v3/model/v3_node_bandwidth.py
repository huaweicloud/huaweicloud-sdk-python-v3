# coding: utf-8

import pprint
import re

import six





class V3NodeBandwidth:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'chargemode': 'str',
        'sharetype': 'str',
        'size': 'str'
    }

    attribute_map = {
        'chargemode': 'chargemode',
        'sharetype': 'sharetype',
        'size': 'size'
    }

    def __init__(self, chargemode=None, sharetype=None, size=None):
        """V3NodeBandwidth - a model defined in huaweicloud sdk"""
        
        

        self._chargemode = None
        self._sharetype = None
        self._size = None
        self.discriminator = None

        if chargemode is not None:
            self.chargemode = chargemode
        if sharetype is not None:
            self.sharetype = sharetype
        if size is not None:
            self.size = size

    @property
    def chargemode(self):
        """Gets the chargemode of this V3NodeBandwidth.

          带宽的计费类型：  - 未传该字段，表示按带宽计费。 - 字段值为空，表示按带宽计费。 - 字段值为“traffic”，表示按流量计费。 - 字段为其它值，会导致创建云服务器失败。  > -  按带宽计费：按公网传输速率（单位为Mbps）计费。当您的带宽利用率高于10%时，建议优先选择按带宽计费。 > -  按流量计费：按公网传输的数据总量（单位为GB）计费。当您的带宽利用率低于10%时，建议优先选择按流量计费。

        :return: The chargemode of this V3NodeBandwidth.
        :rtype: str
        """
        return self._chargemode

    @chargemode.setter
    def chargemode(self, chargemode):
        """Sets the chargemode of this V3NodeBandwidth.

          带宽的计费类型：  - 未传该字段，表示按带宽计费。 - 字段值为空，表示按带宽计费。 - 字段值为“traffic”，表示按流量计费。 - 字段为其它值，会导致创建云服务器失败。  > -  按带宽计费：按公网传输速率（单位为Mbps）计费。当您的带宽利用率高于10%时，建议优先选择按带宽计费。 > -  按流量计费：按公网传输的数据总量（单位为GB）计费。当您的带宽利用率低于10%时，建议优先选择按流量计费。

        :param chargemode: The chargemode of this V3NodeBandwidth.
        :type: str
        """
        self._chargemode = chargemode

    @property
    def sharetype(self):
        """Gets the sharetype of this V3NodeBandwidth.

        带宽的共享类型，取值请参见“[创建云服务器](https://support.huaweicloud.com/api-ecs/zh-cn_topic_0167957246.html) > bandwidth字段数据结构说明”表中“sharetype”参数的描述。

        :return: The sharetype of this V3NodeBandwidth.
        :rtype: str
        """
        return self._sharetype

    @sharetype.setter
    def sharetype(self, sharetype):
        """Sets the sharetype of this V3NodeBandwidth.

        带宽的共享类型，取值请参见“[创建云服务器](https://support.huaweicloud.com/api-ecs/zh-cn_topic_0167957246.html) > bandwidth字段数据结构说明”表中“sharetype”参数的描述。

        :param sharetype: The sharetype of this V3NodeBandwidth.
        :type: str
        """
        self._sharetype = sharetype

    @property
    def size(self):
        """Gets the size of this V3NodeBandwidth.

        带宽大小，取值请参见“[创建云服务器](https://support.huaweicloud.com/api-ecs/zh-cn_topic_0167957246.html) > bandwidth字段数据结构说明”表中“size”参数的描述。

        :return: The size of this V3NodeBandwidth.
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this V3NodeBandwidth.

        带宽大小，取值请参见“[创建云服务器](https://support.huaweicloud.com/api-ecs/zh-cn_topic_0167957246.html) > bandwidth字段数据结构说明”表中“size”参数的描述。

        :param size: The size of this V3NodeBandwidth.
        :type: str
        """
        self._size = size

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
        if not isinstance(other, V3NodeBandwidth):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
