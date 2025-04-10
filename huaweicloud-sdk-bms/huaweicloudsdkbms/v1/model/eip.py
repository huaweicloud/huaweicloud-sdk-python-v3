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
        'iptype': 'str',
        'bandwidth': 'BandWidth',
        'extendparam': 'ExtendParamEip'
    }

    attribute_map = {
        'iptype': 'iptype',
        'bandwidth': 'bandwidth',
        'extendparam': 'extendparam'
    }

    def __init__(self, iptype=None, bandwidth=None, extendparam=None):
        r"""Eip

        The model defined in huaweicloud sdk

        :param iptype: 弹性公网IP地址类型。类型枚举值：5_bgp、5_sbgp详情请参见《虚拟私有云API参考》申请弹性公网IP章节的publicip字段说明。
        :type iptype: str
        :param bandwidth: 
        :type bandwidth: :class:`huaweicloudsdkbms.v1.BandWidth`
        :param extendparam: 
        :type extendparam: :class:`huaweicloudsdkbms.v1.ExtendParamEip`
        """
        
        

        self._iptype = None
        self._bandwidth = None
        self._extendparam = None
        self.discriminator = None

        self.iptype = iptype
        self.bandwidth = bandwidth
        self.extendparam = extendparam

    @property
    def iptype(self):
        r"""Gets the iptype of this Eip.

        弹性公网IP地址类型。类型枚举值：5_bgp、5_sbgp详情请参见《虚拟私有云API参考》申请弹性公网IP章节的publicip字段说明。

        :return: The iptype of this Eip.
        :rtype: str
        """
        return self._iptype

    @iptype.setter
    def iptype(self, iptype):
        r"""Sets the iptype of this Eip.

        弹性公网IP地址类型。类型枚举值：5_bgp、5_sbgp详情请参见《虚拟私有云API参考》申请弹性公网IP章节的publicip字段说明。

        :param iptype: The iptype of this Eip.
        :type iptype: str
        """
        self._iptype = iptype

    @property
    def bandwidth(self):
        r"""Gets the bandwidth of this Eip.

        :return: The bandwidth of this Eip.
        :rtype: :class:`huaweicloudsdkbms.v1.BandWidth`
        """
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, bandwidth):
        r"""Sets the bandwidth of this Eip.

        :param bandwidth: The bandwidth of this Eip.
        :type bandwidth: :class:`huaweicloudsdkbms.v1.BandWidth`
        """
        self._bandwidth = bandwidth

    @property
    def extendparam(self):
        r"""Gets the extendparam of this Eip.

        :return: The extendparam of this Eip.
        :rtype: :class:`huaweicloudsdkbms.v1.ExtendParamEip`
        """
        return self._extendparam

    @extendparam.setter
    def extendparam(self, extendparam):
        r"""Sets the extendparam of this Eip.

        :param extendparam: The extendparam of this Eip.
        :type extendparam: :class:`huaweicloudsdkbms.v1.ExtendParamEip`
        """
        self._extendparam = extendparam

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
