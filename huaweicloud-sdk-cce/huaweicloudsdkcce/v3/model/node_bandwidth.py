# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodeBandwidth:

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
        'size': 'int',
        'sharetype': 'str'
    }

    attribute_map = {
        'chargemode': 'chargemode',
        'size': 'size',
        'sharetype': 'sharetype'
    }

    def __init__(self, chargemode=None, size=None, sharetype=None):
        """NodeBandwidth

        The model defined in huaweicloud sdk

        :param chargemode: 带宽的计费类型： - 未传该字段，表示按带宽计费。 - 字段值为空，表示按带宽计费。 - 字段值为“traffic”，表示按流量计费。 - 字段为其它值，会导致创建云服务器失败。 &gt; - 按带宽计费：按公网传输速率（单位为Mbps）计费。当您的带宽利用率高于10%时，建议优先选择按带宽计费。 &gt; - 按流量计费：只允许在创建按需节点时指定，按公网传输的数据总量（单位为GB）计费。当您的带宽利用率低于10%时，建议优先选择按流量计费。 
        :type chargemode: str
        :param size: 带宽大小，取值请参见取值请参见申请EIP接口中bandwidth.size说明。 [链接请参见[申请EIP](https://support.huaweicloud.com/api-eip/eip_api_0001.html)](tag:hws) [链接请参见[申请EIP](https://support.huaweicloud.com/intl/zh-cn/api-eip/eip_api_0001.html)](tag:hws_hk) 
        :type size: int
        :param sharetype: 带宽的共享类型，共享类型枚举：PER，表示独享。WHOLE，表示共享。
        :type sharetype: str
        """
        
        

        self._chargemode = None
        self._size = None
        self._sharetype = None
        self.discriminator = None

        if chargemode is not None:
            self.chargemode = chargemode
        if size is not None:
            self.size = size
        if sharetype is not None:
            self.sharetype = sharetype

    @property
    def chargemode(self):
        """Gets the chargemode of this NodeBandwidth.

        带宽的计费类型： - 未传该字段，表示按带宽计费。 - 字段值为空，表示按带宽计费。 - 字段值为“traffic”，表示按流量计费。 - 字段为其它值，会导致创建云服务器失败。 > - 按带宽计费：按公网传输速率（单位为Mbps）计费。当您的带宽利用率高于10%时，建议优先选择按带宽计费。 > - 按流量计费：只允许在创建按需节点时指定，按公网传输的数据总量（单位为GB）计费。当您的带宽利用率低于10%时，建议优先选择按流量计费。 

        :return: The chargemode of this NodeBandwidth.
        :rtype: str
        """
        return self._chargemode

    @chargemode.setter
    def chargemode(self, chargemode):
        """Sets the chargemode of this NodeBandwidth.

        带宽的计费类型： - 未传该字段，表示按带宽计费。 - 字段值为空，表示按带宽计费。 - 字段值为“traffic”，表示按流量计费。 - 字段为其它值，会导致创建云服务器失败。 > - 按带宽计费：按公网传输速率（单位为Mbps）计费。当您的带宽利用率高于10%时，建议优先选择按带宽计费。 > - 按流量计费：只允许在创建按需节点时指定，按公网传输的数据总量（单位为GB）计费。当您的带宽利用率低于10%时，建议优先选择按流量计费。 

        :param chargemode: The chargemode of this NodeBandwidth.
        :type chargemode: str
        """
        self._chargemode = chargemode

    @property
    def size(self):
        """Gets the size of this NodeBandwidth.

        带宽大小，取值请参见取值请参见申请EIP接口中bandwidth.size说明。 [链接请参见[申请EIP](https://support.huaweicloud.com/api-eip/eip_api_0001.html)](tag:hws) [链接请参见[申请EIP](https://support.huaweicloud.com/intl/zh-cn/api-eip/eip_api_0001.html)](tag:hws_hk) 

        :return: The size of this NodeBandwidth.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this NodeBandwidth.

        带宽大小，取值请参见取值请参见申请EIP接口中bandwidth.size说明。 [链接请参见[申请EIP](https://support.huaweicloud.com/api-eip/eip_api_0001.html)](tag:hws) [链接请参见[申请EIP](https://support.huaweicloud.com/intl/zh-cn/api-eip/eip_api_0001.html)](tag:hws_hk) 

        :param size: The size of this NodeBandwidth.
        :type size: int
        """
        self._size = size

    @property
    def sharetype(self):
        """Gets the sharetype of this NodeBandwidth.

        带宽的共享类型，共享类型枚举：PER，表示独享。WHOLE，表示共享。

        :return: The sharetype of this NodeBandwidth.
        :rtype: str
        """
        return self._sharetype

    @sharetype.setter
    def sharetype(self, sharetype):
        """Sets the sharetype of this NodeBandwidth.

        带宽的共享类型，共享类型枚举：PER，表示独享。WHOLE，表示共享。

        :param sharetype: The sharetype of this NodeBandwidth.
        :type sharetype: str
        """
        self._sharetype = sharetype

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
        if not isinstance(other, NodeBandwidth):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
