# coding: utf-8

import pprint
import re

import six





class PostPaidServerEip:


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
        'bandwidth': 'PostPaidServerEipBandwidth',
        'extendparam': 'PostPaidServerEipExtendParam'
    }

    attribute_map = {
        'iptype': 'iptype',
        'bandwidth': 'bandwidth',
        'extendparam': 'extendparam'
    }

    def __init__(self, iptype=None, bandwidth=None, extendparam=None):
        """PostPaidServerEip - a model defined in huaweicloud sdk"""
        
        

        self._iptype = None
        self._bandwidth = None
        self._extendparam = None
        self.discriminator = None

        self.iptype = iptype
        self.bandwidth = bandwidth
        if extendparam is not None:
            self.extendparam = extendparam

    @property
    def iptype(self):
        """Gets the iptype of this PostPaidServerEip.

        弹性IP地址类型。

        :return: The iptype of this PostPaidServerEip.
        :rtype: str
        """
        return self._iptype

    @iptype.setter
    def iptype(self, iptype):
        """Sets the iptype of this PostPaidServerEip.

        弹性IP地址类型。

        :param iptype: The iptype of this PostPaidServerEip.
        :type: str
        """
        self._iptype = iptype

    @property
    def bandwidth(self):
        """Gets the bandwidth of this PostPaidServerEip.


        :return: The bandwidth of this PostPaidServerEip.
        :rtype: PostPaidServerEipBandwidth
        """
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, bandwidth):
        """Sets the bandwidth of this PostPaidServerEip.


        :param bandwidth: The bandwidth of this PostPaidServerEip.
        :type: PostPaidServerEipBandwidth
        """
        self._bandwidth = bandwidth

    @property
    def extendparam(self):
        """Gets the extendparam of this PostPaidServerEip.


        :return: The extendparam of this PostPaidServerEip.
        :rtype: PostPaidServerEipExtendParam
        """
        return self._extendparam

    @extendparam.setter
    def extendparam(self, extendparam):
        """Sets the extendparam of this PostPaidServerEip.


        :param extendparam: The extendparam of this PostPaidServerEip.
        :type: PostPaidServerEipExtendParam
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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PostPaidServerEip):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
