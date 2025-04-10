# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodeEIPSpec:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'iptype': 'str',
        'bandwidth': 'NodeBandwidth'
    }

    attribute_map = {
        'iptype': 'iptype',
        'bandwidth': 'bandwidth'
    }

    def __init__(self, iptype=None, bandwidth=None):
        r"""NodeEIPSpec

        The model defined in huaweicloud sdk

        :param iptype: 弹性IP类型，取值请参见申请EIP接口中publicip.type说明。 [链接请参见[申请EIP](https://support.huaweicloud.com/api-eip/eip_api_0001.html)](tag:hws) [链接请参见[申请EIP](https://support.huaweicloud.com/intl/zh-cn/api-eip/eip_api_0001.html)](tag:hws_hk) 
        :type iptype: str
        :param bandwidth: 
        :type bandwidth: :class:`huaweicloudsdkcce.v3.NodeBandwidth`
        """
        
        

        self._iptype = None
        self._bandwidth = None
        self.discriminator = None

        self.iptype = iptype
        if bandwidth is not None:
            self.bandwidth = bandwidth

    @property
    def iptype(self):
        r"""Gets the iptype of this NodeEIPSpec.

        弹性IP类型，取值请参见申请EIP接口中publicip.type说明。 [链接请参见[申请EIP](https://support.huaweicloud.com/api-eip/eip_api_0001.html)](tag:hws) [链接请参见[申请EIP](https://support.huaweicloud.com/intl/zh-cn/api-eip/eip_api_0001.html)](tag:hws_hk) 

        :return: The iptype of this NodeEIPSpec.
        :rtype: str
        """
        return self._iptype

    @iptype.setter
    def iptype(self, iptype):
        r"""Sets the iptype of this NodeEIPSpec.

        弹性IP类型，取值请参见申请EIP接口中publicip.type说明。 [链接请参见[申请EIP](https://support.huaweicloud.com/api-eip/eip_api_0001.html)](tag:hws) [链接请参见[申请EIP](https://support.huaweicloud.com/intl/zh-cn/api-eip/eip_api_0001.html)](tag:hws_hk) 

        :param iptype: The iptype of this NodeEIPSpec.
        :type iptype: str
        """
        self._iptype = iptype

    @property
    def bandwidth(self):
        r"""Gets the bandwidth of this NodeEIPSpec.

        :return: The bandwidth of this NodeEIPSpec.
        :rtype: :class:`huaweicloudsdkcce.v3.NodeBandwidth`
        """
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, bandwidth):
        r"""Sets the bandwidth of this NodeEIPSpec.

        :param bandwidth: The bandwidth of this NodeEIPSpec.
        :type bandwidth: :class:`huaweicloudsdkcce.v3.NodeBandwidth`
        """
        self._bandwidth = bandwidth

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
        if not isinstance(other, NodeEIPSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
