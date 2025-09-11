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
        'bandwidth': 'BandWidth',
        'ipproductid': 'str',
        'iptype': 'str'
    }

    attribute_map = {
        'bandwidth': 'bandwidth',
        'ipproductid': 'ipproductid',
        'iptype': 'iptype'
    }

    def __init__(self, bandwidth=None, ipproductid=None, iptype=None):
        r"""Eip

        The model defined in huaweicloud sdk

        :param bandwidth: 
        :type bandwidth: :class:`huaweicloudsdkdbss.v1.BandWidth`
        :param ipproductid: IP产品ID
        :type ipproductid: str
        :param iptype: EIP类型
        :type iptype: str
        """
        
        

        self._bandwidth = None
        self._ipproductid = None
        self._iptype = None
        self.discriminator = None

        if bandwidth is not None:
            self.bandwidth = bandwidth
        if ipproductid is not None:
            self.ipproductid = ipproductid
        if iptype is not None:
            self.iptype = iptype

    @property
    def bandwidth(self):
        r"""Gets the bandwidth of this Eip.

        :return: The bandwidth of this Eip.
        :rtype: :class:`huaweicloudsdkdbss.v1.BandWidth`
        """
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, bandwidth):
        r"""Sets the bandwidth of this Eip.

        :param bandwidth: The bandwidth of this Eip.
        :type bandwidth: :class:`huaweicloudsdkdbss.v1.BandWidth`
        """
        self._bandwidth = bandwidth

    @property
    def ipproductid(self):
        r"""Gets the ipproductid of this Eip.

        IP产品ID

        :return: The ipproductid of this Eip.
        :rtype: str
        """
        return self._ipproductid

    @ipproductid.setter
    def ipproductid(self, ipproductid):
        r"""Sets the ipproductid of this Eip.

        IP产品ID

        :param ipproductid: The ipproductid of this Eip.
        :type ipproductid: str
        """
        self._ipproductid = ipproductid

    @property
    def iptype(self):
        r"""Gets the iptype of this Eip.

        EIP类型

        :return: The iptype of this Eip.
        :rtype: str
        """
        return self._iptype

    @iptype.setter
    def iptype(self, iptype):
        r"""Sets the iptype of this Eip.

        EIP类型

        :param iptype: The iptype of this Eip.
        :type iptype: str
        """
        self._iptype = iptype

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
