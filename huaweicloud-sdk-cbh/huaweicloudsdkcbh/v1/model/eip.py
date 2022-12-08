# coding: utf-8

import re
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
        'ip_type': 'str',
        'ip_product_id': 'str',
        'bandwidth': 'BandWidth'
    }

    attribute_map = {
        'ip_type': 'ip_type',
        'ip_product_id': 'ip_product_id',
        'bandwidth': 'bandwidth'
    }

    def __init__(self, ip_type=None, ip_product_id=None, bandwidth=None):
        """Eip

        The model defined in huaweicloud sdk

        :param ip_type: eip的类型
        :type ip_type: str
        :param ip_product_id: IP地址对应产品ID
        :type ip_product_id: str
        :param bandwidth: 
        :type bandwidth: :class:`huaweicloudsdkcbh.v1.BandWidth`
        """
        
        

        self._ip_type = None
        self._ip_product_id = None
        self._bandwidth = None
        self.discriminator = None

        self.ip_type = ip_type
        self.ip_product_id = ip_product_id
        self.bandwidth = bandwidth

    @property
    def ip_type(self):
        """Gets the ip_type of this Eip.

        eip的类型

        :return: The ip_type of this Eip.
        :rtype: str
        """
        return self._ip_type

    @ip_type.setter
    def ip_type(self, ip_type):
        """Sets the ip_type of this Eip.

        eip的类型

        :param ip_type: The ip_type of this Eip.
        :type ip_type: str
        """
        self._ip_type = ip_type

    @property
    def ip_product_id(self):
        """Gets the ip_product_id of this Eip.

        IP地址对应产品ID

        :return: The ip_product_id of this Eip.
        :rtype: str
        """
        return self._ip_product_id

    @ip_product_id.setter
    def ip_product_id(self, ip_product_id):
        """Sets the ip_product_id of this Eip.

        IP地址对应产品ID

        :param ip_product_id: The ip_product_id of this Eip.
        :type ip_product_id: str
        """
        self._ip_product_id = ip_product_id

    @property
    def bandwidth(self):
        """Gets the bandwidth of this Eip.

        :return: The bandwidth of this Eip.
        :rtype: :class:`huaweicloudsdkcbh.v1.BandWidth`
        """
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, bandwidth):
        """Sets the bandwidth of this Eip.

        :param bandwidth: The bandwidth of this Eip.
        :type bandwidth: :class:`huaweicloudsdkcbh.v1.BandWidth`
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
        if not isinstance(other, Eip):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
